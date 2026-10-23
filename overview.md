# Overview -- Warpdrive WD-1u4 Foldrunner

## What this is

A physics-honest digital twin of a warp-drive starship, a traversable wormhole portal, the time machine that any wormhole automatically becomes -- and, in the SPECIAL WORKS tab, the same drive folded down to car scale as the WD-88 Foldmobile, a 4.40 m coupe that transitions at exactly 88 mph and solves the "same road, different place in space" problem with a live two-frame ephemeris. Every number is computed from real general-relativity and quantum-field-theory formulas. Nothing is fictional. Where the physics says "impossible," the model says so and shows the computation that proves it.

This is the seventh refit pass. Passes 1-5 (WD-1m through WD-1m5 "Miniframe V") progressively shrank the ship to 0.4586x linear -- mass down 87%, cruise speed up from 0.562c to 0.857c against an unchanged 100 PW beam. Pass 6 (WD-1u2) upscaled every component ~2x linear back to near-full scale (0.9172x, 125,416 t). Pass 7 (WD-1u4) upscales ~2x again to 1.8344x the original WD-1: every hull, ring, coil, radiator and mount dimension is the pass-6 value x 2.0; every component count was re-derived from the doubled geometry (96 ring sectors/coils, 12 decks, 12 pylons, 60 radiator panels, 16 cryo units, 32 RCS pods, 8 antimatter traps, 96 Casimir cassettes, crew 24); every wall/shell/skin thickness scaled x2 once more for structural similarity; and the external beam tap was re-specified at 6.4 EW (x8) to carry the ~8.6x heavier hull. Dry mass: 1,081,381 t -- the million-tonne ship, fully specified part by part. See `Engineering notes` below.

## The ship

| Parameter | Value |
|-----------|-------|
| Mass | 1.082 x 10^9 kg (1,081,381 tonnes) -- was 127,000 t (WD-1), 16,602 t at pass-5 minimum, 125,416 t at pass 6 |
| Bubble radius | 183.44 m -- was 100 m WD-1, 45.86 m at passes 3-5, 91.72 m at pass 6 |
| Wall thickness | 0.2 m -- unchanged (spacetime, not structure) |
| Flat interior | 182.2 m |
| Cruise speed | beta = 0.855 (0.855c) -- was 0.562c (WD-1), 0.857c (pass 5), 0.863c (pass 6), emergent, beam-limited |
| Destination | Proxima Centauri b (4.2465 ly) |
| Cruise time | ~4.97 years in flight (ship = Earth, no dilation) -- was 8.49 yr (WD-1) |
| Crew | 24 -- x2 the WD-1 complement |
| Reactor | 102.7 GW D-3He fusion (aneutronic, 62% direct conversion, 63.7 GW electric), 1.35x electrical margin -- was 22 GW (WD-1), 2.62 GW (passes 4-5), 15.7 GW (pass 6) |
| Radiators | 339,910 m^2, 1550 K design, 1900 K limit -- was 37,440 m^2 (WD-1), 7,081 m^2 (pass 5), 42,489 m^2 (pass 6) |
| Hull wall | 0.44 m (pressure-vessel scaled) -- exactly 2x WD-1's wall, t = P*r/sigma is linear in hull radius |
| Casimir lattice | 96 cassettes, -3.09 MJ total |
| SMES buffer | 2.76 TJ -- was 448 GJ (WD-1), 43.1 GJ (pass 5), 345 GJ (pass 6) |
| Magsail | 2,800 km radius, ~32,600 yr full stop -- was 700 km / 8,000 yr (pass 5), 1,400 km / 15,000 yr (pass 6) |

## Engineering notes -- the pass-7 x2 upscale

The pass rescales every geometric `DIMS` entry by x2.0 again (`SCALE_S = 0.9172 -> 1.8344`) and rederives every dependent quantity from the same first-principles formulas already in the model (`mass_budget()`, `plant_electric_w()`, `radiator_area_m2()`, `boost_profile()` / `max_boost_beta()`, `check_envelope()`). The effects that compounded in the ship's favour while shrinking now compound against it, and the model reports both directions honestly:

