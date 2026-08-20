# Warpdrive WD-1 Foldrunner

A physics-honest digital twin of a warp-drive starship, a traversable wormhole portal, and the time machine that any wormhole automatically becomes. Every number is computed from the real general-relativity and quantum-field-theory formulas. Nothing is fictional. Where the physics says "impossible," the model says so and shows the computation that proves it.

## Quick start

```
python Warpdrive.py                  # interactive 3D viewer (needs pygame)
python Warpdrive.py --selftest       # 157 physics checks
python Warpdrive.py --send           # portal traversal: send things through
python Warpdrive.py --portal         # wormhole construction report
python Warpdrive.py --metric         # Alcubierre metric report
python Warpdrive.py --dilation       # time dilation report
python Warpdrive.py --feasibility    # feasibility scorecard
python Warpdrive.py --voyage 0.5     # headless Sol -> Proxima flight
python Warpdrive.py --all            # every report in order
```

Headless mode works without pygame. All reports and self-tests run on pure Python + NumPy.

## What this is

The WD-1 Foldrunner is a 1.27 x 10^8 kg starship that carries a 100 m bubble of flat spacetime to Proxima Centauri b (4.2465 ly) at beta = 0.562. Inside the bubble the crew are weightless, un-accelerated, and un-dilated for the entire voyage. The drive is subluminal by design -- and that is not a compromise, it is the reason it is buildable.

The model also computes, honestly and with full provenance:

- The Alcubierre superluminal metric and why it is unfunded (negative energy, 38+ orders short).
- The Morris-Thorne traversable wormhole and why it is unbuilt (exotic energy, tidal forces, quantum inequalities).
- The Maldacena-Milekhin-Popov (2020) construction and why it needs unobserved magnetic monopoles.
- The Visser thin-shell wormhole and why concentrating exotic matter costs more, not less.
- The closed-timelike-curve time machine that any wormhole automatically becomes, and Hawking's chronology protection conjecture.
- Quantum teleportation and why it is not a portal (state transfer, not matter; classical channel capped at c).
- The interstellar-medium hazard, magsail braking, photon braking, radiator limits, and the beam-delivered speed limit.

## Interactive viewer

Five tabs (click or press 1-5):

| Tab | Key | What it shows |
|-----|-----|---------------|
| SHIP | 1 | The starship: ring, hull, radiators, reactor, coil sequence |
| METRIC | 2 | The warp bubble: York expansion grid, energy-density hotspots |
| DILATION | 3 | Clock rates: comoving vs static, gravitational drift |
| PORTAL | 4 | The wormhole: throat, flare-out, tidal profile, both mouths |
| FLIGHT | 5 | Flight sim: boost, cruise, brake, arrival (keys W/S/J) |

Press **I** for the full specification panel with math proofs. Press **H** for controls. Press **PgUp/PgDn** to scroll.

---

## Math proofs

Every number in the model follows from a published formula. Below are the proofs, the computed values, and the self-test that verifies each one.

### 1. The Alcubierre metric

```
ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2
```

**Shape function:**

```
f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R))
```

- f = 1 inside the bubble (flat, carried along)
- f = 0 outside (untouched spacetime)
- sigma = 1/delta sets the wall thickness

**Verification:** f(0) = 1, f(R) = 0.5, f(inf) = 0. Numerical integral of r^2 (df/dr)^2 matches the closed form R^2 sigma / 3 to 3.2 x 10^-5 relative error. [Self-test: PASS]

### 2. Alcubierre energy density

```
T^00 = -(c^4 / 8 pi G) (beta^2 rho^2 / 4 r_s^2) (df/dr_s)^2
```

The energy density is **negative** everywhere in the wall. This is the null energy condition (NEC) violation that makes superluminal warp impossible with known matter.

**Total energy:**

```
E = -(c^4 beta^2 / 12 G) INT r^2 (df/dr)^2 dr
```

At R = 100 m, beta = 10, delta = 10^-15 m: E ~ -3.36 x 10^63 J (matches Alcubierre's 1994 estimate; note the negative sign -- this is exotic energy). [Self-test: PASS]

### 3. Ford-Roman quantum inequalities

```
|rho| <= 3 hbar / (32 pi^2 c^3 tau^4)
```

The maximum hold time for a throat of radius b0:

```
tau_max = (3 hbar G b0^2 / (4 pi c^7))^(1/4)
```

For a 12 m throat: tau_max = 3.25 x 10^-26 s. Traversal takes 4.8 s. The throat closes 10^26 times before you are halfway through. [Self-test: PASS]

The Ford-Roman wall thickness limit is ~100 L_Planck (a few hundred Planck lengths, per Pfenning & Ford 1997). The model uses this as an order-of-magnitude bound.

### 4. Morris-Thorne wormhole

```
ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2
```

**Shape function:** b(r) = b0^2 / r
- b(b0) = b0 (throat radius)
- b'(b0) = -1 < 1 (flare-out condition -- the throat opens out, doesn't pinch)

**Throat energy density:**

```
rho = -c^4 / (8 pi G b0^2)
```

For a 12 m throat: rho = -3.34 x 10^40 J/m^3. [Self-test: PASS]

**Tidal acceleration across a body of size L:**

```
a_tidal = c^2 L / b0^2
```

For a 2 m person at a 12 m throat: 1.27 x 10^14 g (lethal). [Self-test: PASS]

**Survivable throat:**

```
b0_min = sqrt(c^2 L / g_limit) = sqrt(9 x 10^16 x 2 / 9.81) = 1.35 x 10^8 m
```

That is 10.6 Earth diameters. The exotic energy bill: -2.73 x 10^51 J (45 orders beyond the Casimir lattice). [Self-test: PASS]

### 5. Portal traversal -- WHERE you come out

