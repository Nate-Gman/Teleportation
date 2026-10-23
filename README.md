# Warpdrive WD-1u4 Foldrunner

A physics-honest digital twin of a warp-drive starship, a traversable wormhole portal, and the time machine that any wormhole automatically becomes. Every number is computed from the real general-relativity and quantum-field-theory formulas. Where the physics says "impossible," the model says so and shows the computation that proves it.

**100% non-fiction -- what that means here.** Every component in the model is real hardware with a real function: there are no props, no easter eggs, no decorative parts that do nothing. Every subsystem carries a derived mass share, a power draw, a duty cycle, a failure mode and a buildability rating -- generated from the ledgers, and enforced by the selftest (a part missing any of them is a failing check, not a style slip). Barriers are reported as quantified engineering requirements -- energy bills in joules, material quantities in tonnes, timescales in years -- not waved through and not hidden. The car-scale WD-88 Field Car is held to the same standard: its cabin Y-manifold is a working pulse-distribution node, its 88 mph is an engineered arming setpoint, and every one of its 18 parts does the job its spec card claims.

## Quick start

```
python Warpdrive.py                  # interactive 3D viewer (needs pygame)
python Warpdrive.py --selftest       # 417 physics checks
python Warpdrive.py --spec           # component-by-component spec sheet
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

The WD-1u4 Foldrunner is a 1.082 x 10^9 kg starship (the WD-1 hull scaled 1.8344x linear overall -- pass 7 upscaled every component ~2x linear from the pass-6 design: crew 24, 96 ring sectors/coils, 12 decks, 60 radiator panels, 16 cryoplant units, 96 Casimir cassettes, 8 antimatter traps, 32 RCS pods, and a 102.7 GW D-3He reactor, with the external beam tap raised to 6.4 EW to carry the ~8.6x heavier hull) that carries a 183.44 m bubble of flat spacetime to Proxima Centauri b (4.2465 ly) at an emergent beta = 0.855 -- up from 0.562 at full scale. Inside the bubble the crew are weightless, un-accelerated, and un-dilated for the entire voyage. The drive is subluminal by design -- and that is not a compromise, it is the reason it is buildable. See `overview.md` for the full rescale rationale (all seven passes: the five Miniframe scale-downs, then the pass-6 and pass-7 x2 upscales with every component re-specified).

The model also computes, honestly and with full provenance:

- The Alcubierre superluminal metric and why it is unfunded (negative energy, 38+ orders short).
- The Morris-Thorne traversable wormhole and why it is unbuilt (exotic energy, tidal forces, quantum inequalities).
- The Maldacena-Milekhin-Popov (2020) construction and why it needs unobserved magnetic monopoles.
- The Visser thin-shell wormhole and why concentrating exotic matter costs more, not less.
- The closed-timelike-curve time machine that any wormhole automatically becomes, and Hawking's chronology protection conjecture.
- Quantum teleportation and why it is not a portal (state transfer, not matter; classical channel capped at c).
- The interstellar-medium hazard, magsail braking, photon braking, radiator limits, and the beam-delivered speed limit.

## Interactive viewer

Six tabs (click the tab, or press TAB to cycle):

| Tab | What it shows |
|-----|---------------|
| SHIP | The starship: ring, hull, radiators, reactor, coil sequence |
| METRIC | The warp bubble: York expansion grid, energy-density hotspots |
| DILATION | Clock rates: comoving vs static, gravitational drift |
| PORTAL | The wormhole: throat, flare-out, tidal profile, both mouths |
| FLIGHT | Flight sim: boost, cruise, brake, arrival (keys G/K/J/T, clickable chips) |
| SPECIAL WORKS | The WD-88 Field Car: the entire drive folded into a 4.40 m road car that transitions at exactly 88 mph (RUN 88 / BRAKE / PARK / FAULT chips, W/S or arrows to drive, `,`/`.` speed nudge, `[`/`]` hop duration) |

All on-screen chips are clickable: the mode tabs, FULL/EXPLODED/ASSEMBLY/
SECTION/LABELS view chips, and the FLIGHT control strip (SHELL, DEST ARRAY,
ALCUBIERRE, BOOST, BRAKE, WARP -/+, RESET, TEST).

Press **I** for the full specification panel -- 39 sections including 10 math proof sections, the component-by-component breakdowns (15b/15c) that explain every part of the ship: role, spec, mass share, power draw, failure mode and buildability rating, every specification key verbatim (15d), every runtime state field plus the complete controls (15e), every public function in the model (15f), and the Field Car's own two sections (20b/20c: the car-scale system map and the same-road-spot ephemeris, derived live). Press **H** for controls. Press **PgUp/PgDn** to scroll.

The same component detail is written to `Infornmational.md`, generated from the live ledgers by `python _gen_info.py` so it cannot drift away from the ship.

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

The UI info panel (press `I` in the visualizer) now contains 39 sections -- 10 proof sections with 47+ individual proofs, component-by-component breakdowns (15b/15c) generated live from the mass, buildability and operations ledgers, every DIMS/PLANT/DRIVE key with its source comment (15d), the full WarpCore/Voyage runtime state, envelope check, controls and CLI (15e), the complete model function registry (15f), and the Field Car sections 20b/20c (the car-scale system map and the full same-road-spot ephemeris with the frame-carrying heading solve). The same data plus the barrier table, feasibility scorecard, honesty-audit checks, portal constructions, time-machine constructions, traversal tests, clock ledger, fuel economy, the mesh budget, module tables, the self-test coverage map, every hover spec-card, and the complete info-panel text verbatim (all 39 sections, all proofs) is emitted to `Infornmational.md` via `python _gen_info.py`. Each proof states the formula, the computed value, and the self-test check that verifies it. The self-test has been expanded from 95 to 417 checks, including 34 numerical-stability edge-case tests, 13 amplification-mechanism tests (chained wormholes, nested wormholes, Tipler cylinder, Gott cosmic strings, Kerr CTC, max-displacement), 23 multi-jump ledger tests (cycle time, breakeven fixed point, backward/forward recurrences, ISM scoop flux, isotope yield, sustainability, fuel-out detection), 30 hostile-input regression tests (zero/negative walls and throats, out-of-domain separations and masses, signed-|beta| superluminal guards, direction validation, rate-diff and body-size clamping), 1 cross-integrator consistency test pinning the voyage boost lock to the `boost_profile` ceiling, 8 TEST-mode demo state-machine tests, and 30+ Field Car checks (exact 88 mph trigger, derived mass/power/ops ledgers, live thermal balance, injected fault fidelity, hostile speed/thermal/ephemeris inputs, pole and 32,000-year solves, lane-heading carry, and hostile build-detail factors).

## Hostile-input hardening (post-stress)

A dedicated fuzz pass (`_fuzz_stress.py`, `_fuzz_props.py` — kept in the repo) hit every physics function with zero, negative, extreme, and boundary inputs across ~4,000 randomized runs. Findings fixed:

| Input | Was | Now |
|-------|-----|-----|
| `warp_energy_integral(delta=0)` | NaN (`inf·0`) | exact razor-wall value ~R²σ/3 (sqrt(h) folded inside the square — d² overflowed before h divided back) |
| `warp_energy_integral(samples<2)` | ZeroDivisionError | clamped to ≥2 |
| `wall_tidal_gradient(delta=0)` | ZeroDivisionError | `inf` (divergent shear); `beta=0` → `0` |
| `mt_throat_density(0)` | ZeroDivisionError | `-inf` |
| `mt_exotic_energy_j(0)` | ZeroDivisionError | `0` (closed form −c⁴b0/6G; volume vanishes faster than density diverges) |
| `mt_exotic_energy_j(b0<0)` | positive energy (!) | `0` — sign can never invert |
| `mt_tidal_g(0)` | ZeroDivisionError | `inf` |
| `mt_proper_length(0)` | ZeroDivisionError | `0` |
| `portal_traversal(b0=0)` | crash | full verdict dict (`survives_tidal=False`) |
| `mouth_sep_m<0` in cycle/CTC | negative times | clamped to 0 |
| `multijump direction` unknown | silently "forward" | `ValueError` — loud failure |
| `rate_diff>1` | unphysical recursion | clamped to domain `[0,1]` |
| `%d` formatting of order-of-magnitude gaps | OverflowError on `inf` | `%.0f` prints `inf` honestly |
| `log10(qi_traversal_ratio=0)` in panel | ValueError | floored at 1e-300 |
| **Signed-beta leaks** | `beta=-2` passed subluminal guards | `energy_conditions`, `horizon_locked`, `static_observer_exists`, `kinetic_energy_j` all test `|beta|` |
| `cruise_load_w(beta<0)` | control term went negative (negative load = power generation) | symmetric in `|beta|`; `bubble_on` clamped ≥0 |
| `overhead_s<0` in `portal_cycle_s` | **negative energy per cycle** — fuel ledger credited energy | clamped ≥0 |
| `mt_traversal_time_s(b0<0)` | negative traversal time | clamped (0) |
| `ctc_exists(sep<0)` | every offset a CTC | separation clamped ≥0 |
| `mt_flare_out(b0<=0)` | reported `satisfied=True` | reports no-throat |
| `mt_embedding_z(b0<=0)` | crash/domain error | `0` (no funnel) |
| `mt_min_throat_m`/`mt_tidal_g` `body_m<0` | `sqrt(neg)` crash / negative shear | clamped ≥0 |
| `rocket_proper_time_s(d<0)` | negative proper time | `0` |
| `boost_profile(mass<0)` | `ok=True` for an impossible ship | `ok=False` |
| `warp_energy_integral(R<=0)` | `sqrt(negative h)` crash | `0` (no bubble → no wall) |
| **`mt_proper_length` midpoint quadrature** | 1.35% systematic error vs `sqrt(r_far²−b0²)` (singular integrand at the throat) | exact closed form — 0 error |
| **Voyage boost integrator** | stale per-tick `core.beam_w` over-delivered → locked cruise at 0.893 while `boost_profile` said 0.857 | beam power per-substep from live position — both paths now lock at 0.8566 |
| `--voyage nan` | clamp laundered NaN into max beta | finite-check with loud fallback |
| `fusion_fuel_kg(E<0)` | negative fuel (negative-energy minting) | clamped ≥0 |
| `portal_cycle_s` / `multijump_plan` | throat traversal invisible — 30 s overhead swallows a 12 m gate but not a survivable 1.4e8 m throat (~650 days to walk) | optional `b0_m` adds `mt_traversal_time_s` to the cycle; breakeven 622 s → 1.8 yr |
| `Voyage.update` / `WarpCore.update` / `_step` `dt<=0 or nan` | ledger rewound (plant_out went negative, ship moved backward) or NaN-poisoned | non-finite/non-positive steps no-op |
| `boost_profile(beta<=0 or nan)` | `ok=True` with **negative range** — a −0.5c "successful" boost | `ok=False`: "no positive subluminal target" |
| `begin_boost(beta_cmd=nan)` | `nan <= 0` comparison slipped the guard | explicit `isfinite` check |
| `rocket_proper_time_s(beta>=1)` | finite "proper time" from capped gamma — imaginary in physics | `inf`: no rocket makes the trip |
| `ford_roman_bound_j_m3(tau=1e300)` | `tau**4` → OverflowError | `-0.0` (bound vanishes honestly) |
| `multijump_plan(cycles<0)` | `range(-3)` → silently vacuous plan | clamped to 0, explicit empty plan |
| **±inf sweep** | `magsail_decel_time_s(inf)` → finite 2.5e11 s (laundered) → `inf`; `warp_energy_integral(samples=inf)` → OverflowError → loud `ValueError`; `report_voyage(beta=inf)` hung in a 2M-iteration no-op loop (begin_boost refused but phase stayed DOCK) → early return | infinite beta → `inf`, infinite samples → `ValueError`, non-finite voyage → refuses without hanging |
| **NaN sweep, systematic (signature-driven, every function)** | 42 sites where a NaN argument became a plausible finite answer — `shape_f/shape_df(delta=nan)` → 1.0/0.0, `wall_tidal_gradient(delta=nan)` → inf, `flat_interior_r` → 0, `ford_roman_wall_limit` → Planck length, `casimir_energy_density`, `fusion_fuel_kg` → 0, `portal_cycle_s`, `multijump_plan(rate_diff=nan)` → **max desync 1.0** via `min()`, `ism_particles_swept`, `magsail_decel`, `max_boost_beta(mass=nan)` → 0.0, `mmp_tidal_mass_kg`, `chain/tipler/gott/kerr` offsets, `portal_traversal(sep=nan)` → CTC-relevant fields, `rocket_proper_time_s(d=nan)` → 0 | explicit `isnan` guards everywhere; `multijump_plan` returns a `nan_input`-flagged empty plan; 2 selftest checks pin ~30 call sites |
| **`max()`/`min()` NaN-laundering (13 sites)** | `beam_power_w(nan)` → **1e17 W full power**; `beam_brake_force_n(nan)` → full force; `mt_traversal_time_s(v=nan)` → fake 4.8e7 s; `mt_min_throat_m(g=nan)` → fake 1.3e13 m; `grav_rate(nan)` → plausible 0.9999…; `ctc_onset_s(nan sep)` → 0; `warp_energy_integral`, `mt_proper_length`, `mt_exotic_energy_j`, `mt_tidal_profile`, `mt_shape_b(+_prime)`, `mt_tidal_g(body)`, `portal_traversal(b0)` — all converted NaN into plausible finite answers | explicit `isnan` guards → NaN propagates through every helper (one selftest check covers all 14 call sites) |

Invariant sweep additionally verified: `shape_f` bounded/symmetric/monotone, `lapse_static∈[0,1]`, clock rates match `sqrt(1+2Φ/c²)/γ` exactly, beam capture ∈[0,1] non-increasing, energy density ≤0 everywhere, MT flare-out `b(b0)=b0, b'<1`, exotic energy linear in b0, offset antisymmetry, CTC iff `|offset|≥D/c`, breakeven ≥ CTC onset always (no evasion), backward recurrence contraction to fixed point, fuel ledger exactness, yield ≤ raw gas.

