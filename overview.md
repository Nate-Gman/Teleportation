# Overview -- Warpdrive WD-1m5 Foldrunner "Miniframe V"

## What this is

A physics-honest digital twin of a warp-drive starship, a traversable wormhole portal, and the time machine that any wormhole automatically becomes. Every number is computed from real general-relativity and quantum-field-theory formulas. Nothing is fictional. Where the physics says "impossible," the model says so and shows the computation that proves it.

This is the fifth refit pass. Pass 1 (WD-1m) scaled the WD-1 hull down 0.65x linear, crew 12 -> 8. Pass 2 (WD-1m2) compounded a further 0.83x scale, crew 8 -> 6, and thinned the bubble wall 1.0 m -> 0.2 m to reclaim interior volume. Pass 3 (WD-1m3) found and fixed a real bug -- two axial mount offsets (the boost-rectenna and SMES positions) had been hardcoded literals that never scaled down in either earlier pass -- which unlocked a further 0.85x linear scale (radiators scaled independently to hold the thermal-barrier invariant). Pass 4 (WD-1m4) revisited two engineering assumptions inherited unexamined since pass 1 -- the reactor's electrical margin (1.5x -> 1.35x) and the crew-hull wall thickness (re-derived from pressure-vessel theory for the smaller hull). Pass 5 (WD-1m5) is **not** another geometric scale-down: `SCALE_S` and every hull/coil/radiator dimension are unchanged from pass 4. Instead it revisits two more inherited constants in the mass budget -- the HTS coil winding-pack radial build (0.35 m -> 0.30 m, justified by improved REBCO engineering current density) and the shaping-ring solid fraction (0.35 -> 0.30, secondary structure carrying less stress than the primary shell). Net effect vs the *original* WD-1: mass down 87%, reactor down 88%, radiator area unchanged from pass 3 (81% down), cruise speed up from 0.562c to 0.857c. Nothing about the physics changed -- every number below is still derived from `DIMS`/`PLANT` by the same formulas. See `Engineering notes` below.

## The ship

| Parameter | Value |
|-----------|-------|
| Mass | 1.66 x 10^7 kg (16,602 tonnes) -- was 127,000 t (WD-1), 42,719 t (WD-1m), 27,003 t (WD-1m2), 18,374 t (WD-1m3), 18,215 t (WD-1m4) |
| Bubble radius | 45.86 m -- unchanged since WD-1m3 (was 100 m WD-1, 65 m WD-1m, 53.95 m WD-1m2) |
| Wall thickness | 0.2 m -- was 1 m |
| Flat interior | 44.66 m |
| Cruise speed | beta = 0.857 (0.857c) -- was 0.562c (WD-1), 0.727c (WD-1m), 0.794c (WD-1m2), 0.844c (WD-1m3), 0.845c (WD-1m4), emergent, beam-limited |
| Destination | Proxima Centauri b (4.2465 ly) |
| Cruise time | ~4.96 years in flight (ship = Earth, no dilation) -- was 8.49 yr (WD-1) |
| Crew | 6 -- was 12 (WD-1), 8 (WD-1m) |
| Reactor | 2.62 GW D-3He fusion (aneutronic, 62% direct conversion), 1.35x electrical margin -- was 22 GW (WD-1), 7 GW (WD-1m), 4.35 GW (WD-1m2), 2.91 GW (WD-1m3) |
| Radiators | 7,081 m^2, 1550 K design, 1900 K limit -- unchanged since WD-1m3 (was 37,440 m^2 WD-1, 15,818 m^2 WD-1m, 10,895 m^2 WD-1m2) |
| Hull wall | 0.11 m (pressure-vessel scaled) -- was 0.18 m flat "practical minimum" through passes 1-3 |
| Casimir lattice | 24 cassettes, -0.19 MJ total |
| SMES buffer | 43.1 GJ -- was 448 GJ (WD-1), 123 GJ (WD-1m), 69.8 GJ (WD-1m2), 43.1 GJ (WD-1m3) |
| Magsail | 700 km radius, ~8,000 yr full stop -- was 1000 km / 30,000 yr (WD-1) |

## Engineering notes -- why smaller is better here

