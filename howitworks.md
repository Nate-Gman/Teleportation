# How It Works -- Warpdrive WD-1m5 Foldrunner "Miniframe V"

A logical, step-by-step explanation of how the warp drive model works, from the physics to the engineering to the barriers. This document explains the *logic* -- for the formulas and proofs, see `README.md`. For the high-level summary and the full five-pass scale-down rationale, see `overview.md`.

This revision covers the fifth refit pass, WD-1m5. Passes 1 and 2 scaled the hull to 0.65x then a further 0.83x linear (crew 12 -> 8 -> 6), and pass 2 thinned the bubble wall from 1.0 m to 0.2 m to buy back usable interior volume. Pass 3 fixed a real bug instead of adding a new lever: two axial mount offsets (the boost rectenna and SMES positions) had been hardcoded literals that never scaled down in either earlier pass, so the fit check had quietly been validating against the wrong (too-large) footprint. Once those became proper, scaling `DIMS` entries, the ship could shrink a further 0.85x linear (overall `SCALE_S = 0.4586`) with radiators scaled independently to hold the thermal-barrier invariant. Pass 4 revisited two inherited engineering margins (reactor reserve 1.5x -> 1.35x, hull wall re-derived from pressure-vessel theory). Pass 5 revisited two inherited mass-model constants (HTS coil winding build 0.35 -> 0.30 m from improved REBCO J_e, shaping-ring solid fraction 0.35 -> 0.30 for secondary structure). Reactor/radiator/coil power are re-derived from physical scaling laws rather than hand-typed throughout. The physics and the barrier verdicts are unchanged (the thermal barrier is deliberately kept failing at 2c by `--selftest`); the numbers below are the current ship's.

---

## 1. The core idea: carry spacetime, don't push through it

A conventional rocket accelerates by throwing mass backward. The faster it goes, the more energy it needs -- and that energy has to be carried aboard, which makes the ship heavier, which needs more energy. This is the rocket equation, and it is brutal: to reach even 0.1c, a chemical rocket would need more fuel than there is mass in the galaxy.

The Alcubierre warp drive (1994) takes a different approach. Instead of moving through spacetime, it *carries* a bubble of flat spacetime with the ship. The space in front of the bubble contracts; the space behind it expands. The ship rides the wave like a surfer -- it never moves relative to the space inside the bubble, so it never experiences acceleration, time dilation, or relativistic mass increase.

**The key insight:** the crew are weightless and un-dilated for the entire voyage. They arrive at the destination having aged exactly as much as the people who stayed home. This is not a defect -- it is the only version of interstellar travel that is useful to a civilization.

---

## 2. The warp bubble: how spacetime bends

### The shape function

The bubble is defined by a shape function f(r) that goes from 1 (inside) to 0 (outside):

```
f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / [2 tanh(sigma R)]
```

- At the center (r=0): f = 1 (flat spacetime, the ship is here)
- At the wall (r=R): f = 1/2 (the transition zone)
- Far outside (r >> R): f = 0 (normal spacetime)

The wall thickness delta controls how sharp the transition is. sigma = 1/delta. A thinner wall means a sharper transition -- and a vastly higher energy bill.

### The shift vector

The Alcubierre metric uses a shift vector that pushes the bubble forward:

```
ds^2 = -c^2 dt^2 + (dx - v_s f(r) dt)^2 + dy^2 + dz^2
```

The ship sits at r=0 where f=1, so the shift vector carries it at velocity v_s. The crew feel nothing because the metric inside is flat Minkowski space.

### The energy density

The stress-energy that sources this metric has a negative energy density:

```
T^00 = -(c^4 / 8 pi G) x (beta^2 rho^2 / 4 r^2) x (df/dr)^2
```

This is **negative** -- it requires exotic matter. That is the first and most famous barrier.

---

## 3. The hardware: what the ship actually looks like

### The warp ring (the drive)

The ship has a 91.7 m diameter toroidal ring centered on the bubble wall (was 200 m at full scale, 130 / 107.9 m after passes 1/2). The ring is not a solid tube -- it is a thin shell (0.27 m wall, was 0.6 m at full scale) of conditioned SiC/W metamaterial, divided into 24 independently driven sectors. The ring's stress-energy is what sources the shift vector. It sits *at* the bubble radius because that is where the curvature is.