A wormhole connects mouth A to mouth B. **You cannot choose the exit independently of where mouth B physically is.** The "where" is controllable only by moving mouth B.

**Verification:** portal_traversal() returns mouth_sep_m = separation of the two mouths. Default = Proxima distance (4.02 x 10^16 m = 4.2465 ly). Custom separation is a parameter. [Self-test: PASS]

### 6. Portal traversal -- WHEN you come out

The two mouths desynchronize whenever they sit at different gravitational potentials or move at different speeds. This is real GR, the same effect GPS satellites correct for daily (45 microseconds/day from gravity, 7 microseconds/day from motion).

**Mouth clock rate:**

```
dtau/dt = sqrt(1 + 2 Phi / c^2) x 1/gamma(beta)
```

- Gravitational: sqrt(1 + 2 Phi/c^2) -- slower in a gravity well
- Kinematic: 1/gamma(beta) -- slower when moving
- A warp drive contributes NOTHING: the interior is flat spacetime, so a mouth carried by warp ages at the same rate as one at rest

**Verification:**
- Flat space, at rest: rate = 1.000000 [PASS]
- Horizon (Phi/c^2 = -0.5): rate = 0 [PASS]
- Phi/c^2 = -0.1: rate = sqrt(0.8) = 0.8944 [PASS]
- beta = 0.6: rate = 1/1.25 = 0.8 [PASS]
- Combined: rate = sqrt(0.8)/gamma(0.5) [PASS]
- Monotonic: deeper well -> slower, faster -> slower [PASS]

**Time offset (linear accumulation):**

```
delta_t = elapsed x (rate_a - rate_b)
```

- Equal rates -> zero offset [PASS]
- rate_a=1, rate_b=0.9, t=100 -> delta_t = 10 s [PASS]
- Doubling t doubles delta_t [PASS]
- Slower B -> positive offset (B behind A) [PASS]
- Clock consistency: rate_a x t = rate_b x t + delta_t [PASS]

### 7. CTC onset -- the time machine boundary

**Morris, Thorne & Yurtsever (1988):** CTCs exist the instant the clock offset exceeds the light-travel time between the mouths.

```
CTCs exist when |delta_t| >= D / c
```

- Before that: you arrive in B's past relative to A's present, but NOT in your own past -- no paradox possible.
- After that: you can step through and arrive before you left -- a time machine.

**Verification:**
- Zero offset -> no CTC [PASS]
- |delta_t| < D/c -> no CTC [PASS]
- |delta_t| = D/c -> CTC (boundary) [PASS]
- |delta_t| > D/c -> CTC [PASS]
- At onset: delta_t = D/c exactly [PASS]
- Proxima light-time = 4.2465 yr [PASS]

**CTC onset time:**

```
t_onset = (D / c) / |rate_a - rate_b|
```

Mouth parked at Phi/c^2 = -0.2 (neutron-star depth): rate gap 0.225 -> time machine in 18.84 yr. [Self-test: PASS]

### 8. Warp cannot desynchronize (the flat-interior theorem)

A warp bubble interior is exactly Minkowski spacetime (f = 1, all derivatives zero). A mouth carried by a warp drive experiences **no kinematic time dilation**, regardless of the bubble's speed.

```
Warp-carried mouth:  offset = 0  (after any elapsed time)
Rocket-carried mouth at beta=0.9:  offset > 0  (desynchronises)
```

**The fast thing cannot build the causality violation. The slow rocket can.** This is a theorem, not a gap. [Self-test: PASS]

### 9. Exotic energy scaling

```
E = -c^4 b0 / (6 G)    (linear in b0)
```

- E is always negative (exotic) [PASS]
- E(100m) / E(10m) = 10.0 (linear scaling) [PASS]
- Casimir shortfall > 0 (always falls short) [PASS]
- Onboard Casimir lattice: -2.0 x 10^6 J
- 12 m throat demand: -2.42 x 10^44 J (38 orders short)
- Survivable throat demand: -2.73 x 10^51 J (45 orders short)

### 10. Quantum teleportation (the real teleporter)

Quantum teleportation (Bennett et al. 1993) is experimentally demonstrated and routine (1400 km via Micius satellite, 2017). It does none of the things a portal does:

- It moves a quantum **state**, not matter.
- It needs pre-shared entanglement.
- It needs 2 classical bits per qubit, and that classical channel is capped at c -- no information moves faster than light.
- No-cloning means the original is destroyed.

**Teleporting one person:**

```
~7 x 10^27 atoms x 100 bits/atom = 7 x 10^29 bits
At 1 Tb/s: 2.22 x 10^10 years = 1.6 x age of universe
```

And you would still arrive at light speed at best. [Self-test: PASS]

---

## Math proofs (every formula, verified)

The UI info panel (press `I` in the visualizer) now contains 6 proof sections with 33 individual proofs. Each proof states the formula, the computed value, and the self-test check that verifies it. The self-test has been expanded from 95 to 120 checks to cover every function.

### Alcubierre metric proofs (section 19c)

1. **Shape function** f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R))
   - f(0) = 1, f(R) = 1/2, f(R+40) = 0 [PASS]

2. **Shape derivative** df/dr = sigma[sech^2(sigma(r+R)) - sech^2(sigma(r-R))] / (2 tanh(sigma R))
   - At r = R: df/dr = -sigma/2 = -0.500000 [PASS]
   - Antisymmetric: df/dr(+R) = -df/dr(-R) [PASS]

3. **Energy density** T^00 = -(c^4/8piG)(beta^2 rho^2/4r^2)(df/dr)^2
   - At equator: -3.01 x 10^41 J/m^3 (NEGATIVE) [PASS]
   - Matches manual closed-form calculation [PASS]

4. **Wall tidal gradient** a ~ beta c^2 |f''|_max L
   - At beta=0.5: 3.52 x 10^15 g (lethal) [PASS]
   - Scales as beta^2 [PASS]