| Doc-vs-code accuracy (round 11) | `multijump_plan(b0_m=...)` reported a `breakeven_s` computed **without** the throat traversal its own `cycle_s` included; selftest/proof text and README claimed wall tidal "scales as beta^2" (the gradient is linear in beta — `beta c^2 |f''| L`) and quoted the stale WD-1 figure 3.52e15 g | breakeven now receives the same `b0_m` as the plan's cycles (regression check added); labels corrected to linear scaling; README figure updated to the current envelope (8.8e16 g at beta=0.5, R=183.44 m, delta=0.2 m) |

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
   - At beta=0.5 (R=183.44 m, delta=0.2 m): 8.8 x 10^16 g (lethal) [PASS]
   - Scales linearly in beta: gradient(1.0) = 2x gradient(0.5) [PASS]

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
   - Crossing at beta=0.5: 3,650 kg D-3He, was 4419 kg at full scale [PASS]

4. **Stefan-Boltzmann radiator** T = (P / (eps sigma A))^(1/4)
   - At beta=0.99: 1439 K (limit 1900 K), was 1649 K at full scale [PASS]
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
   - Cd = 0.85, A = 2.09 x 10^13 m^2, was 3.14 x 10^12 m^2 at full scale (loop 1000 -> 700 km at pass 2, 1400 km at pass 6, 2800 km at pass 7 to restore drag on the x8-heavier hull) [PASS]
   - At beta=0.5: 7.87 x 10^7 N [PASS]
   - Scales as v^2: F(1.0) = 4 x F(0.5) [PASS]
   - Halving time: 17.7 yr (looks feasible) [PASS]
   - Stop time: 8.86 x 10^3 yr (the honest number), was 3 x 10^4 yr at full scale [PASS]

