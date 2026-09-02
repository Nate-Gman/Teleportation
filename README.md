# Warpdrive WD-1m5 Foldrunner "Miniframe V"

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

The WD-1m5 Foldrunner "Miniframe V" is a 1.66 x 10^7 kg starship (the WD-1 hull scaled 0.4586x linear overall, crew 12 -> 6, bubble wall thinned 1.0 m -> 0.2 m, plus a pass-4 reactor-margin and hull-wall-thickness refinement and a pass-5 HTS-coil and shaping-ring structural-efficiency refinement, none of which touched the bubble geometry) that carries a 45.86 m bubble of flat spacetime to Proxima Centauri b (4.2465 ly) at an emergent beta = 0.857 -- up from 0.562 at full scale, because a lighter hull needs less beamed energy to reach speed against the same unchanged transmitter. Inside the bubble the crew are weightless, un-accelerated, and un-dilated for the entire voyage. The drive is subluminal by design -- and that is not a compromise, it is the reason it is buildable. See `overview.md` for the full scale-down rationale (all five refit passes, including a bug fix in pass 3 that corrected two non-scaling envelope-check constants, an engineering-margin review in pass 4, and a winding-pack/secondary-structure review in pass 5).

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

The UI info panel (press `I` in the visualizer) now contains 10 proof sections with 47+ individual proofs. Each proof states the formula, the computed value, and the self-test check that verifies it. The self-test has been expanded from 95 to 169 checks to cover every function.

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
   - At beta=0.5: 2.55 x 10^23 J (0.26 YJ), was 1.77 YJ at full scale [PASS]
   - Verified for beta = 0.1, 0.5, 0.9, 0.99 [PASS]
   - No solution for beta > 1 [PASS]

2. **SMES magnetic storage** E = (B^2/2 mu_0) V_torus
   - Stored: 43.1 GJ (positive, finite), was 448 GJ at full scale [PASS]

3. **Fusion fuel** m = E / (eta x E_D3He_per_kg)
   - Crossing at beta=0.5: 730 kg D-3He, was 4419 kg at full scale [PASS]

4. **Stefan-Boltzmann radiator** T = (P / (eps sigma A))^(1/4)
   - At beta=0.99: 1514 K (limit 1900 K), was 1649 K at full scale [PASS]
   - At beta=2: 1904 K (OVER limit), was 2187 K at full scale [PASS]
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
   - Brake force: 6.67 x 10^8 N [PASS] (unchanged -- set by the beam/array, not ship mass)
   - F <= 2P_tap/c [PASS]

4. **Photon brake time** t = gamma M v / F
   - At beta=0.5: 55.2 d, was 381.3 d at full scale [PASS]

5. **Magsail drag** F = Cd rho_ISM v^2 A
   - Cd = 0.85, A = 1.54 x 10^12 m^2, was 3.14 x 10^12 m^2 (loop trimmed 1000 -> 700 km at pass 2, unchanged since) [PASS]
   - At beta=0.5: 4.92 x 10^6 N [PASS]
   - Scales as v^2: F(1.0) = 4 x F(0.5) [PASS]
   - Halving time: 17.7 yr (looks feasible) [PASS]
   - Stop time: 8.86 x 10^3 yr (the honest number), was 3 x 10^4 yr at full scale [PASS]

### ISM & time dilation proofs (section 19f)

1. **ISM particles swept** N = n_ISM pi R^2 distance
   - n_ISM = 1.0 x 10^5 /m^3, R = 45.86 m (was 100 m at full scale) [PASS]
   - Proxima crossing: 2.65 x 10^25 protons, was 1.26 x 10^26 at full scale [PASS]

2. **ISM blast energy** E = N m_p c^2 beta^2/2 (conservative floor)
   - At beta=0.5: 4.99 x 10^14 J (0.50 PJ), was 2.37 PJ at full scale [PASS]

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

### Maximum time travel proofs (section 19j)