5. **Ford-Roman wall limit** delta_max ~ 100 L_Planck / beta
   - At beta=1: 100.0 L_Planck = 1.62 x 10^-33 m [PASS]
   - Scales as 1/beta [PASS]

### Energy & engineering proofs (section 19d)

1. **Relativistic kinetic energy** KE = (gamma - 1) M c^2
   - At beta=0.5: 1.77 x 10^24 J (1.77 YJ) [PASS]
   - Verified for beta = 0.1, 0.5, 0.9, 0.99 [PASS]
   - No solution for beta > 1 [PASS]

2. **SMES magnetic storage** E = (B^2/2 mu_0) V_torus
   - Stored: 448 GJ (positive, finite) [PASS]

3. **Fusion fuel** m = E / (eta x E_D3He_per_kg)
   - Crossing at beta=0.5: 4419 kg D-3He [PASS]

4. **Stefan-Boltzmann radiator** T = (P / (eps sigma A))^(1/4)
   - At beta=0.99: 1649 K (limit 1900 K) [PASS]
   - At beta=2: 2187 K (OVER limit) [PASS]
   - Round-trip recovers P [PASS]

### Beam & braking proofs (section 19e)

1. **Beam diffraction** d_spot = 2.44 lambda L / D
   - lambda = 1.0 um, D = 1000 km [PASS]
   - At 0.5 ly: spot = 11.5 km [PASS]
   - Spot grows linearly with distance [PASS]

2. **Beam capture** f = (d_rectenna/d_spot)^2, capped at 1.0
   - At 0.5 ly: capture = 0.1201 (12%) [PASS]
   - Never exceeds 1.0 [PASS]

3. **Photon brake force** F = 2P/captured / c
   - Brake force: 6.67 x 10^8 N [PASS]
   - F <= 2P_tap/c [PASS]

4. **Photon brake time** t = gamma M v / F
   - At beta=0.5: 381.3 d [PASS]

5. **Magsail drag** F = Cd rho_ISM v^2 A
   - Cd = 0.85, A = 3.14 x 10^12 m^2 [PASS]
   - At beta=0.5: 1.00 x 10^7 N [PASS]
   - Scales as v^2: F(1.0) = 4 x F(0.5) [PASS]
   - Halving time: 60.1 yr (looks feasible) [PASS]
   - Stop time: 3 x 10^4 yr (the honest number) [PASS]

### ISM & time dilation proofs (section 19f)

1. **ISM particles swept** N = n_ISM pi R^2 distance
   - n_ISM = 1.0 x 10^5 /m^3, R = 100 m [PASS]
   - Proxima crossing: 1.26 x 10^26 protons [PASS]

2. **ISM blast energy** E = N m_p c^2 beta^2/2 (conservative floor)
   - At beta=0.5: 2.37 x 10^15 J (2.37 PJ) [PASS]

3. **Static observer lapse** dtau/dt = sqrt(1 - beta^2 f(r)^2)
   - At centre (f=1): 1/gamma(beta) [PASS]
   - At beta=0.5 centre: 0.866025 = 1/gamma [PASS]
   - At beta=0.5 wall: 0.968246 = sqrt(1-beta^2 f^2) [PASS]
   - No static observer for beta >= 1 [PASS]

4. **Gravitational clock rate** dtau/dt = sqrt(1 + 2Phi/c^2)
   - Earth orbit: 0.999999990129 [PASS]
   - Matches textbook: 1 - 9.87e-9 [PASS]
   - Deep space: 1.0 to 1 part in 1e12 [PASS]

5. **Rocket proper time** tau = (d/beta c) / gamma
   - At beta=0.5 to Proxima: 7.36 yr [PASS]
   - Warp crew age MORE (10.0 yr) -- no dilation dividend [PASS]

### Wormhole proofs (section 19g)

1. **Morris-Thorne shape** b(r) = b0^2/r
   - b(r0) = r0 (identity) [PASS]
   - b'(r0) = -1 < 1 (flare-out) [PASS]
   - Phi = 0 (zero-tidal choice) [PASS]

2. **Throat density** rho = -c^4/(8piG b0^2)
   - At b0=12m: -3.34 x 10^40 J/m^3 [PASS]
   - Scales as 1/b0^2 [PASS]

3. **Exotic energy** E = -c^4 b0/(6G) (linear in b0)
   - At b0=12m: -2.42 x 10^44 J [PASS]
   - E(100m)/E(10m) = 10.0 [PASS]

4. **Tidal profile** a(r) = c^2 |b' - b/r| L / (2r^2)
   - At throat: 1.27 x 10^14 g [PASS]
   - At 2b0: 7.95 x 10^12 g (1/16 of throat) [PASS]
   - At 4b0: 4.97 x 10^11 g (1/64 of throat) [PASS]

5. **Proper length** l = integral dr / sqrt(1 - b(r)/r)
   - To 4b0: 45.85 m = 3.82 b0 [PASS]

6. **Ford-Roman QI** |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)
   - At tau=1s: -3.72 x 10^-62 J/m^3 [PASS]
   - 102 orders below throat demand [PASS]
   - Max hold for 12m: 3.25 x 10^-26 s [PASS]
   - Traversal takes 4.8 s -- 26 orders longer [PASS]

7. **Visser thin-shell** sigma = -c^2/(2piGa) sqrt(1-2GM/(ac^2))
   - At a=12m, M=0: -3.23 x 10^28 kg = -0.0163 M_sun [PASS]
   - E = mc^2 = -2.90 x 10^45 J [PASS]
   - Visser > MT (concentrating costs MORE) [PASS]
   - Vanishes at horizon [PASS]