### ISM & time dilation proofs (section 19f)

1. **ISM particles swept** N = n_ISM pi R^2 distance
   - n_ISM = 1.0 x 10^5 /m^3, R = 183.44 m (was 100 m at full scale) [PASS]
   - Proxima crossing: 4.25 x 10^26 protons, was 1.26 x 10^26 at full scale [PASS]

2. **ISM blast energy** E = N m_p c^2 beta^2/2 (conservative floor)
   - At beta=0.5: 7.98 x 10^15 J (8.0 PJ), was 2.37 PJ at full scale [PASS]

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
   - At beta=0.855: drift = +1.55 s over 4.97 yr [PASS]
   - NOT controllable (set by Sol-Proxima gravitational potential difference)
   - NOT a time machine (1.5 seconds is not a CTC)

7. **All time-travel scenarios remain blocked**
   - Exotic energy: -2.73 x 10^51 J needed, 46 orders short of Casimir [PASS]
   - Quantum inequalities: throat closes in ~1e-22 s vs ~5.4e7 s traversal [PASS]
   - Chronology protection: Hawking CPC (1992) expects vacuum divergence [PASS]
   - The maximum time jump is a mathematical result, not an engineering capability

### Near-light-speed achievement proofs (section 19k)

These proofs show how the ship reaches beta = 0.855 (85.5% of lightspeed) -- not as a declared parameter, but as an emergent result of a race between two clocks. 7 proof blocks, 7 new self-test checks (162 -> 169).

1. **The energy clock** (what the ship needs) KE = (gamma - 1) M c^2
   - M = 1,081,381 t (derived from geometry x density, not declared)
   - gamma = 1/sqrt(1-beta^2) -- diverges at beta=1 (infinite energy)
   - At beta=0.855: KE = 9.00 x 10^25 J = 90.0 YJ [PASS]
   - At beta=0.9: KE = 125.9 YJ (40% more for 5% more speed) [PASS]
   - At beta=0.99: KE = 592.2 YJ (6.6x more for 16% more speed) [PASS]
   - The gamma curve is why near-light speed is hard: each knot costs more than the last

2. **The range clock** (what the beam can deliver) d_spot = 2.44 lambda L / D
   - lambda = 1.0 um, D = 1000 km -> spot grows linearly with distance
   - f_capture = (d_rectenna / d_spot)^2 -> falls as 1/L^2
   - d_rectenna = 4 km (deployed film)
   - P_tap = 6.4 x 10^18 W (~17 ppm of L_sun -- a stellar tap, not a battery)
   - At 0.01 ly: capture = 100%, P = 6.4 x 10^18 W
   - At 0.50 ly: capture = 12%, P = 7.7 x 10^17 W
   - At 0.62 ly: capture = 7.8%, P = 5.0 x 10^17 W (usable range ends)
   - Capture at 1.0 ly is ~1/4 of capture at 0.5 ly (1/L^2 scaling) [PASS]

3. **The race** (two clocks, one winner)
   - The boost integrates in 3-day steps: got += P_captured(x) * dt; v = c * sqrt(1 - 1/(1 + got/(Mc^2))^2); x += v * dt
   - The energy clock says: you need (gamma-1)Mc^2 joules
   - The range clock says: you are moving away, spot grows, capture falls, power drops
   - Whichever runs out FIRST sets the cruise speed
   - At beta=0.855: need 90.02 YJ, delivered 89.93 YJ -> JUST makes it [PASS]
   - At beta=0.87: need 100 YJ, delivered 89.93 YJ -> FALLS SHORT [PASS]
   - At beta=0.9: need 125.9 YJ, delivered 89.93 YJ -> 29% short [PASS]
   - The margin between 0.855 and 0.87 is ~10% of the energy bill -- that is how tight the race is

4. **The mass lever, run both ways** (six refit passes)
   - The beam is external infrastructure. Since KE = (gamma-1)Mc^2, the mass on the receiving end sets how high the ship climbs before it outruns the beam
   - Pass 0 (WD-1): M=127,000 t, tap 100 PW -> beta=0.562 (gamma=1.21)
   - Pass 1 (WD-1m): M=42,719 t -> beta=0.727 (gamma=1.45)
   - Pass 2 (WD-1m2): M=27,003 t -> beta=0.794 (gamma=1.63)
   - Pass 3 (WD-1m3): M=18,374 t -> beta=0.844 (gamma=1.86)
   - Pass 4 (WD-1m4): M=18,215 t -> beta=0.845 (gamma=1.87)
   - Pass 5 (WD-1m5): M=16,602 t -> beta=0.857 (gamma=1.94)
   - Pass 6 (WD-1u2): M=125,416 t, tap 800 PW -> beta=0.863 (gamma=1.98)
   - Pass 7 (WD-1u4): M=1,081,381 t, tap 6.4 EW -> beta=0.855 (gamma=1.93)
   - Passes 1-5 shrank the ship against a FIXED 100 PW tap and the speed rose; passes 6-7 grew it back x8 each and raised the tap x8 each time -- the emergent speed holds near 0.86 because tap/mass is roughly preserved
   - The relationship is NOT linear -- the gamma curve makes each unit of energy worth more than the last
   - Lighter ship reaches higher beta: beta(M)=0.855 > beta(2M)=0.762 [PASS]

5. **Why it cannot reach beta=1** (the hard wall)
   - At beta=1: gamma = infinity -> KE = infinity
   - No finite beam can deliver infinite energy -- this is special relativity, not engineering
   - The gamma curve has a vertical asymptote at beta=1:
     - beta=0.855: gamma=1.93, KE=90.0 YJ
     - beta=0.9: gamma=2.29, KE=125.9 YJ (1.4x for +5%)
     - beta=0.95: gamma=3.20, KE=214.2 YJ (2.4x for +11%)
     - beta=0.99: gamma=7.09, KE=592.2 YJ (6.6x for +16%)
     - beta=0.999: gamma=22.4, KE=2078 YJ (23x for +17%)
     - beta=1.0: gamma=inf, KE=inf (wall)
   - Each percent closer to c costs more than the last percent
   - The ship sits at 85.5% because the beam runs out at 0.62 ly, not because 85.5% is a round number

6. **The boost profile** (303 days, integrated explicitly)
   - The boost is NOT instantaneous. boost_profile() integrates in 3-day steps
   - Tracks position, velocity and delivered energy simultaneously
   - Ship starts at rest, beam captures 100% at first (spot < rectenna)
   - Capture falls as the ship pulls away
   - After ~303 days the energy clock and range clock converge [PASS]
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
| 3 | Negative energy scale | FAIL | 5.66e47 J needed (183.44 m bubble, 0.2 m wall) | 3.1e6 J (Casimir) | 41 orders |
| 4 | Steering above beta=1 | THEOREM | causally disconnected | controllable | theorem |
| 5 | Thermal survival at 2c | FAIL | 1904 K | 1900 K | 0.2% over |
| 6 | Ford-Roman wall thickness | THEOREM | delta_max = 100 L_P | delta = 0.2 m | theorem |
| 7 | QI throat hold time | THEOREM | 3.25e-26 s | 4.8 s traversal | 26 orders |
| 8 | CTC chronology protection | CONJECTURE | divergent vacuum | stable throat | conjecture |

**Routes past each barrier (and why they fail):**