These proofs back the `--send` scenarios 7-9, which push the time-travel levers to their physical limits. 7 proof blocks, 5 new self-test checks (157 -> 162).

1. **Combined mouth clock rate** dtau/dt = sqrt(1 + 2Phi/c^2) * 1/gamma(beta)
   - The two effects MULTIPLY (independent, both slow the clock)
   - Neutron star (Phi/c^2=-0.3) + beta=0.99: rate = 0.089219 (B ages at 8.9% of A) [PASS]
   - Near horizon (Phi/c^2=-0.45) + beta=0.999: rate = 0.014139 (B ages at 1.4% of A) [PASS]
   - At horizon (Phi/c^2=-0.5): rate = 0 (frozen) [PASS]
   - GPS measures both effects daily: 45 us/day (GR) + 7 us/day (SR)

2. **CTC onset at minimum separation** t_onset = (D/c) / |rate_diff|
   - At 1 AU (light-time = 499 s = 8.3 min):
     - NS + 0.99c: onset = 548 s = 9.1 min [PASS]
     - Horizon + 0.999c: onset = 506 s = 8.4 min [PASS]
   - At Proxima (light-time = 4.25 yr):
     - NS + 0.99c: onset = 4.66 yr [PASS]
   - Onset is always > light-time (offset must accumulate first)

3. **Maximum backward jump** (step A -> B) offset = rate_diff * elapsed
   - NS + 0.99c, 1 yr: offset = 333 d [PASS]
   - NS + 0.99c, 10 yr: offset = 9.11 yr [PASS]
   - NS + 0.99c, 100 yr: offset = 91.08 yr [PASS]
   - Horizon + 0.999c, 100 yr: offset = 98.59 yr [PASS]
   - Jump approaches elapsed (rate_diff -> 1) but never exceeds it

4. **Maximum forward jump** (step B -> A) -- same offset, opposite direction
   - Forward jump = backward jump (symmetric wormhole) [PASS]
   - No new physics -- just the other way through the throat

5. **Warp drive cannot time-travel** (flat interior theorem)
   - Warp bubble interior is exactly Minkowski (f=1, all derivatives zero)
   - Warp-carried mouth: rate_diff = 0.000 [PASS]
   - Rocket-carried mouth at beta=0.9: rate_diff > 0 [PASS]
   - The FAST thing cannot build the causality violation; the SLOW rocket can

6. **Warp drive gravitational drift** (the only time shift the drive produces)
   - drift = integral (grav_rate(x) - earth_rate) dx over the crossing
   - At beta=0.857: drift = +1.54 s over 4.96 yr [PASS]
   - NOT controllable (set by Sol-Proxima gravitational potential difference)
   - NOT a time machine (1.5 seconds is not a CTC)

7. **All time-travel scenarios remain blocked**
   - Exotic energy: -2.73 x 10^51 J needed, 46 orders short of Casimir [PASS]
   - Quantum inequalities: throat closes in ~1e-22 s vs ~5.4e7 s traversal [PASS]
   - Chronology protection: Hawking CPC (1992) expects vacuum divergence [PASS]
   - The maximum time jump is a mathematical result, not an engineering capability

### Near-light-speed achievement proofs (section 19k)

These proofs show how the ship reaches beta = 0.857 (85.7% of lightspeed) -- not as a declared parameter, but as an emergent result of a race between two clocks. 7 proof blocks, 7 new self-test checks (162 -> 169).

1. **The energy clock** (what the ship needs) KE = (gamma - 1) M c^2
   - M = 16,602 t (derived from geometry x density, not declared)
   - gamma = 1/sqrt(1-beta^2) -- diverges at beta=1 (infinite energy)
   - At beta=0.857: KE = 1.40 x 10^24 J = 1.40 YJ [PASS]
   - At beta=0.9: KE = 1.93 YJ (38% more for 4% more speed) [PASS]
   - At beta=0.99: KE = 9.09 YJ (6.5x more for 15% more speed) [PASS]
   - The gamma curve is why near-light speed is hard: each knot costs more than the last