8. **MMP wormhole** Q_ext = sqrt(4pi eps0 G) M; t = (GM/c^3) ln(M/M_planck)
   - Q_ext = 7.85 x 10^24 C [PASS]
   - ln(M/M_planck) = 98.1 [PASS]
   - Traversal: 22.2 s (human-scale) [PASS]
   - r_s = safe_b0 (same curvature, different route) [PASS]

9. **Casimir density** rho = -pi^2 hbar c / (720 a^4)
   - At 10nm: -4.33 x 10^4 J/m^3 [PASS]
   - Falls as 1/a^4: 20nm/10nm ratio = 1/16 [PASS]

10. **CTC onset time** t_onset = (D/c) / |rate_a - rate_b|
    - At rate_diff=0.1, D=Proxima: 42.47 yr [PASS]
    - At onset: offset = D/c exactly [PASS]

### Cross-formula consistency proofs (section 19h)

These proofs verify that different formulas computing the same quantity from different routes give the same answer. They catch dimensional errors and typos.

1. **MT density x volume = MT energy** rho * (4/3)pi b0^3 = -c^4 b0/(6G) [PASS]
2. **MT tidal = profile at throat** mt_tidal_g(b0) = mt_tidal_profile(b0, b0) [PASS]
3. **Tidal at b0_min = 1 g** b0_min = sqrt(c^2 L/g) -> a = g by construction [PASS]
4. **Alcubierre energy beta^2 scaling** E(2c)/E(1c) = 4, E(5c)/E(1c) = 25 [PASS]
5. **Alcubierre energy 1/delta scaling** E(0.1)/E(1) = 10 (thinner = costlier) [PASS]
6. **Warp energy = -(c^4/12G) beta^2 I** integral formula cross-check [PASS]
7. **Lorentz gamma = 1/sqrt(1-beta^2)** verified for beta = 0.1, 0.5, 0.9, 0.99 [PASS]
8. **Ford-Roman derivation** |rho_QI(tau_max)| = |rho_throat| recovers tau_max [PASS]
9. **Visser E = mc^2** shell_energy = shell_mass * c^2 [PASS]
10. **MMP mass = c^3 sqrt(L/(4G^2 g))** from tidal formula, solving for M [PASS]
11. **Mouth clock rate = sqrt(1+2Phi/c^2) / gamma** grav x kinematic consistency [PASS]

### Dimensional analysis (all formulas verified)

Every formula has been checked for dimensional consistency in SI base units:

| Formula | Expected units | Verified |
|---------|---------------|----------|
| T^00 = -(c^4/8piG)(beta^2 rho^2/4r^2)(df/dr)^2 | J/m^3 | PASS |
| E = -(c^4/12G) beta^2 I (I in m) | J | PASS |
| KE = (gamma-1) M c^2 | J | PASS |
| rho_MT = -c^4/(8piG b0^2) | J/m^3 | PASS |
| E_MT = -c^4 b0/(6G) | J | PASS |
| a_tidal = c^2 L / b0^2 | m/s^2 | PASS |
| rho_QI = 3hbar/(32pi^2 c^3 tau^4) | J/m^3 | PASS |
| tau_max = (3hbar G b0^2/(4pi c^7))^(1/4) | s | PASS |
| sigma_Visser = -c^2/(2piGa) sqrt(1-2GM/ac^2) | kg/m^2 | PASS |
| rho_Casimir = -pi^2 hbar c / (720 a^4) | J/m^3 | PASS |
| Q_MMP = sqrt(4pi eps0 G) M | C | PASS |
| t_MMP = (GM/c^3) ln(M/M_planck) | s | PASS |
| T_rad = (P/(eps sigma A))^(1/4) | K | PASS |
| d_spot = 2.44 lambda L / D | m | PASS |
| F_magsail = Cd rho v^2 A | N | PASS |
| F_brake = 2P/c | N | PASS |
| tau_rocket = (d/beta c) / gamma | s | PASS |
| t_CTC = (D/c) / rate_diff | s | PASS |

### Barrier engineering analysis (section 19i)

For each of the 8 barriers that block the drive, the model computes the exact number, the threshold, the gap in orders of magnitude, and what a hypothetical route past it would require. This is the "engineer past all barriers" audit -- and the honest answer for 7 of 8 is **no**.

| # | Barrier | Status | Value | Threshold | Gap |
|---|---------|--------|-------|-----------|-----|
| 1 | Bubble wall tidal gradient | FAIL | 7.04e15 g | 1 g | 16 orders |
| 2 | Superluminal NEC (SSV theorem) | THEOREM | NEC violated at v>c | NEC required | theorem |
| 3 | Negative energy scale | FAIL | 3.36e46 J needed | 2.0e6 J (Casimir) | 40 orders |
| 4 | Steering above beta=1 | THEOREM | causally disconnected | controllable | theorem |
| 5 | Thermal survival at 2c | FAIL | 2187 K | 1900 K | 15% over |
| 6 | Ford-Roman wall thickness | THEOREM | delta_max = 100 L_P | delta = 1 m | theorem |
| 7 | QI throat hold time | THEOREM | 3.25e-26 s | 4.8 s traversal | 26 orders |
| 8 | CTC chronology protection | CONJECTURE | divergent vacuum | stable throat | conjecture |

**Routes past each barrier (and why they fail):**