1. **Wall tidal**: Thinner wall -> MORE tidal, not less. Cutting `wall_thick_m` from 1.0 m to 0.2 m to buy back flat interior (see `overview.md`) made this barrier numerically *worse* (1.76e17 g vs 7.04e15 g at 1.0 m) -- an honest trade the model reports rather than hides, since the wall was never a survivable place at either thickness. At QI-legal thickness (100 L_P): even further beyond reach. Anti-route regardless.
2. **Superluminal NEC**: SSV theorem (2022) proves ANY v>c warp violates NEC. No route -- this is a theorem about the whole class, not just Alcubierre's ansatz.
3. **Negative energy**: More Casimir cassettes -> need ~9e42 cassettes. Rescaling the bubble and wall moves the raw exotic-energy demand around (5.66e47 J now, versus 3.36e46 J for the original 100 m/1.0 m-wall bubble and 1.41e47 J for the pass-6 91.72 m/0.2 m-wall bubble), but the onboard Casimir supply is always many orders too small regardless of how these knobs are turned.
4. **Steering**: Forward wall is causally disconnected at v>c. The crew cannot send a control signal to the front of the bubble. The entire trajectory must be pre-laid. Theorem (Everett 1996, Coule 1998, Krasnikov 1998).
5. **Thermal**: More radiator area -> need 385,910 m^2 (have 339,910 m^2, was 65,688 vs 37,440 at full scale). This is the ONLY passable barrier; the pass-7 upscale moved the margin back out (+13.5%, was +20% at pass 6, +0.9% at pass 5) -- it buys beta ~ 1.87 before failing, not superluminal. `--selftest` deliberately keeps this barrier failing at 2c so the redesign cannot claim to have solved it.
6. **Ford-Roman wall**: QI theorem limits wall to 100 L_P = 1.62e-33 m -- twenty-nine orders of magnitude below the ship's actual 0.2 m wall. At that thickness E = 2.08e79 J = 10^9 universes of energy.
7. **QI throat**: Throat closes in 3.25e-26 s. Traversal takes 4.8 s. The throat closes 10^26 times before you are halfway through.
8. **CTC**: Hawking's chronology protection conjecture (1992) expects divergent vacuum fluctuations at the chronology horizon. Not proven, but strongly expected by the majority of the field.

**Scorecard: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable (except thermal at subluminal speeds only).**

This is the honest engineering assessment: the drive cannot fly as drawn. The theorems are not engineering challenges -- they are mathematical proofs about what is possible. The 40-order energy gap is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

---

## Time-displacement amplification mechanisms

A single wormhole can displace you by at most the elapsed time (offset = elapsed * rate_diff, and rate_diff <= 1). To go further in a single traversal, you need either a chain of desynchronized mouths or a different time-machine construction entirely. The model computes the maximum displacement for every mechanism that general relativity admits on paper:

| Mechanism | Formula | Max offset (100 yr, extreme desync) | Barrier |
|-----------|---------|-------------------------------------|---------|
| Single wormhole | elapsed * rate_diff | 98.6 yr | QI + exotic energy |
| **Chain of N wormholes** | N * elapsed * rate_diff | **985.9 yr (N=10)** | N * (exotic energy + QI) |
| Nested wormhole | outer + inner (additive) | 197.2 yr | Same as chain |
| Tipler cylinder | L * omega * R / c^2 | 4.25 yr (L=4.25 ly) | Infinite cylinder, omega*R=c |
| Gott cosmic strings | delta * D / (4 pi) | 445 yr (GUT, 1 ly) | Deficit angle bounded |
| Kerr black-hole CTC | 2*pi*a/c per orbit | ~0.3 ms/orbit | Ring inside unstable horizon |

**Winner: chain of wormholes** -- multiplies the single-wormhole offset by N. The exotic-energy bill and all barriers scale the same way -- no barrier is avoided, only multiplied.

The chain is the only mechanism that gives more than elapsed-time displacement without requiring a different construction. The Tipler cylinder is unbounded in L but requires omega*R = c (a 1 m cylinder spinning at ~50 million rpm). The Gott pair's offset is bounded by the string deficit angle. The Kerr CTC is bounded by the black hole's spin period.

All mechanisms are blocked by the same physics: exotic energy, quantum inequalities, or chronology protection. The amplification multiplies the payoff without touching any barrier.

### Multi-jump: iterated traversal (continuous back-and-forth)

A single hop displaces by the CURRENT offset delta(t) = rate_diff * t, which keeps growing while the desync condition holds. To rejump, the ship returns externally to the departure mouth at beta -- a leg costing Delta = D/(beta c) of coordinate time and cruise_load(beta) * Delta of positive ship energy (constant-beta warp is a stationary spacetime; holding it costs only housekeeping).

**Backward loop** (step A->B into the past, fly B->A): recurrence t <- t(1-r) + Delta converges to the fixed point t* = Delta/r. Net-backward needs t > t* -- which is AFTER single-hop CTC onset (delta > D/c < Delta for beta < 1), so the loop multiplies chronology-protection exposure rather than evading it. Total reachable past = elapsed - Delta/r: at 100 yr elapsed, extreme desync, 1 AU, beta=0.855 that is ~100.0 yr vs 91-98.6 yr for one jump -- three to four cycles drain nearly all of it. [Self-test: PASS]

**Forward loop** (step B->A into the future, fly A->B): recurrence t <- t(1+r) + Delta is GEOMETRIC -- (1+r)^k growth. At r = 0.986, ten cycles carry coordinate time from 100 yr to ~95,000 yr. Unbounded while the desync condition persists. [Self-test: PASS]