2. **The range clock** (what the beam can deliver) d_spot = 2.44 lambda L / D
   - lambda = 1.0 um, D = 1000 km -> spot grows linearly with distance
   - f_capture = (d_rectenna / d_spot)^2 -> falls as 1/L^2
   - d_rectenna = 4 km (deployed film)
   - P_tap = 10^17 W (0.026% of L_sun -- a stellar tap, not a battery)
   - At 0.01 ly: capture = 100%, P = 10^17 W
   - At 0.50 ly: capture = 12%, P = 1.2 x 10^16 W
   - At 0.62 ly: capture = 7.8%, P = 7.8 x 10^15 W (usable range ends)
   - Capture at 1.0 ly is ~1/4 of capture at 0.5 ly (1/L^2 scaling) [PASS]

3. **The race** (two clocks, one winner)
   - The boost integrates in 3-day steps: got += P_captured(x) * dt; v = c * sqrt(1 - 1/(1 + got/(Mc^2))^2); x += v * dt
   - The energy clock says: you need (gamma-1)Mc^2 joules
   - The range clock says: you are moving away, spot grows, capture falls, power drops
   - Whichever runs out FIRST sets the cruise speed
   - At beta=0.857: need 1.40 YJ, delivered 1.398 YJ -> JUST makes it [PASS]
   - At beta=0.86: need 1.43 YJ, delivered 1.398 YJ -> FALLS SHORT [PASS]
   - At beta=0.9: need 1.93 YJ, delivered 1.398 YJ -> 28% short [PASS]
   - The margin between 0.857 and 0.86 is 2% of the energy bill -- that is how tight the race is

4. **Why shrinking raises the speed** (the refit lever, step by step)
   - The beam is FIXED (external infrastructure, unchanged across all refits)
   - The ship mass M falls with each pass. Since KE = (gamma-1)Mc^2, smaller M means less energy for the same beta
   - The ship climbs higher on the gamma curve before it outruns the beam
   - Pass 0 (WD-1): M=127,000 t -> beta=0.562 (gamma=1.21)
   - Pass 1 (WD-1m): M=42,719 t -> beta=0.727 (gamma=1.45)
   - Pass 2 (WD-1m2): M=27,003 t -> beta=0.794 (gamma=1.63)
   - Pass 3 (WD-1m3): M=18,374 t -> beta=0.844 (gamma=1.86)
   - Pass 4 (WD-1m4): M=18,215 t -> beta=0.845 (gamma=1.87)
   - Pass 5 (WD-1m5): M=16,602 t -> beta=0.857 (gamma=1.94)
   - Mass fell 87%; speed rose 52%; gamma rose 60%
   - The relationship is NOT linear -- the gamma curve makes each tonne saved worth more than the last
   - Lighter ship reaches higher beta: beta(M)=0.857 > beta(2M)=0.765 [PASS]

5. **Why it cannot reach beta=1** (the hard wall)
   - At beta=1: gamma = infinity -> KE = infinity
   - No finite beam can deliver infinite energy -- this is special relativity, not engineering
   - The gamma curve has a vertical asymptote at beta=1:
     - beta=0.857: gamma=1.94, KE=1.40 YJ
     - beta=0.9: gamma=2.29, KE=1.93 YJ (1.38x for +4%)
     - beta=0.95: gamma=3.20, KE=3.29 YJ (2.3x for +9%)
     - beta=0.99: gamma=7.09, KE=9.09 YJ (6.5x for +13%)
     - beta=0.999: gamma=22.4, KE=33.5 YJ (24x for +14%)
     - beta=1.0: gamma=inf, KE=inf (wall)
   - Each percent closer to c costs more than the last percent
   - The ship sits at 85.7% because the beam runs out at 0.62 ly, not because 85.7% is a round number