1. **Wall tidal**: Thinner wall -> MORE tidal, not less. At QI-legal thickness (100 L_P): 2.70e81 g. Anti-route.
2. **Superluminal NEC**: SSV theorem (2022) proves ANY v>c warp violates NEC. No route -- this is a theorem about the whole class, not just Alcubierre's ansatz.
3. **Negative energy**: More Casimir cassettes -> need 4e41 cassettes. Each is 1m x 1m. That is 10^29 Earths of Casimir plates.
4. **Steering**: Forward wall is causally disconnected at v>c. The crew cannot send a control signal to the front of the bubble. The entire trajectory must be pre-laid. Theorem (Everett 1996, Coule 1998, Krasnikov 1998).
5. **Thermal**: More radiator area -> need 65688 m^2 (have 37440 m^2). This is the ONLY passable barrier -- 1.8x more radiator area would fix it. But it only buys you beta ~ 1.45, not superluminal.
6. **Ford-Roman wall**: QI theorem limits wall to 100 L_P = 1.62e-33 m. At that thickness E = 2.08e79 J = 10^9 universes of energy.
7. **QI throat**: Throat closes in 3.25e-26 s. Traversal takes 4.8 s. The throat closes 10^26 times before you are halfway through.
8. **CTC**: Hawking's chronology protection conjecture (1992) expects divergent vacuum fluctuations at the chronology horizon. Not proven, but strongly expected by the majority of the field.

**Scorecard: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable (except thermal at subluminal speeds only).**

This is the honest engineering assessment: the drive cannot fly as drawn. The theorems are not engineering challenges -- they are mathematical proofs about what is possible. The 40-order energy gap is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

---

## Environmental sustaining components (math proofs for each subsystem)

Every subsystem that fabricates or sustains the warp drive has its own formula, computed value, and self-test check. Below are the proofs for each environmental sustaining component.

### 1. Mass budget (every kilogram derived from geometry)

**Formula:** Each component mass = volume x density, computed from DIMS geometry.

```
m_component = surface_area x wall_thickness x density    (shells)
m_component = volume x density                            (solids)
```

**Total ship mass:** 1.270 x 10^8 kg (126,986 tonnes) [Self-test: PASS]

| Component | Mass (kg) | % | Formula |
|-----------|-----------|---|---------|
| Warp ring shell | 72,837,680 | 57.4% | 4pi^2 R r x wall x 4100 kg/m^3 |
| HTS field coils (24) | 23,144,013 | 18.2% | 24 x coil_volume x 6000 kg/m^3 |
| Shaping rings (2) | 19,034,914 | 15.0% | 2 x torus_surface x 0.35 x 4100 |
| Pylons (3) | 2,612,736 | 2.1% | 3 x 84 x 3.2 x 1.2 x 2700 |
| Radiators (20) | 2,134,080 | 1.7% | 20 x 52 x 18 x 0.06 x 1900 |
| Fusion reactor | 1,995,397 | 1.6% | torus_surface x 0.9 x 5200 |
| Crew hull shell | 1,786,685 | 1.4% | hull_area x 0.22 x 2700 |
| SMES buffer | 885,896 | 0.7% | torus_surface x 0.25 x 6800 |
| Crew decks (4) | 650,287 | 0.5% | 4 x pi r^2 x 0.35 x 2700 |
| Casimir lattice (24) | 635,904 | 0.5% | 24 x 2.4^2 x 2.0 x 2300 |
| Magsail loop | 420,000 | 0.3% | 4.2e5 kg (HTS cable) |
| Cryoplant (4) | 298,577 | 0.2% | 4 x pi r^2 x 11 x 240 |
| Antimatter traps (2) | 224,264 | 0.2% | 2 x 4pi r^2 x 0.30 x 4400 |
| RCS pods (8) | 191,134 | 0.2% | 8 x pi r^2 x 5 x 900 |
| Deflector | 78,885 | 0.1% | pi r^2 x 0.10 x 3100 |
| Consumables + crew | 38,400 | 0.0% | 12 x 3200 |
| Boost rectenna | 17,593 | 0.0% | pi (2000)^2 x 1e-6 x 1400 |

**Cross-check:** sum(mass_budget) = SHIP_MASS_KG (verified to 1e-6) [Self-test: PASS]

### 2. D-3He fusion reactor (housekeeping power)

The reactor does NOT move the ship. It runs the coils, cryoplant, and hotel load.

**Formula:**
```
P_thermal = 22 GW
P_electrical = P_thermal x eta_direct = 22 x 0.62 = 13.64 GW
m_fuel = E_required / (eta x E_D3He_per_kg)
E_D3He = 3.52 x 10^14 J/kg  (D + 3He -> 4He + p + 18.35 MeV)
```

**Computed values:**
- Thermal output: 22 GW
- Direct conversion efficiency: 62% (aneutronic)
- Fuel for Proxima crossing at beta=0.5: 4,419 kg D-3He [Self-test: PASS]
- Specific energy: 3.52 x 10^14 J/kg

### 3. Stellar-tap boost beam (the only way to accelerate)

The ship cannot carry enough energy to reach cruise speed. A 1000 km phased array beams power from Sol.

**Formula (Airy diffraction):**
```
d_spot = 2.44 x lambda x L / D_aperture
f_capture = (d_rectenna / d_spot)^2   if d_spot > d_rectenna, else 1.0
P_captured = P_tap x f_capture
```

**Computed values:**
- Tap power: 1.0 x 10^17 W (0.026% of L_sun)
- Aperture: 1000 km, wavelength: 1.0 um
- Deployed rectenna: 4 km diameter
- At 0.01 ly: spot = 0.2 km, capture = 100% [Self-test: PASS]
- At 0.10 ly: spot = 2.3 km, capture = 100% [Self-test: PASS]
- At 0.50 ly: spot = 11.5 km, capture = 12.0% [Self-test: PASS]
- At 1.00 ly: spot = 23.1 km, capture = 3.0% [Self-test: PASS]
- Capture never exceeds 1.0 (energy conservation) [Self-test: PASS]
- Usable boost range: 0.62 ly
- Maximum emergent cruise speed: beta = 0.562 [Self-test: PASS]

**Boost energy:**
```
KE = (gamma - 1) M c^2
```
- At beta=0.5: KE = 1.77 x 10^24 J (1.77 YJ), boost time = 207 d [Self-test: PASS]
- At beta=0.562: KE = 2.38 x 10^24 J, boost time = 276 d
- At beta=0.9: KE = 1.48 x 10^25 J -- beam cannot deliver (range exceeded)