### The field coils (the actuators)

24 superconducting REBCO coils (one per ring sector) shape the field. Each coil has 48,000 turns carrying 38,000 A at 18 K -- the same HTS technology as the full-scale ship, just wound onto a smaller 2.84 m bore (was 6.2 m at full scale). The coils are the actuators that reshape the bubble wall -- they are the "steering wheel."

### The crew hull (the payload)

Inside the bubble, the crew live in a 31.2 m x 8.0 m hull with 3 decks (was 68 m x 16 m x 4 decks at full scale). The hull is ordinary aerospace engineering -- Al-Li/composite pressure hull, 6 crew (was 12 at full scale, 8 after pass 1), life support. The hull diameter (8.0 m) has been held constant since pass 2, above the pure linear-scale value, as a practical minimum cabin width for 6 crew plus a corridor. The hull sits in flat spacetime, so it does not need to survive acceleration or tidal forces. The only structural loads are from docking and the magsail deployment.

### The fusion reactor (the housekeeping plant)

A 2.62 GW D-3He spherical tokamak provides housekeeping power (was 22 GW at full scale, 7 / 4.35 / 2.91 GW after passes 1/2/3). It runs the coils, the cryoplant, and life support. It does NOT move the ship -- the energy to reach cruise speed comes from outside (the stellar tap). D-3He is chosen because it is aneutronic: the reaction D + 3He -> 4He + p produces no neutrons, so 62% of the energy can be direct-converted to electricity without a thermal cycle. The reactor is now 88% smaller than the full-scale plant because the loads it covers (coil AC ripple, cryo, shell-servo control) scale down with the smaller ring and coil volumes -- it carries a 1.35x margin over the beta=0.99 cruise load (down from the ~1.5x inherited from WD-1, re-examined in pass 4).

### The radiators (the thermal limit)

20 radiator panels, each 22.61 m x 7.83 m (both faces), total 7,081 m^2 (was 52 m x 18 m / 37,440 m^2 at full scale, 15,818 / 10,895 m^2 after passes 1/2). They radiate waste heat at 1550 K design temperature, with a 1900 K graphite sublimation limit. The thermal balance is:

```
T = (P_waste / (epsilon x sigma_SB x A))^(1/4)
```

At beta=0.99 the radiators run at 1514 K -- within limits, and cooler than the full-scale ship's 1649 K. At beta=2 they run at 1904 K -- the ship still cooks, but the barrier now only trips above beta ~ 1.99 (was ~1.45 at full scale, ~1.79 / ~1.97 after passes 1/2). This is because waste heat keeps falling faster than radiator area as the ship shrinks, so a smaller ship of the same design is intrinsically cooler at any given speed. This is the only barrier that is *passable* -- and it now only needs 0.9% more radiator area, versus 80% at full scale. `--selftest` deliberately hard-asserts that T(2c) still exceeds 1900 K: the redesign is meant to shrink the margin needed to fix this barrier, not to quietly make it disappear. This margin is now thin enough that it is effectively the practical stopping point for further pure shrinkage of the radiators relative to the rest of the hull.

### The Casimir lattice (the exotic-energy attempt)

