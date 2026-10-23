# How It Works -- Warpdrive WD-1u4 Foldrunner

A logical, step-by-step explanation of how the warp drive model works, from the physics to the engineering to the barriers -- and, in section 7, how the same model runs at car scale as the WD-88 Field Car in the SPECIAL WORKS tab. This document explains the *logic* -- for the formulas and proofs, see `README.md`. For the high-level summary and the full refit rationale, see `overview.md`. For the exhaustive component-by-component reference (every part's role, spec, mass, power draw, failure mode and buildability rating, generated live from the model's own ledgers), see `Infornmational.md`.

**A note on the model's discipline: it is 100% non-fiction.** Everything described below is a real, functionally-modelled system -- every part has a job, a mass, a power budget, a failure mode and a buildability rating that the selftest enforces. Where a concept exists only in published physics (negative energy, traversable wormholes, the time machine a wormhole becomes), the model says exactly that, computes the bill, and reports the quantified gap -- it never presents theory as built hardware and never dresses a decorative part up as a working one.

This revision covers the seventh refit pass, WD-1u4. Passes 1-5 shrank the ship to 0.4586x linear (mass 127,000 t -> 16,602 t, cruise 0.562c -> 0.857c against a fixed 100 PW beam); pass 6 upscaled ~2x back to near-full scale (125,416 t); pass 7 upscales ~2x again to 1.8344x WD-1 (crew 24), re-specifying every part rather than merely multiplying: component counts were re-derived from the doubled geometry (96 ring sectors/coils, 12 decks, 12 pylons, 60 radiator panels, 16 cryo units, 32 RCS pods, 8 traps, 96 Casimir cassettes), every wall/shell/skin thickness scaled x2 again for geometric/structural similarity, the magsail loop doubled to 2,800 km to restore drag on the x8-heavier hull, and the external tap was re-specified at 6.4 EW. The mass landed at 1,081,381 t. Reactor/radiator/coil power are re-derived from physical scaling laws rather than hand-typed throughout. The physics and the barrier verdicts are unchanged (the thermal barrier is deliberately kept failing at 2c by `--selftest`); the numbers below are the current ship's.

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

The major subsystems are explained below. For the complete bill of materials -- all 17 mass-budget lines plus the external infrastructure, each with spec, mass share, power draw, duty cycle, failure mode and buildability rating -- see `Infornmational.md` (generated from the same ledgers the model uses, via `python _gen_info.py`).

### The warp ring (the drive)

The ship has a 366.9 m diameter toroidal ring centered on the bubble wall (was 200 m at full scale, 130 / 107.9 / 91.7 / 183.4 m after passes 1/2/3-5/6). The ring is not a solid tube -- it is a thin shell (1.08 m wall, was 0.6 m at full scale) of conditioned SiC/W metamaterial, divided into 96 independently driven sectors. The ring's stress-energy is what sources the shift vector. It sits *at* the bubble radius because that is where the curvature is.

### The field coils (the actuators)

96 superconducting REBCO coils (one per ring sector) shape the field. Each coil has 48,000 turns carrying 38,000 A at 18 K -- the same HTS technology as the full-scale ship, wound around the 27.52 m ring tube on a 27.92 m clear bore (was ~15.2 m at full scale). The coils are the actuators that reshape the bubble wall -- they are the "steering wheel."

### The crew hull (the payload)