**Energy & refueling ledger** (the warp drive's real job in multi-jump):

- Per 1 AU cycle at beta=0.855: ship energy 21.5 TJ, fuel burn ~0.098 kg D-3He -- gram scale.
- ISM scoop via the magsail: A*n_ISM*m_p*v = ~5,700 kg/day raw gas at cruise; after isotope enrichment (D/H 2e-5, 3He/4He 2e-4) the D-3He yield is ~0.51 kg/day.
- Scoop parity is now GONE: the pass-7 housekeeping floor (~1.73 kg/day at 0.05c) already exceeds the slow-beta yield, and burn grows ~b^2 while yield is linear -- the swept minimum net is ~-0.72 kg/day near 0.25c and -6.3 kg/day at cruise (yield 8.21 vs burn 14.56 kg/day at beta=0.855). **ISM refueling is a net loss at every speed for this ship** -- honest consequence of the x8.6 mass, printed, not hidden. [Self-test: PASS]
- At Proxima-scale separation each cycle burns ~0.77 t and scoops ~0.93 t -- still net-positive while moving, but each cycle costs ~5 years of coordinate time.
- Parked, the scoop is zero and housekeeping still burns: refueling requires motion. [Self-test: PASS]
- The exotic throat energy per hop (~2.73e51 J) is reported but never charged to the ship ledger -- that is the physics barrier, not a fuel problem. Fuel-start exhaustion is tracked per cycle (`fuel_out_at_cycle`).

---

## Environmental sustaining components (math proofs for each subsystem)

Every subsystem that fabricates or sustains the warp drive has its own formula, computed value, and self-test check. Below are the proofs for each environmental sustaining component.

### 1. Mass budget (every kilogram derived from geometry)

**Formula:** Each component mass = volume x density, computed from DIMS geometry.

```
m_component = surface_area x wall_thickness x density    (shells)
m_component = volume x density                            (solids)
```

**Total ship mass (WD-1u4, SCALE_S = 1.8344 overall):** 1.082 x 10^9 kg (1,081,381 tonnes) -- was 1.270 x 10^8 kg (126,986 t) at full WD-1 scale, 4.272 x 10^7 kg (42,719 t) after pass 1, 2.700 x 10^7 kg (27,003 t) after pass 2, 1.837 x 10^7 kg (18,374 t) after pass 3, 1.821 x 10^7 kg (18,215 t) after pass 4, 1.660 x 10^7 kg (16,602 t) after pass 5, 1.254 x 10^8 kg (125,416 t) after pass 6. Pass 7 upscaled every linear dimension ~2x again, with every component count re-derived from the doubled geometry (96 ring sectors/coils, 12 decks, 12 pylons, 60 radiator panels, 16 cryo units, 32 RCS pods, 8 antimatter traps, 96 Casimir cassettes) and every wall/shell/skin thickness scaled x2 once more for geometric similarity. [Self-test: PASS]

| Component | Mass (kg) | % | Formula |
|-----------|-----------|---|---------|
| Warp ring shell | 441,245,028 | 40.8% | 4pi^2 R r x ring_wall_m x ring_density (R=183.44 m, r=13.76 m, wall 1.08 m) |
| HTS field coils (96) | 246,504,390 | 22.8% | 96 x coil_volume x coil_density (0.30 m build, 27.92 m bore) |
| Pylons (12) | 140,899,627 | 13.0% | 12 x pylon_len x pylon_w x pylon_t x hull_density (154.08 x 5.88 x 4.80 m) |
| Radiators (60) | 77,499,411 | 7.2% | 60 x rad_len x rad_w x rad_t x rad_rho (90.44 x 31.32 x 0.24 m) |
| Shaping rings (2) | 54,892,108 | 5.1% | 2 x torus_surface x capring_wall_frac x ring_density |
| Crew decks (12) | 31,213,779 | 2.9% | 12 x pi r^2 x deck_t_m x hull_density (1.40 m plates) |
| Fusion reactor | 24,958,427 | 2.3% | torus_surface x reactor_wall_m x reactor_rho (wall 3.60 m) |
| Crew hull shell | 13,112,163 | 1.2% | hull_area x hull_wall_m x hull_density (124.8 m x 32 m, 0.44 m wall) |
| Magsail loop | 12,800,000 | 1.2% | magsail_mass_kg (2800 km loop, x64 cable) |
| Antimatter traps (8) | 12,128,011 | 1.1% | 8 x 4pi r^2 x amtrap_wall_m x amtrap_rho (1.20 m shell) |
| SMES buffer | 11,918,250 | 1.1% | torus_surface x smes_wall_m x smes_rho (1.00 m shell, 40.4 m major) |
| Cryoplant (16) | 7,356,936 | 0.7% | 16 x pi r^2 x cryo_len x cryo_rho |
| RCS pods (32) | 4,715,026 | 0.4% | 32 x pi r^2 x rcs_len x rcs_rho |
| Deflector | 1,060,570 | 0.1% | pi r^2 x deflector_t_m x deflector_rho (0.40 m skin) |
| Casimir lattice (96) | 983,178 | 0.1% | 96 x casimir_plate^2 x casimir_stack x casimir_rho |
| Consumables + crew (24) | 76,800 | 0.0% | 24 x crew_supplies_kg (3,200 kg each) |
| Boost rectenna | 17,593 | 0.0% | pi (2000)^2 x 1e-6 x collector_film_rho (4 km film -- unchanged: set by beam diffraction, not ship size) |

**Cross-check:** sum(mass_budget) = SHIP_MASS_KG (verified to 1e-6) [Self-test: PASS]. The ring/coil/pylon group dominates (~76% of dry mass). Pass 7 re-specified every component at ~2x linear over pass 6: volumes scale ~x8, and every shell/wall/skin thickness scaled x2 again to hold structural margins under geometric similarity (t ~ span for pressure vessels, plate bending, and buckling alike). Pylons grew superlinearly (count x2 AND section x8) because an x8-heavier hull hangs off a doubled span. The bubble wall thickness stayed at 0.2 m (spacetime, not structure), the rectenna stayed 4 km (set by beam diffraction), and the tap was re-specified at 6.4 EW -- external infrastructure sized to a ~8.6x-heavier mission.

### 2. D-3He fusion reactor (housekeeping power)

The reactor does NOT move the ship. It runs the coils, cryoplant, and hotel load.

**Formula:**
```
P_thermal = 102.70 GW     (was 22 GW at full scale, 7 / 4.35 / 2.91 / 2.62 / 15.70 GW after passes 1/2/3/4-5/6)
P_electrical = P_thermal x eta_direct = 102.70 x 0.62 = 63.67 GW     (was 13.64 GW)
m_fuel = E_required / (eta x E_D3He_per_kg)
E_D3He = 3.52 x 10^14 J/kg  (D + 3He -> 4He + p + 18.35 MeV)
```

Grew back from 2.62 GW to 102.70 GW. Passes 1-3 tracked the cruise electrical load down at a fixed ~1.5x margin inherited from WD-1; pass 4 re-examined that margin itself and settled on 1.35x -- still a 35% reserve, comfortably inside the 20-40% band typical of aerospace fusion/fission power-plant design. Pass 7 re-derived the plant from the upscaled loads: the beta=0.99 cruise electrical load is ~47.1 GW (coil AC losses x8 = 38.3 GW, cryo x4 = 2.49 GW, control x4 = 7.06 GW, hotel 0.096 GW for 24 crew); 47.1/0.62 = 76.0 GW thermal x the same 1.35 margin = 102.7 GW. The reactor torus grew x8 in volume again, so specific power density holds steady -- the bigger plant is no more exotic per cubic metre.

**Computed values:**
- Thermal output: 102.70 GW (63.67 GW electrical)
- Direct conversion efficiency: 62% (aneutronic)
- Fuel for Proxima crossing at beta=0.5: 20,129 kg D-3He (was 4,419 kg at full scale) [Self-test: PASS]
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
- Tap power: 6.4 x 10^18 W (~17 ppm of L_sun) -- x8 the pass-6 tap: a ~8.6x heavier hull needs ~8x delivered power to hold the same emergent cruise speed
- Aperture: 1000 km, wavelength: 1.0 um
- Deployed rectenna: 4 km diameter
- At 0.01 ly: spot = 0.2 km, capture = 100% [Self-test: PASS]
- At 0.10 ly: spot = 2.3 km, capture = 100% [Self-test: PASS]
- At 0.50 ly: spot = 11.5 km, capture = 12.0% [Self-test: PASS]
- At 1.00 ly: spot = 23.1 km, capture = 3.0% [Self-test: PASS]
- Capture never exceeds 1.0 (energy conservation) [Self-test: PASS]
- Usable boost range: 0.62 ly
- Maximum emergent cruise speed: beta = 0.855 (was 0.562 at full scale, 0.727 / 0.794 / 0.844 / 0.845 / 0.857 / 0.863 after passes 1/2/3/4/5/6) [Self-test: PASS]

**Boost energy:**
```
KE = (gamma - 1) M c^2
```
- At beta=0.5: KE = 1.51 x 10^25 J (15.1 YJ), boost time = 30 d (was 1.77 YJ / 207 d at full scale -- the x8.5-mass ship costs x8.5 the bill at x64 the beam) [Self-test: PASS]
- At beta=0.855: KE = 9.00 x 10^25 J (90.0 YJ), boost time = 303 d -- the new emergent cruise speed
- At beta=0.9: KE = 1.46 x 10^25 J -- beam cannot deliver (range exceeded)

### 4. SMES magnetic energy storage (transient buffer)

**Formula:**
```
E = (B^2 / 2 mu_0) x V_torus
V_torus = 2 pi^2 R r^2
```

**Computed values:**
- Major radius: 20.18 m, minor radius: 2.20 m (was 11 m / 1.2 m at full scale)
- Field: 60 T (unchanged HTS technology)
- Volume: 2 pi^2 x 20.18 x 2.20^2 = 1,926 m^3
- Energy density: B^2/(2 mu_0) = 60^2 / (2 x 4pi x 10^-7) = 1.43 x 10^9 J/m^3
- Stored: 2.76 x 10^12 J = 2.76 TJ (was 448 GJ at full scale, 123 / 69.8 / 43.1 / 345 GJ after passes 1/2/3-5/6) [Self-test: PASS]
- This is 13 orders of magnitude too small to change the ship's velocity

### 5. Waste-heat radiators (Stefan-Boltzmann thermal balance)

**Formula:**
```
P_waste = P_load / eta_conversion
T = (P_waste / (epsilon x sigma_SB x A))^(1/4)
```

**Computed values:**
- Panels: 60, each 90.44 m x 31.32 m, both faces (was 52 m x 18 m at full scale)
- Total area: 339,910 m^2 (was 37,440 m^2 at full scale, 15,818 / 10,895 / 7,081 / 42,489 m^2 after passes 1/2/3-5/6) [Self-test: PASS]
- Emissivity: 0.92
- Graphite sublimation limit: 1900 K
- Design temperature: 1550 K

| beta | Load (W) | Waste (W) | T (K) | Status |
|------|----------|-----------|-------|--------|
| 0.10 | 4.95e9 | 7.98e9 | 819 | OK |
| 0.50 | 1.64e10 | 2.64e10 | 1105 | OK |
| 0.85 | 3.68e10 | 5.93e10 | 1352 | OK |
| 0.90 | 4.01e10 | 6.46e10 | 1382 | OK |
| 0.99 | 4.71e10 | 7.60e10 | 1439 | OK |
| 1.00 | 4.79e10 | 7.73e10 | 1445 | OK |
| 1.50 | 9.57e10 | 1.54e11 | 1718 | OK |
| 1.87 | ~1.4e11 | ~2.3e11 | ~1900 | OVER LIMIT (barrier threshold) |
| 2.00 | 1.63e11 | 2.62e11 | 1961 | OVER LIMIT |

- Round-trip: P = eps x sigma x A x T^4 recovers P [Self-test: PASS]
- Radiators FAIL above beta ~ 1.87 (was beta ~ 1.45 at full scale, ~1.79 / ~1.97 / ~1.99 / ~1.80 after passes 1/2/3-5/6) [Self-test: PASS] -- the pass-7 radiator area grew x8 against x6.6 waste heat, so the beta=0.99 equilibrium actually cooled to 1439 K. `--selftest` hard-asserts T(2c) still exceeds the 1900 K limit -- the redesign is not allowed to quietly erase this barrier (now +13.5% more radiator area needed to clear beta=2, was +20% at pass 6).

### 6. Cryoplant (HTS coil refrigeration at 18 K)

**Formula:**
```
P_cryo = 2,493 MW (constant, independent of beta; was 740 MW at full scale, 313 / 215.6 / 155.8 / 623.2 MW after passes 1/2/3-5/6)
```

The cryoplant holds the 96 REBCO coils at 18 K. This is a constant overhead -- it does not scale with speed. It was resized because cryostat radiative heat leak scales with cold-surface area, not volume. At cruise, the coil AC losses (38.3 GW at beta=1, was 6.2 GW at full scale) dominate the load.

- 16 cryo units, each 11.00 m diameter x 20.16 m long (was 6 m x 11 m at full scale)
- Cryoplant mass: 7,356,936 kg (was 298,577 kg at full scale)
- Power draw: 2,492.8 MW [Self-test: PASS (cruise_load includes cryo)]

### 7. Casimir negative-energy lattice (the only real exotic-energy source)

**Formula:**
```
rho = -pi^2 hbar c / (720 a^4)
E_cassette = rho x V_gap = rho x plate^2 x gap x n_gaps
E_total = E_cassette x 96 cassettes
```

**Computed values:**
- 96 cassettes, each 1.10 m x 1.10 m plates, 10 nm gap, 3.68 m stack (was 2.40 m / 2.00 m at full scale)
- Plates per cassette: ~61,333,333
- Gap volume per cassette: 0.742 m^3
- Energy density at 10 nm: -4.33 x 10^4 J/m^3 [Self-test: PASS] (a material/nanoscale property -- unaffected by ship scale)
- Energy per cassette: -3.21 x 10^4 J
- Total onboard: -3.09 x 10^6 J (-3.09 MJ) (was -2 MJ at full scale) [Self-test: PASS]
- Warp bubble demand at delta=0.2m for the 183.44 m bubble (superluminal/Alcubierre mode, never actually drawn on): -5.66 x 10^47 J -- larger than pass 6's -1.41 x 10^47 J because the bubble doubled again while the wall thickness held at 0.2 m
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
- Loop radius: 2,800 km (was 1000 km at full scale; doubled again at pass 7 to restore drag on the x8-heavier hull), area: 2.46 x 10^13 m^2 [Self-test: PASS]
- Cd = 0.85, current: 4.4 MA, mass: 12,800,000 kg (x64 the pass-5 cable mass; current doubled again to hold the same loop-centre field B ~ I/r)
- ISM density: 1.0 x 10^5 protons/m^3 (0.1/cm^3)

| beta | Drag (N) | Halving time | Stop time |
|------|----------|-------------|-----------|
| 0.10 | 3.1e6 | 327 yr | 32,340 yr |
| 0.50 | 7.9e7 | 65 yr | 32,600 yr |
| 0.85 | 2.3e8 | 38 yr | 32,630 yr |

- F scales as v^2: F(1.0) = 4 x F(0.5) [Self-test: PASS]
- Halving time = M/(k v0) [Self-test: PASS]
- Stop time ~ 32,600 yr -- the honest number, and the pass-7 price of upscaling: the loop grew to 2,800 km (x4 drag area) but the hull is ~8.6x heavier, so braking time is mass / (Cd rho A) = x8.6 / x4 = LONGER than pass 6's ~15,000 yr. Even at the enlarged sail the ship cannot stop unaided inside millennia [Self-test: PASS]
- Drag falls as v^2 -- the brake fades when you need it most

### 9. Photon brake (destination array)

**Formula:**
```
F = 2P_captured / c        (photon pressure, perfect reflector)
t = gamma x M x v / F
```

**Computed values:**
- At 0.02 ly from destination array: F = 4.27 x 10^10 N [Self-test: PASS] (force scales with the re-specified 6.4 EW tap)
- F <= 2P_tap/c (cannot exceed full beam pressure) [Self-test: PASS]
- Brake time at beta=0.5: 50.8 days (was 381 days at full scale, 128 / 81 / 55 / 55 / 47 days after passes 1/2/3/4/6) -- the x8.6 mass nearly cancels the x8 beam force [Self-test: PASS]
- Requires a destination array already in place at Proxima

### 10. ISM hazard (interstellar medium loading)

**Formula:**
```
N = n_ISM x pi x R^2 x distance
E_blast = N x m_p x c^2 x beta^2 / 2    (conservative floor)
```

**Computed values:**
- ISM density: 1.0 x 10^5 protons/m^3
- Bubble radius: 183.44 m (was 100 m at full scale, 65 / 53.95 / 45.86 / 91.72 m after passes 1/2/3-5/6)
- Proxima crossing: N = 4.25 x 10^26 protons (was 1.26 x 10^26 at full scale) -- swept volume scales with R^2, now ~3.4x full scale [Self-test: PASS]
- Blast at beta=0.5: 7.98 x 10^15 J (8.0 PJ, was 2.37 PJ at full scale) [Self-test: PASS]
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
- Drift at beta=0.855 (was 0.562 at full scale, 0.727 / 0.794 / 0.844 / 0.845 / 0.857 / 0.863 after passes 1/2/3/4/5/6): +1.55 s over the 4.97 yr crossing (crew age 1.55 s more than Earth) -- gravitational-only, never velocity-dilated inside the flat bubble [Self-test: PASS]
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

- 8 traps, 5.248 kg antihydrogen each (was 0.85 kg at full scale -- scaled with the kinetic-energy bill it buffers)
- Total: 41.984 kg antimatter
- Energy: 2.624 x 1.80 x 10^17 = 4.72 x 10^17 J
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

## SPECIAL WORKS -- the WD-88 FIELD CAR (the whole drive, car scale)

The sixth tab is the same model run at car scale: every WD-1 subsystem folded into a 4.40 m stainless gull-wing coupe that drives a real road and fires its field transition at exactly **88 mph** (39.33952 m/s). The body is a real production coupe; the engineering is the same audit discipline as the ship -- every part is derived, massed, powered and given a failure mode, and every component carries a real function.

### The engineering contract (stated in the model, not just here)

- **88 mph is an activation threshold, not physics.** The bubble could in principle fire at a standstill; 88 is the engineered arming setpoint, and the run-up is how the systems come to temperature. The selftest asserts 87.9 mph held does **not** fire, and that the trigger is the real 88 mph = 39.33952 m/s -- not 88 m/s.
- **The cabin Y-manifold is the FIELD TRANSITION SEQUENCER** -- it fans the transition pulse from the SMES into the three conduit arms. The dash strip is the run sequencer display, the dash lever is the physical arming interlock, the console keypad enters the mission destination, and the folded ground hook on the rear deck drains residual shell charge before service. The selftest asserts the sequencer spec card exists.
- **No gasoline engine of any kind.** All four wheels are fusion-fed hub motors; the only fuel aboard is He-3 for the trunk cell. The selftest scans every part name for "engine"/"gas"/"petrol".

### Scale accounting (the honest part)

| Quantity | Ship (WD-1u4) | Car (WD-88) |
|----------|---------------|-------------|
| Shell radius | 183.44 m | 2.90 m (**1/63**) |
| Hull length | 124.76 m | 4.40 m (**1/28**) |
| Wall thickness | 0.2 m | 0.22 m (sigma = 4.5 /m) |
| Exotic bill (beta=1, Alcubierre mode) | -5.66 x 10^47 J | -1.29 x 10^44 J (-0.00072 M_sun) |
| Onboard Casimir energy | -3.09 MJ (96 cassettes) | -56.2 J (12 strips) |
| Shortfall | ~41 orders | ~42 orders |

Downscaling buys the R^2 in the field energy (the car's bill is ~4 orders smaller than the ship's) -- **not a way around the sign of it**. A literal 1/117 build makes a 1.57 m shell, and a 4.4 m car cannot fit inside it; the panel prints that rather than letting the model lie.

### The 18 parts -- every one audited like a ship system

Each part carries a spec card (hover it), a derived mass share (not typed), an ops row (power draw, duty cycle, failure mode), and a place in the mass budget. Zero-mass parts say so: the bubble ("a field has no rest mass"), the trail ("an event's trace"), the road ("the planet supplies this one").

| # | Part | Location | Ship analog | Mass | Draw / duty | Failure mode |
|---|------|----------|-------------|------|-------------|--------------|
| 1 | STAINLESS MONOCOQUE | the shell | crew hull | 570.7 kg | passive / always | none -- it IS the structure |
| 2 | HUB DRIVES + RCS BELLS x4 | corners + tail | drive + RCS pods | 214.0 kg | 30 kW / rolling | hub fault -> limps on three |
| 3 | FIELD CONDUIT RUN | beltline | 96 field coils + pylons | 123.6 kg | 12 kW / armed | quench -> bubble never forms |
| 4 | MICRO FUSION CELL | trunk | D-3He reactor | 150.0 kg | supplies 2.5 MW / continuous | cell trip -> bus browns out |
| 5 | SMES BUFFER STACK | hood | SMES buffer | 45.0 kg | 0.5 kW / holds charge | quench -> 88 mph is just driving |
| 6 | PENNING BOTTLES x2 | floor pan | antimatter traps | 46.0 kg | 2 kW / continuous | field decay -> vented, not detonated |
| 7 | CASIMIR STRIPS x12 | conduit liner | Casimir lattice | 29.8 kg | passive | collapsed gap = 56 J of nothing |
| 8 | WASTE-HEAT LOUVERS | rear deck | radiator wings | 22.0 kg | passive / hot when running | stall -> heat soak, derate |
| 9 | ROOF RECTENNA WHIP | roof | 4 km boost rectenna | 4.0 kg | 0.1 kW / listen | whip loss -> no boost-hear |
| 10 | FORWARD DEFLECTOR STRIP | nose | deflector | 3.0 kg | passive | ablates -- cosmetic |
| 11 | SHAPING HOOPS | nose + tail | fore/aft cap rings | 8.0 kg | 1 kW / armed | tune drift -> shell ends leak |
| 12 | FIELD TRANSITION SEQUENCER | rear bulkhead | pulse distribution | 5.0 kg | 5 mW / always | sequencer fault -> run aborted on interlock |
| 13 | WARP SHELL | around the car | warp bubble | 0 (a field) | on demand | shell collapse -> no jump |
| 14 | KE-RECOVERY LOOP | tail, stowed | magsail | 4.0 kg | 0.2 kW / braking | loop open -> KE undumped |
| 15 | CRYO LOOP | underbody | cryoplant | 56.0 kg | 3 kW / continuous | circulator stalls -> field sags |
| 16 | EPHEMERIS UNIT | dash | navigator/star catalogue | 6.0 kg | 0.15 kW / always | drift -> lands on WRONG pavement |
| 17 | TRANSITION TRAIL | the road behind | -- (the mark) | 0 (an event) | after the event | the scar cannot fail |
| 18 | RUN SURFACE | under the wheels | -- (the planet) | 0 (Earth's) | always | the road does not fail |

**Kerbside mass: 1,410 kg** = 25-line budget (parts 1,287 kg + crew/fluids/fit-out 122.9 kg -- the driver is *drawn*, because the budget books crew mass). **Bus: 49 kW loads vs 2.5 MW cell supply -- margin +2.45 MW**; a negative margin would fail the selftest, same rule as the ship.

### The drive model (`car_mph_step`)

One tick of road speed, the same function the update loop and the selftest both call:

- Throttle: **+30 mph/s** (hub motors); regen brake **-45 mph/s**; rolling drag **-5 mph/s**
- Ceiling: **130 mph**; at 88 mph the transition fires *only while armed*
- A heat-soaked cell (> 1,100 K) **derates the drive to 55 mph** -- below the trigger
- After firing, speed coasts down at -35 mph/s
- Hostile inputs (nan, negative speed) are recovered to 0, never trusted

### The thermal model (`car_thermal_step`)

The trunk cell has a real radiative balance -- the rear-deck louver bank is the radiator, not trim:

- Heat capacity: cell + blanket + plumbing = **60 kJ/K**
- Rejection: Stefan-Boltzmann, **3.0 m^2** louver bank at emissivity **0.88** (the ship's graphite), outward only
- Equilibria: **idle 317 K** (4 kW waste), **hard drive 752 K** (48 kW), **louver-stalled 1,278 K** -- past the 1,100 K service limit, so the drive derates
- A single step can **never overshoot the cell's own radiative equilibrium** -- a hostile dt=10^9 s step yields a bounded temperature, not the 7.8 x 10^8 K blow-up the unguarded integrator produced
- Clamped to **120-6,000 K**: cryo floor below, "nothing aboard is still a solid" above

### Live fault injection (the FAULT chip)

The ops ledger's named failure modes run live -- `FAULT` cycles none -> smes -> louver -> nav -> none, `PARK` clears:

| Fault | What it does (live) |
|-------|---------------------|
| SMES quench | No spike capacity -- the car reaches 88 mph and *just drives*; the transition never arms |
| Louver stall | Rejection area collapses to 12% -- the cell heat-soaks past 1,100 K and the drive derates |
| Ephemeris drift | The transit panel stops pretending: "EPHEMERIS LOST / the bubble has no fix / landing misses by ~transit \|\|d\|\|" |

### The same-road-spot solve (the ephemeris, fully)

The hard part nobody prices: the landing zone is fixed to **Earth**, not to space. Between departure at t0 and arrival at t1 = t0 + hop, the same pavement occupies a different inertial position. "Come back to this road" is a two-frame problem, solved live by the dash ephemeris unit:

**Frame 1 -- inertial heliocentric Earth, first-order Kepler:**

```
M(t)  = 2 pi t / T            T = 365.25 d (Julian year)
r     = a (1 - e cos M)       a = 1 AU, e = 0.0167 (carried for real)
theta = M + 2e sin M          (equation of the centre)
E(t)  = r (cos th, sin th, 0) -- the ecliptic plane
```

**Frame 2 -- the Earth-fixed road at lat 34.05, lon -118.24:**

```
ph(t)  = 2 pi t / T_sid + lon        T_sid = 86,164.0905 s (sidereal day)
s      = R (cos lat cos ph, cos lat sin ph, sin lat),   R = 6,371 km
S(t)p  = tilt by obliquity eps = 23.44 deg about the equinox axis
```

**The solve:**

```
p_road(t) = E(t) + S(t) p
dep    = p_road(t0)     stamped when the transition fires
arr    = p_road(t1)     same lat/lon/alt -- the same pavement
d      = arr - dep       what the bubble must carry the car through
d_orb  = E(t1) - E(t0)   the orbital leg (~2 AU on a half-year hop)
d_spin = S(t1)p - S(t0)p the sidereal leg (~4,000 km on that hop)
```

**And heading.** S(t) rotates the *whole* local frame, so `road_frame()` carries the road's (east, north, up) basis into the ecliptic: the lane's east vector lands as S(t1)*east, and the car arrives **facing down the lane, not across it** -- 45 deg of inertial heading rotation over a 3.7-day hop. A position-only solve would put the car on the pavement sideways; the selftest asserts the ENU basis is orthonormal to 1e-9 and the arrival lane stays tangent to the road.

**Velocity matching** is the other quiet half: the car lands road-relative -- still doing 88 mph over the pavement. The ~29.79 km/s orbital + 0.385 km/s spin inertial speed belongs to the planet, and the road shares it; it is never booked against the chassis.

**And the clock face.** `road_solar_hour()` tracks local mean solar time: the same pavement is a different time of day at t1 -- the panel prints it (e.g. 16.1h -> 7.1h across the default hop).

**Honest limits, stated not hidden:** eccentricity carried to first order only (the missing e^2 term is ~2 km in position); lunar perturbation, nutation, polar motion and the equatorial bulge are neglected; radius is the 6,371 km mean. A production run would swap this for JPL DE440 -- the frame structure is the same, only the tables change.

### The TRANSIT panel -- a live preview, not a post-hoc report

Before the run fires, the panel solves the transit as if it fired *right now*: `dep` shows the current time tagged "(live)", every row populates -- inertial dep/arr, arrival epoch, transit \|\|d\|\|, the orbital/spin leg split, miss-if-unaimed (= \|\|d\|\|), lane rotation angle, road speed, solar-time pair -- and an ecliptic mini-map draws dep->arr around the Sun. `[`/`]` set the hop (x2/x4 per press, 60 s to 10 yr). Only when the solve is invalid does it degrade to "solve invalid -- hop is non-finite"; under nav fault it shows the honest EPHEMERIS LOST block instead of a frozen number.

### The transition trail

The twin scorch streaks the transition leaves behind the wheels, modelled as a real part: hidden until `fired` ("physically there is nothing there yet"), swept streaks running rearward from the rear wheels onto the tarmac. Its ops row is honest: "no failure mode -- the scar cannot fail; it is the record."

### Running the car

| Control | Effect |
|---------|--------|
| `W`/`UP` or RUN 88 chip | Drive (RUN 88 toggles auto-throttle) |
| `S`/`DOWN` or BRAKE chip | Regen brake (tail bar brightens -- no friction discs) |
| PARK chip | Stand down: speed 0, unfire, clear fault, drop the scar |
| FAULT chip | Cycle the injected fault: none -> smes -> louver -> nav |
| `,` / `.` | Speed nudge (-/+2 mph, +/-10 with shift) |
| `[` / `]` | Hop duration x2//2 (x4//4 with shift), 60 s to 10 yr |
| `4` or `X` | Section cut -- removes the +x half of the body, exposing the cabin |
| `N` | Mission reset -- stands the car down completely (no ghost run or scar) |
| `P` | Pause -- the car holds state mid-frame, like the ship's integrator |

The speedometer reads PARKED / ROLLING / ROLLING--ARMING / FIELD TRANSITION / BUBBLE UP; the progress bar marks 88 mph honestly at its true position, and the shell-convergence bar tracks the 1.2 s bubble form-up. The odometer accumulates real miles. The starfield streaks with speed and drifts with the odometer.

### Hostile-input hardening on the car (found by fuzzing, then fixed)

| Input | Was | Now |
|-------|-----|-----|
| `car_thermal_step(dt=1e9)` | 7.8 x 10^8 K | bounded at radiative equilibrium (~300 K) |
| Negative `sp["mph"]` poison | never healed after firing | drag floor heals it to 0 |
| `hop_s < 0` via hostile path | negative hop | floored at 0 every tick |
| `,`/`.`/BRAKE nan boundary | raw nan into `sp["mph"]` | sanitized at the boundary |
| `zoom_at` floor hardcoded 24 m | zoom-in *snapped the camera away* (car home is 15 m) | floor = 5.5% of home distance (~0.8 m on the car) |
| Paused sim | ship froze, car kept coasting | car holds state too |
| `N` reset | car kept its speed/fired/scar | stands the car down fully |
| `build_special_parts(detail=0/-1/nan/inf/1e-6/100)` | unverified | all produce the same finite 18-part car |

Plus the geometry audit pass: deck fittings ride a `deck_top(z)` helper derived from the loft stations (buried conduit, field drivers, service cap, He-3 filler, sloped louver bank, sail louvers on the chamfer faces, aft-facing RCS bells, magsail clear of the tail, seated charge port, flush headlamp doors, canted steering wheel, roof-mounted whip, elliptical shaping hoops that actually wrap the body sections).

### Field Car self-test coverage (~30 of the 417 checks)

- Builds finite at every detail factor; the whole car fits inside its own 2.9 m shell; four hub drives stand at the corners
- Trigger exactness: 87.9 mph held unfired, one-step crossing fires, real 39.33952 m/s
- Overspeed clamps to 130; nan speedometer recovered; negative poison healed by the drag floor
- Quenched SMES: 88 mph is just driving; heat-soaked cell derates below the trigger
- dt=0 / dt=nan produce no motion and no fire
- Thermal: idle/drive/stalled equilibria honest; equilibrium-bound under giant dt; all-nan recovery; 120 K floor under absurd cooling
- Mass budget derived to 1e-6; every part carries ops (power/duty/fail) and mass rows; bus funded with positive margin; transition sequencer spec'd; no gas engine anywhere
- Ephemeris: real eccentricity perihelion->aphelion; road pinned one Earth-radius out at both endpoints; zero hop lands where it left; half-year hop crosses ~2 AU; fractional-day hops shift inertially; lane heading carried (orthonormal ENU, tangent arrival, real inertial rotation); solar-time changes across the hop; nan/inf rejected, wild lat/lon stays on the sphere; poles and +/-32,000-year epochs hold
- 34 named fittings required present (steering wheel, windshield, driver, pedals, seatbelts, sail louvers, field drivers, charge port, TFC switch, lightning hook, fire extinguisher, gauges, ...)

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