24 cassettes of Casimir plates in the ring wall, each with about 15 million plate pairs at 10 nm gap (the gap itself is nanoscale and untouched by the ship's resize). The Casimir effect produces real negative energy density:

```
rho = -pi^2 hbar c / (720 a^4)
```

The total onboard negative energy is -0.19 MJ (was -2 MJ at full scale, -0.55 / -0.31 MJ after passes 1/2). The (45.86 m, 0.2 m-wall) warp bubble would demand -3.54 x 10^46 J if flown in superluminal Alcubierre mode -- which this ship never does. That is smaller than pass 2's -4.89 x 10^46 J, because the bubble shrank further this pass while the wall thickness held steady at 0.2 m. The gap is still ~41 orders of magnitude: no combination of the scale and wall-thickness knobs closes it, because the onboard Casimir supply is never within tens of orders of what any of these bubble configurations demand. This is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

### A bug fix, not a new lever: the mount-offset scaling error

Two components in `_envelope_points()` -- the boost rectenna and the SMES buffer -- had their positions along the ship's spine written as bare numeric literals (`40.0` and `22.0` metres) instead of `DIMS` entries, dating from before either of the first two refit passes existed. Every other axial offset in the model (`cap_offset_m`, `rad_z0_m`, and so on) scaled down correctly each pass; these two silently did not. The bug never tripped a self-test because some *other* part of the ship was always the binding envelope constraint -- until pass 2 shrank the ship enough that it started to matter. Fixing it (`collector_z0_m`, `smes_z0_m`, both now `SCALE_S`-scaled `DIMS` entries) did not change any physics; it corrected a check that had been silently passing for the wrong reason, and in doing so revealed that the ship actually had more genuine room to shrink than the buggy check had reported.

---

## 4. The voyage: how the trip works

### Phase 1: Boost (the stellar tap)

The ship starts at rest near Earth. A 1000 km phased array in the solar system (unchanged, external infrastructure) beams 10^17 W (0.026% of the sun's luminosity) at the ship's 4 km deployed rectenna. The beam is diffraction-limited:

```
d_spot = 2.44 x lambda x L / D
```

At 0.1 ly the spot is 2.3 km -- smaller than the rectenna, so capture is 100%. At 0.5 ly the spot is 11.5 km -- the 4 km rectenna captures only 12%. The beam range is 0.62 ly.

The ship accelerates by absorbing beam energy. The kinetic energy needed is:

```
KE = (gamma - 1) M c^2
```

At beta=0.5 this is 2.33 x 10^23 J (0.23 YJ) -- was 1.77 YJ for the full-scale ship, because the resized hull has 87% less mass to push. The boost to the new maximum speed, beta=0.857 (was 0.562 at full scale, 0.727 / 0.794 / 0.844 / 0.845 after passes 1/2/3/4), takes 300 days. This is *emergent*, not declared -- the same beam array now pushes the lighter ship further before it outruns the diffraction-limited spot.

#### How the cruise speed emerges (the two-clock race)

The speed beta=0.857 is not a parameter anywhere in the model. It falls out of a race between two clocks, and every step is derived from first principles. The full proofs are in info section **19k** (7 verified proof blocks, 7 self-test checks).

**The energy clock:** KE = (gamma - 1) M c^2. The gamma curve diverges at beta=1, so each knot closer to lightspeed costs more than the last:

| beta | gamma | KE | vs beta=0.857 |
|------|-------|----|----------------|
| 0.857 | 1.94 | 1.40 YJ | -- |
| 0.9 | 2.29 | 1.93 YJ | +38% for +4% speed |
| 0.95 | 3.20 | 3.29 YJ | +135% for +9% speed |
| 0.99 | 7.09 | 9.09 YJ | +550% for +13% speed |
| 0.999 | 22.4 | 33.5 YJ | +2300% for +14% speed |
| 1.0 | inf | inf | wall |

**The range clock:** d_spot = 2.44 lambda L / D (Airy diffraction). The 1000 km aperture at 1.0 um produces a spot that grows linearly with distance. The 4 km rectenna captures 100% at 0.1 ly, 12% at 0.5 ly, 7.8% at 0.62 ly. Capture falls as 1/L^2. Past 0.62 ly the beam is too weak to matter.

**The race:** The boost integrates in 3-day steps, tracking position, velocity and delivered energy simultaneously. The ship starts at rest with 100% capture, then capture falls as it pulls away. After 300 days the energy clock and range clock converge: the ship has 1.398 YJ and needs 1.400 YJ. At beta=0.86 it would need 1.43 YJ -- 2% short. That 2% margin is why the cruise speed is 0.857 and not 0.86.

**Why shrinking raises the speed:** The beam is fixed external infrastructure. The ship mass M fell 87% across five refit passes (127,000 t -> 16,602 t). Since KE = (gamma-1)Mc^2, a lighter ship needs less energy for the same beta, so it climbs higher on the gamma curve before outrunning the beam. Speed rose 52% (0.562 -> 0.857); gamma rose 60% (1.21 -> 1.94). The relationship is superlinear -- each tonne saved is worth more than the last, because the gamma curve is steeper at higher beta.

**Why it cannot reach beta=1:** At beta=1, gamma = infinity and KE = infinity. No finite beam can deliver infinite energy. This is special relativity, not engineering. Three levers could raise the speed further (larger aperture, shorter wavelength, lighter ship), but none touch the gamma wall. The beam can push the ship arbitrarily close to c, but never to c.

### Phase 2: Cruise (free flight)

At cruise the bubble is a stationary spacetime solution. The coils need power to hold their shape (598 MW at beta=1, scaling as beta^2 -- was 6.2 GW at full scale), but no energy goes into *changing* the ship's velocity. The cruise is free in the GR sense -- the cost is engineering imperfection (coil ripple, control, refrigeration), and that cost fell along with the hardware.

Door to door (boost + cruise + photon brake, assuming a destination array), the trip now takes about 6.0 years -- was ~8.5 years at full scale, ~7.0 / ~6.5 years after passes 1/2. The crew age the same as Earth ages -- there is no time-dilation dividend, because the warp interior is flat, so the crew clock runs at the same rate as the Earth clock. A relativistic rocket at the same speed would age less (about 2.7 years for the one-way trip) -- but the warp crew arrive in sync with home, which is the point.

### Phase 3: Brake (stopping)

This is the hardest engineering problem. The ship is moving at beta=0.857 and needs to stop. Three options:

**Option A: Magsail (always available, very slow)**

A 700 km superconducting loop (was 1000 km at full scale; unchanged since pass 2) drags against the interstellar medium. The drag force is:

```
F = Cd x rho_ISM x v^2 x A
```

At beta=0.5 this is 4.9 x 10^6 N. The halving time is 16 years. The full stop time is about 8,000 years (was 30,000 at full scale, ~20,600 / ~13,000 / ~8,860 after passes 1/2/4). The drag falls as v^2, so the brake fades exactly when you need it most. This is the honest number -- the magsail alone cannot stop the ship in useful time, though the lighter hull keeps stopping faster with the SAME magsail hardware as pass 2 -- no further magsail changes were needed to see this gain.

**Option B: Photon brake (requires destination infrastructure)**

If a receiver array is already in place at Proxima, it can beam power at the ship. The photon pressure decelerates the ship:

```
F = 2P / c
t = gamma M v / F
```

At beta=0.5 with a 0.02 ly approach: F = 6.67 x 10^8 N (unchanged -- set by the beam, not the ship), brake time = 50 days (was 381 days at full scale, 128 / 81 / 55 / 55 days after passes 1/2/3/4). This is the only way to stop in useful time -- but it requires someone to have already built the array at the destination.

**Option C: Both**

The real plan is to use the magsail for the initial deceleration and the photon brake for the final approach.

### Phase 4: Arrival

At Proxima Centauri b, the ship drops the bubble. The accumulated ISM particles (2.65 x 10^25 protons, was 1.26 x 10^26 at full scale -- the 45.86 m bubble sweeps a smaller cross-section) are released forward as a blast of about 0.50 PJ (was 2.37 PJ at full scale) -- roughly 120 kilotons of TNT. This is a hazard for anything ahead of the ship, but it is a *floor* -- the true spectrum is worse.

The crew arrive having aged about 6.0 years plus roughly 1.6 seconds of gravitational drift (from climbing out of Sol's well and descending into Proxima's, over a shorter crossing than the full-scale ship's 8.49 years). The ship's own gravity contributes about -3.0 x 10^-22 -- twelve orders of magnitude below the best clock ever built, and weaker still than the full-scale ship's -9.43 x 10^-22.

---

## 5. The portal: wormhole construction

### Morris-Thorne wormhole

The model also computes a traversable wormhole. The Morris-Thorne metric is:

```
ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2
```

The shape function b(r) = b0^2/r satisfies the flare-out condition b'(r0) = -1 < 1, which means the throat opens out rather than pinching shut.

### The barriers to a wormhole

1. **Tidal forces:** At a 12 m throat, a 2 m person experiences 1.27 x 10^14 g -- lethal. The survivable throat is 1.35 x 10^8 m (10.6 Earth diameters across).

2. **Exotic energy:** The throat requires -c^4 b0 / (6G) of negative energy. At 12 m: -2.42 x 10^44 J. At the survivable size: -2.73 x 10^51 J.

3. **Quantum inequalities:** The Ford-Roman bound limits how long negative energy can persist. A 12 m throat can stay open for 3.25 x 10^-26 s. Traversal takes 4.8 s. The throat closes 10^26 times before you are halfway through.

### Four constructions, one answer

The model computes four wormhole constructions:
- **Morris-Thorne:** needs -2.42 x 10^44 J of exotic energy (38 orders beyond Casimir)
- **Visser thin-shell:** needs -2.90 x 10^45 J (concentrating costs MORE, not less)
- **MMP (2020):** needs a 45,834 solar mass magnetically charged black hole -- but no magnetic monopole has ever been observed
- **Survivable throat:** needs -2.73 x 10^51 J (45 orders beyond Casimir)

All four are blocked. The verdict is the same regardless of construction.

---

## 6. The time machine: CTCs from wormholes

### How a wormhole becomes a time machine

If the two mouths of a wormhole sit at different gravitational potentials or move at different speeds, their clocks desynchronize:

```
dtau/dt = sqrt(1 + 2 Phi / c^2) x 1/gamma(beta)
```

After time t, the offset is:

```
delta_t = t x (rate_A - rate_B)
```

When |delta_t| >= D/c (the light-time between the mouths), the wormhole becomes a time machine: you can step through and arrive before you left. This is a closed timelike curve (CTC).

### Chronology protection

Hawking's chronology protection conjecture (1992) expects that the vacuum fluctuations diverge at the chronology horizon, destroying the throat before the CTC forms. This is a conjecture, not a theorem -- but it is strongly expected by the majority of the field.

The model computes the CTC onset time:

```
t_onset = (D/c) / |rate_A - rate_B|
```

For a 0.1 rate difference at Proxima distance: 42.5 years. After that, the wormhole is a time machine -- and chronology protection is expected to destroy it.

### Maximum time travel (scenarios 7-9 in `--send`)

The desynchronization can be pushed to physical limits by combining the deepest realistic gravity well (neutron-star surface, Phi/c^2 = -0.3) with the highest realistic velocity (beta = 0.99 on a rocket) and the smallest practical mouth separation (1 AU -- same solar system):

- **Maximum rate difference**: 0.911 (mouth B ages at 8.9% the rate of mouth A)
- **Minimum CTC onset**: 9.1 minutes at 1 AU separation (vs 18.8 years at Proxima distance with a moderate well)
- **Maximum backward jump**: 91 years after 100 years of desynchronization (step A->B)
- **Maximum forward jump**: 91 years, same offset (step B->A -- the wormhole is symmetric)
- **Extreme ceiling**: 98.6 years (near-horizon + 0.999c, 100 yr elapsed)

Both directions use the same offset -- the wormhole doesn't care which way you step. The maximum jump approaches (but cannot exceed) the elapsed time, because the rate difference approaches (but cannot reach) 1.0.

The warp drive itself produces almost no time shift: +1.54 s gravitational drift over the 4.96 yr crossing (not controllable -- set by the Sol-Proxima gravitational potential difference), 0.0 s kinematic dilation (flat interior), and 0.0 desynchronization (a warp-carried mouth ages at the same rate as one at rest). The fast thing cannot build the causality violation; the slow rocket can.

**All scenarios remain blocked** by exotic energy (46 orders short), quantum inequalities (throat closes in ~10^-22 s vs ~10^7 s traversal), or chronology protection. The maximum time jump is a mathematical result, not an engineering capability. The full proofs are in info section **19j** in the viewer (press I), with 7 verified proof blocks covering combined clock rates, CTC onset, maximum backward/forward jumps, the warp-drive flat-interior theorem, gravitational drift, and the barrier analysis.

---

## 7. The honesty layer: why the model says "no"

### Conservation audit

The model runs 12 conservation checks against the live state:

1. **No over-unity:** kinetic energy gained <= beam energy delivered + regen
2. **Recovery bounded:** regen <= kinetic energy (cannot recover more than you have)
3. **Plant within rating:** housekeeping power <= reactor thermal output
4. **Fuel backs output:** fuel mass x specific energy >= energy produced
5. **Exotic never supplied:** the model never pretends negative energy is available
6. **Radiates only outward:** waste heat <= electrical load / efficiency
7. **NEC reported truthfully:** superluminal solutions are flagged as exotic
8. **No velocity dilation dividend:** warp crew age = Earth age (no free time dilation)
9. **Gravitational drift modelled:** the only clock difference is environmental
10. **Beam capture <= 1.0:** cannot capture more than 100% of the beam
11. **All masses positive:** no component has negative mass
12. **Arrival requires stopping:** you cannot arrive without decelerating

**Verdict: HONEST -- nothing created from nothing.**

### The barrier scorecard

8 barriers block the drive:

| Barrier | Status | Why |
|---------|--------|-----|
| Wall tidal gradient | FAIL | 1.76e17 g vs 1 g limit; thinner wall = worse (was 7e15 g before the wall was thinned in pass 2) |
| Superluminal NEC | THEOREM | SSV 2022: any v > c warp violates NEC |
| Negative energy scale | FAIL | 41 orders short of Casimir |
| Steering above beta=1 | THEOREM | causal disconnection (Everett/Coule/Krasnikov) |
| Thermal survival | FAIL | 1904 K vs 1900 K at 2c (passable with more radiators; was 2187 K at full scale) |
| Ford-Roman wall | THEOREM | QI limits wall to 100 L_Planck |
| QI throat hold time | THEOREM | throat closes 10^26x before crossing |
| CTC chronology | CONJECTURE | Hawking 1992: divergent vacuum at horizon |

**Score: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable** (except thermal at subluminal speeds).

---

## 8. What the model actually proves

The model does NOT prove that warp drive is possible. It proves the opposite -- that warp drive as drawn cannot fly. But it does so with full mathematical rigor, showing exactly where the barriers are, how large they are, and what kind of physics would be needed to get past them.

What IS possible:
- **Subluminal warp** (beta < 1) with positive energy (Bobrick-Martire 2021, Fuchs et al. 2024)
- **Beam-powered acceleration** to beta ~ 0.857 for this resized hull (emergent, not declared; was ~0.562 at full scale, ~0.727 / ~0.794 / ~0.844 / ~0.845 after passes 1/2/3/4)
- **Magsail deceleration** (very slow, ~8,000 yr full stop at this scale, was ~30,000 yr at full scale)
- **Photon braking** (requires destination infrastructure)
- **Crew survival** (flat interior, no tidal forces, no time dilation)
- **A smaller, lighter, lower-power hull that flies faster on the same external infrastructure** -- the one genuine engineering lever this model exposes: shrink the ship (and thin its bubble wall to reclaim interior volume) and every honest number keeps moving in your favor, though with diminishing and eventually self-limiting returns (thinner walls make the already-failing tidal barrier numerically worse, and `--selftest` will not let the thermal barrier quietly flip to PASS -- at this scale that margin is down to 0.9% radiator area, close to the practical floor)
- **Finding and fixing modeling bugs as a legitimate efficiency lever** -- pass 3's biggest single gain came not from a new physics trick but from correcting two envelope-check constants that had never been wired up to scale with the rest of the ship, which had been silently overstating how much room the design had used up

What is NOT possible:
- **Superluminal flight** (NEC violation is a theorem)
- **Steering above c** (causal disconnection is a theorem)
- **Wormhole traversal** (QI closes the throat 10^26x before crossing)
- **Time travel** (chronology protection is expected to destroy the throat)
- **Negative energy at scale** (40 orders short of Casimir)

The model is an honest digital twin. It shows what the physics actually says -- not what science fiction would prefer.