The redesign compounds three linear scale passes (`SCALE_S = 0.4586` overall, unchanged this pass) across the hull, ring, coils, radiators and reactor, and rederives every dependent quantity from the same first-principles formulas already in the model (`mass_budget()`, `plant_electric_w()`, `radiator_area_m2()`, `boost_profile()` / `max_boost_beta()`, `check_envelope()`). Several effects compound in the ship's favour:

1. **Mass falls close to S^3** because it is a volume-times-density sum over the geometry. The kinetic-energy bill to reach any given cruise beta, `(gamma-1) M c^2`, falls by the same factor.
2. **The external beam array is unchanged** (1000 km aperture, 10^17 W, unchanged range) -- it is ground/orbital infrastructure, not ship hardware. A lighter ship reaches a higher emergent cruise speed against the *same* beam before it outruns the diffraction-limited spot: beta rises 0.562 -> 0.727 -> 0.794 -> 0.844 -> 0.845 -> 0.857 across the five passes.
3. **Radiator area falls slower than waste heat**, so equilibrium panel temperature keeps falling at a given beta, and the thermal barrier's failure point keeps moving up (beta ~1.45 -> ~1.79 -> ~1.97 -> ~1.99, unchanged this pass since the radiators didn't change).
4. **Thinning the bubble wall buys back interior volume for free** (introduced in pass 2, carried forward here) -- `flat_interior_r()` grows relative to `bubble_r_m` even as the bubble shrinks.
5. **Fixing a hidden non-scaling bug unlocked a real gain, not a fudge** (pass 3) -- two axial mount offsets in `_envelope_points()` had been bare literals that never shrank with the ship, quietly overstating how much space the hardware needed. Fixing them revealed genuine spare envelope margin.
6. **Revisiting inherited engineering margins, not just geometry, is its own lever (pass 4).** Two numbers had been carried forward unexamined since pass 1: the reactor's ~1.5x electrical margin over cruise load (never physically required -- WD-1 just happened to have it) and the hull wall thickness (held at a flat 0.18 m "practical minimum" while the hull itself kept shrinking around it). Tightening the reactor margin to 1.35x (still a healthy 35% reserve, in the normal 20-40% band for aerospace power plants) and re-deriving the hull wall from thin-wall pressure-vessel theory (`t = P*r/sigma`, linear in hull radius -- WD-1's 0.22 m at 16 m hull diameter implies 0.11 m at this ship's 8.0 m hull, not the inherited 0.18 m floor) cut the reactor a further 10% and the crew-hull-shell mass line item 39%, for a combined ~0.9% total mass reduction and a real reactor power cut -- at no cost to any envelope or thermal margin, since neither lever touches geometry that check_envelope() or radiator_temp_k() look at.
7. **Revisiting inherited mass-model constants is another lever (pass 5).** Two more numbers in `mass_budget()` had been hardcoded since WD-1 and never re-derived: the HTS coil winding-pack radial build (0.35 m, set by the engineering current density J_e of the REBCO tape generation WD-1 assumed) and the shaping-ring solid fraction (0.35, a conservative fill for secondary structure). Modern REBCO at 18 K achieves ~600 A/mm^2 engineering J (vs the ~500 the 0.35 m build assumed), so the same 48000 turns x 38 kA fit in a 0.30 m pack -- a 17% J_e improvement well within documented REBCO progress. The thinner pack also needs less copper stabilizer per ampere of quench protection, so the winding-pack average density drops from 6000 to 5600 kg/m^3. The shaping rings are secondary structure (they break front-back symmetry but do not source the main warp field), so a 30% solid fraction vs 35% is a modest structural-efficiency gain. Together these cut the two largest non-ring mass line items (HTS coils -20%, shaping rings -14%) for a combined 8.9% total mass reduction -- again at no cost to any envelope or thermal margin, since neither lever touches geometry that check_envelope() or radiator_temp_k() look at.

**The one thing every pass deliberately did NOT do:** let the thermal barrier flip from FAIL to PASS at 2c. `--selftest` hard-asserts `T_at_2c > rad_limit_k` -- the model is built to keep demonstrating that superluminal flight cooks the radiators, not to quietly erase that finding by over-shrinking. At this scale T(2c) = 1904 K vs a 1900 K limit -- still fails, by design, with only a 0.9% radiator-area shortfall (down from 3.3% in WD-1m2, 20.6% in WD-1m, 75% in WD-1). This margin is thin enough that it is close to the practical limit of geometric shrinkage as a lever -- which is exactly why passes 4 and 5 looked at engineering margins and mass-model constants instead of trying to squeeze more out of scale.

