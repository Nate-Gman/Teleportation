# Overview -- Warpdrive WD-1 Foldrunner

## What this is

A physics-honest digital twin of a warp-drive starship, a traversable wormhole portal, and the time machine that any wormhole automatically becomes. Every number is computed from real general-relativity and quantum-field-theory formulas. Nothing is fictional. Where the physics says "impossible," the model says so and shows the computation that proves it.

## The ship

| Parameter | Value |
|-----------|-------|
| Mass | 1.27 x 10^8 kg (127,000 tonnes) |
| Bubble radius | 100 m |
| Wall thickness | 1 m |
| Flat interior | 94 m |
| Cruise speed | beta = 0.562 (0.562c) |
| Destination | Proxima Centauri b (4.2465 ly) |
| Cruise time | 8.49 years (ship = Earth, no dilation) |
| Crew | 12 |
| Reactor | 22 GW D-3He fusion (aneutronic, 62% direct conversion) |
| Radiators | 37,440 m^2, 1550 K design, 1900 K limit |
| Casimir lattice | 24 cassettes, -2 MJ total |
| SMES buffer | 448 GJ |
| Magsail | 1000 km radius, 30,000 yr full stop |

## The five visualization modes

| Mode | Key | What it shows |
|------|-----|---------------|
| SHIP | 1 | The starship: ring, hull, radiators, reactor, coil sequence |
| METRIC | 2 | The warp bubble: York expansion grid, energy-density hotspots |
| DILATION | 3 | Clock rates: comoving vs static, gravitational drift |
| PORTAL | 4 | The wormhole: throat, flare-out, tidal profile, both mouths |
| FLIGHT | 5 | Flight sim: boost, cruise, brake, arrival (keys W/S/J) |

Press **I** for the full specification panel with 8 math proof sections and 30 total info sections. Press **H** for controls.

## The physics (in one paragraph)

The Alcubierre metric (1994) describes a bubble of flat spacetime carried by a shift vector. The crew inside feel nothing -- no acceleration, no time dilation, no tidal forces. The space in front contracts; the space behind expands; the ship surfs the wave. The cost is the stress-energy that sources the metric: it is **negative** (exotic matter). For subluminal speeds (beta < 1), the Bobrick-Martire (2021) and Fuchs et al. (2024) constructions show that positive-energy shells can produce warp -- this is physically buildable in principle. For superluminal speeds (beta > 1), the Santiago-Schuster-Visser theorem (2022) proves that **any** warp drive violates the null energy condition -- this is a theorem about the whole class, not just Alcubierre's ansatz. The model computes both cases honestly.

## The engineering (in one paragraph)

The ship is accelerated by a 1000 km stellar-tap phased array beaming 10^17 W at a 4 km rectenna. The maximum speed (beta = 0.562) is emergent -- it falls out of the race between energy delivery and diffraction range. The 22 GW D-3He reactor runs housekeeping (coils, cryo, life support) but does not move the ship. Waste heat is radiated by 37,440 m^2 of graphite panels at 1550 K. Deceleration uses a 1000 km magsail (30,000 yr full stop) or a destination photon brake (381 days at beta=0.5, requires infrastructure at Proxima). The Casimir lattice provides -2 MJ of real negative energy -- 40 orders of magnitude short of the -3.36 x 10^46 J the bubble demands.

## The barriers (8 total)

| # | Barrier | Status | Gap |
|---|---------|--------|-----|
| 1 | Bubble wall tidal gradient | FAIL | 7e15 g vs 1 g (16 orders) |
| 2 | Superluminal NEC | THEOREM | SSV 2022: any v > c violates NEC |
| 3 | Negative energy scale | FAIL | 40 orders short of Casimir |
| 4 | Steering above beta=1 | THEOREM | causal disconnection |
| 5 | Thermal survival at 2c | FAIL | 2187 K vs 1900 K (passable) |
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
| Self-test | 157/157 | ALL PHYSICS CHECKS PASS |
| Portal/time-travel | 66/66 | 0 FAILURES |
| Honesty layer | 12/12 | HONEST -- nothing created from nothing |
| Draw paths | 7/7 | ALL OK |
| Info panel sections | 30 | 8 math/barrier proof sections |
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

The drive cannot fly as drawn. 7 of 8 barriers are impassable -- 4 are mathematical theorems, 3 are 40+ order energy gaps, 1 is a strong conjecture. Only the thermal barrier is passable, and only with 80% more radiator area, which buys subluminal beta ~ 1.45, not superluminal travel.

The model is not a proposal. It is an audit. It shows exactly where the physics says no, how large the gap is, and what kind of physics would be needed to change the answer. The theorems are not engineering challenges -- they are mathematical proofs about what is possible. The 40-order energy gap is not a budget shortfall -- it is the difference between what the universe provides and what the metric demands.

**Verdict: HONEST -- nothing created from nothing.**