1. **Mass rises a little faster than S^3** because it is a volume-times-density sum AND every structural thickness scaled x2 again (geometric similarity), AND several counts grew superlinearly (pylons x2 count on x8 section, radiators x2 count on x4 area each). Net dry mass x8.63 to 1,081,381 t.
2. **The external beam tap was re-specified at 6.4 EW** (6.4e18 W, ~17 ppm of L_sun, x8 the pass-6 tap) -- it is ground/orbital infrastructure sized to the mission, and an ~8.6x-heavier hull needs ~8x delivered power to hold the same emergent cruise speed. The aperture, wavelength and range are unchanged: they are transmitter physics, not ship size. Net: beta 0.863 -> 0.855, essentially held.
3. **Component counts were re-derived from the doubled geometry**, not cubed: 96 ring sectors/coils (doubled circumference), 12 decks (doubled hull length), 12 pylons (8x hull on a doubled span), 60 radiator panels (area x8 against waste heat ~x6.6 -- deliberately more margin than needed), 16 cryo units, 32 RCS pods, 8 traps, 96 Casimir cassettes, crew 24.
4. **The reactor re-derived to 102.7 GW th** from the upscaled loads: beta=0.99 cruise electrical ~47.1 GW (coil AC x8 = 38.3 GW, cryo x4 = 2.49 GW, control x4 = 7.06 GW, hotel x2 = 0.096 GW); /0.62 conversion = 76.0 GW thermal x the same 1.35 margin. Torus volume x8, so specific power density holds steady.
5. **Deliberately unchanged:** wall_thick_m and interior_margin (the bubble wall is spacetime, not structure), collector_deploy_km (the 4 km rectenna is set by beam diffraction at the unchanged transmitter, not ship size), Casimir gap/pitch (nanoscale physics), all temperatures and densities, and every portal-gate dimension (a separate installation).
6. **The braking problem is honestly worse again.** The magsail loop doubled to 2,800 km (x4 drag area, x8 cable mass, current doubled to hold loop-centre field) -- but the hull is 8.6x heavier, so full-stop time went from ~15,000 yr to ~32,600 yr. A destination photon brake still stops the ship in ~51 days at beta=0.5 and remains REQUIRED for a rendezvous; the model prints that requirement, it does not hide it.
7. **Scoop parity is gone entirely.** At pass-6 scale the scoop lost only at top speed; at pass-7 scale the housekeeping burn floor (~1.73 kg/day at 0.05c) already exceeds the slow-beta yield, and burn grows ~b^2 while yield is linear -- the ISM scoop is net-NEGATIVE at EVERY beta (best case ~-0.72 kg/day near 0.25c; -6.3 kg/day at cruise). The self-test asserts this rather than pretending refueling still works.

**The one thing every pass deliberately did NOT do:** let the thermal barrier flip from FAIL to PASS at 2c. `--selftest` hard-asserts `T_at_2c > rad_limit_k` -- the model is built to keep demonstrating that superluminal flight cooks the radiators, not to quietly erase that finding. At this scale T(2c) = 1961 K vs a 1900 K limit -- still fails, by design, now needing +13.5% radiator area to clear.

Every number here is re-verified by `--selftest` (417/417) after each change -- nothing was hand-typed to make the story work.

## The six visualization modes

| Mode | Key | What it shows |
|------|-----|---------------|
| SHIP | 1 | The starship: ring, hull, radiators, reactor, coil sequence |
| METRIC | 2 | The warp bubble: York expansion grid, energy-density hotspots |
| DILATION | 3 | Clock rates: comoving vs static, gravitational drift |
| PORTAL | 4 | The wormhole: throat, flare-out, tidal profile, both mouths |
| FLIGHT | 5 | Flight sim: boost, cruise, brake, arrival (keys G/K/J/T) |
| SPECIAL WORKS | 6 | The WD-88 Foldmobile: the whole drive folded into a 4.40 m road car that fires its field transition at exactly 88 mph -- see below |

Press **I** for the full specification panel: 39 sections -- 10 math proof sections, component-by-component breakdowns (15b/15c) generated live from the mass, buildability and operations ledgers, every specification key verbatim (15d), the runtime state machines + controls (15e), the complete function registry (15f), and the Foldmobile's own sections 20b/20c (the car-scale system map and the same-road-spot ephemeris in full). The same per-component detail plus barriers, feasibility, honesty checks, portal constructions, time machines, traversal tests, clock ledger, fuel economy, the mesh budget, module tables, the self-test coverage map, every hover spec-card, and the entire 39-section panel text verbatim lives in `Infornmational.md` (regenerate with `python _gen_info.py`). Press **H** for controls.

