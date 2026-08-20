# How It Works -- Warpdrive WD-1 Foldrunner

A logical, step-by-step explanation of how the warp drive model works, from the physics to the engineering to the barriers. This document explains the *logic* -- for the formulas and proofs, see `README.md`. For the high-level summary, see `overview.md`.

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

The ship has a 200 m diameter toroidal ring centered on the bubble wall. The ring is not a solid tube -- it is a thin shell (0.6 m wall) of conditioned SiC/W metamaterial, divided into 24 independently driven sectors. The ring's stress-energy is what sources the shift vector. It sits *at* the bubble radius because that is where the curvature is.

### The field coils (the actuators)

24 superconducting REBCO coils (one per ring sector) shape the field. Each coil has 48,000 turns carrying 38,000 A at 18 K. The coils are the actuators that reshape the bubble wall -- they are the "steering wheel."

### The crew hull (the payload)

Inside the bubble, the crew live in a 68 m x 16 m hull with 4 decks. The hull is ordinary aerospace engineering -- Al-Li/composite pressure hull, 12 crew, life support. The hull sits in flat spacetime, so it does not need to survive acceleration or tidal forces. The only structural loads are from docking and the magsail deployment.

### The fusion reactor (the housekeeping plant)

A 22 GW D-3He spherical tokamak provides housekeeping power. It runs the coils, the cryoplant, and life support. It does NOT move the ship -- the energy to reach cruise speed comes from outside (the stellar tap). D-3He is chosen because it is aneutronic: the reaction D + 3He -> 4He + p produces no neutrons, so 62% of the energy can be direct-converted to electricity without a thermal cycle.

### The radiators (the thermal limit)

20 radiator panels, each 52 m x 18 m (both faces), total 37,440 m^2. They radiate waste heat at 1550 K design temperature, with a 1900 K graphite sublimation limit. The thermal balance is:

```
T = (P_waste / (epsilon x sigma_SB x A))^(1/4)
```

At beta=0.99 the radiators run at 1649 K -- within limits. At beta=2 they run at 2187 K -- the ship cooks. This is the only barrier that is *passable* (with 80% more radiator area).

### The Casimir lattice (the exotic-energy attempt)

24 cassettes of Casimir plates in the ring wall, each with 33 million plate pairs at 10 nm gap. The Casimir effect produces real negative energy density:

```
rho = -pi^2 hbar c / (720 a^4)
```

The total onboard negative energy is -2 MJ. The warp bubble demands -3.36 x 10^46 J. The gap is 40 orders of magnitude. This is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

---

## 4. The voyage: how the trip works

### Phase 1: Boost (the stellar tap)