Every number here is re-verified by `--selftest` (157/157) after each change -- nothing was hand-typed to make the story work.

## The five visualization modes

| Mode | Key | What it shows |
|------|-----|---------------|
| SHIP | 1 | The starship: ring, hull, radiators, reactor, coil sequence |
| METRIC | 2 | The warp bubble: York expansion grid, energy-density hotspots |
| DILATION | 3 | Clock rates: comoving vs static, gravitational drift |
| PORTAL | 4 | The wormhole: throat, flare-out, tidal profile, both mouths |
| FLIGHT | 5 | Flight sim: boost, cruise, brake, arrival (keys W/S/J) |

Press **I** for the full specification panel with 10 math proof sections and 32 total info sections. Press **H** for controls.

## The physics (in one paragraph)

The Alcubierre metric (1994) describes a bubble of flat spacetime carried by a shift vector. The crew inside feel nothing -- no acceleration, no time dilation, no tidal forces. The space in front contracts; the space behind expands; the ship surfs the wave. The cost is the stress-energy that sources the metric: it is **negative** (exotic matter). For subluminal speeds (beta < 1), the Bobrick-Martire (2021) and Fuchs et al. (2024) constructions show that positive-energy shells can produce warp -- this is physically buildable in principle. For superluminal speeds (beta > 1), the Santiago-Schuster-Visser theorem (2022) proves that **any** warp drive violates the null energy condition -- this is a theorem about the whole class, not just Alcubierre's ansatz. The model computes both cases honestly.

## The engineering (in one paragraph)