## The WD-88 Foldmobile -- the whole drive, car scale (SPECIAL WORKS)

The sixth tab is the same model at car scale: every WD-1 subsystem folded into a 4.40 m stainless gull-wing coupe -- the silhouette is the homage -- that drives a real road on four fusion-fed hub motors and fires its field transition at exactly **88 mph (39.33952 m/s)**. It is not a skin or an easter egg: it is a second audited machine with its own mass budget, power budget, operations ledger, thermal model, fault-injection rig and ephemeris solver, held to the same rule as the ship -- where the physics says impossible, the model says so and shows the number.

| Parameter | Value |
|-----------|-------|
| Kerbside mass | 1,410 kg -- derived, 25-line budget (parts 1,287 kg + crew/fluids/fit-out 122.9 kg); the driver is drawn because the budget books crew mass |
| Bubble radius | 2.90 m -- the smallest shell that encloses the coupe, 1/63 the ship's 183.44 m (hull 1/28: 4.40 m vs 124.76 m) |
| Wall thickness | 0.22 m (sigma = 4.5 /m) |
| Activation speed | 88 mph exactly -- an homage threshold, not physics; 87.9 mph held does NOT fire (selftest-asserted) |
| Top speed / derate | 130 mph ceiling; 55 mph when the cell is heat-soaked past 1,100 K |
| Powerplant | 2.5 MW trunk fusion cell (D-3He microtorus) + 4 hub motors -- **no gasoline engine of any kind** |
| Bus | 49 kW loads vs 2.5 MW supply -- margin +2.45 MW (a negative margin would fail the selftest) |
| KE at the trigger | 1.09 MJ -- well inside the SMES burst rating |
| Exotic bill @ 2.9 m | -1.29 x 10^44 J (-0.00072 M_sun of mass-energy) vs -56.2 J aboard in Casimir strips -- **42 orders short, honestly printed** |
| Thermal balance | 60 kJ/K cell; 3.0 m^2 louver bank, eps=0.88: idle 317 K, drive 752 K, stalled 1,278 K -> derate |
| Hop range | 60 s to 10 years, dialled live with `[`/`]` |

### Where the ship's systems went (the downscale map)

hull -> stainless monocoque | ring + 96 coils -> beltline field conduit run | pylons -> conduit standoffs | fore/aft cap rings -> nose + tail shaping hoops (elliptical -- they actually wrap the body sections) | fusion reactor -> trunk micro cell | SMES -> hood puck | Penning traps -> two under-floor bottles | Casimir lattice -> 12 conduit-liner strips | radiators -> rear-deck louver bank | cryoplant -> underbody He loop | rectenna -> roof whip | deflector -> nose strip | RCS pods -> tail bells + the four hub drives | magsail -> KE-recovery loop at the tail | navigator -> dash ephemeris unit | warp bubble -> exact 2.9 m shell | *plus two parts the ship doesn't need: the TRANSITION TRAIL (the scars on the road, hidden until the run fires) and the RUN SURFACE (the tarmac itself).*

### The homage contract

- **The flux capacitor is FOR SHOW** -- "wired to nothing heavier than an LED," per its own spec card. So are the time-circuit display, the TFC switch, the destination keypad and the folded lightning hook on the rear deck (the film's contact pole; this car charges through the shore port, not a 1.21 GW lightning strike). The selftest asserts the FOR SHOW label.
- **88 is a threshold, not physics** -- the bubble could fire at a standstill; the run-up is how you build the nerve to press it.
- **No gas engine** -- the selftest scans every part name for it.

### The same-road-spot solve (the reason the ephemeris unit exists)

The landing zone is fixed to **Earth**, not to space: between departure and arrival the same pavement rides Earth's orbit (~29.79 km/s) and sidereal spin (~0.385 km/s at the road's latitude) to a completely different inertial position. `car_transit()` solves both frames live -- first-order Kepler for heliocentric Earth (e = 0.0167 carried), sidereal rotation about a pole tilted 23.44 deg out of the ecliptic -- and stamps `dep`/`arr` on the same lat/lon/alt. The delta is split into the orbital leg (~2 AU on a half-year hop) and the spin leg (~4,000 km). **And heading:** S(t) rotates the whole local frame, so the lane's east vector lands as S(t1)*east -- the car arrives facing down the lane (45 deg of inertial lane rotation over a 3.7-day hop), not sideways. The TRANSIT panel previews the whole solve live before firing, with an ecliptic mini-map; under the nav fault it shows "EPHEMERIS LOST" instead of a frozen solve -- the one failure the whole machine exists to prevent. Stated limits: first-order e only (~2 km), no lunar perturbation/nutation/polar motion/bulge, mean 6,371 km radius -- a production run would swap in JPL DE440.