The ship starts at rest near Earth. A 1000 km phased array in the solar system beams 10^17 W (0.026% of the sun's luminosity) at the ship's 4 km deployed rectenna. The beam is diffraction-limited:

```
d_spot = 2.44 x lambda x L / D
```

At 0.1 ly the spot is 2.3 km -- smaller than the rectenna, so capture is 100%. At 0.5 ly the spot is 11.5 km -- the 4 km rectenna captures only 12%. The beam range is 0.62 ly.

The ship accelerates by absorbing beam energy. The kinetic energy needed is:

```
KE = (gamma - 1) M c^2
```

At beta=0.5 this is 1.77 x 10^24 J (1.77 YJ). The boost takes 207 days. The maximum speed the beam can deliver is beta=0.562 -- this is *emergent*, not declared. Nothing in the dimensions names a maximum beta; it falls out of the energy-range race.

### Phase 2: Cruise (free flight)

At cruise the bubble is a stationary spacetime solution. The coils need power to hold their shape (6.2 GW at beta=1, scaling as beta^2), but no energy goes into *changing* the ship's velocity. The cruise is free in the GR sense -- the cost is engineering imperfection (coil ripple, control, refrigeration).

The cruise to Proxima at beta=0.5 takes 8.49 years. The crew age 8.49 years. Earth ages 8.49 years. There is no time-dilation dividend -- the warp interior is flat, so the crew clock runs at the same rate as the Earth clock. A relativistic rocket at the same speed would age only 7.36 years -- but the warp crew arrive in sync with home, which is the point.

### Phase 3: Brake (stopping)

This is the hardest engineering problem. The ship is moving at 0.5c and needs to stop. Three options:

**Option A: Magsail (always available, very slow)**

A 1000 km superconducting loop drags against the interstellar medium. The drag force is:

```
F = Cd x rho_ISM x v^2 x A
```

At beta=0.5 this is 10^7 N. The halving time is 60 years. The full stop time is 30,000 years. The drag falls as v^2, so the brake fades exactly when you need it most. This is the honest number -- the magsail alone cannot stop the ship in useful time.

**Option B: Photon brake (requires destination infrastructure)**

If a receiver array is already in place at Proxima, it can beam power at the ship. The photon pressure decelerates the ship:

```
F = 2P / c
t = gamma M v / F
```

At beta=0.5 with a 0.02 ly approach: F = 6.67 x 10^8 N, brake time = 381 days. This is the only way to stop in useful time -- but it requires someone to have already built the array at the destination.

**Option C: Both**

The real plan is to use the magsail for the initial deceleration and the photon brake for the final approach. The magsail gets you from 0.5c to ~0.05c; the photon brake finishes the job.

### Phase 4: Arrival

At Proxima Centauri b, the ship drops the bubble. The accumulated ISM particles (1.26 x 10^26 protons) are released forward as a blast of 2.37 PJ -- about 600 kilotons of TNT. This is a hazard for anything ahead of the ship, but it is a *floor* -- the true spectrum is worse.

The crew arrive having aged 8.49 years plus 2.35 seconds of gravitational drift (from climbing out of Sol's well and descending into Proxima's). The ship's own gravity contributes -9.43 x 10^-22 -- twelve orders of magnitude below the best clock ever built.

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
| Wall tidal gradient | FAIL | 7e15 g vs 1 g limit; thinner wall = worse |
| Superluminal NEC | THEOREM | SSV 2022: any v > c warp violates NEC |
| Negative energy scale | FAIL | 40 orders short of Casimir |
| Steering above beta=1 | THEOREM | causal disconnection (Everett/Coule/Krasnikov) |
| Thermal survival | FAIL | 2187 K vs 1900 K (passable with more radiators) |
| Ford-Roman wall | THEOREM | QI limits wall to 100 L_Planck |
| QI throat hold time | THEOREM | throat closes 10^26x before crossing |
| CTC chronology | CONJECTURE | Hawking 1992: divergent vacuum at horizon |

**Score: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable** (except thermal at subluminal speeds).

---

## 8. What the model actually proves

The model does NOT prove that warp drive is possible. It proves the opposite -- that warp drive as drawn cannot fly. But it does so with full mathematical rigor, showing exactly where the barriers are, how large they are, and what kind of physics would be needed to get past them.

What IS possible:
- **Subluminal warp** (beta < 1) with positive energy (Bobrick-Martire 2021, Fuchs et al. 2024)
- **Beam-powered acceleration** to beta ~ 0.562 (emergent, not declared)
- **Magsail deceleration** (very slow, 30,000 yr full stop)
- **Photon braking** (requires destination infrastructure)
- **Crew survival** (flat interior, no tidal forces, no time dilation)

What is NOT possible:
- **Superluminal flight** (NEC violation is a theorem)
- **Steering above c** (causal disconnection is a theorem)
- **Wormhole traversal** (QI closes the throat 10^26x before crossing)
- **Time travel** (chronology protection is expected to destroy the throat)
- **Negative energy at scale** (40 orders short of Casimir)

The model is an honest digital twin. It shows what the physics actually says -- not what science fiction would prefer.