### 4. SMES magnetic energy storage (transient buffer)

**Formula:**
```
E = (B^2 / 2 mu_0) x V_torus
V_torus = 2 pi^2 R r^2
```

**Computed values:**
- Major radius: 11 m, minor radius: 1.2 m
- Field: 60 T
- Volume: 2 pi^2 x 11 x 1.2^2 = 313 m^3
- Energy density: B^2/(2 mu_0) = 60^2 / (2 x 4pi x 10^-7) = 1.43 x 10^9 J/m^3
- Stored: 4.48 x 10^11 J = 448 GJ [Self-test: PASS]
- This is 12 orders of magnitude too small to change the ship's velocity

### 5. Waste-heat radiators (Stefan-Boltzmann thermal balance)

**Formula:**
```
P_waste = P_load / eta_conversion
T = (P_waste / (epsilon x sigma_SB x A))^(1/4)
```

**Computed values:**
- Panels: 20, each 52 m x 18 m, both faces
- Total area: 37,440 m^2 [Self-test: PASS]
- Emissivity: 0.92
- Graphite sublimation limit: 1900 K
- Design temperature: 1550 K

| beta | Load (W) | Waste (W) | T (K) | Status |
|------|----------|-----------|-------|--------|
| 0.10 | 1.44e9 | 2.32e9 | 1044 | OK |
| 0.50 | 3.60e9 | 5.80e9 | 1313 | OK |
| 0.56 | 4.11e9 | 6.63e9 | 1357 | OK |
| 0.90 | 7.74e9 | 1.25e10 | 1590 | OK |
| 0.99 | 8.95e9 | 1.44e10 | 1649 | OK |
| 1.00 | 9.09e9 | 1.47e10 | 1655 | OK |
| 1.50 | 1.68e10 | 2.72e10 | 1931 | OVER LIMIT |
| 2.00 | 2.77e10 | 4.47e10 | 2187 | OVER LIMIT |

- Round-trip: P = eps x sigma x A x T^4 recovers P [Self-test: PASS]
- Radiators FAIL above beta ~ 1.45 [Self-test: PASS]

### 6. Cryoplant (HTS coil refrigeration at 18 K)

**Formula:**
```
P_cryo = 740 MW (constant, independent of beta)
```

The cryoplant holds the 24 REBCO coils at 18 K. This is a constant overhead -- it does not scale with speed. At cruise, the coil AC losses (6.2 GW at beta=1) dominate the load.

- 4 cryo units, each 6 m diameter x 11 m long
- Cryoplant mass: 298,577 kg
- Power draw: 740 MW [Self-test: PASS (cruise_load includes cryo)]

### 7. Casimir negative-energy lattice (the only real exotic-energy source)

**Formula:**
```
rho = -pi^2 hbar c / (720 a^4)
E_cassette = rho x V_gap = rho x plate^2 x gap x n_gaps
E_total = E_cassette x 24 cassettes
```

**Computed values:**
- 24 cassettes, each 2.40 m x 2.40 m plates, 10 nm gap, 2.00 m stack
- Plates per cassette: 33,333,333
- Gap volume per cassette: 1.920 m^3
- Energy density at 10 nm: -4.33 x 10^4 J/m^3 [Self-test: PASS]
- Energy per cassette: -8.32 x 10^4 J
- Total onboard: -2.00 x 10^6 J (-2 MJ) [Self-test: PASS]
- Warp bubble demand at delta=1m: -3.36 x 10^46 J
- **Shortfall: 40 orders of magnitude** [Self-test: PASS]
- 1/a^4 scaling verified: rho(20nm)/rho(10nm) = 1/16 [Self-test: PASS]

### 8. Magnetic sail (the only credible way to stop)

**Formula:**
```
F = Cd x rho_ISM x v^2 x A_eff
t_half = M / (k x v0)         where k = Cd x n_ISM x m_p x A
t_stop = (M/k) x (1/v_f - 1/v_0)
```

**Computed values:**
- Loop radius: 1000 km, area: 3.14 x 10^12 m^2 [Self-test: PASS]
- Cd = 0.85, current: 1.6 MA, mass: 420,000 kg
- ISM density: 1.0 x 10^5 protons/m^3 (0.1/cm^3)

| beta | Drag (N) | Halving time | Stop time |
|------|----------|-------------|-----------|
| 0.1 | 4.0e5 | 300 yr | 30,000 yr |
| 0.5 | 1.0e7 | 60 yr | 30,000 yr |
| 1.0 | 4.0e7 | 30 yr | 30,000 yr |

- F scales as v^2: F(1.0) = 4 x F(0.5) [Self-test: PASS]
- Halving time = M/(k v0) [Self-test: PASS]
- Stop time ~ 30,000 yr -- the honest number [Self-test: PASS]
- Drag falls as v^2 -- the brake fades when you need it most

### 9. Photon brake (destination array)

**Formula:**
```
F = 2P_captured / c        (photon pressure, perfect reflector)
t = gamma x M x v / F
```

**Computed values:**
- At 0.02 ly from destination array: F = 6.67 x 10^8 N [Self-test: PASS]
- F <= 2P_tap/c (cannot exceed full beam pressure) [Self-test: PASS]
- Brake time at beta=0.5: 381 days [Self-test: PASS]
- Requires a destination array already in place at Proxima

### 10. ISM hazard (interstellar medium loading)

**Formula:**
```
N = n_ISM x pi x R^2 x distance
E_blast = N x m_p x c^2 x beta^2 / 2    (conservative floor)
```