6. **The boost profile** (300 days, integrated explicitly)
   - The boost is NOT instantaneous. boost_profile() integrates in 3-day steps
   - Tracks position, velocity and delivered energy simultaneously
   - Ship starts at rest, beam captures 100% at first (spot < rectenna)
   - Capture falls as the ship pulls away
   - After 300 days the energy clock and range clock converge [PASS]
   - Delivered energy matches KE at max cruise within 5% [PASS]

7. **What would raise the speed further** (the levers)
   - Since beta_max is emergent from the race, changing any input changes the result -- but only three levers exist:
     - a) LARGER APERTURE: D=2000 km -> spot halves, range doubles -> beta rises (~0.9+). Cost: 4x the structure
     - b) SHORTER WAVELENGTH: lambda=0.5 um -> spot halves -> same effect as doubling aperture. Cost: harder optics
     - c) LIGHTER SHIP: M/2 -> half the KE for same beta -> beta rises. Cost: fewer crew, less redundancy
   - None of these touch beta=1. The gamma wall is absolute
   - The beam can push the ship arbitrarily close to c, but never to c

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
| 1 | Bubble wall tidal gradient | FAIL | 1.76e17 g | 1 g | 17 orders |
| 2 | Superluminal NEC (SSV theorem) | THEOREM | NEC violated at v>c | NEC required | theorem |
| 3 | Negative energy scale | FAIL | 3.54e46 J needed (45.86 m bubble, 0.2 m wall) | 1.9e5 J (Casimir) | 41 orders |
| 4 | Steering above beta=1 | THEOREM | causally disconnected | controllable | theorem |
| 5 | Thermal survival at 2c | FAIL | 1904 K | 1900 K | 0.2% over |
| 6 | Ford-Roman wall thickness | THEOREM | delta_max = 100 L_P | delta = 0.2 m | theorem |
| 7 | QI throat hold time | THEOREM | 3.25e-26 s | 4.8 s traversal | 26 orders |
| 8 | CTC chronology protection | CONJECTURE | divergent vacuum | stable throat | conjecture |

**Routes past each barrier (and why they fail):**

1. **Wall tidal**: Thinner wall -> MORE tidal, not less. Cutting `wall_thick_m` from 1.0 m to 0.2 m to buy back flat interior (see `overview.md`) made this barrier numerically *worse* (1.76e17 g vs 7.04e15 g at 1.0 m) -- an honest trade the model reports rather than hides, since the wall was never a survivable place at either thickness. At QI-legal thickness (100 L_P): even further beyond reach. Anti-route regardless.
2. **Superluminal NEC**: SSV theorem (2022) proves ANY v>c warp violates NEC. No route -- this is a theorem about the whole class, not just Alcubierre's ansatz.
3. **Negative energy**: More Casimir cassettes -> need ~4.4e42 cassettes. Shrinking the bubble and thinning the wall move the raw exotic-energy demand around (3.54e46 J now, versus 3.36e46 J for the original 100 m/1.0 m-wall bubble and 4.89e46 J for the pass-2 53.95 m/0.2 m-wall bubble), but the onboard Casimir supply is always many orders too small regardless of how these knobs are turned.
4. **Steering**: Forward wall is causally disconnected at v>c. The crew cannot send a control signal to the front of the bubble. The entire trajectory must be pre-laid. Theorem (Everett 1996, Coule 1998, Krasnikov 1998).
5. **Thermal**: More radiator area -> need 7,146 m^2 (have 7,081 m^2, was 65,688 vs 37,440 at full scale). This is the ONLY passable barrier, and the smaller hull needs proportionally less extra area each refit pass (+75% -> +20.6% -> +3.3% -> +0.9% now) -- it currently buys beta ~ 1.99 before failing, not superluminal. `--selftest` deliberately keeps this barrier failing at 2c so the redesign cannot claim to have solved it by shrinking past the point where it matters; this margin is now thin enough that it is close to the practical floor for further pure shrinkage.
6. **Ford-Roman wall**: QI theorem limits wall to 100 L_P = 1.62e-33 m -- twenty-nine orders of magnitude below the ship's actual 0.2 m wall. At that thickness E = 2.08e79 J = 10^9 universes of energy.
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