### Live faults and thermal honesty

The ops ledger's failure modes are live: the **FAULT** chip injects an SMES quench (88 mph is just driving -- no spike capacity), a louver stall (rejection x0.12 -> the cell heat-soaks to 1,278 K and the drive derates to 55 mph), or ephemeris drift (the transit solve is honestly lost). **PARK** stands the car down. The thermal integrator is bounded by the cell's own radiative equilibrium -- a hostile 10^9 s step cannot blow it up. Pausing holds the car's state mid-frame; `N` resets it completely.

## The physics (in one paragraph)

The Alcubierre metric (1994) describes a bubble of flat spacetime carried by a shift vector. The crew inside feel nothing -- no acceleration, no time dilation, no tidal forces. The space in front contracts; the space behind expands; the ship surfs the wave. The cost is the stress-energy that sources the metric: it is **negative** (exotic matter). For subluminal speeds (beta < 1), the Bobrick-Martire (2021) and Fuchs et al. (2024) constructions show that positive-energy shells can produce warp -- this is physically buildable in principle. For superluminal speeds (beta > 1), the Santiago-Schuster-Visser theorem (2022) proves that **any** warp drive violates the null energy condition -- this is a theorem about the whole class, not just Alcubierre's ansatz. The model computes both cases honestly.

## The engineering (in one paragraph)