**Computed values:**
- ISM density: 1.0 x 10^5 protons/m^3
- Bubble radius: 100 m
- Proxima crossing: N = 1.26 x 10^26 protons [Self-test: PASS]
- Blast at beta=0.5: 2.37 x 10^15 J (2.37 PJ) [Self-test: PASS]
- The true spectrum is worse -- this is a floor
- The wall collects them; they do not pass through

### 11. Gravitational clock drift (environmental time dilation)

**Formula:**
```
dtau/dt = sqrt(1 + 2 Phi / c^2)
drift = integral_0^D (rate(x) - rate_earth) dx / D x t_total
```

**Computed values:**
- Sol well: M_sun at AU
- Proxima well: 0.1221 M_sun at 0.0485 AU
- Galactic potential: Phi/c^2 = -1.0 x 10^-6 (common to both ends, cancels)
- Drift at beta=0.562: +2.35 s (crew age 2.35 s more than Earth) [Self-test: PASS]
- Ship self-gravity: -9.43 x 10^-22 (negligible, 12 orders below best clock) [Self-test: PASS]
- Warp interior is flat -- no dilation dividend [Self-test: PASS]

### 12. Energy conditions (NEC/WEC/DEC/SEC)

**Formula:**
```
beta < 1: NEC=WEC=DEC=SEC=True  (Bobrick-Martire / Fuchs et al. physical shell)
beta >= 1: NEC=WEC=DEC=SEC=False  (SSV theorem: ANY v > c warp violates NEC)
```

**Computed values:**
- At beta=0.5: all conditions satisfied, class=PHYSICAL [Self-test: PASS]
- At beta=1.5: all conditions violated, class=EXOTIC [Self-test: PASS]
- The SSV theorem (2022) is not about Alcubierre's ansatz -- it is about the whole class

### 13. Horizon lock (causal disconnection at superluminal speed)

**Formula:**
```
beta > 1 -> forward wall causally disconnected from interior
```

- At beta=0.99: static observer exists, steering works [Self-test: PASS]
- At beta=1.01: no static observer, helm locked [Self-test: PASS]
- Theorem: Everett 1996, Coule 1998, Krasnikov 1998
- The entire trajectory must be pre-laid before departure

### 14. Ford-Roman wall thickness limit (QI on the bubble wall)

**Formula:**
```
delta_max ~ 100 L_Planck / beta
```

- At beta=1: delta_max = 100 L_P = 1.62 x 10^-33 m [Self-test: PASS]
- Scales as 1/beta: delta(2) = delta(1)/2 [Self-test: PASS]
- At that thickness: E = 2.08 x 10^79 J = 10^9 universes [Self-test: PASS]
- Source: Ford & Roman 1996, Pfenning & Ford 1997

### 15. Antimatter store (peak fold transitions only)

**Formula:**
```
E = m x 2c^2 = 1.7975 x 10^17 J/kg  (matter + antimatter)
```

- 2 traps, 0.85 kg antihydrogen each
- Total: 1.7 kg antimatter
- Energy: 1.7 x 1.80 x 10^17 = 3.06 x 10^17 J
- Used only for peak fold transitions (bubble spinup/shutdown), not propulsion

### 16. Quantum teleportation (the real teleporter -- for contrast)

**Formula:**
```
bits = atoms x bits_per_atom = 7e27 x 100 = 7e29 bits
time = bits / channel_bps = 7e29 / 1e12 = 7e17 s
```

- State bits: 7.00 x 10^29 [Self-test: PASS]
- Time at 1 Tb/s: 2.22 x 10^10 yr = 1.61 universe ages [Self-test: PASS]
- FTL: False (classical channel capped at c) [Self-test: PASS]
- Destroys original: True (no-cloning theorem) [Self-test: PASS]
- Record: 1400 km (Micius satellite, 2017)
- Moves a quantum STATE, not matter

---

## Test results

### Self-test: 157 / 157 checks pass

```
python Warpdrive.py --selftest
```

Covers:
- Physical constants (CODATA 2018 / IAU 2015)
- Alcubierre shape function, derivative, energy density, integral
- Ford-Roman quantum inequalities and wall thickness limit
- Morris-Thorne wormhole (shape, flare-out, tidal, energy, proper length, tidal profile)
- MMP (2020) construction (charge, mass, traversal time)
- Visser thin-shell wormhole (shell mass, energy, horizon limit)
- Time dilation (lapse, gravitational, rocket, ship self-gravity)
- CTC / time-machine onset (gravity well, warp, rocket)
- Quantum teleportation facts
- ISM particles swept, blast energy
- Magsail drag, halving time, stop time
- Beam diffraction, capture, photon brake force and time
- Kinetic energy, SMES storage, fusion fuel, Stefan-Boltzmann radiator
- Energy ledger / conservation / Casimir
- Portal traversal (mouth clock rate, offset, CTC, tidal, QI)
- Ship and portal geometry
- Full flight simulation with honesty audit
- Formula-level proofs: every function verified against its closed-form expectation
- Cross-formula consistency: density x volume = energy, tidal = profile at throat, E = mc^2, beta^2 scaling, 1/delta scaling, gamma = 1/sqrt(1-beta^2), QI derivation, mouth rate = grav x kinematic
- Barrier engineering analysis: 8 barriers, each with exact value, threshold, gap, passability, and route assessment

### Portal traversal tests: 66 / 66 pass

Covers:
- Mouth clock rate (gravitational, kinematic, combined, monotonicity)
- Time offset (linear accumulation, sign, clock consistency)
- CTC onset (boundary, light-time, margin, onset time)
- Portal placement (WHERE: mouth separation, light-time, custom separation)
- Desynchronization (WHEN: gravity well, SR, warp vs rocket, same well, same speed)
- Survival (tidal: signal, person, object scaling, tiny/huge throat edge cases)
- Throat open (QI: hold time, traversal time, scaling, all sizes blocked)
- Exotic energy (sign, linear scaling, Casimir shortfall)
- CTC scenarios (no desync, small desync, large desync, warp, rocket, margin)
- Verdicts (QI block, tidal block, chronology block)
- Numerical consistency (clock identity, CTC onset, traversal formula)
- Edge cases (zero elapsed, same well, same speed, extreme throat sizes)
- Existing functions (ctc_by_gravity_well, ctc_by_warp_transport)