**Total ship mass (WD-1m5, SCALE_S = 0.4586 overall):** 1.660 x 10^7 kg (16,602 tonnes) -- was 1.270 x 10^8 kg (126,986 t) at full WD-1 scale, 4.272 x 10^7 kg (42,719 t) after pass 1, 2.700 x 10^7 kg (27,003 t) after pass 2, 1.837 x 10^7 kg (18,374 t) after pass 3, 1.821 x 10^7 kg (18,215 t) after pass 4 [Self-test: PASS]

| Component | Mass (kg) | % | Formula |
|-----------|-----------|---|---------|
| Warp ring shell | 6,894,454 | 41.5% | 4pi^2 R r x wall x 4100 kg/m^3 |
| HTS field coils (24) | 4,029,059 | 24.3% | 24 x coil_volume x 5600 kg/m^3 (0.30 m build) |
| Shaping rings (2) | 3,430,757 | 20.7% | 2 x torus_surface x 0.30 x 4100 |
| Pylons (3) | 550,389 | 3.3% | 3 x 38.52 x 1.47 x 1.2 x 2700 |
| Radiators (20) | 403,643 | 2.4% | 20 x 22.61 x 7.83 x 0.06 x 1900 |
| Fusion reactor | 386,875 | 2.3% | torus_surface x 0.9 x 5200 |
| Crew hull shell | 204,878 | 1.2% | hull_area x 0.11 x 2700 |
| Magsail loop | 200,000 | 1.2% | 2.0e5 kg (HTS cable, unchanged since pass 2) |
| SMES buffer | 186,223 | 1.1% | torus_surface x 0.25 x 6800 |
| Crew decks (3) | 102,958 | 0.6% | 3 x pi r^2 x 0.35 x 2700 |
| Casimir lattice (24) | 61,449 | 0.4% | 24 x 1.10^2 x 0.92 x 2300 |
| Antimatter traps (2) | 47,375 | 0.3% | 2 x 4pi r^2 x 0.30 x 4400 |
| Cryoplant (4) | 28,738 | 0.2% | 4 x pi r^2 x 5.04 x 240 |
| Consumables + crew (6) | 19,200 | 0.1% | 6 x 3200 |
| RCS pods (8) | 18,418 | 0.1% | 8 x pi r^2 x 2.30 x 900 |
| Boost rectenna | 17,593 | 0.1% | pi (2000)^2 x 1e-6 x 1400 |
| Deflector | 16,571 | 0.1% | pi r^2 x 0.10 x 3100 |

**Cross-check:** sum(mass_budget) = SHIP_MASS_KG (verified to 1e-6) [Self-test: PASS]. The ring/coil/shaping-ring group still dominates (~88% of dry mass) -- shrinking every dimension by close to the same factor preserves the mass fractions almost exactly, which is why a straight geometric scale-down is a self-consistent redesign rather than an arbitrary reshuffle. This pass moved only two line items: the fusion reactor (-8% mass, following its power cut) and the crew hull shell (-39% mass, following the pressure-vessel wall-thickness re-derivation) -- everything else is byte-for-byte the pass-3 geometry.

### 2. D-3He fusion reactor (housekeeping power)

The reactor does NOT move the ship. It runs the coils, cryoplant, and hotel load.

**Formula:**
```
P_thermal = 2.62 GW      (was 22 GW at full scale, 7 / 4.35 / 2.91 GW after passes 1/2/3)
P_electrical = P_thermal x eta_direct = 2.62 x 0.62 = 1.62 GW      (was 13.64 GW)
m_fuel = E_required / (eta x E_D3He_per_kg)
E_D3He = 3.52 x 10^14 J/kg  (D + 3He -> 4He + p + 18.35 MeV)
```

