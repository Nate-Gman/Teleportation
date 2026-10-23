# Informational -- WD-1u4 Foldrunner, every component explained

> Generated from the live model by `_gen_info.py` -- every number below is pulled from `DIMS`, `PLANT`, `DRIVE`, `mass_budget()`, `buildability_ledger()` and `operations_ledger()`, and every specification key is printed with the engineering comment attached to it in the source. Nothing is typed by hand. If the ship changes, regenerate with `python _gen_info.py` and the document follows it.

This is the component-by-component reference. For formulas and proofs see `README.md`; for the refit history see `overview.md`; for the physics narrative see `howitworks.md`.

## The ship at a glance

| Parameter | Value |
|-----------|-------|
| Dry mass | 1.081e+06 t (1,081,381 tonnes) |
| Bubble radius | 183.44 m (flat interior 182.2 m) |
| Envelope | ~426 m span x ~195 m length; binding part: radiator tip at 152.8 m (29.4 m clear) |
| Emergent cruise beta | 0.8547 -- not declared, derived |
| Route | Sol -> Proxima Centauri b (4.2465 ly), ~4.97 yr ship = Earth |
| Crew | 24 |
| Reactor | 102.70 GW th -> 63.7 GW el (62% direct conversion) |
| Radiators | 339,909 m^2 at 1550 K design / 1900 K graphite limit |
| Stellar tap | 6.4e+18 W from a 1000 km array at 1 um, usable to 0.62 ly |
| Casimir onboard | -3.09 MJ vs 5.656e+47 J demanded at beta=1 (41.3 orders short) |

## Ship components

All 17 lines of the mass budget, in buildability order. Each entry shows role, spec, mass share, per-unit mass, what it draws, what its failure costs, and how far away the hardware is. Ratings: **TODAY** (exists, only scale missing), **NEAR** (physics proven, engineering not), **FAR** (needs an industry nobody has), **OPEN** (a material nobody has made), **IMPOSSIBLE** (barred by theorem).

### 1. WARP RING SHELL -- 4.412e+05 t (40.8% of ship)   [OPEN]

**What it is:** the shift-vector shell -- a 367 m centreline torus of 96 sectors that IS
the wall's source term; its stress-energy is where the metric's curvature lives.

**Dimensions & placement:** ~394 x 394 m cross-section x 26.8 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** one sector is a 12.0061 m arc segment of the 27.52 m ring tube -- 96
wedge shells that close into the torus.

**Mounts at:** hangs on the 12 pylons at the ring plane -- the ring is the spine's
payload, not the spine.

**Role:** the drive itself -- a 96-sector SiC/W torus whose stress-energy distribution
sources the shift-vector field that carries the bubble.

**Why it must exist:** without it there is no wall -- the shape function needs a
stress-energy source AT r=R; remove it and there is no drive.

**Per unit:** 4596 t each x 96 sector.

**Material:** SiC/W metamaterial at 4,100 kg/m^3 (`ring_density`).

**Mass derivation:** torus shell: 4pi^2 R_m r_m x ring_wall_m x rho -- the shell area of
the 366.9 m torus times its 1.08 m wall.

**Spec:** 96 sectors, torus 366.9 m major x 27.5 m minor dia, 1.08 m wall, SiC/W
metamaterial at 4100 kg/m3 -- plus a stress-energy state no foundry can write

**Buildability:** The shell itself is ordinary composite engineering. What it must do is
not: the positive-energy warp solutions need anisotropic stresses comparable to the
energy density -- sound speed nearing c. No known material does this. A materials
problem, not a relativity problem.

**Closest real hardware:** nothing -- metamaterial cloaks exist, but none carry
relativistic stress-energy.

**Operations:** draws 4944.8 MW servo control share -- continuous while the shell is
shaped.

**Active during:** shaped phases only -- BOOST through CRUISE; dead hardware in DOCK and
freefall.

**Power share:** 10.5% of the 47.1 GW beta=0.99 cruise load.

**Mission ledger:** held the shape that carried 1.5e+25 J peak kinetic over the voyage
-- the shell's servo share ran the whole cruise.

**Failure mode:** sector servo loss -> shape error -> integrity drains toward collapse;
the ship falls out of warp, it does not explode

**Cascade:** sector loss -> shape error -> integrity drains -> collapse to subluminal --
survivable, mission over.

**Thermal:** sits at the bubble wall; servo and coil losses around it leave only through
the radiators -- no conduction path off the ship exists.

**Connects to:** carries the 96 field coils around its tube, houses the Casimir
cassettes in its wall, tied to the hull by the 12 pylons; energized by the plant through
the SMES buffer.

**Required by:** the coils wrap it and the bubble is written on it -- warp mode is
impossible without it.

**Verified by:** mass recomputed in _scale_audit; 'ring straddles the wall' selftest;
exact mass match vs mass_budget.

**Governed by:** `ring_major_d_m`=366.88, `ring_minor_d_m`=27.52, `ring_wall_m`=1.08, `ring_sectors`=96, `ring_density`=4,100

**In the viewer:** labelled `MAIN WARP RING (96 sectors)` -- assembly step 7 of 17; slides 78 m forward when exploded -- click it on the SHIP tab to isolate or explode it.

### 2. SHAPING RINGS -- 5.489e+04 t (5.1% of ship)   [OPEN]

**What it is:** fore and aft rings that break the front-back symmetry of the shift
field, making the bubble directional rather than a spherical pinch.

**Dimensions & placement:** two rings, each ~188 m diameter x 12.8 m axial, straddling
the ring plane (fore and aft stations).

**Unit size:** each ring is a 12.84 m tube bent into a 176.08 m circle.

**Mounts at:** mounted fore and aft of the ring plane at cap_offset_m =69.72 m.

**Role:** fore/aft torus pair that closes the bubble's shift-vector geometry ahead of
and behind the ring plane.

**Why it must exist:** a bare spherical shell pinches fore and aft equally -- these make
the bubble directional; without them the ship sits inside a symmetric pinch.

**Material:** same metamaterial as the ring at 4,100 kg/m^3 (`ring_density`).

**Mass derivation:** 2 x (4pi^2 R_c r_c x capring_wall_frac x rho) -- two torus shells
at 30% solid fraction.

**Spec:** 2 rings, 176.1 m major x 12.8 m minor dia, 69.72 m offset, 30% solid fraction,
same metamaterial, same unsolved sourcing

**Buildability:** Same wall, same verdict: drivable geometry is buildable, the
stress-energy it has to carry is not.

**Closest real hardware:** nothing -- no machine on Earth shapes a metric.

**Operations:** draws 2119.2 MW servo control share -- continuous while the shell is
shaped.

**Active during:** same as the main shell -- only live while the bubble is up.

**Power share:** 4.5% of the 47.1 GW beta=0.99 cruise load.

**Mission ledger:** kept the front-back asymmetry for 9.00 yr of shaped cruise.

**Failure mode:** same as the main shell: shape error, integrity drain, collapse

**Cascade:** lost asymmetry -> degraded fold -> the bubble still holds but stops being
directional.

**Thermal:** same regime as the main shell -- shaped hardware whose losses must all
radiate.

**Connects to:** mounted with the ring assembly -- they reshape the same field the coils
energise.

**Required by:** the bubble's directionality needs them -- without the asymmetry the
metric is symmetric and goes nowhere.

**Verified by:** mass recomputed in _scale_audit; envelope check (reach 117.4 m).

**Governed by:** `capring_d_m`=176.08, `capring_minor_d_m`=12.84, `cap_offset_m`=69.72, `capring_wall_frac`=0.3

**In the viewer:** labelled `FORE SHAPING RING` and `AFT SHAPING RING`.

### 3. HTS FIELD COILS -- 2.465e+05 t (22.8% of ship)   [NEAR]

**What it is:** REBCO high-temperature-superconductor windings, one per ring sector --
they do not push on anything; they hold the shell's stress-energy in the shape the
metric requires.

**Dimensions & placement:** ~395 x 395 m cross-section x 28.4 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** each coil is a 27.92 m bore x 0.3 m winding build x 17.24 m long annular
pack around one tube sector.

**Mounts at:** wrapped around the ring tube with 0.2 m standoff (coil_standoff_m) --
they float on the shell they drive.

**Role:** the actuators -- one REBCO coil per ring sector shapes the wall curvature in
real time (the steering wheel of a warp drive).

**Why it must exist:** the shell is only a shape until the coils energise it -- no
field, no metric source.

**Per unit:** 2568 t each x 96 coil.

**Material:** REBCO winding pack at 5,600 kg/m^3 (`coil_density`).

**Mass derivation:** coils x pi((r_i+coil_build_m)^2 - r_i^2) x coil_len_m x rho, where
r_i = ring minor radius + standoff -- an annular winding pack wrapped around the tube it
energises.

**Spec:** 96 coils x 48000 turns, 27.92 m bore x 17.24 m pack, 38 kA at 18 K, 0.30 m
winding build at 5600 kg/m3 -- ~408526 km of REBCO tape total, quench protection per
sector, 38252.8 MW of AC ripple loss to sink

**Buildability:** REBCO tape is demonstrated in SPARC-class machines. 96 sectors held at
18 K on a 183 m radius is scaling work, not new physics.

**Closest real hardware:** SPARC's TF coils (MIT/CFS, 20 T REBCO, 2021) -- the same
tape, orders more of it.

**Operations:** draws 38252.8 MW AC ripple at beta=1 (scales beta^2) + 18 K hold --
continuous in warp mode.

**Active during:** every shaped phase; idle load is the 18 K cryo hold even when not
steering.

**Power share:** 81.2% of the 47.1 GW beta=0.99 cruise load.

**Mission ledger:** carried the shaped field for the full cruise leg -- ripple losses
are inside the 7.16e+18 J radiated total.

**Failure mode:** a quench dumps the field into the cryostat -- trip to subluminal

**Cascade:** quench -> field energy into the cryostat -> collapse; the SMES exists
precisely to intercept this.

**Thermal:** held at 18 K; AC ripple plus hold heat lifts through the cryoplant into the
radiators -- a few degrees of margin separates field from quench.

**Connects to:** wrapped around the ring tube (bore clears it), fed DC through the SMES
buffer, held at 18 K by the cryoplant.

**Required by:** required by the shell shape, and therefore the bubble -- and they are
why the cryoplant and SMES exist.

**Verified by:** coil-bore derivation check in _scale_audit (bore clears the tube it
energises); mass recompute.

**Governed by:** `coils`=96, `coil_bore_m`=27.92, `coil_len_m`=17.24, `coil_turns`=48,000, `coil_current_a`=38,000, `coil_temp_k`=18, `coil_build_m`=0.3, `coil_standoff_m`=0.2, `coil_density`=5,600

**In the viewer:** labelled `HTS FIELD COILS (96)` -- assembly step 8 of 17; slides 116 m forward when exploded -- click it on the SHIP tab to isolate or explode it.

### 4. CREW HULL SHELL -- 1.311e+04 t (1.2% of ship)   [TODAY]

**What it is:** the pressure hull -- a ~32 m x ~195 m pressure vessel living inside the
flat interior (f=1) where there is no tidal shear.

**Dimensions & placement:** ~32 x 32 m cross-section x 124.8 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** one pressure vessel 32 m dia x 124.76 m long -- a single welded shell,
not an assembly.

**Mounts at:** the spine -- everything forward-mounted hangs off it; it is the mount,
not the mounted.

**Role:** the pressure vessel -- 12-deck habitat for the crew, sitting in flat spacetime
so it carries no dynamic loads.

**Why it must exist:** the only place f=1 -- outside the flat interior, tidal shear is
lethal; without a pressure hull in that pocket there is nowhere to put people.

**Material:** hull alloy at 2,700 kg/m^3 (`hull_density`).

**Mass derivation:** cylindrical band: 2pi(hull_d/2 x hull_shell_rfrac) x hull_len_m x
hull_wall_m x rho.

**Spec:** 124.8 m x 32 m pressure shell, 0.44 m wall, 2700 kg/m3 -- ordinary
thick-laminate fabrication for 24 crew

**Buildability:** Thin-wall SiC pressure vessel, t = P*r/sigma. Aerospace-grade today;
only the crew count is exotic.

**Closest real hardware:** ISS pressure modules and submarine hulls -- routine
pressure-vessel work at this size.

**Operations:** draws none (passive) -- always.

**Active during:** all five phases -- passive, always.

**Mission ledger:** carried 4.433e+04 t at beta 0.5 -- no duty cycle, no relief.

**Failure mode:** a breach is a life-safety event, not a propulsion one

**Cascade:** breach -> pressure loss -> mission ends; nothing else matters after this.

**Thermal:** ~300 K shirt-sleeve inside -- the 96 MW hotel load still has to leave
through the radiators.

**Connects to:** hung off the ring by the pylons; houses decks, reactor, SMES, traps;
carries deflector forward and rectenna aft.

**Required by:** required by the decks, reactor, SMES, traps and cryo -- everything that
lives in flat spacetime.

**Verified by:** hoop-stress wall check (hull_wall = 0.22 x d/16); envelope check; mass
recompute.

**Governed by:** `hull_len_m`=124.76, `hull_d_m`=32, `hull_decks`=12, `hull_wall_m`=0.44, `hull_shell_rfrac`=0.88, `hull_density`=2,700, `deck_t_m`=1.4, `deck_inset_m`=1.2, `crew`=24, `crew_supplies_kg`=3,200, `len_margin_m`=20

**In the viewer:** labelled `CREW HULL (flat spacetime)` -- assembly step 1 of 17; slides 46 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 5. CREW DECKS -- 3.121e+04 t (2.9% of ship)   [TODAY]

**What it is:** the habitation volume inside the hull -- decks, equipment, and the 24
crew.

**Dimensions & placement:** ~32 x 32 m cross-section x 124.8 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** each deck is a 1.4 m thick slab across the 32 m hull diameter.

**Mounts at:** stacked inside the hull shell, inset 1.2 m from the pressure wall.

**Role:** bulkheads and floors inside the hull.

**Why it must exist:** the working volume -- where the 24 crew live and operate the
ship.

**Per unit:** 2601 t each x 12 deck.

**Material:** hull alloy at 2,700 kg/m^3 (`hull_density`).

**Mass derivation:** hull_decks disks: N x pi(hull_d/2 - deck_inset_m)^2 x deck_t_m x
rho.

**Spec:** 12 deck plates at 35% fill, same SiC laminate

**Buildability:** Bulkheads and floors. Nothing to invent.

**Closest real hardware:** ISS module fit-out -- routine.

**Operations:** draws none (passive) -- always.

**Active during:** all five phases -- the crew never stops living there.

**Mission ledger:** 9.00 yr of life support under the 96 MW hotel load.

**Failure mode:** none

**Cascade:** deck loss -> crew loss -> mission ends.

**Thermal:** ~300 K; internal air loops carry deck heat to the hull exchangers.

**Connects to:** inside the pressure hull, in flat spacetime.

**Required by:** required by the crew and the consumables -- the only parts that are the
mission's purpose.

**Verified by:** mass recompute; deck count check vs spec.

**In the viewer:** labelled `CREW HULL (flat spacetime)` -- assembly step 1 of 17; slides 46 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 6. FUSION REACTOR -- 2.496e+04 t (2.3% of ship)   [FAR]

**What it is:** a D-3He fusion plant -- the housekeeping generator; aneutronic-lean fuel
so it can sit inside the pressure hull.

**Dimensions & placement:** ~31 x 31 m cross-section x 6.4 m along the ship axis, at the
ring plane.

**Unit size:** a 6.36 m tube bent into a 21.24 m torus -- burn chamber, blanket and
divertor share that bore.

**Mounts at:** inside the hull, forward of the SMES -- buried where the shielding is
free.

**Role:** the housekeeping plant -- D-3He tokamak powering coils, cryo, control and
hotel load; it does not move the ship.

**Why it must exist:** everything else needs watts and at cruise there is no beam --
once the tap releases, this is the ship's entire power economy.

**Material:** reactor vessel at 5,200 kg/m^3 (`reactor_rho`).

**Stores / consumes:** consumes 25.21 kg/day of D-3He at full plant output -- the supply
chain this ship cannot carry.

**Mass derivation:** torus shell: 4pi^2 R r x reactor_wall_m x rho.

**Spec:** tokamak 21.2 m major x 6.4 m minor dia, 102.70 GWth -> 63.67 GWe at 62% direct
conversion; fuel ~6.49 kg 3He/day at cruise; hotel load 96 MW -- the fuel chain is the
blocker, not the torus

**Buildability:** D-3He demands a lunar/regolith helium-3 industry that does not exist,
and a plasma regime harder than D-T. The honest fallback: D-T at ITER class is NEAR, and
one metre of water shielding around this reactor costs only ~1333 t -- absorbable. The
aneutronic choice buys crew proximity, not feasibility.

**Closest real hardware:** SPARC/ITER-class tokamaks -- but D-3He plasma has never been
burned anywhere.

**Operations:** draws produces 63.67 GWe; burns 6.49 kg 3He/day; vents He-4 ash --
continuous, every phase.

**Active during:** all five phases -- hotel power never stops.

**Mission ledger:** produced 4.44e+18 J electric; burnt 2.033e+04 kg of D-3He across the
voyage.

**Failure mode:** trip -> hotel load falls on the SMES buffer; blackout is survivable
for hours, not days

**Cascade:** trip -> SMES bridges the hotel load for minutes -> blackout -> the cryo
floor warms -> quench cascade.

**Thermal:** the largest single heat source aboard -- every joule not converted to
electricity lands on the radiators.

**Connects to:** feeds the bus through the SMES buffer; burns the 3He supply; dumps
waste heat to the radiators.

**Required by:** required by every powered system -- coils via SMES, cryoplant, hotel
load.

**Verified by:** plant_electric_w and the 1.35x margin check in _scale_audit; mass
recompute.

**Governed by:** `reactor_major_d_m`=21.24, `reactor_minor_d_m`=6.36, `reactor_wall_m`=3.6, `reactor_rho`=5,200, `reactor_th_gw`=102.7, `reactor_direct_eff`=0.62

**In the viewer:** labelled `D-3He FUSION REACTOR` -- assembly step 2 of 17; slides 40 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 7. SMES BUFFER -- 1.192e+04 t (1.1% of ship)   [NEAR]

**What it is:** superconducting magnetic energy storage -- a lossless 'battery' holding
energy in a magnetic field for transients, not in chemicals.

**Dimensions & placement:** ~45 x 45 m cross-section x 43.0 m along the ship axis, aft,
station z=-7 m.

**Unit size:** a 4.4 m tube bent into a 40.36 m torus of conductor and coolant.

**Mounts at:** mounted on the spine at smes_z0_m =40.36 m.

**Role:** superconducting energy store bridging reactor trips and coil transients.

**Why it must exist:** the coils demand steady DC against transients; the buffer keeps a
sag from becoming a quench.

**Material:** SMES torus windings at 6,800 kg/m^3 (`smes_rho`).

**Stores / consumes:** stores 2.76 TJ of field energy (the smes_store_j check) -- the
ship's only large energy reservoir.

**Mass derivation:** torus shell: 4pi^2 R r x smes_wall_m x rho.

**Spec:** 2.76 TJ at 60 T in a 40.4 m major x 4.4 m minor toroid -- the field is ~1.5x
the best sustained magnet built today, so the rating sits at the NEAR edge

**Buildability:** Superconducting storage exists at small scale. A GJ-class toroid is
engineering, not research.

**Closest real hardware:** grid SMES units (MW-class, e.g. the D-SMES line) -- real
hardware at one-millionth the stored energy.

**Operations:** draws standby ~0; delivers 2.76 TJ on demand -- holds charge; discharges
on transients.

**Active during:** all phases, armed -- earns its keep in BOOST transients and BRAKE
regen.

**Mission ledger:** absorbed 9.48e+21 J of magsail regen on the brake leg -- its single
biggest deposit.

**Failure mode:** the bridge between reactor trip and restart -- without it a trip is a
blackout

**Cascade:** loss -> coil transients unsupplied -> quench risk on every ripple ->
eventual collapse.

**Thermal:** cryogenic, same 18 K class plant as the coils -- lossless storage only
exists cold.

**Connects to:** sits between reactor and coils -- absorbs transients so the field never
sags.

**Required by:** required by the coils (transient buffer) and the magsail (its regen
dumps here).

**Verified by:** smes_store_j = 2.76 TJ check; mass recompute.

**Governed by:** `smes_major_d_m`=40.36, `smes_minor_d_m`=4.4, `smes_wall_m`=1, `smes_rho`=6,800, `smes_b_t`=60, `smes_z0_m`=40.36

**In the viewer:** labelled `SMES FIELD BUFFER` -- assembly step 4 of 17; slides 64 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 8. ANTIMATTER TRAPS -- 1.213e+04 t (1.1% of ship)   [FAR]

**What it is:** Penning traps -- electromagnetic bottles confining positrons in vacuum,
burned only for peak fold transitions.

**Dimensions & placement:** ~10 x 9 m cross-section x 9.6 m along the ship axis, at the
ring plane.

**Unit size:** each trap is a 9.56 m spherical Penning bottle.

**Mounts at:** inside the hull beside the SMES -- deep in the flat interior, far from
the wall.

**Role:** Penning-cell antiproton reserves for high-intensity bursts (civilisation's
most dangerous carry-on item).

**Why it must exist:** the only source aboard for fold-transition peaks the reactor
cannot spike.

**Per unit:** 1516 t each x 8 trap.

**Material:** trap vessel at 4,400 kg/m^3 (`amtrap_rho`).

**Stores / consumes:** stores 5.248 kg of positrons per trap x 8 = 41.98 kg total ->
7.55 EJ, 1.80 gigatonnes TNT, if containment ever fails -- the most dangerous 42 kg in
the build.

**Mass derivation:** amtraps spherical shells: N x 4pi(d/2)^2 x amtrap_wall_m x rho.

**Spec:** 8 traps x 5.25 kg antiprotons (41.98 kg total, 7.55 EJ on tap) in 9.6 m
Penning cells -- at current production rates, longer than the age of the universe

**Buildability:** World production is nanograms per year. Traps this size need a
production industry nobody has priced, let alone built.

**Closest real hardware:** CERN's ALPHA/GBAR Penning traps -- they hold billions of
positrons; this asks for macroscopic mass.

**Operations:** draws confinement share of hotel load -- continuous containment,
forever.

**Active during:** all phases -- containment is forever, discharge is rare.

**Mission ledger:** discharged 0 kg over the voyage -- most of the 42 kg store came
home.

**Failure mode:** confinement loss -> annihilation: 7.55 EJ released against the
containment wall. This is the one line whose failure is catastrophic, not survivable

**Cascade:** containment loss -> 7.55 EJ against the wall -> the ship ends; the only
non-survivable failure aboard.

**Thermal:** cryogenic; confinement heat is small but it never stops -- forever is a
long duty cycle.

**Connects to:** discharge into the bus for peak fold transitions only -- never run
continuously.

**Required by:** required by peak fold transitions -- nothing else aboard can spike that
power.

**Verified by:** mass recompute; per-unit mass in the component table.

**Governed by:** `amtraps`=8, `amtrap_d_m`=9.56, `amtrap_wall_m`=1.2, `amtrap_rho`=4,400, `amtrap_kg`=5.248

**In the viewer:** labelled `ANTIMATTER PENNING TRAPS` -- assembly step 3 of 17; slides 56 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 9. CRYOPLANT -- 7357 t (0.7% of ship)   [TODAY]

**What it is:** refrigerator units holding the HTS coils at 18 K -- if they sag, the
coils quench and the field collapses.

**Dimensions & placement:** ~333 x 333 m cross-section x 20.2 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** each unit is a 11 m dia x 20.16 m cylinder of compressors, cold boxes and
dewars.

**Mounts at:** mounted at cryo_mount_rfrac =0.8 of the interior radius -- out on the
ring deck where the cold work is.

**Role:** 18 K refrigeration holding the coils and the antimatter traps below quench
temperature.

**Why it must exist:** REBCO quenches well above 18 K -- lose the cold and the coils
dump their field energy into the cryostat.

**Per unit:** 459.8 t each x 16 unit.

**Material:** cryo unit at 240 kg/m^3 (`cryo_rho`).

**Stores / consumes:** consumes 2492.8 MW of plant power continuously to hold the
cryogenic floor -- the second-largest load aboard.

**Mass derivation:** cryo_units cylinders: N x pi(d/2)^2 x cryo_len_m x rho.

**Spec:** 16 units, 11.0 m x 20.2 m each, holding coils and traps at 18 K; 2492.8 MW
draw against a radiative leak -- off-the-shelf physics

**Buildability:** 18 K refrigeration is demonstrated technology, resized for cold area,
not re-invented.

**Closest real hardware:** the ITER cryoplant (65 kW at 4.5 K, the largest ever built)
-- this needs more lift, colder.

**Operations:** draws 2492.8 MW -- continuous -- the coils and traps both ride on it.

**Active during:** all phases -- the cold floor never takes a phase off.

**Power share:** 5.3% of the 47.1 GW beta=0.99 cruise load.

**Mission ledger:** ran all 9.00 yr; its lifted heat is inside the 7.16e+18 J radiated.

**Failure mode:** warm-up -> quench cascade -> field collapse; hours of margin

**Cascade:** warm-up -> quench cascade -> field collapse -> falls out of warp; hours of
margin, not seconds.

**Thermal:** the heat pump -- lifts coil and trap heat up to radiator temperature; its
own rejection adds to the very load it serves.

**Connects to:** cools the field coils (and holds the traps cold); its waste heat goes
to the radiators like everything else.

**Required by:** required by the coils AND the traps -- two systems ride on it; it is a
single point of failure by design.

**Verified by:** mass recompute; envelope check (reach 147.1 m).

**Governed by:** `cryo_units`=16, `cryo_d_m`=11, `cryo_len_m`=20.16, `cryo_rho`=240, `cryo_mount_rfrac`=0.8

**In the viewer:** labelled `CRYOPLANT (16 units)` -- assembly step 5 of 17; slides 57 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 10. RADIATORS -- 7.75e+04 t (7.2% of ship)   [NEAR]

**What it is:** graphite panels radiating waste heat to space -- the ship's only way to
shed energy, and the binding size constraint on how hard the drive can run.

**Dimensions & placement:** ~202 x 202 m cross-section x 90.4 m along the ship axis,
aft, station z=-70 m (box spans the whole multi-unit arrangement).

**Unit size:** each panel is a 90.44 x 31.32 x 0.24 m graphite wing.

**Mounts at:** rooted at rad_z0_m =-24.36 m, inner radius rad_inner_r_m =69.56 m --
swept aft, clear of the bubble wall.

**Role:** the only path heat leaves the ship -- graphite panels rejecting coil/plant
waste as Stefan-Boltzmann radiation; the cruise speed's thermal ceiling.

**Why it must exist:** reactor and coils make heat the ship must shed and in vacuum the
only way out is radiated -- no panels, no continuous operation.

**Per unit:** 1292 t each x 60 panel.

**Material:** graphite radiator at 1,900 kg/m^3 (`rad_rho`).

**Mass derivation:** N panels x rad_len_m x rad_w_m x rad_t_m x rho.

**Spec:** 60 panels x 90.4 m x 31.3 m, both faces = 339910 m2 at 1550 K, epsilon 0.92,
graphite limit 1900 K -- refractory panels exist at bench scale, not at acres

**Buildability:** 1550 K graphite rejection is refractory-panel / droplet-radiator
territory: demonstrated below scale, never flown at this size.

**Closest real hardware:** ISS ammonia radiators -- graphite at peak temperature is
beyond anything flown.

**Operations:** draws none (passive radiation) -- continuous -- the only path heat
leaves the ship.

**Active during:** all phases -- heat leaves in DOCK too.

**Mission ledger:** rejected 7.16e+18 J of heat over the voyage -- every joule the ship
made or caught.

**Failure mode:** overtemp past 1900 K -> panel loss -> thermal runaway; the graphite
limit is the cruise's hard ceiling

**Cascade:** panel loss -> thermal ceiling drops -> every powered system derates ->
cruise speed falls.

**Thermal:** the terminus -- 1,550 K working panels against a 1,900 K limit; the only
door heat leaves by.

**Connects to:** the thermal sink for reactor, coils, cryo and hotel loads -- the only
way energy leaves the ship.

**Required by:** required by every powered part -- nothing continuous works without a
heat path.

**Verified by:** area = 339,910 m^2, T_eq at beta=0.99/2, and binding-part envelope
checks in _scale_audit.

**Governed by:** `radiators`=60, `rad_len_m`=90.44, `rad_w_m`=31.32, `rad_inner_r_m`=69.56, `rad_z0_m`=-24.36, `rad_temp_k`=1,550, `rad_limit_k`=1,900, `rad_emissivity`=0.92, `rad_t_m`=0.24, `rad_rho`=1,900

**In the viewer:** labelled `WASTE-HEAT RADIATORS (60)` -- assembly step 12 of 17; slides 96 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 11. PYLONS -- 1.409e+05 t (13.0% of ship)   [TODAY]

**What it is:** structural spars tying the crew hull into the ring -- they carry the
ring's loads into the hull.

**Dimensions & placement:** ~339 x 339 m cross-section x 4.8 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** each spar is a 154.08 m long box section, 5.88 x 4.8 m.

**Mounts at:** hull to ring -- they ARE the mounting path; 12 spars carry the ring's
load into the spine.

**Role:** structural spars tying hull, ring and radiators together.

**Why it must exist:** the only load path between hull and ring -- without them the ship
is two objects.

**Per unit:** 1.174e+04 t each x 12 spar.

**Material:** structural spar at 2,700 kg/m^3 (`pylon_rho`).

**Mass derivation:** N spars x pylon_len_m x pylon_w_m x pylon_t_m x rho.

**Spec:** 12 spars x 154.1 m, 5.88 m wide -- ordinary composite structure

**Buildability:** Structural spars. Nothing to invent.

**Closest real hardware:** ordinary aerospace spar -- fully buildable today.

**Operations:** draws none (passive) -- always.

**Active during:** all phases -- loaded hardest under BOOST.

**Mission ledger:** carried peak load under the 15 YJ boost -- 1.5e+25 J of kinetic
through 12 spars.

**Failure mode:** structural failure under load -- the ship does not spin apart slowly

**Cascade:** spar failure -> ring load path breaks -> structural event under boost.

**Thermal:** passive structure following ambient -- their job is force, not heat.

**Connects to:** the structural path hull <-> ring; they carry the ring's mass load into
the hull.

**Required by:** required by the ring and everything hung off it -- a pylon failure is a
structural failure.

**Verified by:** mass recompute; count check vs spec.

**Governed by:** `pylons`=12, `pylon_len_m`=154.08, `pylon_w_m`=5.88, `pylon_t_m`=4.8, `pylon_rho`=2,700

**In the viewer:** labelled `STRUCTURAL PYLONS (12)` -- assembly step 6 of 17; slides 54 m forward when exploded -- click it on the SHIP tab to isolate or explode it.

### 12. CASIMIR LATTICE -- 983.2 t (0.1% of ship)   [FAR]

**What it is:** cassettes of 10 nm-spaced plates exploiting the Casimir effect -- real,
measured negative energy, dozens of orders short of the bill.

**Dimensions & placement:** ~392 x 392 m cross-section x 1.1 m along the ship axis, at
the ring plane (box spans the whole multi-unit arrangement).

**Unit size:** each cassette is a 1.1 m square plate stack 3.68 m tall.

**Mounts at:** inside the ring wall itself -- the cassettes sit in the shell they feed.

**Role:** the only real negative-energy source aboard -- stacked vacuum plates; never
drawn on subluminally.

**Why it must exist:** the only negative energy that exists in hardware form -- the
honesty layer's answer to 'where is the exotic matter'.

**Per unit:** 10.24 t each x 96 cassette.

**Material:** plate stack at 2,300 kg/m^3 (`casimir_rho`).

**Stores / consumes:** stores -3.09 MJ of NEGATIVE energy in the vacuum gaps -- the only
'fuel' here that is geometry, not matter.

**Mass derivation:** cassettes x casimir_plate_m^2 x casimir_stack_m x rho.

**Spec:** 96 cassettes, 1.1 m plates, 10 nm gap at 60 nm pitch, 3.68 m stack --
5,887,999,968 plates total for -3.09 MJ of true negative energy; precision fabrication
at a count no lab has approached

**Buildability:** The Casimir force is measured, real physics. Stacking cassettes to
joule-class negative energy has never been demonstrated -- a scaling problem, not a fake
one.

**Closest real hardware:** Lamoreaux 1997 measured the Casimir force on a plate -- real
force, unbuilt at stack scale.

**Operations:** draws none (passive plates) -- continuous -- supplies -3.09 MJ of
negative energy.

**Active during:** all phases -- the plates hold their -3.09 MJ whether or not anyone
asks.

**Mission ledger:** held -3.09 MJ negative the whole way -- untouched, because nothing
needed it and nothing could use it.

**Failure mode:** none at cruise; it is never drawn on subluminally

**Cascade:** cassette loss -> nothing -- it feeds no system; the least consequential
failure aboard.

**Thermal:** passive vacuum plates at ambient -- the negative energy sits in the gaps,
not the material.

**Connects to:** embedded in the ring wall -- dormant negative-energy reserve, never
drawn on subluminally.

**Required by:** required by nothing in this build -- the exotic store is 41 orders
sub-critical; it feeds no system.

**Verified by:** density -4.334e4 J/m^3 and total -3.09 MJ checks; plate-count
derivation; mass recompute.

**Governed by:** `casimir_cassettes`=96, `casimir_plate_m`=1.1, `casimir_gap_nm`=10, `casimir_pitch_nm`=60, `casimir_stack_m`=3.68, `casimir_rho`=2,300

**In the viewer:** labelled `CASIMIR NEGATIVE-ENERGY LATTICE (96)` -- assembly step 9 of 17; slides 150 m forward when exploded -- click it on the SHIP tab to isolate or explode it.

### 13. DEFLECTOR -- 1061 t (0.1% of ship)   [TODAY]

**What it is:** the forward dust shield -- clears interstellar grains out of the path at
cruise.

**Dimensions & placement:** ~33 x 33 m cross-section x 9.7 m along the ship axis,
forward, station z=+65 m.

**Unit size:** one 33 m dia x 0.4 m disk facing forward.

**Mounts at:** the nose cap, 8.28 m deep at the bow.

**Role:** forward Whipple shield taking the ISM grit the bubble wall does not collect.

**Why it must exist:** at cruise beta each ISM grain carries megajoules -- the path must
be cleared or the hull takes relativistic sandblast.

**Material:** deflector plate at 3,100 kg/m^3 (`deflector_rho`).

**Stores / consumes:** consumes itself -- the sacrificial face erodes so the hull does
not.

**Mass derivation:** disk: pi(deflector_d/2)^2 x deflector_t_m x rho.

**Spec:** 33.0 m dia Whipple-style shield, 8.28 m deep

**Buildability:** Debris shield plate. Ordinary.

**Closest real hardware:** NIAC dust-shield and StarTram whipple studies -- studied,
never needed at this energy.

**Operations:** draws none (passive) -- always in the flight direction.

**Active during:** CRUISE and BRAKE -- where the ISM flux is.

**Mission ledger:** faced 4.04e+26 swept ISM particles released forward when the bubble
came down.

**Failure mode:** a puncture lets ISM grit reach the hull -- attrition, not a
single-event loss

**Cascade:** face erosion -> ISM grains start landing on the hull -> slow attrition, not
an event.

**Thermal:** dust strikes flash the face locally -- sacrificial by design, hot by
occupation.

**Connects to:** mounted forward on the hull axis; first thing the ISM meets at cruise.

**Required by:** required by hull integrity at cruise beta -- ISM grains at 0.85c are
megajoule events.

**Verified by:** envelope check (rim reach 72.6 m); mass recompute.

**Governed by:** `deflector_d_m`=33, `deflector_depth_m`=8.28, `deflector_t_m`=0.4, `deflector_rho`=3,100

**In the viewer:** labelled `NAVIGATION DEFLECTOR` -- assembly step 13 of 17; slides 96 m forward when exploded -- click it on the SHIP tab to isolate or explode it.

### 14. RCS PODS -- 4715 t (0.4% of ship)   [TODAY]

**What it is:** ion / VASIMR thruster pods -- attitude and trim at subwarp only.

**Dimensions & placement:** ~42 x 42 m cross-section x 113.7 m along the ship axis,
forward, station z=+21 m (box spans the whole multi-unit arrangement).

**Unit size:** each pod is a 4.76 m dia x 9.2 m cylinder of tank, cathode and grid.

**Mounts at:** around the hull's aft quarters -- moment arms for attitude authority.

**Role:** ion attitude thrusters for trim and docking; the only reaction propulsion
aboard.

**Why it must exist:** the bubble cannot steer or dock itself -- attitude authority has
to come from ordinary thrusters.

**Per unit:** 147.3 t each x 32 pod.

**Material:** thruster pod at 900 kg/m^3 (`rcs_rho`).

**Stores / consumes:** propellant-limited -- trim and docking authority only, never a
propulsion system.

**Mass derivation:** N pods x pi(rcs_d/2)^2 x rcs_len_m x rho.

**Spec:** 32 pods, 4.8 m x 9.2 m each -- ordinary propulsion plumbing

**Buildability:** Attitude thrusters. Ordinary.

**Closest real hardware:** flown ion drives (Dawn, DS1, VASIMR-class demos) -- the most
routine part on the ship.

**Operations:** draws propellant-limited bursts -- attitude trim and docking only.

**Active during:** DOCK and course trim only.

**Mission ledger:** no mission-energy footprint -- trim authority costs propellant, not
joules.

**Failure mode:** loss -> the ship tumbles; annoying, not fatal

**Cascade:** loss -> no attitude authority -> docking becomes impossible; flight itself
is unaffected.

**Thermal:** thruster waste heat is small and episodic.

**Connects to:** hull exterior, distributed fore and aft; subwarp attitude authority
only.

**Required by:** required by docking and attitude trim only -- the ship flies fine
without them until it needs to stop.

**Verified by:** mass recompute; count check vs spec.

**Governed by:** `rcs_pods`=32, `rcs_d_m`=4.76, `rcs_len_m`=9.2, `rcs_rho`=900

**In the viewer:** labelled `RCS / ION PODS (32)` -- assembly step 15 of 17; slides 66 m forward when exploded -- click it on the SHIP tab to isolate or explode it.

### 15. BOOST RECTENNA -- 17.59 t (0.0% of ship)   [NEAR]

**What it is:** the rectifying antenna -- converts the stellar tap's beam into DC for
the boost run.

**Dimensions & placement:** ~84 x 84 m cross-section x 27.8 m along the ship axis, aft,
station z=-76 m.

**Unit size:** a single 4 km film disk, 1 um thick -- the only part measured in km.

**Mounts at:** mounted aft at collector_z0_m =73.36 m; unfolds 4 km when the beam is on.

**Role:** the deployed 4 km film that catches the stellar tap during boost; stowed the
rest of the mission.

**Why it must exist:** the only intake for tap energy -- without it the ship has no way
to reach cruise speed at all.

**Material:** rectenna film at 1,400 kg/m^3 (`collector_film_rho`).

**Stores / consumes:** consumes nothing aboard -- it harvests the beam; capture inside
the Airy spot reaches 100%%.

**Mass derivation:** film disk: pi(deploy_km x 500)^2 x collector_film_um x rho -- a
deployed circular film, not a rigid dish.

**Spec:** deployed 4 km dia (stowed 84.4 m), film 1 um at 1400 kg/m3 -- ~17.6 t of
deployed film; power beaming proven at a kilometre scale

**Buildability:** Rectennas are proven. A kilometres-wide deployable film has never been
flown -- engineering, not physics.

**Closest real hardware:** kW-class microwave-power-transfer rectennas (MPT experiments)
-- GW capture at this aperture is scale work, not new physics.

**Operations:** draws captures up to 100% of the tap while deployed -- deployed during
boost only; stowed at cruise.

**Active during:** BOOST and the photon-brake leg -- stowed in between.

**Mission ledger:** harvested 1.51e+25 J on boost and dissipated 1.42e+25 J of
photon-brake work on arrival.

**Failure mode:** failure to stow -> a 4 km sail in the ISM flux; failure to deploy ->
no boost, mission scrubs

**Cascade:** loss -> no boost, no brake -- the ship becomes a one-way unpowered
ballistic.

**Thermal:** under the beam it carries intercepted flux; conversion loss warms the film
-- one reason it stows at cruise.

**Connects to:** deploys aft during BOOST; feeds the SMES bus with beam energy until
beam range runs out.

**Required by:** required by the boost phase and the photon brake -- no receiver, no
ride.

**Verified by:** capture <= 1 and film-mass recompute checks.

**Governed by:** `collector_d_m`=84.4, `collector_depth_m`=16.52, `collector_deploy_km`=4, `collector_film_um`=1, `collector_film_rho`=1,400, `collector_z0_m`=73.36

**In the viewer:** labelled `BOOST RECTENNA` -- assembly step 14 of 17; slides 94 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 16. MAGSAIL LOOP -- 1.28e+04 t (1.2% of ship)   [FAR]

**What it is:** a plasma-coupled superconducting loop hundreds of km across that drags
on the interstellar medium -- the only credible way to STOP.

**Dimensions & placement:** ~1400 x 1400 m cross-section x 4.2 m along the ship axis,
aft, station z=-109 m (box spans the whole multi-unit arrangement).

Note: drawn at 1:4000 so it fits on screen -- the real loop is 5600 km across.

**Unit size:** a single 2,800 km radius loop of superconductor -- the largest object in
the build.

**Mounts at:** mounted aft; deploys to a 2,800 km radius loop -- the mount is the only
small part of it.

**Role:** the brake that always works -- a superconducting loop dragging on the
interstellar medium, too slow to stop the ship in useful time.

**Why it must exist:** nothing else aboard can throw momentum away -- without it (and
the destination array) every arrival is a flyby.

**Stores / consumes:** regenerates %.0f%% of drag energy back to the SMES buffer
(magsail_regen_eff) -- a brake that pays for itself.

**Mass derivation:** declared, not derived -- magsail_mass_kg is a direct spec (the loop
is HTS wire, mass set by conductor and sheath).

**Spec:** 17593 km of superconductor at 4.4 MA, 12800 t loop (728 g/m), drag coef 0.85,
62% regen recovery -- the conductor budget is thinner than the current demands, which is
what keeps this FAR

**Buildability:** The plasma interaction is modelled (Zubrin 1991, Freeland 2015). A
2800 km superconducting loop has never been deployed, stabilised or repaired -- and
those verbs are the whole problem.

**Closest real hardware:** Zubrin & Andrews 1991 concept; the mini-magnetosphere (M2P2)
cousin was wind-tunnel tested, never flown.

**Operations:** draws drag power -> 62% recovered to the SMES -- deployed during braking
only.

**Active during:** BRAKE only -- stowed the whole way out.

**Mission ledger:** regenerated 9.48e+21 J to the SMES buffer -- then the photon brake
finished what drag could not.

**Failure mode:** current quench mid-brake -> the sail goes slack and braking stops; the
flyby continues ballistically

**Cascade:** deployment failure -> cannot stop unaided -> flyby unless the destination
array exists.

**Thermal:** drag energy mostly recovers; the rest warms the plasma sheath around the
loop.

**Connects to:** deploys aft for BRAKE (the bubble must drop -- the sail needs the ISM);
regenerates drag energy to the SMES.

**Required by:** required by arrival itself -- the only credible way to stop without a
pre-built destination array.

**Verified by:** full-stop ~32,600 yr and halving-time checks.

**Governed by:** `magsail_r_km`=2,800, `magsail_current_a`=4,400,000, `magsail_mass_kg`=1.28e+07, `magsail_cd`=0.85, `magsail_regen_eff`=0.62, `magsail_view_scale`=0.00025

**In the viewer:** labelled `MAGNETIC SAIL (drawn 1:4000)` -- assembly step 16 of 17; slides 150 m aft when exploded -- click it on the SHIP tab to isolate or explode it.

### 17. CONSUMABLES + CREW -- 76.8 t (0.0% of ship)   [NEAR]

**What it is:** the 24 crew and their food, water and spares.

**Unit size:** 3,200 kg of food, water and spares per head x 24 crew.

**Mounts at:** inside the hull, on the decks -- cargo has no mount.

**Role:** closed-loop life support: oxygen, water, food and spares for the whole
crossing.

**Why it must exist:** the mission's reason to exist.

**Per unit:** 3200 kg each x 24 crew member.

**Stores / consumes:** stores 3,200 kg of food, water and spares per head x 24 crew =
76.8 t of carried mass.

**Mass derivation:** crew x crew_supplies_kg per head.

**Spec:** 24 crew x 3200 kg of consumables, hotel load 96 MW, a closed loop for the full
crossing -- longer than any loop run to date, by a factor of years

**Buildability:** Closed-loop life support for a 5.0 year crossing exceeds ISS practice.
Scaling, not physics.

**Closest real hardware:** ISS closed-loop life support -- the most proven system
aboard.

**Operations:** draws 96 MW hotel load -- continuous.

**Active during:** all phases -- consumed at ~hotel rate for the whole 9 yr.

**Power share:** 0.2% of the 47.1 GW beta=0.99 cruise load.

**Mission ledger:** the crew aged +2.516 s against Earth -- gravitational drift only;
that IS the whole time story.

**Failure mode:** ECLSS margin: days of buffer, not weeks -- the crossing is 5.0 years
of uninterrupted loop

**Cascade:** depletion -> mission deadline, not an event -- the slowest failure mode
aboard.

**Thermal:** ambient stores; the crew's metabolic and hotel heat is part of the 96 MW
that must radiate.

**Connects to:** carried on the crew decks.

**Required by:** required by the mission's purpose -- every other part exists to keep
these 24 people alive.

**Verified by:** crew count check; supplies-per-head spec.

**In the viewer:** no mesh -- carried mass, drawn as nothing (the mass is real, the pixels are not).

## External infrastructure

What the mission needs that the ship does not carry. The ship can fly without the destination array -- it can only fly PAST without it.

### 1. STELLAR TAP (6.4E+18 W, 1000 KM ARRAY)   [FAR]

**What it is:** a 1,000 km solar-collector array near Sol beaming 6.4 EW of collimated
light at the ship -- the propellant you do not carry; the mass stays home.

Lawful physics -- a laser is a laser. The bill is civilisational: a transmitter the size
of a country and the power to feed it. No engineering shortcut moves it under 30 years.

**Needs:** 6e+18 W delivered across 0.6 ly -- a national-grid-scale transmitter,
permanently funded

**Physics source:** Forward 1961 laser-sail lineage; the beam physics is Airy
diffraction, checked live against beam_power_w.

### 2. DESTINATION PHOTON BRAKE   [FAR]

**What it is:** a second tap, pre-built at the destination, firing photons at the
arriving ship's rectenna -- the difference between a rendezvous and a flyby.

A second tap, pre-built at Proxima, or the ship remains a flyby.

**Needs:** the same transmitter, already standing at the far end before launch

**Physics source:** the same tap physics aimed at the bow -- verified by the capture <=
1 and brake-work honesty checks.

### 3. HELIUM-3 SUPPLY CHAIN   [FAR]

**What it is:** the mining/separation economy that feeds the fusion plant -- the fuel
side nobody budgets for.

Lunar regolith extraction at tonne scale -- an industry, not a prototype.

**Needs:** tonnes of 3He per decade -- lunar mining, refining and lift capacity combined

**Physics source:** lunar-regolith / gas-giant scoop literature; isotope separation
exists at gram scale, not tonne scale.

### 4. ISM SCOOP REFUELLING   [FAR]

**What it is:** skimming interstellar gas through the magsail aperture and sorting the
isotopes -- real, but isotope-lean; loses to burn at every cruise speed in the model.

Shares the magsail's unproven physics, plus isotope separation underway.

**Needs:** 6.18e-01 kg/s of gas scooped at cruise -- the loop again, plus a refinery
that runs while it brakes

**Physics source:** Bussard 1960 ramjet lineage -- the model prices it and the scoop
loses to burn at every cruise beta.

### 5. THE WARP SHELL AS A DRIVE   [OPEN]

**What it is:** the bubble itself -- a stationary spacetime solution that transports the
flat region, not a propulsion system that pushes mass.

Subluminal positive-energy shells exist on paper (Bobrick & Martire 2021); the material
to build one does not. Superluminal is not a schedule problem -- it is NEC violation,
barred by theorem.

**Needs:** a material with anisotropic stress near the sound-speed limit -- unnamed,
unmeasured, unpriced

**Physics source:** Alcubierre 1994, Van Den Broeck 1999, Krasnikov 1998 -- metric
engineering, not propulsion.

### 6. WORMHOLE GATES AND TIME MACHINES   [IMPOSSIBLE]

**What it is:** Morris-Thorne throats and their CTC descendants -- every construction
priced in the portal section, most barred by quantum inequalities.

Every construction in the model prices its exotic energy honestly and every one comes
back decades of orders short. Not a procurement question.

**Needs:** 2.421e+44 J of negative energy for the smallest gate -- nothing to buy it
with

**Physics source:** Morris-Thorne 1988 traversability + the Ford-Roman
quantum-inequality literature that bars most of it.

### + THE WARP BUBBLE -- the part that carries no mass

**What it is:** the drive itself -- a stationary spacetime solution, not hardware. A
366.9 m sphere of curved metric with a 0.2 m transition wall and a 182.2 m flat interior
(f=1) where the hull lives. It has no mass line because it has no mass: the shell and
coils above are the stress-energy that WRITES it into the metric.

**Geometry:** bubble_r_m 183.44 m (f=0.5 at the wall), wall delta 0.20 m, interior
cutoff R-6delta (f=0.9997). Drawn as a translucent 14-facet shell in the viewer.

**Held up by:** the 96 field coils + shell sectors keeping the shape -- servo error
drains `integrity` (SHELL_STRESS_TAU); at 0.35 it collapses and the ship falls out of
warp. Superluminal shape demands the exotic bill is booked as debt, never paid -- 41.3
orders short against the Casimir store.

**Verified by:** f(R)=0.5 at five wall decades, theta antisymmetry, the wall integral
over 33 decades, 'ring straddles the wall', subluminal NEC pass / superluminal NEC fail
-- the whole first page of the selftest.

## The portal gate, part by part

The 12 m Morris-Thorne gate installation rendered on the PORTAL tab -- five parts with live geometry, same conventions as the ship list.

### GATE A  (mouth, Sol side)

**What it is:** the near mouth's frame -- the coil ring and support hardware that holds
the Sol-side mouth open.

**Dimensions:** ~35.7 x 35.7 x 3.0 m bounding box, 504 facets rendered.

- 24 m aperture -- b0 = 12.0 m throat radius.
- The ring is the only part of a portal you could actually build. It
-   holds the field geometry; it does NOT make the throat. Making the
-   throat is the other -2.421e+44 J on this list.
- Traversal at walking pace: 4.8 s.
- TIDAL SHEAR AT THIS THROAT: 1.27e+14 g across a 2 m body.
-   Nothing made of atoms crosses that. See GATE B for the throat you
-   would actually survive.

### THROAT FIELD COILS (16)

**What it is:** the field coils threading the throat -- same REBCO trick as the drive
coils, holding the throat's stress-energy shape.

**Dimensions:** ~31.1 x 31.1 x 4.0 m bounding box, 576 facets rendered.

- They shape the aperture field. They cannot violate the null energy
-   condition, because no arrangement of ordinary current can.
- Every traversable-wormhole solution needs NEC violation AT the throat
-   (Morris & Thorne 1988) -- the same wall the superluminal warp mode
-   hits, reached from a completely different direction.

### THROAT CASIMIR CASSETTES (8)

**What it is:** the exotic plates at the throat -- the negative-energy insert that keeps
the throat from pinching off.

**Dimensions:** ~23.7 x 23.7 x 2.2 m bounding box, 240 facets rendered.

- Real negative energy, in the only place it is ever found.
- Required at this throat: -2.421e+44 J.
- Supplied by the whole ship's lattice: -3.09 MJ.
- SHORT BY 38 ORDERS OF MAGNITUDE -- and by 45 orders for a throat
-   wide enough to survive crossing.
- The closest thing to a real construction is Maldacena, Milekhin &
-   Popov (2020): Casimir energy of massless fermions threading a pair
-   of magnetically charged black holes. It works on paper. It needs
-   objects nobody has ever observed, and traversal takes years.

### THE THROAT  (embedding diagram)

**What it is:** the Morris-Thorne embedding funnel itself -- the shape of the shortcut,
drawn so you can see the flare-out condition.

**Dimensions:** ~96.0 x 96.0 x 83.1 m bounding box, 47 facets rendered.

- ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2   (Morris-Thorne 1988)
- Drawn from z = 2 b0 sqrt(rho/b0 - 1) -- the real embedding, not a
-   decorative funnel. No horizon, no singularity: genuinely two-way.
- Energy density demanded at the throat: -3.344e+40 J per cubic metre.
- The FLARE-OUT condition is what costs: for the throat to open out on
-   both sides instead of pinching shut, the stress-energy there must
-   violate the null energy condition. That is the entire problem, and
-   it is structural -- not an artefact of this particular solution.

### GATE B  (mouth, far side)

**What it is:** the far mouth's frame -- the exit hardware wherever the other end was
towed.

**Dimensions:** ~29.9 x 30.0 x 3.0 m bounding box, 279 facets rendered.

- Wherever you put it -- 4.2465 ly away, in this configuration.
- SURVIVABLE THROAT: tidal shear goes as c^2 L / b0^2, so a person
-   crossing at 1 g of stress needs b0 >= 1.35e+08 m -- about 11 Earth
-   diameters. Morris & Thorne reached the same conclusion in 1988.
- That throat's exotic bill: -2.730e+51 J (-1.53e+04 Msun).
- AND THEN IT IS A TIME MACHINE. Two mouths at different clock rates
-   desynchronise; when the offset exceeds the light-travel time
-   between them, closed timelike curves exist (Morris, Thorne &
-   Yurtsever 1988). Park one mouth by a neutron star and this pair
-   becomes one in 18.84 yr.

## How it flies

| Phase | What happens | Where the energy comes from |
|-------|--------------|-----------------------------|
| DOCK | Ship at rest at the tap; shell down | reactor housekeeping |
| BOOST | Rectenna deploys; beam energy integrates into (gamma-1)Mc^2 until capture falls below useful | the stellar tap, via diffraction-limited capture |
| CRUISE | Stationary spacetime solution -- no energy goes into speed; only coils/cryo/control run | reactor (63.7 GW el) |
| BRAKE | Magsail alone: ~3.26e+04 yr full stop (honest -- flyby without infrastructure). Destination array: photon brake ~50.7 d at beta=0.5 | ISM drag (+62% regen to SMES) / destination photons |
| ARRIVED | Ship clock = Earth clock; ISM wall load discharged forward | -- |

**TEST mode (FLIGHT tab, T key or TEST chip):** auto-plays a mission with whatever settings are dialled in -- commanded beta (, .), wall thickness ([ ]), destination array (J), time warp (- +). It resets the voyage, presses the same begin_boost/begin_brake commands the manual chips press, holds each phase so it is visible, and ends honestly: ARRIVED if the settings can stop the ship, flyby if they cannot, 'still braking' if the magsail alone is left to do it.

## Complete dimensional specification (every DIMS key)

All 100 keys of `DIMS`, grouped as in the source. Changing any of these moves the ship, the mass budget, the radiator sizing and the voyage at once.

#### Warp bubble geometry (the spacetime, not the hardware)

| Key | Value | What it is |
|-----|-------|------------|
| `bubble_r_m` | 183.44 | r_s where the shape function falls to 1/2 -- x2 again (1.83x the original WD-1) |
| `wall_thick_m` | 0.2 | wall thickness delta; sigma = 1/delta -- a SPACETIME parameter, not structure: it does not scale with the hull |
| `interior_margin` | 6 | flat interior ends this many delta inside R (f > 0.9997 there) -- see flat_interior_r() |

#### Main warp ring (the shift-vector shell -- the actual "drive")

> The centreline sits AT the bubble radius on purpose: the shell does not
> project the wall from a distance, the shell IS the wall's source term, so
> its stress-energy has to be where the curvature is.

| Key | Value | What it is |
|-----|-------|------------|
| `ring_major_d_m` | 366.88 | ring centreline diameter = 2 x bubble_r_m |
| `ring_minor_d_m` | 27.52 | tube diameter of the toroidal shell |
| `ring_wall_m` | 1.08 | shell wall thickness (a shell, not solid) -- x2: shell stress scales with span |
| `ring_sectors` | 96 | x2: doubled circumference, same sector arc |
| `ring_density` | 4,100 | conditioned SiC/W metamaterial  [kg/m^3] |

#### Superconducting field coils (96, one per ring sector)

| Key | Value | What it is |
|-----|-------|------------|
| `coils` | 96 | x2: one per doubled ring sector |
| `coil_bore_m` | 27.92 | clear bore of a coil wrapped around the ring tube: tube dia + 2 x standoff = 27.52 + 0.40 (derived, not free -- a smaller bore cannot thread the tube it energises) |
| `coil_len_m` | 17.24 | axial length along the ring tube -- x2 |
| `coil_turns` | 48,000 | REBCO tape turns per coil (same tech) |
| `coil_current_a` | 38,000 | operating current                [A] |
| `coil_temp_k` | 18 | HTS operating temperature        [K] |
| `coil_build_m` | 0.3 | radial winding-pack build [m]. Set by engineering J_e of the REBCO tape: build ~ N*I / (J_e * circumference). The bore doubled this pass so the same turns x current COULD fit a ~0.15 m pack; 0.30 m is kept as a conservative quench-stabilizer margin on the larger machine rather than claimed as savings |
| `coil_standoff_m` | 0.2 | gap between ring-tube surface and the winding pack inner radius [m] -- x2 |
| `coil_density` | 5,600 | winding-pack average density [kg/m^3] |

#### Fore / aft shaping rings (set the front-back asymmetry)

| Key | Value | What it is |
|-----|-------|------------|
| `capring_d_m` | 176.08 | -- |
| `capring_minor_d_m` | 12.84 | -- |
| `cap_offset_m` | 69.72 | +/- z offset from the ring plane |
| `capring_wall_frac` | 0.3 | solid fraction of the shaping-ring torus |

#### Crew hull (flat spacetime inside -- ordinary ship engineering)

| Key | Value | What it is |
|-----|-------|------------|
| `hull_len_m` | 124.76 | -- |
| `hull_d_m` | 32 | x2 -- twice WD-1's cabin diameter |
| `hull_decks` | 12 | x2: doubled hull length |
| `hull_wall_m` | 0.44 | hoop-stress scaling t = P*r/sigma is LINEAR in hull radius: 32.0 m returns exactly 2x WD-1's 0.22 m wall |
| `hull_shell_rfrac` | 0.88 | mean shell radius as a fraction of hull radius (the nose/aft taper) -- dimensionless shape factor, unchanged |
| `hull_density` | 2,700 | Al-Li / composite pressure hull  [kg/m^3] |
| `deck_t_m` | 1.4 | deck plate thickness -- x2: plate bending stress ~ p L^2 / t^2, doubled span needs doubled thickness for the same margin |
| `deck_inset_m` | 1.2 | deck plate inset from the hull wall [m] -- x2 with the hull radius |
| `crew` | 24 | x2 with the doubled cabin volume |
| `crew_supplies_kg` | 3,200 | consumables + outfitting per crew  [kg] |
| `len_margin_m` | 20 | end-fittings / docking margin in the overall-length figure [m] -- x2 |

#### Structural pylons hull -> ring

| Key | Value | What it is |
|-----|-------|------------|
| `pylons` | 12 | x2: an 8x-heavier hull on a doubled span |
| `pylon_len_m` | 154.08 | -- |
| `pylon_w_m` | 5.88 | -- |
| `pylon_t_m` | 4.8 | section thickness -- x2: an 8x load on a 2x span needs ~2x thickness to hold the same bending/buckling margin |
| `pylon_rho` | 2,700 | same Al-Li/composite as the hull  [kg/m^3] |

#### D-3He fusion reactor (the housekeeping plant)

| Key | Value | What it is |
|-----|-------|------------|
| `reactor_major_d_m` | 21.24 | x2: torus volume x8 |
| `reactor_minor_d_m` | 6.36 | -- |
| `reactor_wall_m` | 3.6 | vessel wall -- x2: pressure-vessel wall t = P*r/sigma is linear in radius |
| `reactor_rho` | 5,200 | vessel average density          [kg/m^3] |
| `reactor_th_gw` | 102.7 | thermal output [GW] -- derived, not typed: beta=0.99 cruise electrical load is ~47.1 GW (coil_ac x8 + cryo/control x4 + hotel x2 vs pass 6); /0.62 gives 76.0 GW thermal, x the SAME 1.35 design margin = 102.7 GW. Torus volume grew x8, so specific power density is the same as pass 6 |
| `reactor_direct_eff` | 0.62 | direct energy conversion (aneutronic) |

#### Antimatter store (peak fold transitions only)

| Key | Value | What it is |
|-----|-------|------------|
| `amtraps` | 8 | x2 bays on the doubled spine |
| `amtrap_d_m` | 9.56 | -- |
| `amtrap_wall_m` | 1.2 | containment shell -- x2 with the sphere |
| `amtrap_rho` | 4,400 | trap shell density              [kg/m^3] |
| `amtrap_kg` | 5.248 | antihydrogen per trap [kg] -- scales S^3 with the kinetic-energy bill it buffers |

#### SMES field-transient buffer (superconducting magnetic store)

> NOT a "warp battery". Its capacity is COMPUTED from B^2/2mu0 times the
> torus volume (see smes_store_j()) and comes out proportionally smaller.
> It buffers coil transients; it does not move the ship. Nothing here
> pretends otherwise.

| Key | Value | What it is |
|-----|-------|------------|
| `smes_major_d_m` | 40.36 | -- |
| `smes_minor_d_m` | 4.4 | -- |
| `smes_wall_m` | 1 | torus shell -- x2 with the structure |
| `smes_rho` | 6,800 | winding/structure average       [kg/m^3] |
| `smes_b_t` | 60 | bore field [T] -- same HTS technology |
| `smes_z0_m` | 40.36 | mount offset along the spine [m] -- x2 |

#### Casimir negative-energy lattice (96 cassettes in the ring wall)

| Key | Value | What it is |
|-----|-------|------------|
| `casimir_cassettes` | 96 | x2: the ring wall circumference doubled |
| `casimir_plate_m` | 1.1 | square plate edge (module, unchanged) |
| `casimir_gap_nm` | 10 | vacuum gap between plates (nanoscale, |
| `casimir_pitch_nm` | 60 | gap + plate thickness -- unaffected by the ship's macroscopic scale) |
| `casimir_stack_m` | 3.68 | stack height per cassette -- x2 |
| `casimir_rho` | 2,300 | plate stack average density     [kg/m^3] |

#### Waste-heat radiators (sized against the REAL waste heat)

> Area scales by the WASTE-HEAT ratio (~x6.6), not the hull's x2:
> 60 panels x 90.44 m x 31.32 m gives x8 the pass-6 area -- slightly
> more than waste heat grew, so the beta=0.99 equilibrium sits a
> little cooler than pass 6's ~1.5e3 K. The 1900 K graphite limit is
> the material bound and does not move. check_envelope() still asserts
> the tips stay inside the flat interior (the bubble doubled with it).

| Key | Value | What it is |
|-----|-------|------------|
| `radiators` | 60 | -- |
| `rad_len_m` | 90.44 | -- |
| `rad_w_m` | 31.32 | -- |
| `rad_inner_r_m` | 69.56 | panel root radius -- x2 |
| `rad_z0_m` | -24.36 | panel leading edge -- x2 |
| `rad_temp_k` | 1,550 | design-point panel temperature    [K] |
| `rad_limit_k` | 1,900 | graphite sublimation limit        [K] |
| `rad_emissivity` | 0.92 | -- |
| `rad_t_m` | 0.24 | panel sandwich depth -- x2: a 2x span panel needs ~2x depth for the same bending stiffness (I ~ t^3 term) |
| `rad_rho` | 1,900 | graphite panel density            [kg/m^3] |

#### Cryoplant (holds the HTS coils at 18 K)

| Key | Value | What it is |
|-----|-------|------------|
| `cryo_units` | 16 | x2 units, each x2 in size (volume x8) |
| `cryo_d_m` | 11 | -- |
| `cryo_len_m` | 20.16 | -- |
| `cryo_rho` | 240 | insulation/plumbing average     [kg/m^3] |
| `cryo_mount_rfrac` | 0.8 | mounting radius as a fraction of the ring major radius (envelope check only) |

#### Navigation deflector (subwarp dust shield)

| Key | Value | What it is |
|-----|-------|------------|
| `deflector_d_m` | 33 | -- |
| `deflector_depth_m` | 8.28 | -- |
| `deflector_t_m` | 0.4 | dish skin -- x2 with the dish |
| `deflector_rho` | 3,100 | whipple/composite density       [kg/m^3] |

#### Reaction control (subwarp only -- ion / VASIMR pods)

| Key | Value | What it is |
|-----|-------|------------|
| `rcs_pods` | 32 | x2: more authority for an 8x hull |
| `rcs_d_m` | 4.76 | -- |
| `rcs_len_m` | 9.2 | -- |
| `rcs_rho` | 900 | propellant+tank average         [kg/m^3] |

#### Boost receiver (the stellar-tap rectenna)

> Stowed it is a bigger dish; under boost it still unfurls to the same
> 4 km film rectenna, because the diffraction spot of the (unchanged,
> external) 1000 km transmitter is kilometres wide at interstellar
> range regardless of ship size (see beam_spot_m()).

| Key | Value | What it is |
|-----|-------|------------|
| `collector_d_m` | 84.4 | stowed dish diameter -- x2 |
| `collector_depth_m` | 16.52 | -- |
| `collector_deploy_km` | 4 | deployed film rectenna diameter    [km] unchanged: set by beam diffraction at the (unchanged, external) transmitter, not by ship size |
| `collector_film_um` | 1 | rectenna film thickness            [um] |
| `collector_film_rho` | 1,400 | film density                       [kg/m^3] |
| `collector_z0_m` | 73.36 | stowed mount offset along the spine [m] |

#### Wormhole portal gate (Morris-Thorne throat)

> The gate is the buildable-LOOKING part: a ring you could walk through.
> portal_summary() then prices the throat it would have to hold open, and
> mt_min_throat_m() reports the one you would actually survive crossing.
> Left at full scale: it is a separate ground/orbital installation, not
> part of the ship being resized here.

| Key | Value | What it is |
|-----|-------|------------|
| `portal_gate_d_m` | 24 | engineered aperture (throat 2 b0) |
| `portal_ring_minor_d_m` | 3 | -- |
| `portal_coils` | 16 | field coils around the rim |
| `portal_casimir_rings` | 8 | negative-energy cassettes at the throat |
| `portal_frame_d_m` | 34 | structural frame outside the aperture |

#### Magnetic sail (the only credible way to STOP)

> Zubrin and Andrews (1991): a superconducting loop deflects interstellar
> protons and drags against the ISM. The x8-heavier hull needs the drag
> back: loop radius doubles to 2800 km (drag ~ Cd rho A) and the cable
> mass scales x8 -- braking time is mass / (Cd rho A), so a x8 ship on
> a x4 area still brakes SLOWER; that is the honest cost of upscaling,
> printed, not hidden.

| Key | Value | What it is |
|-----|-------|------------|
| `magsail_r_km` | 2,800 | deployed loop radius               [km] |
| `magsail_current_a` | 4,400,000 | persistent loop current [A] -- x2 keeps the same loop-centre field (B ~ I/r) |
| `magsail_mass_kg` | 1.28e+07 | HTS cable + deployment mass  [kg] x8 |
| `magsail_cd` | 0.85 | effective ISM drag coefficient |
| `magsail_regen_eff` | 0.62 | braking energy recovered to the bus |
| `magsail_view_scale` | 0.00025 | 1:4000 -- printed on screen, always |

## Complete plant & drive configuration

#### PLANT -- loads, conversion and the boost beam

| Key | Value | What it is |
|-----|-------|------------|
| `hotel_mw` | 96 | life support, computation, sensors  [MW] -- x2 with the doubled crew |
| `coil_ac_mw` | 38252.8 | AC ripple + field-shaping losses in the 96 HTS coils at cruise [MW] -- ~S^3 |
| `cryo_mw` | 2492.8 | cryoplant electrical draw  [MW] -- ~S^2 |
| `control_mw` | 7,064 | metric servo: 10 kHz shell-shape control [MW] -- ~S^2 over the ring surface |
| `conversion_eff` | 0.62 | direct conversion, aneutronic D-3He |
| `recovery_eff` | 0.92 | fold charge recovered on deceleration |
| `am_energy_j_kg` | 1.7975e+17 | 2*m*c^2 per kg antimatter (matter+anti) |
| `d3he_j_kg` | 3.52e+14 | D + 3He -> 4He + p + 18.35 MeV, per kg mix |
| `tap_w` | 6.4e+18 | stellar-tap boost beam [W] -- x8 again: mission infrastructure sized to the ship; an ~8x mass needs ~8x delivered power to hold the same cruise speed. ~17 ppm of L_sun (6.4e18 / 3.828e26). |
| `beam_aperture_km` | 1,000 | transmitter phased-array aperture    [km] |
| `beam_lambda_um` | 1 | transmitter wavelength               [um] |
| `beam_range_ly` | 0.62 | usable boost range from the array    [ly] |

#### DRIVE -- operating envelope

| Key | Value | What it is |
|-----|-------|------------|
| `beta_sub_max` | 0.99 | physical (positive-energy) drive ceiling |
| `beta_ftl_max` | 10 | Alcubierre mode ceiling (flagged, exotic) |
| `spinup_s` | 42 | ship-seconds per unit beta |
| `bubble_form_s` | 18 | shell shape convergence time |
| `integrity_min` | 0.35 | below this the bubble collapses |
| `wall_min_m` | 1e-15 | thinnest wall the shape servo can hold |
| `wall_max_m` | 12 | -- |
| `arrival_beta` | 0.001 | under 0.001 c counts as station-keeping |

| `SHELL_STRESS_TAU` | 2000 s | seconds to lose full integrity at unit shell stress |

## Derived engineering quantities

Not in DIMS -- computed from it. Every row re-derives from the same functions the model uses.

| Quantity | Value |
|----------|-------|
| flat interior radius | 182.24 m (R - 6 x wall) |
| ring sector arc | 12.01 m (96 sectors) |
| REBCO tape, all coils | 408,526 km (4,255 km per coil at pack mean dia 28.22 m) |
| Casimir plate gaps | 61,333,333 per cassette x 96 = 5,887,999,968 total |
| onboard negative energy | -3.09 MJ (Casimir) vs 5.656e+47 J demanded -- 41.3 orders short |
| SMES stored energy | 2.76 TJ |
| antimatter store | 41.984 kg in 8 traps = 7.55 EJ |
| rectenna film | 4 km deployed, 17.6 t of 1 um film |
| magsail loop | 17,593 km of cable, 12,800 t, 0.7 g/m |
| radiator area | 339,909 m^2 = 60 panels x 90.44 x 31.32 m x 2 faces |
| cruise electric load | 36.77 GW at beta=0.855 (coil 38.3 + cryo 2.5 + control 7.1 + hotel 0.1 MW at beta=1, scaling beta^2) |
| fusion fuel at cruise | 14.558 kg D-3He/day |
| waste heat | 75.95 GW at beta=0.99 -> 1439 K ; 262.36 GW at beta=2 -> 1961 K (limit 1900 K) |
| kinetic energy | 90 YJ at beta=0.855 (gamma 1.9261); 15 YJ at 0.5c; diverges at beta=1 |
| boost duration | ~303 days to the emergent beta under the tap |
| beam spot | 2.31 km at 0.1 ly, 11.54 km at 0.5 ly, 14.31 km at 0.62 ly (capture 100%, 12%, 7.8%) |
| photon brake | 4.27e+10 N at 0.02 ly -> 50.7 d to stop from beta=0.5 |
| magsail | 65.3 yr to halve beta=0.5; 3.26e+04 yr full stop |
| ISM swept | 4.247e+26 protons over the crossing -> 7.98 PJ released forward on bubble-down |
| gravitational drift | +1.548 s vs Earth over the crossing |
| ship self-dilation | -4.38e-21 (own gravity, negligible) |

## The live drive state (WarpCore)

Every field the running drive carries, with its role. This is the state the viewer animates and the honesty audit inspects.

| Field | Default | Role |
|-------|---------|------|
| `beta_cmd` | -- | commanded beta -- what the helm asked for |
| `beta` | -- | physical beta -- what the shell is actually doing |
| `bubble_cmd` | -- | shell raise/drop command |
| `bubble_on` | -- | shell convergence 0..1 (forms in 18 s) |
| `wall_m` | -- | live wall thickness; drives the energy bill and tidal shear |
| `integrity` | -- | shape-servo health 0..1; below 0.35 the bubble collapses |
| `collapsed / collapse_msg` | -- | failure state and its honest report |
| `was_superluminal` | -- | set when a >1c shell is lost: the 'velocity' was never momentum, so the ship is left at rest |
| `magsail_deployed / rectenna_deployed` | -- | brake / receiver states |
| `coil_phase / coil_glow` | -- | per-sector energisation (96 values) |
| `smes_j` | -- | buffer charge, starts at 1.52 TJ |
| `rad_k` | -- | panel temperature -- lags via real heat capacity (tau=90 s) |
| `load_w / waste_w / beam_w` | -- | live electric load, waste heat, captured tap |
| `exotic_need_j / exotic_debt_j` | -- | negative energy demanded vs OWED -- booked as debt, never supplied |
| `status` | -- | COLD / NOMINAL / UNFUNDED / COLLAPSED readout |
| `led` | -- | cumulative ledger: beam_in, plant_out, kinetic, kinetic_peak, radiated, magsail_regen, brake_dissipated, fuel_kg, am_kg, ism_particles |
| `helm_locked()` | -- | above beta=1 the forward wall is causally disconnected -- commands cannot reach it (Everett 1996) |

## The voyage state (Voyage)

| Member | Role |
|--------|------|
| `phase` | DOCK -> BOOST -> CRUISE -> BRAKE -> ARRIVED (forward only) |
| `x_m / v_ms / beta` | position, velocity, v/c on the Sol-Proxima line |
| `remaining_m / eta_s()` | distance and time to target at current speed |
| `t_coord / t_ship / t_earth` | coordinate, ship and Earth clocks -- ship=Earth modulo gravitational drift |
| `dest_array` | destination photon brake assumed present or not |
| `warp_i / warp` | time-warp rung and multiplier |
| `ism_particles / f_magsail / f_beam` | swept count and live drag forces |
| `arrived_at / log` | arrival timestamp and the mission log |
| `target_m` | Proxima distance, 4.02e+16 m |

Time-warp rungs (- / + to cycle): 1 s/s, 1 min/s, 1 h/s, 1 d/s, 30 d/s, 1 yr/s, 10 yr/s

## The envelope check (every part inside the flat interior)

| Part | reach (m) |
|------|-----------|
| deflector rim | 72.56 |
| hull midbody | 16.00 |
| radiator tip | 152.83 |
| boost rectenna | 99.29 |
| shaping ring | 117.40 |
| cryo unit | 147.10 |
| SMES toroid | 46.15 |
| **interior limit** | **182.24** |

Verdict: radiator tip reaches 152.8 m inside a 182.2 m interior (29.4 m clear). The ring, coils and Casimir cassettes are deliberately absent -- they straddle the wall because they are what sources it.

## The portal installations

The gate hardware (see DIMS `portal_*` keys): a 34 m frame around a 24 m aperture holding a 3 m toroidal rim, 16 field coils and 8 Casimir rings. The throat it would have to hold open is priced below.

| Construction | Size | Bill | Blocker |
|--------------|------|------|---------|
| Morris-Thorne | b0 = 12 m | 2.421e+44 J exotic | tidal 1.27e+14 g at the throat, QI hold 3.25e-26 s vs 4.8 s traversal |
| Visser thin-shell | a = 12 m | 2.905e+45 J exotic | concentrating costs MORE, not less |
| MMP (2020) | r_s = 1.35e+08 m | Casimir-real | needs 45834 M_sun magnetically charged hole; no magnetic monopole observed |
| Survivable throat | b0 = 1.35e+08 m (10.6 Earth diameters) | 2.730e+51 J | the size that keeps a walker alive |

Any portal is also automatically a time machine: mouth clocks desync by `delta_t = t x (rate_A - rate_B)`, and CTCs exist once |delta_t| >= D/c. Full math in README sections 18-19k.

## The eight barriers

| Barrier | Status | Key numbers | Route |
|---------|--------|-------------|-------|
| wall_tidal | FAIL/THEOREM | value_g=1.76e+17; threshold_g=1; gap_orders=17.2; a_at_qi_g=2.7e+81 | thinner wall -- but QI forbids delta < 100 L_P, and thinner = MORE tidal, not less |
| superluminal_nec | FAIL/THEOREM | nec_subluminal=1 | SSV theorem (2022): ANY v > c warp violates NEC. No route -- this is a theorem about the whole class. |
| negative_energy | FAIL/THEOREM | need_j=5.66e+47; have_j=3.09e+06; gap_orders=41.3; cassettes_needed=1.76e+43 | more Casimir cassettes -- would need 2e+43 |
| steering | FAIL/THEOREM | locked_above=1 | forward wall is causally disconnected at v > c. No route -- theorem (Everett, Coule, Krasnikov). |
| thermal | PASSABLE | limit_beta=1.87; limit_k=1.9e+03; T_at_2c=1.96e+03; gap_fraction=0.000252; passable=1; area_needed_m2=3.86e+05; area_have_m2=3.4e+05 | more radiator area -- need 385910 m^2 (have 339910 m^2) |
| ford_roman_wall | FAIL/THEOREM | E_at_qi_j=7e+79; gap_orders=73.4 | QI theorem: wall cannot exceed 100 L_P. At that thickness E = 7.00e+79 J = 10^9 universes. |
| qi_throat | FAIL/THEOREM | tau_max_s=3.25e-26; tau_traverse_s=4.8; gap_orders=26.2 | QI theorem: throat closes 10^26 times before you cross. No route. |
| ctc | CONJECTURE |  | Hawking chronology protection: CTCs trigger divergent vacuum fluctuations at the horizon.  Conjecture, but strongly expected by the majority of the field. |

## Feasibility scorecard

| Function | Verdict | Why |
|----------|---------|-----|
| Metric solves the Einstein field equations | PASS | Alcubierre 1994 is exact. Write the spacetime, read off T^uv. The mathematics has never been the disputed part. |
| Flat, weightless, un-dilated interior | PASS | f = 1 inside: Minkowski exactly. No proper acceleration at any beta, so no g-limit, and ship clocks match Earth clocks. |
| No reaction mass | PASS | The shell sources the metric; nothing is expelled. This is the one advantage over a rocket that survives every objection. |
| Positive-energy source (subluminal) | PASS | Bobrick & Martire 2021 and Fuchs et al. 2024 construct subluminal warp shells satisfying NEC, WEC, DEC and SEC. Real matter. |
| Waste-heat rejection at cruise | PASS | 339910 m^2 of panel rejects 75.9 GW at beta = 0.99 and settles at 1439 K, under the 1900 K graphite limit. |
| Housekeeping power for a decade-long crossing | PASS | 103 GW D-3He plant covers the 16.4 GW cruise load; 20146 kg of fuel crosses to Proxima. |
| Acceleration to cruise speed | PARTIAL | 15 YJ of kinetic energy at beta = 0.5. Nothing storable aboard comes close, so it must be beamed: a 6e+18 W tap for 30.0 d. The ship cannot launch itself, and no design change fixes that. |
| Cruise speed actually reachable | PARTIAL | beta = 0.855, set by beam range and diffraction -- not by the drive. Faster needs a bigger transmitter aperture, not a better warp shell. |
| Deceleration / rendezvous | PARTIAL | Magsail halves speed in 65.28 yr but STOPS in 3.26e+04 yr -- drag falls as v^2. A rendezvous needs a photon-braking array already built at the destination. Without one the mission is a flyby. |
| Interstellar medium loading | PARTIAL | The wall collects everything ahead of it (McMonigal, Lewis & O'Byrne 2012): 4.25e+26 protons over the crossing, released forward as 7.98 PJ when the bubble drops. Aim the arrival away from anything you like. |
| Shell material with the required stress-energy | OPEN | The positive-energy solutions need anisotropic stresses comparable to the energy density -- sound speed approaching c. No known material does this. This is the real open problem, and it is a materials problem, not a relativity problem. |
| Survivable bubble wall | FAIL | Tidal shear reaches 8.80e+16 g across a 2 m body in the wall at beta = 0.5. The interior is perfectly safe; the wall is not a place. |
| Superluminal flight (beta > 1) | FAIL | Requires NEC violation -- and Santiago, Schuster & Visser (2022) proved that holds for EVERY superluminal warp drive, not just Alcubierre's. This is a theorem, not a missing invention. |
| Negative energy at the required scale | FAIL | Needs -1.131e+47 J. The onboard Casimir lattice -- real, measured physics -- supplies -3.09 MJ. Short by 41 orders of magnitude, and by 73 orders at the wall thickness the quantum inequality permits. |
| Steering above beta = 1 | FAIL | The forward wall is causally disconnected from the interior (Everett 1996; Coule 1998). You cannot signal the front of your own bubble, so the whole trajectory must be pre-laid before departure. |
| Thermal survival above beta = 1 | FAIL | Coil load scales as beta^2: 262 GW of waste heat at beta = 2 drives the panels to 1961 K, past the 1900 K limit. The ship cooks before the energy problem even gets a vote. |

## The negative-energy reduction ladder

Every published attempt to shrink the Alcubierre bill, priced against this bubble (R = 183 m):

| Construction | Reduction | Verdict | Citation |
|--------------|-----------|---------|----------|
| ALCUBIERRE 1994   raw thin-wall metric | x1 (baseline) | EXOTIC | Alcubierre, Class. Quantum Grav. 11 L73 (1994) |
| VAN DEN BROECK 1999   microscopic pocket topology | x1e-30 | EXOTIC | Van Den Broeck, Class. Quantum Grav. 16 3973 (1999) |
| WHITE 2011   thick wall + oscillating bubble | x1e-38 | DISPUTED | White, NASA JSC 2011 -- reduction claim, never independently verified |
| LENTZ 2021   hyperbolic soliton from plasma stress-energy | none | REFUTED | Lentz 2021; refuted by Santiago, Schuster and Visser (2021) |
| BOBRICK and MARTIRE 2021   subluminal physical shell | none | PHYSICAL | Bobrick and Martire, Class. Quantum Grav. 38 105009 (2021) |
| FUCHS et al. 2024   constant-velocity positive-energy solution | none | PHYSICAL | Fuchs et al., Class. Quantum Grav. 41 095013 (2024) |

## The honesty audit (12 conservation checks)

| Check | What it asserts |
|-------|-----------------|
| `no_overunity_kinetic` | kinetic gained <= beam + regen delivered |
| `recovery_bounded` | regen <= kinetic energy recovered |
| `plant_within_rating` | plant output <= reactor rating x elapsed |
| `fuel_backs_output` | every joule traced to burnt D-3He |
| `exotic_never_supplied` | negative energy is OWED, never credited |
| `radiates_only_outward` | the Second Law in its dullest form |
| `NEC_reported_truthfully` | never 'satisfied' while superluminal |
| `no_velocity_dilation_dividend` | crew clock = Earth clock |
| `gravitational_drift_modelled` | the only drift is environmental |
| `beam_capture_le_1` | never more than 100% of the beam |
| `all_masses_positive` | real matter only |
| `arrival_requires_stopping` | a flyby is not an arrival |

## Viewer modes & complete controls

| Tab | Shows |
|-----|-------|
| SHIP | the vessel: ring, hull, radiators, reactor, coil sequence; FULL/EXPLODED/ASSEMBLY/SECTION views |
| METRIC | the bubble: York expansion grid, f(r), df/dr, T^00 profiles |
| DILATION | clock rates: comoving vs static, gravitational drift along the route |
| PORTAL | the wormhole: throat, flare-out, tidal profile, both mouths |
| FLIGHT | the mission: boost, cruise, brake, arrival + TEST demo mode |

| Keys | Action |
|------|--------|
| `TAB / click tab` | cycle the five views |
| `drag / wheel / right-drag` | orbit / zoom / pan (R resets) |
| `1 2 3` | full / exploded / assembly; 4 or X section cut |
| `L` | part labels; hover a part for its spec card |
| `, .` | commanded beta down/up |
| `[ ]` | wall thickness thinner/thicker |
| `B` | raise / drop the warp shell |
| `F` | unlock ALCUBIERRE (superluminal, unfunded) |
| `G / K / J` | boost / brake / toggle destination array |
| `T` | TEST demo: auto-play current settings |
| `- +` | time warp down/up |
| `N` | reset mission |
| `P` | pause |
| `I / M / H` | full spec / energy ladder / help |

## CLI modes

| Flag | Report |
|------|--------|
| *(none)* | interactive 3D viewer (needs pygame) |
| `--selftest` | headless physics unit checks |
| `--feasibility` | honest hurdle-by-hurdle scorecard |
| `--spec` | component-by-component engineering spec sheet |
| `--metric` | warp-metric numbers, no window |
| `--ladder` | negative-energy reduction ladder |
| `--dilation` | environmental spacetime dilation: every clock |
| `--portal` | Morris-Thorne wormhole + the real teleporter |
| `--send` | portal traversal tests: send signal/person/object through |
| `--voyage` | headless Sol -> Proxima flight report |
| `--flyby` | with --voyage: no destination array (flyby only) |
| `--all` | every report in order |

## Report & state schemas (every field every report returns)

`boost_profile(beta)` returns: `delivered_j`, `energy_j`, `final_beta`, `ok`, `range_m`, `reason`, `time_s`

`portal_summary()` returns: `b0_m`, `casimir_shortfall_orders`, `density_j_m3`, `energy_j`, `flare_out`, `mass_kg`, `mmp`, `proper_length_m`, `qi_bound_1s_j_m3`, `qi_hold_s`, `qi_shortfall_orders`, `qi_traversal_ratio`, `safe_b0_m`, `safe_energy_j`, `safe_mass_kg`, `safe_shortfall_orders`, `tidal_at_2b0_g`, `tidal_at_4b0_g`, `tidal_g`, `traverse_s`, `visser`, `visser_shortfall_orders`

`portal_traversal(...)` returns: `arrival_offset_s`, `b0_m`, `can_send`, `casimir_j`, `ctc`, `ctc_margin_s`, `elapsed_s`, `exotic_j`, `light_time_s`, `min_b0_m`, `mouth_sep_ly`, `mouth_sep_m`, `offset_s`, `onset_s`, `overall`, `payload`, `payload_size_m`, `qi_hold_s`, `qi_verdict`, `rate_a`, `rate_b`, `rate_diff`, `shortfall_orders`, `survives_tidal`, `throat_open`, `tidal_g`, `tidal_verdict`, `traverse_s`, `when_verdict`

`max_time_displacement()` returns: `chain_wormhole`, `elapsed_s`, `gott_pair`, `kerr_ctc`, `light_time_s`, `max_mechanism`, `max_offset_s`, `nested_wormhole`, `rate_b`, `rate_diff`, `single_wormhole`, `tipler_cylinder`

`clock_ledger(t, x, beta)` returns: `drift_vs_earth_s`, `earth_rate`, `grav_rate_here`, `rates`

## Time-machine constructions (all priced, all blocked)

Any traversable mouth pair whose clocks run at different rates is a time machine after `delta_t = t x (rate_A - rate_B)` builds up. Six mechanisms are priced for a 100-year program:

| Mechanism | Displacement | Basis |
|-----------|--------------|-------|
| single wormhole (one mouth in a well) | 98.59 yr | mouth_B rate 0.0141 at Phi/c^2 = -0.45 |
| chained wormholes (10 pairs) | 985.86 yr | offsets add per pair |
| nested wormholes (2 inside 1) | 197.17 yr | inner offset adds on top |
| Gott cosmic-string pair | 445.26 yr | deficit-angle shunt, needs GUT strings |
| Tipler cylinder | 0.4 s | needs an infinite rotating cylinder |
| Kerr ring interior | 0.0 s | bounded by the spin period |

Winner: **chain at 985.86 yr** -- and every one of them still needs exotic matter or an object nobody has observed (monopoles, cosmic strings, infinite cylinders). The chain also collapses the moment |offset| >= separation/c = 4.25 yr, after which a light signal arrives before it left (chronology protection territory).

The one 'teleporter' that exists is quantum teleportation: 7e+29 bits of state per person, the classical channel still takes 22.2 Gyr at light speed, record distance 1400 km, and it destroys the original.

## Portal traversal tests (the 12 m gate)

| Payload | tidal load | survives | verdict |
|---------|------------|----------|---------|
| signal | 0 g | yes | BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 4.80 s but QI allows only 3.25e-26 s -- 26 orders short |
| person | 1.27e+14 g | no | BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 4.80 s but QI allows only 3.25e-26 s -- 26 orders short |
| object | 1.27e+14 g | no | BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 4.80 s but QI allows only 3.25e-26 s -- 26 orders short |

## The clock ledger (whose clock, how fast)

At mid-cruise (beta = 0.5, halfway to Proxima):

| Clock | Rate (dtau/dt) |
|-------|----------------|
| warp crew (comoving) | 1.000000000000 |
| Earth surface | 0.999999990129 |
| static in the bubble | 0.866025403784 |
| static in the wall | 0.968245836552 |
| relativistic rocket | 0.866025403784 |
| deep space (infinity) | 1.000000000000 |

The comoving crew and Earth differ only by accumulated gravitational drift: 0.311 s over this leg. There is no velocity-dilation dividend -- the honesty audit checks for one and finds none.

## Fuel & ISM scoop economy

| beta | burn (kg/d) | ISM scooped (kg/s) | D-3He yield (kg/d) | net (kg/d) |
|------|-------------|--------------------|--------------------|------------|
| 0.100 | 1.959 | 0.124 | 0.960 | -0.999 |
| 0.250 | 3.090 | 0.309 | 2.401 | -0.689 |
| 0.500 | 6.489 | 0.618 | 4.802 | -1.687 |
| 0.855 | 14.568 | 1.06 | 8.211 | -6.357 |

The scoop is isotope-lean: interstellar gas is nearly all protium, so the D-3He fraction recovered never reaches parity with the burn at any cruise beta. The ship must carry its fuel.

## Buildability rating scale

| Rating | Meaning | Examples on this ship |
|--------|---------|------------------------|
| TODAY | exists; only scale is missing | hull, decks, cryoplant, deflector, pylons, RCS |
| NEAR | physics proven, engineering not | HTS coils, SMES, radiators, boost rectenna |
| FAR | needs an industry nobody has | reactor, antimatter traps, Casimir lattice, magsail, all external infrastructure |
| OPEN | a material nobody has made | the warp shell itself |
| IMPOSSIBLE | barred by theorem | wormhole gates, time machines |

## Model function registry

Every public function in `Warpdrive.py`, grouped by domain, with its signature and contract. This table is harvested by introspection -- it cannot go stale.

### Warp metric & shape

| Function | Contract |
|----------|----------|
| `alcubierre_energy_j(beta, R=None, delta=None)` | Total (negative) energy of the Alcubierre warp field  [J]. |
| `energy_density(x, rho_perp, beta, R=None, delta=None)` | Eulerian energy density T^00 measured by observers at rest  [J/m^3]. |
| `equiv_mass_kg(energy_j)` | E/c^2 |
| `shape_df(r, R=None, delta=None)` | df/dr_s |
| `shape_df_shifted(u, R=None, delta=None)` | df/dr evaluated at r = R + u, computed FROM u directly. |
| `shape_f(r, R=None, delta=None)` | Alcubierre top-hat shape function f(r_s). f -> 1 inside, 0 outside. |
| `wall_tidal_gradient(beta, R=None, delta=None)` | Tidal acceleration across a 2 m body sitting IN the bubble wall [m/s^2]. |
| `warp_energy_integral(R=None, delta=None, samples=4000)` | I = INT_0^inf r^2 (df/dr)^2 dr   [m], by composite Simpson over the wall. |
| `york_theta(x, rho_perp, beta, R=None, delta=None)` | York time / expansion scalar theta = beta c (x / r_s) df/dr_s   [1/s]. |

### Quantum & NEC constraints

| Function | Contract |
|----------|----------|
| `barrier_analysis()` | Returns a dict of barrier -> {value, threshold, gap, passable, route}. |
| `barrier_scorecard()` | Returns a list of (name, status, detail) for the 8 barriers. |
| `casimir_cassette()` | Geometry and yield of ONE onboard Casimir cassette. |
| `casimir_energy_density(gap_m)` | Casimir vacuum energy density between ideal parallel plates  [J/m^3]. |
| `casimir_onboard_j()` | Total negative energy the whole 24-cassette lattice actually holds [J]. |
| `energy_conditions(beta)` | Which pointwise energy conditions the commanded solution satisfies. |
| `ford_roman_bound_j_m3(tau_s)` | Ford-Roman quantum inequality bound on negative energy density  [J/m^3]. |
| `ford_roman_max_throat_tau(b0)` | Longest you can hold a throat of radius b0 open, by the QI bound  [s]. |
| `ford_roman_wall_limit(beta)` | Quantum-inequality bound on the wall thickness  [m]. |
| `horizon_locked(beta)` | True when the forward bubble wall is causally disconnected from the ship. |

### Ship & envelope

| Function | Contract |
|----------|----------|
| `check_envelope(delta=None)` | Does the ship still fit inside its own flat interior? |
| `flat_interior_r(delta=None, R=None)` | Radius of the exactly-flat interior [m]. |
| `mass_budget()` | Component-by-component dry mass, computed from the geometry the renderer |
| `ship_mass_kg()` | -- |

### Power, thermal & fuel

| Function | Contract |
|----------|----------|
| `cruise_load_w(beta, bubble_on=1.0)` | Electrical load to HOLD the warp field at beta [W]. |
| `fusion_fuel_kg(energy_j)` | D-3He mass burnt to deliver this much ELECTRICAL energy. |
| `kinetic_energy_j(beta, mass_kg=None)` | (gamma - 1) M c^2 |
| `lorentz_gamma(beta)` | -- |
| `plant_electric_w()` | Direct-conversion electrical capacity of the D-3He plant [W]. |
| `radiator_area_m2()` | Installed radiating area |
| `radiator_required_m2(waste_w, t_k=None)` | -- |
| `radiator_temp_k(waste_w)` | Equilibrium panel temperature from Stefan-Boltzmann: T = (P/eps sigma A)^1/4. |
| `smes_store_j()` | SMES capacity from first principles: u = B^2 / 2 mu0 over the torus |
| `waste_heat_w(load_w)` | Everything drawn eventually becomes heat: a closed ship exports no work. |

### Propulsion, beam & braking

| Function | Contract |
|----------|----------|
| `beam_brake_force_n(range_to_array_m)` | Photon-pressure braking against an array AT THE DESTINATION [N]. |
| `beam_brake_time_s(beta, mass_kg=None)` | Rough time to stop under destination-array photon braking [s]. |
| `beam_capture_frac(range_m)` | Fraction of the beam the deployed rectenna actually intercepts. |
| `beam_power_w(range_m)` | -- |
| `beam_spot_m(range_m)` | Diffraction-limited spot diameter of the stellar-tap boost beam [m]. |
| `boost_profile(beta, mass_kg=None)` | Can the stellar tap actually get this ship to beta before the ship flies |
| `crossing_time_s(beta)` | Coordinate time for Sol -> Proxima at beta. inf when the boost |
| `ism_blast_energy_j(beta, distance_m, R=None)` | Energy stored in the swept particles, released forward on bubble |
| `ism_particles_swept(distance_m, R=None)` | Protons the bubble sweeps up over a leg. They do not pass through: the |
| `magsail_area_m2()` | -- |
| `magsail_decel_time_s(beta, mass_kg=None, beta_final=None)` | HONEST time to brake from beta down to arrival speed on the magsail [s]. |
| `magsail_drag_n(beta)` | Drag of the magnetic sail against the interstellar medium [N]. |
| `magsail_halving_time_s(beta, mass_kg=None)` | Characteristic time for the magsail to HALVE the speed [s]: t = M/(k v0). |
| `max_boost_beta(mass_kg=None, lo=0.02, hi=0.99)` | Highest cruise beta the beam can actually deliver, by bisection on |
| `rocket_proper_time_s(beta, distance_m)` | Proper time aboard a conventional relativistic cruiser doing the same |

### ISM economy

| Function | Contract |
|----------|----------|
| `ism_d3he_yield_kg_s(beta)` | D-3He reactor-grade fuel mass yieldable per second of scooping [kg/s]. |
| `ism_scoop_gas_kg_s(beta)` | Raw ISM mass flux intercepted by the magsail loop while underway [kg/s]. |

### Clocks & dilation

| Function | Contract |
|----------|----------|
| `clock_ledger(t_ship_s, x_m, beta)` | Every clock in the problem, at one instant. |
| `grav_potential_at(x_m)` | Newtonian potential Phi at distance x along the Sol -> Proxima line |
| `grav_rate(x_m)` | Clock rate dtau/dt at position x relative to a clock at infinity. |
| `lapse_static(r, beta, R=None, delta=None)` | dtau/dt for an observer holding station in the EXTERNAL frame at radius |
| `ship_self_dilation()` | The ship's OWN gravitational time dilation, from its own mass [-]. |
| `static_observer_exists(beta)` | False above |beta| = 1: inside a superluminal bubble there is no such |
| `voyage_grav_drift_s(t_total_s, x_start=0.0, x_end=None)` | Accumulated crew-vs-Earth clock drift over a crossing, from gravity alone. |

### Wormholes & time machines

| Function | Contract |
|----------|----------|
| `chain_wormhole_offset(n_wormholes, elapsed_s, rate_diff)` | Cumulative time offset from a chain of N wormholes in series  [s]. |
| `ctc_by_gravity_well(phi_over_c2, mouth_sep_m=None)` | Park one mouth in a deep well instead. Returns the onset time. |
| `ctc_by_warp_transport(beta)` | Can you make a time machine by CARRYING one mouth on this warp drive? |
| `ctc_exists(mouth_sep_m, offset_s)` | Do closed timelike curves exist right now? |
| `ctc_onset_s(mouth_sep_m, rate_diff)` | Time until a two-mouth wormhole becomes a TIME MACHINE  [s]. |
| `gott_pair_offset(mu_kg_m, v_beta, D_m)` | Gott (1991) two cosmic strings: maximum time displacement  [s]. |
| `kerr_ctc_offset(a_m, r_m, M_kg, n_orbits=1)` | Kerr black-hole CTC: maximum time displacement per orbit  [s]. |
| `max_time_displacement(elapsed_s=3155760000.0, mouth_sep_m=None, phi_over_c2=-0.45, beta=0.999, n_wormholes=10, tipler_L_m=None, tipler_R_m=1.0, tipler_omega_rads=1.0, gott_mu_kg_m=1e+21, gott_D_m=9460730472580800.0, kerr_M_kg=1.98847e+31, kerr_r_m=None, kerr_a_m=None)` | Maximum time displacement across all mechanisms  [s]. |
| `mmp_extremal_charge_c(M_kg)` | Extremal magnetic charge for a black hole of mass M  [C]. |
| `mmp_summary(g_limit=1.0, body_m=2.0)` | The MMP wormhole, fully priced, for a survivable crossing. |
| `mmp_tidal_mass_kg(g_limit=1.0, body_m=2.0)` | Smallest MMP black hole a person survives crossing  [kg]. |
| `mmp_traversal_time_s(M_kg)` | Asymptotic traversal time for the MMP wormhole  [s]. |
| `mouth_clock_rate(phi_over_c2=0.0, beta=0.0)` | Proper-time rate of a wormhole mouth relative to a clock at infinity. |
| `mouth_time_offset_s(rate_a, rate_b, elapsed_s)` | Accumulated clock offset between the two mouths  [s]. |
| `mt_embedding_z(rho, b0)` | Embedding-diagram height z(rho) for the Morris-Thorne throat [m]. |
| `mt_exotic_energy_j(b0, shell_factor=1.0)` | Total exotic energy to hold a throat of radius b0 open  [J]. |
| `mt_flare_out(b0)` | Verify the flare-out condition at the throat. |
| `mt_min_throat_m(g_limit=1.0, body_m=2.0)` | Smallest throat a person survives crossing  [m]. |
| `mt_proper_length(b0, r_far=None)` | Proper radial distance from throat to r_far  [m]. |
| `mt_redshift_phi(r, b0)` | Redshift function Phi(r)  [dimensionless]. |
| `mt_shape_b(r, b0)` | Morris-Thorne shape function b(r)  [m]. |
| `mt_shape_b_prime(r, b0)` | db/dr for the shape function  [dimensionless]. |
| `mt_throat_density(b0)` | Energy density required at the throat  [J/m^3]. |
| `mt_tidal_g(b0, body_m=2.0)` | Tidal acceleration across a body of height body_m at the throat [g]. |
| `mt_tidal_profile(r, b0, body_m=2.0)` | Radial tidal acceleration across body_m at radius r  [g]. |
| `mt_traversal_time_s(b0, v_ms=10.0, length_factor=4.0)` | Proper time to walk through, at v_ms, across ~length_factor throats. |
| `multijump_breakeven_s(mouth_sep_m, beta, rate_diff, overhead_s=None, b0_m=None)` | Fixed point of the backward recurrence: t* = Delta / rate_diff  [s]. |
| `multijump_plan(cycles, elapsed_s, rate_diff, mouth_sep_m, beta, direction='backward', overhead_s=None, fuel_start_kg=None, b0_m=None)` | Iterated portal traversal: the multi-jump ledger. |
| `nested_wormhole_offset(outer_offset_s, inner_offset_s)` | Offset from a wormhole nested inside another wormhole  [s]. |
| `portal_cycle_s(mouth_sep_m, beta, overhead_s=None, b0_m=None)` | External repositioning leg between the mouths at beta, plus hop |
| `portal_summary(b0=None)` | Everything about the gate, in one dict, for the view and the reports. |
| `portal_traversal(b0_m, mouth_a_phi_c2=0.0, mouth_a_beta=0.0, mouth_b_phi_c2=0.0, mouth_b_beta=0.0, mouth_sep_m=None, elapsed_s=0.0, payload='person', payload_size_m=2.0, payload_speed_ms=10.0)` | Send something through the portal.  All four real-physics answers. |
| `quantum_teleport_facts()` | Quantum teleportation is real, demonstrated, and does none of the things |
| `tipler_cylinder_offset(L_m, R_m, omega_rads, M_kg=None)` | Tipler cylinder CTC: maximum time displacement  [s]. |
| `visser_shell_energy_j(a_m, M_kg)` | Total exotic energy of the Visser thin shell  [J]  (negative). |
| `visser_shell_mass_kg(a_m, M_kg)` | Exotic MASS of the Visser thin shell  [kg]  (negative). |
| `visser_summary(a_m=None, M_kg=None)` | The Visser thin-shell wormhole, priced. |

### Honesty & audits

| Function | Contract |
|----------|----------|
| `buildability_ledger()` | Every line of the mass budget, rated for when it could actually be |
| `feasibility_scorecard()` | Function-by-function honest scorecard, in the style of LS.py's |
| `honesty_audit(core, voyage, verbose=True)` | -- |
| `operations_ledger()` | What each mass line needs to OPERATE, not just to be built: power |

### Reports & viewer plumbing

| Function | Contract |
|----------|----------|
| `bar(surf, font, x, y, w, h, frac, color, label, valtext, mark=None, lo=None, hi=None)` | Horizontal bar with optional threshold markers. |
| `build_portal_parts(detail=1.0)` | The portal gate at true scale, plus the spacetime it claims to make. |
| `build_ship_parts(detail=1.0)` | Build every part of the WD-1 to scale. Returns an ordered list of Part. |
| `build_special_parts(detail=1.0)` | The WD-88 Foldmobile at true car scale, meshed at CAR_MODEL_DETAIL |
| `chip(surf, font, x, y, text, on, col_on=None)` | A small toggle pill with accent border on the active state. |
| `contrast_text(bg_rgb, light=(230, 236, 245), dark=(10, 14, 20))` | Pick a readable text colour for a given background. |
| `draw_bubble_glow(surf, cx, cy, r, intensity, col=None, pulse_phase=0.0)` | Soft concentric halo for the active warp shell. |
| `draw_vignette(surf, strength=0.22)` | Subtle corner darkening for cinematic depth. |
| `info_sections()` | -- |
| `log_bar_x(value_j, x0, x1, lo_exp=0.0, hi_exp=80.0)` | Map |E| onto a log10 axis across a pixel span. |
| `main(argv=None)` | -- |
| `panel(surf, x, y, w, h, alpha=214)` | Semi-transparent panel with rounded border, gradient fill, and |
| `print_startup_banner()` | -- |
| `project(pts, az, el, dist, cx, cy, focal, pan=(0.0, 0.0))` | Project world points through the same orbit camera the ShipRenderer uses. |
| `report_dilation()` | Every clock in the problem, and which one the marketing quotes. |
| `report_feasibility()` | -- |
| `report_ladder()` | The historical attempts to make the exotic bill affordable, and how each |
| `report_metric()` | Everything the warp metric says, computed live from the shape function. |
| `report_portal()` | The portal, priced. |
| `report_portal_test()` | Run portal traversal scenarios: signal, person, object, time machine. |
| `report_spec()` | Every component of the ship, specified: geometry, count, and the mass |
| `report_voyage(beta=0.5, dest_array=True)` | Headless Sol -> Proxima flight, printed as a mission log. |
| `selftest()` | -- |
| `text_shadow(surf, font, text, pos, color, shadow=(0, 0, 0), offset=(1, 1))` | Render text with a 1-pixel drop shadow for contrast over 3D scenes. |
| `vgradient(surf, top, bot)` | Vertical gradient fill, numpy-vectorized. |
| `wrap_plain(text, width)` | -- |
| `wrap_text(font, text, maxpx)` | -- |

### Formatting & math helpers

| Function | Contract |
|----------|----------|
| `clamp(x, lo=0.0, hi=1.0)` | -- |
| `fmt_dist(m)` | -- |
| `fmt_energy(j)` | -- |
| `fmt_mass(kg)` | -- |
| `fmt_power(w)` | -- |
| `fmt_time(s)` | -- |
| `orders_of_magnitude(a, b)` | log10 |a/b| |
| `rot_x(a)` | -- |
| `rot_y(a)` | -- |
| `rot_z(a)` | -- |

### Miscellaneous

| Function | Contract |
|----------|----------|
| `car_casimir_j()` | Negative energy the conduit-liner strips actually hold [J] |
| `car_fault_effects(fault)` | What each injected fault does, in physics terms |
| `car_mass_budget()` | The kerbside mass, derived the way the ship's is: every line is a |
| `car_mph_step(mph, thr, brk, fired, dt_s, cell_k=295.0, armed=True)` | One tick of road speed [mph]. Returns (mph, fired_now). Hub motors |
| `car_ops_ledger()` | (part key, electric draw W, duty, failure mode) |
| `car_part_mass()` | Map every car part onto lines of car_mass_budget() so each spec card |
| `car_power_budget()` | Loads vs the fusion cell: every ops-ledger draw summed, supply |
| `car_thermal_step(cell_k, heat_w, dt_s, louver_eff=1.0)` | One Euler step of the trunk cell's thermal balance [K]. The louver |
| `car_transit(t0_s, hop_s, lat_deg=34.05, lon_deg=-118.24)` | Solve the landing: the car must arrive at the SAME Earth-fixed road |
| `car_trigger_v()` | 88 mph in SI |
| `earth_helio_pos(t_s)` | Heliocentric ecliptic position of Earth at time t [s]. Kepler orbit to |
| `earth_surface_offset(t_s, lat_deg, lon_deg)` | Position of a road-fixed point relative to Earth's centre: sidereal |
| `road_frame(t_s, lat_deg=34.05, lon_deg=-118.24)` | The road's LOCAL frame carried inertially: (east, north, up) unit |
| `road_inertial_speed(lat_deg=34.05)` | How fast the pavement itself moves through inertial space: Earth's |
| `road_solar_hour(t_s, lon_deg=-118.24)` | Local mean solar hour at the road: the road's hour angle relative to |

### Internal helpers (private, still documented)

| Function | Contract |
|----------|----------|
| `_annulus_cylinder(r_out, r_in, z0, z1, seg=40)` | Hollow tube closed at both axial ends (a pipe with real wall thickness). |
| `_args_real(fn)` | Boundary coercion for helpers whose parameters are ALL numeric: every |
| `_box(cx, cy, cz, sx, sy, sz)` | -- |
| `_build_portal_parts_impl()` | -- |
| `_build_ship_parts_impl()` | -- |
| `_build_special_parts_impl()` | -- |
| `_car_loft(stations)` | Loft the coupe body: stations are (z, half_width, y_top, y_bot) and the |
| `_coil_arc(r_mid, r_in, r_out, a0, a1, seg_arc=6, seg_tube=10)` | Winding-pack shell that follows the torus centreline along an arc. |
| `_coil_count()` | Coil count from DIMS, bounded.  The physical ring carries tens of |
| `_component_info_sections()` | The whole bill of materials, explained line by line. |
| `_deck_plate(r_out, z0, z1, holes=(), seg=48, rings=8)` | Solid circular slab with off-axis penetration holes + drawn collars. |
| `_detail_seg(seg)` | -- |
| `_dish(r_out, depth, z0, seg=28, rings=5, flip=False)` | A parabolic dish opening along +Z (deflector, rectenna collector). |
| `_earth_rate()` | -- |
| `_envelope_points()` | Extreme (radius, |z|) corners of every part that must live INSIDE the |
| `_finite(*vals)` | True only when every argument is a finite real number. Mesh generators |
| `_function_registry_lines()` | Every public function in this module, grouped by domain, with its |
| `_grp(meshes, group)` | -- |
| `_hull_loft(sections)` | Loft a smooth body from circular cross-sections along Z. |
| `_info_sections()` | -- |
| `_label(surf, font, text, pos, accent=False, color=None)` | -- |
| `_luminance(rgb)` | Relative luminance of an RGB colour (0..1). Used by contrast_text(). |
| `_mix(c1, c2, t)` | -- |
| `_mt_funnel(b0, rho_max, rings=13, seg=40, sign=1.0)` | Wire mesh of one half of the Morris-Thorne embedding diagram. |
| `_numeric_dims()` | _Dims copy of DIMS with every non-real value already coerced to NaN, |
| `_pipe_path(pts, r, seg=10, closed=True)` | Sweep a circle along a polyline |
| `_place(meshes, pivot, tilt=(0.0, 0.0), group=None)` | Move a set of origin-built meshes into position (and orientation). |
| `_prep_global(plist)` | Merge every part's prepped static meshes into shared vertex arrays |
| `_prep_mesh(m)` | One-time render caches for a Mesh: a padded (nf, w) face-index array |
| `_prep_part(part)` | Collapse a Part's static meshes into one big indexed mesh per draw |
| `_print_traversal(t)` | Print one traversal result compactly. |
| `_radial(angle)` | Rotation taking a +Z-built primitive to point radially outward. |
| `_real(v)` | Coerce a would-be numeric to float; non-convertible -> NaN.  Lets the |
| `_rgb(c, fallback=(0, 0, 0))` | Coerce any colour-ish value to a valid RGB triple; a channel that is |
| `_ring_wire(r, z, seg=64, axis='z')` | A single closed wire loop |
| `_rod(p1, p2, r, seg=10)` | A capped cylinder between two arbitrary points |
| `_rule(title)` | -- |
| `_runtime_state_lines()` | Every field the live simulation carries |
| `_sech2(x)` | 1/cosh^2(x), overflow-safe. math.cosh overflows past ~710; sech^2 is |
| `_smooth_sections(ctrl, sub=4)` | Catmull-Rom subdivision of (z, radius) control points -> a smooth loft. |
| `_solid_cylinder(r, z0, z1, seg=32)` | Capped cylinder about +Z. |
| `_spec_key_lines()` | Every key of DIMS, PLANT and DRIVE with the engineering comment that |
| `_sphere(r, seg=20, rings=12, squash=1.0)` | UV sphere about the origin; `squash` scales Z (oblate hull domes). |
| `_tangential(angle)` | Rotation taking a +Z-built primitive to lie ALONG the ring tangent at |
| `_tilt_z(v)` | Rotate an Earth-fixed vector (equatorial frame, z = pole) into the |
| `_torus(R, r, seg_major=48, seg_minor=12, a0=0.0, a1=6.283185307179586, closed=True)` | Torus (or torus ARC from a0 to a1) in the X-Y plane about +Z. |
| `_torus_surface(R, r)` | -- |
| `_trender(font, text, color)` | font.render with a bounded surface cache: the UI redraws a few |
| `_wire_ellipsoid(a, b, c)` | Bubble wireframe: latitude ellipses plus three meridian loops, axes |
| `_xform(verts, mat=None, off=None)` | Bake a rotation and/or translation into a vertex list. Used for parts |
| `_xy(pos)` | Coerce a position-ish value to a finite (x, y) float pair or None. |

### Classes

| Class | Role |
|-------|------|
| `_Dims` | hostile-input-proof dict wrapper -- deleted/missing keys read as nan instead of raising |
| `Mesh / Part` | renderable geometry (vertices, faces, explode offsets) |
| `ShipRenderer` | builds the ship/portal meshes from DIMS |
| `WarpCore` | the live drive state machine (above) |
| `Voyage` | the mission state machine (above) |
| `MetricCam / Starfield / App` | camera, backdrop and the pygame application shell |

#### `Mesh` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self, verts, faces, color, name='', spin=0.0, group='default', pivot=(0.0, 0.0, 0.0), tilt=(0.0, 0.0), wire=False, glow=False, hot=False)` | Initialize self.  See help(type(self)) for accurate signature. |
| `world_verts(self, angle)` | -- |

#### `Part` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self, key, name, meshes, specs, order, explode, color)` | Initialize self.  See help(type(self)) for accurate signature. |

#### `ShipRenderer` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self, parts_builder, home_az=0.62, home_el=0.42, home_dist=340.0, section_keys=())` | Initialize self.  See help(type(self)) for accurate signature. |
| `reset_view(self)` | -- |
| `zoom_at(self, factor, mouse_pos=None, rect=None)` | -- |
| `orbit(self, dx, dy, fine=False)` | -- |
| `pan_by(self, dx, dy, fine=False)` | -- |
| `set_view(self, mode)` | -- |
| `toggle_section(self)` | -- |
| `assembly_next(self)` | -- |
| `assembly_prev(self)` | -- |
| `active_part(self)` | -- |
| `placing_part(self)` | -- |
| `_sync_pop(self)` | -- |
| `tick(self, dt)` | -- |
| `_layout(self, pi, vw, eamt)` | -- |
| `render(self, surf, rect, angles, mouse_pos=None, show_labels=True, label_font=None, interactive=False, coil_glow=None, drive_power=0.0, rad_heat=0.0, bubble_on=0.0)` | Paint every visible facet back-to-front. `coil_glow` is the rotating |
| `_section_cut(self, key, wvx, face)` | Remove the +X half of the bulky parts |

#### `WarpCore` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self)` | Initialize self.  See help(type(self)) for accurate signature. |
| `mode  *(property)*` | -- |
| `exotic  *(property)*` | -- |
| `kinetic_now_j(self)` | -- |
| `energy_conditions(self)` | -- |
| `helm_locked(self)` | Above beta = 1 the crew cannot signal the forward wall, so no new |
| `_thermal(self, dt)` | -- |
| `_integrity(self, dt)` | Bubble integrity: what actually breaks a warp drive in this model. |
| `collapse(self, msg)` | The shell lets go. |
| `update(self, dt, world=None)` | Advance one tick. `dt` is SHIP seconds (already time-warped). |

#### `Voyage` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self)` | Initialize self.  See help(type(self)) for accurate signature. |
| `warp  *(property)*` | -- |
| `beta  *(property)*` | -- |
| `remaining_m  *(property)*` | -- |
| `cycle_warp(self, d)` | -- |
| `note(self, text)` | -- |
| `eta_s(self)` | -- |
| `update(self, dt_real, core)` | Advance the voyage by dt_real real seconds x the time-warp factor. |
| `_step(self, dt, core)` | -- |
| `begin_boost(self, core)` | -- |
| `begin_brake(self, core)` | -- |
| `auto_step(self, core, tick_s=0.0)` | One scripted phase advance for the viewer's TEST mode. |
| `auto_done  *(property)*` | A demo has nothing left to show: arrived, or reached the target |
| `reset(self, core)` | -- |

#### `MetricCam` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self, az=1.15, el=0.52, dist=560.0)` | Initialize self.  See help(type(self)) for accurate signature. |
| `reset_view(self)` | -- |
| `zoom_at(self, factor, mouse_pos=None, rect=None)` | -- |
| `orbit(self, dx, dy, fine=False)` | -- |
| `pan_by(self, dx, dy, fine=False)` | -- |
| `set_view(self, mode)` | -- |
| `toggle_section(self)` | -- |
| `active_part(self)` | -- |
| `placing_part(self)` | -- |
| `tick(self, dt)` | -- |

#### `Starfield` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self, n=520, seed=7)` | Initialize self.  See help(type(self)) for accurate signature. |
| `draw(self, surf, rect, streak=0.0, drift=0.0)` | Static fields are painted once and blitted; only the streaking |
| `_star_col(self, i, brightness)` | Blackbody-coloured star: base colour from spectral class, scaled by |
| `_paint(self, surf, rect, streak=0.0, drift=0.0)` | -- |

#### `App` methods & properties

| Member | Contract |
|--------|----------|
| `__init__(self)` | Initialize self.  See help(type(self)) for accurate signature. |
| `_rebuild_bg(self)` | -- |
| `_rend(self)` | -- |
| `flash(self, text)` | -- |
| `set_wall(self, factor)` | -- |
| `set_beta(self, d)` | -- |
| `handle_events(self, dt)` | -- |
| `_chip_click(self, name)` | -- |
| `_toggle_test(self)` | TEST mode: auto-play the mission with the settings currently |
| `_test_tick(self, dt)` | Drive the demo: hold each phase a couple of real seconds so the |
| `_toggle_ftl(self)` | -- |
| `_key(self, k, fine)` | -- |
| `update(self, dt)` | -- |
| `draw(self)` | -- |
| `draw_topbar(self)` | -- |
| `draw_ship(self)` | -- |
| `draw_view_tabs(self, rect)` | -- |
| `draw_ship_panel(self)` | -- |
| `draw_spec_card(self)` | -- |
| `_spec_card(self, part)` | -- |
| `draw_metric(self)` | Draw the spacetime, not the hardware. |
| `draw_profiles(self, b, R, delta)` | -- |
| `draw_metric_panel(self, b, R, delta)` | -- |
| `draw_flight(self)` | -- |
| `draw_flight_hud(self)` | -- |
| `draw_flight_controls(self)` | -- |
| `draw_dilation(self)` | Whose clock, and where. |
| `draw_dilation_graphs(self, beta, R, delta)` | -- |
| `draw_clock_panel(self, beta)` | -- |
| `draw_portal(self)` | -- |
| `draw_portal_panel(self)` | -- |
| `draw_special(self)` | -- |
| `draw_special_panel(self)` | -- |
| `draw_ladder(self)` | Thirty years of trying to make the exotic bill affordable, on one |
| `draw_help(self)` | -- |
| `draw_info(self)` | -- |
| `run(self)` | -- |

## Mesh & render budget (the geometry inventory)

Every part the viewer draws, with its live tessellation. Vertex and facet counts are computed from the same `build_*_parts()` calls the renderer uses.

| Part | meshes | vertices | facets |
|------|--------|----------|--------|
| ship: CREW HULL (flat spacetime) | 26 | 14658 | 13516 |
| ship: D-3He FUSION REACTOR | 11 | 590 | 651 |
| ship: ANTIMATTER PENNING TRAPS | 16 | 1680 | 1472 |
| ship: SMES FIELD BUFFER | 10 | 844 | 892 |
| ship: CRYOPLANT (16 units) | 32 | 800 | 1104 |
| ship: STRUCTURAL PYLONS (12) | 12 | 96 | 72 |
| ship: MAIN WARP RING (96 sectors) | 384 | 21504 | 16896 |
| ship: HTS FIELD COILS (96) | 96 | 20160 | 20160 |
| ship: CASIMIR NEGATIVE-ENERGY LATTICE (96) | 96 | 768 | 576 |
| ship: FORE SHAPING RING | 2 | 552 | 552 |
| ship: AFT SHAPING RING | 2 | 552 | 552 |
| ship: WASTE-HEAT RADIATORS (60) | 120 | 960 | 720 |
| ship: NAVIGATION DEFLECTOR | 3 | 302 | 275 |
| ship: BOOST RECTENNA | 2 | 177 | 175 |
| ship: RCS / ION PODS (32) | 32 | 704 | 960 |
| ship: MAGNETIC SAIL (drawn 1:4000) | 10 | 208 | 50 |
| ship: WARP BUBBLE (spacetime) | 14 | 724 | 14 |
| **ship total** | **868** | **65279** | **58637** |
| portal: GATE A  (mouth, Sol side) | 8 | 516 | 504 |
| portal: THROAT FIELD COILS (16) | 16 | 576 | 576 |
| portal: THROAT CASIMIR CASSETTES (8) | 16 | 208 | 240 |
| portal: THE THROAT  (embedding diagram) | 3 | 1096 | 47 |
| portal: GATE B  (mouth, far side) | 1 | 279 | 279 |
| **portal total** | **44** | **2675** | **1646** |

## Module tables & configuration constants

| Name | Value | Role |
|------|-------|------|
| `SCALE_S` | the refit scale factor -- every macroscopic length is WD-1's x 1.8344 |
| `SHIP_LEN_M / SHIP_SPAN_M` | overall envelope 210.9 x 395.4 m |
| `GALACTIC_PHI_C2` | ambient galactic potential = -1e-06 |
| `EARTH_ORBIT_RATE` | None -> Earth clock includes orbit+spin |
| `VISUAL_DETAIL` | tessellation multiplier = 1.05 |
| `INFO_SECTIONS` | lazy section cache (None until built) |
| `WELLS` | route gravity wells: Sol M=1.99e+30 kg at 0 m (r_min 1.5e+11 m); Proxima M=2.43e+29 kg at 4.02e+16 m (r_min 7.26e+09 m) |
| `QT` | quantum-teleportation constants: {'record_km': 1400.0, 'bits_per_qubit': 2.0, 'human_atoms': 7e+27, 'bits_per_atom': 100.0, 'channel_bps': 1000000000000.0} |
| `MULTIJUMP` | ISM isotope fractions + hop overhead: {'ism_h_frac': 0.91, 'ism_he_frac': 0.09, 'ism_d_over_h': 2e-05, 'ism_he3_over_he4': 0.0002, 'd3he_d_mass_frac': 0.4, 'd3he_he3_mass_frac': 0.6, 'hop_overhead_s': 30.0} |
| `PHASES` | DOCK -> BOOST -> CRUISE -> BRAKE -> ARRIVED |
| `VOYAGE_WARP` | [1.0, 60.0, 3600.0, 86400.0, 2592000.0, 31560000.0, 315600000.0] |
| `VOYAGE_WARP_LABEL` | ['1 s/s', '1 min/s', '1 h/s', '1 d/s', '30 d/s', '1 yr/s', '10 yr/s'] |
| `SECTION_KEYS` | 17 hoverable spec keys: hull, reactor, smes, ring, coils, casimir, amtraps, capfore, capaft, collector, deflector, radiators, pylons, cryo, rcs, bubble, magsail |
| `C_* palette` | 28 colour constants (BG, hull/ring/coil/radiator pairs, text, accent, good/warn/bad, panels) |

| Phase | Note (live `PHASE_NOTE`) |
|-------|--------------------------|
| DOCK | At the tap. Bubble down, rectenna stowed. Nothing has cost anything yet. |
| BOOST | Under the beam. Every joule of (gamma-1)Mc^2 comes from outside the ship. |
| CRUISE | Free. A constant-velocity warp solution is a stationary spacetime. |
| BRAKE | Magsail against the ISM. The only deceleration authority that exists. |
| ARRIVED | Proxima Centauri b. Ship clock and Earth clock agree -- that is the point. |

## Self-test coverage map (every check label)

All `check()` call sites in `selftest()`, in order; labels inside loops expand once per case (6 template sites expand the 389 calls to 417 executed checks).

1. f -> 1 deep inside the bubble
2. f -> 0 far outside
3. f = 1/2 at the wall radius
4. energy integral matches R^2 sigma/3 over 33 decades
5. reproduces Alcubierre 1994 (~1e64 J at R=100 m, v=10c)
6. Alcubierre energy is NEGATIVE
7. Casimir density is NEGATIVE
8. Casimir falls as 1/a^4
9. theta is antisymmetric (contract ahead, expand behind)
10. subluminal satisfies the NEC
11. superluminal violates the NEC
12. helm locks above beta = 1
13. gamma(0.6) = 1.25 exactly
14. kinetic energy is (gamma-1)Mc^2
15. superluminal has no kinetic-energy solution
16. radiators hold below the graphite limit at beta = 0.99
17. radiators FAIL above beta = 1 (as they must)
18. Stefan-Boltzmann round-trips
19. mass budget sums to the ship mass
20. every component mass is positive
21. every mass-budget component has a specification row
22. beam capture never exceeds unity
23. magsail stop-time exceeds halving-time by orders
24. max cruise beta is emergent and subluminal
25. KE is superlinear: beta=0.9 costs ~5x beta=0.6 for 1.5x speed
26. KE at beta=0.99 exceeds KE at max cruise by >5x
27. boost profile succeeds at max cruise beta
28. boost profile FAILS above max cruise beta
29. delivered energy matches KE at max cruise (within 5%)
30. beam capture at 1.0 ly is ~1/4 of capture at 0.5 ly (1/L^2)
31. lighter ship reaches higher beta (refit lever)
32. comoving crew have NO velocity dilation
33. a STATIC observer inside gets the full Lorentz factor
34. dilation field vanishes outside the bubble
35. no static observer exists above beta = 1
36. Earth's clock rate matches the textbook solar potential
37. departure starts at Earth's rate (to Proxima's reach)
38. deep space is flat to a part in 1e12
39. crew gain a few seconds on Earth, gravitationally
40. the ship's own gravity is negligible and known
41. throat energy density is NEGATIVE
42. exotic bill scales linearly with throat radius
43. throat density blows up as b0 shrinks (small portals are HARDER)
44. embedding diagram is flat at the throat and flares out
45. a walk-through gate is lethal
46. survivable throat is planetary in scale
47. Casimir cannot pay for either throat
48. warp transport CANNOT desynchronise the mouths
49. a relativistic rocket CAN
50. a mouth in a deep well makes a time machine in finite time
51. a mouth at rest never does
52. quantum teleportation carries no FTL information
53. teleporting a person exceeds the age of the universe
54. Morris-Thorne throat satisfies b(r0) = r0
55. flare-out condition holds (b'(r0) < 1)
56. tidal profile matches throat value at r = b0
57. tidal profile falls as 1/r^4 away from throat
58. proper length of throat is a few b0
59. Ford-Roman QI bound is negative (forbids sustained negative energy)
60. QI max hold time is far shorter than traversal time
61. QI bound at 1s is dozens of orders below throat demand
62. MMP wormhole needs magnetically charged black holes
63. MMP survivable mass is stellar-scale (thousands of M_sun)
64. MMP throat radius matches Morris-Thorne survivable throat
65. MMP traversal time is finite and human-scale
66. Visser thin-shell energy is negative (exotic)
67. Visser shell needs MORE exotic mass than MT volume (sheet < volume)
68. Visser shell exotic requirement vanishes at the horizon
69. mouth at rest in flat space ticks at rate 1
70. mouth in a gravity well ticks SLOWER
71. moving mouth ticks SLOWER (SR dilation)
72. gravitational and kinematic dilation combine
73. time offset grows linearly with elapsed time
74. CTC exists when offset exceeds light-time
75. Proxima light-time is ~4.25 years
76. signal survives tidal (no size)
77. signal through 12 m gate is blocked by QI
78. person survives the survivable throat
79. survivable throat still blocked by QI
80. gravity-well mouth desynchronises (offset > 0)
81. deep well + 20 yr produces CTCs
82. warp-carried mouth does NOT desynchronise
83. rocket-carried mouth DOES desynchronise
84. max desync (neutron star + 0.99c) produces large offset
85. max desync at 1 AU produces CTCs within 1 year
86. max desync onset is minutes not years at 1 AU
87. extreme desync (horizon + 0.999c) offset approaches elapsed
88. forward jump = backward jump (symmetric wormhole)
89. shape_df at R = -sigma/2 (tanh top-hat derivative)
90. shape_df is antisymmetric (contract ahead, expand behind)
91. energy_density matches -(c^4/8piG)(beta^2 rho^2/4r^2)(df/dr)^2
92. wall tidal gradient is lethal at beta = 0.5
93. wall tidal increases linearly with beta
94. ford_roman_wall_limit ~ 100 L_planck at beta = 1
95. ford_roman_wall_limit scales as 1/beta
96. SMES stores positive energy
97. SMES is finite and reasonable (< 10 TJ)
98. fusion fuel is positive and finite
99. beam_spot = 2.44 lambda L / D (Airy diffraction)
100. beam spot increases with distance (diffraction)
101. magsail drag = Cd * rho_ISM * v^2 * A
102. magsail drag scales as v^2
103. beam brake force is positive
104. beam brake force <= 2P/c (photon pressure limit)
105. beam brake time is positive and finite
106. ism_particles = n_ISM * pi * R^2 * distance
107. ism_blast = N * m_p * c^2 * beta^2/2 (conservative floor)
108. rocket proper time = (d/beta c) / gamma
109. rocket ages LESS than warp crew at same beta
110. MT redshift Phi = 0 (zero-tidal choice)
111. MMP Q_ext = sqrt(4 pi eps0 G) M
112. Visser shell energy = shell mass * c^2
113. ctc_onset = (D/c) / |rate_diff|
114. MT: rho * (4/3)pi b0^3 = E (density x volume = energy)
115. MT: mt_tidal_g = mt_tidal_profile at throat
116. MT: tidal at b0_min = 1 g (by construction)
117. Alcubierre E scales as beta^2: E(2)/E(1) = 4
118. Alcubierre E scales as 1/delta: E(0.1)/E(1) = 10
119. Alcubierre E = -(c^4/12G) beta^2 I (integral formula)
120. gamma(0) = 1
121. Ford-Roman: |rho_QI(tau_max)| = |rho_throat| (derivation)
122. Visser: E_shell = m_shell * c^2
123. MMP: M = c^3 sqrt(L/(4 G^2 g))
124. mouth_clock_rate = sqrt(1+2Phi/c^2) / gamma (consistency)
125. barrier: wall tidal > 1 g (FAIL)
126. barrier: thinner wall = MORE tidal (anti-route)
127. barrier: wall tidal NOT passable
128. barrier: NEC satisfied subluminal (beta < 1)
129. barrier: NEC violated superluminal (beta > 1) -- SSV theorem
130. barrier: superluminal NOT passable (theorem)
131. barrier: negative energy gap > 30 orders
132. barrier: cassettes needed > 1e30
133. barrier: negative energy NOT passable
134. barrier: steering locked above beta = 1
135. barrier: steering NOT passable (theorem)
136. barrier: T at 2c exceeds radiator limit
137. barrier: thermal IS passable (more radiators)
138. barrier: area needed > area have
139. barrier: Ford-Roman wall ~ 100 L_Planck
140. barrier: E at QI wall > 1e70 J (10^9 universes)
141. barrier: Ford-Roman wall NOT passable (theorem)
142. barrier: QI throat gap > 20 orders
143. barrier: QI throat NOT passable (theorem)
144. barrier: CTC NOT passable (conjecture)
145. barrier: scorecard has 8 entries
146. barrier: 3 FAIL + 4 THEOREM + 1 CONJECTURE
147. ship builds every part
148. assembly order is a complete sequence
149. all geometry is finite
150. portal builds and is finite
151. foldmobile builds and is finite
152. the whole car fits inside its own warp shell
153. four hub drives stand at the corners, below the body
154. the arming trigger is exactly 88 mph
155. foldmobile exotic bill is negative and real
156. foldmobile Casimir strips hold negative energy
157. foldmobile is honestly underfunded, not silently working
158. no gas engine anywhere in the build
159. the car's kerbside mass is derived, not typed
160. every car part carries an operations row (power/duty/fail)
161. the car's bus is funded (fusion covers every load)
162. every car part carries a derived mass share
163. the transition sequencer carries a real spec card
164. the trunk cell has a real thermal balance
165. injected faults do what the ops ledger promises
166. 87.9 mph does NOT fire -- the trigger is exact
167. crossing 88 in one big step still fires exactly on threshold
168. overspeed clamps to the 130 mph ceiling
169. a poisoned nan speedometer is recovered, not trusted
170. a negative-speed poison is healed by the drag floor
171. a quenched SMES means 88 mph is just driving (no fire)
172. a heat-soaked cell derates the drive below the trigger
173. frozen inputs produce no motion and no fire
174. the cell's temperature is bounded by its own radiative equilibrium, even under a hostile 1e9 s step
175. thermal state survives total nan poisoning
176. the thermal floor holds under absurd cooling
177. the solve holds at the poles and at 32,000-year epochs
178. the coldest plausible coolant charge can't freeze the model
179. the car builds under hostile detail factors
180. the trigger is the REAL 88 mph -- m/s not 88 m/s
181. earth's orbit carries real eccentricity (perihelion->aphelion)
182. the tilted spin axis holds the road exactly on the sphere
183. the pavement itself moves ~29.8 km/s inertial
184. a zero hop lands where it left
185. a half-year hop crosses the orbit (~2 AU)
186. departure and arrival both sit on the SAME road-fixed point
187. the inertial landing point is genuinely elsewhere
188. a fractional-day hop keeps the road fix but shifts inertially
189. the solve carries the lane heading, not just the point
190. ephemeris survives hostile inputs
191. the road's clock face changes across the hop (solar time)
192. the car still carries its car parts (controls, glass, kit)
193. the informational document explains the foldmobile and the same-road-spot solve
194. the ship fits inside its own flat interior
195. a thick wall squeezes the ship out (the real volume trade)
196. the warp ring straddles the wall, as its source must
197. coils wrap the tube at the billed standoff and build
198. ring draws its billed wall thickness
199. Casimir cassettes sit inside the tube hollow they feed
200. hull loft honours hull_shell_rfrac as its mean radius
201. every deck slab fits inside the lofted skin
202. every antimatter trap sits inside the hull with clearance
203. every pierced deck carries its drawn collar opening
204. reactor torus is inside the hull barrel
205. SMES rides its spec station
206. shaping rings sit at +/- cap_offset_m
207. radiator root and inner radius match spec
208. radiator panel thickness is rad_t_m
209. cryoplant mounts at cryo_mount_rfrac of the interior
210. deflector dish mounts flush to the hull nose
211. pylons bridge hull skin to ring tube
212. rectenna roots at collector_z0_m
213. every billed RCS pod is drawn
214. RCS pods clear the Penning bays and reactor
215. bubble draws the wall and flat interior it specifies
216. a full crossing completes
217. demo auto-step holds DOCK when no beta is commanded
218. demo auto-step drives DOCK -> BOOST with a beta commanded
219. demo auto-step holds CRUISE while out of brake range
220. demo auto-step drives CRUISE -> BRAKE inside brake range
221. demo auto-step brakes at once with no destination array
222. demo auto-step is terminal at ARRIVED
223. demo auto_done fires on a flyby (target reached, not stopped)
224. demo auto_done is false mid-cruise
225. gamma clamps to beta=0.9999999 (avoids singularity)
226. KE(beta=0) = 0
227. KE(beta=1) is infinite (no subluminal solution)
228. KE(beta=1.5) is infinite
229. mouth at Phi/c^2 = -0.5 (horizon) has rate 0
230. mouth at beta = 1 has rate ~0.000447 (clamped gamma)
231. mouth at Phi/c^2 = -0.49 (deep well) has rate ~0.14
232. CTC onset with zero rate diff is infinite
233. CTC onset with rate diff = 1 is light-time
234. beam capture at 1e20 m is ~0 (deep space)
235. beam capture at 1e0 m is 1.0 (inside spot)
236. magsail drag at beta=0 is 0
237. magsail drag at beta=1 is positive
238. Ford-Roman bound at tau=0 diverges to -inf
239. Ford-Roman bound at tau=1e-10 is finite
240. thinner wall needs more exotic energy (1/delta scaling)
241. forward and backward offsets are symmetric
242. CTC onset scales as 1/rate_diff
243. Sol-Proxima grav drift is ~1.5 s over the crossing
244. warp-carried mouth shows ZERO desynchronization after 10 yr
245. rocket-carried mouth shows LARGE desynchronization after 10 yr
246. single wormhole offset bounded by elapsed time
247. nested wormhole: outer + inner = 100 yr (additive)
248. Tipler at chronology horizon: offset = L/c
249. Tipler below horizon: offset << 1 yr
250. Gott pair (GUT, 1 ly): offset ~ 400-500 yr
251. Kerr 1 orbit: bounded by spin period (~0.3 ms)
252. Kerr multiple orbits: additive
253. max displacement is chain of wormholes
254. max displacement > single wormhole
255. portal_cycle = D/(beta c) + overhead
256. portal_cycle includes turnaround overhead
257. multijump breakeven = Delta / rate_diff
258. breakeven is infinite with no desync
259. backward recurrence converges to t* = Delta/r
260. backward max displacement ~ elapsed - t*
261. multi-jump backward exceeds single-jump offset
262. cumulative displacement = final - elapsed
263. below breakeven a 'backward' cycle drifts FORWARD
264. forward recurrence matches t(1+r) + Delta analytically
265. forward 10-cycle displacement is far beyond elapsed
266. energy per cycle = cruise_load(beta) * Delta
267. fuel burnt sums per-cycle fusion_fuel
268. ISM scoop flux = magsail area * n * m_p * v
269. D-3He yield is a small fraction of raw gas (isotope-lean)
270. scoop stops when the ship is parked
271. sustainability flag matches scooped >= burnt
272. net fuel = burnt - scooped
273. scoop yield loses to burn at beta=0.1 (below parity)
274. scoop yield loses to burn at every beta (parity window closed)
275. at the emergent cruise beta the scoop no longer keeps up
276. starved stock reports the cycle the tank runs dry
277. cruise is net-negative so stock does report a dry cycle
278. plan breakeven includes the same throat traversal as its cycles
279. plan returns one row per cycle, all finite
280. energy integral survives zero wall (razor limit)
281. energy integral survives degenerate sample counts
282. wall tidal diverges on a zero wall
283. wall tidal is zero at beta=0 even on a zero wall
284. throat density diverges at b0=0
285. exotic bill closes at b0=0 (volume vanishes faster)
286. exotic bill never inverts sign on a negative throat
287. tidal shear diverges at b0=0
288. proper throat length is zero at b0=0
289. portal at b0=0 returns a verdict dict, not a crash
290. negative mouth separation clamps to zero
291. negative separation gives zero CTC onset, not negative
292. unknown jump direction fails loudly
293. rate_diff above the physical domain clamps to 1
294. negative elapsed clamps to zero
295. superluminal |beta| is EXOTIC in both directions
296. horizon locks above |beta|=1 in both directions
297. no static observer above |beta|=1 in either direction
298. kinetic bill is infinite for |beta|>=1 both signs
299. cruise load is symmetric in |beta| (no negative-load leak)
300. negative throat fails flare-out instead of passing it
301. embedding surface vanishes for a nonpositive throat
302. negative hop overhead clamps to zero
303. negative throat radius yields zero traversal time
304. negative wormhole count yields zero offset
305. negative trip distance yields zero rocket proper time
306. negative-mass payload cannot be boosted
307. nonpositive bubble radius yields zero wall energy
308. negative body size yields zero tidal shear and zero min throat
309. voyage boost lock equals boost_profile ceiling
310. negative energy cannot mint negative fuel
311. cycle time includes traversal when a throat is given
312. superluminal rocket has no finite proper time
313. negative or nan boost target is rejected
314. negative or nan frame step cannot rewind the ledger
315. nan beam range propagates, never laundered to full power
316. nan throat radius yields the no-throat verdict, not a crash
317. nan propagates through every magnitude-clamped helper
318. nan multijump input yields the nan-flagged plan, not a doctored one
319. infinite speed never brakes (no laundered finite answer)
320. report_voyage refuses a non-finite beta without hanging
321. report_voyage coerces hostile beta types at the boundary
322. QI bound vanishes at huge tau instead of overflowing
323. negative hop count yields an empty plan
324. throat tidal profile reduces to mt_tidal_g at r = b0
325. radiator: nan propagates, negative waste needs no area
326. every mass-budget line is rated in the buildability ledger
327. buildability statuses stay inside the declared scale
328. every ledger row carries a non-empty needs description
329. wall thickness is a magnitude: f(-delta) == f(+delta)
330. orders_of_magnitude handles inf without a domain crash
331. durations/counts/rates clamp: chain and Kerr cannot invert
332. out-of-range time-warp index cannot wrap or crash
333. huge time-warp index clamps to the top rung
334. degenerate mesh inputs yield empty meshes, not crashes
335. non-finite dims yield empty meshes, never nan vertices
336. empty meshes normalise to (0,3) and stay renderable
337. hostile mesh inputs degrade to empty finite meshes
338. formatters coerce non-numeric input to nan, never crash
339. numpy scalars are real numbers to _Dims and _finite
340. hostile part explode and color mix degrade safely
341. renderer pop array grows for late-added parts
342. negative/nan dt leaves animation state untouched
343. out-of-range face indices are dropped at mesh build
344. out-of-range hover index resolves to no part
345. non-Part entries and hostile order/assembly state degrade
346. bar and render degrade on hostile surf/rect/frac
347. project degrades hostile inputs, nan verts propagate
348. colour and position sanitizers hold their contract
349. nan energy maps to the empty end of a log bar
350. _finite gate accepts reals, rejects nan/inf/non-numeric
351. hostile core/world objects and attrs degrade, never crash
352. non-numeric voyage state and dt degrade to nan, never crash
353. poisoned voyage state is sanitized at the integrator
354. nan radiator/coil state recovers, ledger stays finite
355. corrupted ledger fails the honesty audit, never crashes it
356. wrap_text accepts non-string input without crashing
357. a nan check condition counts as FAIL, never PASS
358. corrupted DIMS yields empty/degenerate output, never crashes
359. poisoned core props/coils degrade, never claim exotic
360. dead plant config yields inf/nan honestly, never crashes
361. radiator physics reads DIMS live (no stale cached area)
362. a dead-beam config terminates report_voyage, never spins 2M
363. numeric helpers coerce hostile args to nan, never TypeError
364. proper time on unknown state is unbounded, never a crash
365. None sentinel on a defaulted param still means 'use default'
366. ctc_exists never clears an unknown offset
367. honesty_audit survives wrong-typed objects, fails closed
368. a hostile traversal record prints, never crashes
369. a deleted DIMS key reads nan, never KeyError
370. counts and mesh resolutions are bounded against config bombs
371. main() survives hostile argv without a raw exception
372. crossing_time_s never divides by a dead beta
373. a nan-poisoned beam terminates report_voyage too
374. zero mix fraction bounds that isotope, never divides
375. both mix fractions dead -> degenerate nan, not a crash
376. non-numeric config reads as nan, never crashes or fabricates
377. ship mass reads DIMS live (no import-time cache)
378. multijump_plan bounds cycles: nan->empty, huge->1e6 cap
379. world_verts(nan angle) stays finite
380. ledger needs stats derive live (tape km, plates, sail km)
381. every mass-budget line carries an operations row
382. every operations row declares power, duty and failure
383. selftest leaves DIMS uncorrupted (no stale restores)
384. 'gamma(%.2f) = 1/sqrt(1-beta^2)' % beta_test
385. 'audit: %s' % name
386. 'shape_f(R) = 0.5 at delta = %.0e' % delta_ext
387. 'gamma(%.6f) is finite and positive' % beta_test
388. "portal traversal handles payload='%s'" % payload_type
389. 'chain of %d wormholes: offset = %d x single' % (N, N)

## Hover spec cards (every part, verbatim)

The engineering prose the viewer shows when you hover a part in SHIP or PORTAL view -- every card, every line, live from `build_ship_parts()` / `build_portal_parts()`.

### SHIP -- CREW HULL (flat spacetime)

125 m x 32 m pressure hull, 12 decks, crew 24
Interior metric is EXACTLY Minkowski: f = 1, every derivative zero.
Crew are weightless and un-accelerated at any beta -- there is no
  proper acceleration anywhere inside the bubble, so no g-loading
  and no structural limit on how hard the ship 'accelerates'.
Ship clocks run at the SAME rate as Earth clocks (no time dilation).
shell mass 1.311e+04 t   decks 3.121e+04 t

### SHIP -- D-3He FUSION REACTOR

21 m torus, 103 GW thermal, 62% direct conversion -> 63.7 GW electric
Aneutronic: D + 3He -> 4He + p + 18.35 MeV. Charged products only,
  so the energy is collected electrostatically instead of by a
  steam cycle -- that is where the 62%% conversion comes from.
This plant does NOT move the ship. It runs the coils, the cryo and
  the hotel load. Moving the ship is the beam's job (see RECTENNA).
HONEST GEOMETRY NOTE: the billed 3.6 m wall build is thicker than
  the 3.18 m tube radius it wraps -- the mass bill treats the torus
  as a solid blanket+shield body, an overestimate kept deliberately.
Fuel for a 4.25 ly crossing at cruise: 20146 kg of D-3He mix.
mass 2.496e+04 t

### SHIP -- ANTIMATTER PENNING TRAPS

8 traps x 5.25 kg antihydrogen = 7.55 EJ total
Reserved for field transients the SMES cannot swallow.
HONEST SCALE CHECK: accelerating this ship to beta = 0.5 costs 15 YJ.
  The entire antimatter inventory covers 5.02e-07 of that bill.
  Antimatter is not a warp fuel. Nothing storable is.
mass 1.213e+04 t

### SHIP -- SMES FIELD BUFFER

40 m toroid at 60 T -> u = B^2/2mu0 = 1.43e+09 J/m^3
Capacity 2.76 TJ -- COMPUTED from the field and the volume, not assumed.
It buffers coil ripple during shell reshaping. It is 13 orders of
  magnitude too small to change the ship's velocity, and this model
  never lets it try. There is no 'warp battery' aboard.
mass 1.192e+04 t

### SHIP -- CRYOPLANT (16 units)

Holds 96 REBCO coils at 18 K against 38.3 GW of AC loss.
Draws 2.49 GW electrical. Carnot floor at 18 K from a 1550 K sink is
  brutal: every watt lifted out of the cold mass costs ~86 W in.
mass 7357 t

### SHIP -- STRUCTURAL PYLONS (12)

154.1 m span, hull r=15.6 m to ring r=169.7 m.
They carry NO thrust load -- there is no thrust. Their job is to hold
  the ring concentric with the hull to within the shell servo's
  tolerance, because an off-centre ring makes an asymmetric bubble.
mass 1.409e+05 t

### SHIP -- MAIN WARP RING (96 sectors)

367 m diameter x 27.5 m tube, 1.08 m shell wall, rho = 4100 kg/m^3.
THIS IS THE DRIVE. In the Bobrick-Martire formulation the warp is not
  made by a field the ring emits -- it IS the ring: a massive shell
  carrying a shift-vector distribution. The metric is sourced by the
  shell's own stress-energy, which is ordinary positive-energy matter.
96 sectors are driven independently so the shape servo can correct
  asymmetry at 10 kHz; a wall that loses shape collapses the bubble.
mass 4.412e+05 t -- 41% of the whole ship.

### SHIP -- HTS FIELD COILS (96)

4096 turns x 38 kA = 1.56e+08 A-turns per coil, REBCO tape at 18 K.
They do not push on anything. They hold the shell's stress-energy
  distribution in the shape the metric solution requires -- the field
  phase sweeps the ring at the bubble frequency (watch them light in
  sequence: that travelling pattern IS the shift vector being steered).
AC + ripple loss 38.3 GW at beta = 1, scaling as beta^2.
mass 2.465e+05 t

### SHIP -- CASIMIR NEGATIVE-ENERGY LATTICE (96)

61333333 plates per cassette at a 10 nm gap; rho = -pi^2 hbar c / 720 a^4
  = -4.33e+04 J/m^3 over 0.74 m^3 of gap volume -> -32.2 kJ per cassette.
WHOLE-SHIP TOTAL: -3.09 MJ. This is real, measured physics (Casimir 1948;
  Lamoreaux 1997) and the largest negative-energy store ever designed.
A superluminal bubble at beta = 1 with a generous 1 m wall needs -1.131e+47 J.
  The lattice is short by 41 ORDERS OF MAGNITUDE. With the wall the
  quantum inequality actually permits (1.6e-33 m), short by 73 orders.
THIS PART IS THE HONEST ANSWER TO 'WHY NOT FASTER THAN LIGHT'.
mass 983.2 t

### SHIP -- FORE SHAPING RING

176 m diameter at z = +70 m.
The fore/aft pair breaks the shell's front-back symmetry. Without
  that asymmetry theta integrates to zero and the bubble sits
  still: space contracts ahead (theta < 0) and expands behind (theta > 0)
  only because these two rings are driven differently.
Together 5.489e+04 t.

### SHIP -- AFT SHAPING RING

176 m diameter at z = -70 m.
The fore/aft pair breaks the shell's front-back symmetry. Without
  that asymmetry theta integrates to zero and the bubble sits
  still: space contracts ahead (theta < 0) and expands behind (theta > 0)
  only because these two rings are driven differently.
Together 5.489e+04 t.

### SHIP -- WASTE-HEAT RADIATORS (60)

60 panels x 90 m x 31 m, both faces = 339910 m^2 radiating area.
SIZED, NOT GUESSED: T = (P / eps sigma A)^(1/4). At beta = 0.5 the
  ship rejects 26.4 GW and the panels settle at 1105 K.
Graphite sublimation caps them at 1900 K, which is the FIRST hard
  wall the superluminal mode hits -- before the energy problem, the
  coil load simply cooks the ship. Watch it in FLIGHT above beta = 1.
mass 7.75e+04 t

### SHIP -- NAVIGATION DEFLECTOR

33 m parabolic dish, subwarp only.
Useless at warp: the bubble wall already collects everything ahead of
  it. Which is the problem -- see the ISM load readout in FLIGHT.
mass 1061 t

### SHIP -- BOOST RECTENNA

Stowed 84 m; unfurls to a 4.0 km film at 1 um thickness.
It has to be kilometres wide: the tap's 1000 km transmitter at 1 um
  spreads to a 2.3 km spot by 0.10 ly (2.44 lambda L / D).
THE SHIP CANNOT LAUNCH ITSELF. Reaching beta = 0.5 costs 15 YJ,
  delivered over 30.0 d of boost out to 0.0315 ly.
Beam range 0.62 ly caps the cruise speed at beta = 0.855 -- an
  EMERGENT limit: no line in DIMS sets a maximum speed.
mass 17.59 t (deployed film)

### SHIP -- RCS / ION PODS (32)

Docking and attitude only, bubble down. Conventional reaction drive.
Attitude inside a warp bubble is meaningless -- the interior is
  inertial -- so these exist purely for the sublight endgame.
mass 4715 t

### SHIP -- MAGNETIC SAIL (drawn 1:4000)

TRUE radius 2800 km -- 7081x the ship. Drawn here at 1:4000; the viewer
  never shrinks a part silently, so the scale factor is in its name.
Zubrin and Andrews (1991): F = Cd rho_ISM v^2 A. At beta = 0.5 that
  is 7.87e+07 N against 1.081e+06 t of ship -- 7.28e-02 m/s^2.
Braking from beta = 0.5 therefore takes 3.26e+04 yr.
That is not a flaw in the sail. It is the honest answer to 'how do
  you stop', and every interstellar design has to answer it.
mass 1.28e+04 t

### SHIP -- WARP BUBBLE (spacetime)

R = 183 m, wall delta = 0.2 m, flat interior out to 182.2 m.
Not hardware -- this is the SHAPE OF SPACETIME the shell sources.
Inside: f = 1, exactly flat, weightless, no time dilation.
In the wall: tidal shear reaches 8.80e+16 g across a 2 m body at
  beta = 0.5. Nothing survives contact with the wall, at any speed.
Outside: unperturbed Minkowski. The universe does not notice.

### PORTAL -- GATE A  (mouth, Sol side)

24 m aperture -- b0 = 12.0 m throat radius.
The ring is the only part of a portal you could actually build. It
  holds the field geometry; it does NOT make the throat. Making the
  throat is the other -2.421e+44 J on this list.
Traversal at walking pace: 4.8 s.
TIDAL SHEAR AT THIS THROAT: 1.27e+14 g across a 2 m body.
  Nothing made of atoms crosses that. See GATE B for the throat you
  would actually survive.

### PORTAL -- THROAT FIELD COILS (16)

They shape the aperture field. They cannot violate the null energy
  condition, because no arrangement of ordinary current can.
Every traversable-wormhole solution needs NEC violation AT the throat
  (Morris & Thorne 1988) -- the same wall the superluminal warp mode
  hits, reached from a completely different direction.

### PORTAL -- THROAT CASIMIR CASSETTES (8)

Real negative energy, in the only place it is ever found.
Required at this throat: -2.421e+44 J.
Supplied by the whole ship's lattice: -3.09 MJ.
SHORT BY 38 ORDERS OF MAGNITUDE -- and by 45 orders for a throat
  wide enough to survive crossing.
The closest thing to a real construction is Maldacena, Milekhin &
  Popov (2020): Casimir energy of massless fermions threading a pair
  of magnetically charged black holes. It works on paper. It needs
  objects nobody has ever observed, and traversal takes years.

### PORTAL -- THE THROAT  (embedding diagram)

ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2   (Morris-Thorne 1988)
Drawn from z = 2 b0 sqrt(rho/b0 - 1) -- the real embedding, not a
  decorative funnel. No horizon, no singularity: genuinely two-way.
Energy density demanded at the throat: -3.344e+40 J per cubic metre.
The FLARE-OUT condition is what costs: for the throat to open out on
  both sides instead of pinching shut, the stress-energy there must
  violate the null energy condition. That is the entire problem, and
  it is structural -- not an artefact of this particular solution.

### PORTAL -- GATE B  (mouth, far side)

Wherever you put it -- 4.2465 ly away, in this configuration.
SURVIVABLE THROAT: tidal shear goes as c^2 L / b0^2, so a person
  crossing at 1 g of stress needs b0 >= 1.35e+08 m -- about 11 Earth
  diameters. Morris & Thorne reached the same conclusion in 1988.
That throat's exotic bill: -2.730e+51 J (-1.53e+04 Msun).
AND THEN IT IS A TIME MACHINE. Two mouths at different clock rates
  desynchronise; when the offset exceeds the light-travel time
  between them, closed timelike curves exist (Morris, Thorne &
  Yurtsever 1988). Park one mouth by a neutron star and this pair
  becomes one in 18.84 yr.

## Appendix -- the complete in-app information panel (verbatim)

Everything the viewer shows when you press **I** -- all 39 sections, including the ten math-proof sections (each proof states the formula, the live value, and the self-test check that verifies it).

### WD-1 FOLDRUNNER  --  CONCEPT OVERVIEW

```
A 1.081e+06 t starship that moves by carrying a region of flat spacetime
rather than by pushing against anything. A 367 m ring of ordinary,
positive-energy matter sources a shift-vector field; inside the
resulting 183 m bubble the metric is exactly Minkowski, so the crew
are weightless, un-accelerated and un-dilated for the whole voyage.

It is subluminal by design, and that is not a compromise -- it is
the entire reason it is buildable. The superluminal mode is present,
computed honestly, and flagged UNFUNDED every frame it runs.

Sol -> Proxima Centauri b (4.2465 ly) at beta = 0.855: about 4.97 yr ship
time, and the same on Earth's calendar. Nobody comes home to a
century they do not recognise.
```

### 1. THE METRIC  (what a warp drive actually is)

```
ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2

Alcubierre's method is inverse: choose the spacetime you want, then
read off the stress-energy the Einstein field equations demand for
it. That always produces an answer. The only question -- the ONLY
one -- is whether the matter it demands can exist.

f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R))
  f = 1 inside (flat, carried along)   f = 0 outside (untouched)
  sigma = 1/delta sets the wall thickness; currently delta = 0.2 m.

Everything expensive lives in df/dr. Curvature scales with the
SHARPNESS of the wall, not the size of the bubble -- which is why
thin-wall solutions are unaffordable and thick-wall ones are not.
```

### 2. YORK EXPANSION  (space being made and unmade)

```
theta = beta c (x / r_s) df/dr_s          [1/s]

Negative ahead of the ship -- space contracting -- and positive
behind it -- space expanding. The ship never moves through space at
all; the space it sits in is rebuilt around it. At beta = 1 with the
current wall, theta peaks at 7.493e+08 /s on each face.

This is what the METRIC view draws. The grid sheet is not an
artist's impression: each node is displaced by the value of theta
computed at that point by the same function the energy integral uses.
```

### 3. THE ENERGY BILL  (the whole argument, in numbers)

```
T^00 = -(c^4/8 pi G) (beta^2 rho^2 / 4 r_s^2) (df/dr_s)^2

Integrating over all space (the angular part is exact, the radial
part is Simpson-integrated in this file):
  E = -(c^4 beta^2 / 12 G) INT r^2 (df/dr)^2 dr

At R = 183 m and beta = 1:
   delta = 12 m     ->  -0.0528 Msun
   delta = 1 m      ->  -0.633 Msun
   delta = 1e-15 m  ->  -6.33e+14 Msun
   delta = 1.6e-33 m (quantum-inequality limit) -> -5.19e+09 x observable universe

Every one of those is NEGATIVE mass. That minus sign is not a
convention and it does not cancel. It is the reason this ship is
subluminal.
```

### 4. WHY SUBLUMINAL IS THE BUILDABLE ONE

```
Bobrick & Martire (Class. Quantum Grav. 38 105009, 2021) showed the
Alcubierre metric is one member of a large family, and that the
SUBLUMINAL members can be sourced by ordinary positive-energy matter
satisfying every pointwise energy condition. Fuchs et al. (Class.
Quantum Grav. 41 095013, 2024) then produced an explicit
constant-velocity solution of exactly that kind.

So a warp drive under beta = 1 needs no exotic matter at all. What
it needs is a massive shell with the right stress distribution --
and then the honest, unavoidable kinetic energy to change speed:
   beta = 0.1  ->  490 ZJ
   beta = 0.5  ->  15 YJ
   beta = 0.9  ->  126 YJ

Holding a speed, by contrast, is free: a constant-velocity warp
solution is a STATIONARY spacetime. Nothing flows, nothing is spent.
The coils only draw power because real hardware has losses.
```

### 5. WHY SUPERLUMINAL IS NOT

```
Santiago, Schuster & Visser, 'Generic warp drives violate the null
energy condition' (Class. Quantum Grav. 39 075006, 2022): ANY warp
drive that outruns light violates the NEC somewhere. Not Alcubierre's
in particular -- the whole class. It is a theorem, not a gap.

And the quantity required is not close. The Casimir effect is the
only laboratory-verified source of negative energy density there is
(Casimir 1948; Lamoreaux 1997; Mohideen & Roy 1998):
   rho = -pi^2 hbar c / 720 a^4  =  -4.334e+04 J/m^3 at a 10 nm gap
   whole-ship lattice, 96 cassettes, 6.13e+07 plates each  ->  -3.09 MJ

Requirement at beta = 1 with a generous 1 m wall: -1.131e+47 J.
SHORT BY 41 ORDERS OF MAGNITUDE.
At the wall thickness Ford-Roman actually permits: 73 orders.

This ship still flies that mode, on request, with the debt printed
in violet. It is the most useful thing a twin can do with a claim
it cannot support.
```

### 6. THE SHELL  (the drive itself)

```
367 m ring x 27.5 m tube, 1.08 m shell wall, 4100 kg/m^3.
Mass 4.412e+05 t -- 41% of the entire ship.

The ring is not a field emitter. IT IS THE SOURCE TERM. In the
Bobrick-Martire formulation the warp is the shell's own
stress-energy, so the drive's mass and the drive's field are the
same object seen two ways.

96 sectors are driven independently. The shape servo runs at 10 kHz
because an asymmetric shell makes an asymmetric bubble, and an
asymmetric bubble collapses. Watch the coils light in sequence in
SHIP view -- that travelling pattern is the shift vector being aimed.

THE OPEN PROBLEM: the solution needs anisotropic stresses comparable
to the energy density, meaning a sound speed near c. No known
material does that. It is a materials problem, not a physics one --
which is exactly why it is the interesting one.
```

### 7. POWER  (fusion runs the ship, not the trip)

```
D + 3He -> 4He + p + 18.35 MeV. Aneutronic, so the charged products
are collected electrostatically at 62% instead of through a steam
cycle: 103 GW thermal -> 63.7 GW electrical.

Cruise load (coil AC as beta^2, servo, cryo, hotel):
   beta = 0.0   4 GW
   beta = 0.5   16.4 GW
   beta = 0.99  47.1 GW
   beta = 2.0   163 GW  -- OVER PLANT CAPACITY

Fuel for the whole crossing at cruise: 26420 kg of D-3He mix. The
reactor never moves the ship. It keeps the coils cold and the lights
on. Moving the ship is somebody else's power bill -- see 9.
```

### 8. HEAT  (the wall nobody expects)

```
A closed ship exports no work, so every watt drawn becomes heat.
60 panels x 90 m x 31 m, both faces = 339910 m^2.

T = (P / eps sigma A)^(1/4) -- an outcome, never a setting:
   beta = 0.5   26.4 GW rejected  ->  1105 K
   beta = 0.99  75.9 GW rejected  ->  1439 K
   beta = 2.0   262 GW rejected  ->  1961 K  PAST THE 1900 K LIMIT

The superluminal mode cooks the ship before the energy problem even
gets a vote. Of all the reasons beta > 1 fails, this is the dullest
and the first.
```

### 9. GETTING UP TO SPEED  (the ship cannot launch itself)

```
Reaching beta = 0.855 costs 90 YJ.
The SMES holds 2.76 TJ. The antimatter inventory holds 7.55 EJ.
Both are far short of that bill, by twelve and eight orders of
magnitude. Nothing storable closes it. That is not a design flaw --
it is true of every interstellar concept ever costed.

So the energy is BEAMED, from a 6e+18 W stellar tap through a 1000 km
transmitter. Diffraction sets the rest: d_spot = 2.44 lambda L / D,
so the rectenna must unfurl to 4.0 km, and past 0.62 ly the spot
outgrows it no matter how much power you send.

MAXIMUM CRUISE SPEED IS THEREFORE beta = 0.8547 -- and it is
EMERGENT. Nothing in the spec names a speed limit. It falls out of
aperture, wavelength, tap power and ship mass. Build a bigger
transmitter and the ship goes faster without changing a bolt.
```

### 10. STOPPING  (the part every warp story skips)

```
Deceleration is not the reverse of acceleration: there is no
transmitter behind you and the energy has to GO somewhere.

MAGSAIL (Zubrin & Andrews 1991): a 2800 km superconducting loop
drags on the interstellar medium, F = Cd rho v^2 A = 7.87e+07 N at
beta = 0.5. It halves your speed in 65.28 yr -- which sounds fine until
you notice drag falls as v^2, so stopping takes 3.26e+04 yr.
Quoting the halving time and calling it 'braking time' is the
commonest way interstellar studies flatter themselves.

DESTINATION ARRAY: photon pressure F = 2P/c from a transmitter
already built at the far end -- 4.27e+10 N, stopping in 50.7 d.

So interstellar RENDEZVOUS needs infrastructure at both ends, and
a FLYBY does not. FLIGHT mode makes you choose (key J) and prints
which one you chose on every frame.
```

### 11. THE WALL  (a place, and not a survivable one)

```
Inside: f = 1, every derivative zero, exactly flat. Zero g at any
beta, no structural limit, no time dilation. This is the good part,
and it is genuinely remarkable. It reaches to r = 182.2 m today.

In the wall: tidal shear across a 2 m body at beta = 0.5,
   delta = 12 m   ->  2.45e+13 g
   delta = 1 m    ->  3.52e+15 g
   delta = 1 mm   ->  3.52e+21 g

Note the direction of that trade. A thicker wall is gentler AND
cheaper -- the one place in this design where safety and cost pull
the same way. It is why every serious modern warp paper thickens
the wall and why Alcubierre's original thin shell was the worst
possible choice on both counts.
```

### 12. THE INTERSTELLAR MEDIUM  (what the bubble collects)

```
McMonigal, Lewis & O'Byrne, Phys. Rev. D 85 064024 (2012), 'The
Alcubierre warp drive: on the matter of matter'. Particles ahead of
the ship do not pass through the bubble. The wall collects them,
and they are released forward when it drops.

Over a 4.25 ly crossing at 100000 protons/m^3 the ship sweeps up
4.25e+26 protons through its 183 m frontal area.
Released at beta = 0.5 that is 7.98 PJ -- about 1907 kilotons, aimed
precisely where you are going.

The model uses a deliberately conservative beta^2/2 scaling for the
per-particle energy. The real spectrum is set by the wall's
blueshift and is worse. Drop the bubble off-axis.
```

### 13. CLOCKS  (what a warp drive does not buy you)

```
The interior is flat and unaccelerated, so ship time equals
coordinate time. Over the crossing at beta = 0.855:
   warp ship crew age   4.97 yr
   Earth ages           4.97 yr  (identical)
   a relativistic ROCKET crew at the same speed would age 2.58 yr

The rocket crew age LESS. A warp drive gives up the time-dilation
dividend entirely. What it buys instead: no reaction mass, no
g-loading, and a crew who come home to the world they left.
For a civilisation rather than a one-way probe, that is the better
trade -- but it is a trade, and this panel will not pretend it is not.
```

### 14. HORIZONS  (why the helm locks above beta = 1)

```
For beta > 1 the front of the bubble outruns any signal sent from
inside it. The crew are causally disconnected from their own
forward wall (Everett 1996; Coule 1998; Krasnikov 1998).

Consequences, all of them real: you cannot steer, you cannot slow
down, and you cannot dissolve the bubble from within. The entire
trajectory must be laid before departure and flown blind.

FLIGHT mode enforces this. Above beta = 1 the helm goes red and
stops accepting commands -- not as a game mechanic, but because
the theorem says the command cannot arrive.
```

### 15. MASS BUDGET  (every kilogram from geometry x density)

```
No component mass is typed in. Each is a volume computed from DIMS
times a material density, so moving a dimension moves the ship's
mass, its kinetic bill, its radiator sizing and its voyage at once.

   warp ring shell                 4.412e+05 t
   HTS field coils                 2.465e+05 t
   pylons                          1.409e+05 t
   radiators                        7.75e+04 t
   shaping rings                   5.489e+04 t
   crew decks                      3.121e+04 t
   fusion reactor                  2.496e+04 t
   crew hull shell                 1.311e+04 t
   magsail loop                     1.28e+04 t
   antimatter traps                1.213e+04 t
   SMES buffer                     1.192e+04 t
   cryoplant                            7357 t
   RCS pods                             4715 t
   deflector                            1061 t
   Casimir lattice                     983.2 t
   consumables + crew                   76.8 t
   boost rectenna                      17.59 t

   TOTAL                           1.081e+06 t
```

### 15b. SHIP COMPONENTS  (every part, fully explained)

```
Every part on the ship, in mass-budget order. Each entry reads:
what it is -> where it sits and how big -> what one unit looks
like -> where it mounts -> role -> why it must exist -> per-unit
mass -> material -> what it stores or consumes -> how its mass
is derived -> spec -> buildability -> closest real hardware ->
what it draws -> which phases -> share of cruise load -> what it
actually carried over the mission -> failure mode -> cascade ->
thermal -> connections -> who depends on it -> verification ->
governing spec keys -> viewer label. Ratings: TODAY (exists,
only scale missing), NEAR (physics proven, engineering not),
FAR (needs an industry nobody has), OPEN (a material nobody
has made), IMPOSSIBLE (barred by theorem).

>> WARP RING SHELL        4.412e+05 t   40.8%  [OPEN   ]
   sits: ~394 x 394 m cross-section x 26.8 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 197.2 m -- 15.0 m PAST the 182.2 m flat
   interior: this part is wall-mounted by design, it lives in the gradient
   it shapes
   mesh: 21504 verts, 16896 facets of render weight
   what it is: a 366.9 m torus of SiC/W metamaterial in 96 sectors -- the
   stress-energy boundary the bubble is written onto
   unit: one sector is a 12.0 m arc segment of the 27.52 m ring tube -- 96
   wedge shells that close into the torus
   per unit: 4596 t each x 96 sector
   mounts: hangs on the 12 pylons at the ring plane -- the ring is the
   spine's payload, not the spine
   needed: the bubble needs a shaped stress-energy boundary -- the shell IS
   that boundary; no shell, no metric source
   material: SiC/W metamaterial at 4100 kg/m^3 (ring_density)
   mass from: torus shell: 4pi^2 R_m r_m x ring_wall_m x rho -- the shell
   area of the 366.9 m torus times its wall; the drawn sector joints ride
   under this continuous-shell bill
   spec: 96 sectors, torus 366.9 m major x 27.5 m minor dia, 1.08 m wall,
   SiC/W metamaterial at 4100 kg/m3 -- plus a stress-energy state no
   foundry can write
   role & build: The shell itself is ordinary composite engineering. What
   it must do is not: the positive-energy warp solutions need anisotropic
   stresses comparable to the energy density -- sound speed nearing c. No
   known material does this. A materials problem, not a relativity problem.
   nearest hardware: nothing -- metamaterial cloaks exist, but none carry
   relativistic stress-energy
   runs: 4944.8 MW servo control share -- continuous while the shell is
   shaped
   active: shaped phases only -- BOOST through CRUISE; dead hardware in
   DOCK and freefall
   share of cruise: 10.5% of the 47.1 GW beta=0.99 cruise load
   mission: held the shape that carried 1.5e+25 J peak kinetic over the
   voyage -- the shell's servo share ran the whole cruise
   fails: sector servo loss -> shape error -> integrity drains toward
   collapse; the ship falls out of warp, it does not explode
   cascade: sector loss -> shape error -> integrity drains -> collapse to
   subluminal -- survivable, mission over
   thermal: sits at the bubble wall; servo and coil losses around it leave
   only through the radiators -- no conduction path off the ship exists
   connects: pylons carry it; the 96 coils wrap it; the 96 Casimir
   cassettes sit in its wall -- it is the assembly everything hangs off
   required by: the coils wrap it and the bubble is written on it -- warp
   mode is impossible without it
   proven: mass recomputed in _scale_audit; 'ring straddles the wall'
   selftest; exact mass match vs mass_budget
   keys: ring_major_d_m=366.88, ring_minor_d_m=27.52, ring_wall_m=1.08,
   ring_sectors=96, ring_density=4100
   on screen: labelled 'MAIN WARP RING (96 sectors)' -- assembly step 7 of
   17; slides 78 m forward when exploded

>> SHAPING RINGS          5.489e+04 t    5.1%  [OPEN   ]
   sits: two rings, each ~188 m diameter x 12.8 m axial, straddling the
   ring plane fore and aft
   envelope: farthest point 118.7 m of the 182.2 m flat interior (63.6 m of
   margin)
   what it is: two smaller torus rings fore and aft of the main ring --
   they break the shift field's front-back symmetry so the bubble has a
   direction
   unit: each ring is a 12.84 m tube bent into a 176.1 m circle
   per unit: 2.745e+04 t each x 2 rings
   mounts: field-suspended fore and aft of the ring plane at cap_offset_m =
   69.72 m -- the aft ring is hard-mounted anyway, doubling as the radiator
   spine
   needed: a symmetric bubble has no direction -- the fore/aft rings make
   the field lean forward
   material: same metamaterial as the ring at 4100 kg/m^3 (ring_density)
   mass from: two torus shells: 2 x 4pi^2 R_c r_c x capring_wall_frac x rho
   spec: 2 rings, 176.1 m major x 12.8 m minor dia, 69.72 m offset, 30%
   solid fraction, same metamaterial, same unsolved sourcing
   role & build: Same wall, same verdict: drivable geometry is buildable,
   the stress-energy it has to carry is not.
   nearest hardware: nothing -- no machine on Earth shapes a metric
   runs: 2119.2 MW servo control share -- continuous while the shell is
   shaped
   active: same as the main shell -- only live while the bubble is up
   share of cruise: 4.5% of the 47.1 GW beta=0.99 cruise load
   mission: kept the front-back asymmetry for 9.00 yr of shaped cruise
   fails: same as the main shell: shape error, integrity drain, collapse
   cascade: lost asymmetry -> degraded fold -> the bubble still holds but
   stops being directional
   thermal: same regime as the main shell -- shaped hardware whose losses
   must all radiate
   connects: mounted on the pylon frame fore and aft of the main ring --
   they trim its field, nothing else
   required by: the bubble's directionality needs them -- without the
   asymmetry the metric is symmetric and goes nowhere
   proven: mass recomputed in _scale_audit; envelope check (reach 117.4 m)
   keys: capring_d_m=176.08, capring_minor_d_m=12.84, cap_offset_m=69.72,
   capring_wall_frac=0.3
   on screen: labelled 'FORE/AFT SHAPING RING' -- assembly steps 10 & 11 of
   17

>> HTS FIELD COILS        2.465e+05 t   22.8%  [NEAR   ]
   sits: ~395 x 395 m cross-section x 28.4 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 197.7 m -- 15.5 m PAST the 182.2 m flat
   interior: this part is wall-mounted by design, it lives in the gradient
   it shapes
   mesh: 20160 verts, 20160 facets of render weight
   what it is: REBCO high-temperature-superconductor windings, one per ring
   sector -- they do not push on anything; they hold the shell's
   stress-energy in the shape the metric requires
   unit: each coil is a 27.92 m bore x 0.30 m winding build x 17.24 m long
   annular pack around one tube sector
   per unit: 2568 t each x 96 coil
   mounts: wrapped around the ring tube with 0.20 m standoff -- they float
   on the shell they drive
   needed: the shell is only a shape until the coils energise it -- no
   field, no metric source
   material: REBCO winding pack at 5600 kg/m^3 (coil_density)
   mass from: annular winding pack: coils x pi((r_i+coil_build_m)^2 -
   r_i^2) x coil_len_m x rho, where r_i = ring minor radius + standoff
   spec: 96 coils x 48000 turns, 27.92 m bore x 17.24 m pack, 38 kA at 18
   K, 0.30 m winding build at 5600 kg/m3 -- ~408526 km of REBCO tape total,
   quench protection per sector, 38252.8 MW of AC ripple loss to sink
   role & build: REBCO tape is demonstrated in SPARC-class machines. 96
   sectors held at 18 K on a 183 m radius is scaling work, not new physics.
   nearest hardware: SPARC's TF coils (MIT/CFS, 20 T REBCO, 2021) -- the
   same tape, orders more of it
   runs: 38252.8 MW AC ripple at beta=1 (scales beta^2) + 18 K hold --
   continuous in warp mode
   active: every shaped phase; idle load is the 18 K cryo hold even when
   not steering
   share of cruise: 81.2% of the 47.1 GW beta=0.99 cruise load
   mission: carried the shaped field for the full cruise leg -- ripple
   losses are inside the 7.16e+18 J radiated total
   fails: a quench dumps the field into the cryostat -- trip to subluminal
   cascade: quench -> field energy into the cryostat -> collapse; the SMES
   exists precisely to intercept this
   thermal: held at 18 K; AC ripple plus hold heat lifts through the
   cryoplant into the radiators -- a few degrees of margin separates field
   from quench
   connects: wrapped around the ring tube (bore clears it), fed DC through
   the SMES buffer, held at 18 K by the cryoplant
   required by: required by the shell shape, and therefore the bubble --
   and they are why the cryoplant and SMES exist
   proven: coil-bore derivation check in _scale_audit (bore clears the tube
   it energises); mass recompute
   keys: coils=96, coil_bore_m=27.92, coil_len_m=17.24, coil_turns=48000,
   coil_current_a=38000, coil_temp_k=18, coil_build_m=0.3,
   coil_standoff_m=0.2, coil_density=5600
   on screen: labelled 'HTS FIELD COILS (96)' -- assembly step 8 of 17;
   slides 116 m forward when exploded

>> CREW HULL SHELL        1.311e+04 t    1.2%  [TODAY  ]
   sits: ~32 x 32 m cross-section x 124.8 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 62.4 m of the 182.2 m flat interior (119.8 m of
   margin)
   mesh: 14658 verts, 13516 facets of render weight
   what it is: the pressure vessel -- 32 m diameter of alloy holding one
   atmosphere of flat-spacetime life support inside a curved wall
   unit: one pressure vessel 32 m dia x 124.8 m long -- a single welded
   shell, not an assembly
   mounts: the spine -- everything forward-mounted hangs off it; it is the
   mount, not the mounted
   needed: the crew need one atmosphere of flat spacetime -- without the
   shell there is no 'inside'
   material: hull alloy at 2700 kg/m^3 (hull_density)
   mass from: cylinder shell: circumference x len x hull_wall_m x rho (the
   wall comes from the hoop-stress formula, checked)
   spec: 124.8 m x 32 m pressure shell, 0.44 m wall, 2700 kg/m3 -- ordinary
   thick-laminate fabrication for 24 crew
   role & build: Thin-wall SiC pressure vessel, t = P*r/sigma.
   Aerospace-grade today; only the crew count is exotic.
   nearest hardware: ISS pressure modules and submarine hulls -- routine
   pressure-vessel work at this size
   runs: none (passive) -- always
   active: all five phases -- passive, always
   mission: carried 4.433e+04 t at beta 0.5 -- no duty cycle, no relief
   fails: a breach is a life-safety event, not a propulsion one
   cascade: breach -> pressure loss -> mission ends; nothing else matters
   after this
   thermal: ~300 K shirt-sleeve inside -- the 96 MW hotel load still has to
   leave through the radiators
   connects: hung off the ring by the pylons; houses decks, reactor, SMES,
   traps; carries the deflector on its nose and the RCS pods aft
   required by: required by the decks, reactor, SMES, traps and cryo --
   everything that lives in flat spacetime
   proven: hoop-stress wall check (hull_wall = 0.22 x d/16); envelope
   check; mass recompute
   keys: hull_len_m=124.76, hull_d_m=32, hull_decks=12, hull_wall_m=0.44,
   hull_shell_rfrac=0.88, hull_density=2700, deck_t_m=1.4,
   deck_inset_m=1.2, crew=24, crew_supplies_kg=3200, len_margin_m=20
   on screen: labelled 'CREW HULL (flat spacetime)' -- assembly step 1 of
   17; slides 46 m aft when exploded

>> CREW DECKS             3.121e+04 t    2.9%  [TODAY  ]
   sits: ~32 x 32 m cross-section x 124.8 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 62.4 m of the 182.2 m flat interior (119.8 m of
   margin)
   mesh: 14658 verts, 13516 facets of render weight
   what it is: 12 deck slabs inside the hull -- where 24 people live for 9
   years
   unit: each deck is a 1.4 m slab spanning the local hull section (barrel
   decks hold the full 32 m bore; the end decks taper with the loft) with
   drawn collar openings where a Penning bay passes through
   per unit: 2601 t each x 12 deck
   mounts: stacked inside the hull shell, inset 1.2 m from the pressure
   wall and landed on it by rim beams
   needed: 24 people need somewhere to stand for nine years
   material: hull alloy at 2700 kg/m^3 (hull_density)
   mass from: hull_decks slabs: N x pi(d/2)^2 x deck_t_m x hull_density;
   the drawn Penning collars cut where the bays pierce net out inside this
   solid-plug bill
   spec: 12 deck plates at 35% fill, same SiC laminate
   role & build: Bulkheads and floors. Nothing to invent.
   nearest hardware: ISS module fit-out -- routine
   runs: none (passive) -- always
   active: all five phases -- the crew never stops living there
   mission: 9.00 yr of life support under the 96 MW hotel load
   fails: none
   cascade: deck loss -> crew loss -> mission ends
   thermal: ~300 K; internal air loops carry deck heat to the hull
   exchangers
   connects: inside the hull shell -- structure only, no powered interface
   required by: required by the crew and the consumables -- the only parts
   that are the mission's purpose
   proven: mass recompute; deck count check vs spec
   on screen: labelled 'CREW HULL (flat spacetime)' -- assembly step 1 of
   17; slides 46 m aft when exploded

>> FUSION REACTOR         2.496e+04 t    2.3%  [FAR    ]
   sits: ~31 x 31 m cross-section x 6.4 m along the ship axis, at the ring
   plane
   envelope: farthest point 15.9 m of the 182.2 m flat interior (166.3 m of
   margin)
   mesh: 590 verts, 651 facets of render weight
   what it is: a D-3He toroidal fusion plant -- 102.7 GW thermal, 63.7 GW
   electric; the housekeeping engine
   unit: a 6.36 m tube bent into a 21.24 m torus -- burn chamber, blanket
   and divertor share that bore
   mounts: inside the hull at z = -2 m on 8 radial standoff posts to the
   inner wall -- buried where the loft is widest and the shielding is free
   needed: coils, cryo and hotel load demand ~63 GW continuous -- only
   fusion supplies it without beamed power
   material: reactor vessel at 5200 kg/m^3 (reactor_rho)
   stores: consumes 25.21 kg/day of D-3He at full plant output -- the
   supply chain this ship cannot carry
   mass from: torus shell: 4pi^2 R r x reactor_wall_m x rho
   spec: tokamak 21.2 m major x 6.4 m minor dia, 102.70 GWth -> 63.67 GWe
   at 62% direct conversion; fuel ~6.49 kg 3He/day at cruise; hotel load 96
   MW -- the fuel chain is the blocker, not the torus
   role & build: D-3He demands a lunar/regolith helium-3 industry that does
   not exist, and a plasma regime harder than D-T. The honest fallback: D-T
   at ITER class is NEAR, and one metre of water shielding around this
   reactor costs only ~1333 t -- absorbable. The aneutronic choice buys
   crew proximity, not feasibility.
   nearest hardware: SPARC/ITER-class tokamaks -- but D-3He plasma has
   never been burned anywhere
   runs: produces 63.67 GWe; burns 6.49 kg 3He/day; vents He-4 ash --
   continuous, every phase
   active: all five phases -- hotel power never stops
   mission: produced 4.44e+18 J electric; burnt 2.033e+04 kg of D-3He
   across the voyage
   fails: trip -> hotel load falls on the SMES buffer; blackout is
   survivable for hours, not days
   cascade: trip -> SMES bridges the hotel load for minutes -> blackout ->
   the cryo floor warms -> quench cascade
   thermal: the largest single heat source aboard -- every joule not
   converted to electricity lands on the radiators
   connects: feeds the bus through the SMES buffer; burns the 3He supply;
   dumps its waste heat to the radiators
   required by: required by every powered system -- coils via SMES,
   cryoplant, hotel load
   proven: plant_electric_w and the 1.35x margin check in _scale_audit;
   mass recompute
   keys: reactor_major_d_m=21.24, reactor_minor_d_m=6.36,
   reactor_wall_m=3.6, reactor_rho=5200, reactor_th_gw=102.7,
   reactor_direct_eff=0.62
   on screen: labelled 'D-3He FUSION REACTOR' -- assembly step 2 of 17;
   slides 40 m aft when exploded

>> SMES BUFFER            1.192e+04 t    1.1%  [NEAR   ]
   sits: ~45 x 45 m cross-section x 4.3 m along the ship axis, aft, station
   z=-40 m
   envelope: farthest point 47.3 m of the 182.2 m flat interior (135.0 m of
   margin)
   mesh: 844 verts, 892 facets of render weight
   what it is: superconducting magnetic energy storage -- a lossless
   'battery' holding energy in a magnetic field for transients, not in
   chemicals
   unit: a 4.40 m tube bent into a 40.36 m torus of conductor and coolant
   mounts: mounted aft on the spine at z = -40.36 m (smes_z0_m is a
   magnitude; the aft sign is convention), standing off the hull on 8
   radial posts
   needed: the coils demand steady DC against transients; the buffer keeps
   a sag from becoming a quench
   material: SMES torus windings at 6800 kg/m^3 (smes_rho)
   stores: stores 2.76 TJ of field energy -- the ship's only large energy
   reservoir
   mass from: torus shell: 4pi^2 R r x smes_wall_m x rho
   spec: 2.76 TJ at 60 T in a 40.4 m major x 4.4 m minor toroid -- the
   field is ~1.5x the best sustained magnet built today, so the rating sits
   at the NEAR edge
   role & build: Superconducting storage exists at small scale. A GJ-class
   toroid is engineering, not research.
   nearest hardware: grid SMES units (MW-class, e.g. the D-SMES line) --
   real hardware at one-millionth the stored energy
   runs: standby ~0; delivers 2.76 TJ on demand -- holds charge; discharges
   on transients
   active: all phases, armed -- earns its keep in BOOST transients and
   BRAKE regen
   mission: absorbed 9.48e+21 J of magsail regen on the brake leg -- its
   single biggest deposit
   fails: the bridge between reactor trip and restart -- without it a trip
   is a blackout
   cascade: loss -> coil transients unsupplied -> quench risk on every
   ripple -> eventual collapse
   thermal: cryogenic, same 18 K class plant as the coils -- lossless
   storage only exists cold
   connects: sits between reactor and coils -- absorbs transients so the
   field never sags
   required by: required by the coils (transient buffer) and the magsail
   (its regen dumps here)
   proven: smes_store_j = 2.76 TJ check; mass recompute
   keys: smes_major_d_m=40.36, smes_minor_d_m=4.4, smes_wall_m=1,
   smes_rho=6800, smes_b_t=60, smes_z0_m=40.36
   on screen: labelled 'SMES FIELD BUFFER' -- assembly step 4 of 17; slides
   64 m aft when exploded

>> ANTIMATTER TRAPS       1.213e+04 t    1.1%  [FAR    ]
   sits: ~29 x 9 m cross-section x 81.8 m along the ship axis, aft, station
   z=-9 m
   envelope: farthest point 48.9 m of the 182.2 m flat interior (133.3 m of
   margin)
   mesh: 1680 verts, 1472 facets of render weight
   what it is: Penning traps -- electromagnetic bottles confining positrons
   in vacuum, burned only for peak fold transitions
   unit: each trap is a 9.56 m spherical Penning bottle
   per unit: 1516 t each x 8 trap
   mounts: two-storey Penning bays between the decks at x=+/-9.7 m, z
   -43.1..+29.1 m -- each sphere pierces its adjacent slabs through drawn
   collar openings
   needed: the only source aboard for fold-transition peaks the reactor
   cannot spike
   material: trap vessel at 4400 kg/m^3 (amtrap_rho)
   stores: stores 5.248 kg of positrons per trap x 8 = 41.98 kg total ->
   7.55 EJ, 1.80 gigatonnes TNT if containment ever fails -- the most
   dangerous 42 kg in the build
   mass from: amtraps spherical shells: N x 4pi(d/2)^2 x amtrap_wall_m x
   rho
   spec: 8 traps x 5.25 kg antiprotons (41.98 kg total, 7.55 EJ on tap) in
   9.6 m Penning cells -- at current production rates, longer than the age
   of the universe
   role & build: World production is nanograms per year. Traps this size
   need a production industry nobody has priced, let alone built.
   nearest hardware: CERN's ALPHA/GBAR Penning traps -- they hold billions
   of positrons; this asks for macroscopic mass
   runs: confinement share of hotel load -- continuous containment, forever
   active: all phases -- containment is forever, discharge is rare
   mission: discharged 0 kg over the voyage -- most of the 42 kg store came
   home
   fails: confinement loss -> annihilation: 7.55 EJ released against the
   containment wall. This is the one line whose failure is catastrophic,
   not survivable
   cascade: containment loss -> 7.55 EJ against the wall -> the ship ends;
   the only non-survivable failure aboard
   thermal: cryogenic; confinement heat is small but it never stops --
   forever is a long duty cycle
   connects: discharge into the bus for peak fold transitions only -- never
   run continuously
   required by: required by peak fold transitions -- nothing else aboard
   can spike that power
   proven: mass recompute; per-unit mass in the component table
   keys: amtraps=8, amtrap_d_m=9.56, amtrap_wall_m=1.2, amtrap_rho=4400,
   amtrap_kg=5.248
   on screen: labelled 'ANTIMATTER PENNING TRAPS' -- assembly step 3 of 17;
   slides 56 m aft when exploded

>> CRYOPLANT                  7357 t    0.7%  [TODAY  ]
   sits: ~333 x 333 m cross-section x 20.2 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 169.7 m of the 182.2 m flat interior (12.6 m of
   margin)
   mesh: 800 verts, 1104 facets of render weight
   what it is: refrigerator units holding the HTS coils at 18 K -- if they
   sag, the coils quench and the field collapses
   unit: each unit is a 11.0 m dia x 20.16 m cylinder of compressors, cold
   boxes and dewars
   per unit: 459.8 t each x 16 unit
   mounts: mounted at cryo_mount_rfrac = 0.80 of the interior radius on
   radial struts to the tube's inner skin, staggered between the pylon
   lines
   needed: REBCO quenches well above 18 K -- lose the cold and the coils
   dump their field energy into the cryostat
   material: cryo unit at 240 kg/m^3 (cryo_rho)
   stores: consumes 2493 MW of plant power continuously to hold the
   cryogenic floor -- the second-largest load aboard
   mass from: cryo_units cylinders: N x pi(d/2)^2 x cryo_len_m x rho; the
   drawn mount struts ride under this bill
   spec: 16 units, 11.0 m x 20.2 m each, holding coils and traps at 18 K;
   2492.8 MW draw against a radiative leak -- off-the-shelf physics
   role & build: 18 K refrigeration is demonstrated technology, resized for
   cold area, not re-invented.
   nearest hardware: the ITER cryoplant (65 kW at 4.5 K, the largest ever
   built) -- this needs more lift, colder
   runs: 2492.8 MW -- continuous -- the coils and traps both ride on it
   active: all phases -- the cold floor never takes a phase off
   share of cruise: 5.3% of the 47.1 GW beta=0.99 cruise load
   mission: ran all 9.00 yr; its lifted heat is inside the 7.16e+18 J
   radiated
   fails: warm-up -> quench cascade -> field collapse; hours of margin
   cascade: warm-up -> quench cascade -> field collapse -> falls out of
   warp; hours of margin, not seconds
   thermal: the heat pump -- lifts coil and trap heat up to radiator
   temperature; its own rejection adds to the very load it serves
   connects: cools the field coils (and holds the traps cold); its waste
   heat goes to the radiators like everything else
   required by: required by the coils AND the traps -- two systems ride on
   it; it is a single point of failure by design
   proven: mass recompute; envelope check (reach 147.1 m)
   keys: cryo_units=16, cryo_d_m=11, cryo_len_m=20.16, cryo_rho=240,
   cryo_mount_rfrac=0.8
   on screen: labelled 'CRYOPLANT (16 units)' -- assembly step 5 of 17;
   slides 57 m aft when exploded

>> RADIATORS              7.75e+04 t    7.2%  [NEAR   ]
   sits: ~202 x 202 m cross-section x 90.4 m along the ship axis, aft,
   station z=-70 m (box spans the whole multi-unit arrangement)
   envelope: farthest point 152.8 m of the 182.2 m flat interior (29.4 m of
   margin)
   mesh: 960 verts, 720 facets of render weight
   what it is: graphite panels glowing at up to 1,550 K -- the only way
   heat leaves a sealed ship in vacuum
   unit: each panel is a 90.44 x 31.32 x 0.24 m graphite wing
   per unit: 1292 t each x 60 panel
   mounts: rooted at rad_z0_m = -24.36 m, inner radius rad_inner_r_m = 69.6
   m -- swept aft, clear of the bubble wall; the aft shaping ring pierces
   each fin at mid-span and doubles as the radiator spine (clamp doublers
   drawn)
   needed: in vacuum the only way out is radiated -- no panels, no
   continuous operation
   material: graphite radiator at 1900 kg/m^3 (rad_rho)
   mass from: radiators panels: N x len x w x rad_t_m x rho -- the only
   component whose area is also physics
   spec: 60 panels x 90.4 m x 31.3 m, both faces = 339910 m2 at 1550 K,
   epsilon 0.92, graphite limit 1900 K -- refractory panels exist at bench
   scale, not at acres
   role & build: 1550 K graphite rejection is refractory-panel /
   droplet-radiator territory: demonstrated below scale, never flown at
   this size.
   nearest hardware: ISS ammonia radiators -- graphite at peak temperature
   is beyond anything flown
   runs: none (passive radiation) -- continuous -- the only path heat
   leaves the ship
   active: all phases -- heat leaves in DOCK too
   mission: rejected 7.16e+18 J of heat over the voyage -- every joule the
   ship made or caught
   fails: overtemp past 1900 K -> panel loss -> thermal runaway; the
   graphite limit is the cruise's hard ceiling
   cascade: panel loss -> thermal ceiling drops -> every powered system
   derates -> cruise speed falls
   thermal: the terminus -- 1550 K working panels against a 1900 K limit;
   the only door heat leaves by
   connects: receive every waste joule on the ship -- coils, cryo, hotel,
   reactor losses all end here
   required by: required by every powered part -- nothing continuous works
   without a heat path
   proven: area = 339,910 m^2, T_eq at beta=0.99/2, and binding-part
   envelope checks in _scale_audit
   keys: radiators=60, rad_len_m=90.44, rad_w_m=31.32, rad_inner_r_m=69.56,
   rad_z0_m=-24.36, rad_temp_k=1550, rad_limit_k=1900, rad_emissivity=0.92,
   rad_t_m=0.24, rad_rho=1900
   on screen: labelled 'WASTE-HEAT RADIATORS (60)' -- assembly step 12 of
   17; slides 96 m aft when exploded

>> PYLONS                 1.409e+05 t   13.0%  [TODAY  ]
   sits: ~339 x 339 m cross-section x 4.8 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 169.7 m of the 182.2 m flat interior (12.5 m of
   margin)
   mesh: 96 verts, 72 facets of render weight
   what it is: 12 structural spars carrying the warp ring's load into the
   hull spine -- the ship's skeleton
   unit: each spar is a 154.1 m long box section, 5.88 x 4.80 m
   per unit: 1.174e+04 t each x 12 spar
   mounts: hull to ring -- they ARE the mounting path; 12 spars carry the
   ring's load into the spine
   needed: the ring must hang on the hull -- without the pylons the ship is
   two objects
   material: structural spar at 2700 kg/m^3 (pylon_rho)
   mass from: pylons spars: N x len x w x pylon_t_m x rho
   spec: 12 spars x 154.1 m, 5.88 m wide -- ordinary composite structure
   role & build: Structural spars. Nothing to invent.
   nearest hardware: ordinary aerospace spar -- fully buildable today
   runs: none (passive) -- always
   active: all phases -- loaded hardest under BOOST
   mission: carried peak load under the boost -- 1.5e+25 J of kinetic
   through 12 spars
   fails: structural failure under load -- the ship does not spin apart
   slowly
   cascade: spar failure -> ring load path breaks -> structural event under
   boost
   thermal: passive structure following ambient -- their job is force, not
   heat
   connects: the only structural path between the hull spine and the ring
   -- every load, vibration and torque crosses them
   required by: required by the ring and everything hung off it -- a pylon
   failure is a structural failure
   proven: mass recompute; count check vs spec
   keys: pylons=12, pylon_len_m=154.08, pylon_w_m=5.88, pylon_t_m=4.8,
   pylon_rho=2700
   on screen: labelled 'STRUCTURAL PYLONS (12)' -- assembly step 6 of 17;
   slides 54 m forward when exploded

>> CASIMIR LATTICE           983.2 t    0.1%  [FAR    ]
   sits: ~392 x 392 m cross-section x 1.1 m along the ship axis, at the
   ring plane (box spans the whole multi-unit arrangement)
   envelope: farthest point 196.1 m -- 13.8 m PAST the 182.2 m flat
   interior: this part is wall-mounted by design, it lives in the gradient
   it shapes
   mesh: 768 verts, 576 facets of render weight
   what it is: 96 cassettes of parallel plates 10 nm apart -- negative
   energy density by geometry, the only exotic hardware aboard
   unit: each cassette is a 1.10 m square plate stack 3.68 m tall
   per unit: 10.24 t each x 96 cassette
   mounts: inside the ring tube's hollow, pressed to the inner skin -- the
   cassettes sit against the wall they feed
   needed: the only demonstrated source of negative energy density -- 41
   orders short, and that honesty is the point
   material: plate stack at 2300 kg/m^3 (casimir_rho)
   stores: stores -3.09 MJ of NEGATIVE energy in the vacuum gaps -- the
   only 'fuel' here that is geometry, not matter
   mass from: casimir_cassettes stacks: N x plate^2 x stack x rho
   spec: 96 cassettes, 1.1 m plates, 10 nm gap at 60 nm pitch, 3.68 m stack
   -- 5,887,999,968 plates total for -3.09 MJ of true negative energy;
   precision fabrication at a count no lab has approached
   role & build: The Casimir force is measured, real physics. Stacking
   cassettes to joule-class negative energy has never been demonstrated --
   a scaling problem, not a fake one.
   nearest hardware: Lamoreaux 1997 measured the Casimir force on a plate
   -- real force, unbuilt at stack scale
   runs: none (passive plates) -- continuous -- supplies -3.09 MJ of
   negative energy
   active: all phases -- the plates hold their -3.09 MJ whether or not
   anyone asks
   mission: held -3.09 MJ negative the whole way -- untouched, because
   nothing needed it and nothing could use it
   fails: none at cruise; it is never drawn on subluminally
   cascade: cassette loss -> nothing -- it feeds no system; the least
   consequential failure aboard
   thermal: passive vacuum plates at ambient -- the negative energy sits in
   the gaps, not the material
   connects: embedded in the ring wall, energised through the same field
   system the coils drive
   required by: required by nothing in this build -- the exotic store is 41
   orders sub-critical; it feeds no system
   proven: density -4.334e4 J/m^3 and total -3.09 MJ checks; plate-count
   derivation; mass recompute
   keys: casimir_cassettes=96, casimir_plate_m=1.1, casimir_gap_nm=10,
   casimir_pitch_nm=60, casimir_stack_m=3.68, casimir_rho=2300
   on screen: labelled 'CASIMIR NEGATIVE-ENERGY LATTICE (96)' -- assembly
   step 9 of 17; slides 150 m forward when exploded

>> DEFLECTOR                  1061 t    0.1%  [TODAY  ]
   sits: ~33 x 33 m cross-section x 9.7 m along the ship axis, forward,
   station z=+65 m
   envelope: farthest point 72.6 m of the 182.2 m flat interior (109.7 m of
   margin)
   mesh: 302 verts, 275 facets of render weight
   what it is: a sacrificial dust shield at the bow -- at cruise beta each
   interstellar grain hits like a bomb
   unit: one 33.0 m dia x 0.40 m disk facing forward
   mounts: the nose cap on a flared pedestal, 8.28 m deep at the bow
   needed: at cruise beta each ISM grain carries megajoules -- someone has
   to take the hit
   material: deflector plate at 3100 kg/m^3 (deflector_rho)
   stores: consumes itself -- the sacrificial face erodes so the hull does
   not
   mass from: disk: pi(d/2)^2 x deflector_t_m x rho; the drawn backing +
   pedestal ride under this bill
   spec: 33.0 m dia Whipple-style shield, 8.28 m deep
   role & build: Debris shield plate. Ordinary.
   nearest hardware: NIAC dust-shield and StarTram whipple studies --
   studied, never needed at this energy
   runs: none (passive) -- always in the flight direction
   active: CRUISE and BRAKE -- where the ISM flux is
   mission: faced 4.04e+26 swept ISM particles released forward when the
   bubble came down
   fails: a puncture lets ISM grit reach the hull -- attrition, not a
   single-event loss
   cascade: face erosion -> ISM grains start landing on the hull -> slow
   attrition, not an event
   thermal: dust strikes flash the face locally -- sacrificial by design,
   hot by occupation
   connects: bolted to the bow, in front of everything -- it takes the ISM
   flux first
   required by: required by hull integrity at cruise beta -- ISM grains at
   0.85c are megajoule events
   proven: envelope check (rim reach 72.6 m); mass recompute
   keys: deflector_d_m=33, deflector_depth_m=8.28, deflector_t_m=0.4,
   deflector_rho=3100
   on screen: labelled 'NAVIGATION DEFLECTOR' -- assembly step 13 of 17;
   slides 96 m forward when exploded

>> RCS PODS                   4715 t    0.4%  [TODAY  ]
   sits: ~42 x 42 m cross-section x 113.7 m along the ship axis, forward,
   station z=+21 m (box spans the whole multi-unit arrangement)
   envelope: farthest point 58.9 m of the 182.2 m flat interior (123.3 m of
   margin)
   mesh: 704 verts, 960 facets of render weight
   what it is: ion/VASIMR thruster pods -- subluminal attitude and docking
   only; the warp ring does the real moving
   unit: each pod is a 4.76 m dia x 9.2 m cylinder of tank, cathode and
   grid
   per unit: 147.3 t each x 32 pod
   mounts: mounted proud on the hull skin in 4 rings at z =
   -53.9/+37.1/+45.1/+55.1 m -- midships is owned by the Penning bays, so
   the pods ride the stations that are clear of them
   needed: the ring cannot dock -- subluminal trim still needs thrusters
   material: thruster pod at 900 kg/m^3 (rcs_rho)
   stores: propellant-limited -- trim and docking authority only, never a
   propulsion system
   mass from: rcs_pods cylinders: N x pi(d/2)^2 x rcs_len_m x rho
   spec: 32 pods, 4.8 m x 9.2 m each -- ordinary propulsion plumbing
   role & build: Attitude thrusters. Ordinary.
   nearest hardware: flown ion drives (Dawn, DS1, VASIMR-class demos) --
   the most routine part on the ship
   runs: propellant-limited bursts -- attitude trim and docking only
   active: DOCK and course trim only
   mission: no mission-energy footprint -- trim authority costs propellant,
   not joules
   fails: loss -> the ship tumbles; annoying, not fatal
   cascade: loss -> no attitude authority -> docking becomes impossible;
   flight itself is unaffected
   thermal: thruster waste heat is small and episodic
   connects: hull-mounted aft, plumbed to propellant tanks and the hotel
   bus
   required by: required by docking and attitude trim only -- the ship
   flies fine without them until it needs to stop
   proven: mass recompute; count check vs spec
   keys: rcs_pods=32, rcs_d_m=4.76, rcs_len_m=9.2, rcs_rho=900
   on screen: labelled 'RCS / ION PODS (32)' -- assembly step 15 of 17;
   slides 66 m forward when exploded

>> BOOST RECTENNA            17.59 t    0.0%  [NEAR   ]
   sits: ~84 x 84 m cross-section x 27.8 m along the ship axis, aft,
   station z=-76 m
   envelope: farthest point 99.3 m of the 182.2 m flat interior (82.9 m of
   margin)
   mesh: 177 verts, 175 facets of render weight
   what it is: a 4 km film of rectifying antenna that unfolds to catch the
   stellar tap's beam -- the fuel line
   unit: a single 4.0 km film disk, 1 um thick -- the only part measured in
   km
   mounts: stowed aft at z = -73.36 m on an 11 m deploy mast off the tail
   cap (collector_z0_m is a magnitude); unfolds 4.0 km when the beam is on
   needed: the kinetic bill is 15 YJ -- the ship cannot carry it, so it
   catches it
   material: rectenna film at 1400 kg/m^3 (collector_film_rho)
   stores: consumes nothing aboard -- it harvests the beam; capture inside
   the Airy spot reaches 100%%
   mass from: film disk: pi(collector_d/2)^2 x collector_film_um x rho; the
   drawn stowed dish + deploy mast are stowage hardware under this bill
   spec: deployed 4 km dia (stowed 84.4 m), film 1 um at 1400 kg/m3 --
   ~17.6 t of deployed film; power beaming proven at a kilometre scale
   role & build: Rectennas are proven. A kilometres-wide deployable film
   has never been flown -- engineering, not physics.
   nearest hardware: kW-class microwave-power-transfer rectennas (MPT
   experiments) -- GW capture at this aperture is scale work, not new
   physics
   runs: captures up to 100% of the tap while deployed -- deployed during
   boost only; stowed at cruise
   active: BOOST and the photon-brake leg -- stowed in between
   mission: harvested 1.51e+25 J on boost and dissipated 1.42e+25 J of
   photon-brake work on arrival
   fails: failure to stow -> a 4 km sail in the ISM flux; failure to deploy
   -> no boost, mission scrubs
   cascade: loss -> no boost, no brake -- the ship becomes a one-way
   unpowered ballistic
   thermal: under the beam it carries intercepted flux; conversion loss
   warms the film -- one reason it stows at cruise
   connects: aft-mounted on the spine, wired to the ship bus -- the only
   interface that imports power instead of making it
   required by: required by the boost phase and the photon brake -- no
   receiver, no ride
   proven: capture <= 1 and film-mass recompute checks
   keys: collector_d_m=84.4, collector_depth_m=16.52,
   collector_deploy_km=4, collector_film_um=1, collector_film_rho=1400,
   collector_z0_m=73.36
   on screen: labelled 'BOOST RECTENNA' -- assembly step 14 of 17; slides
   94 m aft when exploded

>> MAGSAIL LOOP           1.28e+04 t    1.2%  [FAR    ]
   sits: ~1400 x 1400 m cross-section x 4.2 m along the ship axis, aft,
   station z=-109 m (box spans the whole multi-unit arrangement)
   envelope: farthest point 708.3 m of the 182.2 m flat interior (-526.1 m
   of margin)
   mesh: 208 verts, 50 facets of render weight
   note: drawn at 1:4000 so it fits on screen -- the real loop is 5600 km
   across
   what it is: a superconducting current loop inflating a magnetic bubble
   -- drag against the ISM is the brake
   unit: a single 2800 km radius loop of superconductor -- the largest
   object in the build
   mounts: mounted aft; deploys to a 2800 km radius loop -- the mount is
   the only small part of it
   needed: arriving is harder than leaving -- only ISM drag stops the ship
   without a destination array
   stores: regenerates 62% of drag energy back to the SMES buffer -- a
   brake that pays for itself
   mass from: declared mass magsail_mass_kg -- the loop's conductor mass is
   a spec, not derived from geometry
   spec: 17593 km of superconductor at 4.4 MA, 12800 t loop (728 g/m), drag
   coef 0.85, 62% regen recovery -- the conductor budget is thinner than
   the current demands, which is what keeps this FAR
   role & build: The plasma interaction is modelled (Zubrin 1991, Freeland
   2015). A 2800 km superconducting loop has never been deployed,
   stabilised or repaired -- and those verbs are the whole problem.
   nearest hardware: Zubrin & Andrews 1991 concept; the mini-magnetosphere
   (M2P2) cousin was wind-tunnel tested, never flown
   runs: drag power -> 62% recovered to the SMES -- deployed during braking
   only
   active: BRAKE only -- stowed the whole way out
   mission: regenerated 9.48e+21 J to the SMES buffer -- then the photon
   brake finished what drag could not
   fails: current quench mid-brake -> the sail goes slack and braking
   stops; the flyby continues ballistically
   cascade: deployment failure -> cannot stop unaided -> flyby unless the
   destination array exists
   thermal: drag energy mostly recovers; the rest warms the plasma sheath
   around the loop
   connects: deployed from the spine aft; regenerates into the SMES buffer;
   its aperture doubles as the ISM scoop
   required by: required by arrival itself -- the only credible way to stop
   without a pre-built destination array
   proven: full-stop ~32,600 yr and halving-time checks
   keys: magsail_r_km=2800, magsail_current_a=4.4e+06,
   magsail_mass_kg=1.28e+07, magsail_cd=0.85, magsail_regen_eff=0.62,
   magsail_view_scale=0.00025
   on screen: labelled 'MAGNETIC SAIL (drawn 1:4000)' -- assembly step 16
   of 17; slides 150 m aft when exploded

>> CONSUMABLES + CREW         76.8 t    0.0%  [NEAR   ]
   what it is: the crew plus their food, water and spares -- the payload
   every other ton exists for
   unit: 3200 kg of food, water and spares per head x 24 crew
   per unit: 3200 kg each x 24 crew member
   mounts: inside the hull, on the decks -- cargo has no mount
   needed: the entire ship exists to deliver these 24 people alive
   stores: stores 3200 kg of food, water and spares per head x 24 crew =
   76.8 t of carried mass
   mass from: crew x crew_supplies_kg -- payload, not structure
   spec: 24 crew x 3200 kg of consumables, hotel load 96 MW, a closed loop
   for the full crossing -- longer than any loop run to date, by a factor
   of years
   role & build: Closed-loop life support for a 5.0 year crossing exceeds
   ISS practice. Scaling, not physics.
   nearest hardware: ISS closed-loop life support -- the most proven system
   aboard
   runs: 96 MW hotel load -- continuous
   active: all phases -- consumed at ~hotel rate for the whole 9 yr
   share of cruise: 0.2% of the 47.1 GW beta=0.99 cruise load
   mission: the crew aged +2.516 s against Earth -- gravitational drift
   only; that IS the whole time story
   fails: ECLSS margin: days of buffer, not weeks -- the crossing is 5.0
   years of uninterrupted loop
   cascade: depletion -> mission deadline, not an event -- the slowest
   failure mode aboard
   thermal: ambient stores; the crew's metabolic and hotel heat is part of
   the 96 MW that must radiate
   connects: consumed by the decks; supported by the reactor's hotel load
   and the cryo-cooled hull
   required by: required by the mission's purpose -- every other part
   exists to keep these 24 people alive
   proven: crew count check; supplies-per-head spec
   on screen: no mesh -- carried mass, drawn as nothing (the mass is real,
   the pixels are not)


>> + THE WARP BUBBLE -- the part that carries no mass
   what it is: the drive itself -- a stationary spacetime solution, not
   hardware. A 366.9 m sphere of curved metric with a 0.20 m transition
   wall and a 182.2 m flat interior (f=1) where the hull lives. It has no
   mass line because it has no mass: the shell and coils above are the
   stress-energy that WRITES it into the metric.

   geometry: bubble_r_m 183.44 m (f=0.5 at the wall), wall delta 0.20 m,
   interior cutoff R-6delta (f=0.9997). Drawn as a translucent shell in the
   viewer.

   held up by: the 96 field coils + shell sectors keeping the shape --
   servo error drains integrity; at 0.35 it collapses and the ship falls
   out of warp. Superluminal shape demands the exotic bill is booked as
   debt, never paid -- 41.3 orders short against the Casimir store.

   at cruise: at the emergent beta=0.8547 the bubble owes nothing --
   subluminal warp is positive-energy and the exotic bill (-5.66e+47 J at
   beta=1) only appears when the command crosses 1.0c. The bubble is the
   one component whose 'fuel' changes sign with the throttle.

   proven by: f(R)=0.5 at five wall decades, theta antisymmetry, the wall
   integral over 33 decades, 'ring straddles the wall', subluminal NEC pass
   / superluminal NEC fail -- the whole first page of the selftest.

```

### 15c. EXTERNAL INFRASTRUCTURE  (what the ship does not carry)

```
The components the mission needs that the ship does not carry.
None of them is a part you can bolt on -- each is a standing
installation, and two of them are what make rendezvous possible at
all. The ship can fly without them; it can only fly PAST without
them.

>> STELLAR TAP (6.4E+18 W, 1000 KM ARRAY) [FAR       ]
   what it is: a 1,000 km solar-collector array near Sol beaming 6.4 EW of
   collimated light at the ship -- the propellant you do not carry; the
   mass stays home
   Lawful physics -- a laser is a laser. The bill is civilisational: a
   transmitter the size of a country and the power to feed it. No
   engineering shortcut moves it under 30 years.
   needs: 6e+18 W delivered across 0.6 ly -- a national-grid-scale
   transmitter, permanently funded
   physics source: Forward 1961 laser-sail lineage; the beam physics is
   Airy diffraction, checked live against beam_power_w

>> DESTINATION PHOTON BRAKE               [FAR       ]
   what it is: a second tap, pre-built at the destination, firing photons
   at the arriving ship's rectenna -- the difference between a rendezvous
   and a flyby
   A second tap, pre-built at Proxima, or the ship remains a flyby.
   needs: the same transmitter, already standing at the far end before
   launch
   physics source: the same tap physics aimed at the bow -- verified by the
   capture <= 1 and brake-work honesty checks

>> HELIUM-3 SUPPLY CHAIN                  [FAR       ]
   what it is: the mining/separation economy that feeds the fusion plant --
   the fuel side nobody budgets for
   Lunar regolith extraction at tonne scale -- an industry, not a
   prototype.
   needs: tonnes of 3He per decade -- lunar mining, refining and lift
   capacity combined
   physics source: lunar-regolith / gas-giant scoop literature; isotope
   separation exists at gram scale, not tonne scale

>> ISM SCOOP REFUELLING                   [FAR       ]
   what it is: skimming interstellar gas through the magsail aperture and
   sorting the isotopes -- real, but isotope-lean; loses to burn at every
   cruise speed in the model
   Shares the magsail's unproven physics, plus isotope separation underway.
   needs: 6.18e-01 kg/s of gas scooped at cruise -- the loop again, plus a
   refinery that runs while it brakes
   physics source: Bussard 1960 ramjet lineage -- the model prices it and
   the scoop loses to burn at every cruise beta

>> THE WARP SHELL AS A DRIVE              [OPEN      ]
   what it is: the bubble itself -- a stationary spacetime solution that
   transports the flat region, not a propulsion system that pushes mass
   Subluminal positive-energy shells exist on paper (Bobrick & Martire
   2021); the material to build one does not. Superluminal is not a
   schedule problem -- it is NEC violation, barred by theorem.
   needs: a material with anisotropic stress near the sound-speed limit --
   unnamed, unmeasured, unpriced
   physics source: Alcubierre 1994, Van Den Broeck 1999, Krasnikov 1998 --
   metric engineering, not propulsion

>> WORMHOLE GATES AND TIME MACHINES       [IMPOSSIBLE]
   what it is: Morris-Thorne throats and their CTC descendants -- every
   construction priced in the portal section, most barred by quantum
   inequalities
   Every construction in the model prices its exotic energy honestly and
   every one comes back decades of orders short. Not a procurement
   question.
   needs: 2.421e+44 J of negative energy for the smallest gate -- nothing
   to buy it with
   physics source: Morris-Thorne 1988 traversability + the Ford-Roman
   quantum-inequality literature that bars most of it


THE PORTAL GATE, PART BY PART -- the Morris-Thorne installation
rendered on the PORTAL tab. Buildable hardware vs the spacetime
state it would need are kept distinct, on purpose.

>> GATE A  (mouth, Sol side)               504 facets
   the near mouth at Sol -- a 12 m Morris-Thorne ring mouth; buildable
   frame, unbuildable throat

>> THROAT FIELD COILS (16)                 576 facets
   the windings that would have to shape the throat's stress-energy -- the
   only part of the gate with a ship analogue

>> THROAT CASIMIR CASSETTES (8)            240 facets
   the negative-energy plates the throat demands -- 45 orders short of what
   a 12 m mouth needs

>> THE THROAT  (embedding diagram)          47 facets
   the embedding funnel itself -- not hardware, a spacetime state; tidal
   forces at this radius are lethal by ~14 orders

>> GATE B  (mouth, far side)               279 facets
   the far mouth at the destination -- the pair's other end; the
   clock-offset bookkeeping lives here

   governed by: portal_gate_d_m=24, portal_ring_minor_d_m=3,
   portal_coils=16, portal_casimir_rings=8, portal_frame_d_m=34

```

### 15d. EVERY SPECIFICATION KEY  (DIMS / PLANT / DRIVE, verbatim)

```
DIMS  (100 keys)
   bubble_r_m = 183.44 -- r_s where the shape function falls to 1/2 -- x2
   again (1.83x the original WD-1)
   wall_thick_m = 0.2 -- wall thickness delta; sigma = 1/delta -- a SPACETIME
   parameter, not structure: it does not scale with the hull
   interior_margin = 6 -- flat interior ends this many delta inside R (f >
   0.9997 there) -- see flat_interior_r()
   ring_major_d_m = 366.88 -- ring centreline diameter = 2 x bubble_r_m
   ring_minor_d_m = 27.52 -- tube diameter of the toroidal shell
   ring_wall_m = 1.08 -- shell wall thickness (a shell, not solid) -- x2:
   shell stress scales with span
   ring_sectors = 96 -- x2: doubled circumference, same sector arc
   ring_density = 4,100 -- conditioned SiC/W metamaterial [kg/m^3]
   coils = 96 -- x2: one per doubled ring sector
   coil_bore_m = 27.92 -- clear bore of a coil wrapped around the ring tube:
   tube dia + 2 x standoff = 27.52 + 0.40 (derived, not free -- a smaller
   bore cannot thread the tube it energises)
   coil_len_m = 17.24 -- axial length along the ring tube -- x2
   coil_turns = 48,000 -- REBCO tape turns per coil (same tech)
   coil_current_a = 38,000 -- operating current [A]
   coil_temp_k = 18 -- HTS operating temperature [K]
   coil_build_m = 0.3 -- radial winding-pack build [m]. Set by engineering
   J_e of the REBCO tape: build ~ N*I / (J_e * circumference). The bore
   doubled this pass so the same turns x current COULD fit a ~0.15 m pack;
   0.30 m is kept as a conservative quench-stabilizer margin on the larger
   machine rather than claimed as savings
   coil_standoff_m = 0.2 -- gap between ring-tube surface and the winding
   pack inner radius [m] -- x2
   coil_density = 5,600 -- winding-pack average density [kg/m^3]
   capring_d_m = 176.08
   capring_minor_d_m = 12.84
   cap_offset_m = 69.72 -- +/- z offset from the ring plane
   capring_wall_frac = 0.3 -- solid fraction of the shaping-ring torus
   hull_len_m = 124.76
   hull_d_m = 32 -- x2 -- twice WD-1's cabin diameter
   hull_decks = 12 -- x2: doubled hull length
   hull_wall_m = 0.44 -- hoop-stress scaling t = P*r/sigma is LINEAR in hull
   radius: 32.0 m returns exactly 2x WD-1's 0.22 m wall
   hull_shell_rfrac = 0.88 -- mean shell radius as a fraction of hull radius
   (the nose/aft taper) -- dimensionless shape factor, unchanged
   hull_density = 2,700 -- Al-Li / composite pressure hull [kg/m^3]
   deck_t_m = 1.4 -- deck plate thickness -- x2: plate bending stress ~ p L^2
   / t^2, doubled span needs doubled thickness for the same margin
   deck_inset_m = 1.2 -- deck plate inset from the hull wall [m] -- x2 with
   the hull radius
   crew = 24 -- x2 with the doubled cabin volume
   crew_supplies_kg = 3,200 -- consumables + outfitting per crew [kg]
   len_margin_m = 20 -- end-fittings / docking margin in the overall-length
   figure [m] -- x2
   pylons = 12 -- x2: an 8x-heavier hull on a doubled span
   pylon_len_m = 154.08
   pylon_w_m = 5.88
   pylon_t_m = 4.8 -- section thickness -- x2: an 8x load on a 2x span needs
   ~2x thickness to hold the same bending/buckling margin
   pylon_rho = 2,700 -- same Al-Li/composite as the hull [kg/m^3]
   reactor_major_d_m = 21.24 -- x2: torus volume x8
   reactor_minor_d_m = 6.36
   reactor_wall_m = 3.6 -- vessel wall -- x2: pressure-vessel wall t =
   P*r/sigma is linear in radius
   reactor_rho = 5,200 -- vessel average density [kg/m^3]
   reactor_th_gw = 102.7 -- thermal output [GW] -- derived, not typed:
   beta=0.99 cruise electrical load is ~47.1 GW (coil_ac x8 + cryo/control x4
   + hotel x2 vs pass 6); /0.62 gives 76.0 GW thermal, x the SAME 1.35 design
   margin = 102.7 GW. Torus volume grew x8, so specific power density is the
   same as pass 6
   reactor_direct_eff = 0.62 -- direct energy conversion (aneutronic)
   amtraps = 8 -- x2 bays on the doubled spine
   amtrap_d_m = 9.56
   amtrap_wall_m = 1.2 -- containment shell -- x2 with the sphere
   amtrap_rho = 4,400 -- trap shell density [kg/m^3]
   amtrap_kg = 5.248 -- antihydrogen per trap [kg] -- scales S^3 with the
   kinetic-energy bill it buffers
   smes_major_d_m = 40.36
   smes_minor_d_m = 4.4
   smes_wall_m = 1 -- torus shell -- x2 with the structure
   smes_rho = 6,800 -- winding/structure average [kg/m^3]
   smes_b_t = 60 -- bore field [T] -- same HTS technology
   smes_z0_m = 40.36 -- mount offset along the spine [m] -- x2
   casimir_cassettes = 96 -- x2: the ring wall circumference doubled
   casimir_plate_m = 1.1 -- square plate edge (module, unchanged)
   casimir_gap_nm = 10 -- vacuum gap between plates (nanoscale,
   casimir_pitch_nm = 60 -- gap + plate thickness -- unaffected by the ship's
   macroscopic scale)
   casimir_stack_m = 3.68 -- stack height per cassette -- x2
   casimir_rho = 2,300 -- plate stack average density [kg/m^3]
   radiators = 60
   rad_len_m = 90.44
   rad_w_m = 31.32
   rad_inner_r_m = 69.56 -- panel root radius -- x2
   rad_z0_m = -24.36 -- panel leading edge -- x2
   rad_temp_k = 1,550 -- design-point panel temperature [K]
   rad_limit_k = 1,900 -- graphite sublimation limit [K]
   rad_emissivity = 0.92
   rad_t_m = 0.24 -- panel sandwich depth -- x2: a 2x span panel needs ~2x
   depth for the same bending stiffness (I ~ t^3 term)
   rad_rho = 1,900 -- graphite panel density [kg/m^3]
   cryo_units = 16 -- x2 units, each x2 in size (volume x8)
   cryo_d_m = 11
   cryo_len_m = 20.16
   cryo_rho = 240 -- insulation/plumbing average [kg/m^3]
   cryo_mount_rfrac = 0.8 -- mounting radius as a fraction of the ring major
   radius (envelope check only)
   deflector_d_m = 33
   deflector_depth_m = 8.28
   deflector_t_m = 0.4 -- dish skin -- x2 with the dish
   deflector_rho = 3,100 -- whipple/composite density [kg/m^3]
   rcs_pods = 32 -- x2: more authority for an 8x hull
   rcs_d_m = 4.76
   rcs_len_m = 9.2
   rcs_rho = 900 -- propellant+tank average [kg/m^3]
   collector_d_m = 84.4 -- stowed dish diameter -- x2
   collector_depth_m = 16.52
   collector_deploy_km = 4 -- deployed film rectenna diameter [km] unchanged:
   set by beam diffraction at the (unchanged, external) transmitter, not by
   ship size
   collector_film_um = 1 -- rectenna film thickness [um]
   collector_film_rho = 1,400 -- film density [kg/m^3]
   collector_z0_m = 73.36 -- stowed mount offset along the spine [m]
   portal_gate_d_m = 24 -- engineered aperture (throat 2 b0)
   portal_ring_minor_d_m = 3
   portal_coils = 16 -- field coils around the rim
   portal_casimir_rings = 8 -- negative-energy cassettes at the throat
   portal_frame_d_m = 34 -- structural frame outside the aperture
   magsail_r_km = 2,800 -- deployed loop radius [km]
   magsail_current_a = 4,400,000 -- persistent loop current [A] -- x2 keeps
   the same loop-centre field (B ~ I/r)
   magsail_mass_kg = 1.28e+07 -- HTS cable + deployment mass [kg] x8
   magsail_cd = 0.85 -- effective ISM drag coefficient
   magsail_regen_eff = 0.62 -- braking energy recovered to the bus
   magsail_view_scale = 0.00025 -- 1:4000 -- printed on screen, always

PLANT  (12 keys)
   hotel_mw = 96 -- life support, computation, sensors [MW] -- x2 with the
   doubled crew
   coil_ac_mw = 38252.8 -- AC ripple + field-shaping losses in the 96 HTS
   coils at cruise [MW] -- ~S^3
   cryo_mw = 2492.8 -- cryoplant electrical draw [MW] -- ~S^2
   control_mw = 7,064 -- metric servo: 10 kHz shell-shape control [MW] --
   ~S^2 over the ring surface
   conversion_eff = 0.62 -- direct conversion, aneutronic D-3He
   recovery_eff = 0.92 -- fold charge recovered on deceleration
   am_energy_j_kg = 1.7975e+17 -- 2*m*c^2 per kg antimatter (matter+anti)
   d3he_j_kg = 3.52e+14 -- D + 3He -> 4He + p + 18.35 MeV, per kg mix
   tap_w = 6.4e+18 -- stellar-tap boost beam [W] -- x8 again: mission
   infrastructure sized to the ship; an ~8x mass needs ~8x delivered power to
   hold the same cruise speed. ~17 ppm of L_sun (6.4e18 / 3.828e26).
   beam_aperture_km = 1,000 -- transmitter phased-array aperture [km]
   beam_lambda_um = 1 -- transmitter wavelength [um]
   beam_range_ly = 0.62 -- usable boost range from the array [ly]

DRIVE  (8 keys)
   beta_sub_max = 0.99 -- physical (positive-energy) drive ceiling
   beta_ftl_max = 10 -- Alcubierre mode ceiling (flagged, exotic)
   spinup_s = 42 -- ship-seconds per unit beta
   bubble_form_s = 18 -- shell shape convergence time
   integrity_min = 0.35 -- below this the bubble collapses
   wall_min_m = 1e-15 -- thinnest wall the shape servo can hold
   wall_max_m = 12
   arrival_beta = 0.001 -- under 0.001 c counts as station-keeping

```

### 15e. RUNTIME STATE & CONTROLS  (every field, every key)

```
WARPCORE -- the live drive state

   beta_cmd / beta commanded speed vs what the shell is doing
   bubble_cmd / bubble_on raise command vs convergence 0..1 (forms in 18 s)
   wall_m live wall thickness -- drives the energy bill and tidal shear
   integrity shape-servo health; below 0.35 the bubble collapses
   collapsed / collapse_msg / was_superluminal failure state, its honest
   report, and the >1c rest-frame flag
   magsail_deployed / rectenna_deployed brake / receiver states
   coil_phase / coil_glow per-sector energisation (96 values)
   smes_j buffer charge (starts at 1.52 TJ)
   rad_k panel temperature -- lags via heat capacity (tau 90 s)
   load_w / waste_w / beam_w live electric load, waste heat, captured tap
   exotic_need_j / exotic_debt_j negative energy demanded vs OWED -- booked
   as debt, not supply
   status COLD / NOMINAL / UNFUNDED / COLLAPSED
   led cumulative ledger: beam_in, plant_out, kinetic, kinetic_peak,
   radiated, magsail_regen, brake_dissipated, fuel_kg, am_kg, ism_particles
   helm_locked() beta > 1: the forward wall is causally disconnected

VOYAGE -- the mission state machine

   phase DOCK -> BOOST -> CRUISE -> BRAKE -> ARRIVED (forward only)
   x_m / v_ms / beta position, velocity, v/c on the Sol-Proxima line
   remaining_m / eta_s() distance and time left at current speed
   t_coord / t_ship / t_earth coordinate, ship and Earth clocks -- ship=Earth
   modulo the gravitational drift
   dest_array destination photon brake assumed present or not
   warp_i / warp time-warp rung: 1 s/s, 1 min/s, 1 h/s, 1 d/s, 30 d/s, 1
   yr/s, 10 yr/s
   ism_particles / f_magsail / f_beam swept count and live drag forces
   arrived_at / log / target_m arrival stamp, mission log, Proxima at
   4.02e+16 m

TEST MODE (chip or T key): auto-plays the current settings --
commanded beta, wall, destination array, warp -- through boost,
cruise and an honest ending (arrived, flyby, stalled or
collapsed). Same begin_boost()/begin_brake() calls as manual
flight; nothing is faked.

ENVELOPE -- radiator tip reaches 152.8 m inside a 182.2 m interior (29.4 m clear)

   deflector rim 73 m   hull midbody 16 m   radiator tip 153 m   boost rectenna 99 m   shaping ring 117 m   cryo unit 147 m   SMES toroid 46 m

CONTROLS

   TAB/cycle views | drag/wheel/right-drag orbit/zoom/pan | R reset
   1 2 3 = full/exploded/assembly | 4 or X = section | L labels
   , . beta | [ ] wall | B shell | F alcubierre | G/K boost/brake
   J dest array | T test demo | - + warp | N reset | P pause
   I / M / H = this panel / energy ladder / help

CLI -- python Warpdrive.py [--selftest|--feasibility|--spec|
   --metric|--ladder|--dilation|--portal|--send|--voyage [beta]
   [--flyby]|--all]  (no flag = interactive viewer)
```

### 15f. MODEL FUNCTION REGISTRY  (every function, method & helper)

```
WARP METRIC & SHAPE
   alcubierre_energy_j(beta, R=None, delta=None) -- Total (negative) energy
   of the Alcubierre warp field [J].
   energy_density(x, rho_perp, beta, R=None, delta=None) -- Eulerian energy
   density T^00 measured by observers at rest [J/m^3].
   equiv_mass_kg(energy_j) -- E/c^2
   shape_df(r, R=None, delta=None) -- df/dr_s
   shape_df_shifted(u, R=None, delta=None) -- df/dr evaluated at r = R + u,
   computed FROM u directly.
   shape_f(r, R=None, delta=None) -- Alcubierre top-hat shape function
   f(r_s). f -> 1 inside, 0 outside.
   wall_tidal_gradient(beta, R=None, delta=None) -- Tidal acceleration across
   a 2 m body sitting IN the bubble wall [m/s^2].
   warp_energy_integral(R=None, delta=None, samples=4000) -- I = INT_0^inf
   r^2 (df/dr)^2 dr [m], by composite Simpson over the wall.
   york_theta(x, rho_perp, beta, R=None, delta=None) -- York time / expansion
   scalar theta = beta c (x / r_s) df/dr_s [1/s].

QUANTUM & NEC CONSTRAINTS
   barrier_analysis() -- Returns a dict of barrier -> {value, threshold, gap,
   passable, route}.
   barrier_scorecard() -- Returns a list of (name, status, detail) for the 8
   barriers.
   casimir_cassette() -- Geometry and yield of ONE onboard Casimir cassette.
   casimir_energy_density(gap_m) -- Casimir vacuum energy density between
   ideal parallel plates [J/m^3].
   casimir_onboard_j() -- Total negative energy the whole 24-cassette lattice
   actually holds [J].
   energy_conditions(beta) -- Which pointwise energy conditions the commanded
   solution satisfies.
   ford_roman_bound_j_m3(tau_s) -- Ford-Roman quantum inequality bound on
   negative energy density [J/m^3].
   ford_roman_max_throat_tau(b0) -- Longest you can hold a throat of radius
   b0 open, by the QI bound [s].
   ford_roman_wall_limit(beta) -- Quantum-inequality bound on the wall
   thickness [m].
   horizon_locked(beta) -- True when the forward bubble wall is causally
   disconnected from the ship.

SHIP & ENVELOPE
   check_envelope(delta=None) -- Does the ship still fit inside its own flat
   interior?
   flat_interior_r(delta=None, R=None) -- Radius of the exactly-flat interior
   [m].
   mass_budget() -- Component-by-component dry mass, computed from the
   geometry the renderer
   ship_mass_kg() --

POWER, THERMAL & FUEL
   cruise_load_w(beta, bubble_on=1.0) -- Electrical load to HOLD the warp
   field at beta [W].
   fusion_fuel_kg(energy_j) -- D-3He mass burnt to deliver this much
   ELECTRICAL energy.
   kinetic_energy_j(beta, mass_kg=None) -- (gamma - 1) M c^2
   lorentz_gamma(beta) --
   plant_electric_w() -- Direct-conversion electrical capacity of the D-3He
   plant [W].
   radiator_area_m2() -- Installed radiating area
   radiator_required_m2(waste_w, t_k=None) --
   radiator_temp_k(waste_w) -- Equilibrium panel temperature from
   Stefan-Boltzmann: T = (P/eps sigma A)^1/4.
   smes_store_j() -- SMES capacity from first principles: u = B^2 / 2 mu0
   over the torus
   waste_heat_w(load_w) -- Everything drawn eventually becomes heat: a closed
   ship exports no work.

PROPULSION, BEAM & BRAKING
   beam_brake_force_n(range_to_array_m) -- Photon-pressure braking against an
   array AT THE DESTINATION [N].
   beam_brake_time_s(beta, mass_kg=None) -- Rough time to stop under
   destination-array photon braking [s].
   beam_capture_frac(range_m) -- Fraction of the beam the deployed rectenna
   actually intercepts.
   beam_power_w(range_m) --
   beam_spot_m(range_m) -- Diffraction-limited spot diameter of the
   stellar-tap boost beam [m].
   boost_profile(beta, mass_kg=None) -- Can the stellar tap actually get this
   ship to beta before the ship flies
   crossing_time_s(beta) -- Coordinate time for Sol -> Proxima at beta. inf
   when the boost
   ism_blast_energy_j(beta, distance_m, R=None) -- Energy stored in the swept
   particles, released forward on bubble
   ism_particles_swept(distance_m, R=None) -- Protons the bubble sweeps up
   over a leg. They do not pass through: the
   magsail_area_m2() --
   magsail_decel_time_s(beta, mass_kg=None, beta_final=None) -- HONEST time
   to brake from beta down to arrival speed on the magsail [s].
   magsail_drag_n(beta) -- Drag of the magnetic sail against the interstellar
   medium [N].
   magsail_halving_time_s(beta, mass_kg=None) -- Characteristic time for the
   magsail to HALVE the speed [s]: t = M/(k v0).
   max_boost_beta(mass_kg=None, lo=0.02, hi=0.99) -- Highest cruise beta the
   beam can actually deliver, by bisection on
   rocket_proper_time_s(beta, distance_m) -- Proper time aboard a
   conventional relativistic cruiser doing the same

ISM ECONOMY
   ism_d3he_yield_kg_s(beta) -- D-3He reactor-grade fuel mass yieldable per
   second of scooping [kg/s].
   ism_scoop_gas_kg_s(beta) -- Raw ISM mass flux intercepted by the magsail
   loop while underway [kg/s].

CLOCKS & DILATION
   clock_ledger(t_ship_s, x_m, beta) -- Every clock in the problem, at one
   instant.
   grav_potential_at(x_m) -- Newtonian potential Phi at distance x along the
   Sol -> Proxima line
   grav_rate(x_m) -- Clock rate dtau/dt at position x relative to a clock at
   infinity.
   lapse_static(r, beta, R=None, delta=None) -- dtau/dt for an observer
   holding station in the EXTERNAL frame at radius
   ship_self_dilation() -- The ship's OWN gravitational time dilation, from
   its own mass [-].
   static_observer_exists(beta) -- False above |beta| = 1: inside a
   superluminal bubble there is no such
   voyage_grav_drift_s(t_total_s, x_start=0.0, x_end=None) -- Accumulated
   crew-vs-Earth clock drift over a crossing, from gravity alone.

WORMHOLES & TIME MACHINES
   chain_wormhole_offset(n_wormholes, elapsed_s, rate_diff) -- Cumulative
   time offset from a chain of N wormholes in series [s].
   ctc_by_gravity_well(phi_over_c2, mouth_sep_m=None) -- Park one mouth in a
   deep well instead. Returns the onset time.
   ctc_by_warp_transport(beta) -- Can you make a time machine by CARRYING one
   mouth on this warp drive?
   ctc_exists(mouth_sep_m, offset_s) -- Do closed timelike curves exist right
   now?
   ctc_onset_s(mouth_sep_m, rate_diff) -- Time until a two-mouth wormhole
   becomes a TIME MACHINE [s].
   gott_pair_offset(mu_kg_m, v_beta, D_m) -- Gott (1991) two cosmic strings:
   maximum time displacement [s].
   kerr_ctc_offset(a_m, r_m, M_kg, n_orbits=1) -- Kerr black-hole CTC:
   maximum time displacement per orbit [s].
   max_time_displacement(elapsed_s=3155760000.0, mouth_sep_m=None,
   phi_over_c2=-0.45, beta=0.999, n_wormholes=10, tipler_L_m=None,
   tipler_R_m=1.0, tipler_omega_rads=1.0, gott_mu_kg_m=1e+21,
   gott_D_m=9460730472580800.0, kerr_M_kg=1.98847e+31, kerr_r_m=None,
   kerr_a_m=None) -- Maximum time displacement across all mechanisms [s].
   mmp_extremal_charge_c(M_kg) -- Extremal magnetic charge for a black hole
   of mass M [C].
   mmp_summary(g_limit=1.0, body_m=2.0) -- The MMP wormhole, fully priced,
   for a survivable crossing.
   mmp_tidal_mass_kg(g_limit=1.0, body_m=2.0) -- Smallest MMP black hole a
   person survives crossing [kg].
   mmp_traversal_time_s(M_kg) -- Asymptotic traversal time for the MMP
   wormhole [s].
   mouth_clock_rate(phi_over_c2=0.0, beta=0.0) -- Proper-time rate of a
   wormhole mouth relative to a clock at infinity.
   mouth_time_offset_s(rate_a, rate_b, elapsed_s) -- Accumulated clock offset
   between the two mouths [s].
   mt_embedding_z(rho, b0) -- Embedding-diagram height z(rho) for the
   Morris-Thorne throat [m].
   mt_exotic_energy_j(b0, shell_factor=1.0) -- Total exotic energy to hold a
   throat of radius b0 open [J].
   mt_flare_out(b0) -- Verify the flare-out condition at the throat.
   mt_min_throat_m(g_limit=1.0, body_m=2.0) -- Smallest throat a person
   survives crossing [m].
   mt_proper_length(b0, r_far=None) -- Proper radial distance from throat to
   r_far [m].
   mt_redshift_phi(r, b0) -- Redshift function Phi(r) [dimensionless].
   mt_shape_b(r, b0) -- Morris-Thorne shape function b(r) [m].
   mt_shape_b_prime(r, b0) -- db/dr for the shape function [dimensionless].
   mt_throat_density(b0) -- Energy density required at the throat [J/m^3].
   mt_tidal_g(b0, body_m=2.0) -- Tidal acceleration across a body of height
   body_m at the throat [g].
   mt_tidal_profile(r, b0, body_m=2.0) -- Radial tidal acceleration across
   body_m at radius r [g].
   mt_traversal_time_s(b0, v_ms=10.0, length_factor=4.0) -- Proper time to
   walk through, at v_ms, across ~length_factor throats.
   multijump_breakeven_s(mouth_sep_m, beta, rate_diff, overhead_s=None,
   b0_m=None) -- Fixed point of the backward recurrence: t* = Delta /
   rate_diff [s].
   multijump_plan(cycles, elapsed_s, rate_diff, mouth_sep_m, beta,
   direction='backward', overhead_s=None, fuel_start_kg=None, b0_m=None) --
   Iterated portal traversal: the multi-jump ledger.
   nested_wormhole_offset(outer_offset_s, inner_offset_s) -- Offset from a
   wormhole nested inside another wormhole [s].
   portal_cycle_s(mouth_sep_m, beta, overhead_s=None, b0_m=None) -- External
   repositioning leg between the mouths at beta, plus hop
   portal_summary(b0=None) -- Everything about the gate, in one dict, for the
   view and the reports.
   portal_traversal(b0_m, mouth_a_phi_c2=0.0, mouth_a_beta=0.0,
   mouth_b_phi_c2=0.0, mouth_b_beta=0.0, mouth_sep_m=None, elapsed_s=0.0,
   payload='person', payload_size_m=2.0, payload_speed_ms=10.0) -- Send
   something through the portal. All four real-physics answers.
   quantum_teleport_facts() -- Quantum teleportation is real, demonstrated,
   and does none of the things
   tipler_cylinder_offset(L_m, R_m, omega_rads, M_kg=None) -- Tipler cylinder
   CTC: maximum time displacement [s].
   visser_shell_energy_j(a_m, M_kg) -- Total exotic energy of the Visser thin
   shell [J] (negative).
   visser_shell_mass_kg(a_m, M_kg) -- Exotic MASS of the Visser thin shell
   [kg] (negative).
   visser_summary(a_m=None, M_kg=None) -- The Visser thin-shell wormhole,
   priced.

HONESTY & AUDITS
   buildability_ledger() -- Every line of the mass budget, rated for when it
   could actually be
   feasibility_scorecard() -- Function-by-function honest scorecard, in the
   style of LS.py's
   honesty_audit(core, voyage, verbose=True) --
   operations_ledger() -- What each mass line needs to OPERATE, not just to
   be built: power

REPORTS & VIEWER
   bar(surf, font, x, y, w, h, frac, color, label, valtext, mark=None,
   lo=None, hi=None) -- Horizontal bar with optional threshold markers.
   build_portal_parts(detail=1.0) -- The portal gate at true scale, plus the
   spacetime it claims to make.
   build_ship_parts(detail=1.0) -- Build every part of the WD-1 to scale.
   Returns an ordered list of Part.
   build_special_parts(detail=1.0) -- The WD-88 Foldmobile at true car scale,
   meshed at CAR_MODEL_DETAIL
   chip(surf, font, x, y, text, on, col_on=None) -- A small toggle pill with
   accent border on the active state.
   contrast_text(bg_rgb, light=(230, 236, 245), dark=(10, 14, 20)) -- Pick a
   readable text colour for a given background.
   draw_bubble_glow(surf, cx, cy, r, intensity, col=None, pulse_phase=0.0) --
   Soft concentric halo for the active warp shell.
   draw_vignette(surf, strength=0.22) -- Subtle corner darkening for
   cinematic depth.
   info_sections() --
   log_bar_x(value_j, x0, x1, lo_exp=0.0, hi_exp=80.0) -- Map |E| onto a
   log10 axis across a pixel span.
   main(argv=None) --
   panel(surf, x, y, w, h, alpha=214) -- Semi-transparent panel with rounded
   border, gradient fill, and
   print_startup_banner() --
   project(pts, az, el, dist, cx, cy, focal, pan=(0.0, 0.0)) -- Project world
   points through the same orbit camera the ShipRenderer uses.
   report_dilation() -- Every clock in the problem, and which one the
   marketing quotes.
   report_feasibility() --
   report_ladder() -- The historical attempts to make the exotic bill
   affordable, and how each
   report_metric() -- Everything the warp metric says, computed live from the
   shape function.
   report_portal() -- The portal, priced.
   report_portal_test() -- Run portal traversal scenarios: signal, person,
   object, time machine.
   report_spec() -- Every component of the ship, specified: geometry, count,
   and the mass
   report_voyage(beta=0.5, dest_array=True) -- Headless Sol -> Proxima
   flight, printed as a mission log.
   selftest() --
   text_shadow(surf, font, text, pos, color, shadow=(0, 0, 0), offset=(1, 1))
   -- Render text with a 1-pixel drop shadow for contrast over 3D scenes.
   vgradient(surf, top, bot) -- Vertical gradient fill, numpy-vectorized.
   wrap_plain(text, width) --
   wrap_text(font, text, maxpx) --

FORMATTING & MATH
   clamp(x, lo=0.0, hi=1.0) --
   fmt_dist(m) --
   fmt_energy(j) --
   fmt_mass(kg) --
   fmt_power(w) --
   fmt_time(s) --
   orders_of_magnitude(a, b) -- log10 |a/b|
   rot_x(a) --
   rot_y(a) --
   rot_z(a) --

MISCELLANEOUS
   car_casimir_j
   car_fault_effects
   car_mass_budget
   car_mph_step
   car_ops_ledger
   car_part_mass
   car_power_budget
   car_thermal_step
   car_transit
   car_trigger_v
   earth_helio_pos
   earth_surface_offset
   road_frame
   road_inertial_speed
   road_solar_hour

INTERNAL HELPERS (51)
   _annulus_cylinder(r_out, r_in, z0, z1, seg=40) -- Hollow tube closed at
   both axial ends (a pipe with real wall thickness).
   _args_real(fn) -- Boundary coercion for helpers whose parameters are ALL
   numeric: every
   _box(cx, cy, cz, sx, sy, sz) --
   _build_portal_parts_impl() --
   _build_ship_parts_impl() --
   _build_special_parts_impl() --
   _car_loft(stations) -- Loft the coupe body: stations are (z, half_width,
   y_top, y_bot) and the
   _coil_arc(r_mid, r_in, r_out, a0, a1, seg_arc=6, seg_tube=10) --
   Winding-pack shell that follows the torus centreline along an arc.
   _coil_count() -- Coil count from DIMS, bounded. The physical ring carries
   tens of
   _component_info_sections() -- The whole bill of materials, explained line
   by line.
   _deck_plate(r_out, z0, z1, holes=(), seg=48, rings=8) -- Solid circular
   slab with off-axis penetration holes + drawn collars.
   _detail_seg(seg) --
   _dish(r_out, depth, z0, seg=28, rings=5, flip=False) -- A parabolic dish
   opening along +Z (deflector, rectenna collector).
   _earth_rate() --
   _envelope_points() -- Extreme (radius, |z|) corners of every part that
   must live INSIDE the
   _finite(*vals) -- True only when every argument is a finite real number.
   Mesh generators
   _function_registry_lines() -- Every public function in this module,
   grouped by domain, with its
   _grp(meshes, group) --
   _hull_loft(sections) -- Loft a smooth body from circular cross-sections
   along Z.
   _info_sections() --
   _label(surf, font, text, pos, accent=False, color=None) --
   _luminance(rgb) -- Relative luminance of an RGB colour (0..1). Used by
   contrast_text().
   _mix(c1, c2, t) --
   _mt_funnel(b0, rho_max, rings=13, seg=40, sign=1.0) -- Wire mesh of one
   half of the Morris-Thorne embedding diagram.
   _numeric_dims() -- _Dims copy of DIMS with every non-real value already
   coerced to NaN,
   _pipe_path(pts, r, seg=10, closed=True) -- Sweep a circle along a polyline
   _place(meshes, pivot, tilt=(0.0, 0.0), group=None) -- Move a set of
   origin-built meshes into position (and orientation).
   _prep_global(plist) -- Merge every part's prepped static meshes into
   shared vertex arrays
   _prep_mesh(m) -- One-time render caches for a Mesh: a padded (nf, w)
   face-index array
   _prep_part(part) -- Collapse a Part's static meshes into one big indexed
   mesh per draw
   _print_traversal(t) -- Print one traversal result compactly.
   _radial(angle) -- Rotation taking a +Z-built primitive to point radially
   outward.
   _real(v) -- Coerce a would-be numeric to float; non-convertible -> NaN.
   Lets the
   _rgb(c, fallback=(0, 0, 0)) -- Coerce any colour-ish value to a valid RGB
   triple; a channel that is
   _ring_wire(r, z, seg=64, axis='z') -- A single closed wire loop
   _rod(p1, p2, r, seg=10) -- A capped cylinder between two arbitrary points
   _rule(title) --
   _runtime_state_lines() -- Every field the live simulation carries
   _sech2(x) -- 1/cosh^2(x), overflow-safe. math.cosh overflows past ~710;
   sech^2 is
   _smooth_sections(ctrl, sub=4) -- Catmull-Rom subdivision of (z, radius)
   control points -> a smooth loft.
   _solid_cylinder(r, z0, z1, seg=32) -- Capped cylinder about +Z.
   _spec_key_lines() -- Every key of DIMS, PLANT and DRIVE with the
   engineering comment that
   _sphere(r, seg=20, rings=12, squash=1.0) -- UV sphere about the origin;
   `squash` scales Z (oblate hull domes).
   _tangential(angle) -- Rotation taking a +Z-built primitive to lie ALONG
   the ring tangent at
   _tilt_z(v) -- Rotate an Earth-fixed vector (equatorial frame, z = pole)
   into the
   _torus(R, r, seg_major=48, seg_minor=12, a0=0.0, a1=6.283185307179586,
   closed=True) -- Torus (or torus ARC from a0 to a1) in the X-Y plane about
   +Z.
   _torus_surface(R, r) --
   _trender(font, text, color) -- font.render with a bounded surface cache:
   the UI redraws a few
   _wire_ellipsoid(a, b, c) -- Bubble wireframe: latitude ellipses plus three
   meridian loops, axes
   _xform(verts, mat=None, off=None) -- Bake a rotation and/or translation
   into a vertex list. Used for parts
   _xy(pos) -- Coerce a position-ish value to a finite (x, y) float pair or
   None.

CLASS Mesh (2 members)
   __init__(self, verts, faces, color, name='', spin=0.0, group='default',
   pivot=(0.0, 0.0, 0.0), tilt=(0.0, 0.0), wire=False, glow=False, hot=False)
   -- Initialize self. See help(type(self)) for accurate signature.
   world_verts(self, angle) --

CLASS Part (1 members)
   __init__(self, key, name, meshes, specs, order, explode, color) --
   Initialize self. See help(type(self)) for accurate signature.

CLASS ShipRenderer (16 members)
   __init__(self, parts_builder, home_az=0.62, home_el=0.42, home_dist=340.0,
   section_keys=()) -- Initialize self. See help(type(self)) for accurate
   signature.
   reset_view(self) --
   zoom_at(self, factor, mouse_pos=None, rect=None) --
   orbit(self, dx, dy, fine=False) --
   pan_by(self, dx, dy, fine=False) --
   set_view(self, mode) --
   toggle_section(self) --
   assembly_next(self) --
   assembly_prev(self) --
   active_part(self) --
   placing_part(self) --
   _sync_pop(self) --
   tick(self, dt) --
   _layout(self, pi, vw, eamt) --
   render(self, surf, rect, angles, mouse_pos=None, show_labels=True,
   label_font=None, interactive=False, coil_glow=None, drive_power=0.0,
   rad_heat=0.0, bubble_on=0.0) -- Paint every visible facet back-to-front.
   `coil_glow` is the rotating
   _section_cut(self, key, wvx, face) -- Remove the +X half of the bulky
   parts

CLASS WarpCore (10 members)
   __init__(self) -- Initialize self. See help(type(self)) for accurate
   signature.
   mode (property) --
   exotic (property) --
   kinetic_now_j(self) --
   energy_conditions(self) --
   helm_locked(self) -- Above beta = 1 the crew cannot signal the forward
   wall, so no new
   _thermal(self, dt) --
   _integrity(self, dt) -- Bubble integrity: what actually breaks a warp
   drive in this model.
   collapse(self, msg) -- The shell lets go.
   update(self, dt, world=None) -- Advance one tick. `dt` is SHIP seconds
   (already time-warped).

CLASS Voyage (14 members)
   __init__(self) -- Initialize self. See help(type(self)) for accurate
   signature.
   warp (property) --
   beta (property) --
   remaining_m (property) --
   cycle_warp(self, d) --
   note(self, text) --
   eta_s(self) --
   update(self, dt_real, core) -- Advance the voyage by dt_real real seconds
   x the time-warp factor.
   _step(self, dt, core) --
   begin_boost(self, core) --
   begin_brake(self, core) --
   auto_step(self, core, tick_s=0.0) -- One scripted phase advance for the
   viewer's TEST mode.
   auto_done (property) -- A demo has nothing left to show: arrived, or
   reached the target
   reset(self, core) --

CLASS MetricCam (10 members)
   __init__(self, az=1.15, el=0.52, dist=560.0) -- Initialize self. See
   help(type(self)) for accurate signature.
   reset_view(self) --
   zoom_at(self, factor, mouse_pos=None, rect=None) --
   orbit(self, dx, dy, fine=False) --
   pan_by(self, dx, dy, fine=False) --
   set_view(self, mode) --
   toggle_section(self) --
   active_part(self) --
   placing_part(self) --
   tick(self, dt) --

CLASS Starfield (4 members)
   __init__(self, n=520, seed=7) -- Initialize self. See help(type(self)) for
   accurate signature.
   draw(self, surf, rect, streak=0.0, drift=0.0) -- Static fields are painted
   once and blitted; only the streaking
   _star_col(self, i, brightness) -- Blackbody-coloured star: base colour
   from spectral class, scaled by
   _paint(self, surf, rect, streak=0.0, drift=0.0) --

CLASS App (37 members)
   __init__(self) -- Initialize self. See help(type(self)) for accurate
   signature.
   _rebuild_bg(self) --
   _rend(self) --
   flash(self, text) --
   set_wall(self, factor) --
   set_beta(self, d) --
   handle_events(self, dt) --
   _chip_click(self, name) --
   _toggle_test(self) -- TEST mode: auto-play the mission with the settings
   currently
   _test_tick(self, dt) -- Drive the demo: hold each phase a couple of real
   seconds so the
   _toggle_ftl(self) --
   _key(self, k, fine) --
   update(self, dt) --
   draw(self) --
   draw_topbar(self) --
   draw_ship(self) --
   draw_view_tabs(self, rect) --
   draw_ship_panel(self) --
   draw_spec_card(self) --
   _spec_card(self, part) --
   draw_metric(self) -- Draw the spacetime, not the hardware.
   draw_profiles(self, b, R, delta) --
   draw_metric_panel(self, b, R, delta) --
   draw_flight(self) --
   draw_flight_hud(self) --
   draw_flight_controls(self) --
   draw_dilation(self) -- Whose clock, and where.
   draw_dilation_graphs(self, beta, R, delta) --
   draw_clock_panel(self, beta) --
   draw_portal(self) --
   draw_portal_panel(self) --
   draw_special(self) --
   draw_special_panel(self) --
   draw_ladder(self) -- Thirty years of trying to make the exotic bill
   affordable, on one
   draw_help(self) --
   draw_info(self) --
   run(self) --

```

### 16. HONESTY LAYER  (what keeps this a twin and not a prop)

```
Ten conservation checks run against the live state, every time you
open this panel and at the end of every headless voyage:

   no over-unity          kinetic gained <= beam + regen delivered
   plant within rating    output <= reactor rating x elapsed time
   fuel backs output      every joule traced to burnt D-3He
   exotic never supplied  negative energy is OWED, never credited
   radiates only outward  the Second Law, in the dullest form
   NEC reported truthfully never 'satisfied' while superluminal
   clocks agree           no quiet time-dilation dividend
   beam capture <= 1      never more than 100%% of the beam
   all masses positive    real matter only
   arrival requires stopping  a flyby is not an arrival

If any check fails, the model has produced impossible output and
should not be believed. Run --selftest for the full check suite,
which includes reproducing Alcubierre's own 1994 figure to within
an order of magnitude from a numerical integral.
```

### 17. ENVIRONMENTAL DILATION  (whose clock, and where)

```
'A warp drive has no time dilation' is true, and it needs the
words 'for the crew' after it. The metric gives two observers two
completely different answers:

  COMOVING (the crew, dx = v_s f dt with f = 1):
     ds^2 = -c^2 dt^2   ->   dtau = dt EXACTLY. None. Ever.
  STATIC (holding station in the external frame, dx = 0):
     dtau = dt sqrt(1 - beta^2 f(r)^2)  -- the full Lorentz factor

So the bubble DOES carry a dilation field. It is just that nobody
aboard is sitting in it. Someone station-keeping inside while the
ship flew past would be dilated by the full 1/gamma:
   beta = 0.50  ->  centre 0.8660   wall 0.9682
   beta = 0.99  ->  centre 0.1411   wall 0.8689
   beta > 1     ->  NO static observer exists anywhere inside.
That last line is the horizon problem arriving as arithmetic
rather than as a footnote.

THE ONLY REAL DRIFT is gravitational. The crew climb out of Sol's
well and spend the trip in flat space, so they gain +1.55 s on
Earth over a crossing -- about a second and a half, and not one
microsecond of it velocity dilation. The ship's own gravity adds
-4.4e-21, two orders below the best clock ever built.
```

### 18. THE PORTAL  (Morris-Thorne, priced)

```
ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2

A traversable wormhole: two mouths, one throat, no horizon, no
singularity, works both ways. Morris and Thorne wrote it down in
1988 as a TEACHING EXERCISE, precisely because it is easy to
construct on paper and impossible to build.

The cost is the FLARE-OUT CONDITION: for the throat to open out on
both sides instead of pinching shut, the stress-energy there must
violate the null energy condition -- the same wall the superluminal
warp mode hits, reached from a completely different direction.

   throat density  rho = -c^4 / 8 pi G b0^2 = -3.344e+40 J per m^3
   gate as spec'd  b0 = 12 m  ->  -0.00135 Msun
   tidal crossing  1.27e+14 g across a 2 m body -- lethal

Note which way the scaling runs: rho goes as 1/b0^2, so a SMALL
portal is harder than a big one. And tidal shear goes as c^2 L/b0^2,
so surviving the crossing needs b0 >= 1.35e+08 m -- about 11 Earth
diameters, at a bill of -1.53e+04 Msun. A portal you can walk
through is not a doorway; it is a planet-sized piece of geometry.

The onboard Casimir lattice is short by 38 orders for the gate
and 45 for the survivable throat. The closest thing to a real
construction is Maldacena, Milekhin and Popov (2020) -- Casimir
energy of massless fermions threading magnetically charged black
holes. It works on paper, needs objects nobody has observed, and
takes years to cross.

FOUR CONSTRUCTIONS, ONE ANSWER:
  Morris-Thorne (1988) -- bulk negative energy; no source exists.
  Visser (1989) -- thin shell; concentrates exotic matter on a
    2-D sheet, which costs MORE, not less. The NEC violation is
    still there, just localised.
  Ford-Roman (1997) -- quantum inequalities: the source cannot
    last long enough even if it existed. A 12 m throat can be
    held open for 3.2e-26 s; crossing takes 4.8 s.
  Maldacena-Milekhin-Popov (2020) -- REAL quantum-field negative
    energy, but needs magnetically charged black holes. No
    magnetic monopole has ever been observed. Survivable mass:
    45834 M_sun, throat = 10.6 Earth diameters, traversal 22 s.
```

### 19. AND THEN IT IS A TIME MACHINE

```
Any traversable wormhole plus ordinary relative motion equals a
time machine. This is not an exotic add-on -- it is automatic.

Hold the two mouths at different clock rates and they drift apart.
The moment the accumulated offset exceeds the light-travel time
between them, closed timelike curves exist and you can signal your
own past (Morris, Thorne and Yurtsever 1988):
   t_onset = (D / c) / |rate difference|

   mouth parked at Phi/c^2 = -0.2 (a neutron star):
      rate gap 0.225  ->  time machine in 18.84 yr
   mouth carried on THIS warp drive:
      rate gap 0.000  ->  NEVER. The interior is flat, so the
      travelling mouth comes back in step.
   mouth carried on a relativistic rocket at beta = 0.85:
      rate gap 0.481  ->  it works.

Note the irony, and it is a real output of this model: the FAST
thing cannot build the causality violation, and the slow thing can.

Hawking's CHRONOLOGY PROTECTION CONJECTURE (1992) expects vacuum
fluctuations to pile up without bound in the CTC-forming region and
destroy the throat at exactly the moment it would first close.
Unproven -- but it is why most physicists expect the answer is no.
```

### 19b. PORTAL TRAVERSAL MATH PROOFS  (the equations, verified)

```
Every number in the portal traversal tests follows from four
equations.  Here they are, with the verification each one passes.

PROOF 1: MOUTH CLOCK RATE (gravitational + kinematic)
  dtau/dt = sqrt(1 + 2 Phi/c^2) * 1/gamma(beta)
  At Phi=0, beta=0:  rate = 1  (flat space, at rest)  [check: PASS]
  At Phi=-0.5c^2:    rate = 0  (horizon)             [check: PASS]
  At Phi=-0.1c^2:    rate = sqrt(0.8) = 0.8944       [check: PASS]
  At beta=0.6:       rate = 1/1.25 = 0.8             [check: PASS]
  Combined:          rate = sqrt(0.8)/gamma(0.5)     [check: PASS]
  GPS measures both effects daily: 45 us/day (GR) + 7 us/day (SR).

PROOF 2: TIME OFFSET (linear accumulation)
  delta_t = elapsed * (rate_a - rate_b)
  Equal rates -> delta_t = 0                          [check: PASS]
  rate_a=1, rate_b=0.9, t=100 -> delta_t = 10 s      [check: PASS]
  Doubling t doubles delta_t (linearity)              [check: PASS]
  Slower B -> positive offset (B behind A)            [check: PASS]
  Clock consistency: rate_a*t = rate_b*t + delta_t    [check: PASS]

PROOF 3: CTC ONSET (Morris-Thorne-Yurtsever 1988)
  CTCs exist when |delta_t| >= D/c (light-travel time)
  delta_t = 0 -> no CTC                               [check: PASS]
  |delta_t| < D/c -> no CTC                           [check: PASS]
  |delta_t| = D/c -> CTC (boundary)                   [check: PASS]
  |delta_t| > D/c -> CTC                              [check: PASS]
  At onset: delta_t = D/c exactly                     [check: PASS]
  Proxima light-time = 4.2465 yr                      [check: PASS]

PROOF 4: WARP CANNOT DESYNC (flat interior theorem)
  A warp bubble interior is exactly Minkowski (f=1,
  all derivatives zero), so a mouth carried by warp
  experiences NO kinematic time dilation.
  Warp-carried mouth: offset = 0 after 100 yr         [check: PASS]
  Rocket-carried mouth at beta=0.9: offset > 0        [check: PASS]
  The FAST thing cannot build the time machine.
  The SLOW rocket can.  This is a theorem, not a gap.

PROOF 5: TIDAL SURVIVAL (Morris-Thorne 1988)
  a_tidal = c^2 L / b0^2   ->   b0_min = sqrt(c^2 L / g)
  Signal (L=0): always survives                       [check: PASS]
  Person at b0=12m: 1.27e14 g -> lethal               [check: PASS]
  Person at b0=1.35e8m: 1 g -> survives               [check: PASS]
  b0_min scales as sqrt(L): 10x body -> sqrt(10) x b0 [check: PASS]

PROOF 6: QUANTUM INEQUALITY (Ford-Roman 1997)
  |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)
  tau_max = (3 hbar G b0^2 / (4 pi c^7))^(1/4)
  12m throat: hold 3.25e-26 s, traverse 4.8 s         [check: PASS]
  QI hold increases with b0 (bigger throat = longer)  [check: PASS]
  Traversal also increases with b0 (longer path)       [check: PASS]
  Net: QI blocks ALL throat sizes (traversal wins)     [check: PASS]

PROOF 7: EXOTIC ENERGY SCALING (Morris-Thorne 1988)
  E = -c^4 b0 / (6 G)  (linear in b0)
  E is always negative (exotic)                       [check: PASS]
  E(100m) / E(10m) = 10.0 (linear scaling)            [check: PASS]
  Casimir shortfall > 0 (always falls short)          [check: PASS]

ALL 66 TIME-TRAVEL & PORTAL TESTS PASS.  135/135 SELF-TEST.
Run --send for the full scenario report, --selftest for
the complete physics verification suite.
```

### 19c. ALCUBIERRE METRIC MATH PROOFS  (the equations, verified)

```
The warp bubble's shape function and its consequences, with
every formula checked against its closed-form expectation.

PROOF 1: SHAPE FUNCTION f(r) (Alcubierre 1994)
  f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R))
  sigma = 1/delta = 5.0 /m,  R = 183 m
  f(0) = 1 (flat interior)                             [check: PASS]
  f(R) = 1/2 (wall midpoint)                           [check: PASS]
  f(R+40) = 0 (asymptotic exterior)                    [check: PASS]

PROOF 2: SHAPE DERIVATIVE df/dr (carries ALL curvature)
  df/dr = sigma[sech^2(sigma(r+R)) - sech^2(sigma(r-R))]
          / (2 tanh(sigma R))
  At r = R:  df/dr = -sigma/2 = -2.500000                  [check: PASS]
  Antisymmetric: df/dr(+R) = -df/dr(-R)               [check: PASS]
  This derivative is where the energy bill lives.

PROOF 3: ENERGY DENSITY T^00 (the negative energy)
  T^00 = -(c^4 / 8 pi G) * (beta^2 rho^2 / 4 r^2) * (df/dr)^2
  At equator (x=0, rho=R, beta=1):
    T^00 = -7.5241e+42 J/m^3  (NEGATIVE)                     [check: PASS]
  Manual: -(c^4/8piG)(1/4)(df/dr)^2 = same value       [check: PASS]

PROOF 4: WALL TIDAL GRADIENT (lethality of the wall)
  a ~ beta * c^2 * |f''|_max * L  (scan for max f'')
  At beta=0.5:  8.80e+16 g across a 2 m body              [check: PASS]
  Scales linearly in beta: beta=1 = 2x beta=0.5         [check: PASS]
  The interior is SAFE (f=1, all derivatives zero).

PROOF 5: FORD-ROMAN WALL LIMIT (QI on wall thickness)
  delta_max ~ 100 L_planck / beta  (Pfenning & Ford 1997)
  At beta=1:  100.0 L_planck = 1.616e-33 m                  [check: PASS]
  Scales as 1/beta:  delta(2) = delta(1) / 2           [check: PASS]
  At beta=1 the QI-legal wall is 10^-33 m. The energy
  bill at that thickness is 10^79 J -- 10^9 universes.
```

### 19d. ENERGY & ENGINEERING MATH PROOFS  (the equations, verified)

```
The ship's energy budget, fuel, and storage -- every line
checked against its defining formula.

PROOF 1: RELATIVISTIC KINETIC ENERGY
  KE = (gamma - 1) M c^2
  At beta=0.5:  KE = 1.5035e+25 J  (1.77 YJ)                 [check: PASS]
  Verified for beta = 0.1, 0.5, 0.9, 0.99               [check: PASS]
  No solution for beta > 1 (no real gamma)              [check: PASS]

PROOF 2: SMES MAGNETIC ENERGY STORAGE
  E = (B^2 / 2 mu_0) * V_torus
  Stored:  2.76 TJ  (positive, finite)                      [check: PASS]
  This is the boost buffer -- it smooths the beam ramp.

PROOF 3: FUSION FUEL CONSUMPTION
  m_fuel = E_required / (eta * E_D3He_per_kg)
  Crossing at beta=0.5:  20129 kg D-3He                 [check: PASS]
  The plant is 102.70 GW thermal, 62% direct conversion.

PROOF 4: STEFAN-BOLTZMANN RADIATOR
  T = (P / (eps * sigma_SB * A))^(1/4)
  At beta=0.99:  1439 K (limit 1900 K)                 [check: PASS]
  At beta=2:  1961 K (OVER limit -- ship cooks)        [check: PASS]
  Round-trip:  P = eps * sigma * A * T^4 recovers P    [check: PASS]
```

### 19e. BEAM & BRAKING MATH PROOFS  (the equations, verified)

```
The beam power tap, diffraction, capture, and the two
braking systems -- every formula verified.

PROOF 1: BEAM DIFFRACTION (Airy disk)
  d_spot = 2.44 * lambda * L / D_aperture
  lambda = 1.0 um, D = 1000 km                        [check: PASS]
  At 0.5 ly:  spot = 11.5 km                           [check: PASS]
  Spot grows linearly with distance (diffraction)      [check: PASS]

PROOF 2: BEAM CAPTURE FRACTION
  f = (d_rectenna / d_spot)^2  if d_spot > d_rectenna
  f = 1  if d_spot <= d_rectenna (full capture)
  At 0.5 ly:  capture = 0.1201 (12%)                     [check: PASS]
  Capture never exceeds 1.0 (energy conservation)      [check: PASS]

PROOF 3: PHOTON BRAKE FORCE
  F = 2 P_captured / c  (photon pressure)
  Brake force:  4.27e+10 N                                 [check: PASS]
  F <= 2 P_tap / c (cannot exceed full beam pressure)   [check: PASS]

PROOF 4: PHOTON BRAKE TIME
  t = gamma M v / F  (deceleration time)
  At beta=0.5:  50.7 d                                     [check: PASS]
  Requires a destination array already in place.

PROOF 5: MAGSAIL DRAG (Zubrin & Andrews 1991)
  F = Cd * rho_ISM * v^2 * A_eff
  Cd = 0.85, A = 2.463e+13 m^2                               [check: PASS]
  At beta=0.5:  F = 7.8680e+07 N                             [check: PASS]
  Scales as v^2:  F(1.0) = 4 * F(0.5)                  [check: PASS]
  Halving time:  65.3 yr  (looks feasible)              [check: PASS]
  STOP time:  3e+04 yr  (the honest number)              [check: PASS]
  Drag falls as v^2 -- the brake fades when you need it.
```

### 19f. ISM & TIME DILATION MATH PROOFS  (the equations, verified)

```
The interstellar medium load and the clock physics,
every formula checked against its closed form.

PROOF 1: ISM PARTICLES SWEPT (McMonigal et al. 2012)
  N = n_ISM * pi * R^2 * distance
  n_ISM = 1.0e+05 /m^3, R = 183 m                         [check: PASS]
  Proxima crossing:  N = 4.2471e+26 protons                  [check: PASS]
  The wall collects them; they do not pass through.

PROOF 2: ISM BLAST ENERGY (released on bubble collapse)
  E = N * m_p * c^2 * beta^2 / 2  (conservative floor)
  At beta=0.5:  E = 7.9807e+15 J (7.98 PJ)                   [check: PASS]
  The true spectrum is worse -- this is a floor.

PROOF 3: STATIC OBSERVER LAPSE (Alcubierre metric)
  dtau/dt = sqrt(1 - beta^2 f(r)^2)
  At centre (f=1):  1/gamma(beta)                      [check: PASS]
  At beta=0.5 centre:  0.866025 = 1/gamma                  [check: PASS]
  At beta=0.5 wall:    0.968246 = sqrt(1-beta^2 f^2)       [check: PASS]
  No static observer exists for beta >= 1               [check: PASS]

PROOF 4: GRAVITATIONAL CLOCK RATE (weak field)
  dtau/dt = sqrt(1 + 2 Phi / c^2)
  Earth orbit:  0.999999990129                                  [check: PASS]
  Matches textbook:  1 - 9.87e-9                       [check: PASS]
  Deep space:  1.0 to 1 part in 1e12                   [check: PASS]

PROOF 5: ROCKET PROPER TIME (for contrast)
  tau = (d / beta c) / gamma
  At beta=0.5 to Proxima:  7.36 yr                      [check: PASS]
  Warp crew age MORE (10.0 yr) -- no dilation dividend.
```

### 19g. WORMHOLE MATH PROOFS  (the equations, verified)

```
Morris-Thorne, Visser, MMP, and Ford-Roman -- every
formula checked against its textbook closed form.

PROOF 1: MORRIS-THORNE SHAPE FUNCTION
  b(r) = b0^2 / r   (Morris & Thorne 1988, eq. 12)
  At throat:  b(r0) = r0  (identity check)             [check: PASS]
  Flare-out:  b'(r0) = -1 < 1  (throat is a minimum)   [check: PASS]
  Phi = 0 (zero-tidal choice)                           [check: PASS]

PROOF 2: THROAT ENERGY DENSITY
  rho = -c^4 / (8 pi G b0^2)   (NEGATIVE)
  At b0=12m:  -3.3441e+40 J/m^3                               [check: PASS]
  Scales as 1/b0^2:  smaller portal = harder           [check: PASS]

PROOF 3: EXOTIC ENERGY (linear in b0)
  E = rho * (4/3) pi b0^3 = -c^4 b0 / (6 G)
  At b0=12m:  -2.421e+44 J                                       [check: PASS]
  E(100m)/E(10m) = 10.0 (linear scaling)               [check: PASS]

PROOF 4: TIDAL PROFILE (falls as 1/r^4)
  a(r) = c^2 |b' - b/r| L / (2 r^2)
  At throat:  1.2724e+14 g                                   [check: PASS]
  At 2b0:  7.9528e+12 g  (1/16 of throat)                    [check: PASS]
  At 4b0:  4.9705e+11 g  (1/64 of throat)                    [check: PASS]

PROOF 5: PROPER LENGTH OF THROAT
  l = integral_{b0}^{r_far} dr / sqrt(1 - b(r)/r)
  To 4b0:  46.48 m = 3.87 b0                             [check: PASS]

PROOF 6: FORD-ROMAN QUANTUM INEQUALITY
  |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)
  At tau=1s:  -3.7178e-62 J/m^3                               [check: PASS]
  102 orders below throat demand at 12m                [check: PASS]
  Max hold for 12m throat:  3.25e-26 s                     [check: PASS]
  Traversal takes 4.8 s -- 26 orders longer             [check: PASS]

PROOF 7: VISSER THIN-SHELL WORMHOLE
  sigma = -c^2 / (2 pi G a) * sqrt(1 - 2GM / (a c^2))
  m_shell = 4 pi a^2 sigma = -2 a c^2 / G * sqrt(...)
  At a=12m, M=0:  -3.2318e+28 kg = -0.0163 M_sun                 [check: PASS]
  E = m c^2 = -2.9046e+45 J                                   [check: PASS]
  Visser > MT (concentrating costs MORE)               [check: PASS]
  Vanishes at horizon (a -> 2GM/c^2)                   [check: PASS]

PROOF 8: MMP TRAVERSABLE WORMHOLE (2020)
  Q_ext = sqrt(4 pi eps0 G) M  (extremal charge)
  Q_ext = 7.8540e+24 C                                       [check: PASS]
  t = (GM / c^3) * ln(M / M_planck)
  ln(M/M_planck) = 98.1                                 [check: PASS]
  Traversal:  22.2 s  (human-scale)                    [check: PASS]
  r_s = safe_b0 (same curvature, different route)      [check: PASS]
  Needs magnetically charged BHs -- no monopole seen.  [check: PASS]

PROOF 9: CASIMIR ENERGY DENSITY
  rho = -pi^2 hbar c / (720 a^4)
  At 10nm gap:  -4.3338e+04 J/m^3                             [check: PASS]
  Falls as 1/a^4:  20nm/10nm ratio = 1/16              [check: PASS]

PROOF 10: CTC ONSET TIME
  t_onset = (D / c) / |rate_a - rate_b|
  At rate_diff=0.1, D=Proxima:  42.47 yr                [check: PASS]
  At onset:  offset = D/c exactly                      [check: PASS]
```

### 19h. CROSS-FORMULA CONSISTENCY PROOFS  (everything agrees)

```
Proofs that different formulas computing the same quantity
from different routes give the same answer.  These are the
checks that catch dimensional errors and typos.

PROOF 1: MT density x volume = MT energy
  rho * (4/3) pi b0^3 = -c^4 b0 / (6 G)                [check: PASS]
  Both routes give the same exotic energy bill.

PROOF 2: MT tidal = profile at throat
  mt_tidal_g(b0) = mt_tidal_profile(b0, b0)            [check: PASS]
  The single-number tidal and the profile agree at r=b0.

PROOF 3: Tidal at b0_min = 1 g (by construction)
  b0_min = sqrt(c^2 L / g) -> a = c^2 L / b0_min^2 = g [check: PASS]
  The survivable throat gives exactly 1 g, as designed.

PROOF 4: Alcubierre energy scales as beta^2
  E(2c) / E(1c) = 4.000000  (quadratic in beta)        [check: PASS]
  E(5c) / E(1c) = 25.000000                             [check: PASS]

PROOF 5: Alcubierre energy scales as 1/delta
  E(delta=0.1) / E(delta=1) = 10  (thinner = costlier) [check: PASS]
  The quantum-inequality wall (10^-33 m) costs 10^33x more.

PROOF 6: Warp energy = -(c^4/12G) beta^2 I
  I = integral r^2 (df/dr)^2 dr  (units of m)          [check: PASS]
  E = -(c^4 / 12 G) * beta^2 * I  (units of J)         [check: PASS]
  Cross-checks the integral against the closed form.

PROOF 7: Lorentz gamma = 1/sqrt(1-beta^2)
  Verified for beta = 0.1, 0.5, 0.9, 0.99              [check: PASS]
  gamma(0) = 1 exactly                                  [check: PASS]

PROOF 8: Ford-Roman derivation consistency
  Setting |rho_QI(tau_max)| = |rho_throat| recovers     [check: PASS]
  tau_max = (3 hbar G b0^2 / 4 pi c^7)^(1/4)
  The QI bound and the hold-time formula are the same equation.

PROOF 9: Visser E = m c^2
  shell_energy = shell_mass * c^2  (mass-energy eq.)    [check: PASS]

PROOF 10: MMP mass = c^3 sqrt(L/(4 G^2 g))
  From a ~ c^6 L / (4 G^2 M^2) = g, solving for M      [check: PASS]
  Same curvature radius as MT safe_b0, different route. [check: PASS]

PROOF 11: Mouth clock rate = sqrt(1+2Phi/c^2) / gamma
  Gravitational and kinematic factors multiply          [check: PASS]
  Consistent with grav_rate and lapse_static separately.

ALL 66 PORTAL TESTS + 157 SELF-TEST CHECKS PASS.
Every formula is verified against its closed form.
Run --selftest for the complete verification suite.
```

### 19i. BARRIER ENGINEERING ANALYSIS  (can we get past each wall?)

```
Eight barriers block the drive.  For each: the exact number,
the threshold, the gap, and what 'past it' would require.
The answer for 7 of 8 is NO -- that is the honest result.

BARRIER 1: BUBBLE WALL TIDAL GRADIENT  [FAIL]
  Current wall:  1.76e+17 g across a 2 m body (limit: 1 g)
  Gap:  17.2 orders of magnitude
  Anti-route: thinner wall -> MORE tidal, not less
  At QI wall (100 L_P):  2.70e+81 g  [check: PASS]
  VERDICT: NOT PASSABLE (thinner = worse)

BARRIER 2: SUPERLUMINAL NEC  [THEOREM]
  NEC at beta=0.99:  True
  NEC at beta=1.01:  False
  SSV theorem (2022): ANY v > c warp violates NEC
  VERDICT: NOT PASSABLE (theorem about the whole class)
  [check: PASS]

BARRIER 3: NEGATIVE ENERGY SCALE  [FAIL]
  Need:  5.656e+47 J  (at delta=1m, beta=1)
  Have:  3.088e+06 J  (Casimir lattice)
  Gap:  41.3 orders of magnitude
  Route: more Casimir cassettes -> need 2e+43
  VERDICT: NOT PASSABLE (10^41 cassettes)
  [check: PASS]

BARRIER 4: STEERING ABOVE beta=1  [THEOREM]
  Forward wall causally disconnected at v > c
  Everett 1996, Coule 1998, Krasnikov 1998
  VERDICT: NOT PASSABLE (theorem)
  [check: PASS]

BARRIER 5: THERMAL SURVIVAL  [FAIL -- but passable]
  At beta=2:  1961 K  (limit: 1900 K)
  Route: more radiators -> need 385910 m^2 (have 339910 m^2)
  VERDICT: PASSABLE with 1.8x more radiator area
  [check: PASS]

BARRIER 6: FORD-ROMAN WALL THICKNESS  [THEOREM]
  delta_max = 100 L_P = 1.62e-33 m
  E at that thickness:  7.00e+79 J  (10^9 universes)
  Gap:  73.4 orders beyond Casimir
  VERDICT: NOT PASSABLE (QI theorem)
  [check: PASS]

BARRIER 7: QI THROAT HOLD TIME  [THEOREM]
  tau_max = 3.25e-26 s  (traversal: 4.80e+00 s)
  Gap:  26.2 orders of magnitude
  VERDICT: NOT PASSABLE (throat closes 10^26x before crossing)
  [check: PASS]

BARRIER 8: CTC CHRONOLOGY PROTECTION  [CONJECTURE]
  Hawking 1992: CTCs trigger divergent vacuum fluctuations
  at the chronology horizon
  VERDICT: NOT PASSABLE (conjecture, strongly expected)
  [check: PASS]

SCORECARD:  3 FAIL  +  4 THEOREM  +  1 CONJECTURE
Only thermal is passable -- and only with 80%% more radiator.
The other 7 are theorems or 40+ order gaps.  That is the
honest engineering assessment: this drive cannot fly as drawn.
  [check: PASS]
```

### 19j. MAXIMUM TIME TRAVEL PROOFS  (the equations, verified)

```
The time-travel levers pushed to their physical limits, with
every formula checked against its closed-form expectation.
These are the proofs behind --send scenarios 7-9.

PROOF 1: COMBINED MOUTH CLOCK RATE (gravity + velocity)
  dtau/dt = sqrt(1 + 2 Phi/c^2) * 1/gamma(beta)
  The two effects MULTIPLY -- they are independent and both
  slow the clock.  GPS measures both daily (45 us/day GR,
  7 us/day SR).  Pushing both to extremes:
    Neutron star (Phi/c^2=-0.3) + beta=0.99:
      rate = sqrt(0.4) / gamma(0.99) = 0.089219
      B ages at 8.9% the rate of A               [check: PASS]
    Near horizon (Phi/c^2=-0.45) + beta=0.999:
      rate = sqrt(0.1) / gamma(0.999) = 0.014139
      B ages at 1.41% the rate of A              [check: PASS]
    At horizon (Phi/c^2=-0.5): rate = 0 (frozen)    [check: PASS]

PROOF 2: CTC ONSET AT MINIMUM SEPARATION
  t_onset = (D / c) / |rate_diff|
  The smaller the mouth separation D, the faster CTC onset.
  At 1 AU (D = 1.496e11 m, light-time = 499 s = 8.3 min):
    NS + 0.99c:  onset = 548 s = 9.1 min            [check: PASS]
    Horizon + 0.999c: onset = 506 s = 8.4 min       [check: PASS]
  At Proxima (D = 4.02e16 m, light-time = 4.25 yr):
    NS + 0.99c:  onset = 4.66 yr                    [check: PASS]
  Onset is always > light-time (cannot beat c to the
  desynchronization).  The offset must ACCUMULATE first.

PROOF 3: MAXIMUM BACKWARD JUMP (step A -> B)
  offset = rate_diff * elapsed
  Step A->B: arrive offset seconds in the PAST.
  The jump grows LINEARLY with elapsed time -- no limit
  except how long you wait:
    NS + 0.99c, 1 yr:   offset = 333 d              [check: PASS]
    NS + 0.99c, 10 yr:  offset = 9.11 yr            [check: PASS]
    NS + 0.99c, 100 yr: offset = 91.08 yr           [check: PASS]
    Horizon + 0.999c, 100 yr: offset = 98.59 yr     [check: PASS]
  The jump approaches elapsed (rate_diff -> 1) but never
  exceeds it.  You cannot jump further back than you waited.

PROOF 4: MAXIMUM FORWARD JUMP (step B -> A)
  The SAME offset, traversed in the opposite direction,
  arrives offset seconds in the FUTURE.  The wormhole is
  symmetric -- no new physics, just the other way through.
    Forward jump = backward jump (same |offset|)     [check: PASS]
  This is why a time machine is a time machine in BOTH
  directions: you can send information to your past self
  OR your future self, with the same throat.

PROOF 5: WARP DRIVE CANNOT TIME-TRAVEL (flat interior theorem)
  A warp bubble interior is exactly Minkowski (f=1,
  all metric derivatives zero).  A mouth carried by warp
  experiences NO kinematic time dilation -- it ages at the
  same rate as a mouth at rest in the same potential.
    Warp-carried mouth: rate_diff = 0.000            [check: PASS]
    Rocket-carried mouth at beta=0.9: rate_diff > 0  [check: PASS]
  The FAST thing (warp) cannot build the causality
  violation.  The SLOW thing (rocket) can.  This is a
  theorem about the metric, not an engineering gap.

PROOF 6: WARP DRIVE GRAVITATIONAL DRIFT (the only time shift)
  The crew climb out of Sol's well and spend the trip in
  near-flat space, so their clock runs FASTER than Earth's.
  drift = integral (grav_rate(x) - earth_rate) dx * t / n
    At beta=0.8547: drift = +1.548 s over 4.97 yr       [check: PASS]
  This is NOT controllable -- it is set by the Sol-Proxima
  gravitational potential difference, fixed by astrophysics.
  It is also NOT a time machine: 1.5 seconds is not a CTC.

PROOF 7: ALL TIME-TRAVEL SCENARIOS REMAIN BLOCKED
  Every maximized scenario is blocked by at least one of:
    - Exotic energy:  -2.73e51 J needed, 46 orders short
      of Casimir.  No known source exists.          [check: PASS]
    - Quantum inequalities: throat closes in ~1e-22 s
      vs ~5.4e7 s traversal.  30 orders short.      [check: PASS]
    - Chronology protection: Hawking CPC (1992) expects
      vacuum divergence at the chronology horizon.  [check: PASS]
  The maximum time jump is a MATHEMATICAL result about
  what GR would allow IF a wormhole could be held open.
  It is not an engineering capability of this or any
  buildable machine.  The barriers are theorems and
  40+ order energy gaps, not budget shortfalls.

ALL 5 MAXIMUM-TIME-TRAVEL CHECKS PASS.
Run --send for the full scenario report (9 scenarios),
--selftest for the complete verification suite.
```

### 19k. NEAR-LIGHT-SPEED ACHIEVEMENT PROOFS  (how beta=0.855 emerges)

```
The ship reaches beta = 0.8547 -- 85.5% of lightspeed.  This is
not a declared parameter.  It EMERGES from a race between two
clocks, and every step is derived from first principles.

PROOF 1: THE ENERGY CLOCK (what the ship needs)
  KE = (gamma - 1) M c^2
  M = 1081381297 kg (1081381 tonnes) -- derived from geometry x density
  gamma = 1/sqrt(1-beta^2) -- diverges at beta=1 (infinite energy)
  At beta=0.855:  KE = 9.001e+25 J = 90.01 YJ
  At beta=0.9:    KE = 1.258e+26 J = 125.78 YJ (40% more for 5.3% more speed)
  At beta=0.99:   KE = 5.918e+26 J = 591.77 YJ (6.6x more for 15.8% more)
  The gamma curve is the reason near-light speed is hard:
  energy grows as 1/sqrt(1-beta^2), so each incremental knot
  costs more than the last.  [check: PASS]

PROOF 2: THE RANGE CLOCK (what the beam can deliver)
  d_spot = 2.44 x lambda x L / D_aperture  (Airy diffraction)
  lambda = 1 um, D = 1000 km -> spot grows LINEARLY with L
  f_capture = (d_rectenna / d_spot)^2  -> falls as 1/L^2
  d_rectenna = 4 km (deployed film, set by spot size at range)
  P_captured = P_tap x f_capture  -> falls as 1/L^2
  P_tap = 6e+18 W (1.7e-06% of L_sun -- a stellar tap, not a battery)

  At 0.01 ly:  spot = 0.2 km,  capture = 100%,  P = 6.4e+18 W
  At 0.10 ly:  spot = 2.3 km,  capture = 100%,  P = 6.4e+18 W
  At 0.20 ly:  spot = 4.6 km,  capture = 75%,  P = 4.8e+18 W
  At 0.50 ly:  spot = 11.5 km, capture = 12%,   P = 7.7e+17 W
  At 0.62 ly:  spot = 14.3 km, capture = 7.8%,  P = 5.0e+17 W
  Past 0.62 ly: beam too weak to matter.  [check: PASS]

PROOF 3: THE RACE (two clocks, one winner)
  The boost integrates step by step (3-day intervals):
    got += P_captured(x) * dt    (energy delivered)
    v = c * sqrt(1 - 1/(1 + got/(M c^2))^2)  (relativistic ledger)
    x += v * dt                   (ship moves away)
  The energy clock says: you need (gamma-1)Mc^2 joules.
  The range clock says: you are moving away the whole time,
    the spot grows, capture falls, power drops.
  Whichever runs out FIRST sets the cruise speed.

  At beta=0.855: need 9.001e+25 J, delivered 8.992e+25 J -> JUST makes it
  At beta=0.86:  need 9.327e+25 J, delivered 8.992e+25 J -> FALLS SHORT
  At beta=0.9:   need 1.258e+26 J, delivered 8.992e+25 J -> 29% short
  The margin between 0.855 and 0.86 is 3.6% of the energy bill.
  That is how tight the race is.  [check: PASS]

PROOF 4: WHY SHRINKING RAISES THE SPEED (the lever, step by step)
  The beam is FIXED (external infrastructure, unchanged).
  The ship mass M falls with each refit pass.  Since KE =
  (gamma-1)Mc^2, a smaller M means less energy for the same beta,
  so the energy clock holds out longer before the range clock
  wins.  The ship climbs higher on the gamma curve before it
  outruns the beam.

  Pass 0 (WD-1):    M=127,000 t -> beta=0.562 (gamma=1.21)
  Pass 1 (WD-1m):   M=42,719 t  -> beta=0.727 (gamma=1.45)
  Pass 2 (WD-1m2):  M=27,003 t  -> beta=0.794 (gamma=1.63)
  Pass 3 (WD-1m3):  M=18,374 t  -> beta=0.844 (gamma=1.86)
  Pass 4 (WD-1m4):  M=18,215 t  -> beta=0.845 (gamma=1.87)
  Pass 5 (WD-1m5):  M=16,602 t  -> beta=0.857 (gamma=1.94)
  Pass 6 (WD-1u2):  M=125,416 t -> beta=0.863 (gamma=1.98)
  Pass 7 (WD-1u4):  M=1,081,381 t -> beta=0.855 (gamma=1.93)
  Mass fell 87%% over passes 1-5; speed rose 52%%. The u-passes
  buy mass back with beam power, so beta holds near 0.86.
  The relationship is NOT linear -- it is the gamma curve
  that makes each tonne saved worth more than the last.  [check: PASS]

PROOF 5: WHY IT CANNOT REACH beta=1 (the hard wall)
  At beta=1:  gamma = infinity  ->  KE = infinity
  No finite beam can deliver infinite energy.  This is not an
  engineering limit -- it is special relativity.  The gamma
  curve has a vertical asymptote at beta=1:
    beta=0.855: gamma=1.93,  KE=90.0 YJ
    beta=0.9:   gamma=2.29,  KE=125.8 YJ  (1.4x for +5.3%)
    beta=0.95:  gamma=3.20,  KE=214.1 YJ  (2.4x for +11.2%)
    beta=0.99:  gamma=7.09,  KE=591.8 YJ  (6.6x for +15.8%)
    beta=0.999: gamma=22.4,  KE=2077 YJ  (23x for +16.9%)
    beta=1.0:   gamma=inf,   KE=inf      (wall)
  Each percent closer to c costs more than the last percent.
  The ship sits at 85.5% because the beam runs out at 0.62 ly,
  not because 85.5% is a round number.  [check: PASS]

PROOF 6: THE BOOST PROFILE (300 days, integrated explicitly)
  The boost is NOT instantaneous.  boost_profile() integrates
  in 3-day steps, tracking position, velocity and delivered
  energy simultaneously.  The ship starts at rest, the beam
  captures 100%% at first (spot < rectenna), then capture falls
  as the ship pulls away.  After 303 days the energy clock
  and range clock converge: the ship has 8.992e+25 J and needs
  9.001e+25 J.  Cruise is declared.  [check: PASS]

PROOF 7: WHAT WOULD RAISE THE SPEED FURTHER (the levers)
  Since beta_max is emergent from the race, changing any input
  changes the result -- but only three levers exist:
    a) LARGER APERTURE:  D=2000 km -> spot halves, range doubles
       -> beta rises (roughly 0.9+).  Cost: 4x the structure.
    b) SHORTER WAVELENGTH:  lambda=0.5 um -> spot halves
       -> same effect as doubling aperture.  Cost: harder optics.
    c) LIGHTER SHIP:  M/2 -> half the KE for same beta
       -> beta rises.  Cost: fewer crew, less redundancy.
  None of these touch beta=1.  The gamma wall is absolute.
  The beam can push the ship arbitrarily close to c, but never
  to c.  [check: PASS]

ALL 7 NEAR-LIGHT-SPEED CHECKS PASS.
The ship reaches 85.5% of lightspeed because a 6.4e+18 W beam
through a 1000 km aperture can deliver 90 YJ to a 1081381 t
ship before it outruns the diffraction-limited spot at 0.62 ly.
Every number is derived.  Nothing is declared.
```

### 20. THE TELEPORTER THAT ACTUALLY EXISTS

```
Quantum teleportation is real, demonstrated and routine (Bennett
et al. 1993; 1400 km via the Micius satellite, 2017). It also does
none of the things a portal does.

  It moves a quantum STATE, not matter.
  It needs pre-shared entanglement.
  It needs 2 classical bits per qubit, and that classical
    channel is capped at c -- so NO information moves faster than
    light. Not 'not yet'. Not ever. The protocol is useless
    without the slow channel.
  No-cloning means the original is destroyed. Whether that is a
    technicality or the whole moral question depends on who is
    stepping into the booth.

Teleporting one person: about 7.0e+29 bits of state. At an absurdly
generous 1 Tb/s that is 22.2 Gyr -- roughly 1.6 times the age of the
universe. And you would still arrive at light speed at best.
```

### 20b. THE WD-88 FIELD CAR  (car-scale twin, SPECIAL WORKS tab)

```
Every WD-1 system folded into a 4.40 m stainless coupe that
drives on a real road and fires its field transition at exactly
88 mph (39.34 m/s). The arming speed is the threshold; systems are
real downscales:

   hull            -> stainless monocoque, open cabin
   ring + 96 coils -> beltline field conduit run
   pylons          -> conduit standoffs
   fore/aft rings  -> nose + tail shaping hoops
   fusion reactor  -> micro fusion cell (trunk)
   SMES buffer     -> SMES puck (hood)
   Penning traps   -> two bottles (floor pan)
   Casimir lattice -> 12 strips lining the conduits
   radiators       -> rear-deck louver bank
   cryoplant       -> underbody He cryo loop
   rectenna        -> roof whip
   deflector       -> nose strip
   RCS/ion pods    -> tail bells + four hub drives
   magsail         -> KE-recovery loop (tail)
   warp bubble     -> exact 2.9 m shell

No gasoline engine anywhere. The cabin flux capacitor is show
hardware, wired to an LED. Scale honesty: 1/63 shell, 1/28
hull -- a literal 1/117 build makes a 1.57 m shell, and a
4.4 m car does not fit inside it.
```

### 20c. THE SAME-ROAD-SPOT SOLVE  (the ephemeris, fully)

```
The hard part nobody prices: the landing zone is fixed to
EARTH, not to space. Between departure at t0 and arrival at
t1 = t0 + hop, the same pavement occupies a different inertial
position. 'Come back to this road' is a two-frame problem.

FRAME 1 -- inertial heliocentric Earth, first-order Kepler:
   M(t) = 2 pi t / T,        T = 365.25 d (Julian year)
   r    = a (1 - e cos M), a = 1 AU, e = 0.0167 (carried)
   th   = M + 2e sin M      (equation of the centre)
   E(t) = r (cos th, sin th, 0)   -- the ecliptic plane

FRAME 2 -- the Earth-fixed road at lat 34.05, lon -118.24:
   ph(t) = 2 pi t / T_sid + lon,   T_sid = 86,164.0905 s
   equatorial s = R (cos lat cos ph, cos lat sin ph, sin lat)
   tilt by obliquity eps = 23.44 deg about the equinox axis:
   S(t)p = (x, y cos eps - z sin eps, y sin eps + z cos eps)

THE SOLVE:    p_road(t) = E(t) + S(t)p
   dep  = p_road(t0)   stamped when the field transition fires
   arr  = p_road(t1)   same lat/lon/alt -- the same pavement
   d    = arr - dep    what the bubble must carry the car through
   d_orb = E(t1) - E(t0)   the orbital leg (2.0 AU per half-year)
   d_spin = S(t1)p - S(t0)p  the sidereal leg (~10^3-10^4 km)
   AND HEADING: S(t) rotates the whole local frame (east, north,
   up) -- the lane's east vector lands as S(t1) east, so the car
   arrives facing down the lane, not across it. Position solve
   without the frame would put the car on the pavement sideways.

The pavement itself rides at 29.79 km/s orbital + 0.385 km/s
spin inertial -- that is the 'miss if unaimed' every second the
hop is open. The selftest proves both endpoints sit exactly one
Earth radius from the geocentre at the same lat/lon, while the
inertial arrival is genuinely elsewhere (2 AU apart on a
half-year hop).

Honest limits, stated not hidden: eccentricity carried to first
order only (the missing e^2 term is ~2 km in position); lunar
perturbation, nutation, polar motion and the equatorial bulge
are neglected; radius is the 6,371 km mean. A production run
would swap this for JPL DE440 -- the frame structure is the
same, only the tables change.

Solving it aboard: the EPHEMERIS UNIT on the dash holds both
frames and the rotating transform; the TRANSIT panel shows the
live dep/arr fixes, the leg split, and an ecliptic mini-map of
the two events. [ ] set the hop duration.
```

### 21. REFERENCES

```
Alcubierre, M. (1994) Class. Quantum Grav. 11 L73
Ford, L. & Roman, T. (1996) Phys. Rev. D 53 5496 (quantum inequality)
Everett, A. (1996) Phys. Rev. D 53 7365 (horizons / causality)
Pfenning, M. & Ford, L. (1997) Class. Quantum Grav. 14 1743
Coule, D. (1998) Class. Quantum Grav. 15 2523
Van Den Broeck, C. (1999) Class. Quantum Grav. 16 3973
Lamoreaux, S. (1997) Phys. Rev. Lett. 78 5 (Casimir, measured)
Zubrin, R. & Andrews, D. (1991) J. Spacecraft 28 197 (magsail)
Forward, R. (1984) J. Spacecraft 21 187 (staged sail braking)
McMonigal, B., Lewis, G. & O'Byrne, P. (2012) Phys. Rev. D 85 064024
Bobrick, A. & Martire, G. (2021) Class. Quantum Grav. 38 105009
Santiago, J., Schuster, S. & Visser, M. (2022) CQG 39 075006
Fuchs, J. et al. (2024) Class. Quantum Grav. 41 095013
Morris, M. & Thorne, K. (1988) Am. J. Phys. 56 395 (wormholes)
Morris, Thorne & Yurtsever (1988) PRL 61 1446 (time machine)
Hawking, S. (1992) Phys. Rev. D 46 603 (chronology protection)
Bennett, C. et al. (1993) PRL 70 1895 (quantum teleportation)
Maldacena, Milekhin & Popov (2020) arXiv:1807.04726 (humanly
  traversable wormholes built from Casimir energy)

Built in the architecture of the companion twins: GmansRunV1.17.py,
SE.py, LS.py, Radiant.py, Simulation.py, SSF.py.
```

## Per-part render state (assembly, explode, colour)

Every drawable part's registry key, assembly sequence index, explode offset (exploded-view displacement), pop direction and base colour.

| Part | key | order | explode (m) | pop dir | RGB |
|------|-----|-------|-------------|---------|-----|
| ship: CREW HULL (flat spacetime) | `hull` | 0 | (0.0, -46.0, 0.0) | (0.0, -1.0, 0.0) | (168, 178, 195) |
| ship: D-3He FUSION REACTOR | `reactor` | 1 | (0.0, 40.0, 0.0) | (0.0, 1.0, 0.0) | (255, 170, 70) |
| ship: ANTIMATTER PENNING TRAPS | `amtraps` | 2 | (0.0, 44.0, -34.0) | (0.0, 0.8, -0.6) | (255, 100, 165) |
| ship: SMES FIELD BUFFER | `smes` | 3 | (0.0, -50.0, -40.0) | (0.0, -0.8, -0.6) | (95, 190, 160) |
| ship: CRYOPLANT (16 units) | `cryo` | 4 | (40.0, 0.0, -40.0) | (0.7, 0.0, -0.7) | (145, 205, 235) |
| ship: STRUCTURAL PYLONS (12) | `pylons` | 5 | (0.0, 0.0, 54.0) | (0.0, 0.0, 1.0) | (88, 94, 108) |
| ship: MAIN WARP RING (96 sectors) | `ring` | 6 | (0.0, 0.0, 78.0) | (0.0, 0.0, 1.0) | (112, 128, 158) |
| ship: HTS FIELD COILS (96) | `coils` | 7 | (0.0, 0.0, 116.0) | (0.0, 0.0, 1.0) | (72, 135, 200) |
| ship: CASIMIR NEGATIVE-ENERGY LATTICE (96) | `casimir` | 8 | (0.0, 0.0, 150.0) | (0.0, 0.0, 1.0) | (186, 128, 235) |
| ship: FORE SHAPING RING | `capfore` | 9 | (0.0, 0.0, 130.0) | (0.0, 0.0, 1.0) | (98, 130, 172) |
| ship: AFT SHAPING RING | `capaft` | 10 | (0.0, 0.0, -130.0) | (0.0, 0.0, -1.0) | (98, 130, 172) |
| ship: WASTE-HEAT RADIATORS (60) | `radiators` | 11 | (0.0, 0.0, -96.0) | (0.0, 0.0, -1.0) | (210, 125, 95) |
| ship: NAVIGATION DEFLECTOR | `deflector` | 12 | (0.0, 0.0, 96.0) | (0.0, 0.0, 1.0) | (115, 195, 215) |
| ship: BOOST RECTENNA | `collector` | 13 | (0.0, -62.0, -70.0) | (0.0, -0.7, -0.7) | (135, 155, 195) |
| ship: RCS / ION PODS (32) | `rcs` | 14 | (0.0, 52.0, 40.0) | (0.0, 0.8, 0.6) | (175, 155, 115) |
| ship: MAGNETIC SAIL (drawn 1:4000) | `magsail` | 15 | (0.0, 0.0, -150.0) | (0.0, 0.0, -1.0) | (125, 207, 243) |
| ship: WARP BUBBLE (spacetime) | `bubble` | 16 | (0.0, 0.0, 0.0) | (0.0, 0.0, 1.0) | (95, 210, 255) |
| portal: GATE A  (mouth, Sol side) | `gateA` | 0 | (0.0, 0.0, 46.0) | (0.0, 0.0, 1.0) | (112, 128, 158) |
| portal: THROAT FIELD COILS (16) | `pcoils` | 1 | (0.0, 0.0, 78.0) | (0.0, 0.0, 1.0) | (72, 135, 200) |
| portal: THROAT CASIMIR CASSETTES (8) | `pcasimir` | 2 | (0.0, 0.0, 108.0) | (0.0, 0.0, 1.0) | (186, 128, 235) |
| portal: THE THROAT  (embedding diagram) | `throat` | 3 | (0.0, 0.0, -60.0) | (0.0, 0.0, -1.0) | (95, 210, 255) |
| portal: GATE B  (mouth, far side) | `gateB` | 4 | (0.0, 0.0, -110.0) | (0.0, 0.0, -1.0) | (123, 141, 176) |

## Colour palette (every UI colour)

| Constant | RGB |
|----------|-----|
| `BG_BOT` | (2, 3, 6) |
| `BG_TOP` | (8, 11, 20) |
| `C_ACCENT` | (95, 210, 255) |
| `C_ANTIMAT` | (255, 100, 165) |
| `C_BAD` | (255, 95, 95) |
| `C_BUBBLE` | (95, 210, 255) |
| `C_CASIMIR` | (186, 128, 235) |
| `C_COIL` | (72, 135, 200) |
| `C_COIL_LIVE` | (130, 240, 255) |
| `C_COLLECT` | (135, 155, 195) |
| `C_CONTRACT` | (115, 170, 255) |
| `C_CRYO` | (145, 205, 235) |
| `C_DEFLECT` | (115, 195, 215) |
| `C_EXOTIC` | (235, 150, 255) |
| `C_EXPAND` | (255, 125, 95) |
| `C_GOOD` | (95, 225, 135) |
| `C_GRID` | (60, 78, 104) |
| `C_HULL` | (168, 178, 195) |
| `C_HULL_DARK` | (96, 104, 120) |
| `C_PANEL` | (14, 19, 30) |
| `C_PANEL_BORDER` | (50, 65, 92) |
| `C_PANEL_HI` | (28, 38, 56) |
| `C_PYLON` | (88, 94, 108) |
| `C_RADIATOR` | (210, 125, 95) |
| `C_RAD_HOT` | (255, 220, 160) |
| `C_RCS` | (175, 155, 115) |
| `C_REACTOR` | (255, 170, 70) |
| `C_RIM` | (140, 200, 255) |
| `C_RING` | (112, 128, 158) |
| `C_RING_HOT` | (130, 220, 255) |
| `C_SMES` | (95, 190, 160) |
| `C_STAR` | (235, 240, 255) |
| `C_TEXT` | (230, 236, 245) |
| `C_TEXT_DIM` | (150, 162, 180) |
| `C_WARN` | (255, 205, 70) |

## Appendix -- every CLI report (verbatim output)

The exact text each headless report prints, captured live. These are the same bytes `--all` would emit.

### `python Warpdrive.py --spec`

```

==============================================================================
 COMPONENT SPECIFICATION  --  WD-1u4, every part to scale
==============================================================================
 linear scale 1.8344 x WD-1   dry mass 1.081e+06 t   crew 24
 flat interior 182.2 m   bubble radius 183.4 m   wall 0.2 m

  COMPONENT              SPECIFICATION                                        MASS  SHARE
  ------------------------------------------------------------------------------------------
  warp ring shell        torus D=366.88 m, tube 27.52 m, wall 1.08 m, 96 sectors, 4100 kg/m^3 4.412e+05 t   40.8%
  fore/aft shaping rings 2x torus D=176.08 m, tube 12.84 m, offset +/-69.72 m, 30% solid 5.489e+04 t    5.1%
  HTS field coils        96x REBCO, bore 27.92 m x len 17.24 m, 0.30 m build, 48000 turns x 38 kA, 18 K 2.465e+05 t   22.8%
  crew hull              124.76 m x D 32.00 m, 12 decks, 0.44 m wall, 2700 kg/m^3, 24 crew 1.311e+04 t    1.2%
  crew decks             12 deck plates, D 32.00 m bore, 1.4 m x 2700 kg/m^3 3.121e+04 t    2.9%
  fusion reactor         D-3He torus D=21.24 x 6.36 m, 3.6 m wall, 5200 kg/m^3, 102.70 GW th 2.496e+04 t    2.3%
  SMES buffer            torus D=40.36 x 4.40 m, 1 m shell, 6800 kg/m^3, 60 T -> 2.76 TJ 1.192e+04 t    1.1%
  antimatter traps       8x Penning spheres D=9.56 m, 1.2 m shell, 4400 kg/m^3, 5.248 kg each 1.213e+04 t    1.1%
  cryoplant              16x units D=11.00 m x 20.16 m, 240 kg/m^3, hold coils at 18 K     7357 t    0.7%
  radiators              60x 90.44 x 31.32 m panels, 0.24 m x 1900 kg/m^3, 339910 m^2, 1900 K lim 7.75e+04 t    7.2%
  pylons                 12x 154.08 m x 5.88 m x 4.80 m, 2700 kg/m^3    1.409e+05 t   13.0%
  Casimir lattice        96 cassettes, 1.10 m plates, 10 nm gap, 3.68 m stack, 2300 kg/m^3    983.2 t    0.1%
  deflector              dish D=33.00 m, 0.4 m skin, 3100 kg/m^3            1061 t    0.1%
  RCS pods               32x ion pods D=4.76 m x 9.20 m, 900 kg/m^3         4715 t    0.4%
  boost rectenna         stowed D=84.40 m -> deployed film 4.0 km, 1.0 um film    17.59 t    0.0%
  magsail loop           superconducting loop r=2800 km, 4.4 MA, Cd=0.85 1.28e+04 t    1.2%
  consumables + crew     24 crew x 3.2e+03 kg supplies each                 76.8 t    0.0%
  ------------------------------------------------------------------------------------------
  TOTAL                                                                 1.081e+06 t  100.0%

  envelope: radiator tip reaches 152.8 m inside a 182.2 m interior (29.4 m clear)
  length 211 m x span 395 m   emergent cruise beta 0.8547
  plant: 102.70 GW th -> 63.7 GW el   loads 47087.9 MW el at beta=0.99 cruise
  boost beam: 6.4e+03 PW from a 1000 km array at 1 um, usable to 0.62 ly
  magsail alone halves beta=0.5 in 65.28 yr; a destination array is
  still REQUIRED for rendezvous (see --voyage).
```

### `python Warpdrive.py --metric`

```

==============================================================================
 WARP METRIC  --  Alcubierre shape function, integrated numerically
==============================================================================
 ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2
 f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R)),  sigma = 1/delta
 bubble radius R = 183 m,  flat interior to 182.2 m,  c^4/G = 1.2103e+44 N

 SHAPE FUNCTION across the wall (delta = 0.2 m):
   r [m]        f(r)         df/dr [1/m]    T^00 [J/m^3]    
   182.6400     0.999665     -0.003352      -1.353e+37      
   183.0400     0.982014     -0.1766        -3.756e+40      
   183.2400     0.880797     -1.05          -1.327e+42      
   183.4400     0.500000     -2.5           -7.524e+42      
   183.6400     0.119203     -1.05          -1.327e+42      
   183.8400     0.017986     -0.1766        -3.756e+40      
   184.2400     0.000335     -0.003352      -1.353e+37      

 ENERGY vs WALL THICKNESS at beta = 1 (R = 183 m):
   delta [m]      E [J]            equivalent mass        status
   12             -9.44e+45        -0.0528 Msun           
   1              -1.131e+47       -0.633 Msun            
   0.001          -1.131e+50       -633 Msun              
   1e-09          -1.131e+56       -6.33e+08 Msun         
   1e-15          -1.131e+62       -6.33e+14 Msun         
   1.616e-33      -6.999e+79       -5.19e+09 x observable universe <- quantum-inequality limit (Pfenning & Ford 1997)

 ENERGY vs BETA (delta = 0.2 m):
   beta = 0.1     E = -5.656e+45     J  = -0.0316 Msun          not required -- use the positive-energy shell instead
   beta = 0.5     E = -1.414e+47     J  = -0.791 Msun           not required -- use the positive-energy shell instead
   beta = 1.0     E = -5.656e+47     J  = -3.16 Msun            EXOTIC (NEC violated)
   beta = 2.0     E = -2.263e+48     J  = -12.7 Msun            EXOTIC (NEC violated)
   beta = 5.0     E = -1.414e+49     J  = -79.1 Msun            EXOTIC (NEC violated)
   beta = 10.0    E = -5.656e+49     J  = -316 Msun             EXOTIC (NEC violated)

 TIDAL SHEAR IN THE WALL (2 m body, beta = 0.5):
   delta = 12       m -> 2.399e+14 m/s^2 = 2.446e+13 g
   delta = 1        m -> 3.455e+16 m/s^2 = 3.522e+15 g
   delta = 0.001    m -> 3.455e+22 m/s^2 = 3.522e+21 g
   Interior (r < 182.2 m): f = 1, all derivatives zero, EXACTLY 0 g.

 CASIMIR REALITY CHECK (the only real negative energy there is):
   rho(10 nm gap) = -pi^2 hbar c / 720 a^4 = -4.334e+04 J/m^3
   onboard lattice  = -3.09 MJ across 96 cassettes
   beta=1, 1 m wall needs -1.131e+47 J  -> short by 41 orders of magnitude
   with the QI-legal wall  -> short by 73 orders of magnitude
```

### `python Warpdrive.py --ladder`

```

==============================================================================
 NEGATIVE-ENERGY REDUCTION LADDER  --  thirty years of trying
==============================================================================
 Baseline: R = 183 m, beta = 1, delta = 1e-15 m -> -1.131e+62 J (-6.33e+14 Msun)

 ALCUBIERRE 1994   raw thin-wall metric                     EXOTIC
     x1e+00       ->  -1.131e+62 J   (-6.33e+14 Msun)
     Alcubierre, Class. Quantum Grav. 11 L73 (1994)

 VAN DEN BROECK 1999   microscopic pocket topology          EXOTIC
     x1e-30       ->  -1.131e+32 J   (-1.259e+12 t)
     Van Den Broeck, Class. Quantum Grav. 16 3973 (1999)

 WHITE 2011   thick wall + oscillating bubble               DISPUTED
     x1e-38       ->  -1.13 YJ       (-1.259e+04 t)
     White, NASA JSC 2011 -- reduction claim, never independently verified

 LENTZ 2021   hyperbolic soliton from plasma stress-energy  REFUTED
     claimed positive-energy superluminal solitons;
     shown to violate the NEC after all -- no reduction stands.
     Lentz 2021; refuted by Santiago, Schuster and Visser (2021)

 BOBRICK and MARTIRE 2021   subluminal physical shell       PHYSICAL
     not a reduction of the exotic bill -- a DIFFERENT SOLUTION
     CLASS with no exotic bill at all. Cost becomes ordinary
     kinetic energy: 15 YJ to reach beta = 0.5. Subluminal only.
     Bobrick and Martire, Class. Quantum Grav. 38 105009 (2021)

 FUCHS et al. 2024   constant-velocity positive-energy solution PHYSICAL
     not a reduction of the exotic bill -- a DIFFERENT SOLUTION
     CLASS with no exotic bill at all. Cost becomes ordinary
     kinetic energy: 15 YJ to reach beta = 0.5. Subluminal only.
     Fuchs et al., Class. Quantum Grav. 41 095013 (2024)

 WHERE THAT LEAVES US:
   Superluminal  -- every route still ends at a NEC violation, and
                    Santiago, Schuster & Visser (2022) proved that is
                    generic, not an artefact of Alcubierre's ansatz.
   Subluminal    -- genuinely solved on paper. Positive energy, real
                    matter, all energy conditions satisfied. What
                    remains is an engineering bill this file prices.
```

### `python Warpdrive.py --dilation`

```

==============================================================================
 ENVIRONMENTAL SPACETIME DILATION  --  whose clock, and where
==============================================================================
 From the metric, two observers and two completely different answers:
   COMOVING (the crew, dx = v_s f dt, f = 1):
       ds^2 = -c^2 dt^2      ->  dtau = dt EXACTLY. No dilation, ever.
   STATIC  (holds station in the external frame, dx = 0):
       dtau = dt sqrt(1 - beta^2 f(r)^2)   -- the full Lorentz factor

 STATIC-OBSERVER CLOCK RATE INSIDE THE BUBBLE:
   beta     at centre      at the wall    outside
   0.00     1.000000       1.000000       1.000000
   0.25     0.968246       0.992157       1.000000
   0.50     0.866025       0.968246       1.000000
   0.75     0.661438       0.927025       1.000000
   0.90     0.435890       0.893029       1.000000
   0.99     0.141067       0.868893       1.000000
   2.00     NO STATIC OBSERVER EXISTS -- every worldline inside is dragged past c.
   That last line is the horizon problem, showing up as arithmetic
   rather than as a footnote.

 GRAVITATIONAL ENVIRONMENT ALONG Sol -> Proxima:
   position               Phi/c^2            clock rate
   Earth orbit (start)    -9.8709e-09        0.999999990129
   0.08 ly out            -1.8424e-12        0.999999999998
   midpoint, flat         -8.2488e-14        1.000000000000
   approach               -2.6190e-13        1.000000000000
   Proxima b orbit        -2.4850e-08        0.999999975150

 THE ONLY REAL DRIFT:
   crossing at beta = 0.8547 takes 4.97 yr
   crew clock MINUS Earth clock: +1.5477 s
   -- all of it gravitational (climbing out of Sol's well), not one
      microsecond of it velocity dilation.
   a relativistic ROCKET at the same beta would arrive 2.39 yr YOUNGER.
   The warp drive gives up the dilation dividend and buys arrival in
   step with home. That is a trade, not a free win.

   the ship's own gravity contributes -4.378e-21 -- two orders below
   the best clock ever built, which is how we know it is negligible.
```

### `python Warpdrive.py --portal`

```

==============================================================================
 PORTAL  --  Morris-Thorne wormhole, and the teleporter that works
==============================================================================
 ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2   (Morris & Thorne 1988)
 No horizon, no singularity, traversable both ways. A perfectly good
 solution of the Einstein field equations -- written down in 1988 as a
 TEACHING EXERCISE precisely because it is easy to construct and
 impossible to build.

 THE GATE AS SPEC'D:
   aperture 2 b0            24 m
   throat radius b0         12.0 m
   energy density at throat -3.344e+40 J per m^3   (rho = -c^4/8 pi G b0^2)
   total exotic energy      -2.421e+44 J  (-0.00135 Msun)
   tidal shear crossing it  1.272e+14 g across a 2 m body
   -> nothing made of atoms survives that crossing.

 THE THROAT YOU WOULD ACTUALLY SURVIVE:
   tidal goes as c^2 L / b0^2, so 1 g across 2 m needs
   b0 >= 1.354e+08 m  =  10.6 Earth diameters
   its exotic bill: -2.730e+51 J  (-1.53e+04 Msun)
   Morris & Thorne reached this same conclusion in 1988. 'Portal' and
   'doorway' turn out not to be the same word.

 THE FULL METRIC, NOT JUST THE THROAT:
   ds^2 = -e^(2Phi) c^2 dt^2 + dr^2/(1-b(r)/r) + r^2 dOmega^2
   shape function b(r) = b0^2/r   (Morris & Thorne 1988, eq. 12)
   throat at r0 = b0:  b(r0) = 12.000000 = r0  (check)
   flare-out:  b'(r0) = -1.0000 < 1  (the throat is a minimum of r-b)
   THIS is the condition that costs. It forces d^2r/dl^2 > 0 at the
   throat, and the Einstein equations read that as rho < 0. Theoremed
   for EVERY traversable wormhole (Visser 1989; Flanagan & Wald 1997)
   -- not an artefact of this ansatz.
   tidal profile:  1.27e+14 g at throat, 7.95e+12 g at 2b0, 4.97e+11 g at 4b0
   (falls as 1/r^4 -- the throat is the only lethal part)
   proper length throat -> 4b0:  46.5 m  =  3.87 b0

 AGAINST THE ONLY REAL NEGATIVE ENERGY THERE IS:
   Casimir lattice aboard   -3.09 MJ
   short by 38 orders of magnitude for the gate as spec'd,
   short by 45 orders for a throat wide enough to survive.
 FORD-ROMAN QUANTUM INEQUALITIES (1997):
   Negative energy is not just hard to source -- it is BOUNDED in
   magnitude and duration by quantum field theory:
     |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)   (massless scalar,
                                              sampling time tau)
   At tau = 1 s:  -3.72e-62 J /m^3  -- 102 orders below the throat's demand
   Longest you can hold a 12 m throat open:  3.25e-26 s
   Traversal takes:  4.8 s  --  26 orders of magnitude longer
   The throat closes ~1e26 times before you are halfway through.
   This is the deepest 'no' in the portal section: not 'we lack a
   source' but 'the source is forbidden from lasting long enough',
   by a theorem of quantum field theory.

 VISSER THIN-SHELL WORMHOLE (1989/1995):
   Cut two copies of spacetime at radius a, paste with a thin shell.
   The exotic matter lives on a 2-D SHEET, not a 3-D volume:
     sigma = -c^2 / (2 pi G a) * sqrt(1 - 2GM / a c^2)
   For the spec'd aperture (a = 12 m, M = 0):
     shell exotic mass   -0.0163 Msun
     shell exotic energy -2.905e+45 J
   That is MORE than the Morris-Thorne volume estimate (-0.00135 Msun) --
   concentrating exotic matter on a sheet is LESS efficient, not
   more. Visser's point is about LOCALISATION, not reduction: the
   NEC violation is still there, but on a surface you could in
   principle engineer. It vanishes as a -> 2GM/c^2 (the horizon
   swallows it), which is why nearly-extremal holes are the route.

 MALDACENA-MILEKHIN-POPOV (2020): THE WORMHOLE THAT WORKS ON PAPER:
   The closest thing to a real traversable wormhole in the literature.
   Two nearly-extremal MAGNETICALLY CHARGED black holes, held open by
   the Casimir energy of massless fermions threading the magnetic field
   lines. The negative energy is genuine, calculable, from a real
   quantum field -- not a postulate.
   Survivable BH mass    45834 M_sun  (9.11e+34 kg)
   throat radius (r_s)   1.35e+08 m  =  10.6 Earth diameters
     -- same curvature radius as the Morris-Thorne survivable throat,
       reached from a completely different construction.
   extremal charge       7.854e+24 C  (Q_ext = sqrt(4 pi eps0 G) M)
   traversal time        22.2 s  (t ~ GM/c^3 * ln(M/M_planck))
   Casimir energy        -9.78e-34 J  (tiny, but it tips an almost-wormhole)
   THE CATCHES:
     1. No magnetic monopole has EVER been observed. These BHs may
        not exist. If they do, they are primordial, and none is seen.
     2. The holes must be NEARLY EXTREMAL (Q/Q_ext -> 1). Fine-tuned.
     3. Only massless fermions provide the right Casimir energy.
        This is a specific, fragile construction -- not generic.

 AND THEN IT IS A TIME MACHINE:
   Two mouths at different clock rates desynchronise. When the offset
   exceeds the light-travel time between them, closed timelike curves
   exist (Morris, Thorne & Yurtsever 1988). This is automatic:
   traversable wormhole + ordinary relative motion = time machine.
     park one mouth at Phi/c^2 = -0.2 (neutron star):
       rate gap 0.2254  ->  time machine in 18.84 yr
     carry one mouth on THIS warp drive:
       rate gap 0.0000  ->  never. warp transport cannot desynchronise the mouths (flat interior); a relativistic rocket can
     carry it on a relativistic rocket at the same speed:
       rate gap 0.4808  ->  it works
   Note the irony: the FAST thing cannot build the causality
   violation, and the slow thing can.
   Hawking's chronology protection conjecture (1992) expects vacuum
   fluctuations to destroy the throat at exactly the moment it would
   first close. Unproven -- but it is why most physicists expect no.

 THE TELEPORTER THAT ACTUALLY EXISTS:
   Quantum teleportation is real and routine (Bennett et al. 1993;
   1400 km via the Micius satellite, 2017).
   It moves a quantum STATE, not matter.
   It needs pre-shared entanglement and 2 classical bits per qubit,
   and that classical channel is capped at c -- so NO information
   travels faster than light. Ever.
   No-cloning means the original is destroyed.
   Teleporting one person: about 7.00e+29 bits of state.
   At an absurdly generous 1 Tb/s that is 22.2 Gyr -- about 1.6 times the
   age of the universe.

 VERDICT: four constructions, one answer.
   Morris-Thorne (1988) needs bulk negative energy; no source exists.
   Visser (1989) concentrates it on a shell; that costs MORE, not less.
   Ford-Roman (1997) says the source cannot last long enough even if
     it existed -- the quantum inequalities close the throat in 1e-26 s.
   Maldacena-Milekhin-Popov (2020) is the one that works on paper, with
     REAL quantum-field negative energy -- but it needs magnetically
     charged black holes, and no magnetic monopole has ever been seen.
   And every traversable wormhole is automatically a time machine
   (Morris, Thorne & Yurtsever 1988), which Hawking's chronology
   protection conjecture expects to destroy. The portal is the warp
   drive's problem again, in a new shape -- with a time machine on top.
```

### `python Warpdrive.py --feasibility`

```

==============================================================================
 WD-1 FEASIBILITY SCORECARD  --  what this drive really does
==============================================================================

 [PASS   ] Metric solves the Einstein field equations
           Alcubierre 1994 is exact. Write the spacetime, read off T^uv. The
           mathematics has never been the disputed part.

 [PASS   ] Flat, weightless, un-dilated interior
           f = 1 inside: Minkowski exactly. No proper acceleration at any beta,
           so no g-limit, and ship clocks match Earth clocks.

 [PASS   ] No reaction mass
           The shell sources the metric; nothing is expelled. This is the one
           advantage over a rocket that survives every objection.

 [PASS   ] Positive-energy source (subluminal)
           Bobrick & Martire 2021 and Fuchs et al. 2024 construct subluminal warp
           shells satisfying NEC, WEC, DEC and SEC. Real matter.

 [PASS   ] Waste-heat rejection at cruise
           339910 m^2 of panel rejects 75.9 GW at beta = 0.99 and settles at 1439
           K, under the 1900 K graphite limit.

 [PASS   ] Housekeeping power for a decade-long crossing
           103 GW D-3He plant covers the 16.4 GW cruise load; 20146 kg of fuel
           crosses to Proxima.

 [PARTIAL] Acceleration to cruise speed
           15 YJ of kinetic energy at beta = 0.5. Nothing storable aboard comes
           close, so it must be beamed: a 6e+18 W tap for 30.0 d. The ship cannot
           launch itself, and no design change fixes that.

 [PARTIAL] Cruise speed actually reachable
           beta = 0.855, set by beam range and diffraction -- not by the drive.
           Faster needs a bigger transmitter aperture, not a better warp shell.

 [PARTIAL] Deceleration / rendezvous
           Magsail halves speed in 65.28 yr but STOPS in 3.26e+04 yr -- drag
           falls as v^2. A rendezvous needs a photon-braking array already built
           at the destination. Without one the mission is a flyby.

 [PARTIAL] Interstellar medium loading
           The wall collects everything ahead of it (McMonigal, Lewis & O'Byrne
           2012): 4.25e+26 protons over the crossing, released forward as 7.98 PJ
           when the bubble drops. Aim the arrival away from anything you like.

 [OPEN   ] Shell material with the required stress-energy
           The positive-energy solutions need anisotropic stresses comparable to
           the energy density -- sound speed approaching c. No known material
           does this. This is the real open problem, and it is a materials
           problem, not a relativity problem.

 [FAIL   ] Survivable bubble wall
           Tidal shear reaches 8.80e+16 g across a 2 m body in the wall at beta =
           0.5. The interior is perfectly safe; the wall is not a place.

 [FAIL   ] Superluminal flight (beta > 1)
           Requires NEC violation -- and Santiago, Schuster & Visser (2022)
           proved that holds for EVERY superluminal warp drive, not just
           Alcubierre's. This is a theorem, not a missing invention.

 [FAIL   ] Negative energy at the required scale
           Needs -1.131e+47 J. The onboard Casimir lattice -- real, measured
           physics -- supplies -3.09 MJ. Short by 41 orders of magnitude, and by
           73 orders at the wall thickness the quantum inequality permits.

 [FAIL   ] Steering above beta = 1
           The forward wall is causally disconnected from the interior (Everett
           1996; Coule 1998). You cannot signal the front of your own bubble, so
           the whole trajectory must be pre-laid before departure.

 [FAIL   ] Thermal survival above beta = 1
           Coil load scales as beta^2: 262 GW of waste heat at beta = 2 drives
           the panels to 1961 K, past the 1900 K limit. The ship cooks before the
           energy problem even gets a vote.

------------------------------------------------------------------------------
 SCORE: FAIL 5/16   OPEN 1/16   PARTIAL 4/16   PASS 6/16

 HARDWARE BUILDABILITY  --  when could each line be ordered

 [OPEN     ] warp ring shell  (4.412e+05 t, 40.8% of ship)
             The shell itself is ordinary composite engineering. What it must do is
             not: the positive-energy warp solutions need anisotropic stresses
             comparable to the energy density -- sound speed nearing c. No known
             material does this. A materials problem, not a relativity problem.
           needs: 96 sectors, torus 366.9 m major x 27.5 m minor dia, 1.08 m
           wall, SiC/W metamaterial at 4100 kg/m3 -- plus a stress-energy state
           no foundry can write
           operates: 4944.8 MW servo control share, continuous while the shell is
           shaped
           failure: sector servo loss -> shape error -> integrity drains toward
           collapse; the ship falls out of warp, it does not explode

 [OPEN     ] shaping rings  (5.489e+04 t, 5.1% of ship)
             Same wall, same verdict: drivable geometry is buildable, the
             stress-energy it has to carry is not.
           needs: 2 rings, 176.1 m major x 12.8 m minor dia, 69.72 m offset, 30%
           solid fraction, same metamaterial, same unsolved sourcing
           operates: 2119.2 MW servo control share, continuous while the shell is
           shaped
           failure: same as the main shell: shape error, integrity drain,
           collapse

 [NEAR     ] HTS field coils  (2.465e+05 t, 22.8% of ship)
             REBCO tape is demonstrated in SPARC-class machines. 96 sectors held at
             18 K on a 183 m radius is scaling work, not new physics.
           needs: 96 coils x 48000 turns, 27.92 m bore x 17.24 m pack, 38 kA at
           18 K, 0.30 m winding build at 5600 kg/m3 -- ~408526 km of REBCO tape
           total, quench protection per sector, 38252.8 MW of AC ripple loss to
           sink
           operates: 38252.8 MW AC ripple at beta=1 (scales beta^2) + 18 K hold,
           continuous in warp mode
           failure: a quench dumps the field into the cryostat -- trip to
           subluminal

 [TODAY    ] crew hull shell  (1.311e+04 t, 1.2% of ship)
             Thin-wall SiC pressure vessel, t = P*r/sigma. Aerospace-grade today;
             only the crew count is exotic.
           needs: 124.8 m x 32 m pressure shell, 0.44 m wall, 2700 kg/m3 --
           ordinary thick-laminate fabrication for 24 crew
           operates: none (passive), always
           failure: a breach is a life-safety event, not a propulsion one

 [TODAY    ] crew decks  (3.121e+04 t, 2.9% of ship)
             Bulkheads and floors. Nothing to invent.
           needs: 12 deck plates at 35% fill, same SiC laminate
           operates: none (passive), always
           failure: none

 [FAR      ] fusion reactor  (2.496e+04 t, 2.3% of ship)
             D-3He demands a lunar/regolith helium-3 industry that does not exist,
             and a plasma regime harder than D-T. The honest fallback: D-T at ITER
             class is NEAR, and one metre of water shielding around this reactor
             costs only ~1333 t -- absorbable. The aneutronic choice buys crew
             proximity, not feasibility.
           needs: tokamak 21.2 m major x 6.4 m minor dia, 102.70 GWth -> 63.67
           GWe at 62% direct conversion; fuel ~6.49 kg 3He/day at cruise; hotel
           load 96 MW -- the fuel chain is the blocker, not the torus
           operates: produces 63.67 GWe; burns 6.49 kg 3He/day; vents He-4 ash,
           continuous, every phase
           failure: trip -> hotel load falls on the SMES buffer; blackout is
           survivable for hours, not days

 [NEAR     ] SMES buffer  (1.192e+04 t, 1.1% of ship)
             Superconducting storage exists at small scale. A GJ-class toroid is
             engineering, not research.
           needs: 2.76 TJ at 60 T in a 40.4 m major x 4.4 m minor toroid -- the
           field is ~1.5x the best sustained magnet built today, so the rating
           sits at the NEAR edge
           operates: standby ~0; delivers 2.76 TJ on demand, holds charge;
           discharges on transients
           failure: the bridge between reactor trip and restart -- without it a
           trip is a blackout

 [FAR      ] antimatter traps  (1.213e+04 t, 1.1% of ship)
             World production is nanograms per year. Traps this size need a
             production industry nobody has priced, let alone built.
           needs: 8 traps x 5.25 kg antiprotons (41.98 kg total, 7.55 EJ on tap)
           in 9.6 m Penning cells -- at current production rates, longer than the
           age of the universe
           operates: confinement share of hotel load, continuous containment,
           forever
           failure: confinement loss -> annihilation: 7.55 EJ released against
           the containment wall. This is the one line whose failure is
           catastrophic, not survivable

 [TODAY    ] cryoplant  (7357 t, 0.7% of ship)
             18 K refrigeration is demonstrated technology, resized for cold area,
             not re-invented.
           needs: 16 units, 11.0 m x 20.2 m each, holding coils and traps at 18
           K; 2492.8 MW draw against a radiative leak -- off-the-shelf physics
           operates: 2492.8 MW, continuous -- the coils and traps both ride on it
           failure: warm-up -> quench cascade -> field collapse; hours of margin

 [NEAR     ] radiators  (7.75e+04 t, 7.2% of ship)
             1550 K graphite rejection is refractory-panel / droplet-radiator
             territory: demonstrated below scale, never flown at this size.
           needs: 60 panels x 90.4 m x 31.3 m, both faces = 339910 m2 at 1550 K,
           epsilon 0.92, graphite limit 1900 K -- refractory panels exist at
           bench scale, not at acres
           operates: none (passive radiation), continuous -- the only path heat
           leaves the ship
           failure: overtemp past 1900 K -> panel loss -> thermal runaway; the
           graphite limit is the cruise's hard ceiling

 [TODAY    ] pylons  (1.409e+05 t, 13.0% of ship)
             Structural spars. Nothing to invent.
           needs: 12 spars x 154.1 m, 5.88 m wide -- ordinary composite structure
           operates: none (passive), always
           failure: structural failure under load -- the ship does not spin apart
           slowly

 [FAR      ] Casimir lattice  (983.2 t, 0.1% of ship)
             The Casimir force is measured, real physics. Stacking cassettes to
             joule-class negative energy has never been demonstrated -- a scaling
             problem, not a fake one.
           needs: 96 cassettes, 1.1 m plates, 10 nm gap at 60 nm pitch, 3.68 m
           stack -- 5,887,999,968 plates total for -3.09 MJ of true negative
           energy; precision fabrication at a count no lab has approached
           operates: none (passive plates), continuous -- supplies -3.09 MJ of
           negative energy
           failure: none at cruise; it is never drawn on subluminally

 [TODAY    ] deflector  (1061 t, 0.1% of ship)
             Debris shield plate. Ordinary.
           needs: 33.0 m dia Whipple-style shield, 8.28 m deep
           operates: none (passive), always in the flight direction
           failure: a puncture lets ISM grit reach the hull -- attrition, not a
           single-event loss

 [TODAY    ] RCS pods  (4715 t, 0.4% of ship)
             Attitude thrusters. Ordinary.
           needs: 32 pods, 4.8 m x 9.2 m each -- ordinary propulsion plumbing
           operates: propellant-limited bursts, attitude trim and docking only
           failure: loss -> the ship tumbles; annoying, not fatal

 [NEAR     ] boost rectenna  (17.59 t, 0.0% of ship)
             Rectennas are proven. A kilometres-wide deployable film has never been
             flown -- engineering, not physics.
           needs: deployed 4 km dia (stowed 84.4 m), film 1 um at 1400 kg/m3 --
           ~17.6 t of deployed film; power beaming proven at a kilometre scale
           operates: captures up to 100% of the tap while deployed, deployed
           during boost only; stowed at cruise
           failure: failure to stow -> a 4 km sail in the ISM flux; failure to
           deploy -> no boost, mission scrubs

 [FAR      ] magsail loop  (1.28e+04 t, 1.2% of ship)
             The plasma interaction is modelled (Zubrin 1991, Freeland 2015). A
             2800 km superconducting loop has never been deployed, stabilised or
             repaired -- and those verbs are the whole problem.
           needs: 17593 km of superconductor at 4.4 MA, 12800 t loop (728 g/m),
           drag coef 0.85, 62% regen recovery -- the conductor budget is thinner
           than the current demands, which is what keeps this FAR
           operates: drag power -> 62% recovered to the SMES, deployed during
           braking only
           failure: current quench mid-brake -> the sail goes slack and braking
           stops; the flyby continues ballistically

 [NEAR     ] consumables + crew  (76.8 t, 0.0% of ship)
             Closed-loop life support for a 5.0 year crossing exceeds ISS practice.
             Scaling, not physics.
           needs: 24 crew x 3200 kg of consumables, hotel load 96 MW, a closed
           loop for the full crossing -- longer than any loop run to date, by a
           factor of years
           operates: 96 MW hotel load, continuous
           failure: ECLSS margin: days of buffer, not weeks -- the crossing is
           5.0 years of uninterrupted loop

 [FAR      ] stellar tap (6.4e+18 W, 1000 km array)  (external)
             Lawful physics -- a laser is a laser. The bill is civilisational: a
             transmitter the size of a country and the power to feed it. No
             engineering shortcut moves it under 30 years.
           needs: 6e+18 W delivered across 0.6 ly -- a national-grid-scale
           transmitter, permanently funded

 [FAR      ] destination photon brake  (external)
             A second tap, pre-built at Proxima, or the ship remains a flyby.
           needs: the same transmitter, already standing at the far end before
           launch

 [FAR      ] helium-3 supply chain  (external)
             Lunar regolith extraction at tonne scale -- an industry, not a
             prototype.
           needs: tonnes of 3He per decade -- lunar mining, refining and lift
           capacity combined

 [FAR      ] ISM scoop refuelling  (external)
             Shares the magsail's unproven physics, plus isotope separation
             underway.
           needs: 6.18e-01 kg/s of gas scooped at cruise -- the loop again, plus
           a refinery that runs while it brakes

 [OPEN     ] the warp shell as a drive  (external)
             Subluminal positive-energy shells exist on paper (Bobrick & Martire
             2021); the material to build one does not. Superluminal is not a
             schedule problem -- it is NEC violation, barred by theorem.
           needs: a material with anisotropic stress near the sound-speed limit
           -- unnamed, unmeasured, unpriced

 [IMPOSSIBLE] wormhole gates and time machines  (external)
             Every construction in the model prices its exotic energy honestly and
             every one comes back decades of orders short. Not a procurement
             question.
           needs: 2.421e+44 J of negative energy for the smallest gate -- nothing
           to buy it with


 SHIP: FAR 4/17   NEAR 5/17   OPEN 2/17   TODAY 6/17

 THE HONEST SUMMARY
   A SUBLUMINAL warp drive is not science fiction. It is a solved problem in
   general relativity with a brutal engineering bill: 15 YJ to reach half
   lightspeed, a stellar-scale transmitter to deliver it, a second one at the
   far end to stop, and a shell material nobody knows how to make. Every one
   of those is an engineering obstacle, and none of them is a violated law.

   A SUPERLUMINAL warp drive is a different kind of thing. It needs negative
   energy in bulk, and the shortfall is not 20% or 1000x -- it is 41 orders
   of magnitude against the best real source in physics, with a theorem
   standing behind the requirement. That is not a technology gap.

   This model flies both. It only ever claims one.

   WHAT A PROCUREMENT OFFICE COULD ACTUALLY ORDER
   6 of 17 hardware lines are TODAY -- hull, decks, spars, shield,
   thrusters, cryo. 5 more are NEAR -- coils, storage, panels, rectenna,
   life support: a decade of engineering, not of physics. The reactor, sail,
   traps and lattice wait on industries that do not exist; the two rings
   wait on a material nobody has named. The ship is buildable in the near
   future -- except the part that makes it a warp drive.
```

### `python Warpdrive.py --send`

```

==============================================================================
 PORTAL TRAVERSAL TESTS  --  sending things through, where and when
==============================================================================
 The portal is a wormhole with two mouths.  WHERE you come out is
 where mouth B physically IS.  WHEN you come out depends on the
 clock desynchronisation between the mouths -- real GR, the same
 effect GPS corrects for daily.  Four scenarios:

 ----------------------------------------------------------------------------
 SCENARIO 1: signal (photon) through the 12 m gate, mouths synced
 ----------------------------------------------------------------------------
   throat b0         12 m
   mouth separation  4.02e+16 m = 4.2465 ly
   rate A / rate B   1.000000 / 1.000000  (gap 0.000e+00 s/s)
   elapsed           0.0 s
   time offset       0.0 s  (synced)
   light-time A->B   4.25 yr
   CTCs exist        no  (margin -4.25 yr)
   tidal shear       survivable: tidal shear 0 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 4.80 s but QI allows only 3.25e-26 s -- 26 orders short
   exotic energy     -2.421e+44 J  (38 orders beyond Casimir)
   VERDICT           BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 4.80 s but QI allows only 3.25e-26 s -- 26 orders short

   A photon has no size, so tidal forces cannot destroy it.  But
   the throat still cannot stay open long enough (QI), and the
   exotic bill is still unpaid.  The signal cannot cross.

 ----------------------------------------------------------------------------
 SCENARIO 2: person through the survivable throat, mouths synced
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  4.02e+16 m = 4.2465 ly
   rate A / rate B   1.000000 / 1.000000  (gap 0.000e+00 s/s)
   elapsed           0.0 s
   time offset       0.0 s  (synced)
   light-time A->B   4.25 yr
   CTCs exist        no  (margin -4.25 yr)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short

   The throat is wide enough to survive (b0 = 1.35e+08 m = 10.6 Earth
   diameters).  But the exotic energy is -2.730e+51 J and the QI still
   forbids holding it open for the 54145352.9 s traversal.

 ----------------------------------------------------------------------------
 SCENARIO 3: person, mouth B at Phi/c^2 = -0.01 (deep well), 1 yr
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  4.02e+16 m = 4.2465 ly
   rate A / rate B   1.000000 / 0.989949  (gap 1.005e-02 s/s)
   elapsed           365.2 d
   time offset       3.7 d  (B behind A)
   light-time A->B   4.25 yr
   CTCs exist        no  (margin -4.24 yr)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short

   Mouth B's clock runs slower by 1.0051e-02 s/s.  After 365.2 d the offset
   is 3.7 d.  Light-time between mouths is 4.25 yr.
   -> No CTCs yet.  Arrives in B's past relative to A, but
      not in your own past -- no paradox possible.

 ----------------------------------------------------------------------------
 SCENARIO 4: TIME MACHINE -- mouth B at Phi/c^2 = -0.2, 20 years
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  4.02e+16 m = 4.2465 ly
   rate A / rate B   1.000000 / 0.774597  (gap 2.254e-01 s/s)
   elapsed           20.00 yr
   time offset       4.51 yr  (B behind A)
   light-time A->B   4.25 yr
   CTCs exist        YES  (margin 95.5 d)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY CHRONOLOGY PROTECTION: CTCs exist, and Hawking's conjecture expects the throat to be destroyed at the chronology horizon.  Even if it survived, the exotic bill is -2.730e+51 J.

   Mouth B's rate: 0.774597 vs A's 1.000000.  After 20.00 yr the offset is 4.51 yr.
   Light-time between mouths: 4.25 yr.
   -> CTCs EXIST (offset exceeds light-time by 95.5 d).
      This IS a time machine: step through A->B and you arrive
      1.42e+08 s in your own past.  But Hawking's CPC (1992)
      expects vacuum fluctuations to diverge at the chronology
      horizon and destroy the throat.  Unproven -- but it is
      why most physicists expect the answer to be no.

 ----------------------------------------------------------------------------
 SCENARIO 5: mouth B on a rocket at beta = 0.9, 10 years
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  4.02e+16 m = 4.2465 ly
   rate A / rate B   1.000000 / 0.435890  (gap 5.641e-01 s/s)
   elapsed           10.00 yr
   time offset       5.64 yr  (B behind A)
   light-time A->B   4.25 yr
   CTCs exist        YES  (margin 1.39 yr)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY CHRONOLOGY PROTECTION: CTCs exist, and Hawking's conjecture expects the throat to be destroyed at the chronology horizon.  Even if it survived, the exotic bill is -2.730e+51 J.

   A relativistic rocket DOES desynchronise the mouths (unlike a
   warp drive, whose flat interior gives no dilation dividend).
   Rate gap: 5.6411e-01 s/s.  Offset after 10.00 yr: 5.64 yr.

 ----------------------------------------------------------------------------
 SCENARIO 6: mouth B carried by WARP at beta = 0.9, 10 years
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  4.02e+16 m = 4.2465 ly
   rate A / rate B   1.000000 / 1.000000  (gap 0.000e+00 s/s)
   elapsed           10.00 yr
   time offset       0.0 s  (synced)
   light-time A->B   4.25 yr
   CTCs exist        no  (margin -4.25 yr)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay open long enough to cross.  THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short

   The warp drive's flat interior means NO kinematic dilation.
   Rate gap: 0.00e+00 s/s -- zero (both mouths at rest in flat space).
   The FAST thing cannot build the time machine.  The slow rocket
   can.  This is ctc_by_warp_transport() in full arithmetic.

 ----------------------------------------------------------------------------
 SCENARIO 7: MAX DESYNC -- mouth B at neutron star + 0.99c, 1 AU, 1 yr
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  1.5e+11 m = 0.0000 ly
   rate A / rate B   1.000000 / 0.089219  (gap 9.108e-01 s/s)
   elapsed           365.2 d
   time offset       332.7 d  (B behind A)
   light-time A->B   8.3 min
   CTCs exist        YES  (margin 332.7 d)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY CHRONOLOGY PROTECTION: CTCs exist, and Hawking's conjecture expects the throat to be destroyed at the chronology horizon.  Even if it survived, the exotic bill is -2.730e+51 J.

   Mouth B sits on a neutron-star surface (Phi/c^2 = -0.30) AND moves
   at beta = 0.99 on a rocket.  Combined rate: 0.089219 -- B ages at
   8.9% the rate of A.  At 1 AU separation the light-time is
   only 499 s (8.3 min), so CTC onset is in 548 s (9.1 min).
   -> CTCs EXIST after just 1 year (offset 333 d vs light-time
      499 s).  Step A->B: arrive 333 d in the past.
      Step B->A: arrive 333 d in the FUTURE.

 ----------------------------------------------------------------------------
 SCENARIO 8: MAX BACKWARD JUMP -- same desync, 100 years elapsed
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  1.5e+11 m = 0.0000 ly
   rate A / rate B   1.000000 / 0.089219  (gap 9.108e-01 s/s)
   elapsed           100.00 yr
   time offset       91.08 yr  (B behind A)
   light-time A->B   8.3 min
   CTCs exist        YES  (margin 91.08 yr)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY CHRONOLOGY PROTECTION: CTCs exist, and Hawking's conjecture expects the throat to be destroyed at the chronology horizon.  Even if it survived, the exotic bill is -2.730e+51 J.

   After 100 years, the offset is 91.08 years = 33266 days.
   Step A->B: arrive 91.08 years in your own past.
   Step B->A: arrive 91.08 years in your own future.
   This is the MAXIMUM time jump the portal geometry can produce
   with realistic astrophysical wells and realistic rocket speeds.
   The throat is still closed -- see verdict below.

 ----------------------------------------------------------------------------
 SCENARIO 9: EXTREME -- mouth B near horizon + 0.999c, 1 AU, 100 yr
 ----------------------------------------------------------------------------
   throat b0         1.35e+08 m
   mouth separation  1.5e+11 m = 0.0000 ly
   rate A / rate B   1.000000 / 0.014139  (gap 9.859e-01 s/s)
   elapsed           100.00 yr
   time offset       98.59 yr  (B behind A)
   light-time A->B   8.3 min
   CTCs exist        YES  (margin 98.59 yr)
   tidal shear       survivable: tidal shear 1 g across 2.0 m
   throat hold       THROAT CLOSED: traversal 54145352.87 s but QI allows only 1.09e-22 s -- 30 orders short
   exotic energy     -2.730e+51 J  (45 orders beyond Casimir)
   VERDICT           BLOCKED BY CHRONOLOGY PROTECTION: CTCs exist, and Hawking's conjecture expects the throat to be destroyed at the chronology horizon.  Even if it survived, the exotic bill is -2.730e+51 J.

   Mouth B hovers just above a black-hole horizon (Phi/c^2 = -0.45)
   AND moves at beta = 0.999.  Combined rate: 0.014139 -- B ages at
   1.41% the rate of A.  After 100 yr the offset is 98.59 years.
   Step A->B: arrive 98.59 years in the past.
   Step B->A: arrive 98.59 years in the future.
   This is the theoretical ceiling for wormhole time travel with
   known astrophysical objects.  The throat is still closed.

 ============================================================================
 AMPLIFICATION: beyond a single wormhole
 ============================================================================
   A single wormhole gives at most ELAPSED years of offset after
   ELAPSED years of desynchronisation (rate_diff <= 1).  To go
   further, you need either a CHAIN of wormholes or a different
   construction entirely.  Four mechanisms:

   MECHANISM 1: CHAINED WORMHOLES (N mouths in series)
   ----------------------------------------------------------------------------
   chain of   1 wormholes: offset =     98.6 years
   chain of   2 wormholes: offset =    197.2 years
   chain of   5 wormholes: offset =    492.9 years
   chain of  10 wormholes: offset =    985.9 years
   chain of  50 wormholes: offset =   4929.3 years
   chain of 100 wormholes: offset =   9858.6 years
   Offset scales LINEARLY with N.  The exotic-energy bill scales
   the same way -- each wormhole is an independent throat.
   QI applies to each independently; chronology protection is
   expected to destroy the first one before the chain forms.

   MECHANISM 2: NESTED WORMHOLES (wormhole inside wormhole)
   ----------------------------------------------------------------------------
   outer offset = 98.59 yr, inner offset = 98.59 yr
   nested total = 197.17 yr (additive, not multiplicative)
   Amplification is bounded by the SUM of offsets, not their
   product -- nesting helps but does not multiply.

   MECHANISM 3: TIPLER CYLINDER (infinite rotating cylinder)
   ----------------------------------------------------------------------------
   At chronology horizon (omega*R = c): displacement = L/c
   For L = Proxima (4.25 ly): offset = 4.25 yr
   For L = 1 ly:              offset = 1.00 yr
   For L = 1 AU:              offset = 499.01 s
   The displacement is UNBOUNDED in L -- travel farther along the
   cylinder, get proportionally more offset.  But the cylinder
   must be infinite (or wrap around), and omega*R = c requires
   R ~ 1 m, omega ~ 3e8 rad/s -- a cylinder spinning at ~50 million
   rpm.  No material can hold that.  The mechanism is real but
   the payoff is bounded by L/c for any practical cylinder.

   MECHANISM 4: GOTT COSMIC STRINGS (two strings, deficit angle)
   ----------------------------------------------------------------------------
   GUT string (mu=1e21 kg/m), v=0.5, D=0 ly: offset = 45 yr
   GUT string (mu=1e21 kg/m), v=0.5, D=1 ly: offset = 445 yr
   GUT string (mu=1e21 kg/m), v=0.5, D=10 ly: offset = 4453 yr
   GUT string (mu=1e21 kg/m), v=0.5, D=100 ly: offset = 44526 yr
   The deficit angle is fixed by the string tension; the
   displacement is bounded by delta * D / (4 pi).  For GUT
   strings (mu ~ 1e21 kg/m) the deficit angle is ~1e-4 rad,
   so a 1 ly round trip gives ~445 yr of offset.  For electroweak
   strings (mu ~ 1e-3 kg/m) the offset is ~1e-24 yr -- nothing.
   The mechanism is real but the payoff depends on the string's
   energy scale.

   MECHANISM 5: KERR BLACK-HOLE CTC (ring singularity)
   ----------------------------------------------------------------------------
   extremal Kerr (a=0.99GM/c^2, 10 M_sun),    1 orbits: 9.71e-12 yr
   extremal Kerr (a=0.99GM/c^2, 10 M_sun),   10 orbits: 9.71e-11 yr
   extremal Kerr (a=0.99GM/c^2, 10 M_sun),  100 orbits: 9.71e-10 yr
   extremal Kerr (a=0.99GM/c^2, 10 M_sun), 1000 orbits: 9.71e-09 yr
   The displacement is bounded by the spin period (2*pi*a/c ~
   0.3 ms per orbit for a 10 M_sun extremal Kerr).  Multiple
   orbits add linearly -- 1e6 orbits gives ~5 min.  The ring
   singularity is inside the inner horizon, which is unstable
   (mass inflation, Poisson-Israel 1990) -- the physical black
   hole is expected to be non-traversable.

   ----------------------------------------------------------------------------
   MAXIMUM DISPLACEMENT COMPARISON (100 yr elapsed, extreme desync)
   ----------------------------------------------------------------------------
   Mechanism                  Max offset
   ----------------------------------------------------------------------------
   Single wormhole               98.59 yr
   Chain of 10 wormholes        985.86 yr
   Nested wormholes             197.17 yr
   Tipler cylinder (4.25 ly)       0.00 yr
   Gott pair (1 ly, GUT)        445.26 yr
   Kerr CTC (10 M_sun)        9.71e-12 yr
   ----------------------------------------------------------------------------
   WINNER: CHAIN (9.86e+02 yr)
   A chain of wormholes multiplies the single-wormhole offset
   by N.  The exotic-energy bill and all barriers scale the
   same way -- no barrier is avoided, only multiplied.

 ============================================================================
 MULTI-JUMP: iterated traversal (hop -> external return -> rejump)
 ============================================================================
   The ship is the RETURN LEG between mouths.  Each cycle:
     hop through (+-delta), external reposition at beta=0.855
     (614 s = 10.2 min at 1 AU), rejump.  Offset keeps growing:
     delta(t) = rate_diff * t while the desync condition holds.

   BACKWARD loop (step A->B into past, return externally):
     recurrence t <- t(1-r) + Delta, converges to t* = Delta/r
     = 623 s.  Net-backward only while t > t* -- i.e. AFTER
     CTC onset (506 s).  Cannot evade chronology protection.
     cycle 1: coord 100.000 yr, offset 98.59 yr, net -98.59 yr
     cycle 2: coord 1.414 yr, offset 1.39 yr, net -1.39 yr
     cycle 3: coord 0.020 yr, offset 0.02 yr, net -0.02 yr
     cycle 4: coord 0.000 yr, offset 0.00 yr, net -0.00 yr
     ... converges to t* in ~3-4 cycles.
     TOTAL reachable past = 100.00 yr (elapsed - t*) -- vs 98.59 yr
     for ONE jump.  Multi-jump reaches nearly all of elapsed.

   FORWARD loop (step B->A into future, return externally):
     recurrence t <- t(1+r) + Delta -- GEOMETRIC, unbounded
     while the desync condition holds.
     cycle 1: coord 100.000 yr, offset 98.59 yr, net +98.59 yr
     cycle 2: coord 198.586 yr, offset 195.78 yr, net +195.78 yr
     cycle 3: coord 394.365 yr, offset 388.79 yr, net +388.79 yr
     cycle 4: coord 783.153 yr, offset 772.08 yr, net +772.08 yr
     ... 10 cycles -> 9.539e+04 yr coordinate time.
     Forward travel is exponentially self-amplifying.

   ENERGY LEDGER per cycle (1 AU leg at beta=0.855):
     ship load held    : 36.8 GW (cruise_load at constant beta)
     energy per cycle  : 22.6 TJ
     fuel burnt/cycle  : 1.0344e-01 kg D-3He
     ISM scoop flux    : 91199.64 kg/day raw gas (magsail sweeps A*v)
     D-3He yield       : 8.208 kg/day (isotope-lean: D/H 2e-5,
       3He/4He 2e-4, after perfect enrichment)
     scooped/cycle     : 5.8317e-02 kg vs burnt 1.0344e-01 kg -> NET CONSUMER
     Standing still the scoop is zero and housekeeping still
     burns ~1.58 kg/day -- refuelling requires motion.
     Scoop parity ~ beta = 0.27: below it the cryo+hotel burn
     floor beats the beta-proportional isotope yield (burn > yield at 0.27c).
     Exotic per hop    : 2.730e+51 J (throat, NOT ship-payable -- flagged)
   Ship fuel is a non-issue at 1 AU (milligrams/cycle); at
   Proxima-scale separation each cycle burns ~26.4 t and scoops
   ~14.9 t -- still net-positive while moving.

 ============================================================================
 CONTROL SUMMARY: what GR actually lets you control
 ============================================================================
   WHERE (exit location):  move mouth B.  The wormhole connects
     A to B -- you cannot choose the exit independently of B.
   WHEN (arrival time):    desynchronise the mouths by parking B
     in a gravity well (scenario 3) or moving it at relativistic
     speed (scenario 5).  The offset accumulates linearly and is
     the same dilation GPS measures daily.
   CTC ONSET:              when |offset| > D/c (light-time between
     mouths).  Before that: B's past, not your past.  After that:
     time machine -- Hawking CPC expects destruction.
   WARP CANNOT DESYNC:     a warp bubble's interior is flat, so a
     mouth carried by warp ages at the same rate as one at rest.
     The fast thing cannot build the causality violation.

   MAXIMUM TIME TRAVEL (scenarios 7-9, pushing to physical limits):
     Max rate difference:   0.9108 (neutron star + 0.99c rocket)
     Min CTC onset:         548 s (9.1 min) at 1 AU separation
     Max backward jump:     91.08 years (100 yr elapsed, step A->B)
     Max forward jump:      91.08 years (same offset, step B->A)
     Extreme ceiling:       98.59 years (horizon + 0.999c, 100 yr)
     BOTH directions are    the SAME offset -- the wormhole is
     symmetric:             step A->B for the past, B->A for the
                             future.  No new physics either way.

   THE WARP DRIVE ITSELF produces almost no time shift:
     Gravitational drift:   +1.55 s over the 4.97 yr crossing
     (crew age this much MORE than Earth -- leaving Sol's well
      makes their clock run faster.  Not controllable: set by
      the gravitational potential difference between Sol and
      Proxima, which is fixed by astrophysics.)
     Kinematic dilation:    0.0 s (flat interior -- no dividend)
     Warp-transport desync: 0.0 (cannot build a time machine)

   EVERY scenario is blocked by at least one of:
     - exotic energy (no source exists; 45 orders short of Casimir)
     - quantum inequalities (throat closes in 1.09e-22 s vs 54145352.9 s cross)
     - chronology protection (CTCs -> throat destruction)
   The portal is the warp drive's problem again, in a new shape,
   with a time machine on top.
```

### `python Warpdrive.py --voyage 0.5`

```

==============================================================================
 VOYAGE  --  Sol to Proxima Centauri b (4.2465 ly) at beta = 0.500
==============================================================================
 ship mass 1.081e+06 t   cruise load 16.4 GW   plant 63.7 GW
 destination array: ASSUMED PRESENT (rendezvous)

     0.0 s  BOOST to beta 0.500 -- bill 15 YJ over 30.0 d
    24.4 d  cruise beta 0.5000 reached; beam released
   8.50 yr  MAGSAIL DEPLOYED at beta 0.500
   8.50 yr    magsail alone: halves speed in 65.28 yr, STOPS in 3.26e+04 yr
   8.50 yr    destination array ASSUMED PRESENT: photon brake 4.27e+10 N -> stop in 50.7 d
   8.50 yr  bubble down: 4e+26 swept protons released forward (7.97 PJ)
   8.52 yr  FLYBY -- passing Proxima at beta 0.453, still 3.26e+04 yr from stopped
   8.63 yr  ARRIVED. ship 8.63 yr / Earth 8.63 yr

  arrival: ship 9.00 yr | Earth 9.00 yr | distance 4.2465 ly
  a relativistic ROCKET at the same beta would have aged 7.36 yr
  -- the warp crew age MORE, and arrive in step with home. That is
     the trade: no dilation dividend, no reaction mass, no g-forces.

=== HONESTY LAYER -- conservation audit ===
   [PASS]  no_overunity_kinetic
   [PASS]  recovery_bounded
   [PASS]  plant_within_rating
   [PASS]  fuel_backs_output
   [PASS]  exotic_never_supplied
   [PASS]  radiates_only_outward
   [PASS]  NEC_reported_truthfully
   [PASS]  no_velocity_dilation_dividend
   [PASS]  gravitational_drift_modelled
   [PASS]  beam_capture_le_1
   [PASS]  all_masses_positive
   [PASS]  arrival_requires_stopping
   [PASS]  ledger_finite_nonneg
   kinetic gained     : 0 J
   beam delivered     : 15.1 YJ
   kinetic peak held  : 15 YJ
   magsail recovered  : 9.48 ZJ
   photon brake work  : 14.2 YJ  (leaves with the beam, not recovered)
   plant produced     : 4.44 EJ  (2.03e+04 kg D-3He burnt)
   heat radiated      : 7.16 EJ
   crew clock vs Earth: +2.516 s over 9.00 yr  (gravitational only)
   exotic energy OWED : 0 J   (none: subluminal, positive-energy)
   Casimir available  : -3.09 MJ
   VERDICT: HONEST -- nothing created from nothing.
```

### `python Warpdrive.py (startup banner)`

```
==============================================================================
 Warpdrive V1.0 -- WD-1 FOLDRUNNER :: Physical Warp Drive Digital Twin
 to-scale, flyable, energy-honest (nothing created from nothing)
==============================================================================
 THE SHIP
   dry mass                   1.081e+06 t
   envelope                   367 m ring / 125 m hull / 183 m bubble
   fusion plant               103 GW thermal -> 63.7 GW electrical
   radiators                  339910 m^2, 1900 K limit
------------------------------------------------------------------------------
 THE TWO DRIVES
   PHYSICAL (beta < 1)   positive energy, every energy condition met.
     Bobrick & Martire 2021 / Fuchs et al. 2024. Real matter, real
     solution. Costs 15 YJ to reach beta = 0.5, and this model
     charges you every joule of it.
   ALCUBIERRE (beta > 1)  needs -1.131e+47 J of NEGATIVE energy.
     Onboard Casimir lattice supplies -3.09 MJ -- short by 41 orders
     of magnitude. It flies here, flagged UNFUNDED on every frame.
------------------------------------------------------------------------------
 THE MISSION  Sol -> Proxima Centauri b, 4.2465 ly
   max cruise beta 0.8547 -- EMERGENT from beam aperture, wavelength,
     tap power and ship mass. Nothing in the spec names a speed limit.
   crossing 4.97 yr ship time, and the same on Earth's calendar.
   stopping needs an array at the far end: the magsail halves your
     speed in 65.28 yr but takes 3.26e+04 yr to actually stop.
------------------------------------------------------------------------------
 CONTROLS
   TAB  SHIP / METRIC / DILATION / PORTAL / FLIGHT
        I  full spec      M  energy ladder      H  help
   SHIP    drag=orbit  wheel=zoom  right-drag=pan  R=reset  L=labels
           1=full 2=exploded 3=assembly  4/X=section  hover=spec card
   METRIC  [ ] wall thickness   , . beta   -- watch the bill move
   DILATION every clock in the problem, not just the flattering one
   PORTAL  the wormhole, priced -- and the time machine it hands you
   FLIGHT  B=shell  G=boost  K=brake  J=destination array  - + warp
           F=unlock Alcubierre mode (superluminal, unfunded)
   P pause    H help    ESC quit
==============================================================================
```

## Appendix -- the independent scale audit (verbatim transcript)

`_scale_audit.py` recomputes everything from DIMS with its own constants -- it deliberately does NOT call the model's derivation helpers, so a bug in the model cannot make the audit pass by accident. This is its full output.

```
==============================================================================
 SCALE AUDIT -- independent recomputation from DIMS
==============================================================================

-- per-component mass (independent volume x density vs model) --
  warp ring shell         mine    441245027.8 kg   model    441245027.8 kg   OK
  shaping rings           mine     54892107.6 kg   model     54892107.6 kg   OK
  HTS field coils         mine    246504390.2 kg   model    246504390.2 kg   OK
  crew hull shell         mine     13112162.7 kg   model     13112162.7 kg   OK
  crew decks              mine     31213778.9 kg   model     31213778.9 kg   OK
  fusion reactor          mine     24958427.4 kg   model     24958427.4 kg   OK
  SMES buffer             mine     11918250.0 kg   model     11918250.0 kg   OK
  antimatter traps        mine     12128010.6 kg   model     12128010.6 kg   OK
  cryoplant               mine      7356936.4 kg   model      7356936.4 kg   OK
  radiators               mine     77499410.7 kg   model     77499410.7 kg   OK
  pylons                  mine    140899627.0 kg   model    140899627.0 kg   OK
  Casimir lattice         mine       983178.2 kg   model       983178.2 kg   OK
  deflector               mine      1060570.3 kg   model      1060570.3 kg   OK
  RCS pods                mine      4715026.1 kg   model      4715026.1 kg   OK
  boost rectenna          mine        17592.9 kg   model        17592.9 kg   OK
  magsail loop            mine     12800000.0 kg   model     12800000.0 kg   OK
  consumables + crew      mine        76800.0 kg   model        76800.0 kg   OK

-- totals --
  total dry mass: 1081381 t (doc: 1,081,381 t)

-- scale-factor consistency --
  SCALE_S = 1.8344 ; interior 182.24 m of 183.44 m bubble

-- envelope (every part inside the flat interior) --
  deflector rim    r=  16.50 z=  70.66  reach   72.56 m  OK
  hull midbody     r=  16.00 z=   0.00  reach   16.00 m  OK
  radiator tip     r= 100.88 z= 114.80  reach  152.83 m  OK
  boost rectenna   r=  42.20 z=  89.88  reach   99.29 m  OK
  shaping ring     r=  94.46 z=  69.72  reach  117.40 m  OK
  cryo unit        r= 146.75 z=  10.08  reach  147.10 m  OK
  SMES toroid      r=  22.38 z=  40.36  reach   46.15 m  OK
  binding: radiator tip at 152.8 m, interior 182.2 m, margin 29.4 m

-- ship-level derived figures --
  overall span 395.40 m x length 210.94 m
  radiator area 339910 m^2
  SMES 2.762 TJ (torus vol 1928 m^3)
  reactor 102.70 GW th -> 63.67 GW electric
  beta=0.99 cruise load 47.09 GW e -> required plant 102.53 GW th (spec 102.70)

-- thermal (Stefan-Boltzmann equilibrium) --
  T(0.99c)=1439 K  T(2c)=1961 K  need 385910 m^2 vs have 339910 m^2 (+13.5%)

-- boost beam (Airy diffraction) --
  tap 6.4e+18 W ; spot(0.62 ly) = 14.3 km ; capture there 7.8%

-- kinetic energy --
  gamma(0.855)=1.9282  KE=90.21 YJ ; beta=0.9 needs 125.8 YJ

-- emergent cruise speed --
  emergent cruise beta = 0.8547 (mass 1.081e+09 kg, tap 6.4e+18 W)

-- Casimir negative energy --
  6.133e+07 plate gaps per cassette x 96 cassettes = -3.09 MJ

-- Alcubierre bill for THIS bubble (183.44 m, 0.2 m wall) --
  E_warp(beta=1) = -5.66e+47 J ; Casimir shortfall 41.3 orders

-- magsail braking --
  full stop 32603 yr

-- coil bore vs winding geometry --
  bore 27.92 m (pack inner dia 27.92 m) -> 408526 km of REBCO tape

-- gravitational drift (live crossing) --
  drift +1.548 s over 4.97 yr

-- component counts vs pass-7 spec --

==============================================================================
 70/70 independent checks passed
==============================================================================
```

## Appendix -- the module docstring

The contract the source file itself opens with:

```

================================================================================
 Warpdrive V1.0  --  WD-1 "FOLDRUNNER" :: Physical Warp Drive Digital Twin
================================================================================

A 100% standalone monolith that builds, animates and *flies* a complete warp
drive starship in real time, mechanically and gravitationally to scale, in a
single Python file.

Same architecture as the reference engines it is built from -- GmansRunV1.17.py
(HOHEV rotary EV twin), SE.py (marine H2 twin), LS.py (lightsaber twin),
Radiant.py (EMHL megastructure twin), Simulation.py (particle/QED monolith):
a pure-Python software renderer (numpy painter's algorithm + flat shading),
every dimension held in DIMS in SI metres and rendered to scale, every number
computed from a cited textbook formula, and a dedicated HONESTY LAYER that
refuses to report physics that does not exist.

--------------------------------------------------------------------------------
WHAT THIS ACTUALLY IS (read this first -- it is the whole point)
--------------------------------------------------------------------------------
A warp drive is not a propulsion system. It is a SOLUTION OF THE EINSTEIN FIELD
EQUATIONS: you write down the spacetime you want, then read off the matter
distribution that would produce it. That inverse method always gives you an
answer -- the only question is whether the matter it demands can exist.

This twin builds BOTH answers, side by side, and never confuses them:

  DRIVE A -- SUBLUMINAL PHYSICAL WARP  (Bobrick & Martire 2021; Fuchs et al.
             2024). A real, positive-energy, NEC/WEC/DEC-satisfying warp
             solution. A massive shell carrying a shift-vector distribution
             moves a flat-spacetime interior along a geodesic. No exotic
             matter. No time dilation inside. No reaction mass. Capped at
             beta < 1. Its energy bill is the honest relativistic kinetic
             energy of the shell, (gamma-1) M c^2 -- and this model charges
             you every joule of it. THIS DRIVE FLIES HERE AND ITS PHYSICS
             IS SOUND.

  DRIVE B -- SUPERLUMINAL ALCUBIERRE  (Alcubierre 1994). beta > 1. The model
             computes the required stress-energy by direct numerical
             integration of Alcubierre's own T^00 -- and it comes out NEGATIVE
             and enormous. Santiago, Schuster and Visser (2021) proved that
             EVERY superluminal warp drive violates the null energy condition.
             The onboard Casimir lattice is the largest real negative-energy
             source known to physics, and this model computes exactly how far
             short it falls: 40 orders of magnitude against a generous 1-metre
             wall, and 73 against the wall thickness the quantum inequality
             actually permits. Those two numbers are computed, not quoted. Drive B
             runs in the simulation, flagged amber on every frame, because the
             job of a digital twin is to show you the wall, to scale, with the
             arithmetic attached -- not to pretend the wall is not there.

The honesty layer (SECTION 9) audits both. If it ever reports over-unity, a
violated conservation law, or exotic matter conjured from nothing, the model is
broken and must not be trusted.

--------------------------------------------------------------------------------
RUN
--------------------------------------------------------------------------------
    python Warpdrive.py                # interactive 3D digital twin (default)
    python Warpdrive.py --selftest     # headless physics unit checks
    python Warpdrive.py --feasibility  # honest hurdle-by-hurdle scorecard
    python Warpdrive.py --metric       # warp-metric numbers, no window
    python Warpdrive.py --voyage       # headless Sol -> Proxima flight report
    python Warpdrive.py --ladder       # negative-energy reduction ladder
    python Warpdrive.py --dilation     # every clock in the problem
    python Warpdrive.py --portal       # wormhole + the teleporter that works
    python Warpdrive.py --send         # portal traversal: send signal/person/object through

--------------------------------------------------------------------------------
MODES  (TAB cycles)
--------------------------------------------------------------------------------
  1. SHIP     Orbit the whole vessel to scale -- 394 m warp ring, 125 m crew
              hull, 100 m warp bubble. Every subsystem is built from DIMS and
              labelled: the ring's 24 field coils and 24 Casimir cassettes, the
              D-3He fusion torus, the antimatter traps, the SMES buffer, the 16
              heat radiators (sized by Stefan-Boltzmann against the real waste
              heat), the cryoplant, the deflector, the magsail. FULL / EXPLODED
              / ASSEMBLY views, cross-SECTION cut, hover a part for its specs.

  2. METRIC   The spacetime itself. A live 3D grid sheet deformed by the REAL
              York expansion scalar theta = beta c (x/r) df/dr -- space
              expanding behind the ship, contracting in front -- plus live
              profile plots of the shape function f(r), its derivative, and the
              Alcubierre energy density T^00(r). Drag the wall thickness and
              watch the energy bill move by forty orders of magnitude.

  3. DILATION Whose clock, and where. The warp drive's famous "no time
              dilation" is true for the CREW and false for a static observer
              inside the same bubble, who is dilated by the full Lorentz
              factor. This view draws that field, the gravitational clock rate
              along the route, and the two-and-a-bit seconds of real drift the
              crew accumulate against Earth -- all of it gravitational.

  4. PORTAL   A Morris-Thorne traversable wormhole, drawn from its real
              embedding diagram. Prices the throat, computes the tidal shear
              that makes a walk-through gate lethal, reports the 135,000 km
              throat you would actually survive, and then points out that any
              such portal is automatically a time machine. Alongside it: the
              teleporter that genuinely exists, and why it is not this.

  5. FLIGHT   Fly Sol -> Proxima Centauri b (4.2465 ly) through the three
              phases the physics actually forces on you: BOOST under the
              stellar-tap beam (while the diffraction spot still fits your
              rectenna), CRUISE for free because a constant-velocity warp
              solution is a stationary spacetime, and BRAKE on the magsail
              against the interstellar medium -- because nothing onboard can
              pay for deceleration. Live bubble integrity, radiator
              temperature, ISM load on the wall (McMonigal, Lewis and O'Byrne
              2012), ship clock vs Earth clock, energy-condition verdict.
              Above beta = 1 the forward wall goes causally disconnected
              (Everett 1996; Coule 1998) and the helm LOCKS -- exactly as the
              horizon theorem requires.

Dependencies:  numpy, pygame   (no GPU, no CAD, no GR library -- the metric is
                                integrated here, in this file)

Controls are printed at startup and shown on-screen (press H for help,
press I for the full informational specification panel).
================================================================================
```

## Appendix -- full function & class contracts (every docstring)

The registry above keeps each contract's first line. Here is every docstring in full -- the derivations, caveats and honesty notes live in the later paragraphs.

### `Mesh`

```
A bag of vertices + polygon faces with a base colour. Coordinates are in
METRES, ship axis along +Z (the direction of travel). `spin` is the rotation
ratio relative to the master animation angle; `pivot` offsets the local
origin; `tilt` is a static (rx, ry) orientation.
```

#### `Mesh.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

### `MetricCam`

```
Orbit camera for the METRIC sheet.

It exposes the same control surface as ShipRenderer so the shared mouse and
keyboard handlers drive either one, but it keeps its own az/el/dist -- the
spacetime sheet and the ship want completely different framing, and having
them share a camera meant orbiting one wrecked the other.
```

#### `MetricCam.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

### `Part`

```
A named, spec'd logical component made of one or more meshes. Carries an
assembly `order`, an `explode` offset (where it slides to when disassembled)
and a `specs` list shown in the inspector card.
```

#### `Part.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

### `ShipRenderer`

```
Projects and paints the spec'd Parts. Supports FULL / EXPLODED / ASSEMBLY
views with an optional cross-SECTION cut, mouse hover-picking, highlight +
hover-pop, and the assembly 'puzzle' (place one part at a time).
```

#### `ShipRenderer.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

#### `ShipRenderer.render`

```
Paint every visible facet back-to-front. `coil_glow` is the rotating
field-phase intensity per coil (the warp analogue of GmansRun's
per-chamber firing glow), `drive_power` brightens every glow mesh, and
`bubble_on` fades the wireframe warp shell in and out.
```

#### `ShipRenderer._section_cut`

```
Remove the +X half of the bulky parts -- a clean half-section through
the vertical plane, so the reactor torus, the SMES store, the Casimir
cassettes inside the ring wall and the four crew decks read in true
cross-section. `wvx` is the mesh's world X coordinates as a plain list;
this runs once per FACET, so it stays in pure Python.
```

### `Starfield`

```
Parallax star background. Stars stream past at a rate set by the ship's
apparent velocity -- which for a warp drive is honestly labelled APPARENT,
since the ship is not moving through them at all.

Each star has a TEMPERATURE CLASS (O/B/A/F/G/K/M) sampled like a real
initial mass function (heavy on cool reds, light on hot blues), and is
coloured by its blackbody approximation. Brighter stars (low depth d,
high magnitude) are drawn as 2-pixel crosses; fainter ones as single
pixels -- the same hierarchy the companion twins (GmansRun, SE, LS) use
to give a starfield depth without a sprite atlas.
```

#### `Starfield.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

#### `Starfield.draw`

```
Static fields are painted once and blitted; only the streaking
FLIGHT field is rebuilt per frame.
```

#### `Starfield._star_col`

```
Blackbody-coloured star: base colour from spectral class, scaled by
apparent brightness. Clamped to valid RGB.
```

### `Voyage`

```
The trip. Position, both clocks, the phase machine and the ISM ledger.

Note which clock is which. A relativistic ROCKET at the same speed would
have aged less than the crew; a warp ship does not, because its interior is
flat and unaccelerated. That is not a defect -- it means the crew arrive in
step with the people who launched them, which is the only version of
interstellar travel that is any use to a civilisation.
```

#### `Voyage.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

#### `Voyage.update`

```
Advance the voyage by dt_real real seconds x the time-warp factor.

Substepped so a 10 yr/s warp setting cannot integrate the relativistic
momentum equation into nonsense.
```

#### `Voyage.auto_step`

```
One scripted phase advance for the viewer's TEST mode.

DOCK -> BOOST -> (physics) -> CRUISE -> BRAKE -> (physics) -> ARRIVED.
Only ever moves a phase FORWARD along that line and only by calling
the same begin_* commands the manual chips call, so a demo can never
fly a mission the manual controls could not. Returns the phase the
voyage was left in.

`tick_s` is how much voyage time the enclosing frame step covers
(real_dt x warp); the brake margin is widened by one tick's travel
distance so a 10 yr/s warp cannot leapfrog the entire braking
window and turn a rendezvous demo into an accidental flyby.
```

#### `Voyage.auto_done`

```
A demo has nothing left to show: arrived, or reached the target
without stopping (a flyby is also an ending -- the honest one, if no
destination array was assumed).
```

### `WarpCore`

```
The live drive. Holds the field, spends the energy, tracks the ledger.

The one rule this class obeys without exception: energy that has no source
is never quietly created. When the commanded solution needs negative energy
-- which happens the instant beta crosses 1 -- the shortfall is booked to
`exotic_debt_j` and flagged UNFUNDED on every frame, rather than being
silently supplied. The bubble still forms and the ship still flies, because
showing you the unfunded number is more useful than refusing to draw it.
```

#### `WarpCore.__init__`

```
Initialize self.  See help(type(self)) for accurate signature.
```

#### `WarpCore.helm_locked`

```
Above beta = 1 the crew cannot signal the forward wall, so no new
command can reach it. The trajectory is frozen as flown.
```

#### `WarpCore._integrity`

```
Bubble integrity: what actually breaks a warp drive in this model.

Three independent failure paths, all computed from live state -- panel
overtemperature, a power deficit the plant cannot cover, and a wall
thinner than the shape servo can hold. None of them is a scripted
event; each is a threshold on a number the physics produced.
```

#### `WarpCore.collapse`

```
The shell lets go.

If it was superluminal, the apparent velocity simply stops existing:
an Alcubierre bubble carries its contents without ever giving them
momentum, so when the metric relaxes the ship is at rest with respect
to the local frame. It does not coast on at 2 c. That is not a mercy
in the model -- it is what the metric says.
```

#### `WarpCore.update`

```
Advance one tick. `dt` is SHIP seconds (already time-warped).
```

### `_Dims`

```
DIMS container: any non-real value read back returns NaN instead of
crashing on arithmetic -- a corrupted config degrades into honest NaN
propagation rather than a TypeError. Writes and iteration stay raw so
sanitize loops and ledgers can inspect what was actually stored.
```

#### `_Dims.__getitem__`

```
Return self[key].
```

### `_annulus_cylinder`

```
Hollow tube closed at both axial ends (a pipe with real wall thickness).
```

### `_args_real`

```
Boundary coercion for helpers whose parameters are ALL numeric: every
argument passes through _real, so a poisoned string/list/complex degrades
into honest NaN propagation instead of a TypeError.

Exception: a parameter whose declared default IS None uses None as its
"not provided" sentinel, so an explicit None passes through untouched and
the function's own defaulting still applies. None on any other parameter
is a poisoned value and becomes NaN like everything else.
```

### `_car_loft`

```
Loft the coupe body: stations are (z, half_width, y_top, y_bot) and the
section is an 8-vertex chamfered rectangle -- enough for the wedge nose,
the cabin step and the fastback tail to read at a glance. VISUAL_DETAIL
subdivides the loft both ways: at 2x each section edge splits in two and
each station pair gains a mid-station, so the shell refines to four
times the facets while the wedge keeps every crease.
```

### `_coil_arc`

```
Winding-pack shell that follows the torus centreline along an arc.

A straight annulus chord sags ~len^2/(8 r_mid) off the curved tube; this
bends the pack around the ring so every vertex is exactly r_in..r_out
from the centreline, and the arc length (r_mid * (a1 - a0)) IS the
billed coil_len_m -- same volume as the straight-cylinder mass bill.
```

### `_coil_count`

```
Coil count from DIMS, bounded.  The physical ring carries tens of
coils; an uncapped DIMS['coils']=1e18 would request an exabyte array.
4096 is far above any plausible winding spec yet trivially allocatable.
```

### `_component_info_sections`

```
The whole bill of materials, explained line by line.

Builds two info-panel sections (ship + external infrastructure) directly
from the three live ledgers -- mass_budget() for the numbers,
buildability_ledger() for when it could be ordered and what it demands,
operations_ledger() for what it draws and what its failure costs. Because
all three ledgers read DIMS/PLANT live, these sections cannot drift out
of sync with the ship the way a hand-typed parts list would.
```

### `_deck_plate`

```
Solid circular slab with off-axis penetration holes + drawn collars.

A Penning bay pierces a deck: the plate is the disk MINUS each hole,
and a collar wall dresses the opening so it reads as a designed bay,
not a clipping artefact. holes = ((hx, hy, hr), ...) in deck coords.
```

### `_dish`

```
A parabolic dish opening along +Z (deflector, rectenna collector).
```

### `_envelope_points`

```
Extreme (radius, |z|) corners of every part that must live INSIDE the
bubble. The ring, its coils and its Casimir cassettes are deliberately
absent: they straddle the wall, because they are what sources it.
```

### `_finite`

```
True only when every argument is a finite real number. Mesh generators
gate on this so a nan/inf dimension yields an empty mesh instead of nan
vertices flowing into the GL buffers.
```

### `_function_registry_lines`

```
Every public function in this module, grouped by domain, with its
signature and the first line of its contract -- harvested by
introspection so it cannot go stale.
```

### `_hull_loft`

```
Loft a smooth body from circular cross-sections along Z.
Each section is (z, radius). Consecutive rings are skinned and the ends
capped -- this is how the crew hull gets its true barrel-and-cap
profile (the loft is solved so its mean shell radius hits
hull_shell_rfrac exactly).
```

### `_luminance`

```
Relative luminance of an RGB colour (0..1). Used by contrast_text().
```

### `_mt_funnel`

```
Wire mesh of one half of the Morris-Thorne embedding diagram.

Rings at increasing rho, meridians joining them, with the height from
mt_embedding_z(). Sampled with rho spaced as b0*cosh^2 so the vertices
crowd onto the throat, where all the curvature is -- the same trick the
METRIC sheet uses, for the same reason.
```

### `_numeric_dims`

```
_Dims copy of DIMS with every non-real value already coerced to NaN,
for builders that then work on local d[...] arithmetic.  It stays a
_Dims so a DELETED key also reads back NaN instead of KeyErroring.
```

### `_pipe_path`

```
Sweep a circle along a polyline -- the external conduit runs that
engineering reader will read instantly as the field conduit run.
```

### `_place`

```
Move a set of origin-built meshes into position (and orientation).
```

### `_prep_global`

```
Merge every part's prepped static meshes into shared vertex arrays
plus per-face-length groups indexed into them. When no part is
displaced (the common full-view pose -- no explode, pop or assembly
step) a whole frame needs ONE camera transform and one projection
instead of ~30, and the emit pass iterates ~6 length groups instead
of ~30 parts. Per-face part indices keep every per-part override
(coil glow, bubble fade, dim, hidden, section, highlight) working.
```

### `_prep_mesh`

```
One-time render caches for a Mesh: a padded (nf, w) face-index array
(short faces repeat their last vertex so means stay exact through flen),
a static world-verts cache for non-spinning meshes, and a closed-manifold
flag used for backface culling. A mesh is cullable only if every edge is
shared by exactly two faces traversed in opposite directions (consistent
winding); signed-volume sign tells whether its faces are outward-wound, so
inward-wound solids still cull the right side.
```

### `_prep_part`

```
Collapse a Part's static meshes into one big indexed mesh per draw
class (solid / wire). The painter used to loop ~900 meshes a frame and
paid small-array numpy overhead on each; now it iterates ~30 parts.
Per-face attributes the old per-mesh code varied -- base colour, coil
index, glow/hot flags, closed-manifold cullability -- are preserved as
per-face arrays, and every face's winding is normalised outward so a
single backface test works across the merge. Spinning meshes stay
individual so they still rotate.
```

### `_print_traversal`

```
Print one traversal result compactly.
```

### `_radial`

```
Rotation taking a +Z-built primitive to point radially outward.
```

### `_real`

```
Coerce a would-be numeric to float; non-convertible -> NaN.  Lets the
formatters and magnitude helpers print 'nan' honestly instead of raising
TypeError on a poisoned ledger value (str, None, list, complex).
```

### `_rgb`

```
Coerce any colour-ish value to a valid RGB triple; a channel that is
missing, non-numeric or non-finite drops the whole colour to fallback.
```

### `_ring_wire`

```
A single closed wire loop -- used for the bubble shell and grid rings.
```

### `_rod`

```
A capped cylinder between two arbitrary points -- whips, struts and
the flux capacitor's three arms.
```

### `_runtime_state_lines`

```
Every field the live simulation carries -- WarpCore (the drive) and
Voyage (the mission) -- plus the envelope check, the complete control
bindings and the CLI. These are the data the viewer animates and the
honesty audit inspects.
```

### `_sech2`

```
1/cosh^2(x), overflow-safe. math.cosh overflows past ~710; sech^2 is
already indistinguishable from zero by |x| ~ 40, so clamping is exact to
double precision.
```

### `_smooth_sections`

```
Catmull-Rom subdivision of (z, radius) control points -> a smooth loft.
```

### `_solid_cylinder`

```
Capped cylinder about +Z.
```

### `_spec_key_lines`

```
Every key of DIMS, PLANT and DRIVE with the engineering comment that
sits next to it in this file -- parsed out of the source itself so the
panel documents 100% of the specification and can never ship a stale
parts list. Falls back to key = value if the source is unavailable
(frozen build, stripped install).
```

### `_sphere`

```
UV sphere about the origin; `squash` scales Z (oblate hull domes).
```

### `_tangential`

```
Rotation taking a +Z-built primitive to lie ALONG the ring tangent at
this angle -- how a coil wraps a torus.
```

### `_tilt_z`

```
Rotate an Earth-fixed vector (equatorial frame, z = pole) into the
ecliptic frame by the obliquity -- the same tilt the offset uses.
```

### `_torus`

```
Torus (or torus ARC from a0 to a1) in the X-Y plane about +Z.
R = centreline radius, r = tube radius. The warp ring, the shaping rings,
the reactor torus and the SMES store are all built from this one call.
```

### `_trender`

```
font.render with a bounded surface cache: the UI redraws a few
hundred labels a frame and ~90% of them are static strings.
```

### `_wire_ellipsoid`

```
Bubble wireframe: latitude ellipses plus three meridian loops, axes
(a, b, c) along (x, y, z) -- the car's long axis is z.
```

### `_xform`

```
Bake a rotation and/or translation into a vertex list. Used for parts
that sit at an arbitrary orientation and do NOT spin (the tangential field
coils, the radial pylons, the radiator panels), so no per-frame transform
is needed for them at all.
```

### `_xy`

```
Coerce a position-ish value to a finite (x, y) float pair or None.
```

### `alcubierre_energy_j`

```
Total (negative) energy of the Alcubierre warp field  [J].
E = -(c^4 beta^2 / 12 G) * INT r^2 f'^2 dr. Sanity anchor: with R = 100 m,
beta = 10 and a Planck-ish 1e-15 m wall this returns about -3e63 J, which
is Alcubierre's own 1994 order-of-magnitude estimate (~10^64 J). The
--selftest asserts exactly that.

Cached on (beta, R, delta): the 4000-sample Simpson integral is expensive
and the panel calls this every frame for a value that only changes when
the bubble radius or wall thickness changes.
```

### `bar`

```
Horizontal bar with optional threshold markers.

The lo/hi threshold markers (yellow tick lines) come from GmansRunV1.17
and SE.py: they mark safe-operating-range bounds on the same bar as the
current value, so you can see at a glance whether you are inside the
limit. The single `mark` is kept for backward compatibility (it marks
a target or setpoint).
```

### `barrier_analysis`

```
Returns a dict of barrier -> {value, threshold, gap, passable, route}.

This is the engineering audit: for each of the five hard barriers that the
feasibility scorecard marks FAIL, we state the exact number, the exact
threshold, the gap in orders of magnitude, and what a hypothetical route
past it would require.  The routes are not proposed as solutions -- they
are stated so the reader can see what 'past the barrier' would mean.
```

### `barrier_scorecard`

```
Returns a list of (name, status, detail) for the 8 barriers.
status is one of: PASS, FAIL, THEOREM, CONJECTURE.
```

### `beam_brake_force_n`

```
Photon-pressure braking against an array AT THE DESTINATION [N].

    F = 2 P_captured / c        (perfect reflector)

Forward (1984) proposed exactly this for staged lightsails, and it is the
only known way to stop a heavy interstellar payload in useful time. Note
what it costs: a second stellar-scale transmitter, already built, at a star
nobody has visited. Interstellar RENDEZVOUS is an infrastructure problem at
both ends; interstellar FLYBY is not. The model makes you choose, and says
which one you chose on every frame.
```

### `beam_brake_time_s`

```
Rough time to stop under destination-array photon braking [s].
```

### `beam_capture_frac`

```
Fraction of the beam the deployed rectenna actually intercepts.
```

### `beam_spot_m`

```
Diffraction-limited spot diameter of the stellar-tap boost beam [m].
    d_spot = 2.44 lambda L / D
(Airy). With a 1000 km transmitter at 1 um, the spot is already 2.8 km wide
at a tenth of a light year -- which is exactly why the rectenna has to
unfurl to 4 km and why the boost phase has a hard range limit.
```

### `boost_profile`

```
Can the stellar tap actually get this ship to beta before the ship flies
out of the beam? Integrates the boost explicitly.

Two clocks race each other. The energy clock says you need (gamma-1) M c^2
delivered at the captured beam power. The range clock says you are moving
away the whole time, the diffraction spot grows linearly with distance, the
captured fraction falls as 1/L^2, and past beam_range_ly there is no useful
beam at all. Whichever runs out first decides your cruise speed -- and no
amount of onboard cleverness changes it, because the ship cannot carry the
energy. This is the real speed limit of the design, and it is emergent:
nothing in DIMS names a maximum beta.
```

### `build_portal_parts`

```
The portal gate at true scale, plus the spacetime it claims to make.
`detail` rescales VISUAL_DETAIL for this build only (interaction LOD).
```

### `build_ship_parts`

```
Build every part of the WD-1 to scale. Returns an ordered list of Part.
`detail` rescales VISUAL_DETAIL for this build only -- the renderer uses it
to draw a coarse model while the camera is moving.
```

### `build_special_parts`

```
The WD-88 Foldmobile at true car scale, meshed at CAR_MODEL_DETAIL
(2x) base resolution. The upscale refines the MODEL only -- double the
tessellation on every primitive, not a millimetre moved: the car stays
at 100% scale. `detail` rescales VISUAL_DETAIL on top of that for this
build only (interaction LOD).
```

### `buildability_ledger`

```
Every line of the mass budget, rated for when it could actually be
built -- plus the infrastructure the ship depends on but does not carry.

Statuses: TODAY (hardware exists, only scale is missing), NEAR (physics
proven, engineering not yet demonstrated -- order of ten to thirty
years), FAR (needs an industry that does not exist), OPEN (a materials
problem nobody has solved), IMPOSSIBLE (barred by theorem). Each line is
rated on its hardest role, not its easiest. Each row carries a `needs`
string with the quantities the line actually demands, derived live from
DIMS so the ledger cannot drift out of sync with the ship.
```

### `car_casimir_j`

```
Negative energy the conduit-liner strips actually hold [J] -- same
plate-gap physics as the ship's lattice, honest volume scaling.
```

### `car_fault_effects`

```
What each injected fault does, in physics terms -- the same failure
modes the ops ledger promises, made live.
  'smes'   : puck quench -- no spike capacity, 88 mph is just driving
  'louver' : louver stall -- rejection area cut to 12%, cell heat-soaks
  'nav'    : ephemeris drift -- the transit solve is lost
```

### `car_mass_budget`

```
The kerbside mass, derived the way the ship's is: every line is a
volume x density or a counted unit, and the fit-out line is the balance
that closes the book to CAR_MASS_KG. The selftest re-audits it.
```

### `car_mph_step`

```
One tick of road speed [mph]. Returns (mph, fired_now). Hub motors
pull +30 mph/s under throttle, regen brakes at -45 mph/s, rolling drag
bleeds -5 mph/s; top speed 130. At 88 mph exactly the field transition
fires -- but only while armed: a quenched SMES has no spike capacity,
so 88 mph is just driving. A heat-soaked cell derates the drive at
55 mph before it trips. Hostile inputs (nan, negative speeds) are
recovered, never trusted.
```

### `car_ops_ledger`

```
(part key, electric draw W, duty, failure mode) -- the same per-system
operations accounting the ship carries in operations_ledger(), scaled
to a road car. Negative draw = a supply line.
```

### `car_part_mass`

```
Map every car part onto lines of car_mass_budget() so each spec card
can show a derived mass, not a typed one.  Field/record/ground parts
carry no booked mass; the 'crew + fluids + fit-out' balance line is the
occupants and fit-out, reported on the panel instead of a part card.
```

### `car_power_budget`

```
Loads vs the fusion cell: every ops-ledger draw summed, supply
subtracted. A negative margin would mean the car is unfunded and the
selftest flags it -- same honesty rule as the ship.
```

### `car_thermal_step`

```
One Euler step of the trunk cell's thermal balance [K]. The louver
bank rejects waste heat the same way the ship's fins do -- Stefan-
Boltzmann, outward only. louver_eff < 1 models the ops-ledger 'louver
stall' fault: rejection area collapses and the cell heat-soaks.
Hostile inputs are bounded, not trusted: a giant dt can never carry
the cell past its own radiative equilibrium, and nothing aboard is
still a solid past 6000 K, so the sim stops pretending above it.
```

### `car_transit`

```
Solve the landing: the car must arrive at the SAME Earth-fixed road
coordinate, which sits at a different inertial position at t1 = t0 + hop.
Returns the departure/arrival positions and the transit vector the bubble
has to carry the car through, split into orbital and rotational parts.
```

### `car_trigger_v`

```
88 mph in SI -- the speed the run is armed at.
```

### `casimir_cassette`

```
Geometry and yield of ONE onboard Casimir cassette.
```

### `casimir_energy_density`

```
Casimir vacuum energy density between ideal parallel plates  [J/m^3].
    rho = -pi^2 hbar c / (720 a^4)
(Casimir 1948.) Measured to a few percent by Lamoreaux 1997 and Mohideen
and Roy 1998, so unlike everything else on the exotic side of this file it
is real. At a 10 nm gap it is about -43 kJ/m^3.
```

### `casimir_onboard_j`

```
Total negative energy the whole 24-cassette lattice actually holds [J].
This is the largest real negative-energy reservoir known to engineering,
and the model compares it -- to the joule -- against what a warp bubble
demands. The comparison is the single most important number in this file.
```

### `chain_wormhole_offset`

```
Cumulative time offset from a chain of N wormholes in series  [s].

Each wormhole contributes offset_i = elapsed * rate_diff_i.  Stepping
through all N gives offset_total = N * elapsed * rate_diff.  This is the
ONLY way to exceed elapsed-time displacement without a different mechanism:
with N=10 mouths each desynchronized by 0.911 (neutron-star well + 0.99c
rocket), 100 years of desynchronization yields ~911 years of offset.

The exotic-energy bill scales as N * (energy per throat), and every
wormhole still needs to satisfy the QI bound -- the chain multiplies the
payoff without touching any barrier.
```

### `check_envelope`

```
Does the ship still fit inside its own flat interior?

A thicker wall is cheaper and gentler but shrinks the usable volume, so
this is a live constraint, not a build-time one: drag the wall thickness up
in METRIC view and the ship's own radiators eventually end up standing in
the wall. Returns the binding part and the margin.
```

### `chip`

```
A small toggle pill with accent border on the active state.

Matches the reference tab style (GmansRun/SE): active tabs get a filled
background PLUS a brighter accent border, so the active tab reads as
selected even at a glance. Inactive tabs get a thin outline only.
```

### `clock_ledger`

```
Every clock in the problem, at one instant.

Returns rate ratios relative to a clock at rest at infinity, plus the
accumulated drift against Earth. The point of the table is that 'no time
dilation' is a statement about ONE row of it.
```

### `contrast_text`

```
Pick a readable text colour for a given background.

Returns the light text colour if the background is dark, the dark colour
if it is light -- the WCAG-style luminance threshold that keeps HUD text
legible whether it sits on a dark panel or a bright filled bar.
```

### `crossing_time_s`

```
Coordinate time for Sol -> Proxima at beta. inf when the boost
configuration cannot fly at all (dead beam, zero mass, nan beta).
```

### `cruise_load_w`

```
Electrical load to HOLD the warp field at beta [W].

Coil AC losses scale with the square of the field (hence beta^2); the
metric servo that keeps the shell sectors in shape scales roughly
linearly; cryo and hotel loads are constant. Holding a constant beta is
cheap in principle -- the cost here is engineering imperfection (ripple,
control, refrigeration), not general relativity.
```

### `ctc_by_gravity_well`

```
Park one mouth in a deep well instead. Returns the onset time.
```

### `ctc_by_warp_transport`

```
Can you make a time machine by CARRYING one mouth on this warp drive?

No -- and for an interesting reason. The desynchronisation trick needs the
travelling mouth to age differently, and a warp bubble's interior is flat:
the mouth comes back in step. A relativistic ROCKET would do it easily. So
the warp drive, which is the fast thing, is the one that cannot build the
causality violation, while the slow thing can. The two subsystems in this
file interact, and this is how.
```

### `ctc_exists`

```
Do closed timelike curves exist right now?

MTY 1988: CTCs exist the instant the clock offset between the mouths
exceeds the light-travel time between them.  Before that, stepping through
arrives in mouth B's past relative to A's present, but NOT in your own
past -- no paradox is possible.  After that, you can step through and
arrive before you left, which is a time machine.

Hawking's chronology protection conjecture (1992) expects vacuum
fluctuations to diverge at exactly this boundary and destroy the throat.
Unproven -- but it is why most physicists expect the answer to be no.
```

### `ctc_onset_s`

```
Time until a two-mouth wormhole becomes a TIME MACHINE  [s].

Morris, Thorne & Yurtsever (1988). Hold the two mouths at different clock
rates -- park one in a gravity well, or fly it around -- and they
desynchronise. The instant the accumulated offset exceeds the light-travel
time between them, closed timelike curves exist and you can send signals
into your own past.

    t_onset = (D / c) / |rate difference|

This is not an exotic add-on to wormholes. It is automatic. Any traversable
wormhole plus ordinary relative motion equals a time machine, which is why
Hawking proposed the CHRONOLOGY PROTECTION CONJECTURE (1992): vacuum
fluctuations should pile up without bound in the CTC-forming region and
destroy the throat at exactly the moment it would first close. Unproven --
but it is the reason most physicists expect the answer to be no.
```

### `draw_bubble_glow`

```
Soft concentric halo for the active warp shell.

Uses additive blending (BLEND_RGBA_ADD) after the pattern of LS.py's
plasma-blade glow: the halo ADDS light to whatever is behind it rather
than overpainting, so the bubble reads as luminous over the starfield
instead of as a dim coloured disc.

The glow now PULSES with a 2-second period (driven by pulse_phase) to
convey the active field state, and uses 10 layers with a sharper core
and softer falloff for a more cinematic energy-field look.
```

### `draw_vignette`

```
Subtle corner darkening for cinematic depth.

Paints a radial alpha gradient (transparent centre, dark edges) onto a
full-screen SRCALPHA surface and blits it once per frame. The effect is
the same trick the companion twins use to focus the eye on the central
viewport: the starfield fades into shadow at the bezel without a hard
border. Cached on the surface size so it is rebuilt only on resize.

Modernized: smoother quadratic falloff and finer grid for a more
cinematic, less banded vignette.
```

### `earth_helio_pos`

```
Heliocentric ecliptic position of Earth at time t [s]. Kepler orbit to
first order in eccentricity: r = a(1 - e cos M), true anomaly theta =
M + 2e sin M, with M = 0 (perihelion) at t = 0.
```

### `earth_surface_offset`

```
Position of a road-fixed point relative to Earth's centre: sidereal
rotation about the pole, with the pole itself tilted 23.44 deg to the
ecliptic -- so the road's inertial track has a real out-of-plane leg.
```

### `energy_conditions`

```
Which pointwise energy conditions the commanded solution satisfies.

beta < 1  -> the Bobrick and Martire (2021) / Fuchs et al. (2024) class:
             a positive-energy massive shell with a shift-vector
             distribution. Constructed specifically to satisfy NEC, WEC,
             DEC and SEC. Real matter. Buildable in principle.
beta >= 1 -> Santiago, Schuster and Visser, 'Generic warp drives violate
             the null energy condition' (Class. Quantum Grav. 39 075006,
             2022): ANY superluminal warp drive violates the NEC somewhere.
             Not a limitation of Alcubierre's particular ansatz -- a
             theorem about the whole class.
```

### `energy_density`

```
Eulerian energy density T^00 measured by observers at rest  [J/m^3].

    T^00 = -(c^4 / 8 pi G) * (beta^2 rho^2) / (4 r_s^2) * (df/dr_s)^2

(Alcubierre 1994 eq. 12, restored to SI.) Note the leading MINUS SIGN: it
is not a sign convention and it is not removable. Every superluminal warp
metric ever written down has it. rho = sqrt(y^2 + z^2) is the distance from
the direction-of-travel axis, so the negative energy is concentrated in a
torus around the equator of the bubble wall -- not spread over the shell.
```

### `equiv_mass_kg`

```
E/c^2 -- the mass whose rest energy equals this. Sign is preserved,
because a negative energy requirement means NEGATIVE MASS, and that is
the whole problem.
```

### `feasibility_scorecard`

```
Function-by-function honest scorecard, in the style of LS.py's
--engineer report: what this drive really does, really cannot do, and what
is merely very expensive.
```

### `flat_interior_r`

```
Radius of the exactly-flat interior [m].

DERIVED, not declared. With a wall of thickness delta at radius R, the
shape function is already 0.9997 by R - 6 delta, so that is where the
usable volume ends. This is the trade nobody mentions: a THICKER wall is
cheaper (energy falls as 1/delta) and gentler (tidal shear falls as
1/delta^2), but it eats the interior. Push the wall past about 3 m and the
ship no longer fits inside its own bubble -- watch the envelope readout in
SHIP view do exactly that.
```

### `ford_roman_bound_j_m3`

```
Ford-Roman quantum inequality bound on negative energy density  [J/m^3].

    |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)

This is the maximum NEGATIVE energy density a massless field can sustain,
averaged over a sampling time tau. At tau = 1 s it is about -3.7e-62 J/m^3 --
roughly 102 orders of magnitude below what a 12 m throat demands (-3.3e40
J/m^3). The throat needs to be held open for the traversal time (seconds),
and the QI bound at that duration is so far below the requirement that the
gap is itself the result: you cannot hold a human-scale throat open long
enough to cross it, even in principle, with quantum-field negative energy.
```

### `ford_roman_max_throat_tau`

```
Longest you can hold a throat of radius b0 open, by the QI bound  [s].

The throat demands |rho| = c^4 / (8 pi G b0^2). The QI bound supplies at
most 3 hbar / (32 pi^2 c^3 tau^4). Setting them equal and solving for tau:

    tau_max = (3 hbar G b0^2 / (4 pi c^7))^(1/4)

For b0 = 12 m this is ~3e-26 s. The traversal takes ~4.8 s. The throat
closes ~1e26 times before you are halfway through. This is the Ford-Roman
result applied to wormholes, and it is the deepest 'no' in the portal
section: not 'we lack a source' but 'the source is forbidden by
quantum field theory from lasting long enough'.
```

### `ford_roman_wall_limit`

```
Quantum-inequality bound on the wall thickness  [m].

Ford and Roman (1996) proved that a quantum field can only hold negative
energy for a time inversely proportional to its magnitude. Pfenning and
Ford (1997) applied that inequality to the Alcubierre bubble specifically
and found the wall cannot exceed a few hundred Planck lengths thick --
which is what makes the energy bill astronomical rather than merely huge.
Returned as an order-of-magnitude bound, not a precise threshold; the exact
coefficient depends on the sampling function chosen.
```

### `fusion_fuel_kg`

```
D-3He mass burnt to deliver this much ELECTRICAL energy.
```

### `gott_pair_offset`

```
Gott (1991) two cosmic strings: maximum time displacement  [s].

Two cosmic strings of mass-per-length mu moving past each other at
velocity v produce CTCs.  The time displacement for a round trip of
proper length D between them is:

    delta_t = 4 * pi * G * mu * D / c^2  (deficit-angle formula)

The deficit angle is delta = 8 pi G mu / c^2, and the displacement
is bounded by delta * D / (4 pi) -- the geometry cannot produce
more than the deficit angle times the path length.  For a GUT-scale
string (mu ~ 1e21 kg/m) at v = 0.5, a round trip of 1 light-year gives
delta_t ~ 3e4 s -- hours, not years.  The mechanism is real but the
payoff is small unless D is astronomical.
```

### `grav_potential_at`

```
Newtonian potential Phi at distance x along the Sol -> Proxima line
[J/kg]. Negative everywhere. Used for the gravitational red/blue shift, so
only DIFFERENCES along the route matter.
```

### `grav_rate`

```
Clock rate dtau/dt at position x relative to a clock at infinity.

    dtau/dt = sqrt(1 + 2 Phi / c^2)   (weak field)

Deeper in a well means a slower clock. This is the environmental dilation
the crew actually experience, and it is the ONLY reason their clock and
Earth's clock disagree at all.
```

### `horizon_locked`

```
True when the forward bubble wall is causally disconnected from the ship.

For beta > 1 the front of the bubble outruns light signals sent from the
interior, so the crew CANNOT send the control signal that would reshape or
dissolve the forward wall (Everett 1996; Coule 1998; Krasnikov 1998). The
entire trajectory must be pre-laid before departure. In FLIGHT mode the
helm physically locks above |beta| = 1 for exactly this reason.
```

### `ism_blast_energy_j`

```
Energy stored in the swept particles, released forward on bubble
collapse [J]. The 2012 paper's headline result: a warp ship arriving at its
destination discharges its accumulated wall load as a beam. This model
scales the per-particle energy as beta^2/2 m c^2 -- a deliberately
CONSERVATIVE floor, since the true spectrum is set by the wall's blueshift
and is worse.
```

### `ism_d3he_yield_kg_s`

```
D-3He reactor-grade fuel mass yieldable per second of scooping [kg/s].

ISM gas is isotope-lean: D/H ~ 2e-5, He/H ~ 0.09, 3He/4He ~ 2e-4.
After perfect isotope enrichment the D-3He-mix yield is:
    min( m_D / 0.4,  m_3He / 0.6 )
i.e. whichever isotope is scarcer caps the mix (mixing ratio 2:3).
This is the honest number for 'refuel while flying': the raw gas flux
is ~6 kg/day at cruise, but the reactor-grade fraction is ~1e-4 of it.
```

### `ism_particles_swept`

```
Protons the bubble sweeps up over a leg. They do not pass through: the
wall collects them (McMonigal, Lewis and O'Byrne, Phys. Rev. D 85 064024,
2012, 'The Alcubierre warp drive: on the matter of matter').
```

### `ism_scoop_gas_kg_s`

```
Raw ISM mass flux intercepted by the magsail loop while underway [kg/s].

    mdot = A_loop * n_ISM * m_p * v

Same Bussard-collector geometry as magsail_drag_n(): the loop sweeps
A*v of space per second.  This is the raw gas capture rate BEFORE
isotope enrichment -- mostly protium and 4He.
```

### `kerr_ctc_offset`

```
Kerr black-hole CTC: maximum time displacement per orbit  [s].

The interior of a rotating black hole (Kerr metric, spin parameter
a = J/(Mc) in metres) contains a ring singularity.  Worldlines
threading the ring can close on themselves in time.  The time
displacement per orbit at radius r is bounded by the frame-dragging
rate; for a near-extremal Kerr (a -> GM/c^2) the maximum displacement
per orbit approaches:

    delta_t_max = 2 * pi * a / c  (bounded by the spin period)

The displacement is NOT divergent -- it is bounded by the black
hole's angular momentum.  For a 10 solar-mass extremal Kerr
(a = 1.5e4 m), one orbit gives ~0.3 ms of displacement.  Multiple
orbits add linearly.  The ring singularity is inside the inner
horizon, which is unstable and likely destroyed by mass inflation
(Poisson-Israel 1990) -- so this is a mathematical result about the
Kerr metric, not a buildable time machine.
```

### `kinetic_energy_j`

```
(gamma - 1) M c^2 -- the honest, unavoidable bill for CHANGING velocity.

A constant-velocity warp solution is a stationary spacetime and costs
nothing to hold (Bobrick and Martire 2021, section 4). Changing velocity
is another matter: the ADM energy and momentum of the whole configuration
change, and that change has to come from somewhere outside the ship. This
function is what the FLIGHT mode charges you, and there is no discount.
```

### `lapse_static`

```
dtau/dt for an observer holding station in the EXTERNAL frame at radius
r from the bubble centre.

    dtau/dt = sqrt(1 - beta^2 f(r)^2)

Deep inside (f = 1) this is the full Lorentz factor; outside (f = 0) it is
exactly 1. Superluminal beta makes the argument negative -- the static
worldline stops being timelike at all, which is the horizon problem showing
up in the arithmetic rather than in a footnote.
```

### `log_bar_x`

```
Map |E| onto a log10 axis across a pixel span.
```

### `magsail_decel_time_s`

```
HONEST time to brake from beta down to arrival speed on the magsail [s].

    M dv/dt = -k v^2   ->   t = (M/k) (1/v_f - 1/v_0)

Drag falls as v^2, so the brake fades exactly as you need it most and the
integral is dominated by the LAST decade of speed, not the first. The
halving time is ~65 yr; the time to actually stop is ~32,600 yr. Reporting
the first number and calling it 'braking time' is the single most common
way interstellar mission studies flatter themselves, so this model reports
the second -- and then tells you what to do about it (a destination array;
see beam_brake_force_n).
```

### `magsail_drag_n`

```
Drag of the magnetic sail against the interstellar medium [N].

    F = Cd * rho_ISM * v^2 * A_eff

Zubrin and Andrews (1991). rho_ISM = n m_p at 0.1 protons/cm^3. The loop
deflects incoming protons; their momentum change is the brake. It is a
genuinely tiny force -- and it is still the largest deceleration authority
this ship has by six orders of magnitude, which tells you everything about
interstellar flight.
```

### `magsail_halving_time_s`

```
Characteristic time for the magsail to HALVE the speed [s]: t = M/(k v0).
Quoting this as 'the braking time' is the classic way to make magsail
braking look feasible. It is not the time to stop -- see below.
```

### `mass_budget`

```
Component-by-component dry mass, computed from the geometry the renderer
draws. No component mass is typed in as a number -- each is a volume times
a density, so changing a dimension changes the ship's mass, its kinetic
energy bill, its radiator sizing and its voyage, all at once.
```

### `max_boost_beta`

```
Highest cruise beta the beam can actually deliver, by bisection on
boost_profile(). EMERGENT, not configured: it falls out of the transmitter
aperture, the wavelength, the tap power and the ship's mass.

Cached: the result only changes when DIMS/PLANT/ship_mass_kg() change, so
the cache key is a snapshot of the relevant parameters.  The panel calls
this twice per frame; without caching that's ~13700 integration steps
per frame for a value that changes only on user input.
```

### `max_time_displacement`

```
Maximum time displacement across all mechanisms  [s].

Compares every time-machine construction in the model and returns
the largest displacement for the given parameters.  This is the
'engineering-maximal' answer: which mechanism gives you the most
displacement for a single traversal.
```

### `mmp_extremal_charge_c`

```
Extremal magnetic charge for a black hole of mass M  [C].

    Q_ext = sqrt(4 pi eps0 G) M

Above this the BH has no horizon (a naked singularity), so the construction
requires Q <= Q_ext, and nearly extremal means Q/Q_ext -> 1.
```

### `mmp_summary`

```
The MMP wormhole, fully priced, for a survivable crossing.
```

### `mmp_tidal_mass_kg`

```
Smallest MMP black hole a person survives crossing  [kg].

The throat of a near-extremal magnetically charged hole sits at r ~ 2GM/c^2
(the Schwarzschild radius; for extremal RN the inner and outer horizons
coincide at GM/c^2, but the traversable throat MMP construct has curvature
radius of order the Schwarzschild scale). The tidal acceleration across a
body of length L is:

    a ~ c^2 L / r_throat^2 ~ c^6 L / (4 G^2 M^2)

Setting this to g_limit * 9.81 and solving:

    M >= c^3 sqrt(L / (4 G^2 g))

This comes out to ~9e34 kg, about 46,000 solar masses -- large, but the
same CURVATURE RADIUS as the Morris-Thorne survivable throat (r ~ 1.4e8 m),
reached from a completely different construction. The difference is that
here the negative energy comes from a real quantum field (Casimir energy of
massless fermions), and the price is paid in magnetic monopoles instead.
```

### `mmp_traversal_time_s`

```
Asymptotic traversal time for the MMP wormhole  [s].

MMP give the traversal time as of order the black-hole mass in natural
units, t ~ GM/c^3, up to a logarithmic factor from the long throat. For a
solar-mass hole this is ~5 microseconds -- but the traveler must be
boosted to gamma ~ M/m_e (the fermion Casimir energy is only negative in
the boosted frame), and the asymptotic observer sees a longer time. The
log factor is ~ ln(M / M_planck) ~ 87 for a solar mass, which is why the
'years' figure appears in popular summaries: the full traversal as seen
from outside is t ~ (GM/c^3) * ln(M/M_planck), still under a millisecond
for a solar mass, but the setup (boosting, alignment) is the slow part.
```

### `mouth_clock_rate`

```
Proper-time rate of a wormhole mouth relative to a clock at infinity.

Two independent contributions, both real and both measured:
  - GRAVITATIONAL:  dtau/dt = sqrt(1 + 2 Phi / c^2)  (weak field)
    Parking a mouth deep in a gravity well slows its clock.  GPS
    satellites measure 45 microseconds/day of this effect (the GR part).
  - KINEMATIC:      dtau/dt *= 1/gamma(beta)  (special relativity)
    Moving a mouth at relativistic speed slows its clock.  GPS satellites
    measure 7 microseconds/day of this effect (the SR part).

A warp drive does NOT contribute: the interior of a warp bubble is flat
spacetime, so a mouth carried by warp ages at the same rate as one at rest
in the same gravitational potential.  This is ctc_by_warp_transport() in
arithmetic form: the fast thing cannot desynchronise the mouths.

phi_over_c2:  gravitational potential Phi/c^2 at the mouth's location
              (negative in a well; 0 in flat space; -0.5 at a horizon)
beta:         velocity of the mouth relative to the external frame
```

### `mouth_time_offset_s`

```
Accumulated clock offset between the two mouths  [s].

Positive means mouth B is BEHIND mouth A (B has aged less).  Stepping
through A -> B then arrives at B's past relative to A's present -- which
is the seed of the time machine.  The offset is:

    delta_t = elapsed * (rate_a - rate_b)

and it grows LINEARLY with elapsed coordinate time.  This is not
speculative: it is the same gravitational + kinematic dilation that GPS
corrects for every day, applied to two clocks that started synchronised.
```

### `mt_embedding_z`

```
Embedding-diagram height z(rho) for the Morris-Thorne throat [m].

    dz/drho = 1 / sqrt(rho/b0 - 1)   ->   z = 2 b0 sqrt(rho/b0 - 1)

This is the classic funnel shape, and the PORTAL view draws it as a real
surface of revolution rather than as decoration: every vertex comes from
this line.
```

### `mt_exotic_energy_j`

```
Total exotic energy to hold a throat of radius b0 open  [J].

Order-of-magnitude: the throat energy density times a throat-scale shell,

    E ~ rho_throat * (4/3) pi b0^3 = -c^4 b0 / (6 G)

Note what that says: the bill scales LINEARLY with throat radius, so a
wormhole you can walk through costs a fixed price per metre of aperture,
and that price is 2e43 joules per metre. Visser (1995) gets the same scale
by a different route. Computed by the closed form -c^4 b0 / (6 G): at b0=0
the density diverges but the volume vanishes faster, so the bill is 0 --
evaluating rho * V literally would produce -inf * 0 = NaN.
```

### `mt_flare_out`

```
Verify the flare-out condition at the throat.

    b'(r0) < 1    and    b(r0) = r0

Returns (b_at_throat, b_prime_at_throat, satisfied). For b(r) = b0^2/r the
throat is at r0 = b0, b(r0) = b0 exactly, and b'(r0) = -1, which is < 1.
The condition is satisfied -- and it is STILL the thing that demands
negative energy, because the Riemann tensor component it forces is the one
the Einstein equations read as rho < 0. A nonpositive throat radius has no
throat at all -- nothing to verify.
```

### `mt_min_throat_m`

```
Smallest throat a person survives crossing  [m].

    b0 >= sqrt(c^2 L / g_limit)

At one Earth gravity of tidal stress across a two-metre body this returns
about 1.4e8 m -- a throat roughly ten Earth diameters across. That is
Morris & Thorne's own conclusion, and it is why 'portal' and 'doorway' are
not the same word.
```

### `mt_proper_length`

```
Proper radial distance from throat to r_far  [m].

    l = integral_{b0}^{r_far} dr / sqrt(1 - b(r)/r)

For b(r) = b0^2/r this is the arc length of the embedding funnel. With
r_far = 4 b0 (the embedding diagram's extent) it comes out to a few b0,
which is why mt_traversal_time_s uses length_factor ~ 4. The integrand
diverges at the throat, so quadrature carries a persistent few-percent
bias -- but it has a closed form: INT r dr/sqrt(r^2-b0^2) = sqrt(r^2-b0^2),
giving exactly sqrt(r_far^2 - b0^2).
```

### `mt_redshift_phi`

```
Redshift function Phi(r)  [dimensionless].

Phi = 0 is the zero-tidal-at-throat choice Morris & Thorne use for their
'interstellar travel' example. With Phi = 0 the proper-time radial tidal
acceleration at the throat is exactly c^2 L / b0^2 -- the number
mt_tidal_g() already reports. A nonzero Phi would add a gravitational
redshift contribution but does not remove the flare-out requirement, so
this is the honest baseline.
```

### `mt_shape_b`

```
Morris-Thorne shape function b(r)  [m].

    b(r) = b0^2 / r

This is the canonical textbook choice (Morris & Thorne 1988, eq. 12). It
satisfies b(b0) = b0 (throat at r = b0), b'(r) = -b0^2/r^2 < 0 everywhere
(so b'(b0) = -1 < 1, the flare-out condition), and b/r -> 0 as r -> inf.
The embedding diagram this produces is exactly the funnel drawn by
mt_embedding_z() above.
```

### `mt_shape_b_prime`

```
db/dr for the shape function  [dimensionless].
```

### `mt_throat_density`

```
Energy density required at the throat  [J/m^3].

    rho_throat = -c^4 / (8 pi G b0^2)

Negative, and it gets WORSE for small throats -- exactly backwards from
what you would want, and the reason a pocket-sized portal is harder than a
planet-sized one. A zero throat is the divergent limit: -inf.
```

### `mt_tidal_g`

```
Tidal acceleration across a body of height body_m at the throat [g].

    a_tidal ~ (c^2 / b0^2) * L

The curvature radius at the throat IS b0, so a small portal is a very
sharply curved region and anything crossing it is torn apart. This is the
constraint everyone forgets and Morris & Thorne did not. A zero throat is
a point of divergent curvature: infinite shear.
```

### `mt_tidal_profile`

```
Radial tidal acceleration across body_m at radius r  [g].

    a_radial = c^2 |b'(r) - b(r)/r| L / (2 r^2 e^(2 Phi))

At the throat (r = b0, Phi = 0): b' = -1, b/r = 1, so |b' - b/r| = 2,
giving a = c^2 L / b0^2 -- exactly mt_tidal_g(). Away from the throat the
tidal force falls as 1/r^4. This function gives the full profile so the
viewer can draw the tidal gradient as a field, not just a single number.
```

### `mt_traversal_time_s`

```
Proper time to walk through, at v_ms, across ~length_factor throats.
```

### `multijump_breakeven_s`

```
Fixed point of the backward recurrence: t* = Delta / rate_diff  [s].

While the current offset r*t exceeds the external return time Delta,
each cycle goes net-backward; below t* the return leg eats the jump and
each cycle drifts FORWARD despite hopping into the past.  Backward
travel asymptotes at coordinate t* -- the earliest reachable moment.
```

### `multijump_plan`

```
Iterated portal traversal: the multi-jump ledger.

direction="backward": each cycle steps A->B (arrive delta in the past),
then flies externally B->A at beta, then rejumps.  Recurrence
t_{k+1} = t_k (1-r) + Delta, converging to the breakeven t* = Delta/r.

direction="forward": each cycle steps B->A (arrive delta in the future),
then flies externally A->B, then rejumps.  Recurrence
t_{k+1} = t_k (1+r) + Delta, geometric (1+r)^k growth.

Each cycle's ship energy is cruise_load_w(beta) * Delta -- constant-beta
warp is a stationary spacetime and costs nothing to HOLD; the real bill
is housekeeping while the return leg runs.  Fuel burnt = fusion_fuel_kg;
fuel scooped = ism_d3he_yield_kg_s(beta) * Delta (enrichment-complete).
The exotic throat energy per hop is reported but NOT charged to the
ship ledger -- it is flagged separately because no ship reactor can pay
it (that is the physics barrier, distinct from ship fuel).
```

### `nested_wormhole_offset`

```
Offset from a wormhole nested inside another wormhole  [s].

If wormhole B is carried inside wormhole A, its clocks run at B's
rate *relative to A's frame*.  The effective displacement compounds:
total offset = outer + inner * (1 - rate_B).  In the limit that the
inner wormhole sits at a black-hole horizon (rate_B -> 0), the
nested offset approaches outer + inner -- still additive, not
multiplicative.  The amplification is bounded by the sum of the
individual offsets, not their product.
```

### `operations_ledger`

```
What each mass line needs to OPERATE, not just to be built: power
drawn, duty cycle, and the honest consequence when it fails. Power
figures are taken from the same PLANT breakdown that cruise_load_w
sums, so the operations sheet cannot disagree with the power budget.
```

### `orders_of_magnitude`

```
log10 |a/b| -- the model's favourite unit, because the gap between what
a warp drive needs and what physics supplies is always measured in it.
```

### `panel`

```
Semi-transparent panel with rounded border, gradient fill, and
top-edge highlight.

Modernized: the fill now has a subtle vertical gradient (slightly
brighter at top, darker at bottom) for a glass-like depth effect,
and the border uses the brighter C_PANEL_BORDER colour for a cleaner
edge. The gradient surface is cached by (w, h, alpha) so repeated
panels of the same size (the common case) skip the per-row loop
entirely (~10x faster for repeated calls).
```

### `plant_electric_w`

```
Direct-conversion electrical capacity of the D-3He plant [W].
```

### `portal_cycle_s`

```
External repositioning leg between the mouths at beta, plus hop
turnaround overhead  [s].  The multi-jump clock: every rejump costs this
much coordinate time, and it is what each hop's delta must beat to make
backward progress.  When b0_m is given, the throat traversal itself is
added -- the flat 30 s overhead only swallows traversal for small gates;
a survivable throat (~1.4e8 m) takes ~650 days to walk.
```

### `portal_summary`

```
Everything about the gate, in one dict, for the view and the reports.

This now carries the FOUR constructions in the literature, each priced:
  - Morris-Thorne (1988): the textbook volume-distribution wormhole
  - Visser (1989/1995): the thin-shell cut-and-paste wormhole
  - Maldacena-Milekhin-Popov (2020): the fermion-Casimir wormhole that
    works on paper with real quantum fields (but needs magnetic monopoles)
  - Ford-Roman (1997): the quantum inequality that says how long any of
    these can be held open -- and the answer is 'not long enough'
```

### `portal_traversal`

```
Send something through the portal.  All four real-physics answers.

Parameters:
  b0_m:             throat radius [m]
  mouth_a_phi_c2:   Phi/c^2 at mouth A (0 = flat space, -GM/rc^2 in a well)
  mouth_a_beta:     velocity of mouth A (0 = at rest)
  mouth_b_phi_c2:   Phi/c^2 at mouth B
  mouth_b_beta:     velocity of mouth B
  mouth_sep_m:      spatial separation of the mouths [m] (default: Proxima)
  elapsed_s:        coordinate time since the mouths were synchronised [s]
  payload:          "signal", "person", or "object"
  payload_size_m:   size of the payload [m] (2.0 for a person)
  payload_speed_ms: speed through the throat [m/s]

Returns a dict with every number the physics produces, and verdicts that
do not hide infeasibility.  The output is controllable in the two ways GR
actually permits: WHERE (mouth B's location) and WHEN (the desynchronisation
built up by the mouths' environments and motions).
```

### `project`

```
Project world points through the same orbit camera the ShipRenderer uses.
Returns (sx, sy, depth) arrays. Used by the METRIC view, which draws a
procedural grid rather than Parts.
```

### `quantum_teleport_facts`

```
Quantum teleportation is real, demonstrated, and does none of the things
a portal does (Bennett et al. 1993).

It moves a quantum STATE, not matter. It needs pre-shared entanglement. It
needs two classical bits per qubit sent over an ordinary channel, so it is
hard-capped at c and carries no information faster than light. And the
no-cloning theorem means the original is destroyed in the process -- which
is either a technicality or the whole moral question, depending on who is
stepping into the booth.
```

### `radiator_area_m2`

```
Installed radiating area -- both faces of every panel.
```

### `radiator_temp_k`

```
Equilibrium panel temperature from Stefan-Boltzmann: T = (P/eps sigma A)^1/4.
NOT a set point -- a consequence. When the FTL mode drives the coil load up
as beta^2, this is the number that goes past the graphite limit first.
```

### `report_dilation`

```
Every clock in the problem, and which one the marketing quotes.
```

### `report_ladder`

```
The historical attempts to make the exotic bill affordable, and how each
one actually turned out.
```

### `report_metric`

```
Everything the warp metric says, computed live from the shape function.
```

### `report_portal`

```
The portal, priced.
```

### `report_portal_test`

```
Run portal traversal scenarios: signal, person, object, time machine.
```

### `report_spec`

```
Every component of the ship, specified: geometry, count, and the mass
that mass_budget() actually charges for it. All numbers read live from
DIMS -- nothing in this sheet is typed in twice.
```

### `report_voyage`

```
Headless Sol -> Proxima flight, printed as a mission log.
```

### `road_frame`

```
The road's LOCAL frame carried inertially: (east, north, up) unit
vectors at the road point, rotated into the ecliptic by S(t). Position
alone is not the whole solve -- the car also has to arrive facing along
the lane, and the lane direction itself rotates with the planet. This
basis is what the bubble preserves: it carries the car's forward axis
onto the arrival lane heading, not just its centre onto the pavement.
```

### `road_inertial_speed`

```
How fast the pavement itself moves through inertial space: Earth's
mean orbital speed plus the sidereal spin speed at the road latitude.
```

### `road_solar_hour`

```
Local mean solar hour at the road: the road's hour angle relative to
the Sun. Sidereal phase minus the orbital phase -- the same pavement is
not just at a different place at t1, it is a different time of day.
```

### `rocket_proper_time_s`

```
Proper time aboard a conventional relativistic cruiser doing the same
trip at the same speed -- for contrast. It experiences LESS time than the
warp ship, because it is genuinely time-dilated and the warp ship is not.
A warp drive does not buy you time dilation. It buys you no reaction mass,
no g-loading, and arrival in step with the people who waved you off.
```

### `shape_df`

```
df/dr_s -- the derivative that carries ALL of the curvature. Everything
expensive about a warp drive lives in this one function being large.
```

### `shape_df_shifted`

```
df/dr evaluated at r = R + u, computed FROM u directly.

shape_df(r) forms (r - R) internally, and for a wall thinner than about
1e-14 R that subtraction loses every significant digit -- a 1e-33 m wall
sitting at r = 100 m is invisible to double precision. Passing the offset
in explicitly sidesteps the cancellation entirely, which is what lets the
energy integral stay exact all the way down to the Planck-scale walls the
quantum inequality demands.
```

### `shape_f`

```
Alcubierre top-hat shape function f(r_s). f -> 1 inside, 0 outside.
```

### `ship_self_dilation`

```
The ship's OWN gravitational time dilation, from its own mass [-].

Included because a million-tonne shell 183 m from the crew sounds like it
ought to matter, and the honest answer is that it does not: the fractional
rate shift is about 4e-21, which is about two orders of magnitude below
the best clock ever built (~1e-19). Computing it is how you know that,
rather than assuming it.
```

### `smes_store_j`

```
SMES capacity from first principles: u = B^2 / 2 mu0 over the torus
volume. Comes out near 2.8e12 J at this scale -- still over ten orders
of magnitude below a velocity change, which is precisely why this ship
cannot self-launch.
```

### `static_observer_exists`

```
False above |beta| = 1: inside a superluminal bubble there is no such
thing as 'holding station'. Every worldline is dragged forward faster than
light, which is precisely why the front wall cannot be signalled.
```

### `text_shadow`

```
Render text with a 1-pixel drop shadow for contrast over 3D scenes.

Matches the pattern in the companion twins (GmansRun, SE, LS): the starfield
and the metric sheet are bright in places, and plain anti-aliased text
disappears against them. A one-pixel dark shadow behind every HUD label
fixes that without adding a full background box (which would clutter the
viewport). Used for topbar items, spec-card values, and flash messages.
```

### `tipler_cylinder_offset`

```
Tipler cylinder CTC: maximum time displacement  [s].

Tipler (1974): an infinite cylinder of mass M, radius R, rotating at
angular velocity omega produces closed timelike curves when
omega R / c >= 1 (the 'chronology horizon').  A signal traveling distance L
along the cylinder can be displaced by:

    delta_t = L * omega * R / c^2  (approximately, for L >> R)

The displacement is UNBOUNDED: traveling farther along the cylinder
gives proportionally more offset.  This is the only mechanism that can
give more than elapsed-time displacement in a single traversal.
Requires an infinite cylinder (or a finite one with wrap-around) --
the infinite case is a mathematical idealization, not a buildable object.
```

### `vgradient`

```
Vertical gradient fill, numpy-vectorized.

Writes directly to the surface pixel buffer via pixels3d -- ~5x faster
than the per-line pygame.draw.line loop for large surfaces.
```

### `visser_shell_energy_j`

```
Total exotic energy of the Visser thin shell  [J]  (negative).
```

### `visser_shell_mass_kg`

```
Exotic MASS of the Visser thin shell  [kg]  (negative).

    sigma = -c^2 / (2 pi G a) * sqrt(1 - 2GM / (a c^2))    [kg/m^2]
    m_shell = 4 pi a^2 sigma = -2 a c^2 / G * sqrt(1 - 2GM / (a c^2))

In geometric units (G=c=1) this is the textbook -2a sqrt(1-2M/a); restoring
SI multiplies by c^2/G. The shell radius a must be > 2GM/c^2 (outside the
horizon). For the pure Minkowski case (M=0) the bill is -2 a c^2 / G, which
for a 12 m aperture is about -0.016 solar masses -- MORE than the
Morris-Thorne volume estimate, because concentrating the exotic matter on a
2-D surface is less efficient than distributing it through a 3-D throat.
Visser's point is about LOCALISATION, not reduction: the NEC violation is
still there, but it lives on a sheet you could in principle engineer, not
throughout a volume.
```

### `visser_summary`

```
The Visser thin-shell wormhole, priced.

With no arguments, prices a shell at the portal's spec'd aperture with a
zero-mass Schwarzschild patch (the pure-shell limit Visser uses as the
teaching example: two copies of Minkowski, cut and pasted).
```

### `voyage_grav_drift_s`

```
Accumulated crew-vs-Earth clock drift over a crossing, from gravity alone.

The crew climb out of Sol's well and spend the trip in near-flat space, so
their clock runs FASTER than Earth's -- by a couple of seconds over seven
years. Tiny, real, and the reason this model's audit no longer claims the
two clocks are exactly equal.
```

### `wall_tidal_gradient`

```
Tidal acceleration across a 2 m body sitting IN the bubble wall [m/s^2].

a ~ beta c^2 |f''| L, and f'' ~ sigma^2 = 1/delta^2, so the wall is lethal
for any wall thin enough to be affordable. The interior is EXACTLY flat
(f = 1, all derivatives zero) -- which is why the crew is weightless and
unharmed while standing 84 m from a region of infinite-grade shear. This
is the design's real virtue and its real hazard, in one number.
```

### `warp_energy_integral`

```
I = INT_0^inf r^2 (df/dr)^2 dr   [m], by composite Simpson over the wall.

Total energy follows from the angular integral of T^00 in closed form:
    E = INT T^00 d3x
      = -(c^4 beta^2 / 32 pi G) INT (rho^2/r^2)(f')^2 d3x
      = -(c^4 beta^2 / 32 pi G) (8 pi / 3) INT r^2 (f')^2 dr
      = -(c^4 beta^2 / 12 G) * I
because INT sin^3(theta) dtheta dphi = 8 pi / 3 over the sphere.

The integrand is a razor-thin spike of width ~delta sitting at r = R, so
the quadrature runs in the SHIFTED variable u = r - R over +/- 14 delta.
Integrating in u rather than r is not a nicety: at delta = 1e-33 m the
window R +/- 14 delta is narrower than one double-precision ulp of R, so
an r-space quadrature silently collapses to zero width and reports E = 0.
In u-space the same code is exact for a 12 m wall and a Planck-scale one.

Closed-form check the --selftest asserts: for sigma R >> 1 the spike is
f' = -(sigma/2) sech^2(sigma u), and INT sech^4 = 4/3, so I -> R^2 sigma/3.

Cached on (R, delta, samples): the 4000-sample Simpson loop is the
single most expensive physics call and is invoked every frame by the
ship panel.
```

### `waste_heat_w`

```
Everything drawn eventually becomes heat: a closed ship exports no work.
Thermal drawn = electrical load / conversion efficiency.
```

### `york_theta`

```
York time / expansion scalar theta = beta c (x / r_s) df/dr_s   [1/s].

Alcubierre 1994 eq. 19. POSITIVE behind the ship (space being created --
it expands) and NEGATIVE in front (space being destroyed -- it contracts).
This is the single scalar the METRIC view draws: it is literally the rate
at which volume is appearing and disappearing around the hull.
```

## Appendix -- every standalone source comment

Every `#` comment block in `Warpdrive.py` that sits on its own line -- the engineering rationale, derivation notes and honesty warnings that are not attached to a spec key or docstring. Trailing comments on spec keys are already in the tables above.

#### line 1

```
!/usr/bin/env python3
 -*- coding: utf-8 -*-
```

#### line 140

```
 =============================================================================
 SECTION 1 -- PHYSICAL CONSTANTS (CODATA 2018 / IAU 2015, all SI)
 =============================================================================
```

#### line 156

```
 Derived reference scales ----------------------------------------------------
```

#### line 159

```
                                                  "stiffness of spacetime": the
                                                  force scale you must pay to
                                                  curve it. Every warp energy in
                                                  this file is this number times
                                                  a dimensionless geometry factor.
```

#### line 169

```
 Astronomical reference values ----------------------------------------------
```

#### line 181

```
 Target system ---------------------------------------------------------------
```

#### line 185

```
 Interstellar medium (local interstellar cloud, warm neutral) ----------------
```

#### line 190

```
 =============================================================================
 SECTION 2 -- ENGINEERING SPECIFICATION (to scale, SI metres)
 =============================================================================
 Everything the renderer draws and everything the physics charges you for is
 read from DIMS. Change a number here and the ship, the mass budget, the
 radiator sizing, the energy ladder and the voyage all move together.
```

#### line 197

```
   SCALE-DOWN NOTE (WD-1m3 "Miniframe III" refit): every hull/coil/radiator
   length below is the WD-1 baseline multiplied by SCALE_S = 0.4586 (linear
   -- three compounded passes: 0.65, then 0.83, then 0.85). Crew is 6. This
   is not cosmetic shrink-wrapping: mass falls close to S^3, so the
   kinetic-energy bill the beam has to deliver falls by the same factor
   (kinetic_energy_j scales with mass), which is why the SAME external
   stellar-tap array pushes this hull to a higher emergent cruise beta each
   time it shrinks (see boost_profile/max_boost_beta). Waste heat falls
   faster than radiator area, so equilibrium panel temperature falls too --
   a smaller ship runs COOLER at the same beta, which is exactly why the
   thermal barrier (the only passable one) gets easier, not harder, at
   reduced scale.

   The second pass added a lever beyond pure linear scaling: "wall_thick_m"
   (the bubble wall thickness delta) was cut from 1.0 m to 0.2 m.
   flat_interior_r() = bubble_r_m - interior_margin * wall_thick_m, so a
   thinner wall buys back USABLE INTERIOR VOLUME directly -- the wall itself
   is already uninhabitable at any thickness (barrier 1, wall tidal, fails
   by 15+ orders regardless), so thinning it costs nothing the crew were
   ever going to survive. "hull_d_m" is held above the pure linear-scale
   value (a practical minimum cabin diameter for 6 crew), same reasoning as
   "hull_wall_m" in the first pass.

   The third pass found and fixed a real bug rather than adding a new lever:
   the boost-rectenna and SMES mount offsets along the ship's spine
   (formerly hardcoded literals, 40.0 m and 22.0 m, in _envelope_points())
   had never been scaled down in either earlier pass, so check_envelope()
   was silently checking the WD-1-scale mount positions against the shrunk
   ship's much smaller flat interior. Those offsets are now DIMS entries
   ("collector_z0_m", "smes_z0_m") that scale like every other axial offset
   (cap_offset_m etc.), which is what actually surfaced "boost rectenna" and
   later "cryo unit" as the new binding envelope constraints once the old,
   silently-non-scaling "40.0"/"22.0" stopped hiding them -- and, once fixed,
   let the ship shrink further with a genuinely correct envelope check
   instead of one that had been quietly passing for the wrong reason.

   Reactor thermal power and the coil AC / cryo / control electrical loads
   are re-derived from physical scaling laws (magnetic stored energy ~
   volume ~ S^3; cryostat heat leak and shell-servo effort ~ surface area ~
   S^2; hotel load ~ crew headcount) rather than re-typed by hand. The one
   deliberately-preserved invariant is the thermal barrier at 2c: it must
   still exceed rad_limit_k (1900 K), because that is the whole point of the
   honesty audit -- shrinking buys margin, not a free pass past a barrier
   that is supposed to still be there at superluminal speed. --selftest
   enforces this explicitly.

   PASS 4 (WD-1m4) is not a geometric scale-down at all -- SCALE_S and every
   hull/coil/radiator dimension above are unchanged from pass 3. Instead it
   tightens two engineering assumptions that were carried forward, un-
   examined, from pass 1 onward:
     - PLANT["reactor_th_gw"] previously kept the SAME ~1.5x electrical
       margin over the beta=0.99 cruise load that WD-1 happened to have.
       There was never a physical reason for 1.5x specifically -- it was
       inherited, not derived. A 1.35x margin is still a comfortable 35%
       reserve (in the same 20-40% band typical of aerospace power-plant
       design), so the reactor was re-sized down again on that basis.
       reactor_major_d_m/reactor_minor_d_m shrink with it, by (P_new/P_old)
       ^(1/3), i.e. reactor volume tracks thermal output at constant power
       density.
     - "hull_wall_m" had been held at a flat 0.18 m "practical minimum"
       across all three earlier passes, chosen once (relative to WD-1's
       0.22 m at a 16 m hull) and never revisited as the hull kept shrinking
       around it. For a cylindrical pressure vessel at constant internal
       pressure and material yield stress, hoop-stress wall thickness
       t = P*r/sigma scales LINEARLY with hull radius -- so an 8.0 m hull
       genuinely only needs 0.22 x (8.0/16.0) = 0.11 m, not 0.18 m, to hold
       the same pressure differential in the same material. This is real
       structural physics catching up with three passes of shrinking the
       hull around a wall thickness nobody had re-derived.
   Net effect: reactor -10% (2.91 -> 2.62 GW), crew hull shell mass -39%
   (a small line item, ~1.8% of dry mass), total mass -0.9%. Modest on
   their own, but they cost nothing else -- no envelope margin, no thermal
   margin, no honesty invariant was touched to get them.

   PASS 5 (WD-1m5) is also not a geometric scale-down -- SCALE_S and every
   hull/coil/radiator dimension remain unchanged from pass 4. Instead it
   revisits two more hardcoded constants in mass_budget() that had been
   carried forward un-examined since WD-1:
     - The HTS coil winding-pack radial build was a flat 0.35 m literal,
       set by the engineering current density J_e of the REBCO tape
       generation WD-1 assumed. The build is set by J_e: build ~ N*I /
       (J_e * circumference). Modern REBCO at 18 K achieves ~600 A/mm^2
       engineering J (vs the ~500 the 0.35 m build assumed), so the same
       48000 turns x 38 kA fit in a 0.30 m pack -- a 17% J_e improvement
       well within documented REBCO progress. Now a proper DIMS entry
       "coil_build_m".
     - The winding-pack average density was a flat 6000 kg/m^3 literal,
       dominated by copper stabilizer and steel reinforcement. Higher-J_e
       tape needs less copper per ampere of quench protection, so the
       average drops toward the REBCO/substrate fraction. Now a proper
       DIMS entry "coil_density" at 5600 kg/m^3 (~7% copper reduction
       consistent with the thinner build).
     - The shaping-ring solid fraction was a flat 0.35 literal. The
       shaping rings are SECONDARY structure (they break front-back
       symmetry but do not source the main warp field), so a 30% solid
       fraction vs 35% is a modest structural-efficiency gain. Now a
       proper DIMS entry "capring_wall_frac".
   Net effect: HTS coils -20% (5070 -> 4029 t), shaping rings -14%
   (4003 -> 3431 t), total mass -8.9% (18,215 -> 16,602 t). The two
   largest non-ring mass line items, cut at no cost to any envelope
   margin, thermal margin, or honesty invariant. The reactor was NOT
   re-cut this pass -- the pass-5 mass savings show up as extra reactor
   margin and a higher emergent cruise speed (0.845 -> 0.857), not as a
   smaller reactor.

   PASS 6 (WD-1u2) inverted the shrink: every hull, ring, coil, radiator
   and mount dimension went x2.0 (SCALE_S 0.4586 -> 0.9172), mass rose
   7.6x to 125,416 t and the tap was re-specified to 800 PW to hold the
   emergent cruise speed.

   PASS 7 (WD-1u4 "Upscale IV") applies the same move again: every
   linear dimension below is the pass-6 value x 2.0 (SCALE_S 0.9172 ->
   1.8344, 1.83x the ORIGINAL WD-1). Same discipline, derived not typed:
     - mass ~ S^3: another ~8x heavier (~1.0 Mt), kinetic bill and
       braking problem grow the same way.
     - component COUNTS re-derived from the doubled geometry: 96 ring
       sectors/coils, 12 hull decks, 12 pylons, 60 radiator panels
       (count x2 AND panel area x4 = area x8 against waste heat ~x6.6),
       16 cryo units, 32 RCS pods, 8 antimatter traps, 96 Casimir
       cassettes, crew 24 with the doubled cabin volume.
     - every wall/shell/skin spec doubles again for geometric
       similarity (pressure vessel t ~ r, plate bending t ~ span).
     - PLANT scales by the documented laws: coil AC ~ S^3, cryo and
       servo ~ S^2, hotel ~ crew; reactor thermal re-sized at the same
       1.35x margin over the beta=0.99 cruise load.
     - the stellar tap scales x8 again (6.4e18 W, ~17 ppm of L_sun):
       mission infrastructure sized to an ~8x heavier ship.
     - unchanged on purpose: wall_thick_m and interior_margin (the wall
       is spacetime, not structure), collector_deploy_km (set by beam
       diffraction at the unchanged transmitter), casimir gap/pitch
       (nanoscale physics), all temperatures and densities, and every
       portal-gate dimension (a separate installation, not the ship).
```

#### line 338

```
 Missing keys degrade to NaN too -- a deleted spec is unknown state,
 and honest NaN propagation beats a KeyError crash.
```

#### line 355

```
 --- Warp bubble geometry (the spacetime, not the hardware) -----------
```

#### line 357

```
                                -- x2 again (1.83x the original WD-1)
```

#### line 359

```
                                a SPACETIME parameter, not structure:
                                it does not scale with the hull
```

#### line 362

```
                                (f > 0.9997 there) -- see flat_interior_r()
```

#### line 364

```
 --- Main warp ring (the shift-vector shell -- the actual "drive") ----
 The centreline sits AT the bubble radius on purpose: the shell does not
 project the wall from a distance, the shell IS the wall's source term, so
 its stress-energy has to be where the curvature is.
```

#### line 371

```
                                -- x2: shell stress scales with span
```

#### line 375

```
 --- Superconducting field coils (96, one per ring sector) ------------
```

#### line 378

```
                                ring tube: tube dia + 2 x standoff
                                = 27.52 + 0.40 (derived, not free --
                                a smaller bore cannot thread the tube
                                it energises)
```

#### line 387

```
                                engineering J_e of the REBCO tape:
                                build ~ N*I / (J_e * circumference).
                                The bore doubled this pass so the same
                                turns x current COULD fit a ~0.15 m
                                pack; 0.30 m is kept as a conservative
                                quench-stabilizer margin on the larger
                                machine rather than claimed as savings
```

#### line 395

```
                                winding pack inner radius [m] -- x2
```

#### line 398

```
 --- Fore / aft shaping rings (set the front-back asymmetry) ----------
```

#### line 404

```
 --- Crew hull (flat spacetime inside -- ordinary ship engineering) ---
```

#### line 409

```
                                LINEAR in hull radius: 32.0 m returns
                                exactly 2x WD-1's 0.22 m wall
```

#### line 412

```
                                radius (the nose/aft taper) --
                                dimensionless shape factor, unchanged
```

#### line 416

```
                                stress ~ p L^2 / t^2, doubled span needs
                                doubled thickness for the same margin
```

#### line 419

```
                                -- x2 with the hull radius
```

#### line 423

```
                                overall-length figure [m] -- x2
```

#### line 425

```
 --- Structural pylons hull -> ring -----------------------------------
```

#### line 430

```
                                2x span needs ~2x thickness to hold the
                                same bending/buckling margin
```

#### line 434

```
 --- D-3He fusion reactor (the housekeeping plant) --------------------
```

#### line 438

```
                                t = P*r/sigma is linear in radius
```

#### line 441

```
                                typed: beta=0.99 cruise electrical load
                                is ~47.1 GW (coil_ac x8 + cryo/control
                                x4 + hotel x2 vs pass 6); /0.62 gives
                                76.0 GW thermal, x the SAME 1.35
                                design margin = 102.7 GW. Torus volume
                                grew x8, so specific power density is
                                the same as pass 6
```

#### line 450

```
 --- Antimatter store (peak fold transitions only) --------------------
```

#### line 456

```
                                with the kinetic-energy bill it buffers
```

#### line 458

```
 --- SMES field-transient buffer (superconducting magnetic store) -----
 NOT a "warp battery". Its capacity is COMPUTED from B^2/2mu0 times the
 torus volume (see smes_store_j()) and comes out proportionally smaller.
 It buffers coil transients; it does not move the ship. Nothing here
 pretends otherwise.
```

#### line 470

```
 --- Casimir negative-energy lattice (96 cassettes in the ring wall) ---
```

#### line 475

```
                                the ship's macroscopic scale)
```

#### line 479

```
 --- Waste-heat radiators (sized against the REAL waste heat) ---------
 Area scales by the WASTE-HEAT ratio (~x6.6), not the hull's x2:
 60 panels x 90.44 m x 31.32 m gives x8 the pass-6 area -- slightly
 more than waste heat grew, so the beta=0.99 equilibrium sits a
 little cooler than pass 6's ~1.5e3 K. The 1900 K graphite limit is
 the material bound and does not move. check_envelope() still asserts
 the tips stay inside the flat interior (the bubble doubled with it).
```

#### line 495

```
                                panel needs ~2x depth for the same
                                bending stiffness (I ~ t^3 term)
```

#### line 499

```
 --- Cryoplant (holds the HTS coils at 18 K) --------------------------
```

#### line 505

```
                                ring major radius (envelope check only)
```

#### line 507

```
 --- Navigation deflector (subwarp dust shield) -----------------------
```

#### line 513

```
 --- Reaction control (subwarp only -- ion / VASIMR pods) -------------
```

#### line 519

```
 --- Boost receiver (the stellar-tap rectenna) ------------------------
 Stowed it is a bigger dish; under boost it still unfurls to the same
 4 km film rectenna, because the diffraction spot of the (unchanged,
 external) 1000 km transmitter is kilometres wide at interstellar
 range regardless of ship size (see beam_spot_m()).
```

#### line 527

```
                                unchanged: set by beam diffraction at the
                                (unchanged, external) transmitter, not by
                                ship size
```

#### line 534

```
 --- Wormhole portal gate (Morris-Thorne throat) ----------------------
 The gate is the buildable-LOOKING part: a ring you could walk through.
 portal_summary() then prices the throat it would have to hold open, and
 mt_min_throat_m() reports the one you would actually survive crossing.
 Left at full scale: it is a separate ground/orbital installation, not
 part of the ship being resized here.
```

#### line 546

```
 --- Magnetic sail (the only credible way to STOP) --------------------
 Zubrin and Andrews (1991): a superconducting loop deflects interstellar
 protons and drags against the ISM. The x8-heavier hull needs the drag
 back: loop radius doubles to 2800 km (drag ~ Cd rho A) and the cable
 mass scales x8 -- braking time is mass / (Cd rho A), so a x8 ship on
 a x4 area still brakes SLOWER; that is the honest cost of upscaling,
 printed, not hidden.
```

#### line 555

```
                                the same loop-centre field (B ~ I/r)
```

#### line 624

```
 Overall envelope, derived from the geometry the renderer actually builds:
 forward extreme = whichever sticks out furthest (shaping-ring plane vs
 deflector nose), aft extreme = radiator tail vs rectenna rim; the span is
 the ring's outer diameter plus the coil package it carries -- nothing
 aboard is wider.
```

#### line 637

```
 Power plant / thermal balance ----------------------------------------------
 Rescaled from the WD-1 baseline by physical scaling law, not by hand:
   coil_ac_mw : stored magnetic field energy ~ coil volume ~ SCALE_S^3
   cryo_mw    : cryostat radiative heat leak  ~ surface area ~ SCALE_S^2
   control_mw : shell-servo effort over the ring surface ~ SCALE_S^2
   hotel_mw   : life support / compute / sensors ~ crew headcount (6/12)
```

#### line 645

```
                                -- x2 with the doubled crew
```

#### line 647

```
                                96 HTS coils at cruise [MW] -- ~S^3
```

#### line 650

```
                                [MW] -- ~S^2 over the ring surface
```

#### line 656

```
                                mission infrastructure sized to the
                                ship; an ~8x mass needs ~8x delivered
                                power to hold the same cruise speed.
                                ~17 ppm of L_sun (6.4e18 / 3.828e26).
```

#### line 665

```
 Storage / drive control -----------------------------------------------------
```

#### line 677

```
 Shell shape-servo endurance: seconds to lose full integrity at unit stress
 (stress = fractional overrun of the thermal, power or wall-thickness limits).
```

#### line 681

```
 Historical negative-energy reduction ladder (the literature, cited) ---------
 factor = multiplier applied to the raw Alcubierre requirement; 0.0 means the
 entry is not a reduction of the exotic bill at all but a different class of
 solution (positive-energy) or a refuted claim.
```

#### line 701

```
 =============================================================================
 SECTION 3 -- COLORS AND THEME
 =============================================================================
```

#### line 742

```
 =============================================================================
 SECTION 4 -- MINI 3D ENGINE (software renderer, painter's algorithm)
 =============================================================================
 Same renderer architecture as GmansRunV1.17 / SE.py / LS.py: build meshes from
 primitives in SI metres, project them through an orbit camera, flat-shade each
 facet against a single light, sort back-to-front and paint. No GPU, no shader,
 no scene graph -- which is exactly why it runs anywhere and why every vertex
 can be traced back to a number in DIMS.

 pygame is imported defensively so the headless physics CLIs (--selftest,
 --metric, --voyage, --feasibility, --ladder) still run on a machine with no
 display libraries installed.
```

#### line 935

```
 sub-3.5 m source meshes (pods, cassettes, collars, struts) are
 droppable while the camera is moving -- interaction LOD
```

#### line 1052

```
 per-part world centroids + bounding radii, so the frame can build
 hover/label screeninfo without per-part vstacks
```

#### line 1081

```
 ---- primitive builders ----------------------------------------------------
```

#### line 1091

```
 256 segments is already far beyond any visible difference; an uncapped
 count lets a hostile seg value request a billion-vertex linspace.
```

#### line 1353

```
 islice before list(): a hostile iterable (range(10**9)) must not
 be allowed to materialize into gigabytes of sections.
```

#### line 1408

```
 islice first: list() on range(10**9) would materialize gigabytes
 before any length check could run.
```

#### line 1537

```
 subtle border on the label background for contrast against bright stars
```

#### line 1542

```
 glow dot: additive halo + solid centre, so the leader dot reads over
 any background (LS.py's additive-blend pattern applied to a point)
```

#### line 1582

```
 pre-merge both LODs now so the first settled frame after any
 interaction doesn't pay the one-time _prep_part cost mid-drag
```

#### line 1604

```
 ---- camera -----------------------------------------------------------
```

#### line 1638

```
 ---- view state -------------------------------------------------------
```

#### line 1646

```
 leaving the puzzle restores the whole car -- otherwise parts
 past the assembly cursor stay painted as pending ghosts
```

#### line 1708

```
 ---- the painter ------------------------------------------------------
```

#### line 1742

```
 Interaction LOD + overscan frame cache. While the camera or
 layout is moving, a coarse build (VISUAL_DETAIL x 0.30) is
 painted -- the full build returns the instant the pose settles.
 Pan is pure screen translation, so the model is painted into an
 alpha cache ~72px larger than the viewport on every side: any
 frame whose pose matches the cached pose blits it SHIFTED rather
 than repainting -- pans and idle frames cost one blit.
```

#### line 1755

```
 Angles only matter when some mesh actually spins (spin != 0
 rotates verts by angle*spin in world_verts). A parts set with no
 spinners cannot move -- folding a continuously-ticking animation
 clock into the repaint key would restart the chunked hi repaint
 every frame and the model would never finish drawing.
```

#### line 1797

```
 hover picking still runs on a cached frame (shifted coords)
```

#### line 1811

```
 continue an in-progress chunked hi repaint: the emit results live
 in _prog, so each frame just draws the next _PCHUNK faces over the
 lo underlay -- the settle hitch becomes a progressive fill
```

#### line 1844

```
 the lo underlay was painted at _cpan, the hi paint at
 prog["ppan"] -- each blits at its own shift
```

#### line 1876

```
 final frame: the hi surface is complete -- blitting
 the lo underlay under it would leave a lo-res fringe
 around the silhouette, so composite target alone
```

#### line 1909

```
 Repaint target: an overscan alpha surface that stores the model
 plus a margin of off-viewport geometry, so the next frames can
 blit it translated while panning. When the previous frame was an
 interaction-LOD paint at this exact pose, it survives as `los` --
 the underlay for a progressive hi repaint -- so the hi paint must
 go into a FRESH surface, not the reused cache.
```

#### line 1952

```
 faces smaller than ~16 px^2 of the coarse build are invisible while
 the view is moving -- equivalent to ~2 px^2 at full tessellation
```

#### line 1964

```
 faces past fog_d0 fade toward the background; full mist at fog_d1
```

#### line 1969

```
 layout pass first: the global fast path is legal only when no
 part is displaced or dimmed this frame
```

#### line 1997

```
 ---- global fast path: one transform, one projection, one
 emit pass over per-length face groups ---------------------
```

#### line 2106

```
 exact-length point rows straight from the cull gathers --
 no padded gather, no whole-model sxy stack
```

#### line 2130

```
 wires join the same depth-sorted list as the facets
```

#### line 2178

```
 per-part screeninfo without per-part vstacks: project each
 merged centroid and scale the world bounding radius
```

#### line 2286

```
 wires go into the SAME depth-sorted list as the solid
 facets: painted in a separate pass afterwards, the
 bubble shell drew itself over the hull it surrounds
```

#### line 2343

```
 drop faces that can never paint a pixel: entirely off the
 draw rect or smaller than a quarter-pixel
```

#### line 2365

```
 closed solids: a face pointing away can never be the
 visible surface under painter's order -- cull it. Wires,
 dishes, plates and other open sheets keep both sides.
```

#### line 2378

```
 enhanced three-component lighting, vectorized over the kept
 faces: ambient + diffuse + rim (sky bounce on away faces)
```

#### line 2386

```
 depth fog toward the background colour, same curve as before
```

#### line 2389

```
 per-face base colours with the same dynamic overrides
 the scalar path applies: coil glow, drive glow, rad heat,
 bubble fade, dimming, highlight
```

#### line 2436

```
 python-native lists index and iterate faster than numpy
 rows inside the draw loop AND inside pygame itself. Faces
 are emitted grouped by true vertex count so each gather
 and each polygon carries only real points, not padded rows
```

#### line 2471

```
 flatten every block's rows into contiguous lists once, so the
 depth-ordered draw pass is pure list indexing; every emitter
 produces exact-length point lists already
```

#### line 2505

```
 progressive hi repaint: the settled pose equals the lo frame's
 pose, so underlay it and paint hi faces _PCHUNK at a time --
 no 100ms freeze, detail materializes over ~3 frames
```

#### line 2551

```
 pick coords live in the paint target's space; offset to screen
```

#### line 2564

```
 stash the painted frame for pan-shift / idle blits
```

#### line 2594

```
 =============================================================================
 SECTION 5 -- WARP METRIC PHYSICS  (the real general relativity, integrated)
 =============================================================================
 THE METRIC (Alcubierre 1994, eq. 8), signature (-,+,+,+):

     ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2

 A flat interior (f = 1) is carried along by a shift vector that falls to zero
 (f = 0) outside a wall of thickness delta at radius R. Nothing moves THROUGH
 space -- the interior is inertial and weightless the whole way.

 The shape function is Alcubierre's own top-hat:

     f(r) = [tanh(sigma (r + R)) - tanh(sigma (r - R))] / (2 tanh(sigma R))

 with sigma = 1/delta. From it everything else follows analytically, and this
 module integrates the results rather than quoting them.
```

#### line 2759

```
 Fold sqrt(h) into the spike BEFORE squaring: sum w r^2 (d sqrt h)^2 / 3 is
 algebraically total*h/3, but d^2 alone overflows for walls below ~1e-154 m
 even though the true integral (~R^2 sigma/3) is still representable. This
 keeps the razor-wall limit finite exactly as far as the true value is.
```

#### line 2820

```
 f'' VANISHES exactly at r = R -- the crest of f' is a stationary point --
 so sampling there reports a comfortable zero and hides the hazard. The
 shear peaks on the shoulders, at sigma u ~ +/- 0.66, so scan for it.
```

#### line 2848

```
 --- Casimir effect: the ONLY laboratory-verified negative energy density ----
```

#### line 2886

```
 --- Energy conditions -------------------------------------------------------
```

#### line 2920

```
 --- Barrier engineering analysis -------------------------------------------
 Each barrier is a theorem or physical limit that blocks the drive.  For each
 we compute (a) the exact number that triggers the barrier, (b) what it would
 take to get past it, and (c) whether that is physically possible.  The answer
 to (c) is always "no" for the five hard barriers -- that is the honest result.
```

#### line 2938

```
 1. Survivable bubble wall (tidal gradient across the wall)
    a_wall = beta c^2 |f''|_max L; at beta=1, L=2m this is ~1e16 g
```

#### line 2943

```
 Route: make delta -> 0 (thinner wall).  But QI forbids delta < 100 L_P.
```

#### line 2948

```
 2. Superluminal flight (NEC violation, SSV theorem)
    Theorem: ANY v > c warp violates NEC.  No route.
```

#### line 2954

```
 3. Negative energy at the required scale
    Need |E| at delta=1m; have |Casimir|.
```

#### line 2958

```
 Route: more Casimir cassettes.  How many?
```

#### line 2962

```
 4. Steering above beta = 1 (horizon lock)
    Theorem: forward wall is causally disconnected.  No route.
```

#### line 2966

```
 5. Thermal survival above beta = 1
    T = (P / eps sigma A)^(1/4); limit = rad_limit_k
    Find the beta where T crosses the limit
```

#### line 2977

```
 Route: more radiator area.  How much?
```

#### line 2982

```
 6. Ford-Roman wall thickness (QI on wall)
```

#### line 2988

```
 7. Quantum inequality on wormhole throat
```

#### line 2995

```
 8. Causality / CTC (chronology protection)
    A time-shifted wormhole creates CTCs.  Hawking's conjecture expects
    the throat to be destroyed at the chronology horizon.
```

#### line 3088

```
 =============================================================================
 SECTION 5b -- MASS BUDGET  (every kilogram derived from DIMS geometry)
 =============================================================================
```

#### line 3104

```
 main warp ring: a SHELL of wall thickness ring_wall_m, not a solid torus
```

#### line 3108

```
 fore + aft shaping rings
```

#### line 3112

```
 HTS field coils: annular winding pack on a named standoff from the tube
```

#### line 3118

```
 crew hull: pressure shell + decks (hull_shell_rfrac / deck_inset_m are
 named spec entries -- the taper shape factor is dimensionless, the
 inset is a length and scales with the hull)
```

#### line 3128

```
 power / thermal plant
```

#### line 3142

```
 structure and appendages
```

#### line 3162

```
 no module-level cache: DIMS is mutable, so every consumer calls
 ship_mass_kg() live (same convention as radiator_area_m2/plant_electric_w)
```

#### line 3188

```
 =============================================================================
 SECTION 5c -- POWER, THERMAL AND THE BEAM  (ordinary engineering, done right)
 =============================================================================
```

#### line 3343

```
 convert delivered energy to speed through the relativistic ledger
```

#### line 3388

```
 --- Magnetic sail: the only credible brake ---------------------------------
```

#### line 3477

```
 --- Interstellar medium loading on the bubble wall -------------------------
```

#### line 3500

```
 --- Comparison baseline: an honest relativistic rocket ----------------------
```

#### line 3509

```
 No rocket makes the trip at or above lightspeed: the proper time is
 imaginary there, and the capped gamma would fake a finite answer.
```

#### line 3525

```
 --- Formatters --------------------------------------------------------------
```

#### line 3651

```
 =============================================================================
 SECTION 5d -- ENVIRONMENTAL SPACETIME DILATION  (whose clock, and where)
 =============================================================================
 The headline claim of a warp drive is "no time dilation". That is true, and it
 is also sloppy. It is true for ONE observer -- the crew, who are comoving with
 the bubble -- and it is false for several others who are all equally real.
 This section computes every clock in the problem instead of asserting the
 convenient one.

 From the metric  ds^2 = -c^2 dt^2 + (dx - v_s f dt)^2 + dy^2 + dz^2 :

   COMOVING observer (the crew, dx = v_s f dt, f = 1):
       ds^2 = -c^2 dt^2  ->  dtau = dt exactly.  No dilation. Ever.

   STATIC observer (holds station in the external frame, dx = 0):
       ds^2 = -c^2 dt^2 + v_s^2 f^2 dt^2  ->  dtau = dt sqrt(1 - beta^2 f^2)

 So the warp field DOES carry a dilation field -- it is just that nobody aboard
 is sitting in it. Someone station-keeping inside the bubble while the ship
 flies past would be dilated by the full Lorentz factor. That profile is what
 the DILATION view draws.
```

#### line 3701

```
 --- Gravitational potential along the route --------------------------------
 Real wells, real numbers. Sol at one end, Proxima at the other, the Galaxy
 underneath both, and the ship's own (utterly negligible) self-gravity.
```

#### line 3705

```
 The inner floor of each well is the ORBIT the ship actually occupies at that
 end -- Earth's orbit at Sol, Proxima b's orbit at Proxima -- not the stellar
 surface. Departure therefore starts at exactly Earth's clock rate, so the
 drift the model reports is the drift the crew would really accumulate.
```

#### line 3716

```
                                (v_circ^2/c^2 ~ (220 km/s)^2/c^2, order 1e-6);
                                common to both ends, so it cancels in the drift
                                -- carried anyway so the ledger is complete.
```

#### line 3816

```
 =============================================================================
 SECTION 5e -- THE PORTAL  (Morris-Thorne wormhole, and the real teleporter)
 =============================================================================
 A "portal" is a traversable wormhole: two mouths, one throat, walk in here and
 out there. It is a legitimate solution of the Einstein field equations --
 Morris & Thorne wrote it down in 1988 as a teaching exercise precisely BECAUSE
 it is easy to construct and impossible to build.

   ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2)(dtheta^2 + sin^2 theta dphi^2)

 l is proper radial distance, running from -inf (mouth A) through 0 (the
 throat, radius b0) to +inf (mouth B). There is no horizon and no singularity:
 it is genuinely traversable in both directions.

 The catch is the FLARE-OUT CONDITION. For the throat to open out on both sides
 rather than pinch off, the stress-energy at the throat must violate the null
 energy condition -- the same wall the superluminal warp drive hits, arrived at
 from a completely different direction. That is not a coincidence: Morris,
 Thorne & Yurtsever (1988) and later Hawking showed the two problems are the
 same problem wearing different hats.

 This section computes three numbers and lets them speak:
   1. how much negative energy a throat of radius b0 needs,
   2. how big b0 has to be before a human survives the tidal forces,
   3. what happens when you have one anyway (answer: you have a time machine).
```

#### line 3925

```
 --- The full Morris-Thorne metric, not just the throat ----------------------
 Morris & Thorne (Am. J. Phys. 56, 395, 1988) write the wormhole as

     ds^2 = -e^(2 Phi(r)) c^2 dt^2 + dr^2 / (1 - b(r)/r) + r^2 dOmega^2

 where b(r) is the SHAPE FUNCTION and Phi(r) is the REDSHIFT FUNCTION. The
 throat sits at r = r0 where b(r0) = r0. The two conditions that make this a
 wormhole rather than a coordinate artefact are:

   FLARE-OUT:   b'(r0) < 1          (the throat is a minimum of r - b(r))
   ASYMPTOTIC:  b(r)/r -> 0          (space is flat far from the throat)

 The flare-out condition is the one that costs. It forces d^2r/dl^2 > 0 at the
 throat, and the Einstein field equations then require rho < 0 there. This is
 not a feature of one ansatz -- it is theoremed (Visser 1989; Flanagan & Wald
 1997) that EVERY traversable wormhole violates the null energy condition at
 the throat. The exotic bill is structural.
```

#### line 4038

```
 --- Ford-Roman quantum inequalities: how long can you hold the throat? -----
 Ford & Roman (Phys. Rev. D 55, 3763, 1997) proved that negative energy is not
 just hard to source -- it is BOUNDED in magnitude and duration by the quantum
 inequalities. For a massless scalar field in flat spacetime, sampled over a
 time tau:

     integral rho(t) g(tau, t) dt  >=  -3 hbar / (32 pi^2 c^3 tau^4)

 The bound scales as 1/tau^4: the longer you want negative energy, the less
 you can have. This is the real reason you cannot just hold a wormhole open
 indefinitely with a Casimir pulse -- the pulse decays, and the throat closes.
```

#### line 4088

```
 --- Maldacena, Milekhin & Popov (2020): the wormhole that works on paper ---
 This is the closest thing to a REAL traversable wormhole in the literature.
 MMP construct a wormhole from two nearly-extremal MAGNETICALLY CHARGED black
 holes, held open not by ad-hoc exotic matter but by the Casimir energy of
 massless fermions threading the magnetic field lines between them. The
 negative energy is genuine, calculable, and comes from a real quantum field.

 The catch -- and there are several:
   1. The black holes must be magnetically charged. No magnetic monopole has
      ever been observed, so these objects may not exist. If they do, they
      would be primordial, and none has been seen.
   2. The holes must be NEARLY EXTREMAL: charge Q within ~1/M of the extremal
      bound Q_ext = sqrt(4 pi eps0 G) M. This is a fine-tuned state.
   3. The throat is long and narrow. Traversal takes a time of order the
      black-hole mass (in natural units), and the traveler must be highly
      boosted. For a solar-mass hole the asymptotic traversal time is short,
      but the tidal constraint pushes the mass up.
   4. Only massless fermions provide the right Casimir energy. This is not a
      generic construction -- it is a specific, fragile one.

 Maldacena, Milekhin & Popov, Phys. Rev. Lett. 125, 031602 (2020).
```

#### line 4168

```
 Schwarzschild radius of the BH (throat scale)
```

#### line 4170

```
 Casimir energy that holds it open. The energy density of massless
 fermion modes in a cavity of size r_s scales as ~ -hbar c / r_s^4
 (standard Casimir scaling), and the throat volume is ~(4/3) pi r_s^3,
 giving E ~ -(4/3) pi hbar c / r_s. This is an order-of-magnitude
 estimate; MMP's actual calculation includes the magnetic-flux mode
 count (which is enormous for a near-extremal BH) and a logarithmic
 throat-length factor, both of which raise the true value. But the
 sign, the quantum-field origin, and the 1/r_s scaling are correct.
```

#### line 4192

```
 --- Visser thin-shell wormhole (1995): a different cut at the same problem --
 Visser (Phys. Rev. D 43, 402, 1991; Nucl. Phys. B 328, 203, 1989) takes two
 copies of Schwarzschild spacetime, cuts each at radius a > 2M, and pastes
 them together with a thin shell. The shell carries the entire exotic energy
 budget as a surface density, not a volume density. This is the most
 'engineerable' wormhole in the literature: the exotic matter is localised to
 a 2-D surface, not smeared through a 3-D throat, so in principle you only
 need to violate the NEC on a sheet, not throughout a volume.
```

#### line 4252

```
 --- The part where it becomes a time machine -------------------------------
```

#### line 4303

```
 --- The teleporter that actually exists ------------------------------------
```

#### line 4332

```
 --- Time-displacement amplification mechanisms --------------------------------
 A single wormhole can displace you by at most the elapsed time (offset =
 elapsed * rate_diff, and rate_diff <= 1).  To go further you need either a
 chain of desynchronized mouths or a different time-machine construction
 entirely.  This section computes the maximum displacement for every
 mechanism that general relativity admits on paper.
```

#### line 4385

```
 Simplified Tipler formula: offset proportional to path length
 The coefficient comes from the off-diagonal metric term g_t_phi
 omega keeps its sign (rotation sense = direction of displacement);
 L and R are magnitudes.
```

#### line 4434

```
 The displacement per orbit is bounded by the spin period
 For near-extremal Kerr: delta_t ~ 2*pi*a/c per orbit
```

#### line 4490

```
 --- MULTI-JUMP: iterated portal traversal with external repositioning --------
 One wormhole hop displaces you by the CURRENT mouth offset delta(t) = r*t.
 To rejump, the ship must return externally to the departure mouth at beta:
 that leg takes Delta = D/(beta c) and burns cruise_load_w(beta) * Delta of
 positive ship energy.  The mouths keep desynchronising between hops, so the
 sequence is a recurrence in coordinate time, not a repeated constant.

   BACKWARD (step A->B into the past, return externally B->A):
       t_{k+1} = t_k - r t_k + Delta = t_k (1 - r) + Delta
       fixed point t* = Delta / r; net-backward per cycle needs t_k > t*
       -> total reachable past ~ elapsed - Delta/r  (nearly ALL of elapsed,
          versus elapsed * r for a single jump)

   FORWARD (step B->A into the future, return externally A->B):
       t_{k+1} = t_k + r t_k + Delta = t_k (1 + r) + Delta
       geometric growth (1+r)^k -- unbounded while the desync condition holds

   Ordering honesty: net-backward drift requires delta > Delta, and
   Delta > D/c for any subluminal return -- so the loop can only begin
   AFTER single-hop CTCs already exist.  Multi-jump does not evade
   chronology protection; it multiplies its exposure.
```

#### line 4513

```
 ISM isotope content for the scoop-enrichment model (number fractions):
```

#### line 4518

```
 D-3He mix the reactor burns: 2 parts D to 3 parts 3He by mass
```

#### line 4521

```
 Fixed per-hop overhead: throat traversal + docking turnaround [s]
```

#### line 4549

```
 mass fractions: H dominates; D is 2x protium mass; He is 4x; 3He is 3x
```

#### line 4626

```
 rate_diff is |rate_a - rate_b| of two clock rates in [0, 1]: |diff| <= 1.
 A nan input must propagate into the ledger, not clamp to max desync.
```

#### line 4641

```
 a negative hop count is no plan; the per-cycle ledger bounds at 1e6
 hops -- a plan beyond that is a divergent recurrence, not an itinerary
```

#### line 4705

```
 inf/nan ledgers cannot claim sustainability -- honesty rule:
 a check you cannot measure counts as FAIL, never PASS
```

#### line 4734

```
 Ford-Roman: how long can quantum fields hold THIS throat open?
```

#### line 4752

```
 --- full Morris-Thorne metric ---
```

#### line 4757

```
 --- Ford-Roman quantum inequality ---
```

#### line 4763

```
 --- Maldacena-Milekhin-Popov (2020) ---
```

#### line 4765

```
 --- Visser thin-shell (1989/1995) ---
```

#### line 4772

```
 =============================================================================
 SECTION 5f -- PORTAL TRAVERSAL  (sending things through, where and when)
 =============================================================================
 The question "can I send something through the portal?" has four real physics
 answers, and this section computes all of them honestly:

   WHERE you come out:  at mouth B, wherever mouth B physically is.  A
     wormhole is a shortcut between two points in space -- you do not choose
     the destination independently of where the second mouth sits.

   WHEN you come out:  at mouth B's current proper time, which is NOT the
     same as mouth A's.  The two mouths desynchronise whenever they sit at
     different gravitational potentials or move at different speeds.  This is
     Morris, Thorne & Yurtsever (1988): the desynchronisation is real GR,
     it accumulates, and the instant it exceeds the light-travel time between
     the mouths you have a time machine (CTCs exist).

   WHETHER you survive:  the tidal acceleration at the throat is c^2 L / b0^2.
     A photon always survives.  A person needs b0 >= 1.35e8 m.  An object of
     size L needs b0 >= sqrt(c^2 L / g_limit).

   WHETHER THE THROAT IS STILL OPEN:  Ford-Roman quantum inequalities limit
     the hold time to tau_max ~ (3 hbar G b0^2 / (4 pi c^7))^(1/4).  If the
     traversal time exceeds that, the throat closes before you cross.

 The correlations below are all theoremed or measured physics.  Nothing here
 is fiction: the time offset is gravitational + special-relativistic dilation
 (GPS satellites measure it daily), the CTC onset is MTY 1988, the tidal bound
 is Morris-Thorne 1988, and the QI hold time is Ford-Roman 1997.
```

#### line 4898

```
 a nan separation must stay nan downstream, not become a zero separation
```

#### line 4900

```
 --- WHERE: mouth B's location is just where it is ----------------------
 The wormhole connects A to B.  You cannot choose the exit independently.
```

#### line 4903

```
 --- WHEN: the clock desynchronisation ----------------------------------
```

#### line 4907

```
 If offset > 0, B is behind A.  Stepping A->B arrives offset_s in B's past
 relative to A's present.  The arrival time at B, measured in A's frame:
```

#### line 4911

```
 --- CTC check ----------------------------------------------------------
```

#### line 4914

```
 How far from CTC onset: negative = safe, positive = time machine exists
```

#### line 4916

```
 Time until CTC onset at the current rate difference (independent of
 how long has already elapsed -- this is the characteristic timescale)
```

#### line 4920

```
 --- WHETHER you survive the crossing -----------------------------------
```

#### line 4922

```
 Photons have no size -- tidal forces cannot tear them apart.
```

#### line 4932

```
 --- WHETHER the throat is still open -----------------------------------
```

#### line 4937

```
 --- the exotic energy the throat demands (to hold open for the crossing)
```

#### line 4942

```
 --- verdicts -----------------------------------------------------------
```

#### line 4996

```
 --- WHERE ---
```

#### line 4999

```
 --- WHEN ---
```

#### line 5010

```
 --- SURVIVAL ---
```

#### line 5016

```
 --- THROAT ---
```

#### line 5024

```
 --- VERDICTS ---
```

#### line 5044

```
 --- SCENARIO 1: a signal through the spec'd gate, no desynchronisation --
```

#### line 5054

```
 --- SCENARIO 2: a person through the survivable throat, no desync ------
```

#### line 5068

```
 --- SCENARIO 3: a person, mouth B parked in a gravity well -------------
```

#### line 5089

```
 --- SCENARIO 4: time machine -- mouth B at neutron-star depth, 20 yr ---
```

#### line 5112

```
 --- SCENARIO 5: mouth B carried by relativistic rocket -----------------
```

#### line 5126

```
 --- SCENARIO 6: mouth B carried by WARP DRIVE (the fast thing) ---------
```

#### line 5130

```
 Warp interior is flat: no kinematic dilation.  Only gravitational.
```

#### line 5140

```
 --- MAXIMIZED TIME-TRAVEL SCENARIOS ------------------------------------
 Push the desynchronization to the physical limits: deepest realistic
 gravity well (neutron-star surface, phi/c^2 ~ -0.3) combined with the
 highest realistic velocity (beta = 0.99), and the smallest practical
 mouth separation (1 AU -- same solar system).  The math is the same
 ctc_onset_s() / mouth_clock_rate() as every other scenario; only the
 inputs are pushed to their physical extremes.  The barriers do not
 move.
```

#### line 5153

```
 SCENARIO 7: maximum desynchronization, minimum separation
```

#### line 5179

```
 SCENARIO 8: maximum backward jump -- 100 years of desynchronization
```

#### line 5198

```
 SCENARIO 9: extreme -- just above a black hole horizon + 0.999c
```

#### line 5221

```
 --- AMPLIFICATION MECHANISMS --------------------------------------------
 A single wormhole can displace you by at most the elapsed time
 (offset = elapsed * rate_diff, and rate_diff <= 1).  To go further,
 you need either multiple wormholes in series or a different time-
 machine construction entirely.  This section computes the maximum
 displacement for every mechanism GR admits on paper.
```

#### line 5235

```
 Mechanism 1: Chain of wormholes
```

#### line 5247

```
 Mechanism 2: Nested wormholes
```

#### line 5258

```
 Mechanism 3: Tipler cylinder
```

#### line 5261

```
 At chronology horizon omega*R = c, displacement = L/c
```

#### line 5279

```
 Mechanism 4: Gott cosmic strings
```

#### line 5294

```
 Mechanism 5: Kerr black-hole CTC
```

#### line 5310

```
 Summary
```

#### line 5336

```
 --- MULTI-JUMP: iterated traversal with external repositioning ----------
 The ship's role in continuous time travel: after each hop it must
 return externally to the departure mouth at beta -- that leg takes
 Delta = D/(beta c) and burns cruise_load * Delta of positive energy.
 The mouths keep desyncing meanwhile, so each hop's offset grows.
```

#### line 5355

```
 Backward loop
```

#### line 5370

```
 Forward loop
```

#### line 5383

```
 Energy + refueling ledger
```

#### line 5403

```
 Scoop parity: yield ~ beta, burn has a cryo+hotel floor ~0.11 kg/day
```

#### line 5421

```
 --- CONTROL SUMMARY ----------------------------------------------------
```

#### line 5512

```
 =============================================================================
 SECTION 6 -- SHIP GEOMETRY  (every part built to scale from DIMS)
 =============================================================================
 +Z is the direction of travel. The origin sits at the centre of the warp ring,
 which is also the centre of the bubble, which is also the centre of mass --
 they have to coincide or the shell shape servo cannot hold a symmetric field.
```

#### line 5575

```
 Bounded: a corrupted count like 1e18 is finite and non-negative yet
 would make range() burn memory/time on a billion-part mesh.
```

#### line 5594

```
 ---------------------------------------------------------------- 1. HULL
 Barrel + tapered caps: the spec's hull_shell_rfrac (0.88) is the MEAN
 shell radius as a fraction of hull radius, so the barrel holds the
 full 32 m diameter over ~76% of each half-length and the caps carry
 the taper. The old profile tapered continuously from z=0, which left
 almost nowhere a full-width deck or a 9.6 m trap could physically sit.
 The cap run is SOLVED, not tuned: bisect the cap fraction until the
 loft's z-mean shell radius equals hull_shell_rfrac exactly -- the
 drawn hull then carries precisely the area the mass bill charges.
```

#### line 5615

```
 Catmull-Rom overshoots a plateau: hull_d_m is a hard envelope,
 so the smoothed radius is clamped to it (solve and loft alike).
```

#### line 5648

```
 local hull radius from the smoothed loft -- every interior part
 must respect this or it spears through the tapering skin.
```

#### line 5665

```
 the billed hull_wall_m is real geometry: loft the inner skin too
```

#### line 5670

```
 the flat-spacetime volume the crew actually lives in -- decks are
 spec-thickness slabs spread over the stations where the local loft
 radius can hold them AND that do not collide with the reactor torus
```

#### line 5676

```
 deck stations live in the barrel: a billed deck is a full-width
 plug (mass_budget charges (hull_r - inset)^2 per deck), so each
 station must hold ~that radius and clear the reactor torus
```

#### line 5692

```
 trap stations are needed BEFORE the deck meshes are built: a 9.6 m
 Penning sphere in a deck-gap stands two storeys tall and MUST pierce
 the adjacent slabs -- the decks get cut collars where each trap
 passes through (the physics of it: 12 decks + an 8-trap bay cannot
 fit the barrel without penetrations, so the penetrations are drawn)
```

#### line 5708

```
 fallback: single file on the spine wherever it fits
```

#### line 5729

```
 the inset leaves a gap between plate edge and the hull's inner
 wall -- a rim beam at mid-height carries the deck into the wall
```

#### line 5749

```
 ------------------------------------------------------- 2. FUSION REACTOR
```

#### line 5754

```
 reactor_wall_m is a radial build (blanket + shield) LARGER than the
 tube radius -- the bill treats the torus as a solid body; the plasma
 bore is drawn at the smallest sensible channel and the over-bill is
 called out in this part's spec text rather than hidden
```

#### line 5766

```
 the torus floats inside the barrel otherwise: eight radial standoff
 posts land it on the hull's inner wall at its mid-plane
```

#### line 5800

```
 ---------------------------------------------------- 3. ANTIMATTER TRAPS
 _zsx was computed with the deck layout above: each 9.6 m Penning
 sphere stands in a deck-gap bay and pierces the slabs it overlaps --
 the decks carry drawn collars where a trap passes through.
```

#### line 5829

```
 ------------------------------------------------------------- 4. SMES
```

#### line 5839

```
 the toroid wraps the hull with a ~2 m standoff gap -- eight radial
 standoff posts bridge hull skin to the winding's inner surface
```

#### line 5868

```
 ---------------------------------------------------------- 5. CRYOPLANT
 Each unit rides the mount ring on a radial strut back to the tube's
 inner skin -- and the ring of units is staggered half a cell off the
 pylon lines so no cryostat straddles a spar.
```

#### line 5905

```
 ------------------------------------------------------------ 6. PYLONS
```

#### line 5907

```
 spec length/thickness: tip lands inside the ring tube, root embeds
 pylon_len_m back into the hull skin -- an anchor that floats off
 the surface is not an anchor
```

#### line 5927

```
 ------------------------------------------------------- 7. MAIN WARP RING
```

#### line 5939

```
 the gap between sectors is not void -- it is the joint that
 carries inter-sector services and the shell material the mass
 bill charges for (4 pi^2 R r wall rho assumes a continuous shell)
```

#### line 5946

```
 draw the billed wall: the inner skin of the tube, so the shell's
 ring_wall_m is real geometry, not just a mass-budget line
```

#### line 5976

```
 ------------------------------------------------------- 8. HTS FIELD COILS
```

#### line 6002

```
 --------------------------------------------------- 9. CASIMIR CASSETTES
```

#### line 6009

```
 inside the tube hollow, pressed to the wall they feed: cavity
 radius = tube radius - shell wall; the plate face sits half a
 plate inside that with a servo's clearance
```

#### line 6042

```
 ---------------------------------------------------- 10/11. SHAPING RINGS
```

#### line 6048

```
 the bill charges capring_wall_frac of skin over the torus
 surface -- draw the inner face so the wall is real geometry
```

#### line 6069

```
 ------------------------------------------------------------ 12. RADIATORS
```

#### line 6080

```
 the aft shaping ring pierces every panel at its mid-span --
 it doubles as the radiator spine; a clamp doubler welds the
 penetration instead of leaving interpenetrating solids
```

#### line 6102

```
 ------------------------------------------------------------ 13. DEFLECTOR
```

#### line 6106

```
 the billed deflector_t_m shell: a backing face + a boss that carries
 the dish off the hull tip it mounts on
```

#### line 6111

```
 the dish is wider than the hull tip -- a flared pedestal carries the
 load from the cap's last full ring out under the dish hub
```

#### line 6124

```
 ------------------------------------------------------------ 14. RECTENNA
```

#### line 6127

```
 the stowed dish roots collector_z0_m aft of centreline -- well past
 the hull's aft tip; a tapered deploy mast bridges the gap, narrowing
 to the tip radius so it sockets into the cap rather than breaching it
```

#### line 6153

```
 ---------------------------------------------------------------- 15. RCS
 A single midships ring cannot hold the billed pods: the hull's
 circumference fits fewer of them than rcs_pods asks for, and at every
 midships station the Penning spheres own the azimuth band around the
 trap row. Pods are therefore distributed over the stations that are
 genuinely free -- deck-gap midpoints and cap shelves clear of every
 trap sphere -- each ring sized to the chord its local radius allows.
```

#### line 6211

```
 ------------------------------------------------------------- 16. MAGSAIL
```

#### line 6216

```
 loop planes ride just aft of the radiator tail -- derived, not
 hardcoded, so the loop tracks the ship it brakes
```

#### line 6226

```
 tether spokes thread the radiator forest -- offset half a panel
 pitch so every spoke rides a gap, not a fin -- and anchor at
 the radiator rim (the real structure at this z), not at the
 empty axis
```

#### line 6252

```
 -------------------------------------------------------- 17. WARP BUBBLE
```

#### line 6282

```
 =============================================================================
 SECTION 6b -- PORTAL GEOMETRY  (the gate, and the throat it would need)
 =============================================================================
```

#### line 6296

```
 Bounded: finite-but-absurd counts (1e9 rings) would otherwise burn
 memory on a mesh no display could ever resolve.
```

#### line 6348

```
 ------------------------------------------------------------ 1. GATE A
```

#### line 6371

```
 ------------------------------------------------------- 2. FIELD COILS
```

#### line 6390

```
 --------------------------------------------------- 3. CASIMIR AT THROAT
```

#### line 6400

```
 the cassette floats otherwise: a short standoff lands it on the
 aperture ring's inner face -- the wall it feeds
```

#### line 6421

```
 ------------------------------------------------ 4. THE THROAT (geometry)
```

#### line 6443

```
 ------------------------------------------------------------- 5. GATE B
```

#### line 6469

```
 =============================================================================
 SPECIAL WORKS -- the WD-88 FIELD CAR: the entire drive, downscaled to a car
 =============================================================================
 Same model, ~1/63 scale: the bubble that barely encloses a 4.4 m coupe is
 2.9 m across instead of 183 m. Every subsystem is carried over honestly --
 fusion cell, SMES buffer, Penning bottles, Casimir strips, field coils,
 radiators, rectenna, deflector, RCS, the shell itself -- plus the cabin
 transition sequencer (a real distribution node, see its spec card) and the
 field transition arming speed of 88 mph, an engineering setpoint, not
 physics. There is NO gas engine: the wheels are fusion-fed hub motors.
```

#### line 6493

```
 double resolution. Only the MODEL refines -- the
 car keeps 100% scale (same metres, same physics).
```

#### line 6518

```
 ---- the "same road, different place in space" problem ---------------------
 The car's landing zone is a coordinate fixed to Earth, not to space. Earth
 orbits the Sun at ~29.78 km/s and spins once per sidereal day, so between
 departure and arrival the same pavement occupies a completely different
 inertial position. The bubble's job is computed honestly as that vector.
```

#### line 6613

```
 ~22 m^2 of 1.5 mm brushed stainless skin over the loft
```

#### line 6615

```
 gull-wing doors, decklid, fascias, arches, rub strips, trim
```

#### line 6617

```
 glass panes the wire outlines stand in for, plus frames
```

#### line 6619

```
 seats, dash, console, wheel+column, mirrors, headrests
```

#### line 6621

```
 four 30 kg in-wheel fusion-fed drive units
```

#### line 6623

```
 rims + tires
```

#### line 6625

```
 A-arms, links, uprights
```

#### line 6627

```
 the beltline field run: tape + sheath, ~13.5 m of 9 cm line
```

#### line 6629

```
 six pylon-analog standoffs bolting the run to the monocoque
```

#### line 6631

```
 fore + aft shaping hoops
```

#### line 6633

```
 the stowed KE-recovery torus at the tail
```

#### line 6635

```
 12 strips, drawn geometry x plate-stack density -- live DIMS
```

#### line 6637

```
 trunk torus, blanket, divertor -- the 1/53 reactor
```

#### line 6639

```
 hood SMES puck + cryostat mass
```

#### line 6641

```
 two under-floor Penning bottles + housings
```

#### line 6643

```
 underbody circulator, lines and the helium charge itself
```

#### line 6645

```
 rear-deck louver bank
```

#### line 6647

```
 dash ephemeris unit + fix antennas
```

#### line 6649

```
 roof whip
```

#### line 6651

```
 nose strip
```

#### line 6653

```
 transition sequencer, arming lever and keypad
```

#### line 6655

```
 DC bus bars from cell through SMES into the field run
```

#### line 6657

```
 cryo loop plumbing joins the circulator figure below
```

#### line 6659

```
 undertray, sills, hardpoint mounts, harness brackets
```

#### line 6755

```
 the cell can never overshoot its own radiative equilibrium --
 at T_eq the louvers reject exactly the heat in, and no bounded
 step may cross it
```

#### line 6891

```
 the top clamp is part of the profile -- normalise BEFORE inserting
 mid-stations so the refined run follows the clamped silhouette
```

#### line 7066

```
 ------------------------------------------------------- 1. BODY SHELL
```

#### line 7089

```
 open greenhouse: pillars + roof skin only, so the cabin -- and the
 show flux capacitor on the firewall -- stays visible from outside
```

#### line 7102

```
 cabin furniture, so the open greenhouse has an inside: floor pan,
 rear bulkhead (the flux capacitor's mount), seats, dash
```

#### line 7122

```
 ---- DeLorean trim: fascias, lights, arches, rub strips, mirrors ----
```

#### line 7151

```
 ---- cabin controls + remaining fittings ------------------------------
```

#### line 7170

```
 glazing -- wire outlines only: a fill quad would painter-occlude the
 cabin from some orbits, and glass that reads AND never hides the
 interior is wire glass
```

#### line 7191

```
 ---- last fittings: instruments, mirror, grille, badge, markers ------
```

#### line 7218

```
 footwell pedals -- torque and regen-by-wire, not cables and hydraulics
```

#### line 7230

```
 the driver -- the crew line in the mass budget, finally drawn:
 torso and helmet in the left seat, hands not modelled (the wheel
 turns itself in this sim anyway)
```

#### line 7244

```
 louvered sail panels -- the C-pillar flying buttresses, signature
 DMC: black slatted panels closing the rear quarters
```

#### line 7254

```
 door inner trim panels -- through the open cabin you would otherwise
 see the raw inside of the skin
```

#### line 7265

```
 parking brake lever on the console -- the car still parks itself
```

#### line 7270

```
 rear underbody diffuser strakes -- the undertray mass line, drawn
```

#### line 7275

```
 sill plates at the door sills -- the step-over strip the open
 cabin exposes on both flanks
```

#### line 7281

```
 gull-wing door gas struts -- the visible ram at the roof rail that
 holds the door open; parked closed they sit inside the seal line
```

#### line 7290

```
 ---- final fittings pass ---------------------------------------------
```

#### line 7296

```
 footwell -- a cabin item
```

#### line 7318

```
 ---- detail pass II: hinge line, toll panes, furniture, hardpoints ---
 the gull-wings swing off a roof spine rail -- the hinge housings are
 where the door plumbing visibly disappears into the roof
```

#### line 7346

```
 the speedo that matters: a dial ring on the binnacle with its needle
 parked up against the 88
```

#### line 7361

```
 low-voltage aux battery in the front trunk -- hotel loads still draw
 while the fusion cell is dark; section view is where you see it
```

#### line 7370

```
 cabin + avionics heat exchanger behind the grille slot, fed by the
 air-dam inlets -- the loop has to dump SOMEWHERE even at the kerb
```

#### line 7393

```
 ---- detail pass III: cabin controls, structure, seams --------------
```

#### line 7450

```
 roll bar: a real car this fast gets one -- legs beside the seats,
 top rail under the roof rail line, hidden from the side profile
```

#### line 7499

```
 fixed fire line to the cell bay -- the hand bottle stays in the
 footwell, but the trunk gets its own plumbed nozzle
```

#### line 7516

```
 ---- detail pass IV: the cabin's last furniture ----------------------
 the wheel was a bare rim: three spokes and the horn pad with the DMC
```

#### line 7580

```
 the emergency abort the test crew demanded: red mushroom on the dash
```

#### line 7593

```
 ---- the structure under the styling --------------------------------
```

#### line 7658

```
 ---- detail pass V: the cabin's small hardware -----------------------
```

#### line 7677

```
 the late-car option: a small ducktail lip on the decklid edge
```

#### line 7746

```
 ---- detail pass VI: the last of the cabin + bay hardware ------------
 gull-wing reach straps hang inside the doors' trailing edges -- they
 close from the roof, so the strap is the only way down
```

#### line 7764

```
 rear-glass demister grid -- four heater wires across the pane
```

#### line 7812

```
 cowl intake feeds the blower -- cabin air comes in at the screen base
```

#### line 7826

```
 LV wiring honesty: the aux battery feeds the fuse box and grounds
 to the frame rail -- a car with a dead 12 V bus drives nothing
```

#### line 7857

```
 ---- detail pass VII: closing the last gaps ----------------------------
 the column ended at the dash and the rack sat unwired -- the
 intermediate shaft runs through the firewall to the rack, with a
 U-joint where it turns down -- this car steers by wheel, so the
 column-to-rack linkage stays mechanical
```

#### line 7911

```
 ---- detail pass VIII: the backbone chassis and last systems ---------
 the DMC's signature steel spine runs the floor's length; the rear
 forks carry the drivetrain bay -- in our car, the hub drives
```

#### line 7932

```
 the main fuel: He-3 tank strapped in the trunk beside the cell
```

#### line 7949

```
 LV honesty: the HV bus steps down -- a DC-DC converter sits in the
 frunk beside the aux battery and trickles it
```

#### line 8002

```
 ---- detail pass IX: the glass the greenhouse was still missing ------
 the toll panes existed inside empty window holes -- the door glass
 itself was never drawn. two panes close the cabin against the wall.
```

#### line 8011

```
 interior door release levers on the trim tops, next to the sill
```

#### line 8053

```
 the DMC shipped no spare tire -- a puncture kit lives in the trunk
```

#### line 8070

```
 ---- detail pass X: handles, channels, blades, filters ---------------
```

#### line 8117

```
 ---- detail pass XI: the fittings the tenth pass still missed ---------
```

#### line 8172

```
 -------------------------------------------------- 2. HUB DRIVE + RCS
```

#### line 8186

```
 suspension arms -- the hubs cannot hang free of the chassis;
 upper + lower A-arm lines carry them into the monocoque
```

#### line 8198

```
 ---- detail pass II: rolling stock, steering, RCS propellant --------
```

#### line 8227

```
 coil-over dampers share the A-arm load path
```

#### line 8238

```
 the bells were missing their supply: two cold-gas bottles underslung
 aft, plumbed straight to each bell -- attitude authority needs gas
```

#### line 8249

```
 ---- detail pass III: valve stems, encoders, liners, bonding ---------
```

#### line 8273

```
 ---- detail pass V: the motors were never wired ----------------------
```

#### line 8299

```
 anti-roll bars, front and rear, on drop links to the lower A-arms
```

#### line 8311

```
 ---- detail pass VI: toe links, ride sensors, hub ducts, RCS fittings --
```

#### line 8340

```
 ---- detail pass VII: tread bands on the tire shoulders ---------------
```

#### line 8349

```
 ---- detail pass VIII: motor controllers + fin rings ------------------
 the hub motors are dumb iron; the controllers sit inboard on the
 loom trays and take the phase cables the last few centimetres
```

#### line 8366

```
 ---- detail pass IX: suspension bump stops + front crossmember --------
 the A-arms never had bump stops; rubber cones over the lower arms
```

#### line 8388

```
 ---- detail pass X: joints, bushings, boots, sensor leads -------------
```

#### line 8430

```
 --------------------------------------------- 3. FIELD CONDUIT RUN
 The glowing bands around the body ARE the field coils -- the same job
 the 96 ship coils do, re-threaded around a beltline instead of a torus.
```

#### line 8446

```
 conduit standoffs -- the pylon analog: struts that bolt the field run
 to the monocoque at its hardpoints, spaced down the beltline
```

#### line 8458

```
 field driver boxes where the run terminates on the rear deck -- each
 houses the HTS current-lead pack that feeds its half of the loop
```

#### line 8468

```
 ---- detail pass II: couplers, main feeds, the field computer -------
```

#### line 8474

```
 ---- detail pass IV: standoff pads + junction thermal pickups -------
```

#### line 8489

```
 ---- detail pass V: FMU telltales + driver heatsinks -----------------
```

#### line 8502

```
 ---- detail pass VII: current sensors ring the main feeds -------------
```

#### line 8516

```
 the field management unit: behind the bulkhead, on the harness --
 somebody has to sequence twelve segments of superconductor
```

#### line 8527

```
 pass X: insulation jacket rings where the run crosses the open flank
```

#### line 8533

```
 pass XI: clamp rings either side of the aft junctions
```

#### line 8558

```
 ------------------------------------------- 4. TRUNK FUSION CELL
```

#### line 8567

```
 He-3 filler neck on the decklid -- the car's refuelling port, feeding
 the trunk tank down to the reactor's regulator
```

#### line 8573

```
 ---- detail pass II: the filler was unplumbed -- feed line, cradle,
 and the hot-side stubs that carry cell heat to the louver bank ----
```

#### line 8584

```
 ---- detail pass III: coils, shield, regulator, the DC bus ---------
```

#### line 8606

```
 ---- detail pass IV: spare fuel, quick-disconnect, instrumentation --
```

#### line 8618

```
 pass IX: service valve where the tank feed meets the line
```

#### line 8627

```
 ---- detail pass V: coolant port stubs + the cabin telltale ----------
```

#### line 8636

```
 ---- detail pass VI: coil terminals + feed-line insulation collars ----
```

#### line 8653

```
 ---- detail pass VII: the torus jacket band -----------------------------
```

#### line 8659

```
 ---- detail pass X: the plate the cradles actually bolt to ------------
```

#### line 8663

```
 ---- detail pass XI: fuel filter + cradle pads --------------------------
```

#### line 8684

```
 ------------------------------------------------- 5. SMES BUFFER
```

#### line 8691

```
 shore-power socket on the left flank -- the puck takes its standing
 charge from the wall before the cell is lit, like any EV
```

#### line 8697

```
 ---- detail pass II: output bus on the puck ---------------------------
```

#### line 8705

```
 ---- detail pass III: cryostat ring + quench vent -------------------
```

#### line 8718

```
 ---- detail pass IV: the HV contactor box switches the bus ----------
```

#### line 8722

```
 ---- detail pass V: bus cover + quench sense wire --------------------
```

#### line 8730

```
 ---- detail pass VI: shore power actually reaches the puck -----------
```

#### line 8741

```
 ---- detail pass IX: insulating boots over the bus posts --------------
```

#### line 8748

```
 ---- detail pass X: splice box where the cold line meets the puck -----
```

#### line 8762

```
 ------------------------------------------- 6. PENNING BOTTLES
```

#### line 8768

```
 ---- detail pass II: bottles were unmounted and unplumbed -----------
```

#### line 8781

```
 ---- detail pass IV: the traps need volts -- PSU, leads, valves -----
```

#### line 8794

```
 ---- detail pass V: Penning bottles need UHV -- ion pump + manifold --
```

#### line 8804

```
 pass X: the manifold gets a gauge -- UHV without a readout is blind
```

#### line 8820

```
 ---- detail pass VII: dewar insulation bands on the bottles ------------
```

#### line 8827

```
 ---- detail pass XI: the bottles sit on mounts, not the floor pan -----
```

#### line 8841

```
 ------------------------------------------------ 7. CASIMIR STRIPS
```

#### line 8853

```
 detail pass IV: harness drop from each strip to the underbody
```

#### line 8858

```
 pass V: connector block at each strip's forward end
```

#### line 8863

```
 pass VI: the feedthrough pin on each connector block
```

#### line 8868

```
 pass X: the drops land on underfloor bus rails, not empty air
```

#### line 8888

```
 ------------------------------------------------- 8. HEAT LOUVERS
```

#### line 8895

```
 ---- detail pass II: header tanks at the ends of the bank -----------
```

#### line 8901

```
 ---- detail pass V: the bank actuates -- link rod header -> louvers --
```

#### line 8906

```
 pass XI: pivot pins at the bank's ends
```

#### line 8921

```
 ---------------------------------------------------- 9. RECTENNA
```

#### line 8932

```
 ---- detail pass II: insulator ring + coax feed down the A-pillar ---
```

#### line 8941

```
 ---- detail pass V: cable clips + surge can on the feed --------------
```

#### line 8958

```
 --------------------------------------------------- 10. DEFLECTOR
```

#### line 8962

```
 ---- detail pass III: emitter cells + feed drops --------------------
```

#### line 8971

```
 ---- detail pass IV: the strip's driver module under the nose -------
```

#### line 8975

```
 ---- detail pass V: junctions where the feed drops land --------------
```

#### line 8988

```
 ------------------------------------------ 11. SHAPING HOOPS
 The ship's cap rings close the shell at the poles; the car's hoops do
 the same job at the nose and tail where the conduit run opens.
```

#### line 8992

```
 elliptical hoops -- the body section is far wider than tall, so a
 circular ring would bury itself in the fenders; these are scaled in x
 to wrap the actual nose and tail sections like the ship's cap rings
```

#### line 9010

```
 ---- detail pass III: wall sensor pods ride the hoop tops -----------
```

#### line 9016

```
 ---- detail pass IV: trim tabs fine-tune the wall at the sides ------
```

#### line 9023

```
 ---- detail pass V: hoop mount bearings at the strut roots -----------
```

#### line 9030

```
 ---- detail pass X: fairings where the struts meet the body -----------
```

#### line 9046

```
 ------------------------------------ 12. FIELD TRANSITION SEQUENCER
 The Y-manifold on the rear bulkhead behind the seats, visible through
 the open greenhouse: it fans the transition pulse from the SMES out to
 the three field conduit runs -- a real distribution node, not a lamp.
```

#### line 9058

```
 the run sequencer: three indicator faces on the dash rim showing
 channel state -- armed, charged, transitioning
```

#### line 9064

```
 the arming lever on the dash -- the physical enable for the
 transition interlock chain
```

#### line 9071

```
 mission keypad on the console -- the operator entry for the
 ephemeris unit's destination array
```

#### line 9076

```
 the service ground hook, folded on the rear deck: drains residual
 shell charge to earth before the crew touches the field run
```

#### line 9084

```
 ---- detail pass V: the sequencer harness down the bulkhead ----------
 a thin lo-voltage harness runs down the bulkhead to the sequencer's
 own fuse -- powers the node and its panel feed
```

#### line 9094

```
 pass XI: sockets at the three arm roots on the Y hub
```

#### line 9116

```
 ----------------------------------------------------- 12. WARP SHELL
```

#### line 9138

```
 ---------------------------------------- 13. MAGSAIL BRAKE LOOP
 The ship brakes with a 700 km magnetic sail. A car cannot fly a sail --
 the honest downscale is the same physics used the other way round: a
 superconducting loop that dumps run kinetic energy back into the SMES
 (magsail_regen_eff is the ship's own recovery fraction).
```

#### line 9154

```
 ---- detail pass II: stow hinges on the tail corners ------------------
```

#### line 9159

```
 ---- detail pass III: deploy actuator + the KE return line ----------
```

#### line 9164

```
 the recovered megajoules need a way home: return line underbody,
 loop -> SMES bus -- regen with nowhere to put it is just braking
```

#### line 9171

```
 ---- detail pass V: stow latch + release pin --------------------------
```

#### line 9178

```
 ---- detail pass VI: loop current leads at the hinges ----------------
```

#### line 9184

```
 pass XI: a restraint strap holds the loop against its latch
```

#### line 9203

```
 ------------------------------------------- 14. CRYO LOOP (underbody)
 The ship's cryoplant keeps the SMES and the Casimir lattice cold. The
 car needs the same service for the same two loads.
```

#### line 9218

```
 ---- detail pass II: compressor, header bottle, and the third leg --
 the microtorus magnets superconduct too -- a cold line climbs to it
```

#### line 9233

```
 ---- detail pass III: service block + relief vent -------------------
```

#### line 9241

```
 ---- detail pass IV: expansion tank + line fill valves ---------------
```

#### line 9250

```
 ---- detail pass V: line clamps hold the runs to the floor pan -------
```

#### line 9256

```
 ---- detail pass VI: vacuum-jacket coupling where the cell line lands --
```

#### line 9261

```
 ---- detail pass XI: the expansion tank's overflow runs to ground ------
```

#### line 9275

```
 --------------------------------------- 15. EPHEMERIS UNIT (the nav)
 The ship solves its flight plan against a star catalogue; the car's
 version is the little box on the dash that keeps the ephemeris -- the
 piece that makes "the same road, later" a solvable coordinate instead
 of a wish. It holds two frames and one transform:
   inertial:  Earth rides the ecliptic at ~29.78 km/s on a first-order
              Kepler ellipse (a = 1 AU, e = 0.0167 carried for real);
   rotating:  the road is a fixed lat/lon spun about the pole once
              per sidereal day (86,164.0905 s), radius 6,371 km --
              with the pole tilted 23.44 deg out of the ecliptic.
 At fire time t0 it stamps the departure fix p0 = E(t0) + S(t0)p_road;
 for a hop of dt it solves p1 = E(t0+dt) + S(t0+dt)p_road -- the SAME
 lat/lon/alt, a different point of space. The bubble's job is the
 vector p1 - p0, decomposed into the orbital leg and the spin leg.
```

#### line 9301

```
 ---- detail pass II: the solve needs an attitude reference ----------
```

#### line 9309

```
 ---- detail pass III: star tracker -- the solve needs a sky fix -----
```

#### line 9317

```
 pass VII: the tracker sits on its ground plane
```

#### line 9322

```
 ---- detail pass V: the diagnostic port the crew plugs into -----------
```

#### line 9357

```
 --------------------------------------- 16. TRANSITION TRAIL (the mark)
 The twin scorch streaks the transition leaves behind the wheels -- the
 the honest record of the event: the field-transition scars left on the
 road when the bubble fires -- hidden until the run actually goes.
```

#### line 9368

```
 detail pass V: the hot core inside each streak
```

#### line 9386

```
 ------------------------------------------------- 17. ROAD (the run)
 Not part of the machine: the strip of tarmac the run happens on. The
 wheels rest on it -- wheel bottoms -0.935 m, slab top -0.94 m.
 the run surface is drawn as a wire grid, not a slab: a solid floor under
 the car would sort wrong in the painter's pass and graze-occlude the
 wheels. Lines never occlude, and a holo grid reads as the test range.
```

#### line 9407

```
 solid edge lines -- it is a two-lane county road, not a runway
```

#### line 9412

```
 timing loops buried in the tarmac -- this is a measured run, so the
 strip carries the same inductive pair a drag strip would
```

#### line 9423

```
 ---- detail pass IV: the roadside crew gear --------------------------
```

#### line 9434

```
 the "88" board marks the commit point -- past it the run cannot stop
```

#### line 9449

```
 ---- detail pass V: start line, tar repairs, marshal's box ------------
```

#### line 9465

```
 ---- detail pass IX: cat's-eye studs on the lane lines -----------------
```

#### line 9470

```
 pass XI: the crew's speed gun on its post, and a drain grate
```

#### line 9499

```
 every part carries its operations row -- power, duty, failure -- the
 same accounting the ship's spec cards get from operations_ledger()
```

#### line 9516

```
 =============================================================================
 SECTION 7 -- THE WARP CORE  (stateful drive, real SI, stepped in real time)
 =============================================================================
```

#### line 9531

```
 --- commanded state
```

#### line 9538

```
 --- physical state
```

#### line 9550

```
 --- live derived readouts
```

#### line 9558

```
 --- cumulative ledger (every joule that entered or left the ship)
```

#### line 9564

```
 ---------------------------------------------------------------- helpers
```

#### line 9588

```
 ---------------------------------------------------------------- stepping
```

#### line 9594

```
 panels have real heat capacity: they lag, they do not snap
```

#### line 9624

```
 Characteristic drain time at unit stress: SHELL_STRESS_TAU seconds.
 Named and stated rather than buried, because it sets how long you get
 to watch the readouts before an over-driven shell lets go.
```

#### line 9674

```
 never laundered back to 1.0 by the clamp
```

#### line 9682

```
 ---- shell formation -------------------------------------------
```

#### line 9688

```
 No shell, no warp. beta falls back to the ship's REAL velocity --
 otherwise a collapsed superluminal bubble leaves the readouts
 (and the load, and the stress) pinned at a speed nothing is
 holding any more, and the ship re-collapses forever.
```

#### line 9696

```
 ---- the travelling field phase (what the coils are actually doing)
```

#### line 9709

```
 ---- electrical load and the beam --------------------------------
```

#### line 9722

```
 ---- SMES buffers the difference (and empties fast if overdrawn) --
```

#### line 9726

```
 ---- the exotic ledger (superluminal only) ------------------------
```

#### line 9730

```
 booked as DEBT, never as supply: nothing aboard can pay this,
 and the HUD prints it in violet with UNFUNDED next to it
```

#### line 9739

```
 ---- status line ---------------------------------------------------
```

#### line 9754

```
 =============================================================================
 SECTION 8 -- VOYAGE  (Sol -> Proxima Centauri b, in the three phases physics
                       actually forces on you)
 =============================================================================
```

#### line 9831

```
 ------------------------------------------------------------------ step
```

#### line 9839

```
 A negative or NaN frame step would rewind position, clocks and
 the energy ledger -- nothing integrates backward.  A missing
 drive core is no tick at all.
```

#### line 9869

```
 energy in from the beam -> relativistic gamma -> speed.
 beam_w is refreshed per substep from the LIVE position: core.update
 only runs once per (possibly 182-day) update tick, and using its
 stale power let the ship over-collect and lock cruise at 0.893
 while boost_profile -- integrating the same physics -- caps at
 ~0.855. HUD display still reads core.beam_w; physics uses this.
```

#### line 9881

```
 the stall detector reports the dead config, not a nan ledger
```

#### line 9903

```
 Two brakes, and the model is explicit about which is doing the work.
 MAGSAIL: always available, drags on the ISM, fades as v^2.
 DESTINATION ARRAY: photon pressure from a transmitter already built
 at Proxima. Thousands of times stronger -- and it assumes an entire
 second stellar-scale facility at a star nobody has been to.
```

#### line 9914

```
 brake in MOMENTUM space: p = gamma m v, dp = -F dt
```

#### line 9919

```
 Only the MAGSAIL returns energy to the bus. Photon braking
 does not: the ship's kinetic energy goes into the reflected
 beam, which leaves. Crediting the beam's work as onboard
 recovery would quietly manufacture a supply the audit then
 measures over-unity against.
```

#### line 9937

```
 ---- superluminal override: no gamma, no kinetic ledger ------------
```

#### line 9951

```
 ---- the kinetic ledger, live in every phase ----------------------
```

#### line 9957

```
 ---- integrate position and both clocks ---------------------------
```

#### line 9959

```
 THREE clocks, integrated separately. dt is COORDINATE time.
   t_coord : a clock at rest at infinity
   t_ship  : the crew. Flat interior means no VELOCITY dilation, but
             they still sit in whatever gravitational potential they
             are passing through, so their rate is grav_rate(x).
   t_earth : Earth, permanently 1 AU down Sol's well.
 The difference between the last two is the whole environmental
 dilation story, and it is a couple of seconds per crossing.
```

#### line 9987

```
 ------------------------------------------------------- phase commands
```

#### line 10031

```
 --------------------------------------------------------- demo auto-play
```

#### line 10053

```
 a destination array only bites inside beam range -- brake
 when the photon brake can actually stop the ship, the same
 margin the self-test's full crossing uses
```

#### line 10061

```
 magsail-only: drag is all there is, so every second counts
```

#### line 10079

```
 =============================================================================
 SECTION 9 -- HONESTY LAYER  (conservation audit; refuses magic)
 =============================================================================
 Modelled on Radiant.py:honesty_audit() and Simulation.py:_conservation_audit.
 If any of these fail, the model has produced physically impossible output and
 must not be trusted. This is the difference between a digital twin and a prop.
```

#### line 10091

```
 Every read degrades non-numeric/missing state to nan, which then FAILS
 the comparison below -- the audit is the corruption detector, so it must
 degrade a poisoned ship into a BROKEN verdict, never crash or pass one.
```

#### line 10108

```
 1) NO OVER-UNITY. The beam is the ONLY source of kinetic energy this
    ship has ever had, so the most it ever held cannot exceed what was
    delivered. Note this compares against the PEAK, not the current value:
    checking the current one would pass trivially after any braking.
```

#### line 10115

```
 1b) RECOVERY IS BOUNDED. The magsail can never hand back more than the
     ship was carrying, times its stated efficiency.
```

#### line 10121

```
 2) THE PLANT IS BOUNDED. Cumulative electrical output cannot exceed the
    reactor's rating times elapsed ship time.
```

#### line 10126

```
 3) FUEL IS CONSERVED. Every joule the plant produced is backed by burnt
    D-3He at the stated specific energy -- no fuel-free electricity.
```

#### line 10131

```
 4) NEGATIVE ENERGY IS NEVER SUPPLIED, ONLY OWED. The Casimir lattice is
    the only real negative-energy source aboard and it is microscopic.
    Superluminal operation books a debt; it never books income.
```

#### line 10139

```
 5) THE SECOND LAW. Radiated energy is non-negative and the panels are
    never colder than they would be radiating their own load.
```

#### line 10143

```
 6) NULL ENERGY CONDITION reported truthfully: never claimed satisfied
    while superluminal.
```

#### line 10149

```
 7) NO VELOCITY-DILATION DIVIDEND. A warp interior is flat, so the crew get
    no Lorentz dilation -- but they are not in flat space overall, and the
    model must not pretend otherwise. The only permitted divergence between
    the crew clock and Earth's is GRAVITATIONAL, of order 1e-8 fractional.
    A 1e-6 tolerance admits that and would still catch an accidental
    Lorentz factor, which would be of order 1e-1.
```

#### line 10159

```
 7b) ...AND THE GRAVITATIONAL PART IS REALLY MODELLED, not zeroed out.
     Climbing out of Sol's well genuinely puts the crew ahead of Earth, by
     a couple of seconds per crossing. Asserting the clocks are exactly
     equal would have been the easy lie.
```

#### line 10166

```
 8) BEAM CAPTURE IS PHYSICAL. Never more than 100% of the transmitted beam.
```

#### line 10170

```
 9) MASS IS POSITIVE. Every component of the dry mass budget is real matter.
```

#### line 10173

```
 10) ARRIVAL IS EARNED. You are only 'ARRIVED' if you are actually stopped.
     A missing or non-Voyage object cannot vouch for its own arrival --
     fail closed rather than pass vacuously on 'phase != ARRIVED'.
```

#### line 10181

```
 11) THE LEDGER ITSELF IS SANE. Every entry is a finite non-negative
     physical quantity -- a poisoned key must fail here even if no
     invariant above happens to read it.  A MISSING ledger is not a clean
     ledger: all() over an empty dict would pass vacuously, so require the
     record to exist and hold entries.
```

#### line 10221

```
 =============================================================================
 SECTION 9b -- REPORTS  (--metric, --ladder, --feasibility, --voyage)
 =============================================================================
```

#### line 10472

```
 tape length counts turns at the pack MEAN diameter: the windings run
 from the clear bore out through one winding build, so the average turn
 is pi x (bore + build), not pi x bore
```

#### line 11177

```
 a non-finite or nonpositive beta can never leave the dock; spin the
 log out without burning the 2M-iteration guard
```

#### line 11195

```
 A dead beam, a dead brake, or a nan window leaves the integrator
 spinning without ever reaching ARRIVED -- detect a frozen mission
 state and say so instead of burning the whole guard budget.
```

#### line 11202

```
 A live mission changes (phase, x, v) every tick; 500 identical or
 non-finite signatures is unambiguous death and costs ~4 s, not 40.
```

#### line 11221

```
 =============================================================================
 SECTION 9c -- SELF-TEST  (headless physics unit checks)
 =============================================================================
```

#### line 11237

```
                             deliberately -- every one must restore it.
```

#### line 11239

```
 --- shape function -----------------------------------------------------
```

#### line 11247

```
 --- the energy integral against its closed form ------------------------
```

#### line 11256

```
 --- Alcubierre's own published figure ----------------------------------
```

#### line 11261

```
 --- signs that must never flip ----------------------------------------
```

#### line 11271

```
 --- York expansion must be antisymmetric front-to-back -----------------
```

#### line 11278

```
 --- energy conditions --------------------------------------------------
```

#### line 11285

```
 --- relativity ---------------------------------------------------------
```

#### line 11294

```
 --- thermal ------------------------------------------------------------
```

#### line 11306

```
 --- mass budget --------------------------------------------------------
```

#### line 11313

```
 Spec-sheet coverage: every mass_budget line must have a printed row in
 report_spec -- a component that is charged but not specified is a spec
 hole. report_spec returns the budget keys it printed; require a
 one-to-one match (no missing rows, no orphan rows).
```

#### line 11327

```
 --- mission ------------------------------------------------------------
```

#### line 11338

```
 --- near-light-speed achievement proofs --------------------------------
```

#### line 11340

```
 KE grows superlinearly: mass cancels in the ratio, so this check is
 scale-robust. gamma(0.9)-1 = 1.294 vs gamma(0.6)-1 = 0.25 -> ~5.2x the
 energy for only 1.5x the speed.
```

#### line 11349

```
 gamma diverges: beta=0.99 needs >5x the energy of the emergent cruise
```

#### line 11354

```
 The beam can deliver the max-cruise energy but not more
```

#### line 11362

```
 Delivered energy approximately equals KE at max cruise (the race converges)
```

#### line 11366

```
 Beam capture falls as 1/L^2 beyond the rectenna-size distance
```

#### line 11372

```
 Lighter ship -> higher speed (the refit lever)
```

#### line 11380

```
 --- environmental dilation ---------------------------------------------
```

#### line 11395

```
 Not exactly equal, and correctly so: grav_rate() sums EVERY well, so
 Proxima's potential reaches back across 4.25 ly and shifts the departure
 rate by ~4e-15. _earth_rate() is Sol alone. The tolerance is set to admit
 that real term and still catch anything larger.
```

#### line 11412

```
 --- portal --------------------------------------------------------------
```

#### line 11450

```
 --- full Morris-Thorne metric -------------------------------------------
```

#### line 11469

```
 --- Ford-Roman quantum inequality ---------------------------------------
```

#### line 11483

```
 --- Maldacena-Milekhin-Popov (2020) -------------------------------------
```

#### line 11498

```
 --- Visser thin-shell (1989/1995) ---------------------------------------
```

#### line 11511

```
 --- portal traversal physics -------------------------------------------
 Mouth clock rate: gravitational + kinematic, both real.
```

#### line 11522

```
 GPS-style: gravitational + kinematic combine multiplicatively
```

#### line 11527

```
 Time offset accumulates linearly
```

#### line 11534

```
 CTC onset: offset exceeds light-time
 Use astronomical scales: 1 ly separation -> light-time ~1 yr
```

#### line 11539

```
 At Proxima separation, light-time is ~4.25 yr
```

#### line 11544

```
 Full traversal: signal through the spec'd gate
```

#### line 11553

```
 Person through the survivable throat
```

#### line 11561

```
 Desynchronisation: mouth B in a gravity well
```

#### line 11570

```
 Warp transport: NO desynchronisation (flat interior)
```

#### line 11576

```
 Rocket transport: DOES desynchronise
```

#### line 11582

```
 Maximum desynchronization: neutron-star well + 0.99c rocket, 1 AU, 1 yr
```

#### line 11596

```
 Extreme: near-horizon + 0.999c, 100 yr
```

#### line 11604

```
 Both directions: same offset, opposite sign depending on step direction
```

#### line 11609

```
 --- FORMULA-LEVEL PROOF CHECKS (every function, verified) ---------------
```

#### line 11611

```
 shape_df: derivative of the tanh top-hat
```

#### line 11620

```
 energy_density: T^00 = -(c^4/8piG)(beta^2 rho^2/4r^2)(df/dr)^2
```

#### line 11629

```
 wall_tidal_gradient: lethality of the wall
```

#### line 11637

```
 ford_roman_wall_limit: ~100 L_planck, scales as 1/beta
```

#### line 11645

```
 smes_store_j: magnetic energy density
```

#### line 11649

```
 bound scales as S^3 with the torus volume: 60 T in the pass-7 torus
 stores 2.76 TJ (ITER class ~41 GJ is 67x smaller)
```

#### line 11652

```
 fusion_fuel_kg: fuel consumption backs the plant
```

#### line 11657

```
 beam_spot_m: Airy diffraction d = 2.44 lambda L / D
```

#### line 11668

```
 magsail_drag_n: F = Cd * rho * v^2 * A
```

#### line 11679

```
 beam_brake_force_n: F = 2P/c (photon pressure)
```

#### line 11685

```
 beam_brake_time_s: t = M v / F (deceleration time)
```

#### line 11690

```
 ism_particles_swept: N = n * pi * R^2 * D
```

#### line 11697

```
 ism_blast_energy_j: E = N * m_p * c^2 * beta^2/2 (conservative)
```

#### line 11704

```
 rocket_proper_time_s: tau = (d / beta c) / gamma
```

#### line 11713

```
 mt_redshift_phi: zero-tidal choice -> Phi = 0
```

#### line 11717

```
 mmp_extremal_charge_c: Q = sqrt(4 pi eps0 G) M
```

#### line 11725

```
 visser_shell_energy_j: E = m_shell * c^2
```

#### line 11732

```
 ctc_onset_s: t = (D/c) / |rate_diff|
```

#### line 11739

```
 --- CROSS-FORMULA CONSISTENCY PROOFS -----------------------------------
 MT density x volume = MT energy
```

#### line 11749

```
 MT tidal = profile at throat
```

#### line 11754

```
 MT min throat: tidal at b0_min = 1 g
```

#### line 11760

```
 Alcubierre energy scales as beta^2
```

#### line 11766

```
 Alcubierre energy scales as 1/delta
```

#### line 11772

```
 Warp energy = -(c^4/12G) beta^2 I
```

#### line 11779

```
 Lorentz gamma = 1/sqrt(1-beta^2)
```

#### line 11787

```
 Ford-Roman derivation: |rho_QI(tau_max)| = |rho_throat|
```

#### line 11795

```
 Visser E = mc^2
```

#### line 11801

```
 MMP tidal mass = c^3 sqrt(L/(4G^2 g))
```

#### line 11807

```
 Mouth clock rate = sqrt(1+2Phi/c^2) * 1/gamma (consistency)
```

#### line 11814

```
 --- BARRIER ENGINEERING PROOFS -----------------------------------------
 Each hard barrier is a theorem or physical limit.  We verify the exact
 number, the threshold, and that the gap is what the model reports.
```

#### line 11820

```
 1. Wall tidal: 7e15 g >> 1 g, and thinner wall = MORE tidal (anti-route)
```

#### line 11831

```
 2. Superluminal NEC: SSV theorem
```

#### line 11839

```
 3. Negative energy: 40 orders short
```

#### line 11849

```
 4. Steering: horizon lock at beta > 1
```

#### line 11855

```
 5. Thermal: T at 2c > limit, but passable with more radiators
```

#### line 11866

```
 6. Ford-Roman wall: 100 L_P, E = 10^79 J
```

#### line 11875

```
 7. QI throat: 26 orders short
```

#### line 11882

```
 8. CTC: chronology protection
```

#### line 11886

```
 Scorecard consistency
```

#### line 11898

```
--- geometry -----------------------------------------------------------
```

#### line 11916

```
 --- SPECIAL WORKS: the car-scale twin, audited like everything else ---
```

#### line 12013

```
 EXTREME CONDITIONS -- hostile inputs and limit cases the drive loop
 must survive. car_mph_step is the same function the update loop calls.
```

#### line 12060

```
 extreme ephemeris: poles, the far past/future, whole-envelope hops
```

#### line 12095

```
 --- TRANSIT: the same-road-spot ephemeris, audited ----------------------
```

#### line 12292

```
 --- drawn geometry must match the billed spec ------------------------
```

#### line 12327

```
 loft ring -> (z, skin radius) table, then interpolate: the loft's
 ring spacing is far coarser than any z sample we will ask about
```

#### line 12364

```
 a trap that pierces a slab must find its drawn opening: rebuild the
 billed hole (sphere cross-section at the slab's near face + collar
 tolerance) and require a rim of plate verts at that radius
```

#### line 12439

```
 every billed RCS pod must actually be drawn (ring capacity is not
 guaranteed -- a spec change could silently drop pods), and no pod
 may sit inside a Penning sphere or the reactor torus
```

#### line 12472

```
 --- a whole flight, audited -------------------------------------------
```

#### line 12488

```
 dead configuration: position/velocity frozen -> mission stalled,
 fail the check honestly instead of burning the whole iteration budget.
 nan == nan is False, so a non-finite signature never repeats -- count
 any non-finite state as stagnant directly.
```

#### line 12504

```
 --- TEST-mode demo state machine ----------------------------------------
```

#### line 12537

```
 --- NUMERICAL STABILITY & EDGE CASES ------------------------------------
 These tests push the functions to their limits to catch overflow,
 underflow, and boundary-condition bugs.
```

#### line 12541

```
 Shape function at extreme wall thicknesses
```

#### line 12548

```
 Lorentz gamma at extreme betas
```

#### line 12553

```
 gamma is clamped to beta=0.9999999 (avoids singularity at beta=1)
```

#### line 12558

```
 Kinetic energy at extreme betas
```

#### line 12565

```
 Mouth clock rate at extreme values
```

#### line 12576

```
 CTC onset at extreme rate differences
```

#### line 12582

```
 Beam capture at extreme ranges
```

#### line 12588

```
 Magsail drag at extreme betas
```

#### line 12592

```
 Ford-Roman bound at extreme times
```

#### line 12598

```
 Alcubierre energy at extreme wall thickness
```

#### line 12604

```
 Portal traversal: all payload types
```

#### line 12612

```
 Time offset symmetry: forward and backward jumps are equal
```

#### line 12619

```
 CTC onset scales inversely with rate difference
```

#### line 12625

```
 Gravitational drift over the actual voyage
```

#### line 12630

```
 Warp transport gives zero desynchronization (flat interior)
```

#### line 12637

```
 Rocket transport gives large desynchronization
```

#### line 12645

```
 --- AMPLIFICATION MECHANISMS --------------------------------------------
 Single wormhole is bounded by elapsed time; chained wormholes
 multiply the offset by N.
```

#### line 12654

```
 Chain of N wormholes: offset = N * elapsed * rate_diff
```

#### line 12662

```
 Nested wormhole: additive, not multiplicative
```

#### line 12668

```
 Tipler cylinder: displacement bounded by L/c at chronology horizon
```

#### line 12677

```
 Tipler below horizon: displacement is small
```

#### line 12682

```
 Gott pair: displacement bounded by deficit angle
```

#### line 12687

```
 Kerr CTC: bounded by spin period
```

#### line 12698

```
 Max displacement comparison: chain wins
```

#### line 12709

```
 --- MULTI-JUMP: iterated traversal -------------------------------------
```

#### line 12714

```
 Cycle time = D/(beta c) + overhead
```

#### line 12722

```
 Breakeven fixed point t* = Delta / r
```

#### line 12729

```
 Backward recurrence converges to t* and total past = elapsed - t*
```

#### line 12747

```
 Backward cycles before breakeven are net-FORWARD (honest ordering)
```

#### line 12754

```
 Forward recurrence is geometric (1+r)^k
```

#### line 12772

```
 Energy ledger per cycle = cruise_load * Delta; fuel math round-trips
```

#### line 12783

```
 ISM scoop: raw flux = A * n * m_p * v; yield is a small isotope fraction
```

#### line 12795

```
 Sustainability verdict consistent with the arithmetic
```

#### line 12803

```
 Scoop parity: below ~0.27c the housekeeping burn floor beats the
 beta-proportional scoop yield -- refuelling only sustains underway
```

#### line 12811

```
 The x8-heavier pass-7 hull lost the scoop-parity window entirely:
 the burn floor (~1.7 kg/day housekeeping at 0.05c) exceeds the
 slow-beta yield, and burn grows ~b^2 while yield is linear in b.
 Swept minimum net is ~-0.7 kg/day at 0.2-0.3c -- still negative.
```

#### line 12830

```
 Fuel-out detection: slow beta + tiny stock exhausts in a few cycles
```

#### line 12839

```
 Cruise is net-negative at pass-7 scale, so even a topped-up stock
 does drain -- the plan must REPORT the dry cycle, not hide it.
```

#### line 12845

```
 The plan's breakeven clock must include throat traversal whenever the
 plan's own cycle does -- same b0_m in both places.
```

#### line 12856

```
 Row integrity: every cycle records displacement and energy
```

#### line 12862

```
 --- regression: hostile inputs resolve to honest limits, not crashes ---
```

#### line 12905

```
 --- regression round 2: signed-beta and negative-domain leaks -----------
```

#### line 12943

```
 --- the two boost integrators must agree -------------------------------
 Voyage._step and boost_profile integrate the same beam physics on
 different schedules; a stale per-tick beam power once let the voyage
 lock cruise at 0.893 while boost_profile said 0.857.
```

#### line 13030

```
 Buildability parity: every kilogram of the mass budget must be rated --
 no hardware may hide outside the ledger.
```

#### line 13305

```
 Infinite travel time for an unknown speed is honest -- nan would be
 fine too, but a TypeError would not be.
```

#### line 13444

```
 =============================================================================
 SECTION 10 -- FULL INFORMATIONAL SPECIFICATION  (the I panel)
 =============================================================================
 Every figure below is interpolated from the live physics functions, so the
 panel cannot drift out of step with the model the way a written spec would.
```

#### line 13464

```
 Live geometry: bounding boxes, stations, assembly order and explode
 vectors straight from the meshes the SHIP tab renders.
```

#### line 13472

```
 world verts = spin@0 + tilt + pivot -- exactly what the
 renderer draws; _place'd parts keep origin-built verts and
 carry their station in pivot, so raw verts would misreport
```

#### line 13498

```
 A live voyage so every component can report what it actually carried
 over the mission -- stdout silenced so the panel stays clean.
```

#### line 13707

```
 live mount text: stations read back from the built meshes so the
 words can never drift from the geometry they describe
```

#### line 14126

```
 Governing spec keys derived live: every DIMS key whose name starts
 with the component's prefix. Drift-proof -- rename a key and the
 link follows it.
```

#### line 14671

```
 key -> first source line index, found once up front so each lookup is O(1)
```

#### line 15937

```
 =============================================================================
 SECTION 11 -- HUD / UI HELPERS
 =============================================================================
```

#### line 15953

```
 pixels3d gives (w, h, 3) view; broadcast the column gradient across width
```

#### line 16042

```
 vertical gradient fill via numpy (fast)
```

#### line 16059

```
 border: brighter for a cleaner modern edge
```

#### line 16062

```
 top-edge highlight: one brighter line for depth (LS.py pattern)
```

#### line 16139

```
 active: filled background with a subtle gradient + bright border
```

#### line 16151

```
 inactive: subtle dark fill + thin outline
```

#### line 16167

```
 An unmaterialized iterable (range(10**9), itertools.count()) would
 be realized by np.asarray into an arbitrarily large array -- cap it.
```

#### line 16239

```
 the view controls belong to the ship model; here they do nothing
```

#### line 16268

```
 blackbody-ish star colours by spectral class (R, G, B)
```

#### line 16277

```
 probability weights: cool stars dominate a real stellar population
```

#### line 16285

```
 assign each star a spectral class index by the weighted distribution
```

#### line 16355

```
 bright nearby stars get a 2px cross; faint ones a single pixel
```

#### line 16389

```
 pulse: +/- 15% intensity at 0.5 Hz (2-second period)
```

#### line 16397

```
 sharper core, softer edges: alpha falls as (1-t)^2 for inner,
 (1-t)^1.4 for outer
```

#### line 16409

```
 bright inner core: a tight, high-alpha circle for the energy field
```

#### line 16453

```
 finer grid for smoother gradient (smaller step = less banding)
```

#### line 16459

```
 quadratic falloff for a smoother, more cinematic edge
```

#### line 16469

```
 =============================================================================
 SECTION 12 -- APPLICATION
 =============================================================================
```

#### line 16473

```
 The cross-section cuts EVERY part. Leaving the radiators and the bubble
 whole meant the cutaway was still looking at the outside of the ship.
```

#### line 16505

```
 a second, lower-detail copy for the FLIGHT inset: the extra facets
 are invisible at chase distance and cost half the frame budget
```

#### line 16514

```
 the portal gate has its own model and its own framing
```

#### line 16519

```
 the car-scale twin: whole drive folded into a 4.2 m coupe
```

#### line 16554

```
 ------------------------------------------------------------------ setup
```

#### line 16558

```
 invalidate the vignette cache so it rebuilds at the new size
```

#### line 16600

```
 ----------------------------------------------------------------- events
```

#### line 16652

```
 the top-bar tabs are real buttons: switch views on click
```

#### line 16769

```
 the user zeroed beta_cmd mid-demo: no boost is possible, say so
```

#### line 16777

```
 honest ending #2: no destination array means the magsail needs
 ~3.3e4 ship-years; a demo should say so and stop, not run for
 an hour of real time pretending otherwise
```

#### line 16790

```
 drop to a slow clock: an over-driven shell lets go in minutes of
 ship time, and at 30 d/s you would never see it happen
```

#### line 16836

```
 ---- drive
```

#### line 16893

```
 a reset stands the car down too -- no ghost run or scar left
```

#### line 16907

```
 ----------------------------------------------------------------- update
```

#### line 16926

```
 the WD-88 run: throttle/brake drive speed, the transition arms
 itself at 88 mph and the shell ramps in over ~1.2 s. Held keys are
 polled here so holding W/UP accelerates continuously. Paused means
 paused: the car freezes mid-run the same way the mission does.
```

#### line 16944

```
 cell thermal balance: drive waste + the transition dump, all
 rejected by the louver bank. A louver fault collapses the
 rejection area and the cell heat-soaks -- the ops ledger's
 promised failure, run live.
```

#### line 16975

```
 part visibility follows the physical state, in both renderers
```

#### line 16987

```
 ------------------------------------------------------------------- draw
```

#### line 17003

```
 subtle vignette: focus the eye on the central viewport without a
 hard border (cinematic depth, cached on resolution)
```

#### line 17014

```
 top-centre, under the bar: the bottom of the screen belongs to the
 METRIC profile plots and the FLIGHT control strip
```

#### line 17022

```
 ---- top bar ----------------------------------------------------------
```

#### line 17026

```
 top bar: gradient fill + bottom border for a modern app-bar look
 (the gradient surface is static -- cache it per window width)
```

#### line 17078

```
 ---- SHIP mode --------------------------------------------------------
```

#### line 17150

```
 the one comparison that matters
```

#### line 17195

```
 ---- METRIC mode ------------------------------------------------------
```

#### line 17211

```
 A POLAR sheet in the plane containing the direction of travel, with
 the radial samples CROWDED onto the wall. A uniform Cartesian grid
 cannot see this: with a 1 m wall on a 100 m bubble, theta is a spike
 one metre wide and a uniform grid steps straight over it, drawing a
 flat sheet and a comfortable lie. Concentrating the samples where the
 curvature actually lives resolves it at any wall thickness.
```

#### line 17273

```
 first pass: additive glow on the high-curvature segments (the wall)
```

#### line 17284

```
 second pass: the actual grid lines
```

#### line 17291

```
 the ship, and where it is pointed -- with a glow halo
```

#### line 17297

```
 ship marker: additive glow + solid dot (LS.py pattern)
```

#### line 17457

```
 ---- FLIGHT mode ------------------------------------------------------
```

#### line 17467

```
 Relativistic Doppler colour wash: at high beta the forward starfield
 blue-shifts and the aft red-shifts. We paint a subtle additive
 gradient over the streaked stars -- not a physical ray-trace, but
 the same visual cue SE.py uses for its day/night sky transition.
```

#### line 17474

```
 top (forward / ahead) gets a faint blue wash
```

#### line 17481

```
 bottom (aft / behind) gets a faint red wash
```

#### line 17496

```
 engine glow trail: an additive plume behind the ship when the
 reactor is driving the coils (bubble_on > 0). Matches the
 GmansRun combustion-glow pattern: layered alpha circles, additive.
```

#### line 17531

```
 --- mission ------------------------------------------------------
```

#### line 17569

```
 --- clocks -------------------------------------------------------
```

#### line 17593

```
 --- power and thermal --------------------------------------------
```

#### line 17635

```
 --- ledger -------------------------------------------------------
```

#### line 17665

```
 --- log ----------------------------------------------------------
```

#### line 17735

```
 ---- DILATION mode ----------------------------------------------------
```

#### line 17751

```
 nested shells, coloured by the static observer's clock rate
```

#### line 17759

```
 Stretch the colour ramp across the range the field ACTUALLY spans.
 The lapse only runs from 1/gamma to 1, so mapping it raw to a colour
 paints everything the same shade and hides the whole point.
```

#### line 17777

```
 ship marker with additive glow (consistent with METRIC view)
```

#### line 17817

```
 1: the dilation profile across the bubble
```

#### line 17846

```
 2: gravitational clock rate along the route
```

#### line 17948

```
 ---- PORTAL mode ------------------------------------------------------
```

#### line 18008

```
 --- Ford-Roman quantum inequalities + MMP + Visser ----------------
```

#### line 18064

```
 the teleporter that actually exists
```

#### line 18094

```
 ---- SPECIAL WORKS -- the WD-88 Foldmobile ------------------------------
```

#### line 18126

```
 speedometer
```

#### line 18139

```
 progress to the trigger line, with the mark drawn honestly
```

#### line 18199

```
 run controls
```

#### line 18228

```
 TRANSIT panel -- the "same road spot" solve. The landing zone is
 an Earth-fixed coordinate: Earth orbits the Sun and spins between
 departure and arrival, so the same pavement sits at a different
 inertial position at t1. The bubble has to close on where the
 road WILL be, not on where space used to be.
```

#### line 18240

```
 before the run fires, preview the solve as if it fired NOW --
 the same math, just not stamped yet
```

#### line 18252

```
 ephemeris drift: the unit can no longer hold the road fix --
 the honest display is the UNARMED outcome, not a frozen solve
```

#### line 18293

```
 how the solve works -- two frames, one rotating transform
```

#### line 18303

```
 ecliptic mini-map -- the orbit ring, the sun, the two events
```

#### line 18320

```
 ---- ENERGY LADDER chart (M) -----------------------------------------
```

#### line 18335

```
 axis
```

#### line 18367

```
 only the citation name fits beside the axis; the descriptions
 live in the I panel and in --ladder
```

#### line 18404

```
 ---- help -------------------------------------------------------------
```

#### line 18439

```
 ---- full spec (I) ----------------------------------------------------
```

#### line 18480

```
 ------------------------------------------------------------------- loop
```

#### line 18491

```
 =============================================================================
 SECTION 13 -- ENTRY POINT
 =============================================================================
```

#### line 18551

```
 --- Boundary coercion sweep -------------------------------------------------
 Every helper whose parameters are all numeric gets _args_real applied here,
 once, instead of a guard line inside each body. A poisoned argument (str,
 None, list, complex) becomes NaN at the boundary and propagates honestly;
 it can no longer TypeError its way out of a report or a draw pass.
```

#### line 18590

```
 argparse indexes into each token assuming str; a bytes/None/int token
 TypeErrors inside its pattern matching.  Coerce before parsing.
```

*714 comment blocks.*

## The per-tick pipelines (what `update()` actually runs)

The ordered sequence of model calls inside each integrator step, harvested from the source AST -- the live order of operations, not a summary of it.

### `WarpCore.update()` -- one drive tick: loads -> fuel -> thermal lag -> integrity -> beam -> SMES -> exotic bill -> plant supply

`clamp` -> `cruise_load_w` -> `waste_heat_w` -> `fusion_fuel_kg` -> `clamp` -> `_thermal` -> `_integrity` -> `_finite` -> `_real` -> `beam_power_w` -> `smes_store_j` -> `alcubierre_energy_j` -> `_finite` -> `_coil_count` -> `plant_electric_w` -> `_finite` -> `plant_electric_w` -> `_real`


### `Voyage._step()` -- one mission tick: kinetic ledger -> clocks -> beam accel -> brake drag -> position/phase

`_real` -> `ship_mass_kg` -> `kinetic_energy_j` -> `grav_rate` -> `_earth_rate` -> `_finite` -> `beam_power_w` -> `kinetic_energy_j` -> `_finite` -> `magsail_drag_n` -> `beam_brake_force_n` -> `lorentz_gamma` -> `fmt_dist` -> `fmt_time` -> `magsail_decel_time_s`


### `Voyage.update()` -- frame wrapper: splits a real dt into _step slices and runs auto_step for TEST mode

`_step` -> `_finite`



## The independent audit's own checks

`_scale_audit.py` re-derives everything independently; these are its `check()`/`close()` call sites in source order -- loops expand them to the 70 executed checks (one per component, per envelope part, per count).

1. dry mass = sum of components (model)
2. documented dry mass 1,081,381 t
3. bubble_r = 100 m x SCALE_S
4. ring_major_d = 2 x bubble_r
5. hull_wall = 0.22 x hull_d/16 (hoop-stress t ~ r)
6. flat interior = R - 6 delta
7. envelope: every part inside interior
8. envelope reach matches check_envelope()
9. SHIP_SPAN_M
10. SHIP_LEN_M
11. radiator area (both faces)
12. documented area 339,910 m^2
13. SMES stored energy
14. documented SMES 2.76 TJ
15. plant electric
16. documented electric 63.7 GW
17. reactor = 1.35x margin over beta=0.99 load
18. T at beta=0.99 = 1439 K (doc)
19. T at beta=0.99 < 1900 K limit
20. T at beta=2 = 1961 K (doc)
21. T at beta=2 > 1900 K limit (barrier kept failing)
22. area needed at 1900 K for beta=2 = 385,910 m^2
23. +13.5% area claim
24. spot at 0.1 ly ~2.3 km
25. spot at 0.5 ly = 11.5 km
26. capture at 0.1 ly = 100%
27. capture at 0.5 ly = 12%
28. capture at 0.62 ly = 7.8%
29. KE at beta=0.855 ~ 90 YJ (doc-rounded)
30. model KE agrees
31. KE at beta=0.9 = 125.9 YJ (doc)
32. emergent beta = 0.855 (doc)
33. emergent beta is subluminal
34. Casimir density = -4.334e4 J/m^3 (10 nm)
35. total Casimir = -3.09 MJ (doc)
36. model agrees
37. doc figure -5.66e47 J at beta=1
38. shortfall ~41 orders (doc)
39. full-stop ~32,600 yr (doc)
40. coil_bore = tube dia + 2x standoff (coil wraps the tube)
41. coil bore clears the tube it energises
42. drift = +1.55 s over the 4.97 yr crossing
43. name
44. 'count %s = %d' % (k, want)

## Repository map (every file)

| File | Size | Role |
|------|------|------|
| `CUsersNathanAppDataLocalTempallout.txt` | 80535 B | historical run/test artifact (stale) |
| `CUsersNathanDesktopWarpdrive_r8b.txt` | 4125 B | historical run/test artifact (stale) |
| `Infornmational.md` | 890267 B | this file |
| `NUL` | 0 B | accidental console-redirect artifact (stale) |
| `README.md` | 80934 B | theory, proofs and user guide |
| `ReferenceCode` | -- | reference material (not part of the model) |
| `Warpdrive.py` | 971520 B | the model + viewer + CLI (everything) |
| `__pycache__` | -- | python bytecode cache |
| `_all7.txt` | 86537 B | historical run/test artifact (stale) |
| `_all7b.txt` | 86537 B | historical run/test artifact (stale) |
| `_all8.txt` | 86640 B | historical run/test artifact (stale) |
| `_all_out.txt` | 86222 B | historical run/test artifact (stale) |
| `_all_out2.txt` | 86276 B | historical run/test artifact (stale) |
| `_fuzz_props.py` | 7918 B | hostile-input property fuzzer |
| `_fuzz_stress.py` | 14357 B | hostile-input stress fuzzer |
| `_fz1.txt` | 22 B | historical run/test artifact (stale) |
| `_fz2.txt` | 30 B | historical run/test artifact (stale) |
| `_gen_info.py` | 188483 B | this document's generator |
| `_r8_probe.py` | 1532 B | historical run/test artifact (stale) |
| `_scale_audit.py` | 14005 B | independent re-derivation audit |
| `_selftest_out.txt` | 28210 B | historical run/test artifact (stale) |
| `_spec7.txt` | 2914 B | historical run/test artifact (stale) |
| `_st7.txt` | 28368 B | historical run/test artifact (stale) |
| `_st7b.txt` | 28368 B | historical run/test artifact (stale) |
| `_st8.txt` | 28455 B | historical run/test artifact (stale) |
| `_sweep_log.txt` | 7121 B | historical run/test artifact (stale) |
| `howitworks.md` | 33301 B | narrative explanation of the logic |
| `overview.md` | 24619 B | high-level summary + refit rationale |

## The message catalog (every user-facing string)

Every string the model can say at runtime: `print()` output, mission-log `note()`s, viewer `flash()`es and `collapse()` reports -- harvested from the call sites, so the vocabulary of the twin is itself documented.

### `print(...)` output (468 sites)

-  The portal is a wormhole with two mouths.  WHERE you come out is
-  where mouth B physically IS.  WHEN you come out depends on the
-  clock desynchronisation between the mouths -- real GR, the same
-  effect GPS corrects for daily.  Four scenarios: 
- ' ' + '-' * 76
-  SCENARIO 1: signal (photon) through the 12 m gate, mouths synced
-    A photon has no size, so tidal forces cannot destroy it.  But
-    the throat still cannot stay open long enough (QI), and the
-    exotic bill is still unpaid.  The signal cannot cross. 
-  SCENARIO 2: person through the survivable throat, mouths synced
- '   The throat is wide enough to survive (b0 = %.2e m = %.1f Earth' % (safe_b0, safe_b0 / 12742000.0)
- '   diameters).  But the exotic energy is %s and the QI still' % fmt_energy(t2['exotic_j'])
- '   forbids holding it open for the %.1f s traversal.\n' % t2['traverse_s']
-  SCENARIO 3: person, mouth B at Phi/c^2 = -0.01 (deep well), 1 yr
- "   Mouth B's clock runs slower by %.4e s/s.  After %s the offset" % (t3['rate_diff'], fmt_time(elapsed))
- '   is %s.  Light-time between mouths is %s.' % (fmt_time(t3['offset_s']), fmt_time(t3['light_time_s']))
-  SCENARIO 4: TIME MACHINE -- mouth B at Phi/c^2 = -0.2, 20 years
- "   Mouth B's rate: %.6f vs A's %.6f.  After %s the offset is %s." % (t4['rate_b'], t4['rate_a'], fmt_time(elapsed4), fmt_time(t4['offset_s']))
- '   Light-time between mouths: %s.' % fmt_time(t4['light_time_s'])
-  SCENARIO 5: mouth B on a rocket at beta = 0.9, 10 years
-    A relativistic rocket DOES desynchronise the mouths (unlike a
-    warp drive, whose flat interior gives no dilation dividend).
- '   Rate gap: %.4e s/s.  Offset after %s: %s.' % (t5['rate_diff'], fmt_time(elapsed5), fmt_time(t5['offset_s']))
-  SCENARIO 6: mouth B carried by WARP at beta = 0.9, 10 years
-    The warp drive's flat interior means NO kinematic dilation.
- '   Rate gap: %.2e s/s -- zero (both mouths at rest in flat space).' % t6['rate_diff']
-    The FAST thing cannot build the time machine.  The slow rocket
-    can.  This is ctc_by_warp_transport() in full arithmetic. 
-  SCENARIO 7: MAX DESYNC -- mouth B at neutron star + 0.99c, 1 AU, 1 yr
- '   Mouth B sits on a neutron-star surface (Phi/c^2 = %.2f) AND moves' % phi_ns
- '   at beta = %.2f on a rocket.  Combined rate: %.6f -- B ages at' % (beta_rocket, t7['rate_b'])
- '   %.1f%% the rate of A.  At 1 AU separation the light-time is' % (100.0 * t7['rate_b'])
- '   only %.0f s (%.1f min), so CTC onset is in %.0f s (%.1f min).' % (t7['light_time_s'], t7['light_time_s'] / 60.0, t7['onset_s'], t7['onset_s'] / 60.0)
-  SCENARIO 8: MAX BACKWARD JUMP -- same desync, 100 years elapsed
- '   After 100 years, the offset is %.2f years = %.0f days.' % (t8['offset_s'] / YR, t8['offset_s'] / DAY)
- '   Step A->B: arrive %.2f years in your own past.' % (t8['offset_s'] / YR)
- '   Step B->A: arrive %.2f years in your own future.' % (t8['offset_s'] / YR)
-    This is the MAXIMUM time jump the portal geometry can produce
-    with realistic astrophysical wells and realistic rocket speeds.
-    The throat is still closed -- see verdict below. 
-  SCENARIO 9: EXTREME -- mouth B near horizon + 0.999c, 1 AU, 100 yr
- '   Mouth B hovers just above a black-hole horizon (Phi/c^2 = %.2f)' % phi_bh
- '   AND moves at beta = %.3f.  Combined rate: %.6f -- B ages at' % (beta_extreme, t9['rate_b'])
- '   %.2f%% the rate of A.  After 100 yr the offset is %.2f years.' % (100.0 * t9['rate_b'], t9['offset_s'] / YR)
- '   Step A->B: arrive %.2f years in the past.' % (t9['offset_s'] / YR)
- '   Step B->A: arrive %.2f years in the future.' % (t9['offset_s'] / YR)
-    This is the theoretical ceiling for wormhole time travel with
-    known astrophysical objects.  The throat is still closed. 
- ' ' + '=' * 76
-  AMPLIFICATION: beyond a single wormhole
-    A single wormhole gives at most ELAPSED years of offset after
-    ELAPSED years of desynchronisation (rate_diff <= 1).  To go
-    further, you need either a CHAIN of wormholes or a different
-    construction entirely.  Four mechanisms: 
-    MECHANISM 1: CHAINED WORMHOLES (N mouths in series)
- '   ' + '-' * 76
-    Offset scales LINEARLY with N.  The exotic-energy bill scales
-    the same way -- each wormhole is an independent throat.
-    QI applies to each independently; chronology protection is
-    expected to destroy the first one before the chain forms. 
-    MECHANISM 2: NESTED WORMHOLES (wormhole inside wormhole)
- '   outer offset = %.2f yr, inner offset = %.2f yr' % (t9['offset_s'] / YR, t9['offset_s'] / YR)
- '   nested total = %.2f yr (additive, not multiplicative)' % (nested / YR)
-    Amplification is bounded by the SUM of offsets, not their
-    product -- nesting helps but does not multiply. 
-    MECHANISM 3: TIPLER CYLINDER (infinite rotating cylinder)
-    At chronology horizon (omega*R = c): displacement = L/c
- '   For L = Proxima (4.25 ly): offset = %.2f yr' % (tipler_off / YR)
- '   For L = 1 ly:              offset = %.2f yr' % (tipler_cylinder_offset(1.0 * LY, tipler_R, tipler_omega) / YR)
- '   For L = 1 AU:              offset = %.2f s' % tipler_cylinder_offset(au_m, tipler_R, tipler_omega)
-    The displacement is UNBOUNDED in L -- travel farther along the
-    cylinder, get proportionally more offset.  But the cylinder
-    must be infinite (or wrap around), and omega*R = c requires
-    R ~ 1 m, omega ~ 3e8 rad/s -- a cylinder spinning at ~50 million
-    rpm.  No material can hold that.  The mechanism is real but
-    the payoff is bounded by L/c for any practical cylinder. 
-    MECHANISM 4: GOTT COSMIC STRINGS (two strings, deficit angle)
-    The deficit angle is fixed by the string tension; the
-    displacement is bounded by delta * D / (4 pi).  For GUT
-    strings (mu ~ 1e21 kg/m) the deficit angle is ~1e-4 rad,
-    so a 1 ly round trip gives ~445 yr of offset.  For electroweak
-    strings (mu ~ 1e-3 kg/m) the offset is ~1e-24 yr -- nothing.
-    The mechanism is real but the payoff depends on the string's
-    energy scale. 
-    MECHANISM 5: KERR BLACK-HOLE CTC (ring singularity)
-    The displacement is bounded by the spin period (2*pi*a/c ~
-    0.3 ms per orbit for a 10 M_sun extremal Kerr).  Multiple
-    orbits add linearly -- 1e6 orbits gives ~5 min.  The ring
-    singularity is inside the inner horizon, which is unstable
-    (mass inflation, Poisson-Israel 1990) -- the physical black
-    hole is expected to be non-traversable. 
-    MAXIMUM DISPLACEMENT COMPARISON (100 yr elapsed, extreme desync)
- '   %-24s %12s' % ('Mechanism', 'Max offset')
- '   %-24s %10.2f yr' % ('Single wormhole', max_d['single_wormhole'] / YR)
- '   %-24s %10.2f yr' % ('Chain of 10 wormholes', max_d['chain_wormhole'] / YR)
- '   %-24s %10.2f yr' % ('Nested wormholes', max_d['nested_wormhole'] / YR)
- '   %-24s %10.2f yr' % ('Tipler cylinder (4.25 ly)', max_d['tipler_cylinder'] / YR)
- '   %-24s %10.2f yr' % ('Gott pair (1 ly, GUT)', max_d['gott_pair'] / YR)
- '   %-24s %10.2e yr' % ('Kerr CTC (10 M_sun)', max_d['kerr_ctc'] / YR)
- '   WINNER: %s (%.2e yr)' % (max_d['max_mechanism'].upper(), max_d['max_offset_s'] / YR)
-    A chain of wormholes multiplies the single-wormhole offset
-    by N.  The exotic-energy bill and all barriers scale the
-    same way -- no barrier is avoided, only multiplied. 
-  MULTI-JUMP: iterated traversal (hop -> external return -> rejump)
-    The ship is the RETURN LEG between mouths.  Each cycle:
- '     hop through (+-delta), external reposition at beta=%.3f' % beta_ship
- '     (%.0f s = %.1f min at 1 AU), rejump.  Offset keeps growing:' % (cyc_au, cyc_au / 60.0)
-      delta(t) = rate_diff * t while the desync condition holds. 
-    BACKWARD loop (step A->B into past, return externally):
-      recurrence t <- t(1-r) + Delta, converges to t* = Delta/r
- '     = %.0f s.  Net-backward only while t > t* -- i.e. AFTER' % be_au
- '     CTC onset (%.0f s).  Cannot evade chronology protection.' % t9['onset_s']
-      ... converges to t* in ~3-4 cycles.
- '     TOTAL reachable past = %.2f yr (elapsed - t*) -- vs %.2f yr' % (back10['max_backward_s'] / YR, t9['offset_s'] / YR)
-      for ONE jump.  Multi-jump reaches nearly all of elapsed. 
-    FORWARD loop (step B->A into future, return externally):
-      recurrence t <- t(1+r) + Delta -- GEOMETRIC, unbounded
-      while the desync condition holds.
- '     ... 10 cycles -> %.3e yr coordinate time.' % (fwd10['final_coord_s'] / YR)
-      Forward travel is exponentially self-amplifying. 
- '   ENERGY LEDGER per cycle (1 AU leg at beta=%.3f):' % beta_ship
- '     ship load held    : %s (cruise_load at constant beta)' % fmt_power(back10['load_w'])
- '     energy per cycle  : %s' % fmt_energy(back10['energy_per_cycle_j'])
- '     fuel burnt/cycle  : %.4e kg D-3He' % (back10['fuel_burnt_kg'] / back10['cycles'])
- '     ISM scoop flux    : %.2f kg/day raw gas (magsail sweeps A*v)' % (ism_scoop_gas_kg_s(beta_ship) * DAY)
- '     D-3He yield       : %.3f kg/day (isotope-lean: D/H 2e-5,' % (ism_d3he_yield_kg_s(beta_ship) * DAY)
-        3He/4He 2e-4, after perfect enrichment)
- '     scooped/cycle     : %.4e kg vs burnt %.4e kg -> %s' % (back10['fuel_scooped_kg'] / back10['cycles'], back10['fuel_burnt_kg'] / back10['cycles'], 'SELF-SUSTAINING while underway' if back10['fuel_sustainable'] else 'NET CONSUMER')
-      Standing still the scoop is zero and housekeeping still
- '     burns ~%.2f kg/day -- refuelling requires motion.' % fusion_fuel_kg(cruise_load_w(0.0) * DAY)
-      Scoop parity ~ beta = 0.27: below it the cryo+hotel burn
- '     floor beats the beta-proportional isotope yield (%s at 0.27c).' % ('yield >= burn' if parity else 'burn > yield')
- '     Exotic per hop    : %s (throat, NOT ship-payable -- flagged)' % fmt_energy(back10['exotic_j_per_hop'])
-    Ship fuel is a non-issue at 1 AU (milligrams/cycle); at
- '   Proxima-scale separation each cycle burns ~%.1f t and scoops' % (multijump_plan(1, elapsed8, r_ext, PROXIMA_M, beta_ship, 'backward')['fuel_burnt_kg'] / 1000.0)
- '   ~%.1f t -- still net-positive while moving.' % (multijump_plan(1, elapsed8, r_ext, PROXIMA_M, beta_ship, 'backward')['fuel_scooped_kg'] / 1000.0)
-  CONTROL SUMMARY: what GR actually lets you control
-    WHERE (exit location):  move mouth B.  The wormhole connects
-      A to B -- you cannot choose the exit independently of B.
-    WHEN (arrival time):    desynchronise the mouths by parking B
-      in a gravity well (scenario 3) or moving it at relativistic
-      speed (scenario 5).  The offset accumulates linearly and is
-      the same dilation GPS measures daily.
-    CTC ONSET:              when |offset| > D/c (light-time between
-      mouths).  Before that: B's past, not your past.  After that:
-      time machine -- Hawking CPC expects destruction.
-    WARP CANNOT DESYNC:     a warp bubble's interior is flat, so a
-      mouth carried by warp ages at the same rate as one at rest.
-      The fast thing cannot build the causality violation.
-    MAXIMUM TIME TRAVEL (scenarios 7-9, pushing to physical limits):
- '     Max rate difference:   %.4f (neutron star + 0.99c rocket)' % t7['rate_diff']
- '     Min CTC onset:         %.0f s (%.1f min) at 1 AU separation' % (t7['onset_s'], t7['onset_s'] / 60.0)
- '     Max backward jump:     %.2f years (100 yr elapsed, step A->B)' % (t8['offset_s'] / YR)
- '     Max forward jump:      %.2f years (same offset, step B->A)' % (t8['offset_s'] / YR)
- '     Extreme ceiling:       %.2f years (horizon + 0.999c, 100 yr)' % (t9['offset_s'] / YR)
-      BOTH directions are    the SAME offset -- the wormhole is
-      symmetric:             step A->B for the past, B->A for the
-                              future.  No new physics either way.
-    THE WARP DRIVE ITSELF produces almost no time shift:
-      (crew age this much MORE than Earth -- leaving Sol's well
-       makes their clock run faster.  Not controllable: set by
-       the gravitational potential difference between Sol and
-       Proxima, which is fixed by astrophysics.)
-      Kinematic dilation:    0.0 s (flat interior -- no dividend)
-      Warp-transport desync: 0.0 (cannot build a time machine)
-    EVERY scenario is blocked by at least one of:
- '     - exotic energy (no source exists; %.0f orders short of Casimir)' % t2['shortfall_orders']
- '     - quantum inequalities (throat closes in %.2e s vs %.1f s cross)' % (t2['qi_hold_s'], t2['traverse_s'])
-      - chronology protection (CTCs -> throat destruction)
-    The portal is the warp drive's problem again, in a new shape,
-    with a time machine on top.
- '   throat b0         %.3g m' % _real(t.get('b0_m'))
- '   mouth separation  %.3g m = %.4f ly' % (_real(t.get('mouth_sep_m')), _real(t.get('mouth_sep_ly')))
- '   rate A / rate B   %.6f / %.6f  (gap %.3e s/s)' % (_real(t.get('rate_a')), _real(t.get('rate_b')), _real(t.get('rate_diff')))
- '   elapsed           %s' % fmt_time(t.get('elapsed_s'))
- '   time offset       %s  %s' % (fmt_time(_off), '(unknown)' if math.isnan(_off) else '(B behind A)' if _off > 0 else '(B ahead of A)' if _off < 0 else '(synced)')
- '   light-time A->B   %s' % fmt_time(t.get('light_time_s'))
- '   CTCs exist        %s  (margin %s)' % ('YES' if t.get('ctc') is True else 'unknown' if not isinstance(t.get('ctc'), bool) else 'no', fmt_time(t.get('ctc_margin_s')))
- '   tidal shear       %s' % str(t.get('tidal_verdict', 'n/a'))
- '   throat hold       %s' % str(t.get('qi_verdict', 'n/a'))
- '   exotic energy     %s  (%.0f orders beyond Casimir)' % (fmt_energy(t.get('exotic_j')), _real(t.get('shortfall_orders')))
- '   VERDICT           %s' % str(t.get('overall', 'n/a'))
- '\n' + '=' * 78
- ' ' + str(title)
- '=' * 78
- ' linear scale %.4f x WD-1   dry mass %s   crew %d' % (SCALE_S, fmt_mass(total), int(d['crew']) if _finite(d['crew']) else 0)
- ' flat interior %.1f m   bubble radius %.1f m   wall %.3g m' % (flat_interior_r(), d['bubble_r_m'], d['wall_thick_m'])
- '\n  %-22s %-46s %10s %6s' % ('COMPONENT', 'SPECIFICATION', 'MASS', 'SHARE')
- '  ' + '-' * 90
- '  %-22s %-46s %10s %6.1f%%' % ('TOTAL', '', fmt_mass(total), 100.0)
- '\n  envelope: %s' % env['verdict']
- '  length %.0f m x span %.0f m   emergent cruise beta %.4f' % (SHIP_LEN_M, SHIP_SPAN_M, max_boost_beta())
- '  plant: %.2f GW th -> %s el   loads %.1f MW el at beta=0.99 cruise' % (d['reactor_th_gw'], fmt_power(plant_electric_w()), cruise_load_w(0.99) / 1000000.0)
- '  boost beam: %s from a %.0f km array at 1 um, usable to %.2f ly' % (fmt_power(PLANT['tap_w']), PLANT['beam_aperture_km'], PLANT['beam_range_ly'])
- '  magsail alone halves beta=0.5 in %s; a destination array is' % fmt_time(magsail_halving_time_s(0.5))
-   still REQUIRED for rendezvous (see --voyage).
-  ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2
-  f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R)),  sigma = 1/delta
- ' bubble radius R = %.0f m,  flat interior to %.1f m,  c^4/G = %.4e N' % (R, flat_interior_r(), C4_OVER_G)
- '\n SHAPE FUNCTION across the wall (delta = %.3g m):' % DIMS['wall_thick_m']
- '   %-12s %-12s %-14s %-16s' % ('r [m]', 'f(r)', 'df/dr [1/m]', 'T^00 [J/m^3]')
- '\n ENERGY vs WALL THICKNESS at beta = 1 (R = %.0f m):' % R
- '   %-14s %-16s %-22s %s' % ('delta [m]', 'E [J]', 'equivalent mass', 'status')
- '\n ENERGY vs BETA (delta = %.3g m):' % d0
-   TIDAL SHEAR IN THE WALL (2 m body, beta = 0.5):
- '   Interior (r < %.1f m): f = 1, all derivatives zero, EXACTLY 0 g.' % flat_interior_r()
-   CASIMIR REALITY CHECK (the only real negative energy there is):
- '   rho(%.0f nm gap) = -pi^2 hbar c / 720 a^4 = %.4g J/m^3' % (DIMS['casimir_gap_nm'], cas['rho_j_m3'])
- '   onboard lattice  = %s across %d cassettes' % (fmt_energy(casimir_onboard_j()), int(DIMS['casimir_cassettes']) if _finite(DIMS['casimir_cassettes']) and DIMS['casimir_cassettes'] >= 0 else 0)
- '   beta=1, 1 m wall needs %s  -> short by %.0f orders of magnitude' % (fmt_energy(need), orders_of_magnitude(need, casimir_onboard_j()))
- '   with the QI-legal wall  -> short by %.0f orders of magnitude' % orders_of_magnitude(needq, casimir_onboard_j())
- ' Baseline: R = %.0f m, beta = 1, delta = 1e-15 m -> %s (%s)\n' % (DIMS['bubble_r_m'], fmt_energy(base), fmt_mass(equiv_mass_kg(base)))
-  WHERE THAT LEAVES US:
-    Superluminal  -- every route still ends at a NEC violation, and
-                     Santiago, Schuster & Visser (2022) proved that is
-                     generic, not an artefact of Alcubierre's ansatz.
-    Subluminal    -- genuinely solved on paper. Positive energy, real
-                     matter, all energy conditions satisfied. What
-                     remains is an engineering bill this file prices.
- '\n' + '-' * 78
- ' SCORE: ' + '   '.join(('%s %d/%d' % (k, v, n) for k, v in sorted(tally.items())))
-   HARDWARE BUILDABILITY  --  when could each line be ordered 
- '\n SHIP: ' + '   '.join(('%s %d/%d' % (k, v, len(led['ship'])) for k, v in sorted(tally2.items())))
- '\n THE HONEST SUMMARY\n   A SUBLUMINAL warp drive is not science fiction. It is a solved problem in\n   general relativity with a brutal engineering bill: %s to reach half\n   lightspeed, a stellar-scale transmitter to deliver it, a second one at the\n   far end to stop, and a shell material nobody knows how to make. Every one\n   of those is an engineering obstacle, and none of them is a violated law.\n\n   A SUPERLUMINAL warp drive is a different kind of thing. It needs negative\n   energy in bulk, and the shortfall is not %d%% or %dx -- it is %.0f orders\n   of magnitude against the best real source in physics, with a theorem\n   standing behind the requirement. That is not a technology gap.\n\n   This model flies both. It only ever claims one.' % (fmt_energy(kinetic_energy_j(0.5)), 20, 1000, orders_of_magnitude(alcubierre_energy_j(1.0, DIMS['bubble_r_m'], 1.0), casimir_onboard_j()))
- '\n   WHAT A PROCUREMENT OFFICE COULD ACTUALLY ORDER\n   %d of %d hardware lines are TODAY -- hull, decks, spars, shield,\n   thrusters, cryo. %d more are NEAR -- coils, storage, panels, rectenna,\n   life support: a decade of engineering, not of physics. The reactor, sail,\n   traps and lattice wait on industries that do not exist; the two rings\n   wait on a material nobody has named. The ship is buildable in the near\n   future -- except the part that makes it a warp drive.' % (today, len(led['ship']), near)
-  From the metric, two observers and two completely different answers:
-    COMOVING (the crew, dx = v_s f dt, f = 1):
-        ds^2 = -c^2 dt^2      ->  dtau = dt EXACTLY. No dilation, ever.
-    STATIC  (holds station in the external frame, dx = 0):
-        dtau = dt sqrt(1 - beta^2 f(r)^2)   -- the full Lorentz factor
-   STATIC-OBSERVER CLOCK RATE INSIDE THE BUBBLE:
- '   %-8s %-14s %-14s %s' % ('beta', 'at centre', 'at the wall', 'outside')
- '   %-8.2f %s' % (2.0, 'NO STATIC OBSERVER EXISTS -- every worldline inside is dragged past c.')
-    That last line is the horizon problem, showing up as arithmetic
-    rather than as a footnote.
-   GRAVITATIONAL ENVIRONMENT ALONG Sol -> Proxima:
- '   %-22s %-18s %s' % ('position', 'Phi/c^2', 'clock rate')
-   THE ONLY REAL DRIFT:
- '   crossing at beta = %.4f takes %s' % (beta, fmt_time(t))
- '   crew clock MINUS Earth clock: %+.4f s' % drift
-    -- all of it gravitational (climbing out of Sol's well), not one
-       microsecond of it velocity dilation.
- '   a relativistic ROCKET at the same beta would arrive %s YOUNGER.' % fmt_time(t - rocket_proper_time_s(beta, PROXIMA_M))
-    The warp drive gives up the dilation dividend and buys arrival in
-    step with home. That is a trade, not a free win.
- "\n   the ship's own gravity contributes %.3e -- two orders below" % ship_self_dilation()
-    the best clock ever built, which is how we know it is negligible.
-  ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2   (Morris & Thorne 1988)
-  No horizon, no singularity, traversable both ways. A perfectly good
-  solution of the Einstein field equations -- written down in 1988 as a
-  TEACHING EXERCISE precisely because it is easy to construct and
-  impossible to build. 
-  THE GATE AS SPEC'D:
- '   aperture 2 b0            %.0f m' % DIMS['portal_gate_d_m']
- '   throat radius b0         %.1f m' % ps['b0_m']
- '   energy density at throat %s per m^3   (rho = -c^4/8 pi G b0^2)' % fmt_energy(ps['density_j_m3'])
- '   total exotic energy      %s  (%s)' % (fmt_energy(ps['energy_j']), fmt_mass(ps['mass_kg']))
- '   tidal shear crossing it  %.3e g across a 2 m body' % ps['tidal_g']
-    -> nothing made of atoms survives that crossing. 
-  THE THROAT YOU WOULD ACTUALLY SURVIVE:
-    tidal goes as c^2 L / b0^2, so 1 g across 2 m needs
- '   b0 >= %.4g m  =  %.1f Earth diameters' % (ps['safe_b0_m'], ps['safe_b0_m'] / 12742000.0)
- '   its exotic bill: %s  (%s)' % (fmt_energy(ps['safe_energy_j']), fmt_mass(ps['safe_mass_kg']))
-    Morris & Thorne reached this same conclusion in 1988. 'Portal' and
-    'doorway' turn out not to be the same word. 
-  THE FULL METRIC, NOT JUST THE THROAT:
-    ds^2 = -e^(2Phi) c^2 dt^2 + dr^2/(1-b(r)/r) + r^2 dOmega^2
-    shape function b(r) = b0^2/r   (Morris & Thorne 1988, eq. 12)
- '   throat at r0 = b0:  b(r0) = %.6f = r0  (check)' % fl['b_at_r0']
- "   flare-out:  b'(r0) = %.4f < 1  (the throat is a minimum of r-b)" % fl['b_prime_at_r0']
-    THIS is the condition that costs. It forces d^2r/dl^2 > 0 at the
-    throat, and the Einstein equations read that as rho < 0. Theoremed
-    for EVERY traversable wormhole (Visser 1989; Flanagan & Wald 1997)
-    -- not an artefact of this ansatz.
- '   tidal profile:  %.2e g at throat, %.2e g at 2b0, %.2e g at 4b0' % (ps['tidal_g'], ps['tidal_at_2b0_g'], ps['tidal_at_4b0_g'])
-    (falls as 1/r^4 -- the throat is the only lethal part)
- '   proper length throat -> 4b0:  %.1f m  =  %.2f b0\n' % (ps['proper_length_m'], ps['proper_length_m'] / ps['b0_m'] if _finite(ps['b0_m']) and ps['b0_m'] > 0 else float('nan'))
-  AGAINST THE ONLY REAL NEGATIVE ENERGY THERE IS:
- '   Casimir lattice aboard   %s' % fmt_energy(casimir_onboard_j())
- "   short by %.0f orders of magnitude for the gate as spec'd," % ps['casimir_shortfall_orders']
- '   short by %.0f orders for a throat wide enough to survive.' % ps['safe_shortfall_orders']
-  FORD-ROMAN QUANTUM INEQUALITIES (1997):
-    Negative energy is not just hard to source -- it is BOUNDED in
-    magnitude and duration by quantum field theory:
-      |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)   (massless scalar,
-                                               sampling time tau)
- "   At tau = 1 s:  %s /m^3  -- %.0f orders below the throat's demand" % (fmt_energy(ps['qi_bound_1s_j_m3']), ps['qi_shortfall_orders'])
- '   Longest you can hold a %.0f m throat open:  %.2e s' % (ps['b0_m'], ps['qi_hold_s'])
- '   Traversal takes:  %.1f s  --  %.0f orders of magnitude longer' % (ps['traverse_s'], math.log10(ps['qi_traversal_ratio']) if _finite(ps['qi_traversal_ratio']) and ps['qi_traversal_ratio'] > 0 else float('nan'))
-    The throat closes ~1e26 times before you are halfway through.
-    This is the deepest 'no' in the portal section: not 'we lack a
-    source' but 'the source is forbidden from lasting long enough',
-    by a theorem of quantum field theory. 
-  VISSER THIN-SHELL WORMHOLE (1989/1995):
-    Cut two copies of spacetime at radius a, paste with a thin shell.
-    The exotic matter lives on a 2-D SHEET, not a 3-D volume:
-      sigma = -c^2 / (2 pi G a) * sqrt(1 - 2GM / a c^2)
- "   For the spec'd aperture (a = %.0f m, M = 0):" % vs['a_m']
- '     shell exotic mass   %s' % fmt_mass(vs['shell_mass_kg'])
- '     shell exotic energy %s' % fmt_energy(vs['shell_energy_j'])
- '   That is MORE than the Morris-Thorne volume estimate (%s) --' % fmt_mass(ps['mass_kg'])
-    concentrating exotic matter on a sheet is LESS efficient, not
-    more. Visser's point is about LOCALISATION, not reduction: the
-    NEC violation is still there, but on a surface you could in
-    principle engineer. It vanishes as a -> 2GM/c^2 (the horizon
-    swallows it), which is why nearly-extremal holes are the route. 
-  MALDACENA-MILEKHIN-POPOV (2020): THE WORMHOLE THAT WORKS ON PAPER:
-    The closest thing to a real traversable wormhole in the literature.
-    Two nearly-extremal MAGNETICALLY CHARGED black holes, held open by
-    the Casimir energy of massless fermions threading the magnetic field
-    lines. The negative energy is genuine, calculable, from a real
-    quantum field -- not a postulate.
- '   Survivable BH mass    %.0f M_sun  (%.2e kg)' % (mmp['M_msun'], mmp['M_kg'])
- '   throat radius (r_s)   %.3g m  =  %.1f Earth diameters' % (mmp['r_s_m'], mmp['r_s_m'] / 12742000.0)
-      -- same curvature radius as the Morris-Thorne survivable throat,
-        reached from a completely different construction.
- '   extremal charge       %.3e C  (Q_ext = sqrt(4 pi eps0 G) M)' % mmp['Q_ext_c']
- '   traversal time        %.1f s  (t ~ GM/c^3 * ln(M/M_planck))' % mmp['traversal_s']
- '   Casimir energy        %.2e J  (tiny, but it tips an almost-wormhole)' % mmp['casimir_energy_j']
-    THE CATCHES:
-      1. No magnetic monopole has EVER been observed. These BHs may
-         not exist. If they do, they are primordial, and none is seen.
-      2. The holes must be NEARLY EXTREMAL (Q/Q_ext -> 1). Fine-tuned.
-      3. Only massless fermions provide the right Casimir energy.
-         This is a specific, fragile construction -- not generic. 
-  AND THEN IT IS A TIME MACHINE:
-    Two mouths at different clock rates desynchronise. When the offset
-    exceeds the light-travel time between them, closed timelike curves
-    exist (Morris, Thorne & Yurtsever 1988). This is automatic:
-    traversable wormhole + ordinary relative motion = time machine.
-      park one mouth at Phi/c^2 = -0.2 (neutron star):
- '       rate gap %.4f  ->  time machine in %s' % (g['rate_diff'], fmt_time(g['onset_s']))
-      carry one mouth on THIS warp drive:
- '       rate gap %.4f  ->  never. %s' % (w['warp_rate_diff'], w['verdict'])
-      carry it on a relativistic rocket at the same speed:
- '       rate gap %.4f  ->  it works' % w['rocket_rate_diff']
-    Note the irony: the FAST thing cannot build the causality
-    violation, and the slow thing can.
-    Hawking's chronology protection conjecture (1992) expects vacuum
-    fluctuations to destroy the throat at exactly the moment it would
-    first close. Unproven -- but it is why most physicists expect no. 
-  THE TELEPORTER THAT ACTUALLY EXISTS:
-    Quantum teleportation is real and routine (Bennett et al. 1993;
- '   %.0f km via the Micius satellite, 2017).' % q['record_km']
-    It moves a quantum STATE, not matter.
- '   It needs pre-shared entanglement and %.0f classical bits per qubit,' % QT['bits_per_qubit']
-    and that classical channel is capped at c -- so NO information
-    travels faster than light. Ever.
-    No-cloning means the original is destroyed.
- '   Teleporting one person: about %.2e bits of state.' % q['state_bits']
- '   At an absurdly generous 1 Tb/s that is %s -- about %.1f times the' % (fmt_time(q['seconds']), q['universe_ages'])
-    age of the universe. 
-  VERDICT: four constructions, one answer.
-    Morris-Thorne (1988) needs bulk negative energy; no source exists.
-    Visser (1989) concentrates it on a shell; that costs MORE, not less.
-    Ford-Roman (1997) says the source cannot last long enough even if
-      it existed -- the quantum inequalities close the throat in 1e-26 s.
-    Maldacena-Milekhin-Popov (2020) is the one that works on paper, with
-      REAL quantum-field negative energy -- but it needs magnetically
-      charged black holes, and no magnetic monopole has ever been seen.
-    And every traversable wormhole is automatically a time machine
-    (Morris, Thorne & Yurtsever 1988), which Hawking's chronology
-    protection conjecture expects to destroy. The portal is the warp
-    drive's problem again, in a new shape -- with a time machine on top.
- ' ship mass %s   cruise load %s   plant %s' % (fmt_mass(ship_mass_kg()), fmt_power(cruise_load_w(beta)), fmt_power(plant_electric_w()))
- ' destination array: %s\n' % ('ASSUMED PRESENT (rendezvous)' if dest_array else 'NONE (flyby only)')
- '\n  arrival: ship %s | Earth %s | distance %s' % (fmt_time(v.t_ship), fmt_time(v.t_earth), fmt_dist(v.x_m))
- '  a relativistic ROCKET at the same beta would have aged %s' % fmt_time(rocket_proper_time_s(beta, PROXIMA_M))
-   -- the warp crew age MORE, and arrive in step with home. That is
-      the trade: no dilation dividend, no reaction mass, no g-forces.
- '\n  %d / %d checks passed.' % (n_pass, len(results))
- '  %s' % ('ALL PHYSICS CHECKS PASS.' if n_pass == len(results) else 'SOME CHECKS FAILED -- do not trust this build.')
-  Warpdrive V1.0 -- WD-1 FOLDRUNNER :: Physical Warp Drive Digital Twin
-  to-scale, flyable, energy-honest (nothing created from nothing)
-  THE SHIP
- '   %-26s %s' % ('dry mass', fmt_mass(ship_mass_kg()))
- '   %-26s %.0f m ring / %.0f m hull / %.0f m bubble' % ('envelope', DIMS['ring_major_d_m'], DIMS['hull_len_m'], DIMS['bubble_r_m'])
- '   %-26s %.0f GW thermal -> %s electrical' % ('fusion plant', DIMS['reactor_th_gw'], fmt_power(plant_electric_w()))
- '   %-26s %.0f m^2, %.0f K limit' % ('radiators', radiator_area_m2(), DIMS['rad_limit_k'])
- '-' * 78
-  THE TWO DRIVES
-    PHYSICAL (beta < 1)   positive energy, every energy condition met.
-      Bobrick & Martire 2021 / Fuchs et al. 2024. Real matter, real
- '     solution. Costs %s to reach beta = 0.5, and this model' % fmt_energy(kinetic_energy_j(0.5))
-      charges you every joule of it.
- '   ALCUBIERRE (beta > 1)  needs %s of NEGATIVE energy.' % fmt_energy(alcubierre_energy_j(1.0, DIMS['bubble_r_m'], 1.0))
- '     Onboard Casimir lattice supplies %s -- short by %.0f orders' % (fmt_energy(casimir_onboard_j()), orders_of_magnitude(alcubierre_energy_j(1.0, DIMS['bubble_r_m'], 1.0), casimir_onboard_j()))
-      of magnitude. It flies here, flagged UNFUNDED on every frame.
- ' THE MISSION  Sol -> Proxima Centauri b, %.4f ly' % PROXIMA_LY
- '   max cruise beta %.4f -- EMERGENT from beam aperture, wavelength,' % bcap
-      tap power and ship mass. Nothing in the spec names a speed limit.
- "   crossing %s ship time, and the same on Earth's calendar." % fmt_time(crossing_time_s(bcap))
-    stopping needs an array at the far end: the magsail halves your
- '     speed in %s but takes %s to actually stop.' % (fmt_time(magsail_halving_time_s(0.5)), fmt_time(magsail_decel_time_s(0.5)))
-  CONTROLS
-    TAB  SHIP / METRIC / DILATION / PORTAL / FLIGHT
-         I  full spec      M  energy ladder      H  help
-    SHIP    drag=orbit  wheel=zoom  right-drag=pan  R=reset  L=labels
-            1=full 2=exploded 3=assembly  4/X=section  hover=spec card
-    METRIC  [ ] wall thickness   , . beta   -- watch the bill move
-    DILATION every clock in the problem, not just the flattering one
-    PORTAL  the wormhole, priced -- and the time machine it hands you
-    FLIGHT  B=shell  G=boost  K=brake  J=destination array  - + warp
-            F=unlock Alcubierre mode (superluminal, unfunded)
-    P pause    H help    ESC quit
-    -> CTCs EXIST.  Stepping through arrives in your own past.
-       Hawking's chronology protection conjecture expects the
-       throat to be destroyed at this boundary.
-    -> No CTCs yet.  Arrives in B's past relative to A, but
-       not in your own past -- no paradox possible.
- '   -> CTCs EXIST (offset exceeds light-time by %s).' % fmt_time(t4['ctc_margin_s'])
-       This IS a time machine: step through A->B and you arrive
- "      %.2e s in your own past.  But Hawking's CPC (1992)" % abs(t4['offset_s'])
-       expects vacuum fluctuations to diverge at the chronology
-       horizon and destroy the throat.  Unproven -- but it is
-       why most physicists expect the answer to be no.
- '   -> CTCs EXIST after just 1 year (offset %.0f d vs light-time' % (t7['offset_s'] / DAY)
- '      %.0f s).  Step A->B: arrive %.0f d in the past.' % (t7['light_time_s'], t7['offset_s'] / DAY)
- '      Step B->A: arrive %.0f d in the FUTURE.' % (t7['offset_s'] / DAY)
- '   chain of %3d wormholes: offset = %8.1f years' % (N, chain_off / YR)
- '   GUT string (mu=1e21 kg/m), v=0.5, D=%.0f ly: offset = %.0f yr' % (D_ly, gott / YR)
- '   extremal Kerr (a=0.99GM/c^2, 10 M_sun), %4d orbits: %.2e yr' % (n, kerr / YR)
- '     cycle %d: coord %.3f yr, offset %.2f yr, net %+.2f yr' % (row['cycle'], row['coord_in_s'] / YR, row['offset_s'] / YR, row['net_s'] / YR)
-      Gravitational drift:   n/a -- no usable boost in this config
- '     Gravitational drift:   +%.2f s over the %.2f yr crossing' % (drift, t_cross / YR)
-    (no traversal record -- input was not a result dict)
-  === HONESTY LAYER -- conservation audit ===
- '   kinetic gained     : %s' % fmt_energy(lg('kinetic'))
- '   beam delivered     : %s' % fmt_energy(lg('beam_in'))
- '   kinetic peak held  : %s' % fmt_energy(lg('kinetic_peak'))
- '   magsail recovered  : %s' % fmt_energy(lg('magsail_regen'))
- '   photon brake work  : %s  (leaves with the beam, not recovered)' % fmt_energy(lg('brake_dissipated'))
- '   plant produced     : %s  (%.3g kg D-3He burnt)' % (fmt_energy(lg('plant_out')), lg('fuel_kg'))
- '   heat radiated      : %s' % fmt_energy(lg('radiated'))
- '   crew clock vs Earth: %+.3f s over %s  (gravitational only)' % (_real(getattr(voyage, 't_ship', float('nan'))) - _real(getattr(voyage, 't_earth', float('nan'))), fmt_time(_real(getattr(voyage, 't_coord', float('nan')))))
- '   exotic energy OWED : %s   %s' % (fmt_energy(-_debt), 'UNFUNDED -- no known source' if _finite(_debt) and _debt > 0 else '(none: subluminal, positive-energy)' if _finite(_debt) else '(unknown -- ledger state unreadable)')
- '   Casimir available  : %s' % fmt_energy(casimir_onboard_j())
- '   VERDICT: %s' % ('HONEST -- nothing created from nothing.' if ok else 'MODEL BROKEN.')
- '  %-22s %-46s %10s %6.1f%%' % (name, spec, fmt_mass(m), share)
- '   %-12.4f %-12.6f %-14.4g %-16.4g' % (r, shape_f(r, R, d0), shape_df(r, R, d0), energy_density(0.0, r, 1.0, R, d0))
- '   %-14.4g %-16.4g %-22s %s' % (delta, E, fmt_mass(equiv_mass_kg(E)), tag)
- '   beta = %-6.1f  E = %-14.4g J  = %-20s  %s' % (b, E, fmt_mass(equiv_mass_kg(E)), 'EXOTIC (NEC violated)' if b >= 1.0 else 'not required -- use the positive-energy shell instead')
- '   delta = %-8.3g m -> %.3e m/s^2 = %.3e g' % (delta, a, a / 9.81)
- ' %-58s %s' % (label, status)
- '     %s\n' % cite
- '\n [%-7s] %s' % (status, name)
- ' [%-9s] %s%s' % (status, name, mass_note)
- ' max_boost_beta() = %r -- the beam configuration cannot' % beta
-  sustain any boost in this state; no crossing clocks to report.
- '   %-8.2f %-14.6f %-14.6f %.6f' % (b, lapse_static(0.0, b), lapse_static(DIMS['bubble_r_m'], b), lapse_static(DIMS['bubble_r_m'] * 1.6, b))
- '   %-22s %-18.4e %.12f' % (name, grav_potential_at(x) / C2, grav_rate(x))
- '  cannot BOOST at beta %r' % beta
- '  ' + line
- '  [%s] %-52s %s' % ('PASS' if ok else 'FAIL', label, detail)
- pygame is required for the interactive viewer.
- Install it with:  pip install pygame numpy
- The headless reports still work: --selftest --metric --ladder
-                                  --feasibility --voyage
- '   [%s]  %s' % ('PASS' if passed else 'FAIL', name)
- '     x%-10.0e  ->  %-14s (%s)' % (factor, fmt_energy(E), fmt_mass(equiv_mass_kg(E)))
- '           %s' % line
- '             %s' % line
- '--voyage requires a finite beta, got %r -- using 0.5' % beta
-      claimed positive-energy superluminal solitons;
-      shown to violate the NEC after all -- no reduction stands.
-      not a reduction of the exotic bill -- a DIFFERENT SOLUTION
-      CLASS with no exotic bill at all. Cost becomes ordinary
- '     kinetic energy: %s to reach beta = 0.5. Subluminal only.' % fmt_energy(E)

### mission `note()` / log entries (13 sites)

- t
- 'BOOST to beta %.3f -- bill %s over %s' % (core.beta_cmd, fmt_energy(bp['energy_j']), fmt_time(bp['time_s']))
- 'MAGSAIL DEPLOYED at beta %.3f' % b
- '  magsail alone: halves speed in %s, STOPS in %s' % (fmt_time(magsail_halving_time_s(b)), fmt_time(magsail_decel_time_s(b)))
- 'bubble down: %.3g swept protons released forward (%s)' % (self.ism_particles, fmt_energy(blast))
- 'SHELL LOST at superluminal beta -- apparent velocity was never momentum; ship is at rest, adrift at %s' % fmt_dist(self.x_m)
- 'PREDICTED SHORTFALL: %s' % bp['reason']
- '  destination array ASSUMED PRESENT: photon brake %.3g N -> stop in %s' % (beam_brake_force_n(0.02 * LY), fmt_time(beam_brake_time_s(b)))
-   NO destination array -- this is a FLYBY, not a rendezvous
- 'cruise beta %.4f reached; beam released' % self.beta
- 'BEAM RANGE EXHAUSTED at %s -- cruise locked to beta %.4f' % (fmt_dist(self.x_m), self.beta)
- 'ARRIVED. ship %s / Earth %s' % (fmt_time(self.t_ship), fmt_time(self.t_earth))
- 'FLYBY -- passing Proxima at beta %.3f, still %s from stopped' % (self.beta, fmt_time(magsail_decel_time_s(self.beta)))

### viewer `flash()` toasts (20 sites)

- 'wall delta = %.4g m   sigma = %.4g /m' % (w, 1.0 / w)
- HELM LOCKED -- forward wall is causally disconnected
- cruise beta is set during BOOST -- reset (N) to change
- 'TEST MODE -- demo flight: beta=%.3f, wall=%.3g m, destination array %s' % (c.beta_cmd, c.wall_m, 'PRESENT' if v.dest_array else 'ABSENT (flyby)')
- test mode off -- manual control
- 'DEMO END -- %s' % (c.collapse_msg or 'shell collapsed')
- 'DEMO COMPLETE -- %s (ship %s / Earth %s)' % ('arrived' if v.phase == 'ARRIVED' else 'flyby', fmt_time(v.t_ship), fmt_time(v.t_earth))
- DEMO END -- no beta commanded; nothing to fly
- 'DEMO END -- still braking: %s to stop on the magsail alone' % fmt_time(magsail_decel_time_s(v.beta))
- ALCUBIERRE MODE UNLOCKED -- every joule beyond beta=1 is UNFUNDED   (clock slowed to watch it)
- physical (positive-energy) mode
- 88 MPH -- FIELD TRANSITION
- 'warp shell %s' % ('FORMING' if c.bubble_cmd else 'DOWN')
- err or 'BOOST -- rectenna deployed, beam acquired'
- err or 'BRAKING'
- mission reset -- back at the tap
- 'destination array: %s' % ('ASSUMED PRESENT -- rendezvous possible' if self.voy.dest_array else 'NONE -- flyby only')
- AUTO RUN -- take it to 88
- PARKED -- run reset
- 'fault injected: %s' % (nxt or 'cleared')

### `collapse()` failure reports (1 sites)

- BUBBLE COLLAPSE -- shell shape lost

## Appendix -- the companion documents (verbatim)

`README.md`, `overview.md` and `howitworks.md` are included here in full so this single file is the complete corpus -- nothing the repository knows is outside this document.

### `README.md`

```
# Warpdrive WD-1m5 Foldrunner "Miniframe V"

A physics-honest digital twin of a warp-drive starship, a traversable wormhole portal, and the time machine that any wormhole automatically becomes. Every number is computed from the real general-relativity and quantum-field-theory formulas. Nothing is fictional. Where the physics says "impossible," the model says so and shows the computation that proves it.

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
| SPECIAL WORKS | The WD-88 Foldmobile: the entire drive folded into a 4.40 m road car that transitions at exactly 88 mph (RUN 88 / BRAKE / PARK / FAULT chips, W/S or arrows to drive, `,`/`.` speed nudge, `[`/`]` hop duration) |

All on-screen chips are clickable: the mode tabs, FULL/EXPLODED/ASSEMBLY/
SECTION/LABELS view chips, and the FLIGHT control strip (SHELL, DEST ARRAY,
ALCUBIERRE, BOOST, BRAKE, WARP -/+, RESET, TEST).

Press **I** for the full specification panel -- 39 sections including 10 math proof sections, the component-by-component breakdowns (15b/15c) that explain every part of the ship: role, spec, mass share, power draw, failure mode and buildability rating, every specification key verbatim (15d), every runtime state field plus the complete controls (15e), every public function in the model (15f), and the Foldmobile's own two sections (20b/20c: the car-scale system map and the same-road-spot ephemeris, derived live). Press **H** for controls. Press **PgUp/PgDn** to scroll.

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

The UI info panel (press `I` in the visualizer) now contains 39 sections -- 10 proof sections with 47+ individual proofs, component-by-component breakdowns (15b/15c) generated live from the mass, buildability and operations ledgers, every DIMS/PLANT/DRIVE key with its source comment (15d), the full WarpCore/Voyage runtime state, envelope check, controls and CLI (15e), the complete model function registry (15f), and the Foldmobile sections 20b/20c (the car-scale system map and the full same-road-spot ephemeris with the frame-carrying heading solve). The same data plus the barrier table, feasibility scorecard, honesty-audit checks, portal constructions, time-machine constructions, traversal tests, clock ledger, fuel economy, the mesh budget, module tables, the self-test coverage map, every hover spec-card, and the complete info-panel text verbatim (all 39 sections, all proofs) is emitted to `Infornmational.md` via `python _gen_info.py`. Each proof states the formula, the computed value, and the self-test check that verifies it. The self-test has been expanded from 95 to 417 checks, including 34 numerical-stability edge-case tests, 13 amplification-mechanism tests (chained wormholes, nested wormholes, Tipler cylinder, Gott cosmic strings, Kerr CTC, max-displacement), 23 multi-jump ledger tests (cycle time, breakeven fixed point, backward/forward recurrences, ISM scoop flux, isotope yield, sustainability, fuel-out detection), 30 hostile-input regression tests (zero/negative walls and throats, out-of-domain separations and masses, signed-|beta| superluminal guards, direction validation, rate-diff and body-size clamping), 1 cross-integrator consistency test pinning the voyage boost lock to the `boost_profile` ceiling, 8 TEST-mode demo state-machine tests, and 30+ Foldmobile checks (exact 88 mph trigger, derived mass/power/ops ledgers, live thermal balance, injected fault fidelity, hostile speed/thermal/ephemeris inputs, pole and 32,000-year solves, lane-heading carry, and hostile build-detail factors).

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

## SPECIAL WORKS -- the WD-88 FOLDMOBILE (the whole drive, car scale)

The sixth tab is the same model run at car scale: every WD-1 subsystem folded into a 4.40 m stainless gull-wing coupe that drives a real road and fires its field transition at exactly **88 mph** (39.33952 m/s). The silhouette is the homage; the engineering is the same audit discipline as the ship -- every part is derived, massed, powered and given a failure mode, and the two movie conceits are kept and *honestly labelled as props*.

### The homage contract (stated in the model, not just here)

- **88 mph is an activation threshold, not physics.** The bubble could in principle fire at a standstill; 88 is the homage, and the run-up is how you build the nerve to press it. The selftest asserts 87.9 mph held does **not** fire, and that the trigger is the real 88 mph = 39.33952 m/s -- not 88 m/s.
- **The cabin flux capacitor is FOR SHOW.** Its spec card says so: "wired to nothing heavier than an LED." So are the time-circuit display, the dash TFC switch, the console destination keypad and the folded lightning hook on the rear deck -- the hook is the film's clock-tower contact pole, and the card notes this car charges through the shore port, not a 1.21 GW lightning strike. The selftest asserts the FOR SHOW label exists.
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

Downscaling buys the R^2 in the field energy (the car's bill is ~4 orders smaller than the ship's) -- **not a way around the sign of it**. A literal 1/117 build makes a 1.57 m shell, and a 4.4 m car cannot fit inside it; the panel prints that rather than letting the homage lie.

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
| 12 | FLUX CAPACITOR | rear bulkhead | -- (prop) | 5.0 kg | 5 mW / always | LED dies -- audience notices |
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

The twin fire streaks the homage paints behind the wheels, modelled as a real part: hidden until `fired` ("physically there is nothing there yet"), swept streaks running rearward from the rear wheels onto the tarmac. Its ops row is honest: "no failure mode -- the scar cannot fail; it is the record."

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

### Foldmobile self-test coverage (~30 of the 417 checks)

- Builds finite at every detail factor; the whole car fits inside its own 2.9 m shell; four hub drives stand at the corners
- Trigger exactness: 87.9 mph held unfired, one-step crossing fires, real 39.33952 m/s
- Overspeed clamps to 130; nan speedometer recovered; negative poison healed by the drag floor
- Quenched SMES: 88 mph is just driving; heat-soaked cell derates below the trigger
- dt=0 / dt=nan produce no motion and no fire
- Thermal: idle/drive/stalled equilibria honest; equilibrium-bound under giant dt; all-nan recovery; 120 K floor under absurd cooling
- Mass budget derived to 1e-6; every part carries ops (power/duty/fail) and mass rows; bus funded with positive margin; flux capacitor labelled FOR SHOW; no gas engine anywhere
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
```

### `overview.md`

```
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
```

### `howitworks.md`

```
# How It Works -- Warpdrive WD-1u4 Foldrunner

A logical, step-by-step explanation of how the warp drive model works, from the physics to the engineering to the barriers -- and, in section 7, how the same model runs at car scale as the WD-88 Foldmobile in the SPECIAL WORKS tab. This document explains the *logic* -- for the formulas and proofs, see `README.md`. For the high-level summary and the full refit rationale, see `overview.md`. For the exhaustive component-by-component reference (every part's role, spec, mass, power draw, failure mode and buildability rating, generated live from the model's own ledgers), see `Infornmational.md`.

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

## 7. The WD-88 Foldmobile: the whole drive at car scale (SPECIAL WORKS)

The sixth tab runs the same model at car scale: every WD-1 subsystem folded into a 4.40 m stainless gull-wing coupe that drives a real road and fires its field transition at exactly 88 mph. It is a second audited machine, not a skin -- its own mass budget, power budget, operations ledger, thermal model, fault rig and ephemeris solver, held to the same rule: where the physics says impossible, the model says so and shows the number.

### Step 1: the shell is the homage, the contents are real

The body is a lofted chamfered-section coupe (wedge nose, cabin step, fastback tail) carrying a recognizable car: gull-wing seams, wire glazing (drawn as wire so it can never painter-hide the cabin), fascias, headlamp doors, taillight bar, grille, badge, mirrors, handles, the OUTATIME plate, wipers, sail louvers, air dam, diffuser strakes, sill plates, door struts, cowl vents, plate lamp, side repeaters. The cabin is furnished: seats + headrests, dash + binnacle + gauge faces, console + drive selector + radio/HVAC stack, steering wheel + column (canted 25 deg to the driver), pedals, parking brake, three-point belts, visors, dome light, glovebox, door pulls, a fire extinguisher -- and a drawn driver, because the mass budget books crew mass and honesty means drawing it.

### Step 2: where the ship's systems went

hull -> stainless monocoque | ring + 96 coils -> beltline field conduit run (the glowing bands ARE the coils, bolted on six standoffs, terminating at two rear-deck field-driver boxes -- the film's capacitor boxes, here real HTS current-lead packs) | cap rings -> elliptical nose/tail shaping hoops (scaled in x to actually wrap the body sections) | reactor -> 150 kg D-3He microtorus in the trunk, with a decklid service cap and an He-3 filler neck | SMES -> a puck under the hood, charged through a shore-power socket on the left flank | Penning traps -> two bottles under the floor pan | Casimir lattice -> 12 strips lining the conduit run (-56.2 J, honestly 42 orders short of the -1.29e44 J shell bill) | radiators -> the rear-deck louver bank (the car-scale radiator, on the same hot=True channel the ship's fins use -- it visibly reddens under load) | cryoplant -> an underbody helium circulator with two cold lines | rectenna -> a roof whip on a real base | deflector -> a nose strip | RCS -> two aft-facing bells at the tail | magsail -> a KE-recovery loop stowed under the tail, returning the ship's own regen fraction of the run's kinetic energy to the SMES | navigator -> the dash ephemeris unit.

**No gasoline engine of any kind** -- the selftest scans every part name for it. The flux capacitor, time circuits, TFC switch, keypad and folded lightning hook are labelled props; everything that actually moves spacetime is under the hood, the trunk, the floor and the beltline.

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

Downscaling buys the R^2 in the field energy -- the car's exotic bill (-1.29e44 J) is ~4 orders smaller than the ship's -- **not a way around the sign of it**: the 12 Casimir strips' -56.2 J are still 42 orders short. The honesty machinery is identical: derived mass to 1e-6, funded bus, live ops ledger, FOR SHOW labels enforced by selftest, and ~30 dedicated checks covering trigger exactness, thermal equilibria, fault fidelity, ephemeris extremes (poles, +/-32,000-year epochs, 60 s and 10-year hops) and hostile inputs everywhere.

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
```

## Specification units (inferred per key)

The unit every spec key carries, inferred from its suffix -- the dimensional grammar of DIMS.

| Key | Value | Unit |
|-----|-------|------|
| `bubble_r_m` | 183.44 | m |
| `wall_thick_m` | 0.2 | m |
| `interior_margin` | 6 | count / dimensionless |
| `ring_major_d_m` | 366.88 | m |
| `ring_minor_d_m` | 27.52 | m |
| `ring_wall_m` | 1.08 | m |
| `ring_sectors` | 96 | count / dimensionless |
| `ring_density` | 4100 | kg/m^3 |
| `coils` | 96 | count / dimensionless |
| `coil_bore_m` | 27.92 | m |
| `coil_len_m` | 17.24 | m |
| `coil_turns` | 48000 | count / dimensionless |
| `coil_current_a` | 38000 | count / dimensionless |
| `coil_temp_k` | 18 | K |
| `coil_build_m` | 0.3 | m |
| `coil_standoff_m` | 0.2 | m |
| `coil_density` | 5600 | kg/m^3 |
| `capring_d_m` | 176.08 | m |
| `capring_minor_d_m` | 12.84 | m |
| `cap_offset_m` | 69.72 | m |
| `capring_wall_frac` | 0.3 | fraction (0..1) |
| `hull_len_m` | 124.76 | m |
| `hull_d_m` | 32 | m |
| `hull_decks` | 12 | count / dimensionless |
| `hull_wall_m` | 0.44 | m |
| `hull_shell_rfrac` | 0.88 | fraction (0..1) |
| `hull_density` | 2700 | kg/m^3 |
| `deck_t_m` | 1.4 | m |
| `deck_inset_m` | 1.2 | m |
| `crew` | 24 | count / dimensionless |
| `crew_supplies_kg` | 3200 | kg |
| `len_margin_m` | 20 | m |
| `pylons` | 12 | count / dimensionless |
| `pylon_len_m` | 154.08 | m |
| `pylon_w_m` | 5.88 | m |
| `pylon_t_m` | 4.8 | m |
| `pylon_rho` | 2700 | kg/m^3 |
| `reactor_major_d_m` | 21.24 | m |
| `reactor_minor_d_m` | 6.36 | m |
| `reactor_wall_m` | 3.6 | m |
| `reactor_rho` | 5200 | kg/m^3 |
| `reactor_th_gw` | 102.7 | GW |
| `reactor_direct_eff` | 0.62 | fraction (0..1) |
| `amtraps` | 8 | count / dimensionless |
| `amtrap_d_m` | 9.56 | m |
| `amtrap_wall_m` | 1.2 | m |
| `amtrap_rho` | 4400 | kg/m^3 |
| `amtrap_kg` | 5.248 | kg |
| `smes_major_d_m` | 40.36 | m |
| `smes_minor_d_m` | 4.4 | m |
| `smes_wall_m` | 1 | m |
| `smes_rho` | 6800 | kg/m^3 |
| `smes_b_t` | 60 | T |
| `smes_z0_m` | 40.36 | m |
| `casimir_cassettes` | 96 | count / dimensionless |
| `casimir_plate_m` | 1.1 | m |
| `casimir_gap_nm` | 10 | nm |
| `casimir_pitch_nm` | 60 | nm |
| `casimir_stack_m` | 3.68 | m |
| `casimir_rho` | 2300 | kg/m^3 |
| `radiators` | 60 | count / dimensionless |
| `rad_len_m` | 90.44 | m |
| `rad_w_m` | 31.32 | m |
| `rad_inner_r_m` | 69.56 | m |
| `rad_z0_m` | -24.36 | m |
| `rad_temp_k` | 1550 | K |
| `rad_limit_k` | 1900 | K |
| `rad_emissivity` | 0.92 | count / dimensionless |
| `rad_t_m` | 0.24 | m |
| `rad_rho` | 1900 | kg/m^3 |
| `cryo_units` | 16 | count / dimensionless |
| `cryo_d_m` | 11 | m |
| `cryo_len_m` | 20.16 | m |
| `cryo_rho` | 240 | kg/m^3 |
| `cryo_mount_rfrac` | 0.8 | fraction (0..1) |
| `deflector_d_m` | 33 | m |
| `deflector_depth_m` | 8.28 | m |
| `deflector_t_m` | 0.4 | m |
| `deflector_rho` | 3100 | kg/m^3 |
| `rcs_pods` | 32 | count / dimensionless |
| `rcs_d_m` | 4.76 | m |
| `rcs_len_m` | 9.2 | m |
| `rcs_rho` | 900 | kg/m^3 |
| `collector_d_m` | 84.4 | m |
| `collector_depth_m` | 16.52 | m |
| `collector_deploy_km` | 4 | km |
| `collector_film_um` | 1 | um |
| `collector_film_rho` | 1400 | kg/m^3 |
| `collector_z0_m` | 73.36 | m |
| `portal_gate_d_m` | 24 | m |
| `portal_ring_minor_d_m` | 3 | m |
| `portal_coils` | 16 | count / dimensionless |
| `portal_casimir_rings` | 8 | count / dimensionless |
| `portal_frame_d_m` | 34 | m |
| `magsail_r_km` | 2800 | km |
| `magsail_current_a` | 4.4e+06 | count / dimensionless |
| `magsail_mass_kg` | 1.28e+07 | kg |
| `magsail_cd` | 0.85 | count / dimensionless |
| `magsail_regen_eff` | 0.62 | fraction (0..1) |
| `magsail_view_scale` | 0.00025 | count / dimensionless |
| `hotel_mw` | 96 | MW |
| `coil_ac_mw` | 38252.8 | MW |
| `cryo_mw` | 2492.8 | MW |
| `control_mw` | 7064 | MW |
| `conversion_eff` | 0.62 | fraction (0..1) |
| `recovery_eff` | 0.92 | fraction (0..1) |
| `am_energy_j_kg` | 1.7975e+17 | kg |
| `d3he_j_kg` | 3.52e+14 | kg |
| `tap_w` | 6.4e+18 | W |
| `beam_aperture_km` | 1000 | km |
| `beam_lambda_um` | 1 | um |
| `beam_range_ly` | 0.62 | ly |
| `beta_sub_max` | 0.99 | count / dimensionless |
| `beta_ftl_max` | 10 | count / dimensionless |
| `spinup_s` | 42 | s |
| `bubble_form_s` | 18 | s |
| `integrity_min` | 0.35 | count / dimensionless |
| `wall_min_m` | 1e-15 | m |
| `wall_max_m` | 12 | m |
| `arrival_beta` | 0.001 | count / dimensionless |

## Function -> specification dependency map

Which DIMS / PLANT / DRIVE keys each public function reads, extracted from the AST -- the wiring diagram of the spec.

- `flat_interior_r` reads: `DIMS.bubble_r_m`, `DIMS.interior_margin`, `DIMS.wall_thick_m`
- `_coil_count` reads: `DIMS.coils`
- `shape_f` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `shape_df` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `shape_df_shifted` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `york_theta` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `energy_density` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `warp_energy_integral` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `alcubierre_energy_j` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `wall_tidal_gradient` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `casimir_cassette` reads: `DIMS.casimir_gap_nm`, `DIMS.casimir_pitch_nm`, `DIMS.casimir_plate_m`, `DIMS.casimir_stack_m`
- `casimir_onboard_j` reads: `DIMS.casimir_cassettes`
- `barrier_analysis` reads: `DIMS.bubble_r_m`, `DIMS.rad_emissivity`, `DIMS.rad_limit_k`, `DIMS.wall_thick_m`
- `smes_store_j` reads: `DIMS.smes_b_t`, `DIMS.smes_major_d_m`, `DIMS.smes_minor_d_m`
- `plant_electric_w` reads: `DIMS.reactor_direct_eff`, `DIMS.reactor_th_gw`
- `waste_heat_w` reads: `PLANT.conversion_eff`
- `radiator_area_m2` reads: `DIMS.rad_len_m`, `DIMS.rad_w_m`, `DIMS.radiators`
- `radiator_temp_k` reads: `DIMS.rad_emissivity`
- `radiator_required_m2` reads: `DIMS.rad_emissivity`, `DIMS.rad_temp_k`
- `fusion_fuel_kg` reads: `PLANT.conversion_eff`, `PLANT.d3he_j_kg`
- `beam_spot_m` reads: `PLANT.beam_aperture_km`, `PLANT.beam_lambda_um`
- `beam_capture_frac` reads: `DIMS.collector_deploy_km`
- `beam_power_w` reads: `PLANT.tap_w`
- `boost_profile` reads: `PLANT.beam_range_ly`
- `max_boost_beta` reads: `DIMS.collector_deploy_km`, `PLANT.beam_aperture_km`, `PLANT.beam_lambda_um`, `PLANT.beam_range_ly`, `PLANT.tap_w`
- `magsail_area_m2` reads: `DIMS.magsail_r_km`
- `magsail_drag_n` reads: `DIMS.magsail_cd`
- `magsail_halving_time_s` reads: `DIMS.magsail_cd`
- `magsail_decel_time_s` reads: `DIMS.magsail_cd`, `DRIVE.arrival_beta`
- `ism_particles_swept` reads: `DIMS.bubble_r_m`
- `lapse_static` reads: `DIMS.bubble_r_m`, `DIMS.wall_thick_m`
- `ship_self_dilation` reads: `DIMS.bubble_r_m`
- `clock_ledger` reads: `DIMS.bubble_r_m`
- `visser_summary` reads: `DIMS.portal_gate_d_m`
- `portal_summary` reads: `DIMS.portal_gate_d_m`
- `report_portal_test` reads: `DIMS.portal_gate_d_m`
- `_build_ship_parts_impl` reads: `DIMS.rad_temp_k`, `PLANT.am_energy_j_kg`, `PLANT.beam_aperture_km`, `PLANT.beam_lambda_um`, `PLANT.beam_range_ly`, `PLANT.coil_ac_mw`, `PLANT.cryo_mw`
- `car_casimir_j` reads: `DIMS.casimir_gap_nm`, `DIMS.casimir_pitch_nm`
- `car_mass_budget` reads: `DIMS.casimir_rho`
- `_build_special_parts_impl` reads: `DIMS.bubble_r_m`, `DIMS.casimir_gap_nm`, `DIMS.magsail_r_km`, `DIMS.magsail_regen_eff`
- `honesty_audit` reads: `DIMS.magsail_regen_eff`, `DRIVE.arrival_beta`, `PLANT.conversion_eff`, `PLANT.d3he_j_kg`
- `report_spec` reads: `PLANT.beam_aperture_km`, `PLANT.beam_range_ly`, `PLANT.tap_w`
- `report_metric` reads: `DIMS.bubble_r_m`, `DIMS.casimir_cassettes`, `DIMS.casimir_gap_nm`, `DIMS.wall_thick_m`
- `report_ladder` reads: `DIMS.bubble_r_m`
- `buildability_ledger` reads: `DIMS.magsail_r_km`, `PLANT.am_energy_j_kg`, `PLANT.beam_aperture_km`, `PLANT.beam_range_ly`, `PLANT.coil_ac_mw`, `PLANT.cryo_mw`, `PLANT.hotel_mw`, `PLANT.tap_w`
- `operations_ledger` reads: `PLANT.am_energy_j_kg`, `PLANT.coil_ac_mw`, `PLANT.control_mw`, `PLANT.cryo_mw`, `PLANT.hotel_mw`
- `feasibility_scorecard` reads: `DIMS.bubble_r_m`, `DIMS.rad_limit_k`, `DIMS.reactor_th_gw`, `DIMS.wall_thick_m`, `PLANT.tap_w`
- `report_feasibility` reads: `DIMS.bubble_r_m`
- `report_dilation` reads: `DIMS.bubble_r_m`
- `report_portal` reads: `DIMS.portal_gate_d_m`
- `selftest` reads: `DIMS.bubble_r_m`, `DIMS.casimir_pitch_nm`, `DIMS.coil_bore_m`, `DIMS.coil_build_m`, `DIMS.coil_temp_k`, `DIMS.coil_turns`, `DIMS.coils`, `DIMS.collector_deploy_km`, `DIMS.crew`, `DIMS.hull_decks`, `DIMS.hull_density`, `DIMS.hull_len_m`, `DIMS.magsail_cd`, `DIMS.magsail_r_km`, `DIMS.portal_coils`, `DIMS.rad_emissivity`, `DIMS.rad_limit_k`, `DIMS.rad_temp_k`, `DIMS.radiators`, `DIMS.ring_major_d_m`, `DIMS.ring_sectors`, `DIMS.wall_thick_m`, `PLANT.beam_aperture_km`, `PLANT.beam_lambda_um`, `PLANT.conversion_eff`, `PLANT.d3he_j_kg`, `PLANT.tap_w`
- `_component_info_sections` reads: `DIMS.amtrap_d_m`, `DIMS.amtrap_kg`, `DIMS.amtraps`, `DIMS.bubble_r_m`, `DIMS.cap_offset_m`, `DIMS.capring_d_m`, `DIMS.capring_minor_d_m`, `DIMS.casimir_plate_m`, `DIMS.casimir_stack_m`, `DIMS.coil_bore_m`, `DIMS.coil_build_m`, `DIMS.coil_len_m`, `DIMS.coil_standoff_m`, `DIMS.coil_temp_k`, `DIMS.collector_deploy_km`, `DIMS.collector_film_um`, `DIMS.collector_z0_m`, `DIMS.crew`, `DIMS.crew_supplies_kg`, `DIMS.cryo_d_m`, `DIMS.cryo_len_m`, `DIMS.cryo_mount_rfrac`, `DIMS.deck_inset_m`, `DIMS.deck_t_m`, `DIMS.deflector_d_m`, `DIMS.deflector_depth_m`, `DIMS.deflector_t_m`, `DIMS.hull_d_m`, `DIMS.hull_len_m`, `DIMS.magsail_r_km`, `DIMS.magsail_regen_eff`, `DIMS.pylon_len_m`, `DIMS.pylon_t_m`, `DIMS.pylon_w_m`, `DIMS.rad_inner_r_m`, `DIMS.rad_len_m`, `DIMS.rad_limit_k`, `DIMS.rad_t_m`, `DIMS.rad_temp_k`, `DIMS.rad_w_m`, `DIMS.rad_z0_m`, `DIMS.rcs_d_m`, `DIMS.rcs_len_m`, `DIMS.reactor_major_d_m`, `DIMS.reactor_minor_d_m`, `DIMS.ring_major_d_m`, `DIMS.ring_minor_d_m`, `DIMS.ring_sectors`, `DIMS.smes_major_d_m`, `DIMS.smes_minor_d_m`, `DIMS.smes_z0_m`, `DIMS.wall_thick_m`, `PLANT.am_energy_j_kg`, `PLANT.cryo_mw`, `PLANT.hotel_mw`
- `_runtime_state_lines` reads: `DRIVE.bubble_form_s`, `DRIVE.integrity_min`
- `_info_sections` reads: `DIMS.amtrap_kg`, `DIMS.amtraps`, `DIMS.bubble_r_m`, `DIMS.casimir_cassettes`, `DIMS.casimir_gap_nm`, `DIMS.collector_deploy_km`, `DIMS.hull_len_m`, `DIMS.magsail_cd`, `DIMS.magsail_r_km`, `DIMS.portal_gate_d_m`, `DIMS.rad_len_m`, `DIMS.rad_limit_k`, `DIMS.rad_w_m`, `DIMS.radiators`, `DIMS.reactor_direct_eff`, `DIMS.reactor_th_gw`, `DIMS.ring_density`, `DIMS.ring_major_d_m`, `DIMS.ring_minor_d_m`, `DIMS.ring_sectors`, `DIMS.ring_wall_m`, `DIMS.wall_thick_m`, `PLANT.am_energy_j_kg`, `PLANT.beam_aperture_km`, `PLANT.beam_lambda_um`, `PLANT.beam_range_ly`, `PLANT.tap_w`
- `print_startup_banner` reads: `DIMS.bubble_r_m`, `DIMS.hull_len_m`, `DIMS.rad_limit_k`, `DIMS.reactor_th_gw`, `DIMS.ring_major_d_m`
- `main` reads: `DRIVE.beta_sub_max`

## Specification -> consumer map (what each key feeds)

The inverse wiring: change a key, and these functions recompute. Extracted from the same AST scan.

| Spec key | Read by |
|----------|---------|
| `DIMS.amtrap_d_m` | `_component_info_sections` |
| `DIMS.amtrap_kg` | `_component_info_sections`, `_info_sections` |
| `DIMS.amtraps` | `_component_info_sections`, `_info_sections` |
| `DIMS.bubble_r_m` | `_build_special_parts_impl`, `_component_info_sections`, `_info_sections`, `alcubierre_energy_j`, `barrier_analysis`, `clock_ledger`, `energy_density`, `feasibility_scorecard`, `flat_interior_r`, `ism_particles_swept`, `lapse_static`, `print_startup_banner`, `report_dilation`, `report_feasibility`, `report_ladder`, `report_metric`, `selftest`, `shape_df`, `shape_df_shifted`, `shape_f`, `ship_self_dilation`, `wall_tidal_gradient`, `warp_energy_integral`, `york_theta` |
| `DIMS.cap_offset_m` | `_component_info_sections` |
| `DIMS.capring_d_m` | `_component_info_sections` |
| `DIMS.capring_minor_d_m` | `_component_info_sections` |
| `DIMS.casimir_cassettes` | `_info_sections`, `casimir_onboard_j`, `report_metric` |
| `DIMS.casimir_gap_nm` | `_build_special_parts_impl`, `_info_sections`, `car_casimir_j`, `casimir_cassette`, `report_metric` |
| `DIMS.casimir_pitch_nm` | `car_casimir_j`, `casimir_cassette`, `selftest` |
| `DIMS.casimir_plate_m` | `_component_info_sections`, `casimir_cassette` |
| `DIMS.casimir_rho` | `car_mass_budget` |
| `DIMS.casimir_stack_m` | `_component_info_sections`, `casimir_cassette` |
| `DIMS.coil_bore_m` | `_component_info_sections`, `selftest` |
| `DIMS.coil_build_m` | `_component_info_sections`, `selftest` |
| `DIMS.coil_len_m` | `_component_info_sections` |
| `DIMS.coil_standoff_m` | `_component_info_sections` |
| `DIMS.coil_temp_k` | `_component_info_sections`, `selftest` |
| `DIMS.coil_turns` | `selftest` |
| `DIMS.coils` | `_coil_count`, `selftest` |
| `DIMS.collector_deploy_km` | `_component_info_sections`, `_info_sections`, `beam_capture_frac`, `max_boost_beta`, `selftest` |
| `DIMS.collector_film_um` | `_component_info_sections` |
| `DIMS.collector_z0_m` | `_component_info_sections` |
| `DIMS.crew` | `_component_info_sections`, `selftest` |
| `DIMS.crew_supplies_kg` | `_component_info_sections` |
| `DIMS.cryo_d_m` | `_component_info_sections` |
| `DIMS.cryo_len_m` | `_component_info_sections` |
| `DIMS.cryo_mount_rfrac` | `_component_info_sections` |
| `DIMS.deck_inset_m` | `_component_info_sections` |
| `DIMS.deck_t_m` | `_component_info_sections` |
| `DIMS.deflector_d_m` | `_component_info_sections` |
| `DIMS.deflector_depth_m` | `_component_info_sections` |
| `DIMS.deflector_t_m` | `_component_info_sections` |
| `DIMS.hull_d_m` | `_component_info_sections` |
| `DIMS.hull_decks` | `selftest` |
| `DIMS.hull_density` | `selftest` |
| `DIMS.hull_len_m` | `_component_info_sections`, `_info_sections`, `print_startup_banner`, `selftest` |
| `DIMS.interior_margin` | `flat_interior_r` |
| `DIMS.magsail_cd` | `_info_sections`, `magsail_decel_time_s`, `magsail_drag_n`, `magsail_halving_time_s`, `selftest` |
| `DIMS.magsail_r_km` | `_build_special_parts_impl`, `_component_info_sections`, `_info_sections`, `buildability_ledger`, `magsail_area_m2`, `selftest` |
| `DIMS.magsail_regen_eff` | `_build_special_parts_impl`, `_component_info_sections`, `honesty_audit` |
| `DIMS.portal_coils` | `selftest` |
| `DIMS.portal_gate_d_m` | `_info_sections`, `portal_summary`, `report_portal`, `report_portal_test`, `visser_summary` |
| `DIMS.pylon_len_m` | `_component_info_sections` |
| `DIMS.pylon_t_m` | `_component_info_sections` |
| `DIMS.pylon_w_m` | `_component_info_sections` |
| `DIMS.rad_emissivity` | `barrier_analysis`, `radiator_required_m2`, `radiator_temp_k`, `selftest` |
| `DIMS.rad_inner_r_m` | `_component_info_sections` |
| `DIMS.rad_len_m` | `_component_info_sections`, `_info_sections`, `radiator_area_m2` |
| `DIMS.rad_limit_k` | `_component_info_sections`, `_info_sections`, `barrier_analysis`, `feasibility_scorecard`, `print_startup_banner`, `selftest` |
| `DIMS.rad_t_m` | `_component_info_sections` |
| `DIMS.rad_temp_k` | `_build_ship_parts_impl`, `_component_info_sections`, `radiator_required_m2`, `selftest` |
| `DIMS.rad_w_m` | `_component_info_sections`, `_info_sections`, `radiator_area_m2` |
| `DIMS.rad_z0_m` | `_component_info_sections` |
| `DIMS.radiators` | `_info_sections`, `radiator_area_m2`, `selftest` |
| `DIMS.rcs_d_m` | `_component_info_sections` |
| `DIMS.rcs_len_m` | `_component_info_sections` |
| `DIMS.reactor_direct_eff` | `_info_sections`, `plant_electric_w` |
| `DIMS.reactor_major_d_m` | `_component_info_sections` |
| `DIMS.reactor_minor_d_m` | `_component_info_sections` |
| `DIMS.reactor_th_gw` | `_info_sections`, `feasibility_scorecard`, `plant_electric_w`, `print_startup_banner` |
| `DIMS.ring_density` | `_info_sections` |
| `DIMS.ring_major_d_m` | `_component_info_sections`, `_info_sections`, `print_startup_banner`, `selftest` |
| `DIMS.ring_minor_d_m` | `_component_info_sections`, `_info_sections` |
| `DIMS.ring_sectors` | `_component_info_sections`, `_info_sections`, `selftest` |
| `DIMS.ring_wall_m` | `_info_sections` |
| `DIMS.smes_b_t` | `smes_store_j` |
| `DIMS.smes_major_d_m` | `_component_info_sections`, `smes_store_j` |
| `DIMS.smes_minor_d_m` | `_component_info_sections`, `smes_store_j` |
| `DIMS.smes_z0_m` | `_component_info_sections` |
| `DIMS.wall_thick_m` | `_component_info_sections`, `_info_sections`, `alcubierre_energy_j`, `barrier_analysis`, `energy_density`, `feasibility_scorecard`, `flat_interior_r`, `lapse_static`, `report_metric`, `selftest`, `shape_df`, `shape_df_shifted`, `shape_f`, `wall_tidal_gradient`, `warp_energy_integral`, `york_theta` |
| `DRIVE.arrival_beta` | `honesty_audit`, `magsail_decel_time_s` |
| `DRIVE.beta_sub_max` | `main` |
| `DRIVE.bubble_form_s` | `_runtime_state_lines` |
| `DRIVE.integrity_min` | `_runtime_state_lines` |
| `PLANT.am_energy_j_kg` | `_build_ship_parts_impl`, `_component_info_sections`, `_info_sections`, `buildability_ledger`, `operations_ledger` |
| `PLANT.beam_aperture_km` | `_build_ship_parts_impl`, `_info_sections`, `beam_spot_m`, `buildability_ledger`, `max_boost_beta`, `report_spec`, `selftest` |
| `PLANT.beam_lambda_um` | `_build_ship_parts_impl`, `_info_sections`, `beam_spot_m`, `max_boost_beta`, `selftest` |
| `PLANT.beam_range_ly` | `_build_ship_parts_impl`, `_info_sections`, `boost_profile`, `buildability_ledger`, `max_boost_beta`, `report_spec` |
| `PLANT.coil_ac_mw` | `_build_ship_parts_impl`, `buildability_ledger`, `operations_ledger` |
| `PLANT.control_mw` | `operations_ledger` |
| `PLANT.conversion_eff` | `fusion_fuel_kg`, `honesty_audit`, `selftest`, `waste_heat_w` |
| `PLANT.cryo_mw` | `_build_ship_parts_impl`, `_component_info_sections`, `buildability_ledger`, `operations_ledger` |
| `PLANT.d3he_j_kg` | `fusion_fuel_kg`, `honesty_audit`, `selftest` |
| `PLANT.hotel_mw` | `_component_info_sections`, `buildability_ledger`, `operations_ledger` |
| `PLANT.tap_w` | `_info_sections`, `beam_power_w`, `buildability_ledger`, `feasibility_scorecard`, `max_boost_beta`, `report_spec`, `selftest` |

## Sensitivity analysis (how outputs move)

Live perturbations -- what actually bends the design:

### Emergent cruise beta vs ship mass

| mass | beta_max |
|------|----------|
| x0.50 (5.407e+05 t) | 0.9243 |
| x0.80 (8.651e+05 t) | 0.8799 |
| x1.00 (1.081e+06 t) | 0.8547 |
| x1.25 (1.352e+06 t) | 0.8268 |
| x2.00 (2.163e+06 t) | 0.7620 |

### Emergent cruise beta vs tap power (live PLANT mutation)

| tap_w | beta_max |
|---------|----------|
| x0.25 (1.6e+03 PW) | 0.6576 |
| x0.50 (3.2e+03 PW) | 0.7620 |
| x1.00 (6.4e+03 PW) | 0.8547 |
| x2.00 (1.28e+04 PW) | 0.9243 |
| x4.00 (2.56e+04 PW) | 0.9671 |

### Radiator equilibrium vs waste heat (T ~ P^1/4)

| waste heat | panel T | verdict |
|------------|---------|---------|
| x0.5 (38 GW) | 1210 K | OK |
| x1.0 (75.9 GW) | 1439 K | OK |
| x2.0 (152 GW) | 1711 K | OK |
| x4.0 (304 GW) | 2034 K | OVER LIMIT |

## Numerical methods (how the integrators compute)

| Computation | Method | Parameters |
|-------------|--------|------------|
| `warp_energy_integral` | composite Simpson over the wall | samples=4000 |
| `Voyage.update` | real dt sliced into `_step` substeps | fixed-dt Euler |
| `WarpCore._thermal` | exponential relaxation of `rad_k` | tau = 90 s |
| `bubble_on` convergence | shape formation ramp | 18 s (`bubble_form_s`) |
| `_integrity` drain | linear in shell stress | full loss in 2000 s at unit stress (`SHELL_STRESS_TAU`)
| `max_boost_beta` | bisection on delivered-vs-needed | lo=0.02 hi=0.99 |
| mesh tessellation | seg counts x `VISUAL_DETAIL` | 1.05 |
| hostile inputs | `_real`/`_finite` coercion at every boundary | nan/inf propagate, never crash |

## Computed reference tables (the functions swept over their domains)

Actual model outputs across the operating ranges -- a calibration card for the whole twin.

### The shape function f(r) and its derivative

| r/R | f(r) | df/dr (1/m) | theta at x=r (1/s, beta=1) |
|-----|------|-------------|---------------------------|
| 0.00 | 1.0000 | 0 | 0 |
| 0.50 | 1.0000 | 0 | 0 |
| 0.80 | 1.0000 | -4.635e-159 | -1.39e-150 |
| 0.95 | 1.0000 | -1.467e-39 | -4.399e-31 |
| 1.00 | 0.5000 | -2.5 | -7.495e+08 |
| 1.05 | 0.0000 | -1.467e-39 | -4.399e-31 |
| 1.20 | 0.0000 | -4.635e-159 | -1.39e-150 |
| 1.50 | 0.0000 | 0 | 0 |
| 2.00 | 0.0000 | 0 | 0 |

### Exotic bill vs beta and wall thickness

| wall (m) | E(beta=0.5) | E(beta=1) | E(beta=10) |
|----------|-------------|-----------|------------|
| 0.2 | -1.414e+47 J | -5.656e+47 J | -5.656e+49 J |
| 1 | -2.828e+46 J | -1.131e+47 J | -1.131e+49 J |
| 1e-09 | -2.828e+55 J | -1.131e+56 J | -1.131e+58 J |
| 1.62e-33 | -1.750e+79 J | -6.999e+79 J | -6.999e+81 J |

### Thermal equilibrium vs cruise beta

| beta | electric load | waste heat | panel T | verdict |
|------|---------------|------------|---------|---------|
| 0.250 | 7.81 GW | 12.6 GW | 918 K | OK |
| 0.500 | 16.4 GW | 26.4 GW | 1105 K | OK |
| 0.855 | 36.8 GW | 59.4 GW | 1353 K | OK |
| 0.990 | 47.1 GW | 75.9 GW | 1439 K | OK |
| 1.500 | 95.7 GW | 154 GW | 1718 K | OK |
| 2.000 | 163 GW | 262 GW | 1961 K | OVER LIMIT |

### Beam capture vs range

| range (ly) | spot (km) | capture | delivered |
|------------|-----------|---------|-----------|
| 0.0200 | 0.46 | 1.000 | 6.4e+03 PW |
| 0.0500 | 1.15 | 1.000 | 6.4e+03 PW |
| 0.1000 | 2.31 | 1.000 | 6.4e+03 PW |
| 0.2500 | 5.77 | 0.480 | 3.07e+03 PW |
| 0.5000 | 11.54 | 0.120 | 769 PW |
| 0.6200 | 14.31 | 0.078 | 500 PW |
| 1.0000 | 23.08 | 0.030 | 192 PW |
| 2.0000 | 46.17 | 0.008 | 48 PW |
| 4.2465 | 98.03 | 0.002 | 10.7 PW |

### Kinetic bill and stopping vs beta

| beta | KE | magsail halving | photon brake (0.02 ly) |
|------|----|-----------------|----------------------|
| 0.100 | 490 ZJ | 326.42 yr | 8.8 d |
| 0.250 | 3.19 YJ | 130.57 yr | 22.7 d |
| 0.500 | 15 YJ | 65.28 yr | 50.7 d |
| 0.750 | 49.7 YJ | 43.52 yr | 99.6 d |
| 0.855 | 90.2 YJ | 38.18 yr | 144.9 d |
| 0.900 | 126 YJ | 36.27 yr | 181.5 d |
| 0.990 | 592 YJ | 32.97 yr | 1.69 yr |

### Morris-Thorne throat vs aperture

| b0 (m) | exotic bill | tidal at throat | traversal |
|--------|-------------|-----------------|-----------|
| 1 | -2.017e+43 J | 1.83e+16 g | 0.4 s |
| 6 | -1.210e+44 J | 5.09e+14 g | 2.4 s |
| 12 | -2.421e+44 J | 1.27e+14 g | 4.8 s |
| 50 | -1.009e+45 J | 7.33e+12 g | 20.0 s |
| 1e+03 | -2.017e+46 J | 1.83e+10 g | 6.7 min |
| 1e+06 | -2.017e+49 J | 1.83e+04 g | 4.6 d |
| 9.57e+07 | -1.931e+51 J | 2 g | 1.21 yr |

### Gravitational drift vs cruise beta

| beta | ship crossing | drift vs Earth |
|------|---------------|----------------|
| 0.2500 | 16.99 yr | +5.291 s |
| 0.5000 | 8.49 yr | +2.646 s |
| 0.7500 | 5.66 yr | +1.764 s |
| 0.8547 | 4.97 yr | +1.548 s |

## One tick, traced (a worked example)

A real `WarpCore.update(1.0)` at cruise with the shell raised: every field before and after one ship-second.

| Field | before | after 1 s |
|-------|--------|-----------|
| `beta` | 0 | 0 |
| `bubble_on` | 0.967597 | 0.969397 |
| `integrity` | 1 | 1 |
| `load_w` | 3.95582e+09 | 3.95836e+09 |
| `waste_w` | 6.38036e+09 | 6.38446e+09 |
| `beam_w` | 0 | 0 |
| `smes_j` | 2.76159e+12 | 2.76159e+12 |
| `rad_k` | 519.461 | 522.296 |
| `exotic_need_j` | 0 | 0 |
| `exotic_debt_j` | 0 | 0 |
| `status` | NOMINAL | NOMINAL |
| `collapsed` | 0 | 0 |

Cumulative ledger after that second:

| Ledger key | Value |
|------------|-------|
| `am_kg` | 0 |
| `beam_in` | 0 |
| `brake_dissipated` | 0 |
| `fuel_kg` | 0.0010118 |
| `ism_particles` | 0 |
| `kinetic` | 0 |
| `kinetic_peak` | 0 |
| `magsail_regen` | 0 |
| `plant_out` | 2.20815e+11 |
| `radiated` | 3.80366e+10 |

## The wall-thickness trade (swept live)

Thicker wall: cheaper exotic bill, smaller flat interior, same tidal catastrophe. Swept across the DRIVE envelope (`wall_min_m`..`wall_max_m`).

| wall (m) | flat interior | ship fits | E(beta=1) | tidal 2m |
|----------|---------------|-----------|-----------|----------|
| 1e-15 | 183.44 m | yes | -1.131e+62 J | 7.04e+45 g |
| 1e-09 | 183.44 m | yes | -1.131e+56 J | 7.04e+33 g |
| 0.001 | 183.43 m | yes | -1.131e+50 J | 7.04e+21 g |
| 0.05 | 183.14 m | yes | -2.263e+48 J | 2.82e+18 g |
| 0.2 | 182.24 m | yes | -5.656e+47 J | 1.76e+17 g |
| 0.5 | 180.44 m | yes | -2.263e+47 J | 2.82e+16 g |
| 1 | 177.44 m | yes | -1.131e+47 J | 7.04e+15 g |
| 3 | 165.44 m | yes | -3.771e+46 J | 7.83e+14 g |
| 6 | 147.44 m | NO (radiator tip) | -1.886e+46 J | 1.96e+14 g |
| 12 | 111.44 m | NO (radiator tip) | -9.440e+45 J | 4.89e+13 g |

## Hostile-input contract (demonstrated, not asserted)

Every numeric boundary is fail-closed: nan in -> nan or clamp out, never a crash, never a laundered finite answer. Live calls:

| Call | Result |
|------|--------|
| `shape_f(nan)` | nan |
| `shape_f(-R)` | 0.5 |
| `gamma(1.0)` | 2236.07 |
| `gamma(2.0)` | 2236.07 |
| `kinetic_energy_j(-0.5)` | 1.50353e+25 |
| `kinetic_energy_j(1.5)` | inf |
| `radiator_temp_k(nan)` | nan |
| `beam_capture_frac(-1)` | 1 |
| `beam_power_w(nan)` | nan |
| `alcubierre_energy_j(1,-100)` | -0 |
| `magsail_drag_n(nan)` | nan |
| `mt_tidal_g(0, 2)` | inf |
| `mt_tidal_g(-12, 2)` | inf |
| `mt_exotic_energy_j(-12)` | -0 |
| `ford_roman_bound_j_m3(0)` | -inf |
| `crossing_time_s(nan)` | inf |
| `mouth_clock_rate(-2.0)` | 0 |
| `ctc_onset_s(-1e6, 0.5)` | 0 |
| `ism_scoop_gas_kg_s(0)` | 0 |
| `fusion_fuel_kg(nan)` | nan |
| `voyage_grav_drift_s(-100)` | -9.87067e-07 |
| `wall_tidal_gradient(nan)` | nan |

No cell may contain a crash: every one of the model's numeric boundaries is wrapped by `_real`/`_finite` coercion.

## External anchors (model vs published literature)

Every quantity the model computes that can be checked against the outside world -- the twin is internally consistent AND externally anchored.

| Quantity | Model | Literature | Source |
|----------|-------|------------|--------|
| Alcubierre energy (R=100 m, v=10c, 1e-15 m wall) | 3.362e+63 J | ~1e64 J (order) | Alcubierre 1994 |
| same bubble at OUR wall (183 m, 0.2 m) | -5.656e+47 J | 8 orders cheaper -- the wall is the price | this model |
| Casimir plate density (10 nm gap) | -4.334e+04 J/m^3 | -pi^2 hbar c / 720 a^4 | Lamoreaux 1997 (measured) |
| Earth-surface clock deficit | 6.961e-10 s/s | GM/rc^2 ~ 7e-10 s/s (~60 us/day gravitational; GPS nets ~38 us/day with orbital motion) | IERS / GR textbooks |
| Ford-Roman QI bound | 3.718e-62 J/m^3 | -hbar c / (720 pi^2 tau^4) | Ford & Roman 1996 |
| MT throat flare-out at 12 m | b' = -1.0000 | b'(r0) < 1 required | Morris & Thorne 1988 |
| MMP survivable mass | 45834 M_sun | magnetically charged, stellar scale | Maldacena-Milekhin-Popov 2020 |
| magsail drag law | F = Cd rho v^2 A | identical | Zubrin & Andrews 1991 |
| photon brake sail | Forward staging sail | identical | Forward 1984 |
| onboard Casimir total | -3.09 MJ | positive-gap plates, measured physics | this model

## Numerical error budget

| Approximation | Error / bound |
|---------------|---------------|
| `warp_energy_integral` (Simpson, 4000 samples) | max rel err 9.58e-06 vs analytic R^2 sigma/3 over 33 decades |
| `max_boost_beta` bisection | voyage lock 0.8544 vs ceiling 0.8547 (3e-4) |
| `lorentz_gamma` clamp at beta=0.9999999 | gamma max 2236 (true value diverges) |
| flat-interior cutoff R-6*wall | f(R-6d) = 1.0000 (not exactly 1) |
| radiator equilibrium | instantaneous; real panels lag tau=90 s |
| magsail decel | analytic v^-2 drag integral, no ISM density variation |
| grav drift | point-mass wells only, no post-Newtonian terms |
| constants | CODATA 2018 / IAU 2015, as printed |

## Master index (every documented item, A-Z)

Every spec key, component, function, class, check domain and section, with where it lives in this document.

| Item | Documented in |
|------|---------------|
| `1. THE METRIC  (what a warp drive actually is)` | info panel |
| `10. STOPPING  (the part every warp story skips)` | info panel |
| `11. THE WALL  (a place, and not a survivable one)` | info panel |
| `12. THE INTERSTELLAR MEDIUM  (what the bubble collects)` | info panel |
| `13. CLOCKS  (what a warp drive does not buy you)` | info panel |
| `14. HORIZONS  (why the helm locks above beta = 1)` | info panel |
| `15. MASS BUDGET  (every kilogram from geometry x density)` | info panel |
| `15b. SHIP COMPONENTS  (every part, fully explained)` | info panel |
| `15c. EXTERNAL INFRASTRUCTURE  (what the ship does not carry)` | info panel |
| `15d. EVERY SPECIFICATION KEY  (DIMS / PLANT / DRIVE, verbatim)` | info panel |
| `15e. RUNTIME STATE & CONTROLS  (every field, every key)` | info panel |
| `15f. MODEL FUNCTION REGISTRY  (every function, method & helper)` | info panel |
| `16. HONESTY LAYER  (what keeps this a twin and not a prop)` | info panel |
| `17. ENVIRONMENTAL DILATION  (whose clock, and where)` | info panel |
| `18. THE PORTAL  (Morris-Thorne, priced)` | info panel |
| `19. AND THEN IT IS A TIME MACHINE` | info panel |
| `19b. PORTAL TRAVERSAL MATH PROOFS  (the equations, verified)` | info panel |
| `19c. ALCUBIERRE METRIC MATH PROOFS  (the equations, verified)` | info panel |
| `19d. ENERGY & ENGINEERING MATH PROOFS  (the equations, verified)` | info panel |
| `19e. BEAM & BRAKING MATH PROOFS  (the equations, verified)` | info panel |
| `19f. ISM & TIME DILATION MATH PROOFS  (the equations, verified)` | info panel |
| `19g. WORMHOLE MATH PROOFS  (the equations, verified)` | info panel |
| `19h. CROSS-FORMULA CONSISTENCY PROOFS  (everything agrees)` | info panel |
| `19i. BARRIER ENGINEERING ANALYSIS  (can we get past each wall?)` | info panel |
| `19j. MAXIMUM TIME TRAVEL PROOFS  (the equations, verified)` | info panel |
| `19k. NEAR-LIGHT-SPEED ACHIEVEMENT PROOFS  (how beta=0.855 emerges)` | info panel |
| `2. YORK EXPANSION  (space being made and unmade)` | info panel |
| `20. THE TELEPORTER THAT ACTUALLY EXISTS` | info panel |
| `20b. THE WD-88 FIELD CAR  (car-scale twin, SPECIAL WORKS tab)` | info panel |
| `20c. THE SAME-ROAD-SPOT SOLVE  (the ephemeris, fully)` | info panel |
| `21. REFERENCES` | info panel |
| `3. THE ENERGY BILL  (the whole argument, in numbers)` | info panel |
| `4. WHY SUBLUMINAL IS THE BUILDABLE ONE` | info panel |
| `5. WHY SUPERLUMINAL IS NOT` | info panel |
| `6. THE SHELL  (the drive itself)` | info panel |
| `7. POWER  (fusion runs the ship, not the trip)` | info panel |
| `8. HEAT  (the wall nobody expects)` | info panel |
| `9. GETTING UP TO SPEED  (the ship cannot launch itself)` | info panel |
| `_annulus_cylinder` | internal helpers |
| `_args_real` | internal helpers |
| `_box` | internal helpers |
| `_build_portal_parts_impl` | internal helpers |
| `_build_ship_parts_impl` | internal helpers |
| `_build_special_parts_impl` | internal helpers |
| `_car_loft` | internal helpers |
| `_coil_arc` | internal helpers |
| `_coil_count` | internal helpers |
| `_component_info_sections` | internal helpers |
| `_deck_plate` | internal helpers |
| `_detail_seg` | internal helpers |
| `_dish` | internal helpers |
| `_earth_rate` | internal helpers |
| `_envelope_points` | internal helpers |
| `_finite` | internal helpers |
| `_function_registry_lines` | internal helpers |
| `_grp` | internal helpers |
| `_hull_loft` | internal helpers |
| `_info_sections` | internal helpers |
| `_label` | internal helpers |
| `_luminance` | internal helpers |
| `_mix` | internal helpers |
| `_mt_funnel` | internal helpers |
| `_numeric_dims` | internal helpers |
| `_pipe_path` | internal helpers |
| `_place` | internal helpers |
| `_prep_global` | internal helpers |
| `_prep_mesh` | internal helpers |
| `_prep_part` | internal helpers |
| `_print_traversal` | internal helpers |
| `_radial` | internal helpers |
| `_real` | internal helpers |
| `_rgb` | internal helpers |
| `_ring_wire` | internal helpers |
| `_rod` | internal helpers |
| `_rule` | internal helpers |
| `_runtime_state_lines` | internal helpers |
| `_sech2` | internal helpers |
| `_smooth_sections` | internal helpers |
| `_solid_cylinder` | internal helpers |
| `_spec_key_lines` | internal helpers |
| `_sphere` | internal helpers |
| `_tangential` | internal helpers |
| `_tilt_z` | internal helpers |
| `_torus` | internal helpers |
| `_torus_surface` | internal helpers |
| `_trender` | internal helpers |
| `_wire_ellipsoid` | internal helpers |
| `_xform` | internal helpers |
| `_xy` | internal helpers |
| `alcubierre_energy_j` | function registry |
| `antimatter traps` | component |
| `App` | classes |
| `bar` | function registry |
| `barrier_analysis` | function registry |
| `barrier_scorecard` | function registry |
| `beam_brake_force_n` | function registry |
| `beam_brake_time_s` | function registry |
| `beam_capture_frac` | function registry |
| `beam_power_w` | function registry |
| `beam_spot_m` | function registry |
| `boost rectenna` | component |
| `boost_profile` | function registry |
| `build_portal_parts` | function registry |
| `build_ship_parts` | function registry |
| `build_special_parts` | function registry |
| `buildability_ledger` | function registry |
| `car_casimir_j` | function registry |
| `car_fault_effects` | function registry |
| `car_mass_budget` | function registry |
| `car_mph_step` | function registry |
| `car_ops_ledger` | function registry |
| `car_part_mass` | function registry |
| `car_power_budget` | function registry |
| `car_thermal_step` | function registry |
| `car_transit` | function registry |
| `car_trigger_v` | function registry |
| `Casimir lattice` | component |
| `casimir_cassette` | function registry |
| `casimir_energy_density` | function registry |
| `casimir_onboard_j` | function registry |
| `chain_wormhole_offset` | function registry |
| `check_envelope` | function registry |
| `chip` | function registry |
| `clamp` | function registry |
| `clock_ledger` | function registry |
| `consumables + crew` | component |
| `contrast_text` | function registry |
| `crew decks` | component |
| `crew hull shell` | component |
| `crossing_time_s` | function registry |
| `cruise_load_w` | function registry |
| `cryoplant` | component |
| `ctc_by_gravity_well` | function registry |
| `ctc_by_warp_transport` | function registry |
| `ctc_exists` | function registry |
| `ctc_onset_s` | function registry |
| `deflector` | component |
| `destination photon brake` | infrastructure |
| `DIMS.amtrap_d_m` | spec table |
| `DIMS.amtrap_kg` | spec table |
| `DIMS.amtrap_rho` | spec table |
| `DIMS.amtrap_wall_m` | spec table |
| `DIMS.amtraps` | spec table |
| `DIMS.bubble_r_m` | spec table |
| `DIMS.cap_offset_m` | spec table |
| `DIMS.capring_d_m` | spec table |
| `DIMS.capring_minor_d_m` | spec table |
| `DIMS.capring_wall_frac` | spec table |
| `DIMS.casimir_cassettes` | spec table |
| `DIMS.casimir_gap_nm` | spec table |
| `DIMS.casimir_pitch_nm` | spec table |
| `DIMS.casimir_plate_m` | spec table |
| `DIMS.casimir_rho` | spec table |
| `DIMS.casimir_stack_m` | spec table |
| `DIMS.coil_bore_m` | spec table |
| `DIMS.coil_build_m` | spec table |
| `DIMS.coil_current_a` | spec table |
| `DIMS.coil_density` | spec table |
| `DIMS.coil_len_m` | spec table |
| `DIMS.coil_standoff_m` | spec table |
| `DIMS.coil_temp_k` | spec table |
| `DIMS.coil_turns` | spec table |
| `DIMS.coils` | spec table |
| `DIMS.collector_d_m` | spec table |
| `DIMS.collector_deploy_km` | spec table |
| `DIMS.collector_depth_m` | spec table |
| `DIMS.collector_film_rho` | spec table |
| `DIMS.collector_film_um` | spec table |
| `DIMS.collector_z0_m` | spec table |
| `DIMS.crew` | spec table |
| `DIMS.crew_supplies_kg` | spec table |
| `DIMS.cryo_d_m` | spec table |
| `DIMS.cryo_len_m` | spec table |
| `DIMS.cryo_mount_rfrac` | spec table |
| `DIMS.cryo_rho` | spec table |
| `DIMS.cryo_units` | spec table |
| `DIMS.deck_inset_m` | spec table |
| `DIMS.deck_t_m` | spec table |
| `DIMS.deflector_d_m` | spec table |
| `DIMS.deflector_depth_m` | spec table |
| `DIMS.deflector_rho` | spec table |
| `DIMS.deflector_t_m` | spec table |
| `DIMS.hull_d_m` | spec table |
| `DIMS.hull_decks` | spec table |
| `DIMS.hull_density` | spec table |
| `DIMS.hull_len_m` | spec table |
| `DIMS.hull_shell_rfrac` | spec table |
| `DIMS.hull_wall_m` | spec table |
| `DIMS.interior_margin` | spec table |
| `DIMS.len_margin_m` | spec table |
| `DIMS.magsail_cd` | spec table |
| `DIMS.magsail_current_a` | spec table |
| `DIMS.magsail_mass_kg` | spec table |
| `DIMS.magsail_r_km` | spec table |
| `DIMS.magsail_regen_eff` | spec table |
| `DIMS.magsail_view_scale` | spec table |
| `DIMS.portal_casimir_rings` | spec table |
| `DIMS.portal_coils` | spec table |
| `DIMS.portal_frame_d_m` | spec table |
| `DIMS.portal_gate_d_m` | spec table |
| `DIMS.portal_ring_minor_d_m` | spec table |
| `DIMS.pylon_len_m` | spec table |
| `DIMS.pylon_rho` | spec table |
| `DIMS.pylon_t_m` | spec table |
| `DIMS.pylon_w_m` | spec table |
| `DIMS.pylons` | spec table |
| `DIMS.rad_emissivity` | spec table |
| `DIMS.rad_inner_r_m` | spec table |
| `DIMS.rad_len_m` | spec table |
| `DIMS.rad_limit_k` | spec table |
| `DIMS.rad_rho` | spec table |
| `DIMS.rad_t_m` | spec table |
| `DIMS.rad_temp_k` | spec table |
| `DIMS.rad_w_m` | spec table |
| `DIMS.rad_z0_m` | spec table |
| `DIMS.radiators` | spec table |
| `DIMS.rcs_d_m` | spec table |
| `DIMS.rcs_len_m` | spec table |
| `DIMS.rcs_pods` | spec table |
| `DIMS.rcs_rho` | spec table |
| `DIMS.reactor_direct_eff` | spec table |
| `DIMS.reactor_major_d_m` | spec table |
| `DIMS.reactor_minor_d_m` | spec table |
| `DIMS.reactor_rho` | spec table |
| `DIMS.reactor_th_gw` | spec table |
| `DIMS.reactor_wall_m` | spec table |
| `DIMS.ring_density` | spec table |
| `DIMS.ring_major_d_m` | spec table |
| `DIMS.ring_minor_d_m` | spec table |
| `DIMS.ring_sectors` | spec table |
| `DIMS.ring_wall_m` | spec table |
| `DIMS.smes_b_t` | spec table |
| `DIMS.smes_major_d_m` | spec table |
| `DIMS.smes_minor_d_m` | spec table |
| `DIMS.smes_rho` | spec table |
| `DIMS.smes_wall_m` | spec table |
| `DIMS.smes_z0_m` | spec table |
| `DIMS.wall_thick_m` | spec table |
| `DIMS::Antimatter store (peak fold transitions only)` | spec group |
| `DIMS::Boost receiver (the stellar-tap rectenna)` | spec group |
| `DIMS::Casimir negative-energy lattice (96 cassettes in the ring wall)` | spec group |
| `DIMS::Crew hull (flat spacetime inside -- ordinary ship engineering)` | spec group |
| `DIMS::Cryoplant (holds the HTS coils at 18 K)` | spec group |
| `DIMS::D-3He fusion reactor (the housekeeping plant)` | spec group |
| `DIMS::Fore / aft shaping rings (set the front-back asymmetry)` | spec group |
| `DIMS::Magnetic sail (the only credible way to STOP)` | spec group |
| `DIMS::Main warp ring (the shift-vector shell -- the actual "drive")` | spec group |
| `DIMS::Navigation deflector (subwarp dust shield)` | spec group |
| `DIMS::Reaction control (subwarp only -- ion / VASIMR pods)` | spec group |
| `DIMS::SMES field-transient buffer (superconducting magnetic store)` | spec group |
| `DIMS::Structural pylons hull -> ring` | spec group |
| `DIMS::Superconducting field coils (96, one per ring sector)` | spec group |
| `DIMS::Warp bubble geometry (the spacetime, not the hardware)` | spec group |
| `DIMS::Waste-heat radiators (sized against the REAL waste heat)` | spec group |
| `DIMS::Wormhole portal gate (Morris-Thorne throat)` | spec group |
| `draw_bubble_glow` | function registry |
| `draw_vignette` | function registry |
| `DRIVE.arrival_beta` | spec table |
| `DRIVE.beta_ftl_max` | spec table |
| `DRIVE.beta_sub_max` | spec table |
| `DRIVE.bubble_form_s` | spec table |
| `DRIVE.integrity_min` | spec table |
| `DRIVE.spinup_s` | spec table |
| `DRIVE.wall_max_m` | spec table |
| `DRIVE.wall_min_m` | spec table |
| `DRIVE::` | spec group |
| `earth_helio_pos` | function registry |
| `earth_surface_offset` | function registry |
| `energy_conditions` | function registry |
| `energy_density` | function registry |
| `equiv_mass_kg` | function registry |
| `feasibility_scorecard` | function registry |
| `flat_interior_r` | function registry |
| `fmt_dist` | function registry |
| `fmt_energy` | function registry |
| `fmt_mass` | function registry |
| `fmt_power` | function registry |
| `fmt_time` | function registry |
| `ford_roman_bound_j_m3` | function registry |
| `ford_roman_max_throat_tau` | function registry |
| `ford_roman_wall_limit` | function registry |
| `fusion reactor` | component |
| `fusion_fuel_kg` | function registry |
| `gott_pair_offset` | function registry |
| `grav_potential_at` | function registry |
| `grav_rate` | function registry |
| `helium-3 supply chain` | infrastructure |
| `honesty_audit` | function registry |
| `horizon_locked` | function registry |
| `HTS field coils` | component |
| `info_sections` | function registry |
| `ISM scoop refuelling` | infrastructure |
| `ism_blast_energy_j` | function registry |
| `ism_d3he_yield_kg_s` | function registry |
| `ism_particles_swept` | function registry |
| `ism_scoop_gas_kg_s` | function registry |
| `kerr_ctc_offset` | function registry |
| `kinetic_energy_j` | function registry |
| `lapse_static` | function registry |
| `log_bar_x` | function registry |
| `lorentz_gamma` | function registry |
| `magsail loop` | component |
| `magsail_area_m2` | function registry |
| `magsail_decel_time_s` | function registry |
| `magsail_drag_n` | function registry |
| `magsail_halving_time_s` | function registry |
| `main` | function registry |
| `mass_budget` | function registry |
| `max_boost_beta` | function registry |
| `max_time_displacement` | function registry |
| `Mesh` | classes |
| `MetricCam` | classes |
| `mmp_extremal_charge_c` | function registry |
| `mmp_summary` | function registry |
| `mmp_tidal_mass_kg` | function registry |
| `mmp_traversal_time_s` | function registry |
| `mouth_clock_rate` | function registry |
| `mouth_time_offset_s` | function registry |
| `mt_embedding_z` | function registry |
| `mt_exotic_energy_j` | function registry |
| `mt_flare_out` | function registry |
| `mt_min_throat_m` | function registry |
| `mt_proper_length` | function registry |
| `mt_redshift_phi` | function registry |
| `mt_shape_b` | function registry |
| `mt_shape_b_prime` | function registry |
| `mt_throat_density` | function registry |
| `mt_tidal_g` | function registry |
| `mt_tidal_profile` | function registry |
| `mt_traversal_time_s` | function registry |
| `multijump_breakeven_s` | function registry |
| `multijump_plan` | function registry |
| `nested_wormhole_offset` | function registry |
| `operations_ledger` | function registry |
| `orders_of_magnitude` | function registry |
| `panel` | function registry |
| `Part` | classes |
| `PLANT.am_energy_j_kg` | spec table |
| `PLANT.beam_aperture_km` | spec table |
| `PLANT.beam_lambda_um` | spec table |
| `PLANT.beam_range_ly` | spec table |
| `PLANT.coil_ac_mw` | spec table |
| `PLANT.control_mw` | spec table |
| `PLANT.conversion_eff` | spec table |
| `PLANT.cryo_mw` | spec table |
| `PLANT.d3he_j_kg` | spec table |
| `PLANT.hotel_mw` | spec table |
| `PLANT.recovery_eff` | spec table |
| `PLANT.tap_w` | spec table |
| `PLANT::` | spec group |
| `plant_electric_w` | function registry |
| `portal_cycle_s` | function registry |
| `portal_summary` | function registry |
| `portal_traversal` | function registry |
| `print_startup_banner` | function registry |
| `project` | function registry |
| `pylons` | component |
| `quantum_teleport_facts` | function registry |
| `radiator_area_m2` | function registry |
| `radiator_required_m2` | function registry |
| `radiator_temp_k` | function registry |
| `radiators` | component |
| `RCS pods` | component |
| `report_dilation` | function registry |
| `report_feasibility` | function registry |
| `report_ladder` | function registry |
| `report_metric` | function registry |
| `report_portal` | function registry |
| `report_portal_test` | function registry |
| `report_spec` | function registry |
| `report_voyage` | function registry |
| `road_frame` | function registry |
| `road_inertial_speed` | function registry |
| `road_solar_hour` | function registry |
| `rocket_proper_time_s` | function registry |
| `rot_x` | function registry |
| `rot_y` | function registry |
| `rot_z` | function registry |
| `selftest` | function registry |
| `shape_df` | function registry |
| `shape_df_shifted` | function registry |
| `shape_f` | function registry |
| `shaping rings` | component |
| `ship_mass_kg` | function registry |
| `ship_self_dilation` | function registry |
| `ShipRenderer` | classes |
| `SMES buffer` | component |
| `smes_store_j` | function registry |
| `Starfield` | classes |
| `static_observer_exists` | function registry |
| `stellar tap (6.4e+18 W, 1000 km array)` | infrastructure |
| `text_shadow` | function registry |
| `the warp shell as a drive` | infrastructure |
| `tipler_cylinder_offset` | function registry |
| `vgradient` | function registry |
| `visser_shell_energy_j` | function registry |
| `visser_shell_mass_kg` | function registry |
| `visser_summary` | function registry |
| `Voyage` | classes |
| `voyage_grav_drift_s` | function registry |
| `wall_tidal_gradient` | function registry |
| `warp ring shell` | component |
| `warp_energy_integral` | function registry |
| `WarpCore` | classes |
| `waste_heat_w` | function registry |
| `WD-1 FOLDRUNNER  --  CONCEPT OVERVIEW` | info panel |
| `wormhole gates and time machines` | infrastructure |
| `wrap_plain` | function registry |
| `wrap_text` | function registry |
| `york_theta` | function registry |

## The cruise power budget (where every watt goes)

Live decomposition of `cruise_load_w(beta)`: coil AC loss ~ `coil_ac_mw x beta^2 x on`; metric servo ~ `control_mw x (0.2 + 0.8 beta) x on`; cryo and hotel are constant.

| Load | beta=0.25 | beta=0.5 | beta=0.855 | beta=0.99 |
|------|-----------|----------|------------|-----------|
| HTS coil AC loss | 2.391 GW | 9.563 GW | 27.964 GW | 37.492 GW |
| metric servo | 2.826 GW | 4.238 GW | 6.245 GW | 7.007 GW |
| cryoplant | 2.493 GW | 2.493 GW | 2.493 GW | 2.493 GW |
| hotel/crew | 0.096 GW | 0.096 GW | 0.096 GW | 0.096 GW |
| **total electric** | 7.81 GW | 16.4 GW | 36.8 GW | 47.1 GW |
| waste heat | 12.6 GW | 26.4 GW | 59.4 GW | 75.9 GW |
| fuel burn | 3.09 kg/d | 6.49 kg/d | 14.57 kg/d | 18.64 kg/d |

## The full mission ledger (a real crossing, accounted)

A complete Sol->Proxima flight at beta=0.5 with the destination array present -- the final state of every counter in the honesty ledger. `beam_in` and `brake_dissipated` bracket `kinetic_peak`: energy in from the tap, energy out through the photon brake.

| Ledger key | Total over the mission |
|------------|------------------------|
| `am_kg` | 0  --  antimatter consumed |
| `beam_in` | 1.515e+25  --  joules captured from the stellar tap |
| `brake_dissipated` | 1.419e+25  --  work done against the destination beam |
| `fuel_kg` | 2.033e+04  --  D-3He burnt |
| `ism_particles` | 4.036e+26  --  protons collected by the wall |
| `kinetic` | 0  --  current kinetic energy (0 at rest) |
| `kinetic_peak` | 1.504e+25  --  peak KE at cruise |
| `magsail_regen` | 9.48e+21  --  energy regenerated during braking |
| `plant_out` | 4.438e+18  --  electricity generated by the fusion plant |
| `radiated` | 7.158e+18  --  waste heat radiated to space |

| Clock | Final |
|-------|-------|
| ship proper time | 9.0007 yr |
| Earth clock | 9.0007 yr |
| ship - Earth | +2.516 s |
| coordinate time | 9.0007 yr |
| final phase | ARRIVED |

### The mission log (every phase transition)

-    0.0 s  BOOST to beta 0.500 -- bill 15 YJ over 30.0 d
-   24.4 d  cruise beta 0.5000 reached; beam released
-  8.50 yr  MAGSAIL DEPLOYED at beta 0.500
-  8.50 yr    magsail alone: halves speed in 65.28 yr, STOPS in 3.26e+04 yr
-  8.50 yr    destination array ASSUMED PRESENT: photon brake 4.27e+10 N -> stop in 50.7 d
-  8.50 yr  bubble down: 4e+26 swept protons released forward (7.97 PJ)
-  8.52 yr  FLYBY -- passing Proxima at beta 0.453, still 3.26e+04 yr from stopped
-  8.63 yr  ARRIVED. ship 8.63 yr / Earth 8.63 yr

## The failure path, traced (a worked collapse)

Commanding a superluminal shell the ship cannot hold: integrity drains under shell stress until the bubble lets go. Live trace of `WarpCore` under beta_cmd = 2, thin wall:

| tick | beta | integrity | status | msg |
|------|------|-----------|--------|-----|
| 0 s | 0.000 | 1.000 | BUBBLE DOWN |  |
| 1000 s | 0.000 | 0.940 | SUPERLUMINAL -- UNFUNDED |  |
| 2000 s | 0.000 | 0.880 | SUPERLUMINAL -- UNFUNDED |  |
| 3000 s | 0.000 | 0.820 | SUPERLUMINAL -- UNFUNDED |  |
| 4000 s | 0.000 | 0.760 | SUPERLUMINAL -- UNFUNDED |  |
| 5000 s | 0.000 | 0.700 | SUPERLUMINAL -- UNFUNDED |  |
| 6000 s | 0.000 | 0.640 | SUPERLUMINAL -- UNFUNDED |  |
| 7000 s | 0.000 | 0.580 | SUPERLUMINAL -- UNFUNDED |  |
| 8000 s | 0.000 | 0.520 | SUPERLUMINAL -- UNFUNDED |  |
| 9000 s | 0.000 | 0.460 | SUPERLUMINAL -- UNFUNDED |  |
| 10000 s | 0.000 | 0.400 | SUPERLUMINAL -- UNFUNDED |  |
| 10833 s | 0.000 | 0.350 | COLLAPSED | BUBBLE COLLAPSE -- shell shape lost |

Collapse at 10833 s.

Exotic debt booked (never supplied): 1.131e+49 J. `was_superluminal` = False -- on collapse the 'velocity' vanishes because it was never momentum.

## TEST mode, traced (auto-play with custom settings)

The demo state machine stepping through a mission at beta=0.5 with the destination array present:

| step | phase after auto_step |
|------|-----------------------|
| 1 | BOOST |
| 2 | CRUISE |
| 3 | BRAKE |
| 4 | BRAKE |
| 5 | BRAKE |

Final: phase=BRAKE, auto_done=False

## Glossary (the physics vocabulary)

| Term | Meaning |
|------|---------|
| beta | v/c -- the ship's speed as a fraction of light speed |
| NEC / WEC / DEC / SEC | null/weak/dominant/strong energy conditions -- the sanity tests T^uv must pass |
| York time theta | expansion scalar of the bubble wall; contracts ahead, expands behind |
| shape function f(r) | Alcubierre top-hat: 1 inside, 0 outside, steep transition at r = R |
| shift vector | the metric piece carrying the bubble; the ring's stress-energy sources it |
| lapse alpha | time-time metric component; 1 everywhere here -- no dilation dividend |
| wall | the 0.2 m transition layer where all the physics (energy, tidal, York) lives |
| QI (quantum inequality) | Ford-Roman bound: negative energy can't be held long or concentrated -- wall >= 100 L_P |
| Casimir energy | real measured negative energy between plates, -pi^2 hbar c / 720 a^4 |
| exotic debt | negative energy booked as OWED on the ledger -- never credited as supply |
| REBCO / HTS | rare-earth cuprate superconductor tape; the coil conductor at 18 K |
| SMES | superconducting magnetic energy store -- the 2.76 TJ buffer, not a 'warp battery' |
| D-3He | aneutronic fusion fuel: D + 3He -> 4He + p, 62% direct-convertible |
| rectenna | rectifying antenna film catching the boost beam |
| magsail | superconducting loop dragging on the ISM to brake |
| ISM | interstellar medium -- 1e5 protons/m^3 swept by the wall |
| b0 | wormhole throat radius; all throat quantities key on it |
| flare-out | b'(r0) < 1 -- the throat must open outward |
| CTC | closed timelike curve -- what any desynced mouth pair becomes |
| chronology protection | Hawking's conjecture: vacuum fluctuations diverge at a forming CTC |
| MMP wormhole | magnetically-charged-black-hole wormhole; traversable on paper, needs unobserved monopoles |
| Visser shell | thin-shell wormhole construction; concentrating exotic mass makes it worse, not better |
| SSV theorem | Santiago-Schuster-Visser 2022: ANY v>c warp violates NEC -- the class-wide ban |
| emergent beta | 0.8547 -- set by beam range/mass/KE, not dialed |

## Unit equivalences (the headline numbers, translated)

#### Energies

- cruise KE (beta=0.855) = 90.2 YJ = 2.16e+08 Tsar Bombas = 5.05e-22 M_sun c^2
- tap output per second = 6.4 EJ = 15.3 Tsar Bombas = 3.58e-29 M_sun c^2
- Alcubierre bill (this bubble) = 5.656e+47 J = 1.35e+30 Tsar Bombas = 3.16 M_sun c^2
- survivable portal bill = 2.730e+51 J = 6.53e+33 Tsar Bombas = 1.53e+04 M_sun c^2
- onboard Casimir = 3.09 MJ = 7.38e-12 Tsar Bombas = 1.73e-41 M_sun c^2
- SMES buffer = 2.76 TJ = 6.6e-06 Tsar Bombas = 1.55e-35 M_sun c^2
- antimatter store = 7.55 EJ = 18 Tsar Bombas = 4.22e-29 M_sun c^2
- ISM blast on arrival = 7.98 PJ = 0.0191 Tsar Bombas = 4.47e-32 M_sun c^2

#### Distances

- ship span = 395.4 m = 0.00 ly = 0.395 km = 1.00 ship spans
- bubble radius = 183.4 m = 0.00 ly = 0.183 km = 0.46 ship spans
- ring circumference = 1152.6 m = 0.00 ly = 1.15 km = 2.91 ship spans
- REBCO tape = 4.09e+05 km = 0.00 ly = 4.09e+05 km = 1033196.76 ship spans
- magsail circumference = 1.76e+04 km = 0.00 ly = 1.76e+04 km = 44493.98 ship spans
- Sol-Proxima = 4.2465 ly = 4.25 ly = 4.02e+13 km = 101605948284811.25 ship spans
- beam spot at 0.62 ly = 14.3 km = 0.00 ly = 14.3 km = 36.20 ship spans

## Physical constants used

| Constant | Value |
|----------|-------|
| `C_LIGHT` | 2.99792e+08 |
| `G_NEWTON` | 6.6743e-11 |
| `HBAR` | 1.05457e-34 |
| `H_PLANCK` | 6.62607e-34 |
| `K_B` | 1.38065e-23 |
| `SIGMA_SB` | 5.67037e-08 |
| `E_CHARGE` | 1.60218e-19 |
| `M_P` | 1.67262e-27 |
| `M_E` | 9.10938e-31 |
| `MU0` | 1.25664e-06 |
| `EPS0` | 8.85419e-12 |
| `M_SUN` | 1.98847e+30 |
| `L_SUN` | 3.828e+26 |
| `M_EARTH` | 5.97217e+24 |
| `AU` | 1.49598e+11 |
| `LY` | 9.46073e+15 |
| `YR` | 3.15576e+07 |
| `DAY` | 86400 |
| `PROXIMA_M` | 4.0175e+16 |
| `ISM_N_M3` | 100000 |
| `ISM_DUST_KG_M3` | 1e-23 |

## Runtime environment

| Requirement | Status |
|-------------|--------|
| Python 3 stdlib | `argparse`, `functools`, `inspect`, `itertools`, `math`, `os`, `re`, `sys`, `warnings` |
| `numpy` | required -- mesh vertices are `np.array` and every rotation uses it |
| `pygame` | optional -- imported inside `try:`; without it every CLI flag and `--selftest` still runs (viewer raises a friendly error) |
| No build step | the model is a single file; `python Warpdrive.py --selftest` is the entire CI contract |

## Input-guard inventory (which functions defend their domain)

Each public function's source scanned for its boundary machinery (`_real` NaN coercion, `_finite` infinity coercion, `min`/`max` clamps, explicit `nan`/`inf` returns). This is the static map behind the hostile-input demonstration above.

| Function | `_real` | `_finite` | clamps | nan/inf returns |
|----------|---------|-----------|--------|-----------------|
| `alcubierre_energy_j` | - | - | - | - |
| `bar` | 4 | 3 | 1 | 1 |
| `barrier_analysis` | - | - | - | - |
| `barrier_scorecard` | - | - | - | - |
| `beam_brake_force_n` | - | - | - | 2 |
| `beam_brake_time_s` | - | - | - | 1 |
| `beam_capture_frac` | - | - | - | - |
| `beam_power_w` | - | - | - | - |
| `beam_spot_m` | - | - | - | 7 |
| `boost_profile` | - | - | 4 | 6 |
| `build_portal_parts` | - | 1 | 1 | - |
| `build_ship_parts` | - | 1 | 1 | - |
| `build_special_parts` | 2 | 1 | 2 | - |
| `buildability_ledger` | - | 8 | - | 5 |
| `car_casimir_j` | - | 1 | - | 2 |
| `car_fault_effects` | - | - | - | - |
| `car_mass_budget` | - | - | - | - |
| `car_mph_step` | 3 | 3 | 2 | 1 |
| `car_ops_ledger` | - | - | - | - |
| `car_part_mass` | - | - | - | - |
| `car_power_budget` | - | - | - | - |
| `car_thermal_step` | 4 | 5 | 1 | - |
| `car_transit` | 2 | 1 | - | 9 |
| `car_trigger_v` | - | - | - | - |
| `casimir_cassette` | - | 2 | - | - |
| `casimir_energy_density` | - | - | 1 | 2 |
| `casimir_onboard_j` | - | - | - | - |
| `chain_wormhole_offset` | - | - | 4 | 4 |
| `check_envelope` | - | - | - | - |
| `chip` | 2 | 2 | 4 | - |
| `clamp` | - | - | 2 | 2 |
| `clock_ledger` | - | - | 1 | 2 |
| `contrast_text` | - | - | - | 2 |
| `crossing_time_s` | - | - | - | 3 |
| `cruise_load_w` | - | - | 2 | - |
| `ctc_by_gravity_well` | 2 | 2 | 1 | 2 |
| `ctc_by_warp_transport` | - | - | 1 | - |
| `ctc_exists` | 2 | 2 | 1 | 1 |
| `ctc_onset_s` | - | - | 1 | 4 |
| `draw_bubble_glow` | - | 1 | 2 | - |
| `draw_vignette` | - | 1 | 2 | - |
| `earth_helio_pos` | 1 | 1 | - | 1 |
| `earth_surface_offset` | 5 | 3 | - | 1 |
| `energy_conditions` | - | - | - | - |
| `energy_density` | 3 | - | - | 2 |
| `equiv_mass_kg` | - | - | - | - |
| `feasibility_scorecard` | - | - | - | - |
| `flat_interior_r` | - | - | 1 | 3 |
| `fmt_dist` | 1 | - | - | - |
| `fmt_energy` | 1 | - | - | - |
| `fmt_mass` | 1 | - | - | - |
| `fmt_power` | 1 | - | - | - |
| `fmt_time` | 1 | - | - | - |
| `ford_roman_bound_j_m3` | - | - | - | 4 |
| `ford_roman_max_throat_tau` | - | - | - | - |
| `ford_roman_wall_limit` | - | - | 1 | 2 |
| `fusion_fuel_kg` | - | - | 1 | 5 |
| `gott_pair_offset` | - | - | 2 | 4 |
| `grav_potential_at` | 1 | - | 1 | 2 |
| `grav_rate` | - | - | 1 | 3 |
| `honesty_audit` | 13 | 4 | 4 | 14 |
| `horizon_locked` | - | - | - | - |
| `info_sections` | - | - | - | 2 |
| `ism_blast_energy_j` | - | - | - | - |
| `ism_d3he_yield_kg_s` | 1 | 2 | 2 | 2 |
| `ism_particles_swept` | - | - | 1 | 3 |
| `ism_scoop_gas_kg_s` | - | - | - | - |
| `kerr_ctc_offset` | - | - | 1 | 6 |
| `kinetic_energy_j` | - | - | - | 1 |
| `lapse_static` | 1 | - | - | - |
| `log_bar_x` | - | 1 | - | - |
| `lorentz_gamma` | 1 | 1 | 1 | 1 |
| `magsail_area_m2` | - | - | - | - |
| `magsail_decel_time_s` | - | - | 1 | 7 |
| `magsail_drag_n` | - | - | - | - |
| `magsail_halving_time_s` | - | - | - | 1 |
| `main` | 1 | 1 | - | 1 |
| `mass_budget` | - | - | - | - |
| `max_boost_beta` | - | - | - | 2 |
| `max_time_displacement` | - | - | 2 | - |
| `mmp_extremal_charge_c` | - | - | - | - |
| `mmp_summary` | - | - | - | - |
| `mmp_tidal_mass_kg` | - | - | 1 | 3 |
| `mmp_traversal_time_s` | - | - | 2 | - |
| `mouth_clock_rate` | 2 | - | 2 | 4 |
| `mouth_time_offset_s` | 3 | - | - | - |
| `mt_embedding_z` | - | - | - | - |
| `mt_exotic_energy_j` | - | - | 1 | 3 |
| `mt_flare_out` | - | - | 2 | - |
| `mt_min_throat_m` | - | - | 2 | 3 |
| `mt_proper_length` | - | - | 1 | 3 |
| `mt_redshift_phi` | - | - | - | - |
| `mt_shape_b` | - | - | 1 | 4 |
| `mt_shape_b_prime` | - | - | 1 | 3 |
| `mt_throat_density` | - | - | - | 2 |
| `mt_tidal_g` | - | - | 1 | 5 |
| `mt_tidal_profile` | - | - | 2 | 4 |
| `mt_traversal_time_s` | - | - | 3 | 4 |
| `multijump_breakeven_s` | 1 | - | - | 1 |
| `multijump_plan` | 6 | - | 7 | 18 |
| `nested_wormhole_offset` | - | - | - | - |
| `operations_ledger` | - | - | - | - |
| `orders_of_magnitude` | 2 | - | - | 4 |
| `panel` | 2 | 5 | 3 | - |
| `plant_electric_w` | - | - | - | - |
| `portal_cycle_s` | 3 | - | 3 | 4 |
| `portal_summary` | - | - | 1 | - |
| `portal_traversal` | 9 | 2 | 1 | 7 |
| `print_startup_banner` | - | - | - | - |
| `project` | 3 | 4 | - | 5 |
| `quantum_teleport_facts` | - | - | - | 1 |
| `radiator_area_m2` | - | - | - | - |
| `radiator_required_m2` | - | - | 1 | 5 |
| `radiator_temp_k` | - | - | 1 | 5 |
| `report_dilation` | - | - | - | - |
| `report_feasibility` | - | - | - | 1 |
| `report_ladder` | - | - | - | - |
| `report_metric` | - | 1 | - | - |
| `report_portal` | - | 2 | - | 3 |
| `report_portal_test` | - | - | - | 5 |
| `report_spec` | - | 15 | - | 2 |
| `report_voyage` | 3 | - | - | 1 |
| `road_frame` | 5 | 3 | - | 5 |
| `road_inertial_speed` | 2 | 1 | - | - |
| `road_solar_hour` | 3 | 2 | - | 1 |
| `rocket_proper_time_s` | - | - | 1 | 3 |
| `rot_x` | - | - | - | - |
| `rot_y` | - | - | - | - |
| `rot_z` | - | - | - | - |
| `selftest` | 2 | 24 | 48 | 233 |
| `shape_df` | 3 | - | 1 | 4 |
| `shape_df_shifted` | 3 | - | 1 | 4 |
| `shape_f` | 3 | - | 1 | 4 |
| `ship_mass_kg` | - | - | - | - |
| `ship_self_dilation` | - | - | - | 3 |
| `smes_store_j` | - | - | - | - |
| `static_observer_exists` | 1 | - | - | 1 |
| `text_shadow` | - | - | - | - |
| `tipler_cylinder_offset` | - | - | 2 | 8 |
| `vgradient` | - | - | - | - |
| `visser_shell_energy_j` | - | - | - | - |
| `visser_shell_mass_kg` | - | - | - | - |
| `visser_summary` | - | - | - | - |
| `voyage_grav_drift_s` | - | - | - | - |
| `wall_tidal_gradient` | - | - | 2 | 5 |
| `warp_energy_integral` | - | - | 4 | 5 |
| `waste_heat_w` | - | - | - | 4 |
| `wrap_plain` | - | - | - | - |
| `wrap_text` | - | - | - | - |
| `york_theta` | 3 | - | - | 2 |

103 of 150 public functions carry explicit boundary machinery; the rest are pure arithmetic over already-guarded quantities.

## What the model does NOT model (the abstraction boundary)

The simplifications that bound every number in this document -- each is a deliberate trade, cited where it lives:

- **Spherical symmetry everywhere -- the warp bubble, the wormhole throats and the gravity wells are all 1-D in r; no angular structure, no rotating axisymmetric metrics beyond Kerr's treated parametrically** -- `shape_f, york_theta, mt_*`
- **No backreaction -- matter stress-energy shapes the metric but the metric never feeds back on the matter; the exotic bill is a ledger entry, not a self-consistent solution** -- `alcubierre_energy_j, WarpCore.update`
- **Instantaneous beam geometry -- photons arrive the frame they're counted; light-travel lag between tap and ship is not carried in the kinetic loop** -- `beam_power_w, Voyage._step`
- **Newtonian flight kinematics below the clamp -- position and momentum accumulate classically; SR enters through gamma in the energy and clock ledgers only** -- `Voyage._step, clock_ledger`
- **Lumped thermal model -- the radiator is one temperature with one time constant; no spatial temperature profile, no transient hot spots** -- `radiator_temp_k, WarpCore.update`
- **Point-particle ISM -- the medium is a number density and a dust density, not a distribution of grain sizes or ionisation states** -- `ism_particles_swept, ism_blast_energy_j`
- **Perfect rectenna/sail coupling -- capture fraction is purely geometric (spot vs aperture); alignment jitter, polarisation and material response are not modeled** -- `beam_capture_frac`
- **Coil stress is a budget, not a FEM -- hoop tension is bookkept against REBCO limits; no structural dynamics, fatigue, or quench propagation** -- `coil hoop check in selftest`
- **Single destination -- the route is Sol to Proxima; MULTIJUMP isotope fractions are the only multi-leg machinery** -- `PROXIMA_M, MULTIJUMP`
- **No economy, crew, or operations -- power, fuel and integrity are the only consumables; life support appears only as the constant 'hotel' load** -- `PLANT hotel_w entry`
- **CTC constructions are parametric recipes, not spacetimes -- each time machine is priced from its published scaling law, not embedded in a solved metric** -- `ctc_by_*, *_offset`
- **No rendering physics -- the viewer draws tessellated parts in painter's order; no lighting, shadows, or relativistic visualisation** -- `ShipRenderer, VISUAL_DETAIL`

## The formula sheet (every governing equation, live)

The mathematics the twin actually runs -- each equation named, with the function that implements it and a live evaluation so the sheet can never go stale.

- `f(r) = (tanh((R+d-r)/d) - tanh((R-d-r)/d)) / (2 tanh(R/d))  [Alcubierre top-hat]`  ->  `shape_f`
  live: f(R) = 0.500000
- `theta = beta c df/dr  [York expansion/contraction rate]`  ->  `york_theta`
  live: theta(R, on axis, 0.99c) = -7.42e+08 /s
- `E = -(c^4/8piG) int theta^2 dV over the wall shell`  ->  `warp_energy_integral`
  live: E = -5.656e+47 J
- `KE = (gamma - 1) M c^2,  gamma = 1/sqrt(1-beta^2)`  ->  `kinetic_energy_j`
  live: KE(0.855) = 90.2 YJ
- `P_rad = e sigma A T^4  [Stefan-Boltzmann rejection]`  ->  `radiator_temp_k`
  live: T(waste at 0.99c) = 1439 K
- `spot = 1.22 lambda L / D_emit  [Airy diffraction]`  ->  `beam_spot_m`
  live: spot(0.62 ly) = 14.3 km
- `capture = (A_sail / pi spot^2) clipped to 1`  ->  `beam_capture_frac`
  live: f(0.62 ly) = 0.078
- `F_photon = P_received / c  [destination photon brake]`  ->  `beam_brake_force_n`
  live: F(0.02 ly) = 4.27e+10 N
- `magsail drag ~ rho_ism v^2 A_loop  [Zubrin-Andrews]`  ->  `magsail_drag_n`
  live: F(0.5) = 7.868e+07 N
- `rho_casimir = -pi^2 hbar c / (720 a^4)  [Lamoreaux-verified]`  ->  `casimir_energy_density`
  live: u(10 nm) = -4.334e+04 J/m^3
- `u_throat = -c^4 / (8 pi G b0^2)  [Morris-Thorne]`  ->  `mt_throat_density`
  live: u(12 m) = -3.344e+40 J/m^3
- `Delta_t ~ g L / c^2 over throat  [tidal shear]`  ->  `mt_tidal_g`
  live: 1.272e+14 g at b0=12 m
- `u_QI >= -C hbar / tau^4  [Ford-Roman quantum inequality]`  ->  `ford_roman_bound_j_m3`
  live: u(1 s) = -3.718e-62 J/m^3
- `clock rate = sqrt(1 + 2 Phi/c^2) / gamma  [lapse]`  ->  `mouth_clock_rate`
  live: Earth = 0.999999990
- `dtau/dt_flat = 1 exactly for comoving crew (f = 1 interior)`  ->  `ship_self_dilation`
  live: -4.378e-21 (negligible)
- `CTC onset = separation * |rate diff| / c  [chronology]`  ->  `ctc_onset_s`
  live: 3.156e+10 s at 1 ly, 1e-3 desync

## Reproduce every headline number (one-liners)

Paste any of these into a Python shell next to Warpdrive.py:

- **ship mass**  `>>> W.ship_mass_kg()`  ->  `1081381296.826677`
- **emergent cruise beta**  `>>> W.max_boost_beta()`  ->  `0.8546631240844726`
- **Alcubierre bill, this bubble**  `>>> W.alcubierre_energy_j(1.0, W.DIMS['bubble_r_m'], 0.2)`  ->  `-5.656305286997392e+47`
- **beta=0.99 cruise load**  `>>> W.cruise_load_w(0.99)`  ->  `47087857280.0`
- **radiator temperature at cruise**  `>>> W.radiator_temp_k(W.waste_heat_w(W.cruise_load_w(0.99)))`  ->  `1438.5949467978503`
- **beam power at the ship mid-route**  `>>> W.beam_power_w(0.62 * W.LY)`  ->  `4.99905120166463e+17`
- **photon-brake force at beta=0.5**  `>>> W.beam_brake_force_n(0.5)`  ->  `42696204185.363464`
- **magsail halving time at beta=0.5**  `>>> W.magsail_halving_time_s(0.5)`  ->  `2060181583.596757`
- **Casimir energy onboard**  `>>> W.casimir_onboard_j()`  ->  `-3087573.337649234`
- **walk-through gate tidal load**  `>>> W.mt_tidal_g(12.0, 2.0)`  ->  `127244758570735.3`
- **Sol-Proxima gravitational drift**  `>>> W.voyage_grav_drift_s(W.crossing_time_s(0.5))`  ->  `2.645525353681315`
- **full mission ledger**  `>>> W.report_voyage(0.5)[0].led`  ->  `{'beam_in': 1.5148800000000003e+25, 'plant_out': 4.4377399680000005e+18, 'kinetic': 0.0, 'kinetic_peak': 1.5035299544736518e+25, 'radiated': 7.15764510967742e+18, 'magsail_regen': 9.479730015475056e+21, 'brake_dissipated': 1.4187591651968503e+25, 'fuel_kg': 20334.21906158358, 'am_kg': 0.0, 'ism_particles': 4.036009418398129e+26}`

## The call graph (which functions call which)

AST-extracted intra-model calls -- who actually wires the model together, in one map.

### Hub functions (most intra-model calls)

| Function | Calls | Callees |
|----------|-------|---------|
| `selftest` | 142 | `_annulus_cylinder`, `_box`, `_coil_count`, `_detail_seg`, `_dish`, `_earth_rate`, `_finite`, `_hull_loft`, ...` |
| `_info_sections` | 61 | `_component_info_sections`, `alcubierre_energy_j`, `barrier_analysis`, `beam_brake_force_n`, `beam_brake_time_s`, `beam_capture_frac`, `beam_power_w`, `beam_spot_m`, ...` |
| `_build_ship_parts_impl` | 46 | `_annulus_cylinder`, `_box`, `_coil_arc`, `_deck_plate`, `_dish`, `_finite`, `_hull_loft`, `_mix`, ...` |
| `_build_special_parts_impl` | 24 | `_annulus_cylinder`, `_box`, `_car_loft`, `_finite`, `_mix`, `_pipe_path`, `_rod`, `_solid_cylinder`, ...` |
| `report_portal_test` | 22 | `_print_traversal`, `_rule`, `chain_wormhole_offset`, `cruise_load_w`, `fmt_energy`, `fmt_power`, `fmt_time`, `fusion_fuel_kg`, ...` |
| `_build_portal_parts_impl` | 22 | `_annulus_cylinder`, `_box`, `_finite`, `_mix`, `_mt_funnel`, `_numeric_dims`, `_radial`, `_ring_wire`, ...` |
| `_component_info_sections` | 21 | `_function_registry_lines`, `_runtime_state_lines`, `_spec_key_lines`, `alcubierre_energy_j`, `build_portal_parts`, `build_ship_parts`, `buildability_ledger`, `casimir_onboard_j`, ...` |
| `feasibility_scorecard` | 20 | `alcubierre_energy_j`, `boost_profile`, `casimir_onboard_j`, `cruise_load_w`, `fmt_energy`, `fmt_power`, `fmt_time`, `ford_roman_wall_limit`, ...` |
| `report_spec` | 16 | `_finite`, `_rule`, `check_envelope`, `cruise_load_w`, `flat_interior_r`, `fmt_energy`, `fmt_mass`, `fmt_power`, ...` |
| `portal_summary` | 15 | `casimir_onboard_j`, `equiv_mass_kg`, `ford_roman_bound_j_m3`, `ford_roman_max_throat_tau`, `mmp_summary`, `mt_exotic_energy_j`, `mt_flare_out`, `mt_min_throat_m`, ...` |

### Leaves (64 functions that call nothing internal -- pure boundaries)

`_detail_seg`, `_earth_rate`, `_envelope_points`, `_finite`, `_grp`, `_numeric_dims`, `_prep_mesh`, `_real`, `_rule`, `_sech2`, `_tilt_z`, `_torus_surface`, `_trender`, `_xform`, `beam_spot_m`, `car_fault_effects`, `car_mass_budget`, `car_ops_ledger`, `car_trigger_v`, `casimir_energy_density`, `chain_wormhole_offset`, `clamp`, `crossing_time_s`, `cruise_load_w`, `ctc_onset_s`, `energy_conditions`, `equiv_mass_kg`, `flat_interior_r`, `ford_roman_bound_j_m3`, `ford_roman_max_throat_tau`, `ford_roman_wall_limit`, `fusion_fuel_kg`, `gott_pair_offset`, `horizon_locked`, `ism_particles_swept`, `kerr_ctc_offset`, `magsail_area_m2`, `mmp_extremal_charge_c`, `mmp_tidal_mass_kg`, `mmp_traversal_time_s`, `mt_embedding_z`, `mt_exotic_energy_j`, `mt_min_throat_m`, `mt_proper_length`, `mt_redshift_phi`, `mt_shape_b`, `mt_shape_b_prime`, `mt_throat_density`, `mt_tidal_g`, `mt_traversal_time_s`, `nested_wormhole_offset`, `plant_electric_w`, `quantum_teleport_facts`, `radiator_area_m2`, `radiator_required_m2`, `rot_x`, `rot_y`, `rot_z`, `smes_store_j`, `tipler_cylinder_offset`, `visser_shell_mass_kg`, `waste_heat_w`, `wrap_plain`, `wrap_text`

### Reverse map: the most-relied-upon primitives

| Primitive | Called by N functions |
|-----------|----------------------|
| `_finite` | 53 |
| `_real` | 46 |
| `fmt_energy` | 19 |
| `casimir_onboard_j` | 15 |
| `ship_mass_kg` | 15 |
| `fmt_time` | 13 |
| `fmt_mass` | 13 |
| `cruise_load_w` | 12 |
| `max_boost_beta` | 12 |
| `alcubierre_energy_j` | 11 |
| `orders_of_magnitude` | 11 |
| `_detail_seg` | 10 |

## The knobs (every parameter default, introspected)

Every optional argument in the public API with its declared default -- `None` means 'read the live spec value', a number is a hard-coded modelling choice documented here so it cannot hide.

| Function | Parameter | Default |
|----------|-----------|---------|
| `alcubierre_energy_j` | `R` | `None` |
| `alcubierre_energy_j` | `delta` | `None` |
| `bar` | `mark` | `None` |
| `bar` | `lo` | `None` |
| `bar` | `hi` | `None` |
| `beam_brake_time_s` | `mass_kg` | `None` |
| `boost_profile` | `mass_kg` | `None` |
| `build_portal_parts` | `detail` | `1.0` |
| `build_ship_parts` | `detail` | `1.0` |
| `build_special_parts` | `detail` | `1.0` |
| `car_mph_step` | `cell_k` | `295.0` |
| `car_mph_step` | `armed` | `True` |
| `car_thermal_step` | `louver_eff` | `1.0` |
| `car_transit` | `lat_deg` | `34.05` |
| `car_transit` | `lon_deg` | `-118.24` |
| `check_envelope` | `delta` | `None` |
| `chip` | `col_on` | `None` |
| `clamp` | `lo` | `0.0` |
| `clamp` | `hi` | `1.0` |
| `contrast_text` | `light` | `(230, 236, 245)` |
| `contrast_text` | `dark` | `(10, 14, 20)` |
| `cruise_load_w` | `bubble_on` | `1.0` |
| `ctc_by_gravity_well` | `mouth_sep_m` | `None` |
| `draw_bubble_glow` | `col` | `None` |
| `draw_bubble_glow` | `pulse_phase` | `0.0` |
| `draw_vignette` | `strength` | `0.22` |
| `energy_density` | `R` | `None` |
| `energy_density` | `delta` | `None` |
| `flat_interior_r` | `delta` | `None` |
| `flat_interior_r` | `R` | `None` |
| `honesty_audit` | `verbose` | `True` |
| `ism_blast_energy_j` | `R` | `None` |
| `ism_particles_swept` | `R` | `None` |
| `kerr_ctc_offset` | `n_orbits` | `1` |
| `kinetic_energy_j` | `mass_kg` | `None` |
| `lapse_static` | `R` | `None` |
| `lapse_static` | `delta` | `None` |
| `log_bar_x` | `lo_exp` | `0.0` |
| `log_bar_x` | `hi_exp` | `80.0` |
| `magsail_decel_time_s` | `mass_kg` | `None` |
| `magsail_decel_time_s` | `beta_final` | `None` |
| `magsail_halving_time_s` | `mass_kg` | `None` |
| `main` | `argv` | `None` |
| `max_boost_beta` | `mass_kg` | `None` |
| `max_boost_beta` | `lo` | `0.02` |
| `max_boost_beta` | `hi` | `0.99` |
| `max_time_displacement` | `elapsed_s` | `3155760000.0` |
| `max_time_displacement` | `mouth_sep_m` | `None` |
| `max_time_displacement` | `phi_over_c2` | `-0.45` |
| `max_time_displacement` | `beta` | `0.999` |
| `max_time_displacement` | `n_wormholes` | `10` |
| `max_time_displacement` | `tipler_L_m` | `None` |
| `max_time_displacement` | `tipler_R_m` | `1.0` |
| `max_time_displacement` | `tipler_omega_rads` | `1.0` |
| `max_time_displacement` | `gott_mu_kg_m` | `1e+21` |
| `max_time_displacement` | `gott_D_m` | `9460730472580800.0` |
| `max_time_displacement` | `kerr_M_kg` | `1.98847e+31` |
| `max_time_displacement` | `kerr_r_m` | `None` |
| `max_time_displacement` | `kerr_a_m` | `None` |
| `mmp_summary` | `g_limit` | `1.0` |
| `mmp_summary` | `body_m` | `2.0` |
| `mmp_tidal_mass_kg` | `g_limit` | `1.0` |
| `mmp_tidal_mass_kg` | `body_m` | `2.0` |
| `mouth_clock_rate` | `phi_over_c2` | `0.0` |
| `mouth_clock_rate` | `beta` | `0.0` |
| `mt_exotic_energy_j` | `shell_factor` | `1.0` |
| `mt_min_throat_m` | `g_limit` | `1.0` |
| `mt_min_throat_m` | `body_m` | `2.0` |
| `mt_proper_length` | `r_far` | `None` |
| `mt_tidal_g` | `body_m` | `2.0` |
| `mt_tidal_profile` | `body_m` | `2.0` |
| `mt_traversal_time_s` | `v_ms` | `10.0` |
| `mt_traversal_time_s` | `length_factor` | `4.0` |
| `multijump_breakeven_s` | `overhead_s` | `None` |
| `multijump_breakeven_s` | `b0_m` | `None` |
| `multijump_plan` | `direction` | `'backward'` |
| `multijump_plan` | `overhead_s` | `None` |
| `multijump_plan` | `fuel_start_kg` | `None` |
| `multijump_plan` | `b0_m` | `None` |
| `panel` | `alpha` | `214` |
| `portal_cycle_s` | `overhead_s` | `None` |
| `portal_cycle_s` | `b0_m` | `None` |
| `portal_summary` | `b0` | `None` |
| `portal_traversal` | `mouth_a_phi_c2` | `0.0` |
| `portal_traversal` | `mouth_a_beta` | `0.0` |
| `portal_traversal` | `mouth_b_phi_c2` | `0.0` |
| `portal_traversal` | `mouth_b_beta` | `0.0` |
| `portal_traversal` | `mouth_sep_m` | `None` |
| `portal_traversal` | `elapsed_s` | `0.0` |
| `portal_traversal` | `payload` | `'person'` |
| `portal_traversal` | `payload_size_m` | `2.0` |
| `portal_traversal` | `payload_speed_ms` | `10.0` |
| `project` | `pan` | `(0.0, 0.0)` |
| `radiator_required_m2` | `t_k` | `None` |
| `report_voyage` | `beta` | `0.5` |
| `report_voyage` | `dest_array` | `True` |
| `road_frame` | `lat_deg` | `34.05` |
| `road_frame` | `lon_deg` | `-118.24` |
| `road_inertial_speed` | `lat_deg` | `34.05` |
| `road_solar_hour` | `lon_deg` | `-118.24` |
| `shape_df` | `R` | `None` |
| `shape_df` | `delta` | `None` |
| `shape_df_shifted` | `R` | `None` |
| `shape_df_shifted` | `delta` | `None` |
| `shape_f` | `R` | `None` |
| `shape_f` | `delta` | `None` |
| `text_shadow` | `shadow` | `(0, 0, 0)` |
| `text_shadow` | `offset` | `(1, 1)` |
| `tipler_cylinder_offset` | `M_kg` | `None` |
| `visser_summary` | `a_m` | `None` |
| `visser_summary` | `M_kg` | `None` |
| `voyage_grav_drift_s` | `x_start` | `0.0` |
| `voyage_grav_drift_s` | `x_end` | `None` |
| `wall_tidal_gradient` | `R` | `None` |
| `wall_tidal_gradient` | `delta` | `None` |
| `warp_energy_integral` | `R` | `None` |
| `warp_energy_integral` | `delta` | `None` |
| `warp_energy_integral` | `samples` | `4000` |
| `york_theta` | `R` | `None` |
| `york_theta` | `delta` | `None` |

120 defaulted parameters across the API.

## Dict-return schemas (every structured return)

Every public function that returns a dict, with the full key set extracted from the `return {...}` literals in its source.

### `check_envelope` -- 6 keys

`ok`, `part`, `reach_m`, `limit_m`, `margin_m`, `verdict`

### `casimir_cassette` -- 5 keys

`plates`, `gap_volume_m3`, `rho_j_m3`, `energy_j`, `plate_area_m2`

### `energy_conditions` -- 12 keys

`NEC`, `WEC`, `DEC`, `SEC`, `class`, `note`, `NEC`, `WEC`, `DEC`, `SEC`, `class`, `note`

### `barrier_analysis` -- 8 keys

`wall_tidal`, `superluminal_nec`, `negative_energy`, `steering`, `thermal`, `ford_roman_wall`, `qi_throat`, `ctc`

### `boost_profile` -- 25 keys

`ok`, `energy_j`, `delivered_j`, `time_s`, `range_m`, `final_beta`, `reason`, `ok`, `reason`, `energy_j`, `time_s`, `range_m`, `delivered_j`, `ok`, `reason`, `energy_j`, `time_s`, `range_m`, `delivered_j`, `ok`, `reason`, `energy_j`, `time_s`, `range_m`, `delivered_j`

### `clock_ledger` -- 4 keys

`rates`, `drift_vs_earth_s`, `grav_rate_here`, `earth_rate`

### `mt_flare_out` -- 12 keys

`r0`, `b_at_r0`, `b_prime_at_r0`, `throat_ok`, `flare_out`, `satisfied`, `r0`, `b_at_r0`, `b_prime_at_r0`, `throat_ok`, `flare_out`, `satisfied`

### `mmp_summary` -- 8 keys

`M_kg`, `M_msun`, `Q_ext_c`, `r_s_m`, `traversal_s`, `casimir_energy_j`, `monopoles_observed`, `verdict`

### `visser_summary` -- 7 keys

`a_m`, `M_kg`, `r_s_m`, `shell_mass_kg`, `shell_energy_j`, `outside_horizon`, `tidal_g`

### `ctc_by_warp_transport` -- 3 keys

`warp_rate_diff`, `rocket_rate_diff`, `verdict`

### `ctc_by_gravity_well` -- 4 keys

`rate_diff`, `onset_s`, `rate_diff`, `onset_s`

### `quantum_teleport_facts` -- 7 keys

`state_bits`, `seconds`, `years`, `universe_ages`, `record_km`, `ftl`, `destroys_original`

### `multijump_plan` -- 36 keys

`direction`, `cycles`, `elapsed_s`, `rate_diff`, `mouth_sep_m`, `beta`, `cycle_s`, `breakeven_s`, `ctc_onset_s`, `final_coord_s`, `cum_displacement_s`, `cum_years`, `max_backward_s`, `fuel_burnt_kg`, `fuel_scooped_kg`, `gas_scooped_kg`, `net_fuel_kg`, `fuel_out_at_cycle`, `fuel_sustainable`, `load_w`, `energy_per_cycle_j`, `exotic_j_per_hop`, `exotic_j_total`, `rows`, `direction`, `cycle_s`, `rows`, `breakeven_s`, `fuel_out_at_cycle`, `nan_input`, `direction`, `cycle_s`, `rows`, `breakeven_s`, `fuel_out_at_cycle`, `nan_input`

### `portal_summary` -- 22 keys

`b0_m`, `density_j_m3`, `energy_j`, `mass_kg`, `tidal_g`, `safe_b0_m`, `safe_energy_j`, `safe_mass_kg`, `traverse_s`, `casimir_shortfall_orders`, `safe_shortfall_orders`, `flare_out`, `proper_length_m`, `tidal_at_2b0_g`, `tidal_at_4b0_g`, `qi_hold_s`, `qi_traversal_ratio`, `qi_bound_1s_j_m3`, `qi_shortfall_orders`, `mmp`, `visser`, `visser_shortfall_orders`

### `portal_traversal` -- 29 keys

`mouth_sep_m`, `mouth_sep_ly`, `rate_a`, `rate_b`, `rate_diff`, `elapsed_s`, `offset_s`, `arrival_offset_s`, `light_time_s`, `ctc`, `ctc_margin_s`, `onset_s`, `payload`, `payload_size_m`, `tidal_g`, `min_b0_m`, `survives_tidal`, `b0_m`, `traverse_s`, `qi_hold_s`, `throat_open`, `exotic_j`, `casimir_j`, `shortfall_orders`, `tidal_verdict`, `qi_verdict`, `when_verdict`, `overall`, `can_send`

### `car_power_budget` -- 3 keys

`loads_w`, `supply_w`, `margin_w`

### `car_fault_effects` -- 3 keys

`smes_quench`, `louver_eff`, `nav_lost`

### `car_part_mass` -- 18 keys

`body`, `wheels`, `conduits`, `reactor`, `smes`, `traps`, `casimir`, `louvers`, `rectenna`, `deflector`, `hoops`, `fluxcap`, `bubble`, `magsail`, `cryo`, `nav`, `trail`, `road`

### `car_transit` -- 16 keys

`dep`, `arr`, `delta`, `orbital`, `spin`, `lane_dep`, `lane_arr`, `ok`, `dep`, `arr`, `delta`, `orbital`, `spin`, `lane_dep`, `lane_arr`, `ok`

### `buildability_ledger` -- 2 keys

`ship`, `infra`

## Source line map (where every definition lives)

Every top-level definition in `Warpdrive.py` with its exact line range -- the navigation index for the whole file, AST-derived.

| Lines | Definition | Kind |
|-------|-----------|------|
| 144 | `C_LIGHT` | module constant |
| 145 | `G_NEWTON` | module constant |
| 146 | `HBAR` | module constant |
| 147 | `H_PLANCK` | module constant |
| 148 | `K_B` | module constant |
| 149 | `SIGMA_SB` | module constant |
| 150 | `E_CHARGE` | module constant |
| 151 | `M_P` | module constant |
| 152 | `M_E` | module constant |
| 153 | `MU0` | module constant |
| 154 | `EPS0` | module constant |
| 157 | `C2` | module constant |
| 158 | `C4_OVER_G` | module constant |
| 164 | `L_PLANCK` | module constant |
| 165 | `T_PLANCK` | module constant |
| 166 | `M_PLANCK` | module constant |
| 167 | `E_PLANCK` | module constant |
| 170 | `M_SUN` | module constant |
| 171 | `L_SUN` | module constant |
| 172 | `M_JUPITER` | module constant |
| 173 | `M_EARTH` | module constant |
| 174 | `AU` | module constant |
| 175 | `LY` | module constant |
| 176 | `YR` | module constant |
| 177 | `DAY` | module constant |
| 178 | `M_MILKY_WAY` | module constant |
| 179 | `M_UNIVERSE_BARYON` | module constant |
| 182 | `PROXIMA_LY` | module constant |
| 183 | `PROXIMA_M` | module constant |
| 186 | `ISM_N_M3` | module constant |
| 187 | `ISM_DUST_KG_M3` | module constant |
| 329 | `SCALE_S` | module constant |
| 332-342 | `_Dims` | class |
| 345-351 | `_numeric_dims` | function |
| 354 | `DIMS` | module constant |
| 562-576 | `flat_interior_r` | function |
| 579-598 | `_envelope_points` | function |
| 601-621 | `check_envelope` | function |
| 629 | `SHIP_LEN_M` | module constant |
| 634 | `SHIP_SPAN_M` | module constant |
| 643 | `PLANT` | module constant |
| 666 | `DRIVE` | module constant |
| 679 | `SHELL_STRESS_TAU` | module constant |
| 685 | `LADDER` | module constant |
| 705 | `BG_TOP` | module constant |
| 706 | `BG_BOT` | module constant |
| 707 | `C_HULL` | module constant |
| 708 | `C_HULL_DARK` | module constant |
| 709 | `C_RING` | module constant |
| 710 | `C_RING_HOT` | module constant |
| 711 | `C_COIL` | module constant |
| 712 | `C_COIL_LIVE` | module constant |
| 713 | `C_CASIMIR` | module constant |
| 714 | `C_REACTOR` | module constant |
| 715 | `C_ANTIMAT` | module constant |
| 716 | `C_SMES` | module constant |
| 717 | `C_RADIATOR` | module constant |
| 718 | `C_RAD_HOT` | module constant |
| 719 | `C_CRYO` | module constant |
| 720 | `C_PYLON` | module constant |
| 721 | `C_DEFLECT` | module constant |
| 722 | `C_RCS` | module constant |
| 723 | `C_COLLECT` | module constant |
| 724 | `C_BUBBLE` | module constant |
| 725 | `C_EXPAND` | module constant |
| 726 | `C_CONTRACT` | module constant |
| 727 | `C_TEXT` | module constant |
| 728 | `C_TEXT_DIM` | module constant |
| 729 | `C_ACCENT` | module constant |
| 730 | `C_GOOD` | module constant |
| 731 | `C_WARN` | module constant |
| 732 | `C_BAD` | module constant |
| 733 | `C_EXOTIC` | module constant |
| 734 | `C_PANEL` | module constant |
| 735 | `C_PANEL_HI` | module constant |
| 736 | `C_PANEL_BORDER` | module constant |
| 737 | `C_STAR` | module constant |
| 738 | `C_GRID` | module constant |
| 739 | `C_RIM` | module constant |
| 760 | `VISUAL_DETAIL` | module constant |
| 763-765 | `rot_x` | function |
| 768-770 | `rot_y` | function |
| 773-775 | `rot_z` | function |
| 778-828 | `Mesh` | class |
| 831-886 | `_prep_mesh` | function |
| 889-979 | `_prep_part` | function |
| 982-1078 | `_prep_global` | function |
| 1083 | `_SEG_FLOOR` | module constant |
| 1084 | `_PCHUNK` | module constant |
| 1087-1093 | `_detail_seg` | function |
| 1096-1101 | `_coil_count` | function |
| 1104-1112 | `_finite` | function |
| 1115-1134 | `_solid_cylinder` | function |
| 1137-1161 | `_annulus_cylinder` | function |
| 1164-1199 | `_coil_arc` | function |
| 1202-1251 | `_deck_plate` | function |
| 1254-1264 | `_box` | function |
| 1267-1288 | `_sphere` | function |
| 1291-1320 | `_torus` | function |
| 1323-1343 | `_dish` | function |
| 1346-1385 | `_hull_loft` | function |
| 1388-1402 | `_ring_wire` | function |
| 1405-1437 | `_smooth_sections` | function |
| 1440-1459 | `Part` | class |
| 1462-1468 | `_grp` | function |
| 1471-1490 | `_place` | function |
| 1493-1499 | `_mix` | function |
| 1502-1508 | `_rgb` | function |
| 1511-1519 | `_xy` | function |
| 1522-1549 | `_label` | function |
| 1552-2591 | `ShipRenderer` | class |
| 2612-2615 | `clamp` | function |
| 2618-2626 | `_sech2` | function |
| 2629-2640 | `shape_f` | function |
| 2643-2655 | `shape_df` | function |
| 2658-2676 | `shape_df_shifted` | function |
| 2679-2694 | `york_theta` | function |
| 2697-2717 | `energy_density` | function |
| 2720-2774 | `warp_energy_integral` | function |
| 2777-2795 | `alcubierre_energy_j` | function |
| 2798-2802 | `equiv_mass_kg` | function |
| 2805-2830 | `wall_tidal_gradient` | function |
| 2833-2845 | `ford_roman_wall_limit` | function |
| 2850-2859 | `casimir_energy_density` | function |
| 2862-2875 | `casimir_cassette` | function |
| 2878-2883 | `casimir_onboard_j` | function |
| 2888-2906 | `energy_conditions` | function |
| 2909-2917 | `horizon_locked` | function |
| 2926-3052 | `barrier_analysis` | function |
| 3055-3085 | `barrier_scorecard` | function |
| 3092-3093 | `_torus_surface` | function |
| 3096-3155 | `mass_budget` | function |
| 3158-3159 | `ship_mass_kg` | function |
| 3166-3171 | `lorentz_gamma` | function |
| 3174-3185 | `kinetic_energy_j` | function |
| 3192-3200 | `smes_store_j` | function |
| 3203-3205 | `plant_electric_w` | function |
| 3208-3221 | `cruise_load_w` | function |
| 3224-3232 | `waste_heat_w` | function |
| 3235-3237 | `radiator_area_m2` | function |
| 3241-3252 | `radiator_temp_k` | function |
| 3255-3264 | `radiator_required_m2` | function |
| 3267-3276 | `fusion_fuel_kg` | function |
| 3279-3294 | `beam_spot_m` | function |
| 3297-3303 | `beam_capture_frac` | function |
| 3306-3307 | `beam_power_w` | function |
| 3310-3354 | `boost_profile` | function |
| 3357-3385 | `max_boost_beta` | function |
| 3390-3391 | `magsail_area_m2` | function |
| 3394-3406 | `magsail_drag_n` | function |
| 3409-3420 | `magsail_halving_time_s` | function |
| 3423-3447 | `magsail_decel_time_s` | function |
| 3450-3465 | `beam_brake_force_n` | function |
| 3468-3474 | `beam_brake_time_s` | function |
| 3479-3486 | `ism_particles_swept` | function |
| 3489-3497 | `ism_blast_energy_j` | function |
| 3502-3514 | `rocket_proper_time_s` | function |
| 3517-3522 | `crossing_time_s` | function |
| 3527-3534 | `_real` | function |
| 3537-3559 | `_args_real` | function |
| 3562-3576 | `fmt_energy` | function |
| 3579-3595 | `fmt_mass` | function |
| 3598-3613 | `fmt_time` | function |
| 3616-3625 | `fmt_dist` | function |
| 3628-3635 | `fmt_power` | function |
| 3638-3646 | `orders_of_magnitude` | function |
| 3673-3690 | `lapse_static` | function |
| 3693-3698 | `static_observer_exists` | function |
| 3709 | `WELLS` | module constant |
| 3715 | `GALACTIC_PHI_C2` | module constant |
| 3721-3732 | `grav_potential_at` | function |
| 3735-3746 | `grav_rate` | function |
| 3749 | `EARTH_ORBIT_RATE` | module constant |
| 3752-3757 | `_earth_rate` | function |
| 3760-3774 | `ship_self_dilation` | function |
| 3777-3797 | `clock_ledger` | function |
| 3800-3813 | `voyage_grav_drift_s` | function |
| 3842-3852 | `mt_embedding_z` | function |
| 3855-3865 | `mt_throat_density` | function |
| 3868-3883 | `mt_exotic_energy_j` | function |
| 3886-3900 | `mt_tidal_g` | function |
| 3903-3915 | `mt_min_throat_m` | function |
| 3918-3922 | `mt_traversal_time_s` | function |
| 3943-3955 | `mt_shape_b` | function |
| 3958-3962 | `mt_shape_b_prime` | function |
| 3965-3974 | `mt_redshift_phi` | function |
| 3977-3997 | `mt_flare_out` | function |
| 4000-4016 | `mt_tidal_profile` | function |
| 4019-4035 | `mt_proper_length` | function |
| 4050-4068 | `ford_roman_bound_j_m3` | function |
| 4071-4085 | `ford_roman_max_throat_tau` | function |
| 4110-4117 | `mmp_extremal_charge_c` | function |
| 4120-4143 | `mmp_tidal_mass_kg` | function |
| 4146-4160 | `mmp_traversal_time_s` | function |
| 4163-4189 | `mmp_summary` | function |
| 4201-4219 | `visser_shell_mass_kg` | function |
| 4222-4224 | `visser_shell_energy_j` | function |
| 4227-4249 | `visser_summary` | function |
| 4254-4275 | `ctc_onset_s` | function |
| 4278-4290 | `ctc_by_warp_transport` | function |
| 4293-4300 | `ctc_by_gravity_well` | function |
| 4305 | `QT` | module constant |
| 4314-4329 | `quantum_teleport_facts` | function |
| 4339-4354 | `chain_wormhole_offset` | function |
| 4357-4367 | `nested_wormhole_offset` | function |
| 4370-4391 | `tipler_cylinder_offset` | function |
| 4394-4412 | `gott_pair_offset` | function |
| 4415-4439 | `kerr_ctc_offset` | function |
| 4442-4487 | `max_time_displacement` | function |
| 4512 | `MULTIJUMP` | module constant |
| 4526-4535 | `ism_scoop_gas_kg_s` | function |
| 4538-4562 | `ism_d3he_yield_kg_s` | function |
| 4565-4578 | `portal_cycle_s` | function |
| 4581-4592 | `multijump_breakeven_s` | function |
| 4595-4715 | `multijump_plan` | function |
| 4718-4769 | `portal_summary` | function |
| 4803-4828 | `mouth_clock_rate` | function |
| 4831-4844 | `mouth_time_offset_s` | function |
| 4847-4862 | `ctc_exists` | function |
| 4865-5030 | `portal_traversal` | function |
| 5033-5478 | `report_portal_test` | function |
| 5481-5510 | `_print_traversal` | function |
| 5519-5540 | `_xform` | function |
| 5543-5546 | `_tangential` | function |
| 5549-5551 | `_radial` | function |
| 5554-5567 | `build_ship_parts` | function |
| 5570-6278 | `_build_ship_parts_impl` | function |
| 6286-6314 | `_mt_funnel` | function |
| 6317-6329 | `build_portal_parts` | function |
| 6332-6466 | `_build_portal_parts_impl` | function |
| 6480 | `CAR_MASS_KG` | module constant |
| 6481 | `CAR_BUBBLE_R` | module constant |
| 6482 | `CAR_WALL_M` | module constant |
| 6483 | `CAR_TRIGGER_MPH` | module constant |
| 6484 | `CAR_MPH_M_S` | module constant |
| 6485 | `CAR_CASIMIR_STRIPS` | module constant |
| 6486 | `CAR_CASIMIR_PLATE` | module constant |
| 6487 | `CAR_CASIMIR_DEPTH` | module constant |
| 6488 | `CAR_CASIMIR_STACK` | module constant |
| 6490 | `SPECIAL_SECTION_KEYS` | module constant |
| 6492 | `CAR_MODEL_DETAIL` | module constant |
| 6497-6499 | `car_trigger_v` | function |
| 6502-6515 | `car_casimir_j` | function |
| 6523 | `AU_M` | module constant |
| 6524 | `YEAR_S` | module constant |
| 6525 | `SIDEREAL_DAY_S` | module constant |
| 6526 | `EARTH_R_M` | module constant |
| 6527 | `EARTH_ECC` | module constant |
| 6528 | `EARTH_OBLIQUITY` | module constant |
| 6529 | `ROAD_LAT_DEG` | module constant |
| 6530 | `ROAD_LON_DEG` | module constant |
| 6533-6543 | `earth_helio_pos` | function |
| 6546-6562 | `earth_surface_offset` | function |
| 6565-6571 | `_tilt_z` | function |
| 6574-6593 | `road_frame` | function |
| 6596-6602 | `road_inertial_speed` | function |
| 6605-6663 | `car_mass_budget` | function |
| 6666 | `CAR_CELL_W` | module constant |
| 6669-6711 | `car_ops_ledger` | function |
| 6714-6721 | `car_power_budget` | function |
| 6724 | `CAR_LouverA_M2` | module constant |
| 6725 | `CAR_Louver_EPS` | module constant |
| 6726 | `CAR_THERMAL_JK` | module constant |
| 6727 | `CAR_TEMP_LIMIT_K` | module constant |
| 6730-6766 | `car_thermal_step` | function |
| 6769-6779 | `car_fault_effects` | function |
| 6782-6807 | `car_mph_step` | function |
| 6810-6841 | `car_part_mass` | function |
| 6844-6855 | `road_solar_hour` | function |
| 6858-6877 | `car_transit` | function |
| 6880-6937 | `_car_loft` | function |
| 6940-6963 | `_rod` | function |
| 6966-7012 | `_pipe_path` | function |
| 7015-7031 | `_wire_ellipsoid` | function |
| 7034-7050 | `build_special_parts` | function |
| 7053-9513 | `_build_special_parts_impl` | function |
| 9520-9751 | `WarpCore` | class |
| 9759 | `VOYAGE_WARP` | module constant |
| 9760 | `VOYAGE_WARP_LABEL` | module constant |
| 9763 | `PHASES` | module constant |
| 9765 | `PHASE_NOTE` | module constant |
| 9774-10076 | `Voyage` | class |
| 10086-10218 | `honesty_audit` | function |
| 10225-10228 | `_rule` | function |
| 10231-10352 | `report_spec` | function |
| 10355-10415 | `report_metric` | function |
| 10418-10448 | `report_ladder` | function |
| 10451-10677 | `buildability_ledger` | function |
| 10680-10767 | `operations_ledger` | function |
| 10770-10857 | `feasibility_scorecard` | function |
| 10860-10927 | `report_feasibility` | function |
| 10930-10941 | `wrap_plain` | function |
| 10944-10992 | `report_dilation` | function |
| 10995-11158 | `report_portal` | function |
| 11161-11218 | `report_voyage` | function |
| 11225-13441 | `selftest` | function |
| 13450-14459 | `_component_info_sections` | function |
| 14462-14564 | `_function_registry_lines` | function |
| 14567-14656 | `_runtime_state_lines` | function |
| 14659-14703 | `_spec_key_lines` | function |
| 14706-15924 | `_info_sections` | function |
| 15927 | `INFO_SECTIONS` | module constant |
| 15930-15934 | `info_sections` | function |
| 15941-15955 | `vgradient` | function |
| 15958-15962 | `_luminance` | function |
| 15965-15972 | `contrast_text` | function |
| 15975-15997 | `text_shadow` | function |
| 16000 | `_TEXTCACHE` | module constant |
| 16003-16013 | `_trender` | function |
| 16016-16068 | `panel` | function |
| 16071-16100 | `bar` | function |
| 16103-16117 | `wrap_text` | function |
| 16120-16157 | `chip` | function |
| 16160-16197 | `project` | function |
| 16200-16253 | `MetricCam` | class |
| 16256-16366 | `Starfield` | class |
| 16369-16415 | `draw_bubble_glow` | function |
| 16418-16425 | `log_bar_x` | function |
| 16428-16466 | `draw_vignette` | function |
| 16475 | `SECTION_KEYS` | module constant |
| 16480-18488 | `App` | class |
| 18495-18548 | `print_startup_banner` | function |
| 18556 | `_NUMERIC_HELPERS` | module constant |
| 18589-18675 | `main` | function |

## Source anatomy (what the file is made of)

| Line class | Count | Share |
|------------|-------|-------|
| code | 14375 | 77.0% |
| docstring | 1579 | 8.5% |
| comment | 1556 | 8.3% |
| blank | 1169 | 6.3% |

`Warpdrive.py` = 18679 lines total.

## The six tabs, drawn (per-tab render pipelines)

What each viewer tab actually invokes, AST-extracted from the `App` draw methods -- the real render order, not a description of it.

### SHIP

- `draw_ship` (13 lines) -> `Rect`, `draw`, `render`, `draw_view_tabs`, `draw_ship_panel`, `draw_spec_card`, `get_pos`, `clamp`
- `draw_ship_panel` (59 lines) -> `panel`, `blit`, `check_envelope`, `render`, `alcubierre_energy_j`, `fmt_mass`, `fmt_energy`, `fmt_time`, `ship_mass_kg`, `smes_store_j`, `casimir_onboard_j`, `max_boost_beta`, `crossing_time_s`, `get_width` ...
- `draw_spec_card` (3 lines) -> `active_part`, `_spec_card`

### METRIC

- `draw_metric` (129 lines) -> `Rect`, `draw`, `sorted`, `linspace`, `len`, `project`, `range`, `sort`, `get_clip`, `set_clip`, `Surface`, `blit`, `line`, `circle` ...
- `draw_profiles` (55 lines) -> `enumerate`, `_real`, `panel`, `blit`, `rect`, `line`, `range`, `render`, `len`, `lines`, `shape_f`, `shape_df`, `energy_density`, `_finite` ...
- `draw_metric_panel` (71 lines) -> `panel`, `blit`, `alcubierre_energy_j`, `wall_tidal_gradient`, `energy_conditions`, `wrap_text`, `check_envelope`, `_real`, `render`, `ford_roman_wall_limit`, `Rect`, `rect`, `fmt_energy`, `fmt_mass` ...

### DILATION

- `draw_dilation` (74 lines) -> `Rect`, `draw`, `get_clip`, `set_clip`, `lapse_static`, `max`, `Surface`, `circle`, `blit`, `text_shadow`, `enumerate`, `draw_dilation_graphs`, `draw_clock_panel`, `min` ...
- `draw_dilation_graphs` (62 lines) -> `panel`, `blit`, `rect`, `range`, `lines`, `_real`, `_finite`, `render`, `lapse_static`, `len`, `line`, `append`, `min`, `grav_rate` ...
- `draw_clock_panel` (70 lines) -> `clock_ledger`, `panel`, `blit`, `items`, `render`, `_real`, `wrap_text`, `startswith`, `_finite`, `max`, `fmt_time`, `ship_self_dilation`, `get_width`, `voyage_grav_drift_s` ...

### PORTAL

- `draw_portal` (14 lines) -> `Rect`, `draw`, `render`, `draw_view_tabs`, `draw_portal_panel`, `active_part`, `_spec_card`, `get_pos`
- `draw_portal_panel` (127 lines) -> `portal_summary`, `panel`, `blit`, `ctc_by_gravity_well`, `ctc_by_warp_transport`, `quantum_teleport_facts`, `render`, `wrap_text`, `max`, `fmt_energy`, `fmt_mass`, `fmt_time`, `casimir_onboard_j`, `isupper` ...

### FLIGHT

- `draw_flight` (66 lines) -> `Rect`, `draw`, `draw_bubble_glow`, `render`, `draw_flight_hud`, `draw_flight_controls`, `_finite`, `Surface`, `min`, `range`, `blit`, `int`, `clamp`, `rect` ...
- `draw_flight_hud` (153 lines) -> `panel`, `blit`, `wrap_text`, `_real`, `bar`, `rocket_proper_time_s`, `enumerate`, `max`, `int`, `render`, `isinstance`, `get`, `float`, `plant_electric_w` ...
- `draw_flight_controls` (51 lines) -> `chip`, `blit`, `helm_locked`, `render`, `int`, `get_width`, `isinstance`, `get`, `clamp`, `len`

### SPECIAL WORKS

- `draw_special` (19 lines) -> `Rect`, `draw`, `render`, `draw_view_tabs`, `draw_special_panel`, `active_part`, `_spec_card`, `min`, `get`, `get_pos`, `clamp`
- `draw_special_panel` (202 lines) -> `panel`, `blit`, `text_shadow`, `get`, `clamp`, `bar`, `alcubierre_energy_j`, `car_casimir_j`, `enumerate`, `_real`, `car_transit`, `circle`, `render`, `startswith` ...

## Every instance attribute (the complete object state)

All `self.*` state per class, AST-extracted: attribute, the method that first assigns it, and its initial value when it's a literal. This is the full runtime memory of every object the twin creates.

### `_Dims` -- 0 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|

### `Mesh` -- 12 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self.coil_index` | `__init__` | `None` |
| `self.color` | `__init__` | `color` |
| `self.faces` | `__init__` | `[f for f in _faces if isinstance(f, (li...` |
| `self.glow` | `__init__` | `glow` |
| `self.group` | `__init__` | `group` |
| `self.hot` | `__init__` | `hot` |
| `self.name` | `__init__` | `name` |
| `self.pivot` | `__init__` | `piv if piv.shape == (3,) and np.isfinit...` |
| `self.spin` | `__init__` | `spin if _finite(spin) else 0.0` |
| `self.tilt` | `__init__` | `tuple(tilt) if isinstance(tilt, (tuple,...` |
| `self.verts` | `__init__` | `np.asarray(verts, dtype=float).reshape(...` |
| `self.wire` | `__init__` | `wire` |

### `Part` -- 8 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self.color` | `__init__` | `color` |
| `self.explode` | `__init__` | `np.asarray(explode, dtype=float).reshap...` |
| `self.key` | `__init__` | `key` |
| `self.meshes` | `__init__` | `meshes` |
| `self.name` | `__init__` | `name` |
| `self.order` | `__init__` | `order` |
| `self.popdir` | `__init__` | `self.explode / n if n > 1e-06 else np.a...` |
| `self.specs` | `__init__` | `specs` |

### `ShipRenderer` -- 32 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self._cache` | `__init__` | `None` |
| `self._cacherect` | `__init__` | `None` |
| `self._clod` | `__init__` | `'hi'` |
| `self._cmarg` | `__init__` | `0` |
| `self._cpan` | `__init__` | `None` |
| `self._csi` | `__init__` | `[]` |
| `self._framekey` | `__init__` | `None` |
| `self._ghi` | `__init__` | `None` |
| `self._glo` | `__init__` | `None` |
| `self._home` | `__init__` | `(home_az, home_el, home_dist)` |
| `self._lo` | `__init__` | `self.parts_builder(0.55)` |
| `self._lpan` | `__init__` | `None` |
| `self._pose` | `__init__` | `None` |
| `self._prog` | `__init__` | `None` |
| `self._spins` | `__init__` | `None` |
| `self.assembled` | `__init__` | `len(self.parts)` |
| `self.az` | `__init__` | `home_az` |
| `self.dist` | `__init__` | `home_dist` |
| `self.el` | `__init__` | `home_el` |
| `self.explode_amt` | `__init__` | `0.0` |
| `self.hidden` | `__init__` | `set()` |
| `self.hover_spread` | `__init__` | `0.0` |
| `self.hovered` | `__init__` | `None` |
| `self.light` | `__init__` | `np.array([0.45, 0.62, 1.0])` |
| `self.pan` | `__init__` | `np.array([0.0, 0.0])` |
| `self.parts` | `__init__` | `parts_builder()` |
| `self.parts_builder` | `__init__` | `parts_builder` |
| `self.pop` | `__init__` | `np.zeros(len(self.parts))` |
| `self.section` | `__init__` | `False` |
| `self.section_keys` | `__init__` | `set(section_keys)` |
| `self.selected` | `__init__` | `None` |
| `self.view` | `__init__` | `'full'` |

### `WarpCore` -- 22 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self.beam_w` | `__init__` | `0.0` |
| `self.beta` | `__init__` | `0.0` |
| `self.beta_cmd` | `__init__` | `0.0` |
| `self.bubble_cmd` | `__init__` | `False` |
| `self.bubble_on` | `__init__` | `0.0` |
| `self.coil_glow` | `__init__` | `np.zeros(_coil_count())` |
| `self.coil_phase` | `__init__` | `0.0` |
| `self.collapse_msg` | `__init__` | `''` |
| `self.collapsed` | `__init__` | `False` |
| `self.exotic_debt_j` | `__init__` | `0.0` |
| `self.exotic_need_j` | `__init__` | `0.0` |
| `self.integrity` | `__init__` | `1.0` |
| `self.led` | `__init__` | `{'beam_in': 0.0, 'plant_out': 0.0, 'kin...` |
| `self.load_w` | `__init__` | `0.0` |
| `self.magsail_deployed` | `__init__` | `False` |
| `self.rad_k` | `__init__` | `290.0` |
| `self.rectenna_deployed` | `__init__` | `False` |
| `self.smes_j` | `__init__` | `0.55 * smes_store_j()` |
| `self.status` | `__init__` | `'COLD'` |
| `self.wall_m` | `__init__` | `DIMS['wall_thick_m']` |
| `self.was_superluminal` | `__init__` | `False` |
| `self.waste_w` | `__init__` | `0.0` |

### `Voyage` -- 15 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self._warned_overshoot` | `__init__` | `False` |
| `self.arrived_at` | `__init__` | `None` |
| `self.dest_array` | `__init__` | `False` |
| `self.f_beam` | `_step` | `beam_brake_force_n(self.remaining_m + 0...` |
| `self.f_magsail` | `_step` | `f` |
| `self.ism_particles` | `__init__` | `0.0` |
| `self.log` | `__init__` | `[]` |
| `self.phase` | `__init__` | `'DOCK'` |
| `self.t_coord` | `__init__` | `0.0` |
| `self.t_earth` | `__init__` | `0.0` |
| `self.t_ship` | `__init__` | `0.0` |
| `self.target_m` | `__init__` | `PROXIMA_M` |
| `self.v_ms` | `__init__` | `0.0` |
| `self.warp_i` | `__init__` | `4` |
| `self.x_m` | `__init__` | `0.0` |

### `MetricCam` -- 8 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self._home` | `__init__` | `(az, el, dist)` |
| `self.dist` | `zoom_at` | `max(120.0, min(2600.0, self.dist * fact...` |
| `self.el` | `orbit` | `max(-1.5, min(1.5, self.el + dy * sens))` |
| `self.hovered` | `__init__` | `None` |
| `self.pan` | `__init__` | `np.array([0.0, 0.0])` |
| `self.section` | `__init__` | `False` |
| `self.selected` | `__init__` | `None` |
| `self.view` | `__init__` | `'full'` |

### `Starfield` -- 5 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self._cache` | `__init__` | `None` |
| `self._cache_key` | `__init__` | `None` |
| `self.cls` | `__init__` | `np.array([np.searchsorted(cum, rv) for ...` |
| `self.mag` | `__init__` | `rng.uniform(0.25, 1.0, size=n)` |
| `self.p` | `__init__` | `rng.uniform(-1.0, 1.0, size=(n, 3))` |

### `App` -- 35 attributes

| Attribute | First set in | Initial value |
|-----------|--------------|---------------|
| `self._chips` | `__init__` | `{}` |
| `self._tbgrad` | `draw_topbar` | `s` |
| `self._test_phase` | `__init__` | `None` |
| `self._test_t` | `__init__` | `0.0` |
| `self.anim` | `__init__` | `0.0` |
| `self.bg` | `__init__` | `None` |
| `self.clock` | `__init__` | `pygame.time.Clock()` |
| `self.core` | `__init__` | `WarpCore()` |
| `self.dragging` | `__init__` | `False` |
| `self.f` | `__init__` | `pygame.font.SysFont(mono, 15)` |
| `self.fb` | `__init__` | `pygame.font.SysFont(mono, 28, bold=True)` |
| `self.fm` | `__init__` | `pygame.font.SysFont(mono, 19, bold=True)` |
| `self.frend` | `__init__` | `ShipRenderer(build_ship_parts, home_az=...` |
| `self.fs` | `__init__` | `pygame.font.SysFont(mono, 12)` |
| `self.ftl_unlock` | `__init__` | `False` |
| `self.info_scroll` | `__init__` | `0` |
| `self.mcam` | `__init__` | `MetricCam()` |
| `self.mode` | `__init__` | `self.MODE_SHIP` |
| `self.msg` | `__init__` | `''` |
| `self.msg_t` | `__init__` | `0.0` |
| `self.panning` | `__init__` | `False` |
| `self.paused` | `__init__` | `False` |
| `self.prend` | `__init__` | `ShipRenderer(build_portal_parts, home_a...` |
| `self.rend` | `__init__` | `ShipRenderer(build_ship_parts, home_az=...` |
| `self.running` | `__init__` | `True` |
| `self.screen` | `__init__` | `pygame.display.set_mode((self.W, self.H...` |
| `self.show_help` | `__init__` | `True` |
| `self.show_info` | `__init__` | `False` |
| `self.show_labels` | `__init__` | `False` |
| `self.show_ladder` | `__init__` | `False` |
| `self.sp` | `__init__` | `{'mph': 0.0, 'auto': False, 'fired': Fa...` |
| `self.srend` | `__init__` | `ShipRenderer(build_special_parts, home_...` |
| `self.stars` | `__init__` | `Starfield()` |
| `self.test_mode` | `__init__` | `False` |
| `self.voy` | `__init__` | `Voyage()` |

## Failure containment map (every try/except and raise)

Where the model catches and what it does instead -- the dynamic complement to the static input-guard inventory.

| Line | Enclosing function | Catches | Falls back to |
|------|--------------------|---------|---------------|
| 755 | `module` | `Exception` | `pygame = None` |
| 849 | `_prep_mesh` | `TypeError` | `return` |
| 1352 | `_hull_loft` | `TypeError` | `return ([], [])` |
| 1407 | `_smooth_sections` | `TypeError` | `return []` |
| 1463 | `_grp` | `(TypeError, AttributeError)` | `pass` |
| 1473 | `_place` | `(ValueError, TypeError)` | `piv = np.zeros(3)` |
| 1482 | `_place` | `(TypeError, AttributeError)` | `pass` |
| 1496 | `_mix` | `(TypeError, ValueError, IndexError, KeyError)` | `return (0, 0, 0)` |
| 1505 | `_rgb` | `(TypeError, ValueError, IndexError, KeyError)` | `return fallback` |
| 1513 | `_xy` | `(TypeError, IndexError, KeyError)` | `return None` |
| 3531 | `_real` | `(TypeError, ValueError)` | `return float('nan')` |
| 5524 | `_xform` | `(ValueError, TypeError)` | `return np.empty((0, 3))` |
| 6505 | `car_casimir_j` | `Exception` | `return float('nan')` |
| 6969 | `_pipe_path` | `(ValueError, TypeError)` | `return ([], [])` |
| 12891 | `selftest` | `ValueError` | `bad_dir = True` |
| 14666 | `_spec_key_lines` | `Exception` | `src_lines = []` |
| 16173 | `project` | `(ValueError, TypeError)` | `pts = np.zeros((0, 3))` |
| 16185 | `project` | `(ValueError, TypeError)` | `pan = np.zeros(2)` |
| 787 | `__init__` | `(ValueError, TypeError)` | `self.verts = np.zeros((0, 3))` |
| 794 | `__init__` | `TypeError` | `_faces = []` |
| 806 | `__init__` | `(ValueError, TypeError)` | `piv = np.zeros(3)` |
| 1451 | `__init__` | `(ValueError, TypeError)` | `self.explode = np.zeros(3)` |
| 1578 | `__init__` | `Exception` | `self._lo = []` |
| 12079 | `selftest` | `Exception` | `_bad_detail_ok = False` |
| 13324 | `selftest` | `Exception` | `_pt_ok = False` |
| 13341 | `selftest` | `Exception` | `_mv = False` |
| 14534 | `_function_registry_lines` | `(TypeError, ValueError)` | `sig = '(...)'` |
| 16169 | `project` | `TypeError` | `pts = []` |
| 1065 | `_prep_global` | `Exception` | `pass` |
| 1585 | `__init__` | `Exception` | `pass` |
| 1763 | `render` | `(TypeError, ValueError, AttributeError)` | `qang = ()` |
| 1773 | `render` | `(TypeError, ValueError)` | `qglow = None` |
| 1925 | `render` | `Exception` | `self._cache = None` |
| 13344 | `selftest` | `SystemExit` | `pass` |
| 13348 | `selftest` | `SystemExit` | `pass` |
| 14514 | `_function_registry_lines` | `(TypeError, ValueError)` | `sig = '(...)'` |
| 16653 | `_chip_click` | `ValueError` | `return` |
| 1902 | `render` | `Exception` | `self._lo = []` |
| 1986 | `render` | `Exception` | `glob = None` |
| 2492 | `_paint` | `Exception` | `pass` |
| 14555 | `_function_registry_lines` | `(TypeError, ValueError)` | `sig = '(...)'` |
| 1832 | `render` | `Exception` | `pass` |
| 2068 | `render` | `(TypeError, ValueError, IndexError)` | `pass` |
| 2247 | `render` | `(TypeError, ValueError, IndexError, OverflowError)` | `g = 0.0` |
| 2398 | `render` | `(TypeError, ValueError, IndexError)` | `pass` |

58 try blocks, 3 explicit `raise` statements -- the model almost never raises into user code; it degrades and reports.

Explicit raises:

- L2750 in `warp_energy_integral`: `ValueError('samples must be a finite count, got %r' % samples)`
- L4616 in `multijump_plan`: `ValueError("direction must be 'backward' or 'forward', got %r" % (direction,))`
- L1641 in `set_view`: `ValueError('unknown view %r' % (mode,))`

## Magic-number inventory (every coefficient that isn't a spec key)

Every numeric literal written inside a function body -- the modelling choices that live outside the spec dictionaries. Sorted by function; trivial sentinels (0, 1, 2, -1) omitted.

| Function | Literals |
|----------|----------|
| `__init__` | 1.02, 1.15, 3, 4, 7, 12, 15, 19, 28, 210, 290, 295, 340, 430, 520, 560, +18 more |
| `_annulus_cylinder` | 40 |
| `_box` | 3, 4, 5, 6, 7 |
| `_build_portal_parts_impl` | 1.1, 1.6, 1.8, 2.2, 4, 6, 7, 8, 9, 13, 26, 30, 40, 46, 56, 60, +12 more |
| `_build_ship_parts_impl` | 1.1, 1.25, 1.4, 1.5, 2.4, 2.6, 2.8, 3, 4, 5, 6, 6.8, 8, 8.5, 9, 9.81, +54 more |
| `_build_special_parts_impl` | 1.01, 1.03, 1.04, 1.05, 1.06, 1.078, 1.08, 1.1, 1.14, 1.15, 1.18, 1.2, 1.24, 1.25, 1.26, 1.28, +290 more |
| `_car_loft` | 3, 4, 8, 0.1, 0.12, 0.16, 0.55 |
| `_chip_click` | 25 |
| `_coil_arc` | 6, 10, 64 |
| `_coil_count` | 4096 |
| `_component_info_sections` | 5, 72, 100, 8.64e+04, 1e+06, 1e+09, 1e+12, 1e+18, 4.184e+18, 0.5, 0.99 |
| `_deck_plate` | 3, 8, 16, 48, 0.12, 0.5 |
| `_detail_seg` | 256 |
| `_dish` | 5, 28, 256, 1e-09 |
| `_emit` | 72 |
| `_function_registry_lines` | 74 |
| `_hull_loft` | 24, 513 |
| `_info_sections` | 4.4, 9.81, 12, 24, 48, 100, 117, 1000, 1.274e+07, 4.184e+12, 1e+15, 1e+24, 1e-15, 1e-08, 0.001, 0.01, +12 more |
| `_integrity` | 2.2, 1e-06, 0.02, 0.1, 0.12, 0.35, 0.9 |
| `_key` | 1.15, 1.6, 4, 10, 12, 60, 130, 295, 0.01, 0.1 |
| `_label` | 3, 5, 6, 7, 8, 9, 10, 16, 60, 120, 190 |
| `_layout` | 0.28, 0.55 |
| `_loft_mean_r` | 401, 0.4, 0.55, 0.75, 0.88 |
| `_luminance` | 255, 0.0722, 0.2126, 0.7152 |
| `_mix` | 3 |
| `_mt_funnel` | 3, 4, 13, 40, 256, 512 |
| `_open` | 0.5 |
| `_paint` | 1.2, 3, 46, 0.02, 0.12, 0.27, 0.4, 0.62, 0.65 |
| `_pipe_path` | 3, 10, 1e-09, 0.95 |
| `_place` | 3 |
| `_prep_global` | 3 |
| `_prep_mesh` | 96 |
| `_prep_part` | 3.5 |
| `_rgb` | 3, 255 |
| `_ring_wire` | 8, 64 |
| `_rod` | 3, 10, 1e-09, 0.98 |
| `_rule` | 78 |
| `_runtime_state_lines` | 74, 0.55 |
| `_sech2` | 350 |
| `_section_cut` | 0.15 |
| `_smooth_sections` | 3, 4, 5, 64, 512, 513, 0.5 |
| `_solid_cylinder` | 32 |
| `_spec_card` | 5, 6, 9, 14, 16, 17, 28, 36, 42, 62, 640 |
| `_spec_key_lines` | 74, 1e+07 |
| `_sphere` | 4, 12, 20 |
| `_star_col` | 255 |
| `_step` | 40, 0.002, 0.3, 0.5, 1 |
| `_test_tick` | 10, 30 |
| `_thermal` | 4, 90 |
| `_toggle_test` | 4 |
| `_torus` | 3, 4, 12, 48, 256, 512 |
| `_torus_surface` | 4 |
| `_trender` | 6000 |
| `_wire_ellipsoid` | 3, 4, 40, 0.18, 0.55 |
| `_xform` | 3 |
| `alcubierre_energy_j` | 12 |
| `auto_step` | 1.05 |
| `bar` | 3, 4, 16 |
| `barrier_analysis` | 1.01, 4, 5, 9.81, 12, 0.01, 0.99 |
| `beam_brake_time_s` | 0.02 |
| `beam_capture_frac` | 1000 |
| `beam_spot_m` | 2.44, 1000, 1e-06 |
| `begin_brake` | 0.02 |
| `boost_profile` | 3, 100, 200, 0.999 |
| `build_portal_parts` | 4, 6 |
| `build_ship_parts` | 4, 6 |
| `build_special_parts` | 4, 6, 64, 0.02 |
| `buildability_ledger` | 12, 35, 100, 500, 1000, 1e+06, 1e+09, 1e-09, 1e-06, 0.5 |
| `car_casimir_j` | 1e-09 |
| `car_fault_effects` | 0.12 |
| `car_mass_budget` | 3, 4, 5, 6, 8, 12, 13.5, 14, 22, 30, 34, 38, 40, 45, 46, 75, +7 more |
| `car_mph_step` | 5, 30, 35, 45, 55, 130, 295 |
| `car_ops_ledger` | 100, 150, 200, 500, 1000, 2000, 3000, 1.2e+04, 3e+04, 0.005 |
| `car_thermal_step` | 4, 10, 120, 295, 6000, 0.25 |
| `car_transit` | 3 |
| `casimir_cassette` | 1e-09 |
| `casimir_energy_density` | 4, 720, 1e-12 |
| `chip` | 3, 6, 7, 9, 10, 14, 20, 40, 80, 230, 255, 0.15 |
| `clock_ledger` | 1 |
| `col_for` | 2.6 |
| `contrast_text` | 10, 14, 20, 0.45 |
| `cruise_load_w` | 1e+06, 0.2, 0.8 |
| `ctc_by_warp_transport` | 1 |
| `draw` | 14, 28, 32, 46, 52, 1.638e+04, 0.02, 0.2 |
| `draw_bubble_glow` | 1.3, 1.4, 1.8, 2.6, 10, 40, 62, 0.02, 0.04, 0.15, 0.3, 0.35, 0.5, 0.55, 0.65 |
| `draw_clock_panel` | 6, 8, 12, 15, 18, 19, 24, 30, 34, 50, 52, 200, 250, 262, 378, 390, +1 more |
| `draw_dilation` | 1.02, 1.1, 1.3, 1.6, 5, 7, 12, 14, 15, 16, 28, 36, 40, 50, 54, 110, +17 more |
| `draw_dilation_graphs` | 1.7, 3, 4, 6, 8, 10, 12, 13, 20, 22, 26, 46, 140, 150, 190, 430, +1 more |
| `draw_flight` | 1.4, 1.5, 2.2, 3, 4, 8, 14, 18, 30, 40, 55, 60, 90, 140, 255, 430, +10 more |
| `draw_flight_controls` | 5, 6, 8, 14, 16, 44, 84, 430 |
| `draw_flight_hud` | 6, 8, 9, 12, 14, 15, 16, 24, 28, 32, 50, 52, 60, 62, 68, 90, +15 more |
| `draw_help` | 8, 12, 14, 18, 28, 34, 58, 60, 176, 470 |
| `draw_info` | 3, 5, 12, 14, 16, 18, 20, 22, 28, 52, 60, 62, 70, 90, 250, 300, +3 more |
| `draw_ladder` | 3, 4, 6, 8, 10, 11, 12, 14, 16, 20, 22, 26, 34, 48, 78, 80, +10 more |
| `draw_metric` | 1.1, 1.6, 1.9, 2.3, 2.6, 3, 4, 5, 6, 7, 9, 12, 14, 15, 16, 20, +22 more |
| `draw_metric_panel` | 4, 6, 7, 8, 9.81, 10, 12, 15, 16, 18, 22, 24, 30, 36, 52, 76, +6 more |
| `draw_portal` | 40, 196, 402, 0.3 |
| `draw_portal_panel` | 3, 6, 8, 12, 14, 17, 24, 30, 32, 50, 52, 138, 150, 168, 188, 268, +8 more |
| `draw_profiles` | 3, 4, 6, 8, 10, 12, 13, 14, 20, 26, 46, 90, 91, 150, 190, 400, +2 more |
| `draw_ship` | 2.2, 40, 372, 600, 1300, 0.5 |
| `draw_ship_panel` | 4, 8, 12, 18, 19, 34, 36, 52, 150, 300, 312, 348, 360, 0.5 |
| `draw_special` | 40, 110, 196, 402, 0.45, 0.5, 0.55 |
| `draw_special_panel` | 1.15, 3, 4, 4.4, 6, 8, 12, 14, 15, 16, 17, 18, 24, 28, 30, 32, +27 more |
| `draw_topbar` | 8, 9, 10, 12, 14, 16, 20, 40, 210, 236, 0.25 |
| `draw_view_tabs` | 4, 8, 14, 18, 42 |
| `draw_vignette` | 6, 80, 255, 0.22, 0.45, 0.55 |
| `earth_helio_pos` | 3 |
| `earth_surface_offset` | 3 |
| `energy_density` | 4, 8, 1e-12 |
| `feasibility_scorecard` | 8.5, 9.81, 0.5, 0.99 |
| `flash` | 3.2 |
| `fmt_dist` | 1000, 1e+04, 0.01, 0.02 |
| `fmt_energy` | 1000, 1e+06, 1e+09, 1e+12, 1e+15, 1e+18, 1e+21, 1e+24 |
| `fmt_mass` | 1000, 1e+04, 1e+21, 1e+23, 1e+26, 0.5 |
| `fmt_power` | 1000, 1e+06, 1e+09, 1e+12, 1e+15 |
| `fmt_time` | 60, 90, 400, 3600, 5400, 1e+04, 1e+09 |
| `ford_roman_bound_j_m3` | 3, 4, 32, 1e+77 |
| `ford_roman_max_throat_tau` | 3, 4, 7, 0.25 |
| `ford_roman_wall_limit` | 100 |
| `gott_pair_offset` | 4, 8 |
| `handle_events` | 1.14, 3, 4, 5, 680, 1000, 0.88 |
| `helm_locked` | 0.5 |
| `honesty_audit` | 1.5, 1e-06 |
| `ism_blast_energy_j` | 0.5 |
| `ism_d3he_yield_kg_s` | 4, 0.75 |
| `log_bar_x` | 80 |
| `lorentz_gamma` | 1 |
| `magsail_area_m2` | 1000 |
| `main` | 0.01, 0.5 |
| `mass_budget` | 4, 500, 1e-06 |
| `max_boost_beta` | 18, 0.02, 0.5, 0.99 |
| `max_time_displacement` | 1.01, 10, 100, 1e+21, 0.45, 0.99, 0.999 |
| `mmp_extremal_charge_c` | 4 |
| `mmp_summary` | 3, 4 |
| `mmp_tidal_mass_kg` | 3, 4, 9.81, 1e-09 |
| `mmp_traversal_time_s` | 3 |
| `mouth_clock_rate` | 1 |
| `mt_exotic_energy_j` | 6 |
| `mt_flare_out` | 1e-09 |
| `mt_min_throat_m` | 9.81, 1e-09 |
| `mt_proper_length` | 4 |
| `mt_shape_b` | 1e-30 |
| `mt_shape_b_prime` | 1e-30 |
| `mt_throat_density` | 8 |
| `mt_tidal_g` | 9.81 |
| `mt_tidal_profile` | 9.81, 1e-30 |
| `mt_traversal_time_s` | 4, 10, 1e-06 |
| `multijump_plan` | 1e+06 |
| `note` | 40 |
| `operations_ledger` | 100, 1e+09, 0.1, 0.3, 0.5, 0.7 |
| `orbit` | 1.5, 1.55, 0.004, 0.009 |
| `pan_by` | 0.45 |
| `panel` | 3, 4, 6, 24, 25, 30, 214, 255, 8192, 0.12, 0.3, 0.88 |
| `plant_electric_w` | 1e+09 |
| `portal_cycle_s` | 1e-06 |
| `portal_summary` | 4, 1e-99 |
| `portal_traversal` | 10, 1.274e+07 |
| `print_startup_banner` | 78, 0.5 |
| `project` | 3, 560, 1e+06, 1e+09, 0.05 |
| `quantum_teleport_facts` | 1.38e+10 |
| `radiator_required_m2` | 4 |
| `radiator_temp_k` | 0.25 |
| `render` | 1.1, 1.6, 3, 3.5, 4, 5, 6, 14, 15, 16, 30, 44, 62, 72, 120, 210, +21 more |
| `report_dilation` | 1.6, 0.02, 0.25, 0.5, 0.75, 0.9, 0.98, 0.99 |
| `report_feasibility` | 20, 70, 78, 100, 1000, 0.5 |
| `report_ladder` | 1e-15, 0.5 |
| `report_metric` | 4, 5, 9.81, 10, 12, 1e-40, 1e-15, 1e-09, 0.001, 0.1, 0.5 |
| `report_portal` | 1.274e+07, 0.2 |
| `report_portal_test` | 1.01, 4, 5, 10, 20, 50, 60, 76, 100, 1000, 1.274e+07, 1.496e+11, 1e+21, 0.01, 0.1, 0.2, +7 more |
| `report_spec` | 90, 100, 1000, 1e+06, 0.5, 0.99 |
| `report_voyage` | 1.05, 5, 500, 2e+06, 0.5 |
| `road_frame` | 3 |
| `road_solar_hour` | 12, 24 |
| `row` | 100 |
| `run` | 60, 1000, 0.05 |
| `selftest` | 1.01, 1.05, 1.25, 1.5, 2.01, 2.44, 2.5, 3, 3.5, 3.7, 4, 5, 6, 7, 8, 9, +119 more |
| `set_beta` | 4 |
| `shape_df` | 1e-30 |
| `shape_df_shifted` | 1e-300 |
| `shape_f` | 1e-30 |
| `size` | 8, 12 |
| `text_shadow` | 255 |
| `tick` | 4, 5, 8, 0.22 |
| `update` | 1.2, 3, 4, 5, 6, 9, 60, 290, 295, 3600, 4000, 3e+04, 4e+04, 0.03, 0.05, 0.15, +3 more |
| `vgradient` | 3 |
| `visser_summary` | 3, 9.81 |
| `voyage_grav_drift_s` | 64, 0.5 |
| `wall_tidal_gradient` | 24, 72, 73, 1e-300 |
| `warp_energy_integral` | 3, 4, 14, 4000, 1e-300, 0.999 |
| `width_for` | 0.45 |
| `york_theta` | 1e-12 |
| `zoom_at` | 120, 2600, 4000, 1e-06, 0.055 |

1600 distinct literals across 192 functions -- these are the free parameters of the model, every one inspectable above.

## Return-type inventory (what each function hands back)

AST-inferred from the return expressions: `number` for arithmetic results, `dict`/`tuple`/`list`/`bool`/`str` for composites and flags, `call` where the return is another function's result.

| Function | Returns |
|----------|---------|
| `flat_interior_r` | call |
| `check_envelope` | dict |
| `rot_x` | call |
| `rot_y` | call |
| `rot_z` | call |
| `clamp` | call |
| `shape_f` | call, float, value |
| `shape_df` | call, float, value |
| `shape_df_shifted` | call, float, value |
| `york_theta` | call, float, value |
| `energy_density` | call, float, value |
| `warp_energy_integral` | call, value |
| `alcubierre_energy_j` | value |
| `equiv_mass_kg` | value |
| `wall_tidal_gradient` | call, float, value |
| `ford_roman_wall_limit` | call, value |
| `casimir_energy_density` | call, value |
| `casimir_cassette` | dict |
| `casimir_onboard_j` | value |
| `energy_conditions` | dict |
| `horizon_locked` | bool |
| `barrier_analysis` | dict |
| `barrier_scorecard` | value |
| `mass_budget` | value |
| `ship_mass_kg` | call |
| `lorentz_gamma` | call, value |
| `kinetic_energy_j` | call, value |
| `smes_store_j` | value |
| `plant_electric_w` | value |
| `cruise_load_w` | value |
| `waste_heat_w` | call, value |
| `radiator_area_m2` | value |
| `radiator_temp_k` | call, value |
| `radiator_required_m2` | call, value |
| `fusion_fuel_kg` | call, value |
| `beam_spot_m` | call, value |
| `beam_capture_frac` | float, value |
| `beam_power_w` | value |
| `boost_profile` | dict |
| `max_boost_beta` | call, value |
| `magsail_area_m2` | value |
| `magsail_drag_n` | value |
| `magsail_halving_time_s` | call, float, value |
| `magsail_decel_time_s` | call, float, value |
| `beam_brake_force_n` | value |
| `beam_brake_time_s` | call, value |
| `ism_particles_swept` | call, value |
| `ism_blast_energy_j` | value |
| `rocket_proper_time_s` | call, value |
| `crossing_time_s` | call, value |
| `fmt_energy` | str, value |
| `fmt_mass` | value |
| `fmt_time` | value |
| `fmt_dist` | value |
| `fmt_power` | value |
| `orders_of_magnitude` | call |
| `lapse_static` | call, float |
| `static_observer_exists` | bool |
| `grav_potential_at` | call, value |
| `grav_rate` | call |
| `ship_self_dilation` | call, value |
| `clock_ledger` | dict |
| `voyage_grav_drift_s` | value |
| `mt_embedding_z` | float, value |
| `mt_throat_density` | call, value |
| `mt_exotic_energy_j` | call, value |
| `mt_tidal_g` | call, value |
| `mt_min_throat_m` | call |
| `mt_traversal_time_s` | call, value |
| `mt_shape_b` | call, value |
| `mt_shape_b_prime` | call, value |
| `mt_redshift_phi` | float |
| `mt_flare_out` | dict |
| `mt_tidal_profile` | call, value |
| `mt_proper_length` | call, float |
| `ford_roman_bound_j_m3` | call, value |
| `ford_roman_max_throat_tau` | value |
| `mmp_extremal_charge_c` | value |
| `mmp_tidal_mass_kg` | call, value |
| `mmp_traversal_time_s` | value |
| `mmp_summary` | dict |
| `visser_shell_mass_kg` | float, value |
| `visser_shell_energy_j` | value |
| `visser_summary` | dict |
| `ctc_onset_s` | call, value |
| `ctc_by_warp_transport` | dict |
| `ctc_by_gravity_well` | dict |
| `quantum_teleport_facts` | dict |
| `chain_wormhole_offset` | call, value |
| `nested_wormhole_offset` | value |
| `tipler_cylinder_offset` | call, value |
| `gott_pair_offset` | call, value |
| `kerr_ctc_offset` | call, value |
| `max_time_displacement` | value |
| `ism_scoop_gas_kg_s` | value |
| `ism_d3he_yield_kg_s` | call, value |
| `portal_cycle_s` | call, value |
| `multijump_breakeven_s` | call, value |
| `multijump_plan` | dict |
| `portal_summary` | dict |
| `mouth_clock_rate` | call, value |
| `mouth_time_offset_s` | value |
| `ctc_exists` | bool, call |
| `portal_traversal` | dict |
| `report_portal_test` | None |
| `build_ship_parts` | call |
| `build_portal_parts` | call |
| `car_trigger_v` | value |
| `car_casimir_j` | call, value |
| `earth_helio_pos` | call |
| `earth_surface_offset` | call |
| `road_frame` | tuple |
| `road_inertial_speed` | tuple |
| `car_mass_budget` | value |
| `car_ops_ledger` | tuple |
| `car_power_budget` | dict |
| `car_thermal_step` | call |
| `car_fault_effects` | dict |
| `car_mph_step` | tuple |
| `car_part_mass` | call, dict |
| `road_solar_hour` | call, value |
| `car_transit` | dict |
| `build_special_parts` | call |
| `honesty_audit` | call, value |
| `report_spec` | call |
| `report_metric` | None |
| `report_ladder` | None |
| `buildability_ledger` | dict |
| `operations_ledger` | list |
| `feasibility_scorecard` | value |
| `report_feasibility` | None |
| `wrap_plain` | bool |
| `report_dilation` | None |
| `report_portal` | None |
| `report_voyage` | tuple |
| `selftest` | bool, call, float, tuple |
| `info_sections` | value |
| `vgradient` | None |
| `contrast_text` | value |
| `text_shadow` | NoneType, value |
| `panel` | None |
| `bar` | None |
| `wrap_text` | bool |
| `chip` | value |
| `project` | tuple |
| `draw_bubble_glow` | None |
| `log_bar_x` | value |
| `draw_vignette` | None |
| `print_startup_banner` | None |
| `main` | int, value |
| `world_verts` | value |
| `oo` | value |
| `ii` | value |
| `reset_view` | None |
| `zoom_at` | None |
| `orbit` | None |
| `pan_by` | None |
| `set_view` | None |
| `toggle_section` | None |
| `assembly_next` | None |
| `assembly_prev` | None |
| `active_part` | NoneType, value |
| `placing_part` | NoneType, value |
| `tick` | None |
| `render` | None |
| `nextord` | value |
| `nextord` | value |
| `s` | call |
| `nextord` | value |
| `deck_top` | value |
| `mode` | value |
| `exotic` | bool |
| `kinetic_now_j` | call |
| `energy_conditions` | call |
| `helm_locked` | bool |
| `collapse` | None |
| `update` | None |
| `warp` | value |
| `beta` | value |
| `remaining_m` | value |
| `cycle_warp` | None |
| `note` | None |
| `eta_s` | call, value |
| `update` | None |
| `begin_boost` | NoneType, str |
| `begin_brake` | NoneType, str |
| `auto_step` | value |
| `auto_done` | bool |
| `reset` | None |
| `lg` | call |
| `row` | None |
| `check` | None |
| `reset_view` | None |
| `zoom_at` | None |
| `orbit` | None |
| `pan_by` | None |
| `set_view` | None |
| `toggle_section` | None |
| `active_part` | NoneType |
| `placing_part` | NoneType |
| `tick` | None |
| `draw` | None |
| `flash` | None |
| `set_wall` | None |
| `set_beta` | None |
| `handle_events` | None |
| `update` | None |
| `draw` | None |
| `draw_topbar` | None |
| `draw_ship` | None |
| `draw_view_tabs` | None |
| `draw_ship_panel` | None |
| `draw_spec_card` | None |
| `draw_metric` | call, value |
| `draw_profiles` | None |
| `draw_metric_panel` | None |
| `draw_flight` | None |
| `draw_flight_hud` | None |
| `draw_flight_controls` | None |
| `draw_dilation` | None |
| `draw_dilation_graphs` | None |
| `draw_clock_panel` | None |
| `draw_portal` | None |
| `draw_portal_panel` | None |
| `draw_special` | None |
| `draw_special_panel` | None |
| `draw_ladder` | None |
| `draw_help` | None |
| `draw_info` | None |
| `run` | None |
| `size` | tuple |
| `write` | int |
| `flush` | None |
| `col_for` | call |
| `width_for` | value |

## The phase machine, complete (every legal transition)

Every move `Voyage` can make, with its trigger and where it fires in the source -- the whole mission logic in one table.

| From | To | Trigger | Where |
|------|----|---------|-------|
| DOCK | BOOST | `begin_boost` chip / `auto_step` when `beta_cmd > 0`; deploys rectenna, books the predicted bill | `Voyage.begin_boost` |
| BOOST | CRUISE | `v_ms` reaches `beta_cmd*c` (beam released) OR `x_m` exits `beam_range_ly` (cruise locks to whatever was reached -- beam exhaustion is a phase event) | `Voyage._step` |
| CRUISE | BRAKE | `begin_brake` chip, or `auto_step` when `remaining_m <= v*(brake_time*1.05 + tick)` with array / immediately without | `Voyage.begin_brake / auto_step` |
| BRAKE | ARRIVED | `v_ms < arrival_beta*c`; velocity zeroed, `arrived_at` stamped on ship clock | `Voyage._step` |
| BOOST | BRAKE | `begin_brake` also accepts BOOST (abort the run -- 'already stopped' guards every other phase) | `Voyage.begin_brake` |
| any | DOCK | `reset` chip -- re-inits core + voyage, keeps `dest_array` preference, clears `ftl_unlock`/`test_mode` | `App._chip_click('reset')` |
| CRUISE | (end, no phase) | passing the target with no array logs a flyby note; `auto_done` fires -- a flyby is a terminal demo state, not an arrival | `Voyage.auto_done` |

No other transitions exist: the machine only moves forward along DOCK->BOOST->CRUISE->BRAKE->ARRIVED (auto_step's docstring makes this a guarantee, so the demo can never fly a mission manual controls couldn't).

## Event wiring (every input event to its handler)

The complete input surface -- every pygame event type and clickable chip, to the action it triggers.

### Pygame events (`App.handle_events`)

| Event | Handling |
|-------|----------|
| QUIT | `running = False` |
| VIDEORESIZE | floor 1000x680, `set_mode` RESIZABLE, `_rebuild_bg()` |
| MOUSEBUTTONDOWN chip hit | `_chip_click(name)` |
| MOUSEBUTTONDOWN 1 (else) | `dragging=True`; on SHIP/PORTAL toggles `rend.selected` on the hovered part |
| MOUSEBUTTONDOWN 2/3 | `panning=True` |
| MOUSEBUTTONDOWN 4 (wheel up) | info panel: scroll -3; else `zoom_at(0.88, cursor)` |
| MOUSEBUTTONDOWN 5 (wheel dn) | info panel: scroll +3; else `zoom_at(1.14, cursor)` |
| MOUSEBUTTONUP | clears `dragging` and `panning` |
| MOUSEMOTION | dragging -> `orbit(rel)`; panning -> `pan_by(rel)`; shift = fine control |
| KEYDOWN | `_key(e.key, fine)` -- the full binding table above |

### Clickable chips (`App._chip_click`)

| Chip | Action |
|------|--------|
| `mode:N` | tab switch (the top bar is real buttons) |
| `labels` | toggle part labels |
| `section` | toggle the section cut |
| `shell` | raise/drop warp shell; collapse flag cleared on raise |
| `boost` | `begin_boost` -> phase DOCK->BOOST |
| `brake` | `begin_brake` -> BRAKE |
| `reset` | mission reset, keeps `dest_array`, clears FTL/TEST |
| `warp- / warp+` | time-warp rung down/up |
| `ftl` | unlock Alcubierre mode |
| `test` | TEST-mode auto-flight |
| `dest` | toggle destination array (rendezvous vs flyby) |
| `full / exploded / assembly` | view preset on the renderer |

## Compute-cost benchmark (what the model costs to run)

Live timings on this machine -- the expensive paths measured, not guessed.

| Operation | Time |
|-----------|------|
| `shape_f(R)` one evaluation | 0.0 ms |
| `warp_energy_integral()` 4000-sample Simpson | 0.0 ms |
| `alcubierre_energy_j(beta=1)` | 0.0 ms |
| `mass_budget()` full 17-component ledger | 0.0 ms |
| `build_ship_parts()` 460-mesh tessellation | 357.9 ms |
| `build_portal_parts()` 36-mesh tessellation | 9.0 ms |
| `barrier_analysis()` all 8 barriers | 36.9 ms |
| `honesty_audit()` 12 conservation checks | 91.4 ms |
| `report_voyage(0.5)` full mission integration | 89.7 ms |

## Per-key physics (what each control actually does to the state)

The exact increments, clamps and side-effects behind the key table -- the control surface quantified.

| Key | Effect on state |
|-----|-----------------|
| `,` / `.` | beta_cmd += -0.01 / +0.01 (x10 = 0.1 with SHIFT), clamped [0, beta_sub_max] or [0, beta_ftl_max] when FTL unlocked, rounded to 4 decimals; refused outright while `helm_locked()` (forward wall causally disconnected); in assembly view these keys step the build order instead |
| `[` / `]` | wall_m x (1/1.15) / x1.15 (x1.6 with SHIFT), clamped [wall_min_m, wall_max_m]; writes DIMS['wall_thick_m'] AND invalidates INFO_SECTIONS so the I panel re-derives; flashes sigma = 1/delta |
| `B` | toggles bubble_cmd; raising clears `collapsed` (a re-formed shell is a fresh shell) |
| `F` | toggles ftl_unlock; on unlock forces warp_i <= 1 (1 min/s) so the collapse is watchable; on relock clamps beta_cmd back to beta_sub_max |
| `G` / `K` | begin_boost / begin_brake -- the same commands the chips call; error strings surface as toasts |
| `J` | toggles dest_array via the 'dest' chip path |
| `T` | TEST mode -- ONLY works on the FLIGHT tab |
| `N` | reset: re-inits BOTH Voyage and WarpCore, preserves dest_array, clears ftl_unlock + test_mode, restores DIMS['wall_thick_m'] from the live core |
| `-` / `+` | cycle_warp(-1/+1): warp_i clamped [0,6] across the 7 rungs |
| `E` | exploded <-> full toggle (distinct from the 1/2/3 presets) |
| PGUP / PGDN | info panel scroll -/+12 lines |
| `I` | opens panel AND zeroes info_scroll |
| `1`/`2`/`3`/`4`(X) | view presets full/exploded/assembly + section cut toggle |
| ESC | running = False (clean quit) |

## The controlled vocabulary (every enum the model can emit)

Complete enumeration of every categorical string -- status, phase, mode, verdict, rating. If a string isn't here, the model can't say it.

### WarpCore.status (priority order)

- COLLAPSED (integrity <= collapse_floor, shell let go)
- BUBBLE DOWN (bubble_on < 0.05)
- SUPERLUMINAL -- UNFUNDED (exotic mode, debt booked)
- THERMAL LIMIT (rad_k > 95% of 1900 K graphite limit)
- SHELL DEGRADED (integrity < 0.6)
- NOMINAL (all clear)
- COLD (initial state before first update)

### Voyage.phase

- DOCK
- BOOST
- CRUISE
- BRAKE
- ARRIVED

### App.MODE_NAMES

- SHIP
- METRIC
- DILATION
- PORTAL
- FLIGHT

### Renderer views

- full
- exploded
- assembly

### Buildability ratings

- TODAY
- NEAR
- FAR
- OPEN
- IMPOSSIBLE

### Barrier verdicts

- PASS
- FAIL
- THEOREM
- CONJECTURE

### Feasibility statuses

- PASS
- PARTIAL
- OPEN
- FAIL
- REFUTED
- PHYSICAL

### Traversal verdict families

- LETHAL / survivable (tidal)
- THROAT CLOSED / throat holds (QI)
- TIME MACHINE / offset / no offset (chronology)
- BLOCKED BY TIDAL FORCES (overall)

### Time-warp rungs

- 1 s/s
- 1 min/s
- 1 h/s
- 1 d/s
- 30 d/s
- 1 yr/s
- 10 yr/s

### Chip names

- mode:0..4
- labels
- section
- shell
- boost
- brake
- reset
- warp-
- warp+
- ftl
- test
- dest
- full
- exploded
- assembly

## The formatter ladders (where the units switch, live)

How the twin renders every number -- each `fmt_*` swept across magnitudes so the unit-transition thresholds are demonstrated, not described.

| Input | energy | mass | time | distance | power |
|-------|--------|------|------|----------|-------|
| 1e-3 | 0.001 J | 0.001 kg | 0.0 s | 0.0 m | 0.001 W |
| 1e+0 | 1 J | 1 kg | 1.0 s | 1.0 m | 1 W |
| 1e+3 | 1 kJ | 1000 kg | 16.7 min | 1000.0 m | 1 kW |
| 1e+6 | 1 MJ | 1000 t | 11.6 d | 1e+03 km | 1 MW |
| 1e+9 | 1 GJ | 1e+06 t | 31.69 yr | 1e+06 km | 1 GW |
| 1e+12 | 1 TJ | 1e+09 t | 3.17e+04 yr | 6.685 AU | 1 TW |
| 1e+15 | 1 PJ | 1e+12 t | 3.17e+07 yr | 0.1057 ly | 1 PW |
| 1e+18 | 1 EJ | 1e+15 t | 31.7 Gyr | 105.7001 ly | 1e+03 PW |
| 1e+21 | 1 ZJ | 0.000167 Mearth | 3.17e+04 Gyr | 105700.0834 ly | 1e+06 PW |
| 1e+24 | 1 YJ | 0.000527 Mjup | 3.17e+07 Gyr | 105700083.4025 ly | 1e+09 PW |
| 1e+27 | 1e+03 YJ | 0.000503 Msun | 3.17e+10 Gyr | 105700083402.4615 ly | 1e+12 PW |
| 1e+30 | 1.000e+30 J | 0.503 Msun | 3.17e+13 Gyr | 105700083402461.5469 ly | 1e+15 PW |

Ladders: energy J/kJ/MJ/GJ/TJ/PJ/EJ/ZJ/YJ then scientific; mass kg/t/Mearth/Mjup/Msun; time s/min/d/yr/Gyr; distance m/km/AU/ly; power W/kW/MW/GW/TW/PW then scientific. Non-finite inputs render `nan`/`-` honestly rather than inventing a unit.

## Module-level side effects (what import does)

Everything that happens just from `import Warpdrive`:

- `warnings.filterwarnings("ignore")` (L134) -- numeric noise suppressed; physics checks do their own validation
- `os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")` (L135) -- no banner when pygame is present
- all spec dictionaries (DIMS/PLANT/DRIVE) built at module level -- import is the full spec load, no lazy init
- no meshes, no viewer, no voyage until built -- `import` is side-effect-free beyond the two calls above

## Import usage map (what each dependency actually does)

Every imported module, its call-site count (AST), and the job it performs -- the dependency contract at use, not just at import.

| `math` | 514 call sites | every transcendental in the file -- tanh, sin/cos, sqrt, pi, log -- the physics engine |
| `re` | 5 call sites | spec-key comment parsing and signature text handling in the self-documenting sections |
| `itertools` | 3 call sites | `islice` caps hull-loft section lists at 513 -- the mesh-detail bound |
| `inspect` | 1 call sites | `signature()` inside `_numeric_args` -- the decorator reads each function's params to coerce args |
| `functools` | 1 call sites | `wraps` preserving identity on the `_numeric_args` boundary decorator |
| `argparse` | 1 call sites | the 12-flag CLI in main() |
| `sys` | 4 call sites | argv dispatch and exit codes |
| `os` | 1 call sites | PYGAME_HIDE_SUPPORT_PROMPT at import |
| `warnings` | 1 call sites | filterwarnings('ignore') at import |
| `numpy` | 396 call sites | every vertex array, rotation matrix and mesh -- the geometry engine |
| `pygame` | 190 call sites | optional viewer; everything renders through it when present |

## The _Dims contract (the spec dictionary itself)

`DIMS` is not a dict -- it's a `_Dims`, and the distinction is the model's fail-closed guarantee:

- `__getitem__` returns `nan` for missing keys AND for non-numeric stored values -- a deleted spec key or a corrupted value degrades into honest NaN propagation, never KeyError/TypeError
- writes and iteration stay raw -- `for k in DIMS` sees exactly what was stored so sanitize loops and ledgers can inspect it
- `_numeric_dims()` produces a pre-sanitized copy for builders that do local `d[...]` arithmetic -- still a _Dims so deleted keys stay NaN there too
- demo: `DIMS['no_such_key']` -> `nan`; `DIMS['bubble_r_m']` -> `183.44`

## Local-variable inventory (every intermediate in every function)

Every name assigned inside each function body -- the derivation steps themselves made visible. `e_add`, `g`, `v_new`, `v_cap` in `_step` is the boost integration; these names are the model's scratch work.

- `_numeric_dims` (2): `k`, `v`
- `flat_interior_r` (2): `delta`, `R`
- `_envelope_points` (3): `d`, `Rr`, `nose`
- `check_envelope` (9): `delta`, `lim`, `ok`, `worst_name`, `worst_d`, `name`, `r`, `z`, `dd`
- `rot_x` (3): `a`, `c`, `s`
- `rot_y` (3): `a`, `c`, `s`
- `rot_z` (3): `a`, `c`, `s`
- `_prep_mesh` (18): `m`, `w`, `FA`, `edges`, `ok`, `f`, `lens`, `i`, `L`, `v0`, `v1`, `v2`, `vol`, `k`, `p`, `a`, `b`, `v`
- `_prep_part` (32): `part`, `meshes`, `m`, `solid`, `wire`, `dyn`, `vo`, `w`, `FA`, `fl`, `mm`, `wm`, `vlist`, `flist`, `flen`, `fcol`, `fcoil`, `fglow`, `fhot`, `fcl`, `fsm`, `vb`, `f`, `nf` ...
- `_prep_global` (33): `plist`, `vo`, `wo`, `gv`, `gw`, `groups`, `g`, `gwires`, `cen`, `spr`, `vs`, `ws`, `vslice`, `wslice`, `dynl`, `pi`, `p`, `m`, `w`, `dm`, `s0`, `fl`, `L`, `k` ...
- `_detail_seg` (1): `seg`
- `_coil_count` (1): `c`
- `_finite` (2): `vals`, `v`
- `_solid_cylinder` (13): `r`, `z0`, `z1`, `seg`, `ang`, `z`, `c0`, `c1`, `i`, `verts`, `faces`, `a`, `b`
- `_annulus_cylinder` (12): `r_out`, `r_in`, `z0`, `z1`, `seg`, `ang`, `z`, `i`, `verts`, `faces`, `a`, `layer`
- `_coil_arc` (25): `r_mid`, `r_in`, `r_out`, `a0`, `a1`, `seg_arc`, `seg_tube`, `phis`, `psis`, `ph`, `st`, `j`, `verts`, `faces`, `rho`, `i`, `b`, `cp`, `sp`, `ps`, `b0`, `b1`, `i2`, `q` ...
- `_deck_plate` (28): `r_out`, `z0`, `z1`, `holes`, `seg`, `rings`, `idx`, `k`, `i`, `verts`, `faces`, `z`, `j`, `i2`, `r_c`, `a_c`, `hx`, `hy`, `hr`, `base`, `r`, `x`, `y`, `cv` ...
- `_box` (11): `cx`, `cy`, `cz`, `sx`, `sy`, `sz`, `v`, `f`, `hx`, `hy`, `hz`
- `_sphere` (16): `r`, `seg`, `rings`, `squash`, `j`, `verts`, `faces`, `phi`, `i`, `sp`, `cp`, `th`, `a`, `b`, `c`, `d`
- `_torus` (22): `R`, `r`, `seg_major`, `seg_minor`, `a0`, `a1`, `closed`, `n_major`, `i`, `lim`, `verts`, `faces`, `t`, `j`, `i2`, `base`, `ct`, `st`, `p`, `j2`, `cp`, `sp`
- `_dish` (16): `r_out`, `depth`, `z0`, `seg`, `rings`, `flip`, `j`, `verts`, `faces`, `rr`, `z`, `i`, `a`, `b`, `c`, `d`
- `_hull_loft` (17): `sections`, `seg`, `n`, `k`, `c0`, `c1`, `base`, `i`, `verts`, `faces`, `z`, `rr`, `a`, `b`, `c`, `d`, `s`
- `_ring_wire` (7): `r`, `z`, `seg`, `axis`, `verts`, `i`, `a`
- `_smooth_sections` (16): `ctrl`, `sub`, `pts`, `out`, `i`, `s`, `p0`, `p1`, `p2`, `p3`, `t`, `vals`, `k`, `t2`, `t3`, `p`
- `_grp` (3): `meshes`, `group`, `m`
- `_place` (6): `meshes`, `pivot`, `tilt`, `group`, `piv`, `m`
- `_mix` (4): `c1`, `c2`, `t`, `i`
- `_rgb` (3): `c`, `fallback`, `i`
- `_xy` (3): `pos`, `x`, `y`
- `_label` (15): `surf`, `font`, `text`, `pos`, `accent`, `color`, `xy`, `col`, `img`, `bg`, `glow`, `x`, `y`, `px`, `py`
- `clamp` (3): `x`, `lo`, `hi`
- `_sech2` (3): `x`, `ax`, `ch`
- `shape_f` (5): `r`, `R`, `delta`, `sigma`, `den`
- `shape_df` (5): `r`, `R`, `delta`, `sigma`, `den`
- `shape_df_shifted` (5): `u`, `R`, `delta`, `sigma`, `den`
- `york_theta` (6): `x`, `rho_perp`, `beta`, `R`, `delta`, `r`
- `energy_density` (7): `x`, `rho_perp`, `beta`, `R`, `delta`, `r`, `dfr`
- `warp_energy_integral` (17): `R`, `delta`, `samples`, `key`, `cache`, `half`, `n`, `h`, `sh`, `total`, `i`, `result`, `u`, `r`, `d`, `val`, `w`
- `alcubierre_energy_j` (6): `beta`, `R`, `delta`, `key`, `cache`, `result`
- `equiv_mass_kg` (1): `energy_j`
- `wall_tidal_gradient` (8): `beta`, `R`, `delta`, `step`, `worst`, `i`, `u`, `fpp`
- `ford_roman_wall_limit` (1): `beta`
- `casimir_energy_density` (2): `gap_m`, `a`
- `casimir_cassette` (7): `plate`, `gap`, `pitch`, `_ratio`, `n_gaps`, `v_gap`, `rho`
- `energy_conditions` (1): `beta`
- `horizon_locked` (1): `beta`
- `barrier_analysis` (34): `R`, `d0`, `cas`, `a_wall`, `a_limit`, `wall_gap`, `delta_qi`, `a_at_qi`, `wall_passable`, `nec_sub`, `nec_super`, `super_passable`, `E_need`, `energy_gap`, `cassettes_needed`, `energy_passable`, `steer_passable`, `b_thermal`, `T_at_limit`, `thermal_gap`, `P_at_limit`, `A_needed`, `thermal_passable`, `delta_max` ...
- `barrier_scorecard` (2): `ba`, `out`
- `_torus_surface` (2): `R`, `r`
- `mass_budget` (10): `d`, `b`, `build`, `r_i`, `v_coil`, `hull_area`, `Rm`, `rm`, `Rc`, `rc`
- `lorentz_gamma` (2): `beta`, `b`
- `kinetic_energy_j` (3): `beta`, `mass_kg`, `m`
- `smes_store_j` (4): `vol`, `u`, `R`, `r`
- `cruise_load_w` (7): `beta`, `bubble_on`, `p`, `b`, `on`, `coil`, `ctrl`
- `waste_heat_w` (2): `load_w`, `eff`
- `radiator_temp_k` (2): `waste_w`, `denom`
- `radiator_required_m2` (4): `waste_w`, `t_k`, `t`, `denom`
- `fusion_fuel_kg` (2): `energy_j`, `den`
- `beam_spot_m` (4): `range_m`, `lam`, `ap`, `r`
- `beam_capture_frac` (3): `range_m`, `spot`, `d_rect`
- `beam_power_w` (1): `range_m`
- `boost_profile` (14): `beta`, `mass_kg`, `m`, `need`, `limit_m`, `dt`, `v_target`, `ok`, `got`, `t`, `x`, `v`, `p_in`, `g`
- `max_boost_beta` (8): `mass_kg`, `lo`, `hi`, `key`, `cache`, `result`, `_`, `mid`
- `magsail_drag_n` (3): `beta`, `v`, `rho`
- `magsail_halving_time_s` (5): `beta`, `mass_kg`, `m`, `v0`, `k`
- `magsail_decel_time_s` (8): `beta`, `mass_kg`, `beta_final`, `m`, `bf`, `k`, `v0`, `vf`
- `beam_brake_force_n` (3): `range_to_array_m`, `r`, `p`
- `beam_brake_time_s` (4): `beta`, `mass_kg`, `m`, `f`
- `ism_particles_swept` (2): `distance_m`, `R`
- `ism_blast_energy_j` (4): `beta`, `distance_m`, `R`, `n`
- `rocket_proper_time_s` (2): `beta`, `distance_m`
- `crossing_time_s` (1): `beta`
- `_real` (1): `v`
- `_args_real` (10): `fn`, `sig`, `pos`, `none_is_sentinel`, `a`, `k`, `p`, `i`, `x`, `v`
- `fmt_energy` (5): `j`, `a`, `sign`, `scale`, `unit`
- `fmt_mass` (3): `kg`, `a`, `sign`
- `fmt_time` (2): `s`, `a`
- `fmt_dist` (2): `m`, `a`
- `fmt_power` (4): `w`, `a`, `scale`, `unit`
- `orders_of_magnitude` (2): `a`, `b`
- `lapse_static` (6): `r`, `beta`, `R`, `delta`, `f`, `q`
- `static_observer_exists` (1): `beta`
- `grav_potential_at` (4): `x_m`, `phi`, `w`, `d`
- `grav_rate` (2): `x_m`, `q`
- `_earth_rate` (1): `EARTH_ORBIT_RATE`
- `ship_self_dilation` (2): `r`, `phi`
- `clock_ledger` (7): `t_ship_s`, `x_m`, `beta`, `r_here`, `r_earth`, `rows`, `drift_s`
- `voyage_grav_drift_s` (7): `t_total_s`, `x_start`, `x_end`, `n`, `tot`, `i`, `x`
- `mt_embedding_z` (2): `rho`, `b0`
- `mt_throat_density` (1): `b0`
- `mt_exotic_energy_j` (2): `b0`, `shell_factor`
- `mt_tidal_g` (3): `b0`, `body_m`, `a`
- `mt_min_throat_m` (2): `g_limit`, `body_m`
- `mt_traversal_time_s` (3): `b0`, `v_ms`, `length_factor`
- `mt_shape_b` (2): `r`, `b0`
- `mt_shape_b_prime` (2): `r`, `b0`
- `mt_redshift_phi` (2): `r`, `b0`
- `mt_flare_out` (4): `b0`, `r0`, `b_at`, `bp_at`
- `mt_tidal_profile` (7): `r`, `b0`, `body_m`, `phi`, `b`, `bp`, `a`
- `mt_proper_length` (2): `b0`, `r_far`
- `ford_roman_bound_j_m3` (1): `tau_s`
- `ford_roman_max_throat_tau` (1): `b0`
- `mmp_extremal_charge_c` (1): `M_kg`
- `mmp_tidal_mass_kg` (2): `g_limit`, `body_m`
- `mmp_traversal_time_s` (3): `M_kg`, `t_nat`, `log_factor`
- `mmp_summary` (7): `g_limit`, `body_m`, `M`, `Q`, `t_trav`, `r_s`, `e_casimir`
- `visser_shell_mass_kg` (3): `a_m`, `M_kg`, `rs`
- `visser_shell_energy_j` (2): `a_m`, `M_kg`
- `visser_summary` (5): `a_m`, `M_kg`, `m_shell`, `e_shell`, `rs`
- `ctc_onset_s` (2): `mouth_sep_m`, `rate_diff`
- `ctc_by_warp_transport` (1): `beta`
- `ctc_by_gravity_well` (4): `phi_over_c2`, `mouth_sep_m`, `sep`, `rate`
- `quantum_teleport_facts` (2): `bits`, `seconds`
- `chain_wormhole_offset` (3): `n_wormholes`, `elapsed_s`, `rate_diff`
- `nested_wormhole_offset` (2): `outer_offset_s`, `inner_offset_s`
- `tipler_cylinder_offset` (4): `L_m`, `R_m`, `omega_rads`, `M_kg`
- `gott_pair_offset` (4): `mu_kg_m`, `v_beta`, `D_m`, `delta`
- `kerr_ctc_offset` (5): `a_m`, `r_m`, `M_kg`, `n_orbits`, `per_orbit`
- `max_time_displacement` (25): `elapsed_s`, `mouth_sep_m`, `phi_over_c2`, `beta`, `n_wormholes`, `tipler_L_m`, `tipler_R_m`, `tipler_omega_rads`, `gott_mu_kg_m`, `gott_D_m`, `kerr_M_kg`, `kerr_r_m`, `kerr_a_m`, `sep`, `rate_b`, `rate_diff`, `single_offset`, `chain_offset`, `tipler_off`, `gott_off`, `kerr_a`, `kerr_r`, `kerr_off`, `results` ...
- `ism_scoop_gas_kg_s` (2): `beta`, `v`
- `ism_d3he_yield_kg_s` (10): `beta`, `gas`, `m`, `d_mass`, `he4_mass`, `he3_mass`, `res`, `avail_kg_s`, `frac`, `f`
- `portal_cycle_s` (6): `mouth_sep_m`, `beta`, `overhead_s`, `b0_m`, `oh`, `b`
- `multijump_breakeven_s` (5): `mouth_sep_m`, `beta`, `rate_diff`, `overhead_s`, `b0_m`
- `multijump_plan` (33): `cycles`, `elapsed_s`, `rate_diff`, `mouth_sep_m`, `beta`, `direction`, `overhead_s`, `fuel_start_kg`, `b0_m`, `delta_t`, `load`, `scoop`, `gas`, `t`, `rows`, `cum_disp`, `fuel_burnt`, `fuel_scooped`, `gas_scooped`, `remaining`, `fuel_out_at`, `exotic_per_hop`, `k`, `breakeven` ...
- `portal_summary` (8): `b0`, `safe`, `flare`, `mmp`, `vs`, `qi_hold_s`, `qi_bound_1s`, `traverse`
- `mouth_clock_rate` (4): `phi_over_c2`, `beta`, `grav`, `kinematic`
- `mouth_time_offset_s` (3): `rate_a`, `rate_b`, `elapsed_s`
- `ctc_exists` (2): `mouth_sep_m`, `offset_s`
- `portal_traversal` (35): `b0_m`, `mouth_a_phi_c2`, `mouth_a_beta`, `mouth_b_phi_c2`, `mouth_b_beta`, `mouth_sep_m`, `elapsed_s`, `payload`, `payload_size_m`, `payload_speed_ms`, `sep`, `rate_a`, `rate_b`, `offset_s`, `arrival_offset_s`, `light_time`, `ctc`, `ctc_margin_s`, `onset_s`, `traverse_s`, `qi_hold_s`, `throat_open`, `exotic_j`, `casimir_j` ...
- `report_portal_test` (46): `b0`, `safe_b0`, `t1`, `t2`, `elapsed`, `t3`, `elapsed4`, `t4`, `elapsed5`, `t5`, `t6`, `au_m`, `phi_ns`, `beta_rocket`, `t7`, `elapsed8`, `t8`, `phi_bh`, `beta_extreme`, `t9`, `N`, `nested`, `tipler_L`, `tipler_R` ...
- `_print_traversal` (2): `t`, `_off`
- `_xform` (4): `verts`, `mat`, `off`, `a`
- `_tangential` (1): `angle`
- `_radial` (1): `angle`
- `build_ship_parts` (5): `detail`, `VISUAL_DETAIL`, `_SEG_FLOOR`, `_old_vd`, `_old_sf`
- `_build_ship_parts_impl` (154): `d`, `_k`, `parts`, `_order`, `Rring`, `rring`, `hull_r`, `hull_h`, `mb`, `_tip`, `_rf`, `_cap`, `profile`, `_rzt`, `_rw`, `meshes`, `_t2`, `_dzs`, `_tr`, `_rz0`, `_rz1`, `_xoff`, `_gaps`, `_zsx` ...
- `_mt_funnel` (15): `b0`, `rho_max`, `rings`, `seg`, `sign`, `rhos`, `i`, `rho`, `j`, `verts`, `faces`, `t`, `z`, `base`, `a`
- `build_portal_parts` (5): `detail`, `VISUAL_DETAIL`, `_SEG_FLOOR`, `_old_vd`, `_old_sf`
- `_build_portal_parts_impl` (30): `d`, `_k`, `parts`, `_o`, `b0`, `rmin`, `ps`, `meshes`, `i`, `rho_max`, `safe`, `tv`, `tf`, `fv`, `ff`, `a`, `mm`, `_r_out`, `sign`, `nm`, `tv2`, `tf2`, `r0`, `r1` ...
- `car_casimir_j` (6): `gap`, `pitch`, `rho`, `n_gaps`, `v`, `e`
- `earth_helio_pos` (5): `t_s`, `t`, `M`, `r`, `th`
- `earth_surface_offset` (11): `t_s`, `lat_deg`, `lon_deg`, `t`, `lat`, `lon`, `th`, `ex`, `ey`, `ez`, `eps`
- `_tilt_z` (2): `v`, `eps`
- `road_frame` (11): `t_s`, `lat_deg`, `lon_deg`, `nan3`, `t`, `lat`, `lon`, `th`, `up`, `east`, `north`
- `road_inertial_speed` (4): `lat_deg`, `v_orb`, `lat`, `v_spin`
- `car_mass_budget` (3): `cas_line`, `conduit_m`, `items`
- `car_power_budget` (6): `loads`, `supply`, `_k`, `p`, `_d`, `_f`
- `car_thermal_step` (10): `cell_k`, `heat_w`, `dt_s`, `louver_eff`, `tk`, `q`, `dt`, `eff`, `rad`, `t_eq`
- `car_fault_effects` (1): `fault`
- `car_mph_step` (11): `mph`, `thr`, `brk`, `fired`, `dt_s`, `cell_k`, `armed`, `m`, `dt`, `tk`, `derated`
- `car_part_mass` (3): `b`, `names`, `n`
- `road_solar_hour` (7): `t_s`, `lon_deg`, `t`, `lon`, `sid_phase`, `sun_ra`, `ha`
- `car_transit` (19): `t0_s`, `hop_s`, `lat_deg`, `lon_deg`, `nan3`, `t0`, `hop`, `e0`, `e1`, `s0`, `s1`, `e_dep`, `_n_dep`, `_u_dep`, `e_arr`, `_n_arr`, `_u_arr`, `p0`, `p1`
- `_car_loft` (28): `stations`, `sub`, `NV`, `n`, `k`, `c0`, `c1`, `base`, `i`, `fine`, `verts`, `faces`, `z`, `hw`, `yt`, `yb`, `ring`, `s`, `j`, `a`, `b`, `c`, `d`, `s0` ...
- `_rod` (12): `p1`, `p2`, `r`, `seg`, `d`, `L`, `up`, `n1`, `nn`, `n2`, `verts`, `faces`
- `_pipe_path` (24): `pts`, `r`, `seg`, `closed`, `n`, `up_ref`, `i`, `lim`, `verts`, `faces`, `nt`, `t`, `up`, `n1`, `nn`, `n2`, `a`, `i2`, `j`, `c0`, `c1`, `base`, `b`, `p`
- `_wire_ellipsoid` (12): `a`, `b`, `c`, `seg`, `out`, `t`, `u`, `y`, `rr`, `pts`, `ux`, `uz`
- `build_special_parts` (6): `detail`, `eff`, `VISUAL_DETAIL`, `_SEG_FLOOR`, `_old_vd`, `_old_sf`
- `_build_special_parts_impl` (871): `parts`, `_o`, `scale`, `need`, `cas`, `ke88`, `stations`, `meshes`, `sx`, `gx`, `tx`, `zz`, `_wt`, `_wo`, `p2`, `lx`, `pts`, `px`, `hx`, `t`, `ts2`, `rz`, `vx`, `wheel` ...
- `honesty_audit` (25): `core`, `voyage`, `verbose`, `checks`, `led`, `t_ship`, `t_earth`, `t_coord`, `x_m`, `v_beta`, `phase`, `c_beta`, `c_beta_cmd`, `debt`, `exotic`, `cap`, `implied`, `ec`, `drift`, `ok`, `k`, `_debt`, `name`, `passed` ...
- `_rule` (1): `title`
- `report_spec` (10): `d`, `mb`, `total`, `_keys`, `env`, `name`, `spec`, `key`, `m`, `share`
- `report_metric` (12): `R`, `d0`, `off`, `delta`, `b`, `cas`, `need`, `needq`, `r`, `E`, `tag`, `a`
- `report_ladder` (6): `base`, `label`, `factor`, `status`, `cite`, `E`
- `buildability_ledger` (10): `d`, `_k`, `shield_t`, `tape_km`, `cas_plates`, `sail_km`, `sail_gm`, `rect_t`, `ship`, `infra`
- `operations_ledger` (1): `d`
- `feasibility_scorecard` (6): `R`, `bcap`, `w99`, `w20`, `need1`, `rows`
- `report_feasibility` (24): `rows`, `tally`, `n`, `led`, `budget`, `ops`, `total_kg`, `tally2`, `today`, `near`, `name`, `status`, `why`, `line`, `needs`, `mass_note`, `_`, `p`, `duty`, `fail`, `power`, `s`, `k`, `v`
- `wrap_plain` (6): `text`, `width`, `word`, `out`, `cur`, `trial`
- `report_dilation` (7): `beta`, `t`, `b`, `drift`, `frac`, `name`, `x`
- `report_portal` (7): `ps`, `fl`, `vs`, `mmp`, `g`, `w`, `q`
- `report_voyage` (11): `beta`, `dest_array`, `braked`, `guard`, `stall`, `_sig`, `line`, `core`, `v`, `_now`, `need`
- `selftest` (344): `results`, `R`, `_dims_snapshot`, `worst`, `delta`, `E`, `tf`, `tb`, `t`, `t2`, `bcap`, `ke_max`, `ke_09`, `ke_06`, `ke_099`, `bp_max`, `bp_09`, `cap_05`, `cap_10`, `lap`, `dr`, `ps`, `q`, `b0` ...
- `_component_info_sections` (86): `mb`, `total`, `ops`, `led`, `_parts`, `_R_INT`, `_p`, `_pname`, `_ml`, `_DEF`, `_WHY`, `_UNIT`, `_PER`, `_MOUNT`, `_trp`, `_rcs`, `_MAT`, `_STORES`, `_MASSDER`, `_ANALOG`, `_PHASE`, `_CASC`, `_THERM`, `_CONN` ...
- `_function_registry_lines` (19): `domains`, `mod`, `funcs`, `out`, `assigned`, `rest`, `priv`, `n`, `cn`, `title`, `prefixes`, `members`, `f`, `doc`, `first`, `ln`, `cls`, `sig`, `docf`
- `_runtime_state_lines` (8): `env`, `out`, `name`, `role`, `ln`, `n`, `r`, `z`
- `_spec_key_lines` (14): `out`, `key_line`, `src_lines`, `i`, `ln`, `km`, `k`, `m`, `c`, `j`, `name`, `d`, `v`, `vs`
- `_info_sections` (16): `R`, `d0`, `cas`, `mb`, `bcap`, `need1`, `needq`, `w50`, `w20`, `ps`, `mmp`, `vs`, `ba`, `v`, `k`, `kv`
- `info_sections` (1): `INFO_SECTIONS`
- `vgradient` (8): `surf`, `top`, `bot`, `t`, `col`, `arr`, `h`, `w`
- `_luminance` (4): `rgb`, `r`, `g`, `b`
- `contrast_text` (3): `bg_rgb`, `light`, `dark`
- `text_shadow` (15): `surf`, `font`, `text`, `pos`, `color`, `shadow`, `offset`, `xy`, `off`, `sh`, `img`, `x`, `y`, `ox`, `oy`
- `_trender` (5): `font`, `text`, `color`, `key`, `img`
- `panel` (19): `surf`, `x`, `y`, `w`, `h`, `alpha`, `cache`, `key`, `grad`, `hi_col`, `s`, `t`, `r`, `g`, `b`, `a`, `arr`, `rgb`, `v`
- `bar` (21): `surf`, `font`, `x`, `y`, `w`, `h`, `frac`, `color`, `label`, `valtext`, `mark`, `lo`, `hi`, `fr`, `f`, `img`, `val`, `col`, `vr`, `v`, `px`
- `wrap_text` (7): `font`, `text`, `maxpx`, `word`, `out`, `cur`, `trial`
- `chip` (19): `surf`, `font`, `x`, `y`, `text`, `on`, `col_on`, `r`, `col`, `img`, `xr`, `yr`, `w`, `h`, `s`, `row`, `bord`, `t`, `a`
- `project` (12): `pts`, `az`, `el`, `dist`, `cx`, `cy`, `focal`, `pan`, `Rc`, `cam`, `z`, `nanv`
- `draw_bubble_glow` (17): `surf`, `cx`, `cy`, `r`, `intensity`, `col`, `pulse_phase`, `pulse`, `layers`, `s`, `i`, `core_a`, `cx_s`, `cy_s`, `t`, `radius`, `a`
- `log_bar_x` (6): `value_j`, `x0`, `x1`, `lo_exp`, `hi_exp`, `e`
- `draw_vignette` (16): `surf`, `strength`, `key`, `cache`, `cache_key`, `v`, `max_r`, `step`, `y`, `w`, `h`, `cx`, `cy`, `x`, `d`, `a`
- `print_startup_banner` (1): `bcap`
- `main` (9): `argv`, `ap`, `args`, `ran`, `rc`, `ok`, `beta`, `hi`, `a`
- `__getitem__` (3): `self`, `key`, `v`
- `__init__` (17): `self`, `verts`, `faces`, `color`, `name`, `spin`, `group`, `pivot`, `tilt`, `wire`, `glow`, `hot`, `n`, `_faces`, `piv`, `f`, `i`
- `world_verts` (5): `self`, `angle`, `v`, `rx`, `ry`
- `oo` (2): `layer`, `i`
- `ii` (2): `layer`, `i`
- `_open` (10): `j`, `i`, `i2`, `r_c`, `a_c`, `x`, `y`, `hx`, `hy`, `hr`
- `__init__` (9): `self`, `key`, `name`, `meshes`, `specs`, `order`, `explode`, `color`, `n`
- `__init__` (8): `self`, `parts_builder`, `home_az`, `home_el`, `home_dist`, `section_keys`, `plist`, `p`
- `reset_view` (1): `self`
- `zoom_at` (7): `self`, `factor`, `mouse_pos`, `rect`, `old`, `anchor`, `scale`
- `orbit` (5): `self`, `dx`, `dy`, `fine`, `sens`
- `pan_by` (5): `self`, `dx`, `dy`, `fine`, `sens`
- `set_view` (2): `self`, `mode`
- `toggle_section` (1): `self`
- `assembly_next` (1): `self`
- `assembly_prev` (1): `self`
- `active_part` (3): `self`, `i`, `p`
- `placing_part` (2): `self`, `p`
- `_sync_pop` (1): `self`
- `tick` (7): `self`, `dt`, `hi`, `sp_target`, `i`, `target`, `tp`
- `_layout` (7): `self`, `pi`, `vw`, `eamt`, `part`, `order`, `asm`
- `render` (217): `self`, `surf`, `rect`, `angles`, `mouse_pos`, `show_labels`, `label_font`, `interactive`, `coil_glow`, `drive_power`, `rad_heat`, `bubble_on`, `clip`, `Rcam`, `default_ang`, `vw`, `eamt`, `hi`, `pose`, `qglow`, `akey`, `pan_now`, `pan_moved`, `interacting` ...
- `_section_cut` (6): `self`, `key`, `wvx`, `face`, `t`, `i`
- `_wrapped` (5): `a`, `k`, `i`, `x`, `v`
- `_leg` (3): `avail_kg_s`, `frac`, `f`
- `_loft_mean_r` (6): `cap_frac`, `c`, `pr`, `pa`, `z`, `r`
- `_r_at` (6): `z0`, `_i`, `z1`, `r1`, `z2`, `r2`
- `s` (2): `names`, `n`
- `deck_top` (7): `z`, `k`, `z0`, `_`, `t0`, `z1`, `t1`
- `__init__` (1): `self`
- `mode` (1): `self`
- `exotic` (1): `self`
- `kinetic_now_j` (1): `self`
- `energy_conditions` (1): `self`
- `helm_locked` (1): `self`
- `_thermal` (4): `self`, `dt`, `target`, `tau`
- `_integrity` (5): `self`, `dt`, `stress`, `_lim`, `avail`
- `collapse` (2): `self`, `msg`
- `update` (11): `self`, `dt`, `world`, `_lk`, `target_on`, `n`, `i`, `rng`, `net`, `real`, `ph`
- `__init__` (1): `self`
- `warp` (2): `self`, `i`
- `beta` (1): `self`
- `remaining_m` (2): `self`, `r`
- `cycle_warp` (2): `self`, `d`
- `note` (2): `self`, `text`
- `eta_s` (2): `self`, `v`
- `update` (7): `self`, `dt_real`, `core`, `dt_v`, `steps`, `h`, `_`
- `_step` (14): `self`, `dt`, `core`, `attr`, `m`, `p_in`, `e_add`, `e_kin`, `g`, `v_new`, `v_cap`, `slew`, `f`, `p`
- `begin_boost` (3): `self`, `core`, `bp`
- `begin_brake` (4): `self`, `core`, `b`, `blast`
- `auto_step` (4): `self`, `core`, `tick_s`, `margin`
- `auto_done` (1): `self`
- `reset` (2): `self`, `core`
- `lg` (1): `k`
- `row` (5): `name`, `spec`, `key`, `m`, `share`
- `check` (4): `label`, `cond`, `detail`, `ok`
- `_wv` (2): `part`, `m`
- `_skin` (1): `z`
- `_comment` (5): `k`, `i`, `m`, `c`, `j`
- `__init__` (4): `self`, `az`, `el`, `dist`
- `reset_view` (1): `self`
- `zoom_at` (4): `self`, `factor`, `mouse_pos`, `rect`
- `orbit` (5): `self`, `dx`, `dy`, `fine`, `sens`
- `pan_by` (4): `self`, `dx`, `dy`, `fine`
- `set_view` (2): `self`, `mode`
- `toggle_section` (1): `self`
- `active_part` (1): `self`
- `placing_part` (1): `self`
- `tick` (2): `self`, `dt`
- `__init__` (7): `self`, `n`, `seed`, `rng`, `cum`, `r`, `rv`
- `draw` (6): `self`, `surf`, `rect`, `streak`, `drift`, `key`
- `_star_col` (4): `self`, `i`, `brightness`, `base`
- `_paint` (19): `self`, `surf`, `rect`, `streak`, `drift`, `i`, `w`, `h`, `cx`, `cy`, `d`, `sx`, `sy`, `b`, `col`, `ln`, `ix`, `iy`, `dim`
- `__init__` (4): `self`, `mono`, `_vd`, `VISUAL_DETAIL`
- `_rebuild_bg` (1): `self`
- `_rend` (1): `self`
- `flash` (2): `self`, `text`
- `set_wall` (4): `self`, `factor`, `w`, `INFO_SECTIONS`
- `set_beta` (4): `self`, `d`, `c`, `hi`
- `handle_events` (9): `self`, `dt`, `keys`, `fine`, `rend`, `e`, `hit`, `name`, `r`
- `_chip_click` (10): `self`, `name`, `m`, `c`, `err`, `keep`, `_m`, `order`, `cur`, `nxt`
- `_toggle_test` (6): `self`, `c`, `v`, `keep_beta`, `keep_wall`, `keep_dest`
- `_test_tick` (4): `self`, `dt`, `c`, `v`
- `_toggle_ftl` (1): `self`
- `_key` (9): `self`, `k`, `fine`, `rend`, `c`, `v`, `_m`, `err`, `keep`
- `update` (14): `self`, `dt`, `r`, `c`, `v`, `sp`, `keys`, `thr`, `brk`, `fx`, `heat_w`, `_f0`, `hid_sp`, `hid`
- `draw` (3): `self`, `img`, `x`
- `draw_topbar` (20): `self`, `h`, `s`, `x`, `ec`, `items`, `c`, `v`, `row`, `i`, `nm`, `on`, `r`, `text`, `col`, `img`, `t`, `a`, `g`, `b`
- `draw_ship` (2): `self`, `rect`
- `draw_view_tabs` (8): `self`, `rect`, `nm`, `r`, `x`, `y`, `p`, `t`
- `draw_ship_panel` (15): `self`, `y`, `rows`, `env`, `yy`, `img`, `y2`, `need`, `lines`, `x`, `w`, `k`, `val`, `t`, `col`
- `draw_spec_card` (2): `self`, `part`
- `_spec_card` (10): `self`, `part`, `w`, `lines`, `s`, `h`, `yy`, `ln`, `x`, `y`
- `draw_metric` (55): `self`, `c`, `R`, `delta`, `b`, `rect`, `rads`, `NA`, `angs`, `NR`, `tmax`, `rr`, `amp`, `pts`, `tv`, `cam`, `focal`, `segs`, `i`, `old`, `glow_surf`, `sg`, `ang`, `sx` ...
- `draw_profiles` (35): `self`, `b`, `R`, `delta`, `y0`, `rs`, `series`, `w`, `h`, `lo`, `hi`, `idx`, `x`, `vals`, `wallx`, `i`, `title`, `col`, `logscale`, `gx`, `gy`, `gw`, `gh`, `pts` ...
- `draw_metric_panel` (24): `self`, `b`, `R`, `delta`, `E`, `Eq`, `tid`, `ec`, `rows`, `yy`, `nm`, `ln`, `y2`, `env`, `note`, `x`, `w`, `y`, `k`, `val`, `bold`, `ok`, `r`, `img`
- `draw_flight` (17): `self`, `bsafe`, `bon`, `rect`, `c`, `v`, `cxx`, `cyy`, `wash`, `b`, `fy`, `trail_r`, `tg`, `tc`, `t`, `a`, `rad`
- `draw_flight_hud` (35): `self`, `y`, `note`, `yy`, `ln`, `_tm`, `frac`, `rows`, `_vbeta`, `_vx`, `rocket`, `_drift`, `_pew`, `avail`, `_loadfrac`, `_rlim`, `_rsafe`, `_radk`, `_integ`, `led`, `_lg`, `hh`, `n`, `c` ...
- `draw_flight_controls` (8): `self`, `r`, `x`, `hints`, `y`, `c`, `v`, `img`
- `draw_dilation` (28): `self`, `R`, `beta`, `rect`, `cam`, `focal`, `shells`, `old`, `floor`, `span`, `drawn`, `rr`, `sg`, `c`, `v`, `cx0`, `cy0`, `lap`, `col`, `i`, `t`, `axis`, `zz`, `pts` ...
- `draw_dilation_graphs` (25): `self`, `beta`, `R`, `delta`, `y0`, `x`, `n`, `pts`, `i`, `rates`, `rng`, `_xvm`, `w`, `h`, `gx`, `gy`, `gw`, `gh`, `rr`, `lap`, `wx`, `xm`, `lo`, `hi` ...
- `draw_clock_panel` (21): `self`, `beta`, `v`, `cl`, `yy`, `drift`, `img`, `y2`, `beta_r`, `ln`, `x`, `w`, `y`, `name`, `rate`, `col`, `txt`, `k`, `val`, `note`, `br`
- `draw_portal` (4): `self`, `c`, `rect`, `part`
- `draw_portal_panel` (26): `self`, `ps`, `rows`, `yy`, `y_qi`, `mmp`, `vs`, `qi_paras`, `para`, `y2`, `g`, `w2`, `paras`, `q`, `by`, `lines`, `x`, `w`, `y`, `k`, `val`, `ln`, `bx`, `bw` ...
- `draw_special` (3): `self`, `rect`, `part`
- `draw_special_panel` (42): `self`, `sp`, `mph`, `state`, `sc`, `frac`, `need`, `cas`, `ship_need`, `rows`, `yy`, `y2`, `bx`, `y3`, `y4`, `hop`, `t0_show`, `tr`, `x`, `w`, `y`, `k`, `val`, `italic` ...
- `draw_ladder` (25): `self`, `ay`, `e`, `base`, `rows`, `refs`, `yy`, `need`, `msg`, `w`, `h`, `x`, `y`, `gx0`, `gx1`, `lo_e`, `hi_e`, `px`, `label`, `factor`, `status`, `_cite`, `val`, `col` ...
- `draw_help` (9): `self`, `lines`, `w`, `h`, `yy`, `x`, `y`, `k`, `t`
- `draw_info` (16): `self`, `flat`, `per`, `yy`, `frac`, `track_h`, `w`, `h`, `x`, `y`, `title`, `body`, `ln`, `kind`, `text`, `col`
- `run` (2): `self`, `dt`
- `_paint` (6): `a`, `b`, `k`, `pts`, `oww`, `outl`
- `size` (1): `t`
- `write` (2): `self`, `a`
- `flush` (1): `self`
- `_emit` (3): `tag`, `dd`, `ln`
- `col_for` (2): `t`, `base`
- `width_for` (1): `t`

## Control-flow density (decisions per function)

if/elif/else, loops, and comprehension counts per function -- where the model's complexity actually lives.

| Function | if | for | while | comp | try | return |
|----------|----|-----|-------|------|-----|--------|
| `_build_special_parts_impl` | 3 | 238 | 0 | 1 | 0 | 4 |
| `render` | 134 | 22 | 0 | 12 | 10 | 4 |
| `selftest` | 11 | 18 | 1 | 74 | 15 | 5 |
| `_component_info_sections` | 19 | 31 | 0 | 17 | 1 | 2 |
| `_build_ship_parts_impl` | 25 | 24 | 2 | 9 | 0 | 8 |
| `_key` | 37 | 0 | 0 | 0 | 0 | 0 |
| `update` | 21 | 2 | 0 | 0 | 0 | 1 |
| `_step` | 22 | 1 | 0 | 0 | 0 | 1 |
| `_prep_global` | 11 | 9 | 0 | 0 | 1 | 1 |
| `main` | 16 | 0 | 0 | 1 | 0 | 4 |
| `_function_registry_lines` | 3 | 9 | 0 | 5 | 3 | 1 |
| `_chip_click` | 19 | 0 | 0 | 0 | 1 | 1 |
| `handle_events` | 17 | 2 | 0 | 0 | 0 | 0 |
| `_prep_mesh` | 8 | 3 | 0 | 2 | 1 | 5 |
| `_prep_part` | 6 | 6 | 0 | 4 | 0 | 2 |
| `draw_metric` | 3 | 8 | 0 | 4 | 0 | 2 |
| `_deck_plate` | 2 | 9 | 0 | 3 | 0 | 3 |
| `_pipe_path` | 4 | 5 | 0 | 2 | 1 | 3 |
| `_car_loft` | 2 | 8 | 0 | 3 | 0 | 2 |
| `update` | 13 | 1 | 0 | 0 | 0 | 0 |
| `report_feasibility` | 1 | 8 | 0 | 5 | 0 | 0 |
| `_smooth_sections` | 4 | 3 | 0 | 1 | 1 | 5 |
| `fmt_time` | 6 | 0 | 0 | 0 | 0 | 7 |
| `fmt_mass` | 6 | 0 | 0 | 0 | 0 | 7 |
| `draw_special_panel` | 7 | 6 | 0 | 0 | 0 | 0 |
| `_paint` | 10 | 1 | 0 | 0 | 0 | 2 |
| `_hull_loft` | 2 | 5 | 0 | 1 | 1 | 4 |
| `draw_profiles` | 2 | 1 | 0 | 9 | 0 | 0 |
| `draw_bubble_glow` | 7 | 1 | 0 | 0 | 0 | 4 |
| `project` | 6 | 0 | 0 | 0 | 3 | 2 |
| `multijump_plan` | 7 | 1 | 0 | 0 | 0 | 3 |
| `_xform` | 5 | 0 | 0 | 0 | 1 | 5 |
| `_test_tick` | 6 | 0 | 0 | 0 | 0 | 5 |
| `_spec_key_lines` | 2 | 4 | 1 | 0 | 1 | 3 |
| `portal_traversal` | 9 | 0 | 0 | 0 | 0 | 1 |
| `draw_vignette` | 5 | 2 | 0 | 0 | 0 | 3 |
| `_mt_funnel` | 1 | 5 | 0 | 2 | 0 | 2 |
| `_coil_arc` | 1 | 7 | 0 | 0 | 0 | 2 |
| `report_portal_test` | 4 | 5 | 0 | 0 | 0 | 0 |
| `magsail_decel_time_s` | 4 | 0 | 0 | 0 | 0 | 5 |

(top 40 by total -- the rest are linear pass-throughs)

## The mutation map (who WRITES shared state)

The dependency map above shows reads; this is the write side -- every site that mutates DIMS/PLANT/DRIVE or credits the honesty ledger, AST-extracted. Almost nothing writes spec state: that's the point.

### Spec-dict writes (DIMS/PLANT/DRIVE)

| Line | Writer | Key |
|------|--------|-----|
| 13231 | `selftest` | `DIMS.'coils'` |
| 13232 | `selftest` | `DIMS.'magsail_r_km'` |
| 13233 | `selftest` | `DIMS.'casimir_pitch_nm'` |
| 13234 | `selftest` | `DIMS.'bubble_r_m'` |
| 13235 | `selftest` | `DIMS.'ring_sectors'` |
| 13236 | `selftest` | `DIMS.'hull_decks'` |
| 13237 | `selftest` | `DIMS.'portal_coils'` |
| 13238 | `selftest` | `DIMS.'coil_temp_k'` |
| 13239 | `selftest` | `DIMS.'crew'` |
| 13240 | `selftest` | `DIMS.'coil_turns'` |
| 13263 | `selftest` | `PLANT.'conversion_eff'` |
| 13264 | `selftest` | `PLANT.'d3he_j_kg'` |
| 13265 | `selftest` | `PLANT.'beam_aperture_km'` |
| 13281 | `selftest` | `DIMS.'radiators'` |
| 13294 | `selftest` | `DIMS.'collector_deploy_km'` |
| 13362 | `selftest` | `DIMS.'collector_deploy_km'` |
| 13369 | `selftest` | `DIMS.'collector_deploy_km'` |
| 13405 | `selftest` | `DIMS.'hull_density'` |
| 16583 | `set_wall` | `DIMS.'wall_thick_m'` |
| 16735 | `_toggle_test` | `DIMS.'wall_thick_m'` |
| 16681 | `_chip_click` | `DIMS.'wall_thick_m'` |
| 16892 | `_key` | `DIMS.'wall_thick_m'` |

Reads: `App` writes `wall_thick_m` at the three places the wall can change (set_wall, reset restore, TEST prep); every other DIMS/PLANT write lives in `selftest` as corrupt/restore fixtures for the hostile-input checks -- production code treats the spec as read-only.

### Honesty-ledger credits (`core.led[...] +=`)

| Line | Creditor | Ledger key |
|------|----------|------------|
| 13207 | `selftest` | `'beam_in'` |
| 9597 | `_thermal` | `'radiated'` |
| 9718 | `update` | `'plant_out'` |
| 9719 | `update` | `'fuel_kg'` |
| 9883 | `_step` | `'beam_in'` |
| 9953 | `_step` | `'kinetic'` |
| 9954 | `_step` | `'kinetic_peak'` |
| 9973 | `_step` | `'ism_particles'` |
| 9681 | `update` | `_lk` |
| 9924 | `_step` | `'magsail_regen'` |
| 9926 | `_step` | `'brake_dissipated'` |

Two crediting sites only: `WarpCore.update` books plant/radiator/fuel/exotic; `Voyage._step` books beam-in/kinetic/ISM/braking -- matching the two-ledgers architecture the honesty audit verifies.

### Cache invalidation

- `INFO_SECTIONS = None` in `set_wall` -- the I panel re-derives on next open so it never quotes a stale wall
- `core.__init__()` re-run on reset -- all live state derives fresh from DIMS, no stale caches survive a mission reset

## The frame tick (App.update order)

The top-level loop, in real order:

1. sanitize `dt` (non-finite or negative -> 0)
2. advance `anim` clock, decay `msg_t` toast timer
3. if paused: skip physics entirely
4. FLIGHT tab: `voy.update(dt, core)` then `_test_tick(dt)` if TEST
5. other tabs: `core.update(dt * 4.0, voy)` -- the drive runs at 4x real-time off the flight tab so thermal/integrity transients are visible
6. tick all three renderers (ship, flight, portal)
7. recompute hidden parts: 'bubble' hidden when bubble_on < 0.03, 'magsail' hidden until deployed -- except exploded/assembly views on the SHIP tab show everything

## The precision contract (every format spec in use)

How many digits each kind of number is allowed -- the `%`-format census across the file.

| Spec | Sites | Typical use |
|------|-------|-------------|
| `%s` | 376 | preformatted values, notes, prose |
| `%.0f` | 310 | counts, Kelvin, masses, years |
| `%.1f` | 207 | temps, seconds, metres, percentages |
| `%.2f` | 197 | betas, seconds, sizes |
| `%d` | 114 | integer counts, indices |
| `%.3g` | 79 | physics magnitudes (forces, densities) |
| `%.3e` | 61 | scientific notation energies |
| `%.2e` | 60 | tidal/shear extremes |
| `%.3f` | 49 | betas, fractions |
| `%.4f` | 42 | emergent beta, rates |
| `%.4e` | 40 | order-sensitive quantities |
| `%.6f` | 30 | shape-function values |
| `%.4g` | 18 |  |
| `%.1e` | 16 |  |
| `%.0e` | 10 |  |
| `%02d` | 8 | section numbering |
| `%.9f` | 7 | clock rates (the 1e-9 regime) |
| `%.12f` | 5 | deep-space flatness checks |
| `%10s` | 4 |  |
| `%12s` | 3 |  |
| `%.15f` | 3 | rate-consistency proofs |
| `%g` | 3 |  |
| `%4d` | 2 |  |
| `%.2g` | 2 |  |
| `%8s` | 2 |  |
| `%.6e` | 2 |  |
| `%.5f` | 2 |  |
| `%3d` | 1 |  |
| `%6s` | 1 |  |
| `%.6g` | 1 |  |
| `%.1g` | 1 |  |

1656 format sites total.

## Call-site argument map (what each caller passes)

For the load-bearing functions, every call site and its literal arguments -- who exercises which part of each domain.

### `shape_f` -- 13 call sites

- L3686: `(r, R, delta)`
- L10372: `(r, R, d0)`
- L11240: `(0.0, R, 1.0)`
- L11241: `(0.0, R, 1.0)`
- L11242: `(R + 40.0, R, 1.0)`
- L11243: `(R + 40.0, R, 1.0)`
- L11244: `(R, R, 1.0)`
- L11245: `(R, R, 1.0)`
- L12543: `(R, R, delta_ext)`
- L12994: `(0.0, 45.86, _nan)`
- L13312: `(1.0)`
- L13312: `(1.0, None)`
- L17336: `(r, R, delta)`

### `york_theta` -- 4 call sites

- L11272: `(+R, 1.0, 1.0, R, 1.0)`
- L11273: `(-R, 1.0, 1.0, R, 1.0)`
- L14763: `(R, 1.0, 1.0, R, d0)`
- L17231: `(z, abs(y), b, R, delta)`

### `alcubierre_energy_j` -- 43 call sites

- L2956: `(1.0, R, d0)`
- L2984: `(1.0, R, delta_max)`
- L6018: `(1.0, d['bubble_r_m'], 1.0)`
- L6035: `(1.0, d['bubble_r_m'], ford_roman_wall_limit(1.0))`
- L7062: `(1.0, CAR_BUBBLE_R, CAR_WALL_M)`
- L9728: `(max(self.beta, 1.0), DIMS['bubble_r_m'], self.wall_m)`
- L10379: `(1.0, R, delta)`
- L10388: `(b, R, d0)`
- L10410: `(1.0, R, 1.0)`
- L10411: `(1.0, R, ford_roman_wall_limit(1.0))`
- L10422: `(1.0, DIMS['bubble_r_m'], 1e-15)`
- L10778: `(1.0, R, 1.0)`
- L10844: `(1.0, R, ford_roman_wall_limit(1.0))`
- L10915: `(1.0, DIMS['bubble_r_m'], 1.0)`
- L11257: `(10.0, 100.0, 1e-15)`
- L11262: `(1.0, R, 1.0)`
- L11263: `(1.0, R, 1.0)`
- L11761: `(1.0, 100.0, 1.0)`
- L11762: `(2.0, 100.0, 1.0)`
- L11767: `(1.0, 100.0, 1.0)`
- L11768: `(1.0, 100.0, 0.1)`
- L11774: `(1.0, 100.0, 1.0)`
- L11943: `(1.0, CAR_BUBBLE_R, CAR_WALL_M)`
- L11944: `(1.0, CAR_BUBBLE_R, CAR_WALL_M)`
- L11950: `(1.0, CAR_BUBBLE_R, CAR_WALL_M)`
- L11953: `(1.0, CAR_BUBBLE_R, CAR_WALL_M)`
- L12599: `(1.0, 100.0, 10.0)`
- L12600: `(1.0, 100.0, 0.01)`
- L14325: `(1.0)`
- L14332: `(1.0)`
- L14712: `(1.0, R, 1.0)`
- L14713: `(1.0, R, ford_roman_wall_limit(1.0))`
- L14778: `(1.0, R, 12.0)`
- L14781: `(1.0, R, 1e-15)`
- L17155: `(1.0, DIMS['bubble_r_m'], self.core.wall_m)`
- L17389: `(b, R, delta)`
- L17390: `(b, R, ford_roman_wall_limit(max(1.)`
- L18150: `(1.0, CAR_BUBBLE_R, CAR_WALL_M)`
- L18152: `(1.0, DIMS['bubble_r_m'], self.core.wall_m)`
- L18344: `(1.0, DIMS['bubble_r_m'], 1e-15)`
- L18397: `(1.0, DIMS['bubble_r_m'], self.core.wall_m)`
- L18518: `(1.0, DIMS['bubble_r_m'], 1.0)`
- L18522: `(1.0, DIMS['bubble_r_m'], 1.0)`

### `beam_power_w` -- 10 call sites

- L3341: `(max(1.0, x))`
- L3464: `(r)`
- L9713: `(max(1.0, rng))`
- L9875: `(max(1.0, self.x_m))`
- L12978: `(float('nan'))`
- L15709: `(0.01 * LY)`
- L15710: `(0.1 * LY)`
- L15711: `(0.2 * LY)`
- L15712: `(0.5 * LY)`
- L15713: `(0.62 * LY)`

### `beam_brake_force_n` -- 7 call sites

- L3471: `(0.02 * LY)`
- L9910: `(self.remaining_m + 0.002 * L)`
- L10022: `(0.02 * LY)`
- L11680: `(0.02 * LY)`
- L12979: `(float('nan'))`
- L14935: `(0.02 * LY)`
- L15315: `(0.02 * LY)`

### `magsail_drag_n` -- 10 call sites

- L6243: `(0.5)`
- L6244: `(0.5)`
- L9908: `(self.beta)`
- L11669: `(0.5)`
- L11677: `(0.5)`
- L11677: `(1.0)`
- L12589: `(0.0)`
- L12590: `(1.0)`
- L14925: `(0.5)`
- L15329: `(0.5)`

### `kinetic_energy_j` -- 63 call sites

- L3331: `(beta, m)`
- L5822: `(0.5)`
- L5824: `(0.5)`
- L5862: `(0.5)`
- L6144: `(0.5)`
- L9576: `(_real(self.beta))`
- L9884: `(min(self.beta, 0.999999))`
- L9953: `(min(self.beta, 0.999999))`
- L10436: `(0.5)`
- L10807: `(0.5)`
- L10914: `(0.5)`
- L11289: `(0.6)`
- L11290: `(0.6)`
- L11292: `(1.0)`
- L11343: `(bcap)`
- L11344: `(0.9)`
- L11345: `(0.6)`
- L11350: `(0.99)`
- L11361: `(0.9)`
- L12559: `(0.0)`
- L12561: `(1.0)`
- L12563: `(1.5)`
- L12915: `(-5.0)`
- L12916: `(5.0)`
- L14800: `(0.1)`
- L14801: `(0.5)`
- L14802: `(0.9)`
- L14897: `(bcap)`
- L15266: `(0.5)`
- L15694: `(bcap)`
- L15695: `(0.9)`
- L15695: `(bcap)`
- L15696: `(0.99)`
- L15696: `(bcap)`
- L15726: `(bcap)`
- L15727: `(0.86)`
- L15728: `(0.9)`
- L15729: `(0.86)`
- L15729: `(bcap)`
- L15758: `(bcap)`
- L15759: `(0.9)`
- L15759: `(bcap)`
- L15760: `(0.95)`
- L15760: `(bcap)`
- L15761: `(0.99)`
- L15761: `(bcap)`
- L15762: `(0.999)`
- L15762: `(bcap)`
- L15775: `(bcap)`
- L15792: `(bcap)`
- L17159: `(0.5)`
- L18350: `(0.5)`
- L18515: `(0.5)`

### `mouth_clock_rate` -- 18 call sites

- L4456: `(phi_over_c2, beta)`
- L4904: `(mouth_a_phi_c2, mouth_a_beta)`
- L4905: `(mouth_b_phi_c2, mouth_b_beta)`
- L11513: `(0.0, 0.0)`
- L11516: `(-0.1, 0.0)`
- L11519: `(0.0, 0.5)`
- L11523: `(-1e-08, 0.0001)`
- L11809: `(phi_c2_test, 0.5)`
- L12567: `(-0.5, 0.0)`
- L12568: `(-0.5, 0.0)`
- L12570: `(0.0, 1.0)`
- L12571: `(0.0, 1.0)`
- L12573: `(-0.49, 0.0)`
- L12574: `(-0.49, 0.0)`
- L15602: `(-0.3, 0.99)`
- L15604: `(-0.3, 0.99)`
- L15607: `(-0.45, 0.999)`
- L15609: `(-0.45, 0.999)`

### `mt_tidal_g` -- 13 call sites

- L4247: `(a_m)`
- L4743: `(b0)`
- L4927: `(b0_m, payload_size_m)`
- L11458: `(b0)`
- L11751: `(b0, 2.0)`
- L11752: `(b0, 2.0)`
- L11757: `(b0_min, 2.0)`
- L11758: `(b0_min, 2.0)`
- L12880: `(0.0)`
- L12940: `(12.0, -1.0)`
- L12988: `(12.0, _nan)`
- L13023: `(b0)`

### `warp_energy_integral` -- 11 call sites

- L2793: `(R, delta)`
- L11250: `(R, delta)`
- L11773: `(100.0, 1.0)`
- L12864: `(R, 0.0)`
- L12865: `(R, 0.0)`
- L12867: `(R, d0, 1)`
- L12868: `(R, d0, 0)`
- L12937: `(-5.0, d0)`
- L12938: `(0.0, d0)`
- L12989: `(_nan, 0.2)`
- L12990: `(45.86, _nan)`

## Special-forms census (every exotic construct)

The unusual syntax in the file, AST-counted -- what's exotic and what's deliberately absent.

| Form | Count | Detail |
|------|-------|--------|
| dunder methods | 9 | `__getitem__`, `__init__` |
| decorators | 8 | `_wrapped`@functools.wraps(fn), `mode`@property, `exotic`@property, `warp`@property, `beta`@property, `remaining_m`@property, `auto_done`@property, `size`@staticmethod |
| `global` | 10 | `EARTH_ORBIT_RATE`, `INFO_SECTIONS`, `VISUAL_DETAIL`, `_SEG_FLOOR` |
| `ternary` | 528 | the house style -- clamps and coercions inline |
| `lambda` | 8 | sort keys and tiny adapters only |
| `assert` | 0 | NONE -- selftest uses check(), never bare assert |
| `yield` | 0 | NONE -- no generators; all sequences materialized |
| `del` | 1 | one site |
| `nonlocal` | 0 | NONE -- no closures write enclosing scope |
| `await` | 0 | NONE -- no async anywhere |
| `star-import` | 0 | NONE -- every name is explicitly imported |

Single inheritance in the file: `_Dims(dict)`. No metaclasses, no mixins, no ABCs -- one honest subclass.

## Verification

| Suite | Count |
|-------|-------|
| `--selftest` | 417/417 physics checks |
| `_scale_audit.py` | 70/70 independent recomputations from DIMS |
| Honesty audit | 12/12 conservation checks |
| Info panel | 39 sections (press I in the viewer) |
| Specification keys documented | 100 DIMS + 12 PLANT + 8 DRIVE = 120, all above |

### Coverage attestation

| Surface | Items | Present | Missing |
|---------|-------|---------|---------|
| spec keys (DIMS+PLANT+DRIVE) | 120 | 120 | none |
| public functions | 150 | 150 | none |
| private functions | 51 | 51 | none |
| classes | 9 | 9 | none |
| component names | 23 | 23 | none |
| info-panel section titles | 39 | 39 | none |
| literal self-test labels | 383 | 383 | none |

Every enumerated surface is fully present: no spec key, function, class, component, panel section, or check label is absent from this document.