Inside the bubble, the crew live in a 124.8 m x 32.0 m hull with 12 decks (was 68 m x 16 m x 4 decks at full scale, 31.2 m x 8.0 m x 3 decks at pass 5, 62.4 m x 16.0 m x 6 decks at pass 6). The hull is ordinary aerospace engineering -- Al-Li/composite pressure hull with a 0.44 m wall (exactly 2x WD-1's: t = P*r/sigma is linear in radius), 24 crew, life support. The hull sits in flat spacetime, so it does not need to survive acceleration or tidal forces. The only structural loads are from docking and the magsail deployment.

### The fusion reactor (the housekeeping plant)

A 102.7 GW D-3He spherical tokamak provides housekeeping power (was 22 GW at full scale, 7 / 4.35 / 2.91 / 2.62 / 15.7 GW after passes 1/2/3/4-5/6). It runs the coils, the cryoplant, and life support. It does NOT move the ship -- the energy to reach cruise speed comes from outside (the stellar tap). D-3He is chosen because it is aneutronic: the reaction D + 3He -> 4He + p produces no neutrons, so 62% of the energy can be direct-converted to electricity without a thermal cycle. The plant was re-derived at pass 7 from the upscaled loads -- the beta=0.99 cruise electrical load is ~47.1 GW (coil AC x8, cryo/control x4, hotel x2 vs pass 6) -- and carries the same 1.35x margin over it. The reactor torus grew x8 in volume again, so specific power density holds steady.

### The radiators (the thermal limit)

60 radiator panels, each 90.44 m x 31.32 m (both faces), total 339,910 m^2 (was 52 m x 18 m / 37,440 m^2 at full scale, 15,818 / 10,895 / 7,081 / 42,489 m^2 after passes 1/2/3-5/6). They radiate waste heat at 1550 K design temperature, with a 1900 K graphite sublimation limit. The thermal balance is:

```
T = (P_waste / (epsilon x sigma_SB x A))^(1/4)
```

At beta=0.99 the radiators run at 1439 K -- within limits, and cooler than the full-scale ship's 1649 K. At beta=2 they run at 1961 K -- the ship still cooks, and the barrier now trips above beta ~ 1.87 (was ~1.45 at full scale, ~1.79 / ~1.97 / ~1.99 / ~1.80 after passes 1/2/3-5/6). The pass-7 area grew x8 against x6.6 waste heat, cooling the beta=0.99 equilibrium to 1439 K. This is the only barrier that is *passable* -- and it now needs +13.5% more radiator area (was +80% at full scale, +20% at pass 6). `--selftest` deliberately hard-asserts that T(2c) still exceeds 1900 K: the redesign is meant to track the margin needed to fix this barrier, not to quietly make it disappear.

### The Casimir lattice (the exotic-energy attempt)

96 cassettes of Casimir plates in the ring wall, each with about 61 million plate pairs at 10 nm gap (the gap itself is nanoscale and untouched by the ship's resize). The Casimir effect produces real negative energy density:

```
rho = -pi^2 hbar c / (720 a^4)
```

The total onboard negative energy is -3.09 MJ (was -2 MJ at full scale, -0.55 / -0.31 / -0.19 / -0.77 MJ after passes 1/2/3-5/6). The (183.44 m, 0.2 m-wall) warp bubble would demand -5.66 x 10^47 J if flown in superluminal Alcubierre mode -- which this ship never does. The gap is ~41 orders of magnitude: no combination of the scale and wall-thickness knobs closes it, because the onboard Casimir supply is never within tens of orders of what any of these bubble configurations demand. This is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

### A bug fix, not a new lever: the mount-offset scaling error

Two components in `_envelope_points()` -- the boost rectenna and the SMES buffer -- had their positions along the ship's spine written as bare numeric literals (`40.0` and `22.0` metres) instead of `DIMS` entries, dating from before either of the first two refit passes existed. Every other axial offset in the model (`cap_offset_m`, `rad_z0_m`, and so on) scaled down correctly each pass; these two silently did not. The bug never tripped a self-test because some *other* part of the ship was always the binding envelope constraint -- until pass 2 shrank the ship enough that it started to matter. Fixing it (`collector_z0_m`, `smes_z0_m`, both now `SCALE_S`-scaled `DIMS` entries) did not change any physics; it corrected a check that had been silently passing for the wrong reason, and in doing so revealed that the ship actually had more genuine room to shrink than the buggy check had reported.

---

## 4. The voyage: how the trip works

### Phase 1: Boost (the stellar tap)

The ship starts at rest near Earth. A 1000 km phased array in the solar system (external infrastructure, re-specified at pass 7 to 6.4 x 10^18 W = ~17 ppm of the sun's luminosity for the heavier hull) beams at the ship's 4 km deployed rectenna. The beam is diffraction-limited:

```
d_spot = 2.44 x lambda x L / D
```

At 0.1 ly the spot is 2.3 km -- smaller than the rectenna, so capture is 100%. At 0.5 ly the spot is 11.5 km -- the 4 km rectenna captures only 12%. The beam range is 0.62 ly.

The ship accelerates by absorbing beam energy. The kinetic energy needed is:

```
KE = (gamma - 1) M c^2
```

At beta=0.5 this is 1.51 x 10^25 J (15.1 YJ) -- 8.5x the full-scale bill (1.77 YJ at WD-1), because the hull is now 8.5x the original mass. The boost to the new maximum speed, beta=0.855 (was 0.562 at full scale, 0.727 / 0.794 / 0.844 / 0.845 / 0.857 / 0.863 after passes 1/2/3/4/5/6), takes ~303 days. This is *emergent*, not declared -- the x64-original tap pushes the x8.5 ship to almost exactly the same ceiling before it outruns the diffraction-limited spot.

#### How the cruise speed emerges (the two-clock race)

The speed beta=0.855 is not a parameter anywhere in the model. It falls out of a race between two clocks, and every step is derived from first principles. The full proofs are in info section **19k** (7 verified proof blocks, 7 self-test checks).

**The energy clock:** KE = (gamma - 1) M c^2. The gamma curve diverges at beta=1, so each knot closer to lightspeed costs more than the last:

| beta | gamma | KE | vs beta=0.855 |
|------|-------|----|----------------|
| 0.855 | 1.93 | 90.0 YJ | -- |
| 0.9 | 2.29 | 125.9 YJ | +40% for +5% speed |
| 0.95 | 3.20 | 214.2 YJ | +138% for +11% speed |
| 0.99 | 7.09 | 592.2 YJ | +558% for +16% speed |
| 0.999 | 22.4 | 2078 YJ | +2210% for +17% speed |
| 1.0 | inf | inf | wall |

**The range clock:** d_spot = 2.44 lambda L / D (Airy diffraction). The 1000 km aperture at 1.0 um produces a spot that grows linearly with distance. The 4 km rectenna captures 100% at 0.1 ly, 12% at 0.5 ly, 7.8% at 0.62 ly. Capture falls as 1/L^2. Past 0.62 ly the beam is too weak to matter.

**The race:** The boost integrates in 3-day steps, tracking position, velocity and delivered energy simultaneously. The ship starts at rest with 100% capture, then capture falls as it pulls away. After ~303 days the energy clock and range clock converge: the ship has 89.93 YJ and needs 90.02 YJ. At beta=0.87 it would need 100 YJ -- 11% short. That margin is why the cruise speed is 0.855 and not 0.87.

**The mass lever, run both ways:** Since KE = (gamma-1)Mc^2, the mass on the receiving end sets how high the ship climbs before it outruns the beam. Passes 1-5 shrank the ship 87% (127,000 t -> 16,602 t) against a fixed 100 PW tap and speed rose 52% (0.562 -> 0.857). Passes 6-7 grew it back ~x8 each time and re-specified the tap x8 each time (800 PW, then 6.4 EW) -- the emergent speed holds near 0.86 because tap/mass is roughly preserved. The relationship is superlinear in both directions, because the gamma curve is steeper at higher beta.

**Why it cannot reach beta=1:** At beta=1, gamma = infinity and KE = infinity. No finite beam can deliver infinite energy. This is special relativity, not engineering. Three levers could raise the speed further (larger aperture, shorter wavelength, lighter ship), but none touch the gamma wall. The beam can push the ship arbitrarily close to c, but never to c.

### Phase 2: Cruise (free flight)

At cruise the bubble is a stationary spacetime solution. The coils need power to hold their shape (38.3 GW at beta=1, scaling as beta^2 -- was 6.2 GW at full scale, coil count now 96), but no energy goes into *changing* the ship's velocity. The cruise is free in the GR sense -- the cost is engineering imperfection (coil ripple, control, refrigeration), and that cost grew back along with the hardware.

Door to door (boost + cruise + photon brake, assuming a destination array), the trip now takes about 5.9 years at the emergent beta=0.855 -- was ~8.5 years at full scale, ~7.0 / ~6.5 / ~6.0 / ~5.7 years after passes 1/2/3-5/6. The crew age the same as Earth ages -- there is no time-dilation dividend, because the warp interior is flat, so the crew clock runs at the same rate as the Earth clock. A relativistic rocket at the same speed would age less (about 2.6 years for the one-way trip) -- but the warp crew arrive in sync with home, which is the point.

### Phase 3: Brake (stopping)

This is the hardest engineering problem. The ship is moving at beta=0.855 and needs to stop. Three options:

**Option A: Magsail (always available, very slow)**

A 2,800 km superconducting loop (was 1000 km at full scale; doubled again at pass 7 to restore drag on the x8-heavier hull) drags against the interstellar medium. The drag force is:

```
F = Cd x rho_ISM x v^2 x A
```

At beta=0.5 this is 7.9 x 10^7 N. The halving time is 65 years. The full stop time is about 32,600 years (was 30,000 at full scale, ~20,600 / ~13,000 / ~8,860 / ~8,000 / ~15,000 after passes 1/2/4/5/6). The drag falls as v^2, so the brake fades exactly when you need it most. This is the honest number -- the magsail alone cannot stop the ship in useful time, and each x8 mass growth costs ~x2 the stopping time even with a doubled loop.

**Option B: Photon brake (requires destination infrastructure)**

If a receiver array is already in place at Proxima, it can beam power at the ship. The photon pressure decelerates the ship:

```
F = 2P / c
t = gamma M v / F
```

At beta=0.5 with a 0.02 ly approach: F = 4.27 x 10^10 N (set by the beam), brake time = 51 days (was 381 days at full scale, 128 / 81 / 55 / 55 / 50 / 47 days after passes 1/2/3/4/5/6). This is the only way to stop in useful time -- but it requires someone to have already built the array at the destination.

**Option C: Both**

The real plan is to use the magsail for the initial deceleration and the photon brake for the final approach.

### Phase 4: Arrival

At Proxima Centauri b, the ship drops the bubble. The accumulated ISM particles (4.25 x 10^26 protons, was 1.26 x 10^26 at full scale -- the 183.44 m bubble sweeps ~3.4x the full-scale cross-section) are released forward as a blast of about 8.0 PJ (was 2.37 PJ at full scale) -- roughly 1.9 megatons of TNT. This is a hazard for anything ahead of the ship, but it is a *floor* -- the true spectrum is worse.

The crew arrive having aged about 6.0 years plus roughly 1.6 seconds of gravitational drift (from climbing out of Sol's well and descending into Proxima's, over a shorter crossing than the full-scale ship's 8.49 years). The ship's own gravity contributes about -4.4 x 10^-21 -- two orders of magnitude below the best clock ever built, and stronger than the full-scale ship's -9.43 x 10^-22.

### TEST mode: the mission flies itself

The FLIGHT tab carries a TEST chip (also the T key) that auto-plays a mission with whatever settings are currently dialled in -- commanded beta (`,`/`.`), wall thickness (`[`/`]`), destination array on/off (`J`), and time warp (`-`/`+`). It resets the voyage while keeping those settings, then presses the same `begin_boost`/`begin_brake` commands the manual buttons press -- the physics is the ordinary integrator, only the button-pushing is scripted. The demo ends honestly: **ARRIVED** if the dialled-in configuration can actually stop the ship (destination array + photon brake in range), a labelled **flyby** if it reaches Proxima still moving, "still braking" with the real stop-time if the magsail alone is left to do it, or the collapse message if the settings cook the shell. At maximum time warp the brake margin is widened by one tick's travel distance, so a 10 yr/s demo cannot leapfrog the braking window into an accidental flyby.

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

The warp drive itself produces almost no time shift: +1.55 s gravitational drift over the 4.97 yr crossing (not controllable -- set by the Sol-Proxima gravitational potential difference), 0.0 s kinematic dilation (flat interior), and 0.0 desynchronization (a warp-carried mouth ages at the same rate as one at rest). The fast thing cannot build the causality violation; the slow rocket can.

**All scenarios remain blocked** by exotic energy (46 orders short), quantum inequalities (throat closes in ~10^-22 s vs ~10^7 s traversal), or chronology protection. The maximum time jump is a mathematical result, not an engineering capability. The full proofs are in info section **19j** in the viewer (press I), with 7 verified proof blocks covering combined clock rates, CTC onset, maximum backward/forward jumps, the warp-drive flat-interior theorem, gravitational drift, and the barrier analysis.

---

## 7. The WD-88 Field Car: the whole drive at car scale (SPECIAL WORKS)

The sixth tab runs the same model at car scale: every WD-1 subsystem folded into a 4.40 m stainless gull-wing coupe that drives a real road and fires its field transition at exactly 88 mph. It is a second audited machine, not a skin -- its own mass budget, power budget, operations ledger, thermal model, fault rig and ephemeris solver, held to the same rule: where the physics says impossible, the model says so and shows the number.

### Step 1: a real coupe shell, real contents

The body is a lofted chamfered-section coupe (wedge nose, cabin step, fastback tail) carrying a recognizable car: gull-wing seams, wire glazing (drawn as wire so it can never painter-hide the cabin), fascias, headlamp doors, taillight bar, grille, badge, mirrors, handles, the registration plate, wipers, sail louvers, air dam, diffuser strakes, sill plates, door struts, cowl vents, plate lamp, side repeaters. The cabin is furnished: seats + headrests, dash + binnacle + gauge faces, console + drive selector + radio/HVAC stack, steering wheel + column (canted 25 deg to the driver), pedals, parking brake, three-point belts, visors, dome light, glovebox, door pulls, a fire extinguisher -- and a drawn driver, because the mass budget books crew mass and honesty means drawing it.

### Step 2: where the ship's systems went

hull -> stainless monocoque | ring + 96 coils -> beltline field conduit run (the glowing bands ARE the coils, bolted on six standoffs, terminating at two rear-deck field-driver boxes, each a real HTS current-lead pack) | cap rings -> elliptical nose/tail shaping hoops (scaled in x to actually wrap the body sections) | reactor -> 150 kg D-3He microtorus in the trunk, with a decklid service cap and an He-3 filler neck | SMES -> a puck under the hood, charged through a shore-power socket on the left flank | Penning traps -> two bottles under the floor pan | Casimir lattice -> 12 strips lining the conduit run (-56.2 J, honestly 42 orders short of the -1.29e44 J shell bill) | radiators -> the rear-deck louver bank (the car-scale radiator, on the same hot=True channel the ship's fins use -- it visibly reddens under load) | cryoplant -> an underbody helium circulator with two cold lines | rectenna -> a roof whip on a real base | deflector -> a nose strip | RCS -> two aft-facing bells at the tail | magsail -> a KE-recovery loop stowed under the tail, returning the ship's own regen fraction of the run's kinetic energy to the SMES | navigator -> the dash ephemeris unit.

**No gasoline engine of any kind** -- the selftest scans every part name for it. The cabin hardware is all functional: the Y-manifold field transition sequencer, run sequencer display, arming lever, mission keypad and folded service ground hook; everything that actually moves spacetime is under the hood, the trunk, the floor and the beltline.

### Step 3: the drive loop (`car_mph_step`)

One tick of road speed, the same function the update loop and the selftest both call: hub motors pull **+30 mph/s** under throttle, regen brakes at **-45 mph/s**, rolling drag bleeds **-5 mph/s**; ceiling **130 mph**. At **exactly 88 mph** (39.33952 m/s -- the selftest asserts it is not 88 m/s) the transition fires -- but only while armed: a quenched SMES has no spike capacity, so 88 mph is just driving. Past the 1,100 K cell limit the drive **derates to 55 mph**. After firing, speed coasts down at -35 mph/s. Hostile inputs -- nan speedometer, negative speed -- are recovered, never trusted.

### Step 4: the thermal loop (`car_thermal_step`)

The rear-deck louvers are not trim -- they are the radiator. The trunk cell (60 kJ/K including blanket and plumbing) rejects heat through a 3.0 m^2 louver bank at emissivity 0.88, Stefan-Boltzmann, outward only. Audited equilibria: **idle 317 K, hard drive 752 K, louver-stalled 1,278 K** -- past the 1,100 K service limit, so the drive honestly derates. A single step can never overshoot the cell's own radiative equilibrium (at T_eq the louvers reject exactly the heat in), so a hostile 10^9 s step yields a bounded temperature, and the whole thing clamps to 120-6,000 K -- cryo floor below, "nothing aboard is still a solid" above.

### Step 5: live fault injection (the FAULT chip)

The ops ledger's failure modes run live: **smes** quench -> no spike capacity, the car rolls to 130 and never fires; **louver** stall -> rejection area x0.12 -> heat soak -> derate; **nav** drift -> the transit panel shows "EPHEMERIS LOST / the bubble has no fix / landing misses by ~transit ||d||" instead of a frozen solve. PARK clears the fault and stands the car down.

### Step 6: the same-road-spot solve (the ephemeris, fully)

The landing zone is fixed to **Earth**, not to space -- between departure and arrival, the same pavement rides Earth's orbit and rotation to a different inertial position. The solve:

- **Inertial frame:** Earth on a first-order Kepler ellipse, a = 1 AU, e = 0.0167 carried for real: M = 2pi t/T, r = a(1 - e cos M), theta = M + 2e sin M.
- **Rotating frame:** the road, a fixed lat/lon (34.05, -118.24) spun once per sidereal day (86,164.0905 s) at 6,371 km, with the pole tilted 23.44 deg out of the ecliptic.
- **The transit:** p_road(t) = E(t) + S(t)p; dep and arr are the same lat/lon/alt at two instants; the bubble's job is d = arr - dep, split into the orbital leg (~2 AU on a half-year hop) and the spin leg (~4,000 km).
- **Heading:** S(t) rotates the whole local (east, north, up) frame, so the lane's east vector lands as S(t1)*east -- the car arrives facing down the lane, not sideways (45 deg inertial rotation over a 3.7-day hop; selftest-verified orthonormal to 1e-9).
- **Velocity:** the car lands road-relative -- still doing 88 mph over the pavement. The ~29.79 km/s orbital + 0.385 km/s spin belongs to the planet and is never booked against the chassis.
- **Honest limits:** first-order e only (~2 km), no lunar perturbation/nutation/polar motion/bulge, mean radius -- a production run swaps in JPL DE440; the frame structure is unchanged.

The TRANSIT panel previews the whole solve live before firing (`[`/`]` dial the hop, 60 s to 10 yr), draws dep->arr on an ecliptic mini-map, and after the run leaves the TRANSITION TRAIL -- the twin scars on the tarmac, a part that only exists after the event.

### What the model proves at this scale

Downscaling buys the R^2 in the field energy -- the car's exotic bill (-1.29e44 J) is ~4 orders smaller than the ship's -- **not a way around the sign of it**: the 12 Casimir strips' -56.2 J are still 42 orders short. The honesty machinery is identical: derived mass to 1e-6, funded bus, live ops ledger, real-function spec cards enforced by selftest, and ~30 dedicated checks covering trigger exactness, thermal equilibria, fault fidelity, ephemeris extremes (poles, +/-32,000-year epochs, 60 s and 10-year hops) and hostile inputs everywhere.

---

## 8. The honesty layer: why the model says "no"

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
| Thermal survival | FAIL | 1990 K vs 1900 K at 2c (passable with more radiators; was 2187 K at full scale) |
| Ford-Roman wall | THEOREM | QI limits wall to 100 L_Planck |
| QI throat hold time | THEOREM | throat closes 10^26x before crossing |
| CTC chronology | CONJECTURE | Hawking 1992: divergent vacuum at horizon |

**Score: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable** (except thermal at subluminal speeds).

---

## 9. What the model actually proves

The model does NOT prove that warp drive is possible. It proves the opposite -- that warp drive as drawn cannot fly. But it does so with full mathematical rigor, showing exactly where the barriers are, how large they are, and what kind of physics would be needed to get past them.

What IS possible:
- **Subluminal warp** (beta < 1) with positive energy (Bobrick-Martire 2021, Fuchs et al. 2024)
- **Beam-powered acceleration** to beta ~ 0.855 for this hull (emergent, not declared; was ~0.562 at full scale, ~0.727 / ~0.794 / ~0.844 / ~0.845 / ~0.857 / ~0.863 after passes 1/2/3/4/5/6)
- **Magsail deceleration** (very slow, ~32,600 yr full stop at this scale, was ~30,000 yr at full scale)
- **Photon braking** (requires destination infrastructure)
- **Crew survival** (flat interior, no tidal forces, no time dilation)
- **The mass/tap lever, run honestly in both directions** -- the genuine engineering lever this model exposes: passes 1-5 shrank the ship against a fixed 100 PW beam (0.562c -> 0.857c); passes 6-7 grew it back ~x8 each and re-specified the tap each time (800 PW, then 6.4 EW), holding the emergent speed near 0.86c at the cost of honest consequences (32,600 yr magsail stop, +13.5% thermal-barrier margin needed, scoop parity lost at EVERY speed). `--selftest` still will not let the thermal barrier quietly flip to PASS.
- **Finding and fixing modeling bugs as a legitimate efficiency lever** -- pass 3's biggest single gain came not from a new physics trick but from correcting two envelope-check constants that had never been wired up to scale with the rest of the ship, which had been silently overstating how much room the design had used up

What is NOT possible:
- **Superluminal flight** (NEC violation is a theorem)
- **Steering above c** (causal disconnection is a theorem)
- **Wormhole traversal** (QI closes the throat 10^26x before crossing)
- **Time travel** (chronology protection is expected to destroy the throat)
- **Negative energy at scale** (40 orders short of Casimir)

The model is an honest digital twin. It shows what the physics actually says -- not what science fiction would prefer.