The ship is accelerated by a 1000 km stellar-tap phased array beaming 6.4 x 10^18 W at a 4 km rectenna -- external infrastructure, re-specified at x8 power again for the heavier hull. The maximum speed (beta = 0.855, up from 0.562 at the original full scale) is emergent -- it falls out of the race between energy delivery and diffraction range. The 102.7 GW D-3He reactor (63.7 GW electric at the same 1.35x margin) runs housekeeping (coils, cryo, life support) but does not move the ship. Waste heat is radiated by 339,910 m^2 of graphite panels at 1550 K. Deceleration uses a 2,800 km magsail (~32,600 yr full stop -- longer than pass 6's 15,000 yr, the honest price of upscaling) or a destination photon brake (51 days at beta=0.5, requires infrastructure at Proxima). The Casimir lattice provides -3.09 MJ of real negative energy -- 41 orders of magnitude short of the -5.66 x 10^47 J the bubble would demand in superluminal (Alcubierre) mode; the ship never draws on this because it flies subluminal, positive-energy.

## How the ship reaches 85.5% of lightspeed (emergent, not declared)

The cruise speed beta = 0.855 is not a parameter -- it emerges from a race between two clocks. The full proofs are in info section **19k** (press I in the viewer), with 7 verified proof blocks.

**The energy clock:** KE = (gamma - 1) M c^2. The ship needs 90.0 YJ to reach beta=0.855. The gamma curve diverges at beta=1, so each knot closer to lightspeed costs more than the last: beta=0.9 needs 125.9 YJ (+40%), beta=0.99 needs 592.2 YJ (+6.6x).

**The range clock:** d_spot = 2.44 lambda L / D (Airy diffraction). The 1000 km aperture at 1.0 um produces a spot that grows linearly with distance. The 4 km rectenna captures 100% at 0.1 ly, 12% at 0.5 ly, 7.8% at 0.62 ly. Past 0.62 ly the beam is too weak to matter. Capture falls as 1/L^2.

**The race:** The boost integrates in 3-day steps. The ship starts at rest with 100% capture, then capture falls as it pulls away. After ~303 days the energy clock and range clock converge: the ship has 89.93 YJ and needs 90.02 YJ. At beta=0.87 it would need 100 YJ -- 11% short. That margin is why the cruise speed is 0.855 and not 0.87.

**The mass lever, run both ways:** Since KE = (gamma-1)Mc^2, the mass on the receiving end sets how high the ship climbs before it outruns the beam. Passes 1-5 shrank the ship 87% against a fixed 100 PW tap and the speed rose 52% (0.562 -> 0.857). Passes 6-7 grew it back x8 each time AND grew the tap x8 each time -- the emergent speed holds near 0.86 because tap/mass is roughly preserved. The relationship is superlinear in both directions -- the gamma curve makes each unit of delivered energy worth more than the last.

**Why it cannot reach beta=1:** At beta=1, gamma = infinity and KE = infinity. No finite beam can deliver infinite energy. This is special relativity, not engineering. The beam can push the ship arbitrarily close to c, but never to c. Three levers could raise the speed further (larger aperture, shorter wavelength, lighter ship or stronger tap), but none touch the gamma wall.

## The barriers (8 total)

| # | Barrier | Status | Gap |
|---|---------|--------|-----|
| 1 | Bubble wall tidal gradient | FAIL | 1.76e17 g vs 1 g (17 orders; unchanged by the upscale because the wall thickness, not the radius, sets the shear) |
| 2 | Superluminal NEC | THEOREM | SSV 2022: any v > c violates NEC |
| 3 | Negative energy scale | FAIL | 41 orders short of Casimir |
| 4 | Steering above beta=1 | THEOREM | causal disconnection |
| 5 | Thermal survival at 2c | FAIL | 1961 K vs 1900 K (passable, +13.5% more radiator area needed) |
| 6 | Ford-Roman wall thickness | THEOREM | QI limits wall to 100 L_Planck |
| 7 | QI throat hold time | THEOREM | 26 orders short |
| 8 | CTC chronology protection | CONJECTURE | Hawking 1992 |

**Score: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable** (except thermal at subluminal speeds).

## The portal (wormhole)

Four constructions are computed, all blocked:

| Construction | Exotic energy | Blocked by |
|-------------|--------------|------------|
| Morris-Thorne (12 m) | -2.42 x 10^44 J | QI: throat closes in 3.25e-26 s |
| Visser thin-shell (12 m) | -2.90 x 10^45 J | QI (concentrating costs MORE) |
| MMP (2020) | Casimir (real) | No magnetic monopoles observed |
| Survivable throat | -2.73 x 10^51 J | QI + 45 orders short of Casimir |

## The time machine (CTC)

Any wormhole with desynchronized mouths becomes a time machine when the time offset exceeds the light-time between mouths. The onset time is:

```
t_onset = (D/c) / |rate_A - rate_B|
```

For a 0.1 rate difference at Proxima distance: 42.5 years. Hawking's chronology protection conjecture expects the throat to be destroyed at the chronology horizon by divergent vacuum fluctuations.

### Maximum time travel (pushing to physical limits)

The desynchronization can be maximized by combining the deepest realistic gravity well with the highest realistic velocity, and placing the mouths as close together as possible. The `--send` report now includes scenarios 7-9 that push these levers to their physical extremes:

| Configuration | Rate difference | Mouth separation | CTC onset | Max jump (100 yr) |
|---------------|----------------|-----------------|-----------|-------------------|
| Neutron star + 0.99c rocket | 0.911 | 1 AU | 9.1 min | 91 yr past or future |
| Near-horizon + 0.999c rocket | 0.986 | 1 AU | 8.4 min | 98.6 yr past or future |

Key findings:
- **Both directions are the same offset** -- step A->B for the past, B->A for the future. The wormhole is symmetric.
- **CTC onset can be as fast as 8.4 minutes** (1 AU separation, extreme desync) -- but the throat is still closed.
- **The maximum backward/forward jump approaches the elapsed time** (98.6 yr offset after 100 yr) -- you can nearly jump the full elapsed time, but not more.
- **The warp drive itself produces almost no time shift**: +1.55 s gravitational drift over the 4.97 yr crossing (not controllable -- set by the Sol-Proxima gravitational potential difference), 0.0 s kinematic dilation (flat interior), and 0.0 desynchronization (cannot build a time machine). The fast thing cannot build the causality violation; the slow rocket can.

**All scenarios remain blocked** by at least one of: exotic energy (46 orders short of Casimir), quantum inequalities (throat closes in ~10^-22 s vs ~10^7 s traversal), or chronology protection (CTCs -> throat destruction). The maximum time jump is a mathematical result, not an engineering capability. The full proofs are in info section **19j** (press I in the viewer, or see `README.md` section 19j).

### Amplification: beyond a single wormhole

A single wormhole gives at most `elapsed` years of offset after `elapsed` years of desynchronization (rate_diff <= 1). To go further, the model computes five amplification mechanisms:

| Mechanism | Max offset (100 yr, extreme desync) | Scaling |
|-----------|-------------------------------------|---------|
| Single wormhole | 98.6 yr | elapsed * rate_diff |
| **Chain of N wormholes** | **985.9 yr (N=10)** | N * elapsed * rate_diff |
| Nested wormhole | 197.2 yr | outer + inner (additive) |
| Tipler cylinder | 4.25 yr (L=4.25 ly) | L * omega * R / c^2 |
| Gott cosmic strings | 445 yr (GUT, 1 ly) | delta * D / (4 pi) |
| Kerr black-hole CTC | ~0.3 ms/orbit | 2*pi*a/c per orbit |

**Winner: chain of wormholes.** Each wormhole contributes elapsed * rate_diff independently; N mouths give N * elapsed * rate_diff. The exotic-energy bill and all barriers scale the same way -- no barrier is avoided, only multiplied.

### Multi-jump: continuous forward/backward travel

Each cycle = hop through a desynchronized throat + external return leg at beta (Delta = D/(beta c), costing cruise_load * Delta of ship energy). The mouths keep desyncing meanwhile, so offsets grow:

| Direction | Recurrence | Result (100 yr, extreme desync, 1 AU, beta=0.855) |
|-----------|-----------|---------------------------------------------------|
| Backward (A->B hops) | t <- t(1-r) + Delta -> t* = Delta/r | ~100.0 yr reachable (elapsed - t*), converges in ~3-4 cycles vs 91-98.6 yr for one jump |
| Forward (B->A hops) | t <- t(1+r) + Delta, geometric | ~95,000 yr in 10 cycles ((1+r)^k growth) |

Net-backward requires delta > Delta > D/c -- the loop only works after single-hop CTCs already exist, so it multiplies chronology-protection exposure rather than evading it.

**Energy/refueling**: per 1 AU cycle at beta=0.855 the ship burns ~0.098 kg D-3He (21.5 TJ housekeeping during the leg) but scoops only ~6e-2 kg of enrichable D-3He from the magsail's ISM flux -- **net-NEGATIVE at every speed now**: the pass-7 burn floor already exceeds slow-beta yield and burn grows ~b^2 against the linear yield (best case ~-0.72 kg/day near 0.25c). The scoop is dead weight at this scale -- honest, printed, not hidden. Parked ships burn ~0.5 kg/day with no scoop. The exotic throat energy per hop stays flagged separately -- it is a physics barrier, not a fuel problem.

## The teleporter (quantum, for contrast)

Quantum teleportation is real (Bennett 1993, Micius satellite 2017, 1400 km). It does none of the things a portal does:

- Moves a quantum **state**, not matter
- Requires pre-shared entanglement
- Classical channel capped at c (no FTL)
- No-cloning: the original is destroyed
- Teleporting one person: 7 x 10^29 bits at 1 Tb/s = 2.22 x 10^10 years = 1.61 universe ages

## Verification

| Suite | Count | Result |
|-------|-------|--------|
| Self-test | 417/417 | ALL PHYSICS CHECKS PASS |
| Portal/time-travel | 66/66 | 0 FAILURES |
| Honesty layer | 12/12 | HONEST -- nothing created from nothing |
| Draw paths | 7/7 | ALL OK |
| Info panel sections | 39 | 10 math/barrier proof sections + component-by-component breakdowns (15b/15c/15d) + Foldmobile 20b/20c |
| Dimensional analysis | 28/28 | All units correct |
| Cross-formula consistency | 11/11 | All agree |
| Barrier analysis | 8/8 | All barriers verified |
| Numerical stability | 34/34 | Edge cases verified (extreme params, boundaries) |

## Files

| File | Purpose |
|------|---------|
| `Warpdrive.py` | The model (Python + Pygame, ~17,000 lines: ship + portal + time machine + the WD-88 Foldmobile) |
| `README.md` | Full formulas, proofs, and computed values |
| `overview.md` | This file -- what it is, what changed, why |
| `howitworks.md` | Step-by-step walkthrough of the physics pipeline |
| `Infornmational.md` | Everything documented, generated live by `_gen_info.py`: components, all 120 spec keys, derived quantities, barriers, feasibility, honesty checks, portals, time machines, state machines, controls, CLI, all functions/classes, mesh budget, self-test map, spec cards and the verbatim info panel |