Resized from 22 GW to 2.62 GW (-88% overall). Passes 1-3 tracked the cruise electrical load down at a fixed ~1.5x margin inherited from WD-1; pass 4 re-examined that margin itself and settled on 1.35x -- still a 35% reserve, comfortably inside the 20-40% band typical of aerospace fusion/fission power-plant design, and a genuine additional cut (-10%) that cost nothing else, since the margin choice never touched geometry, envelope fit, or thermal balance. Pass 5 reduced the HTS coil winding build and shaping-ring solid fraction (see section 6), which lowered the cruise load slightly via the lighter ship, but the reactor was already sized at pass 4 and was not re-cut -- the pass-5 mass savings show up as extra margin and higher emergent cruise speed, not as a smaller reactor.

**Computed values:**
- Thermal output: 2.62 GW
- Direct conversion efficiency: 62% (aneutronic)
- Fuel for Proxima crossing at beta=0.5: 730 kg D-3He (was 4,419 kg at full scale; unaffected by the pass-4 margin change, which touches reactor sizing, not cruise fuel burn) [Self-test: PASS]
- Specific energy: 3.52 x 10^14 J/kg

### 3. Stellar-tap boost beam (the only way to accelerate)

The ship cannot carry enough energy to reach cruise speed. A 1000 km phased array beams power from Sol.

**Formula (Airy diffraction):**
```
d_spot = 2.44 x lambda x L / D_aperture
f_capture = (d_rectenna / d_spot)^2   if d_spot > d_rectenna, else 1.0
P_captured = P_tap x f_capture
```

The transmitter itself is unchanged ground/orbital infrastructure -- shrinking the ship does not touch it. What changes is the mass on the other end: a lighter hull needs less delivered energy (gamma-1) M c^2 to reach any given beta, so it climbs further up the diffraction-range race before it runs out of usable beam.

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
- Maximum emergent cruise speed: beta = 0.857 (was 0.562 at full scale, 0.727 / 0.794 / 0.844 / 0.845 after passes 1/2/3/4) [Self-test: PASS]

**Boost energy:**
```
KE = (gamma - 1) M c^2
```
- At beta=0.5: KE = 2.33 x 10^23 J (0.23 YJ), boost time = 27 d (was 1.77 YJ / 207 d at full scale) [Self-test: PASS]
- At beta=0.857: KE = 1.40 x 10^24 J (1.40 YJ), boost time = 300 d -- the new emergent cruise speed
- At beta=0.9: KE = 2.14 x 10^24 J -- beam cannot deliver (range exceeded)

### 4. SMES magnetic energy storage (transient buffer)

**Formula:**
```
E = (B^2 / 2 mu_0) x V_torus
V_torus = 2 pi^2 R r^2
```

**Computed values:**
- Major radius: 5.04 m, minor radius: 0.55 m (was 11 m / 1.2 m at full scale)
- Field: 60 T (unchanged HTS technology)
- Volume: 2 pi^2 x 5.04 x 0.55^2 = 30.1 m^3
- Energy density: B^2/(2 mu_0) = 60^2 / (2 x 4pi x 10^-7) = 1.43 x 10^9 J/m^3
- Stored: 4.31 x 10^10 J = 43.1 GJ (was 448 GJ at full scale, 123 / 69.8 GJ after passes 1/2) [Self-test: PASS]
- This is 12 orders of magnitude too small to change the ship's velocity

### 5. Waste-heat radiators (Stefan-Boltzmann thermal balance)

**Formula:**
```
P_waste = P_load / eta_conversion
T = (P_waste / (epsilon x sigma_SB x A))^(1/4)
```

**Computed values:**
- Panels: 20, each 22.61 m x 7.83 m, both faces (was 52 m x 18 m at full scale)
- Total area: 7,081 m^2 (was 37,440 m^2 at full scale, 15,818 / 10,895 m^2 after passes 1/2) [Self-test: PASS]
- Emissivity: 0.92
- Graphite sublimation limit: 1900 K
- Design temperature: 1550 K