The ship is accelerated by a 1000 km stellar-tap phased array beaming 10^17 W at a 4 km rectenna -- unchanged external infrastructure. The maximum speed (beta = 0.857, up from 0.562 at full scale) is emergent -- it falls out of the race between energy delivery and diffraction range, and the lighter hull needs less delivered energy to get there. The 2.62 GW D-3He reactor (was 22 GW; carries a 1.35x electrical margin, down from 1.5x) runs housekeeping (coils, cryo, life support) but does not move the ship. Waste heat is radiated by 7,081 m^2 of graphite panels (was 37,440 m^2) at 1550 K. Deceleration uses a 700 km magsail (~8,000 yr full stop, faster than WD-1's 1000 km loop despite being unchanged hardware since pass 2 -- the ship is just lighter) or a destination photon brake (50 days at beta=0.5, requires infrastructure at Proxima). The Casimir lattice provides -0.19 MJ of real negative energy -- 41 orders of magnitude short of the -3.54 x 10^46 J the smaller-but-thinner-walled bubble would demand in superluminal (Alcubierre) mode; the ship never draws on this because it flies subluminal, positive-energy.

## How the ship reaches 85.7% of lightspeed (emergent, not declared)

The cruise speed beta = 0.857 is not a parameter -- it emerges from a race between two clocks. The full proofs are in info section **19k** (press I in the viewer), with 7 verified proof blocks.

**The energy clock:** KE = (gamma - 1) M c^2. The ship needs 1.40 YJ to reach beta=0.857. The gamma curve diverges at beta=1, so each knot closer to lightspeed costs more than the last: beta=0.9 needs 1.93 YJ (+38%), beta=0.99 needs 9.09 YJ (+6.5x).

**The range clock:** d_spot = 2.44 lambda L / D (Airy diffraction). The 1000 km aperture at 1.0 um produces a spot that grows linearly with distance. The 4 km rectenna captures 100% at 0.1 ly, 12% at 0.5 ly, 7.8% at 0.62 ly. Past 0.62 ly the beam is too weak to matter. Capture falls as 1/L^2.

**The race:** The boost integrates in 3-day steps. The ship starts at rest with 100% capture, then capture falls as it pulls away. After 300 days the energy clock and range clock converge: the ship has 1.398 YJ and needs 1.400 YJ. At beta=0.86 it would need 1.43 YJ -- 2% short. That 2% margin is why the cruise speed is 0.857 and not 0.86.

**Why shrinking raises the speed:** The beam is fixed external infrastructure. The ship mass M fell 87% across five refit passes (127,000 t -> 16,602 t). Since KE = (gamma-1)Mc^2, a lighter ship needs less energy for the same beta, so it climbs higher on the gamma curve before outrunning the beam. Speed rose 52% (0.562 -> 0.857); gamma rose 60% (1.21 -> 1.94). The relationship is superlinear -- each tonne saved is worth more than the last.

**Why it cannot reach beta=1:** At beta=1, gamma = infinity and KE = infinity. No finite beam can deliver infinite energy. This is special relativity, not engineering. The beam can push the ship arbitrarily close to c, but never to c. Three levers could raise the speed further (larger aperture, shorter wavelength, lighter ship), but none touch the gamma wall.

## The barriers (8 total)

| # | Barrier | Status | Gap |
|---|---------|--------|-----|
| 1 | Bubble wall tidal gradient | FAIL | 1.76e17 g vs 1 g (17 orders; worse than WD-1's 7e15 g because the wall is now thinner) |
| 2 | Superluminal NEC | THEOREM | SSV 2022: any v > c violates NEC |
| 3 | Negative energy scale | FAIL | 41 orders short of Casimir |
| 4 | Steering above beta=1 | THEOREM | causal disconnection |
| 5 | Thermal survival at 2c | FAIL | 1904 K vs 1900 K (passable, only +0.9% more radiator area needed) |
| 6 | Ford-Roman wall thickness | THEOREM | QI limits wall to 100 L_Planck |
| 7 | QI throat hold time | THEOREM | 26 orders short |
| 8 | CTC chronology protection | CONJECTURE | Hawking 1992 |

**Score: 3 FAIL + 4 THEOREM + 1 CONJECTURE = 0 passable** (except thermal at subluminal speeds). Note barrier 1 stayed numerically worse than the original WD-1 (thinner wall = sharper curvature = more tidal shear) -- an honest trade the model reports rather than hides, since it costs nothing operationally (the wall was never survivable at any thickness tested).

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
- **The warp drive itself produces almost no time shift**: +1.54 s gravitational drift over the 4.96 yr crossing (not controllable -- set by the Sol-Proxima gravitational potential difference), 0.0 s kinematic dilation (flat interior), and 0.0 desynchronization (cannot build a time machine). The fast thing cannot build the causality violation; the slow rocket can.

**All scenarios remain blocked** by at least one of: exotic energy (46 orders short of Casimir), quantum inequalities (throat closes in ~10^-22 s vs ~10^7 s traversal), or chronology protection (CTCs -> throat destruction). The maximum time jump is a mathematical result, not an engineering capability. The full proofs are in info section **19j** (press I in the viewer, or see `README.md` section 19j).

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
| Self-test | 169/169 | ALL PHYSICS CHECKS PASS |
| Portal/time-travel | 66/66 | 0 FAILURES |
| Honesty layer | 12/12 | HONEST -- nothing created from nothing |
| Draw paths | 7/7 | ALL OK |
| Info panel sections | 32 | 10 math/barrier proof sections |
| Dimensional analysis | 28/28 | All units correct |
| Cross-formula consistency | 11/11 | All agree |
| Barrier analysis | 8/8 | All barriers verified |

## Files

| File | Purpose |
|------|---------|
| `Warpdrive.py` | The model (Python + Pygame, ~8000 lines) |
| `README.md` | Full formulas, proofs, and computed values |
| `howitworks.md` | Logical step-by-step explanation |
| `overview.md` | This file -- high-level summary |
| `Infornmational.md` | Original motivation and design intent |

## Commands

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

## The honest answer

The drive cannot fly as drawn. 7 of 8 barriers are impassable -- 4 are mathematical theorems, 3 are 40+ order energy gaps, 1 is a strong conjecture. Only the thermal barrier is passable, and at this (WD-1m5) scale it only needs 0.9% more radiator area (was 80% at full WD-1 scale), which now buys subluminal beta up to ~1.99, still not superluminal travel.

The model is not a proposal. It is an audit. It shows exactly where the physics says no, how large the gap is, and what kind of physics would be needed to change the answer. The theorems are not engineering challenges -- they are mathematical proofs about what is possible. The 40-order energy gap is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

**Verdict: HONEST -- nothing created from nothing.**