### Honesty layer: HONEST

```
VERDICT: HONEST -- nothing created from nothing.
```

Ten conservation checks run against the live state:
1. No over-unity (kinetic gained <= beam + regen)
2. Plant within rating
3. Fuel backs output
4. Exotic never supplied (owed, not credited)
5. Radiates only outward
6. NEC reported truthfully
7. Clocks agree (no dilation dividend)
8. Beam capture <= 1
9. All masses positive
10. Arrival requires stopping

---

## Portal traversal scenarios

Run `python Warpdrive.py --send` for the full report. Six scenarios:

| # | Payload | Mouth B | Offset | CTCs? | Blocked by |
|---|---------|---------|--------|-------|------------|
| 1 | Signal | Synced, 12 m gate | 0 | No | Quantum inequalities |
| 2 | Person | Synced, survivable | 0 | No | Quantum inequalities |
| 3 | Person | Phi/c^2 = -0.01, 1 yr | 3.7 days | No | Quantum inequalities |
| 4 | Person | Phi/c^2 = -0.2, 20 yr | 4.51 yr | Yes | Chronology protection |
| 5 | Person | Rocket beta=0.9, 10 yr | 5.64 yr | Yes | Chronology protection |
| 6 | Person | Warp beta=0.9, 10 yr | 0 | No | Quantum inequalities |

**Every scenario is blocked.** The portal is the warp drive's problem again, in a new shape, with a time machine on top.

### What GR lets you control

- **WHERE** (exit location): move mouth B. The wormhole connects A to B.
- **WHEN** (arrival time): desynchronize the mouths by parking B in a gravity well or moving it at relativistic speed. The offset accumulates linearly and is the same dilation GPS measures daily.
- **CTC onset**: when |offset| > D/c. Before that: B's past, not your past. After that: time machine.
- **Warp cannot desync**: a warp bubble's interior is flat, so a mouth carried by warp ages at the same rate as one at rest. The fast thing cannot build the causality violation.

---

## Physical constants

All values match CODATA 2018, IAU 2015, or exact SI definitions:

| Constant | Value | Source |
|----------|-------|--------|
| c | 2.99792458 x 10^8 m/s | exact (SI) |
| G | 6.67430 x 10^-11 m^3/kg/s^2 | CODATA 2018 |
| hbar | 1.054571817 x 10^-34 J s | exact (SI) |
| h | 6.62607015 x 10^-34 J s | exact (SI) |
| k_B | 1.380649 x 10^-23 J/K | exact (SI) |
| sigma_SB | 5.670374419 x 10^-8 W/m^2/K^4 | derived |
| e | 1.602176634 x 10^-19 C | exact (SI) |
| m_p | 1.67262192369 x 10^-27 kg | CODATA 2018 |
| m_e | 9.1093837015 x 10^-31 kg | CODATA 2018 |
| mu_0 | 1.25663706212 x 10^-6 H/m | CODATA 2018 |
| eps_0 | 8.8541878128 x 10^-12 F/m | CODATA 2018 |
| M_sun | 1.98847 x 10^30 kg | IAU 2015 |
| M_earth | 5.97217 x 10^24 kg | IAU 2015 |
| AU | 1.495978707 x 10^11 m | exact (IAU) |
| ly | 9.4607304725808 x 10^15 m | IAU 2015 |
| yr | 3.15576 x 10^7 s | IAU Julian year |

Derived: c^4/G = 1.21 x 10^44 N, Planck length = 1.616 x 10^-35 m, Planck mass = 2.176 x 10^-8 kg, Planck time = 5.391 x 10^-44 s. All verified.

---

## References

- Alcubierre, M. (1994) Class. Quantum Grav. 11 L73
- Ford, L. & Roman, T. (1996) Phys. Rev. D 53 5496
- Everett, A. (1996) Phys. Rev. D 53 7365
- Pfenning, M. & Ford, L. (1997) Class. Quantum Grav. 14 1743
- Coule, D. (1998) Class. Quantum Grav. 15 2523
- Van Den Broeck, C. (1999) Class. Quantum Grav. 16 3973
- Lamoreaux, S. (1997) Phys. Rev. Lett. 78 5 (Casimir, measured)
- Zubrin, R. & Andrews, D. (1991) J. Spacecraft 28 197 (magsail)
- Forward, R. (1984) J. Spacecraft 21 187 (staged sail braking)
- McMonigal, B., Lewis, G. & O'Byrne, P. (2012) Phys. Rev. D 85 064024
- Bobrick, A. & Martire, G. (2021) Class. Quantum Grav. 38 105009
- Santiago, J., Schuster, S. & Visser, M. (2022) CQG 39 075006
- Fuchs, J. et al. (2024) Class. Quantum Grav. 41 095013
- Morris, M. & Thorne, K. (1988) Am. J. Phys. 56 395 (wormholes)
- Morris, Thorne & Yurtsever (1988) PRL 61 1446 (time machine)
- Hawking, S. (1992) Phys. Rev. D 46 603 (chronology protection)
- Bennett, C. et al. (1993) PRL 70 1895 (quantum teleportation)
- Maldacena, Milekhin & Popov (2020) arXiv:1807.04726

## License

This is a physics simulation and educational tool. It does not claim that any of the speculative constructions (superluminal warp, traversable wormholes, time machines) are experimentally demonstrated or engineerable. Where the physics says impossible, the model says so and shows the computation.