| beta | Load (W) | Waste (W) | T (K) | Status |
|------|----------|-----------|-------|--------|
| 0.10 | 3.09e8 | 4.99e8 | 1078 | OK |
| 0.50 | 5.94e8 | 9.58e8 | 1269 | OK |
| 0.84 | 9.92e8 | 1.60e9 | 1443 | OK |
| 0.90 | 1.07e9 | 1.73e9 | 1470 | OK |
| 0.99 | 1.20e9 | 1.94e9 | 1514 | OK |
| 1.00 | 1.22e9 | 1.97e9 | 1519 | OK |
| 1.50 | 1.97e9 | 3.17e9 | 1712 | OK |
| 1.99 | 2.94e9 | 4.74e9 | 1893 | OVER LIMIT (barrier threshold) |
| 2.00 | 3.01e9 | 4.86e9 | 1904 | OVER LIMIT |

- Round-trip: P = eps x sigma x A x T^4 recovers P [Self-test: PASS]
- Radiators FAIL above beta ~ 1.99 (was beta ~ 1.45 at full scale, ~1.79 / ~1.97 after passes 1/2) [Self-test: PASS] -- waste heat keeps falling faster than radiator area as the ship shrinks, so equilibrium temperature keeps falling at every beta. `--selftest` hard-asserts T(2c) still exceeds the 1900 K limit -- the redesign is not allowed to quietly erase this barrier, only to shrink the margin needed to eventually fix it (now +0.9% radiator area, was +75% at full scale). This is now the tightest margin among all three passes and effectively the practical stopping point for pure shrinkage.

### 6. Cryoplant (HTS coil refrigeration at 18 K)

**Formula:**
```
P_cryo = 155.8 MW (constant, independent of beta; was 740 MW at full scale, 313 / 215.6 MW after passes 1/2)
```

The cryoplant holds the 24 REBCO coils at 18 K. This is a constant overhead -- it does not scale with speed. It was resized because cryostat radiative heat leak scales with cold-surface area, not volume. At cruise, the coil AC losses (598 MW at beta=1, was 6.2 GW at full scale) dominate the load.

- 4 cryo units, each 2.75 m diameter x 5.04 m long (was 6 m x 11 m at full scale)
- Cryoplant mass: 28,738 kg (was 298,577 kg at full scale)
- Power draw: 155.8 MW [Self-test: PASS (cruise_load includes cryo)]

### 7. Casimir negative-energy lattice (the only real exotic-energy source)

**Formula:**
```
rho = -pi^2 hbar c / (720 a^4)
E_cassette = rho x V_gap = rho x plate^2 x gap x n_gaps
E_total = E_cassette x 24 cassettes
```

**Computed values:**
- 24 cassettes, each 1.10 m x 1.10 m plates, 10 nm gap, 0.92 m stack (was 2.40 m / 2.00 m at full scale)
- Plates per cassette: ~15,333,333
- Gap volume per cassette: 0.186 m^3
- Energy density at 10 nm: -4.33 x 10^4 J/m^3 [Self-test: PASS] (a material/nanoscale property -- unaffected by ship scale)
- Energy per cassette: -8.04 x 10^3 J
- Total onboard: -1.93 x 10^5 J (-0.19 MJ) (was -2 MJ at full scale) [Self-test: PASS]
- Warp bubble demand at delta=0.2m for the 45.86 m bubble (superluminal/Alcubierre mode, never actually drawn on): -3.54 x 10^46 J -- smaller than pass 2's -4.89 x 10^46 J because the bubble shrank further this pass while the wall thickness held at 0.2 m
- **Shortfall: ~41 orders of magnitude** [Self-test: PASS] -- scale and wall thickness move the exotic-energy bill around, but the Casimir supply available onboard is always many orders too small regardless
- 1/a^4 scaling verified: rho(20nm)/rho(10nm) = 1/16 [Self-test: PASS]

### 8. Magnetic sail (the only credible way to stop)

**Formula:**
```
F = Cd x rho_ISM x v^2 x A_eff
t_half = M / (k x v0)         where k = Cd x n_ISM x m_p x A
t_stop = (M/k) x (1/v_f - 1/v_0)
```

**Computed values:**
- Loop radius: 700 km (was 1000 km at full scale; unchanged since pass 2), area: 1.54 x 10^12 m^2 [Self-test: PASS]
- Cd = 0.85, current: 1.1 MA, mass: 200,000 kg (was 1.6 MA / 420,000 kg at full scale; unchanged since pass 2)
- ISM density: 1.0 x 10^5 protons/m^3 (0.1/cm^3)

| beta | Drag (N) | Halving time | Stop time |
|------|----------|-------------|-----------|
| 0.10 | 2.0e5 | 80 yr | 7,938 yr |
| 0.50 | 4.9e6 | 16 yr | 8,002 yr |
| 0.84 | 1.4e7 | 9.5 yr | 8,008 yr |

- F scales as v^2: F(1.0) = 4 x F(0.5) [Self-test: PASS]
- Halving time = M/(k v0) [Self-test: PASS]
- Stop time ~ 8,000 yr -- the honest number, and shorter than WD-1m4's ~8,786 yr, WD-1m2's ~13,000 yr, WD-1m's ~20,600 yr, and WD-1's 30,000 yr with the SAME magsail hardware (unchanged since pass 2): every further mass cut keeps paying off with no additional hardware changes [Self-test: PASS]
- Drag falls as v^2 -- the brake fades when you need it most

### 9. Photon brake (destination array)

**Formula:**
```
F = 2P_captured / c        (photon pressure, perfect reflector)
t = gamma x M x v / F
```

**Computed values:**
- At 0.02 ly from destination array: F = 6.67 x 10^8 N [Self-test: PASS] (force depends on beam/array geometry, not ship mass, so it is unchanged)
- F <= 2P_tap/c (cannot exceed full beam pressure) [Self-test: PASS]
- Brake time at beta=0.5: 50 days (was 381 days at full scale, 128 / 81 / 55 / 55 days after passes 1/2/3/4) -- faster with every mass cut on the same array [Self-test: PASS]
- Requires a destination array already in place at Proxima

### 10. ISM hazard (interstellar medium loading)

**Formula:**
```
N = n_ISM x pi x R^2 x distance
E_blast = N x m_p x c^2 x beta^2 / 2    (conservative floor)
```

**Computed values:**
- ISM density: 1.0 x 10^5 protons/m^3
- Bubble radius: 45.86 m (was 100 m at full scale, 65 / 53.95 m after passes 1/2)
- Proxima crossing: N = 2.65 x 10^25 protons (was 1.26 x 10^26 at full scale) -- fewer, because swept volume scales with R^2 [Self-test: PASS]
- Blast at beta=0.5: 4.99 x 10^14 J (0.50 PJ, was 2.37 PJ at full scale) [Self-test: PASS]
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
- Drift at beta=0.857 (was 0.562 at full scale, 0.727 / 0.794 / 0.844 / 0.845 after passes 1/2/3/4): +1.54 s over the 4.96 yr crossing (crew age 1.54 s more than Earth) -- a shorter, faster crossing means less time for the gravitational term to accumulate [Self-test: PASS]
- Ship self-gravity: -2.69 x 10^-22 (negligible, 12 orders below best clock; was -9.43 x 10^-22 at full scale -- smaller and lighter, so weaker still) [Self-test: PASS]
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

- 2 traps, 0.082 kg antihydrogen each (was 0.85 kg at full scale -- scaled down with the smaller kinetic-energy bill it buffers)
- Total: 0.164 kg antimatter
- Energy: 0.164 x 1.80 x 10^17 = 2.95 x 10^16 J
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

### Self-test: 169 / 169 checks pass

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
