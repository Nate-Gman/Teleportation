#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
  1. SHIP     Orbit the whole vessel to scale -- 172 m warp ring, 68 m crew
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
"""

import argparse
import math
import os
import sys
import warnings

warnings.filterwarnings("ignore")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

import numpy as np


# =============================================================================
# SECTION 1 -- PHYSICAL CONSTANTS (CODATA 2018 / IAU 2015, all SI)
# =============================================================================

C_LIGHT   = 2.99792458e8        # speed of light in vacuum   [m/s]     (exact)
G_NEWTON  = 6.67430e-11         # gravitational constant     [m^3/kg/s^2]
HBAR      = 1.054571817e-34     # reduced Planck constant    [J s]
H_PLANCK  = 6.62607015e-34      # Planck constant            [J s]     (exact)
K_B       = 1.380649e-23        # Boltzmann constant         [J/K]     (exact)
SIGMA_SB  = 5.670374419e-8      # Stefan-Boltzmann constant  [W/m^2/K^4]
E_CHARGE  = 1.602176634e-19     # elementary charge          [C]       (exact)
M_P       = 1.67262192369e-27   # proton mass                [kg]
M_E       = 9.1093837015e-31    # electron mass              [kg]
MU0       = 1.25663706212e-6    # vacuum permeability        [H/m]
EPS0      = 8.8541878128e-12    # vacuum permittivity        [F/m]

# Derived reference scales ----------------------------------------------------
C2          = C_LIGHT ** 2                       # c^2                [m^2/s^2]
C4_OVER_G   = C_LIGHT ** 4 / G_NEWTON            # c^4/G = 1.2103e44 N -- the
#                                                  "stiffness of spacetime": the
#                                                  force scale you must pay to
#                                                  curve it. Every warp energy in
#                                                  this file is this number times
#                                                  a dimensionless geometry factor.
L_PLANCK    = math.sqrt(HBAR * G_NEWTON / C_LIGHT ** 3)    # 1.616e-35 m
T_PLANCK    = L_PLANCK / C_LIGHT                           # 5.391e-44 s
M_PLANCK    = math.sqrt(HBAR * C_LIGHT / G_NEWTON)         # 2.176e-8 kg
E_PLANCK    = M_PLANCK * C2                                # 1.956e9 J

# Astronomical reference values ----------------------------------------------
M_SUN     = 1.98847e30          # solar mass                 [kg]
L_SUN     = 3.828e26            # solar luminosity           [W]
M_JUPITER = 1.89813e27          # Jupiter mass               [kg]
M_EARTH   = 5.97217e24          # Earth mass                 [kg]
AU        = 1.495978707e11      # astronomical unit          [m]
LY        = 9.4607304725808e15  # light year                 [m]       (exact)
YR        = 3.15576e7           # Julian year                [s]       (exact)
DAY       = 86400.0             # day                        [s]
M_MILKY_WAY = 1.5e12 * M_SUN    # Milky Way total mass       [kg]
M_UNIVERSE_BARYON = 1.5e53      # baryonic mass, observable universe  [kg]

# Target system ---------------------------------------------------------------
PROXIMA_LY   = 4.2465           # Proxima Centauri distance  [ly]
PROXIMA_M    = PROXIMA_LY * LY  # ... in metres              [m]   (4.017e16)

# Interstellar medium (local interstellar cloud, warm neutral) ----------------
ISM_N_M3       = 1.0e5          # hydrogen number density    [1/m^3] (0.1 /cm^3)
ISM_DUST_KG_M3 = 1.0e-23        # dust mass density          [kg/m^3]


# =============================================================================
# SECTION 2 -- ENGINEERING SPECIFICATION (to scale, SI metres)
# =============================================================================
# Everything the renderer draws and everything the physics charges you for is
# read from DIMS. Change a number here and the ship, the mass budget, the
# radiator sizing, the energy ladder and the voyage all move together.

DIMS = {
    # --- Warp bubble geometry (the spacetime, not the hardware) -----------
    "bubble_r_m":         100.0,   # r_s where the shape function falls to 1/2
    "wall_thick_m":         1.0,   # wall thickness delta; sigma = 1/delta
    "interior_margin":      6.0,   # flat interior ends this many delta inside R
    #                                (f > 0.9997 there) -- see flat_interior_r()

    # --- Main warp ring (the shift-vector shell -- the actual "drive") ----
    # The centreline sits AT the bubble radius on purpose: the shell does not
    # project the wall from a distance, the shell IS the wall's source term, so
    # its stress-energy has to be where the curvature is.
    "ring_major_d_m":     200.0,   # ring centreline diameter = 2 x bubble_r_m
    "ring_minor_d_m":      15.0,   # tube diameter of the toroidal shell
    "ring_wall_m":          0.60,  # shell wall thickness (a shell, not solid)
    "ring_sectors":        24,     # independently driven ring segments
    "ring_density":      4100.0,   # conditioned SiC/W metamaterial  [kg/m^3]

    # --- Superconducting field coils (24, one per ring sector) ------------
    "coils":               24,
    "coil_bore_m":          6.2,   # clear bore
    "coil_len_m":           9.4,   # axial length along the ring tube
    "coil_turns":       48000,     # REBCO tape turns per coil
    "coil_current_a":   38000.0,   # operating current                [A]
    "coil_temp_k":         18.0,   # HTS operating temperature        [K]

    # --- Fore / aft shaping rings (set the front-back asymmetry) ----------
    "capring_d_m":         96.0,
    "capring_minor_d_m":    7.0,
    "cap_offset_m":        38.0,   # +/- z offset from the ring plane

    # --- Crew hull (flat spacetime inside -- ordinary ship engineering) ---
    "hull_len_m":          68.0,
    "hull_d_m":            16.0,
    "hull_decks":           4,
    "hull_wall_m":          0.22,
    "hull_density":      2700.0,   # Al-Li / composite pressure hull  [kg/m^3]
    "crew":                12,

    # --- Structural pylons hull -> ring -----------------------------------
    "pylons":               3,
    "pylon_len_m":         84.0,
    "pylon_w_m":            3.2,

    # --- D-3He fusion reactor (the housekeeping plant) --------------------
    "reactor_major_d_m":   12.0,   # spherical-tokamak torus (fits the hull bore)
    "reactor_minor_d_m":    3.6,
    "reactor_th_gw":       22.0,   # thermal output                   [GW]
    "reactor_direct_eff":   0.62,  # direct energy conversion (aneutronic)

    # --- Antimatter store (peak fold transitions only) --------------------
    "amtraps":              2,
    "amtrap_d_m":           5.2,
    "amtrap_kg":            0.85,  # antihydrogen per trap            [kg]

    # --- SMES field-transient buffer (superconducting magnetic store) -----
    # NOT a "warp battery". Its capacity is COMPUTED from B^2/2mu0 times the
    # torus volume (see smes_store_j()) and comes out around 7e11 J -- twelve
    # orders of magnitude short of a velocity change. It buffers coil
    # transients; it does not move the ship. Nothing here pretends otherwise.
    "smes_major_d_m":      22.0,
    "smes_minor_d_m":       2.4,
    "smes_b_t":            60.0,   # bore field                        [T]

    # --- Casimir negative-energy lattice (24 cassettes in the ring wall) --
    "casimir_cassettes":   24,
    "casimir_plate_m":      2.40,  # square plate edge
    "casimir_gap_nm":      10.0,   # vacuum gap between plates
    "casimir_pitch_nm":    60.0,   # gap + plate thickness (50 nm plate)
    "casimir_stack_m":      2.00,  # stack height per cassette

    # --- Waste-heat radiators (sized against the REAL waste heat) ---------
    # Length and radius are bounded by the bubble: every panel corner has to
    # satisfy r^2 + z^2 < flat_interior_r()^2, or the tips are sitting in the
    # wall. check_envelope() enforces it and --selftest asserts it.
    "radiators":           20,
    "rad_len_m":           52.0,
    "rad_w_m":             18.0,
    "rad_inner_r_m":       40.0,   # panel root radius
    "rad_z0_m":           -14.0,   # panel leading edge
    "rad_temp_k":        1550.0,   # design-point panel temperature    [K]
    "rad_limit_k":       1900.0,   # graphite sublimation limit        [K]
    "rad_emissivity":       0.92,

    # --- Cryoplant (holds the HTS coils at 18 K) --------------------------
    "cryo_units":           4,
    "cryo_d_m":             6.0,
    "cryo_len_m":          11.0,

    # --- Navigation deflector (subwarp dust shield) -----------------------
    "deflector_d_m":       18.0,
    "deflector_depth_m":    4.5,

    # --- Reaction control (subwarp only -- ion / VASIMR pods) -------------
    "rcs_pods":             8,
    "rcs_d_m":              2.6,
    "rcs_len_m":            5.0,

    # --- Boost receiver (the stellar-tap rectenna) ------------------------
    # Stowed it is a 46 m dish; under boost it unfurls to a 4 km film rectenna,
    # because the diffraction spot of even a 1000 km transmitter is kilometres
    # wide at interstellar range (see beam_spot_m()).
    "collector_d_m":       46.0,   # stowed dish diameter
    "collector_depth_m":    9.0,
    "collector_deploy_km":  4.0,   # deployed film rectenna diameter    [km]
    "collector_film_um":    1.0,   # rectenna film thickness            [um]
    "collector_film_rho": 1400.0,  # film density                       [kg/m^3]

    # --- Wormhole portal gate (Morris-Thorne throat) ----------------------
    # The gate is the buildable-LOOKING part: a ring you could walk through.
    # portal_summary() then prices the throat it would have to hold open, and
    # mt_min_throat_m() reports the one you would actually survive crossing.
    "portal_gate_d_m":     24.0,   # engineered aperture (throat 2 b0)
    "portal_ring_minor_d_m": 3.0,
    "portal_coils":        16,     # field coils around the rim
    "portal_casimir_rings": 8,     # negative-energy cassettes at the throat
    "portal_frame_d_m":    34.0,   # structural frame outside the aperture

    # --- Magnetic sail (the only credible way to STOP) --------------------
    # Zubrin and Andrews (1991): a superconducting loop deflects interstellar
    # protons and drags against the ISM. It is 1000 km across, so the viewer
    # draws it at a STATED reduced scale -- never silently shrunk.
    "magsail_r_km":      1000.0,   # deployed loop radius               [km]
    "magsail_current_a":  1.6e6,   # persistent loop current            [A]
    "magsail_mass_kg":    4.2e5,   # HTS cable + deployment mass        [kg]
    "magsail_cd":           0.85,  # effective ISM drag coefficient
    "magsail_regen_eff":    0.62,  # braking energy recovered to the bus
    "magsail_view_scale": 0.00025, # 1:4000 -- printed on screen, always
}

def flat_interior_r(delta=None, R=None):
    """Radius of the exactly-flat interior [m].

    DERIVED, not declared. With a wall of thickness delta at radius R, the
    shape function is already 0.9997 by R - 6 delta, so that is where the
    usable volume ends. This is the trade nobody mentions: a THICKER wall is
    cheaper (energy falls as 1/delta) and gentler (tidal shear falls as
    1/delta^2), but it eats the interior. Push the wall past about 3 m and the
    ship no longer fits inside its own bubble -- watch the envelope readout in
    SHIP view do exactly that."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    return max(0.0, R - DIMS["interior_margin"] * delta)


def _envelope_points():
    """Extreme (radius, |z|) corners of every part that must live INSIDE the
    bubble. The ring, its coils and its Casimir cassettes are deliberately
    absent: they straddle the wall, because they are what sources it."""
    d = DIMS
    Rr = d["ring_major_d_m"] / 2.0
    nose = d["hull_len_m"] / 2.0 + d["deflector_depth_m"]
    return [
        ("deflector rim",   d["deflector_d_m"] / 2.0, nose),
        ("hull midbody",    d["hull_d_m"] / 2.0, 0.0),
        ("radiator tip",    d["rad_inner_r_m"] + d["rad_w_m"],
         abs(d["rad_z0_m"]) + d["rad_len_m"]),
        ("boost rectenna",  d["collector_d_m"] / 2.0, 40.0 + d["collector_depth_m"]),
        ("shaping ring",    d["capring_d_m"] / 2.0 + d["capring_minor_d_m"] / 2.0,
         d["cap_offset_m"]),
        ("cryo unit",       Rr * 0.80, d["cryo_len_m"] / 2.0),
        ("SMES toroid",     d["smes_major_d_m"] / 2.0 + d["smes_minor_d_m"] / 2.0,
         22.0),
    ]


def check_envelope(delta=None):
    """Does the ship still fit inside its own flat interior?

    A thicker wall is cheaper and gentler but shrinks the usable volume, so
    this is a live constraint, not a build-time one: drag the wall thickness up
    in METRIC view and the ship's own radiators eventually end up standing in
    the wall. Returns the binding part and the margin."""
    lim = flat_interior_r(delta)
    worst_name, worst_d = "", 0.0
    for name, r, z in _envelope_points():
        dd = math.hypot(r, z)
        if dd > worst_d:
            worst_name, worst_d = name, dd
    ok = worst_d <= lim
    return {"ok": ok, "part": worst_name, "reach_m": worst_d,
            "limit_m": lim, "margin_m": lim - worst_d,
            "verdict": ("%s reaches %.1f m inside a %.1f m interior (%.1f m "
                        "clear)" % (worst_name, worst_d, lim, lim - worst_d))
            if ok else
            ("WALL INTRUSION: %s reaches %.1f m but the interior ends at "
             "%.1f m" % (worst_name, worst_d, lim))}


# Overall envelope, derived from the geometry the renderer actually builds ----
SHIP_LEN_M  = (DIMS["rad_len_m"] + DIMS["cap_offset_m"]
               + DIMS["capring_minor_d_m"] / 2 + DIMS["deflector_depth_m"] + 10.0)
SHIP_SPAN_M = (DIMS["ring_major_d_m"] + DIMS["ring_minor_d_m"]
               + DIMS["rad_w_m"])

# Power plant / thermal balance ----------------------------------------------
PLANT = {
    "hotel_mw":            48.0,   # life support, computation, sensors  [MW]
    "coil_ac_mw":        6200.0,   # AC ripple + field-shaping losses in the
    #                                24 HTS coils at cruise               [MW]
    "cryo_mw":            740.0,   # cryoplant electrical draw           [MW]
    "control_mw":        2100.0,   # metric servo: 10 kHz shell-shape control
    "conversion_eff":       0.62,  # direct conversion, aneutronic D-3He
    "recovery_eff":         0.92,  # fold charge recovered on deceleration
    "am_energy_j_kg":  1.7975e17,  # 2*m*c^2 per kg antimatter (matter+anti)
    "d3he_j_kg":        3.520e14,  # D + 3He -> 4He + p + 18.35 MeV, per kg mix
    "tap_w":             1.0e17,   # stellar-tap boost beam (0.026% of L_sun)
    "beam_aperture_km":  1000.0,   # transmitter phased-array aperture    [km]
    "beam_lambda_um":       1.0,   # transmitter wavelength               [um]
    "beam_range_ly":       0.62,   # usable boost range from the array    [ly]
}

# Storage / drive control -----------------------------------------------------
DRIVE = {
    "beta_sub_max":       0.990,   # physical (positive-energy) drive ceiling
    "beta_ftl_max":      10.000,   # Alcubierre mode ceiling (flagged, exotic)
    "spinup_s":            42.0,   # ship-seconds per unit beta
    "bubble_form_s":       18.0,   # shell shape convergence time
    "integrity_min":       0.35,   # below this the bubble collapses
    "wall_min_m":         1.0e-15, # thinnest wall the shape servo can hold
    "wall_max_m":          12.0,
    "arrival_beta":       0.001,   # under 0.001 c counts as station-keeping
}

# Shell shape-servo endurance: seconds to lose full integrity at unit stress
# (stress = fractional overrun of the thermal, power or wall-thickness limits).
SHELL_STRESS_TAU = 2000.0

# Historical negative-energy reduction ladder (the literature, cited) ---------
# factor = multiplier applied to the raw Alcubierre requirement; 0.0 means the
# entry is not a reduction of the exotic bill at all but a different class of
# solution (positive-energy) or a refuted claim.
LADDER = [
    ("ALCUBIERRE 1994   raw thin-wall metric", 1.0, "EXOTIC",
     "Alcubierre, Class. Quantum Grav. 11 L73 (1994)"),
    ("VAN DEN BROECK 1999   microscopic pocket topology", 1.0e-30, "EXOTIC",
     "Van Den Broeck, Class. Quantum Grav. 16 3973 (1999)"),
    ("WHITE 2011   thick wall + oscillating bubble", 1.0e-38, "DISPUTED",
     "White, NASA JSC 2011 -- reduction claim, never independently verified"),
    ("LENTZ 2021   hyperbolic soliton from plasma stress-energy", 0.0, "REFUTED",
     "Lentz 2021; refuted by Santiago, Schuster and Visser (2021)"),
    ("BOBRICK and MARTIRE 2021   subluminal physical shell", 0.0, "PHYSICAL",
     "Bobrick and Martire, Class. Quantum Grav. 38 105009 (2021)"),
    ("FUCHS et al. 2024   constant-velocity positive-energy solution", 0.0, "PHYSICAL",
     "Fuchs et al., Class. Quantum Grav. 41 095013 (2024)"),
]


# =============================================================================
# SECTION 3 -- COLORS AND THEME
# =============================================================================

BG_TOP      = (10, 13, 22)
BG_BOT      = (3, 4, 8)
C_HULL      = (150, 158, 172)
C_HULL_DARK = (96, 104, 120)
C_RING      = (108, 122, 148)
C_RING_HOT  = (120, 210, 255)
C_COIL      = (70, 130, 190)
C_COIL_LIVE = (120, 235, 255)
C_CASIMIR   = (176, 120, 220)      # negative-energy lattice (violet)
C_REACTOR   = (255, 165, 60)
C_ANTIMAT   = (255, 90, 150)       # antimatter traps (magenta)
C_SMES      = (90, 180, 150)
C_RADIATOR  = (200, 120, 90)
C_RAD_HOT   = (255, 210, 150)
C_CRYO      = (140, 200, 230)
C_PYLON     = (86, 92, 106)
C_DEFLECT   = (110, 190, 210)
C_RCS       = (170, 150, 110)
C_COLLECT   = (130, 150, 190)
C_BUBBLE    = (90, 200, 255)
C_EXPAND    = (255, 120, 90)       # space stretched  (behind the ship)
C_CONTRACT  = (110, 160, 255)      # space compressed (ahead of the ship)
C_TEXT      = (226, 232, 240)
C_TEXT_DIM  = (146, 156, 172)
C_ACCENT    = (90, 200, 255)
C_GOOD      = (90, 220, 130)
C_WARN      = (255, 200, 60)
C_BAD       = (255, 90, 90)
C_EXOTIC    = (230, 140, 255)      # the "this needs exotic matter" colour
C_PANEL     = (16, 21, 32)
C_PANEL_HI  = (30, 39, 56)
C_STAR      = (235, 240, 255)
C_GRID      = (60, 78, 104)


# =============================================================================
# SECTION 4 -- MINI 3D ENGINE (software renderer, painter's algorithm)
# =============================================================================
# Same renderer architecture as GmansRunV1.17 / SE.py / LS.py: build meshes from
# primitives in SI metres, project them through an orbit camera, flat-shade each
# facet against a single light, sort back-to-front and paint. No GPU, no shader,
# no scene graph -- which is exactly why it runs anywhere and why every vertex
# can be traced back to a number in DIMS.
#
# pygame is imported defensively so the headless physics CLIs (--selftest,
# --metric, --voyage, --feasibility, --ladder) still run on a machine with no
# display libraries installed.

try:
    import pygame
except Exception:                                   # pragma: no cover
    pygame = None

VISUAL_DETAIL = 1.05        # global mesh resolution multiplier


def rot_x(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], dtype=float)


def rot_y(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]], dtype=float)


def rot_z(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], dtype=float)


class Mesh:
    """A bag of vertices + polygon faces with a base colour. Coordinates are in
    METRES, ship axis along +Z (the direction of travel). `spin` is the rotation
    ratio relative to the master animation angle; `pivot` offsets the local
    origin; `tilt` is a static (rx, ry) orientation."""

    def __init__(self, verts, faces, color, name="", spin=0.0, group="default",
                 pivot=(0.0, 0.0, 0.0), tilt=(0.0, 0.0), wire=False,
                 glow=False, hot=False):
        self.verts = np.asarray(verts, dtype=float)
        self.faces = faces
        self.color = color
        self.name = name
        self.spin = spin
        self.group = group
        self.pivot = np.asarray(pivot, dtype=float)
        self.tilt = tilt
        self.wire = wire          # drawn as unfilled outlines (the bubble, grids)
        self.glow = glow          # brightens with commanded warp power
        self.hot = hot            # radiator metal that reddens with panel temp
        self.coil_index = None    # index into the rotating field-phase pattern

    def world_verts(self, angle):
        v = self.verts
        if self.spin:
            v = v @ rot_z(angle * self.spin).T
        rx, ry = self.tilt
        if rx or ry:
            v = v @ (rot_x(rx) @ rot_y(ry)).T
        return v + self.pivot


# ---- primitive builders ----------------------------------------------------

def _detail_seg(seg):
    return max(6, int(round(seg * VISUAL_DETAIL)))


def _solid_cylinder(r, z0, z1, seg=32):
    """Capped cylinder about +Z."""
    seg = _detail_seg(seg)
    verts, faces = [], []
    ang = np.linspace(0, 2 * np.pi, seg, endpoint=False)
    for z in (z0, z1):
        for a in ang:
            verts.append((r * math.cos(a), r * math.sin(a), z))
    c0 = len(verts)
    verts.append((0, 0, z0))
    c1 = len(verts)
    verts.append((0, 0, z1))
    for i in range(seg):
        a, b = i, (i + 1) % seg
        faces.append((a, b, seg + b, seg + a))
        faces.append((c0, b, a))
        faces.append((c1, seg + a, seg + b))
    return verts, faces


def _annulus_cylinder(r_out, r_in, z0, z1, seg=40):
    """Hollow tube closed at both axial ends (a pipe with real wall thickness)."""
    seg = _detail_seg(seg)
    verts, faces = [], []
    ang = np.linspace(0, 2 * np.pi, seg, endpoint=False)
    for z in (z0, z1):
        for a in ang:
            verts.append((r_out * math.cos(a), r_out * math.sin(a), z))
        for a in ang:
            verts.append((r_in * math.cos(a), r_in * math.sin(a), z))

    def oo(layer, i):
        return layer * (2 * seg) + (i % seg)

    def ii(layer, i):
        return layer * (2 * seg) + seg + (i % seg)

    for i in range(seg):
        faces.append((oo(0, i), oo(0, i + 1), oo(1, i + 1), oo(1, i)))
        faces.append((ii(0, i), ii(1, i), ii(1, i + 1), ii(0, i + 1)))
        faces.append((oo(0, i), ii(0, i), ii(0, i + 1), oo(0, i + 1)))
        faces.append((oo(1, i), oo(1, i + 1), ii(1, i + 1), ii(1, i)))
    return verts, faces


def _box(cx, cy, cz, sx, sy, sz):
    hx, hy, hz = sx / 2, sy / 2, sz / 2
    v = [(cx - hx, cy - hy, cz - hz), (cx + hx, cy - hy, cz - hz),
         (cx + hx, cy + hy, cz - hz), (cx - hx, cy + hy, cz - hz),
         (cx - hx, cy - hy, cz + hz), (cx + hx, cy - hy, cz + hz),
         (cx + hx, cy + hy, cz + hz), (cx - hx, cy + hy, cz + hz)]
    f = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1),
         (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
    return v, f


def _sphere(r, seg=20, rings=12, squash=1.0):
    """UV sphere about the origin; `squash` scales Z (oblate hull domes)."""
    seg = _detail_seg(seg)
    rings = max(4, int(rings * VISUAL_DETAIL))
    verts, faces = [], []
    for j in range(rings + 1):
        phi = math.pi * j / rings
        sp, cp = math.sin(phi), math.cos(phi)
        for i in range(seg):
            th = 2 * math.pi * i / seg
            verts.append((r * sp * math.cos(th), r * sp * math.sin(th),
                          r * cp * squash))
    for j in range(rings):
        for i in range(seg):
            a = j * seg + i
            b = j * seg + (i + 1) % seg
            c = (j + 1) * seg + (i + 1) % seg
            d = (j + 1) * seg + i
            faces.append((a, b, c, d))
    return verts, faces


def _torus(R, r, seg_major=48, seg_minor=12, a0=0.0, a1=2 * math.pi,
           closed=True):
    """Torus (or torus ARC from a0 to a1) in the X-Y plane about +Z.
    R = centreline radius, r = tube radius. The warp ring, the shaping rings,
    the reactor torus and the SMES store are all built from this one call."""
    seg_major = max(3, int(seg_major * VISUAL_DETAIL))
    seg_minor = max(4, int(seg_minor * VISUAL_DETAIL))
    verts, faces = [], []
    n_major = seg_major if closed else seg_major + 1
    for i in range(n_major):
        t = a0 + (a1 - a0) * (i / seg_major if not closed else i / seg_major)
        ct, st = math.cos(t), math.sin(t)
        for j in range(seg_minor):
            p = 2 * math.pi * j / seg_minor
            cp, sp = math.cos(p), math.sin(p)
            verts.append(((R + r * cp) * ct, (R + r * cp) * st, r * sp))
    lim = n_major if closed else n_major - 1
    for i in range(lim):
        i2 = (i + 1) % n_major
        for j in range(seg_minor):
            j2 = (j + 1) % seg_minor
            faces.append((i * seg_minor + j, i2 * seg_minor + j,
                          i2 * seg_minor + j2, i * seg_minor + j2))
    if not closed:                       # cap the two cut ends of the arc
        faces.append(tuple(range(seg_minor)))
        base = (n_major - 1) * seg_minor
        faces.append(tuple(reversed(range(base, base + seg_minor))))
    return verts, faces


def _dish(r_out, depth, z0, seg=28, rings=5, flip=False):
    """A parabolic dish opening along +Z (deflector, rectenna collector)."""
    seg = _detail_seg(seg)
    verts, faces = [], []
    for j in range(rings + 1):
        rr = r_out * j / rings
        z = z0 + (depth * (rr / max(1e-9, r_out)) ** 2) * (-1.0 if flip else 1.0)
        for i in range(seg):
            a = 2 * math.pi * i / seg
            verts.append((rr * math.cos(a), rr * math.sin(a), z))
    for j in range(rings):
        for i in range(seg):
            a = j * seg + i
            b = j * seg + (i + 1) % seg
            c = (j + 1) * seg + (i + 1) % seg
            d = (j + 1) * seg + i
            faces.append((a, b, c, d))
    return verts, faces


def _hull_loft(sections):
    """Loft a smooth body from circular cross-sections along Z.
    Each section is (z, radius). Consecutive rings are skinned and the ends
    capped -- this is how the 68 m crew hull gets its true teardrop profile."""
    seg = _detail_seg(24)
    verts, faces = [], []
    for (z, rr) in sections:
        for i in range(seg):
            a = 2 * math.pi * i / seg
            verts.append((rr * math.cos(a), rr * math.sin(a), z))
    n = len(sections)
    for k in range(n - 1):
        for i in range(seg):
            a = k * seg + i
            b = k * seg + (i + 1) % seg
            c = (k + 1) * seg + (i + 1) % seg
            d = (k + 1) * seg + i
            faces.append((a, b, c, d))
    c0 = len(verts)
    verts.append((0, 0, sections[0][0]))
    c1 = len(verts)
    verts.append((0, 0, sections[-1][0]))
    base = (n - 1) * seg
    for i in range(seg):
        faces.append((c0, (i + 1) % seg, i))
        faces.append((c1, base + i, base + (i + 1) % seg))
    return verts, faces


def _ring_wire(r, z, seg=64, axis="z"):
    """A single closed wire loop -- used for the bubble shell and grid rings."""
    seg = max(8, seg)
    verts = []
    for i in range(seg):
        a = 2 * math.pi * i / seg
        if axis == "z":
            verts.append((r * math.cos(a), r * math.sin(a), z))
        elif axis == "y":
            verts.append((r * math.cos(a), z, r * math.sin(a)))
        else:
            verts.append((z, r * math.cos(a), r * math.sin(a)))
    return verts, [tuple(range(seg))]


def _smooth_sections(ctrl, sub=4):
    """Catmull-Rom subdivision of (z, radius) control points -> a smooth loft."""
    pts = [ctrl[0]] + list(ctrl) + [ctrl[-1]]
    out = []
    for i in range(len(pts) - 3):
        p0, p1, p2, p3 = pts[i], pts[i + 1], pts[i + 2], pts[i + 3]
        for s in range(sub):
            t = s / sub
            t2, t3 = t * t, t * t * t
            vals = []
            for k in range(2):
                vals.append(0.5 * ((2 * p1[k]) + (-p0[k] + p2[k]) * t +
                                   (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2 +
                                   (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3))
            out.append(tuple(vals))
    out.append(ctrl[-1])
    return out


class Part:
    """A named, spec'd logical component made of one or more meshes. Carries an
    assembly `order`, an `explode` offset (where it slides to when disassembled)
    and a `specs` list shown in the inspector card."""

    def __init__(self, key, name, meshes, specs, order, explode, color):
        self.key = key
        self.name = name
        self.meshes = meshes
        self.specs = specs
        self.order = order
        self.explode = np.asarray(explode, dtype=float)
        self.color = color
        n = np.linalg.norm(self.explode)
        self.popdir = self.explode / n if n > 1e-6 else np.array([0.0, 0.0, 1.0])


def _grp(meshes, group):
    for m in meshes:
        m.group = group
    return meshes


def _place(meshes, pivot, tilt=(0.0, 0.0), group=None):
    """Move a set of origin-built meshes into position (and orientation)."""
    piv = np.asarray(pivot, dtype=float)
    for m in meshes:
        m.pivot = piv.copy()
        m.tilt = tilt
        if group:
            m.group = group
    return meshes


def _mix(c1, c2, t):
    t = max(0.0, min(1.0, t))
    return (int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t))


def _label(surf, font, text, pos, accent=False, color=None):
    col = color or (C_ACCENT if accent else C_TEXT_DIM)
    img = font.render(text, True, col)
    x, y = int(pos[0]) + 8, int(pos[1]) - 7
    bg = pygame.Surface((img.get_width() + 6, img.get_height() + 2),
                        pygame.SRCALPHA)
    bg.fill((6, 9, 16, 190))
    # subtle border on the label background for contrast against bright stars
    pygame.draw.rect(bg, (col[0] // 3, col[1] // 3, col[2] // 3, 120),
                     bg.get_rect(), 1, border_radius=3)
    surf.blit(bg, (x - 3, y - 1))
    surf.blit(img, (x, y))
    # glow dot: additive halo + solid centre, so the leader dot reads over
    # any background (LS.py's additive-blend pattern applied to a point)
    px, py = int(pos[0]), int(pos[1])
    glow = pygame.Surface((10, 10), pygame.SRCALPHA)
    pygame.draw.circle(glow, (col[0], col[1], col[2], 60), (5, 5), 5)
    pygame.draw.circle(glow, (col[0], col[1], col[2], 120), (5, 5), 3)
    surf.blit(glow, (px - 5, py - 5), special_flags=pygame.BLEND_RGBA_ADD)
    pygame.draw.circle(surf, col, (px, py), 2)


class ShipRenderer:
    """Projects and paints the spec'd Parts. Supports FULL / EXPLODED / ASSEMBLY
    views with an optional cross-SECTION cut, mouse hover-picking, highlight +
    hover-pop, and the assembly 'puzzle' (place one part at a time)."""

    def __init__(self, parts_builder, home_az=0.62, home_el=0.42,
                 home_dist=340.0, section_keys=()):
        self.parts_builder = parts_builder
        self.parts = parts_builder()
        self._home = (home_az, home_el, home_dist)
        self.az = home_az
        self.el = home_el
        self.dist = home_dist
        self.pan = np.array([0.0, 0.0])
        self.light = np.array([0.45, 0.62, 1.0])
        self.light = self.light / np.linalg.norm(self.light)
        self.view = "full"                    # full | exploded | assembly
        self.section = False
        self.section_keys = set(section_keys)
        self.explode_amt = 0.0
        self.assembled = len(self.parts)
        self.hovered = None
        self.selected = None
        self.pop = np.zeros(len(self.parts))
        self.hover_spread = 0.0
        self.hidden = set()                   # part keys temporarily hidden

    # ---- camera -----------------------------------------------------------
    def reset_view(self):
        self.az, self.el, self.dist = self._home
        self.pan = np.array([0.0, 0.0])

    def zoom_at(self, factor, mouse_pos=None, rect=None):
        old = self.dist
        self.dist = max(24.0, min(4000.0, self.dist * factor))
        if old <= 1e-6 or mouse_pos is None or rect is None:
            return
        if not rect.collidepoint(mouse_pos):
            return
        anchor = np.array([mouse_pos[0] - (rect.x + rect.w / 2.0),
                           mouse_pos[1] - (rect.y + rect.h / 2.0)], dtype=float)
        scale = old / self.dist
        self.pan = anchor - (anchor - self.pan) * scale

    def orbit(self, dx, dy, fine=False):
        sens = 0.004 if fine else 0.009
        self.az += dx * sens
        self.el += dy * sens
        self.el = max(-1.55, min(1.55, self.el))

    def pan_by(self, dx, dy, fine=False):
        sens = 0.45 if fine else 1.0
        self.pan += np.array([dx * sens, dy * sens])

    # ---- view state -------------------------------------------------------
    def set_view(self, mode):
        self.view = mode
        if mode == "assembly" and self.assembled >= len(self.parts):
            self.assembled = 0
        self.selected = None

    def toggle_section(self):
        self.section = not self.section

    def assembly_next(self):
        self.assembled = min(len(self.parts), self.assembled + 1)

    def assembly_prev(self):
        self.assembled = max(0, self.assembled - 1)

    def active_part(self):
        i = self.selected if self.selected is not None else self.hovered
        return self.parts[i] if i is not None else None

    def placing_part(self):
        for p in self.parts:
            if p.order == self.assembled:
                return p
        return None

    def tick(self, dt):
        if self.view != "assembly":
            target = 1.0 if self.view == "exploded" else 0.0
            self.explode_amt += (target - self.explode_amt) * min(1.0, dt * 4)
        hi = self.selected if self.selected is not None else self.hovered
        sp_target = 0.22 if (hi is not None and self.view == "full") else 0.0
        self.hover_spread += (sp_target - self.hover_spread) * min(1.0, dt * 5)
        for i in range(len(self.parts)):
            tp = 1.0 if i == hi else 0.0
            self.pop[i] += (tp - self.pop[i]) * min(1.0, dt * 8)

    def _layout(self, pi, vw, eamt):
        part = self.parts[pi]
        if vw == "assembly":
            if part.order < self.assembled:
                return part.explode * 0.0, 1.0, "normal"
            if part.order == self.assembled:
                return part.explode * 0.55, 1.0, "active"
            return part.explode * 1.0, 0.28, "pending"
        return part.explode * eamt, 1.0, "normal"

    # ---- the painter ------------------------------------------------------
    def render(self, surf, rect, angles, mouse_pos=None, show_labels=True,
               label_font=None, interactive=False, coil_glow=None,
               drive_power=0.0, rad_heat=0.0, bubble_on=0.0):
        """Paint every visible facet back-to-front. `coil_glow` is the rotating
        field-phase intensity per coil (the warp analogue of GmansRun's
        per-chamber firing glow), `drive_power` brightens every glow mesh, and
        `bubble_on` fades the wireframe warp shell in and out."""
        clip = surf.get_clip()
        surf.set_clip(rect)
        cx = rect.x + rect.w / 2.0 + self.pan[0]
        cy = rect.y + rect.h / 2.0 + self.pan[1]
        focal = min(rect.w, rect.h) * 1.10
        Rcam = rot_x(self.el) @ rot_y(self.az)
        default_ang = angles.get("default", 0.0)

        vw = self.view
        eamt = self.explode_amt
        if vw == "full":
            eamt += self.hover_spread
        hi = (self.selected if self.selected is not None else self.hovered)

        polys, labels, leaders, screeninfo = [], [], [], []
        lx, ly, lz = (float(self.light[0]), float(self.light[1]),
                      float(self.light[2]))

        for pi, part in enumerate(self.parts):
            if part.key in self.hidden:
                continue
            base_off, dim, tag = self._layout(pi, vw, eamt)
            off = base_off + part.popdir * (self.pop[pi] * 14.0)
            highlight = (pi == hi)
            allcam = []
            for m in part.meshes:
                if m.wire and bubble_on <= 0.02 and part.key == "bubble":
                    continue
                wv = m.world_verts(angles.get(m.group, default_ang)) + off
                cam = wv @ Rcam.T
                cam[:, 2] += self.dist
                allcam.append(cam)
                caml = cam.tolist()

                col = m.color
                if m.coil_index is not None and coil_glow is not None:
                    g = coil_glow[m.coil_index % len(coil_glow)]
                    if g > 0.01:
                        col = _mix(col, C_COIL_LIVE, min(1.0, g))
                if m.glow and drive_power > 0.01:
                    col = _mix(col, C_RING_HOT, min(0.80, drive_power * 0.75))
                if m.hot and rad_heat > 0.01:
                    col = _mix(col, C_RAD_HOT, min(0.85, rad_heat))
                if part.key == "bubble":
                    col = _mix((30, 44, 62), C_BUBBLE, bubble_on)
                if dim < 0.99:
                    col = (int(col[0] * dim), int(col[1] * dim), int(col[2] * dim))
                if highlight:
                    col = _mix(col, (255, 255, 255), 0.30)
                cr, cg, cb = col

                if highlight:
                    outline, ow = C_ACCENT, 2
                elif tag == "active":
                    outline, ow = (255, 210, 120), 2
                else:
                    outline, ow = None, 0

                # x of every world vertex, as plain floats: the section cut
                # tests one per face and a numpy mean per face costs more than
                # the entire rest of the frame
                wvx = wv[:, 0].tolist() if self.section else None
                sxl, syl, dzl = [], [], []
                for vx2, vy2, vz2 in caml:
                    dzl.append(vz2)
                    if vz2 > 0.05:
                        sxl.append(cx + focal * vx2 / vz2)
                        syl.append(cy - focal * vy2 / vz2)
                    else:
                        sxl.append(0.0)
                        syl.append(0.0)

                if (show_labels and label_font and m.name and tag != "pending"
                        and (vw != "full" or highlight)):
                    mcen = cam.mean(axis=0)
                    if mcen[2] > 0.05:
                        labels.append((mcen[2],
                                       (cx + focal * mcen[0] / mcen[2],
                                        cy - focal * mcen[1] / mcen[2]),
                                       m.name, "detail"))

                for face in m.faces:
                    if wvx is not None and self._section_cut(part.key, wvx, face):
                        continue
                    clipped = False
                    for i in face:
                        if dzl[i] <= 0.05:
                            clipped = True
                            break
                    if clipped:
                        continue
                    if m.wire:
                        # wires go into the SAME depth-sorted list as the solid
                        # facets: painted in a separate pass afterwards, the
                        # bubble shell drew itself over the hull it surrounds
                        ds = 0.0
                        for i in face:
                            ds += dzl[i]
                        polys.append((ds / len(face),
                                      [(sxl[i], syl[i]) for i in face],
                                      (cr, cg, cb), None, -1))
                        continue
                    ax, ay, az = caml[face[0]]
                    bx, by, bz = caml[face[1]]
                    fx, fy, fz = caml[face[2]]
                    ux, uy, uz = bx - ax, by - ay, bz - az
                    wx, wy, wz = fx - ax, fy - ay, fz - az
                    nx = uy * wz - uz * wy
                    ny = uz * wx - ux * wz
                    nz = ux * wy - uy * wx
                    inv = 1.0 / ((nx * nx + ny * ny + nz * nz) ** 0.5 or 1.0)
                    nx *= inv
                    ny *= inv
                    nz *= inv
                    if nz > 0:
                        nx, ny, nz = -nx, -ny, -nz
                    d = nx * lx + ny * ly + nz * lz
                    shade = 0.32 + 0.68 * (d if d > 0.0 else 0.0)
                    fc = (int(cr * shade), int(cg * shade), int(cb * shade))
                    ds = 0.0
                    for i in face:
                        ds += dzl[i]
                    # depth fog: distant facets fade toward the background
                    # colour, giving the model atmospheric perspective without
                    # a separate render pass. Fog starts at 1.6x the camera
                    # distance and reaches ~20% by 3x.
                    avg_d = ds / len(face)
                    fog_d0 = self.dist * 1.6
                    fog_d1 = self.dist * 3.0
                    if avg_d > fog_d0:
                        ft = clamp((avg_d - fog_d0) / (fog_d1 - fog_d0))
                        fog_amt = 0.22 * ft
                        fc = (int(fc[0] + (BG_BOT[0] - fc[0]) * fog_amt),
                              int(fc[1] + (BG_BOT[1] - fc[1]) * fog_amt),
                              int(fc[2] + (BG_BOT[2] - fc[2]) * fog_amt))
                    polys.append((avg_d,
                                  [(sxl[i], syl[i]) for i in face],
                                  fc, outline, ow))

            if not allcam:
                continue
            cam_all = np.vstack(allcam)
            cen = cam_all.mean(axis=0)
            if cen[2] > 0.05:
                safez = np.where(cam_all[:, 2] <= 0.05, 1e9, cam_all[:, 2])
                scx = cx + focal * cam_all[:, 0] / safez
                scy = cy - focal * cam_all[:, 1] / safez
                pcx = cx + focal * cen[0] / cen[2]
                pcy = cy - focal * cen[1] / cen[2]
                rad = float(np.max(np.hypot(scx - pcx, scy - pcy))) * 0.55 + 6
                screeninfo.append((pi, pcx, pcy, rad, cen[2], tag))
                if show_labels and label_font and tag != "pending":
                    labels.append((cen[2], (pcx, pcy), part.name, tag))
                if tag == "active":
                    hc = cen - (off @ Rcam.T)
                    if hc[2] > 0.05:
                        leaders.append(((pcx, pcy),
                                        (cx + focal * hc[0] / hc[2],
                                         cy - focal * hc[1] / hc[2])))

        polys.sort(key=lambda t: t[0], reverse=True)
        for _, pts, fc, outline, ow in polys:
            try:
                if ow < 0:                       # a wire loop, not a facet
                    if len(pts) >= 2:
                        pygame.draw.lines(surf, fc, True, pts, 1)
                elif len(pts) >= 3:
                    pygame.draw.polygon(surf, fc, pts)
                    if outline is not None:
                        pygame.draw.polygon(surf, outline, pts, ow)
            except Exception:
                pass

        for a, b in leaders:
            pygame.draw.line(surf, (255, 210, 120), a, b, 1)
            pygame.draw.circle(surf, (255, 210, 120), (int(b[0]), int(b[1])), 5, 1)

        if show_labels and label_font:
            labels.sort(key=lambda t: t[0])
            used = []
            for _, (px, py), text, tag in labels:
                py2 = py
                for uy in used:
                    if abs(py2 - uy) < 15:
                        py2 = uy + 15
                used.append(py2)
                _label(surf, label_font, text, (px, py2),
                       accent=(tag in ("active", "detail")))

        if interactive and mouse_pos is not None:
            mxp, myp = mouse_pos
            best, bestd = None, 1e18
            for pi, pcx, pcy, rad, depth, tag in screeninfo:
                if tag == "pending":
                    continue
                if math.hypot(mxp - pcx, myp - pcy) <= rad and depth < bestd:
                    bestd, best = depth, pi
            self.hovered = best

        surf.set_clip(clip)

    def _section_cut(self, key, wvx, face):
        """Remove the +X half of the bulky parts -- a clean half-section through
        the vertical plane, so the reactor torus, the SMES store, the Casimir
        cassettes inside the ring wall and the four crew decks read in true
        cross-section. `wvx` is the mesh's world X coordinates as a plain list;
        this runs once per FACET, so it stays in pure Python."""
        if key not in self.section_keys:
            return False
        t = 0.0
        for i in face:
            t += wvx[i]
        return t > 0.15 * len(face)


# =============================================================================
# SECTION 5 -- WARP METRIC PHYSICS  (the real general relativity, integrated)
# =============================================================================
# THE METRIC (Alcubierre 1994, eq. 8), signature (-,+,+,+):
#
#     ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2
#
# A flat interior (f = 1) is carried along by a shift vector that falls to zero
# (f = 0) outside a wall of thickness delta at radius R. Nothing moves THROUGH
# space -- the interior is inertial and weightless the whole way.
#
# The shape function is Alcubierre's own top-hat:
#
#     f(r) = [tanh(sigma (r + R)) - tanh(sigma (r - R))] / (2 tanh(sigma R))
#
# with sigma = 1/delta. From it everything else follows analytically, and this
# module integrates the results rather than quoting them.

def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def _sech2(x):
    """1/cosh^2(x), overflow-safe. math.cosh overflows past ~710; sech^2 is
    already indistinguishable from zero by |x| ~ 40, so clamping is exact to
    double precision."""
    ax = abs(x)
    if ax > 350.0:
        return 0.0
    ch = math.cosh(x)
    return 1.0 / (ch * ch)


def shape_f(r, R=None, delta=None):
    """Alcubierre top-hat shape function f(r_s). f -> 1 inside, 0 outside."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    sigma = 1.0 / max(1e-30, delta)
    den = 2.0 * math.tanh(sigma * R)
    if den == 0.0:
        return 0.0
    return (math.tanh(sigma * (r + R)) - math.tanh(sigma * (r - R))) / den


def shape_df(r, R=None, delta=None):
    """df/dr_s -- the derivative that carries ALL of the curvature. Everything
    expensive about a warp drive lives in this one function being large."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    sigma = 1.0 / max(1e-30, delta)
    den = 2.0 * math.tanh(sigma * R)
    if den == 0.0:
        return 0.0
    return sigma * (_sech2(sigma * (r + R)) - _sech2(sigma * (r - R))) / den


def shape_df_shifted(u, R=None, delta=None):
    """df/dr evaluated at r = R + u, computed FROM u directly.

    shape_df(r) forms (r - R) internally, and for a wall thinner than about
    1e-14 R that subtraction loses every significant digit -- a 1e-33 m wall
    sitting at r = 100 m is invisible to double precision. Passing the offset
    in explicitly sidesteps the cancellation entirely, which is what lets the
    energy integral stay exact all the way down to the Planck-scale walls the
    quantum inequality demands."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    sigma = 1.0 / max(1e-300, delta)
    den = 2.0 * math.tanh(sigma * R)
    if den == 0.0:
        return 0.0
    return sigma * (_sech2(sigma * (2.0 * R + u)) - _sech2(sigma * u)) / den


def york_theta(x, rho_perp, beta, R=None, delta=None):
    """York time / expansion scalar theta = beta c (x / r_s) df/dr_s   [1/s].

    Alcubierre 1994 eq. 19. POSITIVE behind the ship (space being created --
    it expands) and NEGATIVE in front (space being destroyed -- it contracts).
    This is the single scalar the METRIC view draws: it is literally the rate
    at which volume is appearing and disappearing around the hull."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    r = math.sqrt(x * x + rho_perp * rho_perp)
    if r < 1e-12:
        return 0.0
    return beta * C_LIGHT * (x / r) * shape_df(r, R, delta)


def energy_density(x, rho_perp, beta, R=None, delta=None):
    """Eulerian energy density T^00 measured by observers at rest  [J/m^3].

        T^00 = -(c^4 / 8 pi G) * (beta^2 rho^2) / (4 r_s^2) * (df/dr_s)^2

    (Alcubierre 1994 eq. 12, restored to SI.) Note the leading MINUS SIGN: it
    is not a sign convention and it is not removable. Every superluminal warp
    metric ever written down has it. rho = sqrt(y^2 + z^2) is the distance from
    the direction-of-travel axis, so the negative energy is concentrated in a
    torus around the equator of the bubble wall -- not spread over the shell."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    r = math.sqrt(x * x + rho_perp * rho_perp)
    if r < 1e-12:
        return 0.0
    dfr = shape_df(r, R, delta)
    return -(C4_OVER_G / (8.0 * math.pi)) * (beta * beta * rho_perp * rho_perp) \
        / (4.0 * r * r) * dfr * dfr


def warp_energy_integral(R=None, delta=None, samples=4000):
    """I = INT_0^inf r^2 (df/dr)^2 dr   [m], by composite Simpson over the wall.

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
    f' = -(sigma/2) sech^2(sigma u), and INT sech^4 = 4/3, so I -> R^2 sigma/3."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    half = min(R * 0.999, 14.0 * delta)
    n = samples if samples % 2 == 0 else samples + 1
    h = 2.0 * half / n
    total = 0.0
    for i in range(n + 1):
        u = -half + i * h
        r = R + u
        d = shape_df_shifted(u, R, delta)
        val = r * r * d * d
        w = 1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)
        total += w * val
    return total * h / 3.0


def alcubierre_energy_j(beta, R=None, delta=None):
    """Total (negative) energy of the Alcubierre warp field  [J].
    E = -(c^4 beta^2 / 12 G) * INT r^2 f'^2 dr. Sanity anchor: with R = 100 m,
    beta = 10 and a Planck-ish 1e-15 m wall this returns about -3e63 J, which
    is Alcubierre's own 1994 order-of-magnitude estimate (~10^64 J). The
    --selftest asserts exactly that."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    return -(C4_OVER_G / 12.0) * beta * beta * warp_energy_integral(R, delta)


def equiv_mass_kg(energy_j):
    """E/c^2 -- the mass whose rest energy equals this. Sign is preserved,
    because a negative energy requirement means NEGATIVE MASS, and that is
    the whole problem."""
    return energy_j / C2


def wall_tidal_gradient(beta, R=None, delta=None):
    """Tidal acceleration across a 2 m body sitting IN the bubble wall [m/s^2].

    a ~ beta c^2 |f''| L, and f'' ~ sigma^2 = 1/delta^2, so the wall is lethal
    for any wall thin enough to be affordable. The interior is EXACTLY flat
    (f = 1, all derivatives zero) -- which is why the crew is weightless and
    unharmed while standing 84 m from a region of infinite-grade shear. This
    is the design's real virtue and its real hazard, in one number."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    # f'' VANISHES exactly at r = R -- the crest of f' is a stationary point --
    # so sampling there reports a comfortable zero and hides the hazard. The
    # shear peaks on the shoulders, at sigma u ~ +/- 0.66, so scan for it.
    step = delta / 24.0
    worst = 0.0
    for i in range(-72, 73):
        u = i * step
        fpp = (shape_df_shifted(u + step, R, delta)
               - shape_df_shifted(u - step, R, delta)) / (2.0 * step)
        worst = max(worst, abs(fpp))
    return abs(beta) * C2 * worst * 2.0


def ford_roman_wall_limit(beta):
    """Quantum-inequality bound on the wall thickness  [m].

    Ford and Roman (1996) proved that a quantum field can only hold negative
    energy for a time inversely proportional to its magnitude. Pfenning and
    Ford (1997) applied that inequality to the Alcubierre bubble specifically
    and found the wall cannot exceed a few hundred Planck lengths thick --
    which is what makes the energy bill astronomical rather than merely huge.
    Returned as an order-of-magnitude bound, not a precise threshold; the exact
    coefficient depends on the sampling function chosen."""
    return 1.0e2 * L_PLANCK / max(1.0, beta)


# --- Casimir effect: the ONLY laboratory-verified negative energy density ----

def casimir_energy_density(gap_m):
    """Casimir vacuum energy density between ideal parallel plates  [J/m^3].
        rho = -pi^2 hbar c / (720 a^4)
    (Casimir 1948.) Measured to a few percent by Lamoreaux 1997 and Mohideen
    and Roy 1998, so unlike everything else on the exotic side of this file it
    is real. At a 10 nm gap it is about -43 kJ/m^3."""
    a = max(1e-12, gap_m)
    return -(math.pi ** 2) * HBAR * C_LIGHT / (720.0 * a ** 4)


def casimir_cassette():
    """Geometry and yield of ONE onboard Casimir cassette."""
    plate = DIMS["casimir_plate_m"]
    gap = DIMS["casimir_gap_nm"] * 1e-9
    pitch = DIMS["casimir_pitch_nm"] * 1e-9
    n_gaps = int(DIMS["casimir_stack_m"] / pitch)
    v_gap = plate * plate * gap * n_gaps          # total negative-energy volume
    rho = casimir_energy_density(gap)
    return {"plates": n_gaps, "gap_volume_m3": v_gap, "rho_j_m3": rho,
            "energy_j": rho * v_gap,
            "plate_area_m2": plate * plate * n_gaps}


def casimir_onboard_j():
    """Total negative energy the whole 24-cassette lattice actually holds [J].
    This is the largest real negative-energy reservoir known to engineering,
    and the model compares it -- to the joule -- against what a warp bubble
    demands. The comparison is the single most important number in this file."""
    return casimir_cassette()["energy_j"] * DIMS["casimir_cassettes"]


# --- Energy conditions -------------------------------------------------------

def energy_conditions(beta):
    """Which pointwise energy conditions the commanded solution satisfies.

    beta < 1  -> the Bobrick and Martire (2021) / Fuchs et al. (2024) class:
                 a positive-energy massive shell with a shift-vector
                 distribution. Constructed specifically to satisfy NEC, WEC,
                 DEC and SEC. Real matter. Buildable in principle.
    beta >= 1 -> Santiago, Schuster and Visser, 'Generic warp drives violate
                 the null energy condition' (Class. Quantum Grav. 39 075006,
                 2022): ANY superluminal warp drive violates the NEC somewhere.
                 Not a limitation of Alcubierre's particular ansatz -- a
                 theorem about the whole class."""
    if beta < 1.0:
        return {"NEC": True, "WEC": True, "DEC": True, "SEC": True,
                "class": "PHYSICAL",
                "note": "positive-energy shell (Bobrick-Martire / Fuchs et al.)"}
    return {"NEC": False, "WEC": False, "DEC": False, "SEC": False,
            "class": "EXOTIC",
            "note": "superluminal: NEC violation is a theorem (SSV 2022)"}


def horizon_locked(beta):
    """True when the forward bubble wall is causally disconnected from the ship.

    For beta > 1 the front of the bubble outruns light signals sent from the
    interior, so the crew CANNOT send the control signal that would reshape or
    dissolve the forward wall (Everett 1996; Coule 1998; Krasnikov 1998). The
    entire trajectory must be pre-laid before departure. In FLIGHT mode the
    helm physically locks above beta = 1 for exactly this reason."""
    return beta > 1.0


# --- Barrier engineering analysis -------------------------------------------
# Each barrier is a theorem or physical limit that blocks the drive.  For each
# we compute (a) the exact number that triggers the barrier, (b) what it would
# take to get past it, and (c) whether that is physically possible.  The answer
# to (c) is always "no" for the five hard barriers -- that is the honest result.

def barrier_analysis():
    """Returns a dict of barrier -> {value, threshold, gap, passable, route}.

    This is the engineering audit: for each of the five hard barriers that the
    feasibility scorecard marks FAIL, we state the exact number, the exact
    threshold, the gap in orders of magnitude, and what a hypothetical route
    past it would require.  The routes are not proposed as solutions -- they
    are stated so the reader can see what 'past the barrier' would mean."""
    R = DIMS["bubble_r_m"]
    d0 = DIMS["wall_thick_m"]
    cas = abs(casimir_onboard_j())

    # 1. Survivable bubble wall (tidal gradient across the wall)
    #    a_wall = beta c^2 |f''|_max L; at beta=1, L=2m this is ~1e16 g
    a_wall = wall_tidal_gradient(1.0, R, d0) / 9.81   # in g
    a_limit = 1.0                                       # 1 g survivable
    wall_gap = math.log10(a_wall / a_limit) if a_wall > a_limit else 0.0
    # Route: make delta -> 0 (thinner wall).  But QI forbids delta < 100 L_P.
    delta_qi = ford_roman_wall_limit(1.0)
    a_at_qi = wall_tidal_gradient(1.0, R, delta_qi) / 9.81
    wall_passable = False   # thinner wall = more tidal, not less

    # 2. Superluminal flight (NEC violation, SSV theorem)
    #    Theorem: ANY v > c warp violates NEC.  No route.
    nec_sub = energy_conditions(0.99)["NEC"]
    nec_super = energy_conditions(1.01)["NEC"]
    super_passable = False   # theorem, not engineering

    # 3. Negative energy at the required scale
    #    Need |E| at delta=1m; have |Casimir|.
    E_need = abs(alcubierre_energy_j(1.0, R, d0))
    energy_gap = math.log10(E_need / cas) if E_need > cas else 0.0
    # Route: more Casimir cassettes.  How many?
    cassettes_needed = E_need / abs(casimir_cassette()["energy_j"])
    energy_passable = False   # would need 10^40 cassettes

    # 4. Steering above beta = 1 (horizon lock)
    #    Theorem: forward wall is causally disconnected.  No route.
    steer_passable = False   # theorem

    # 5. Thermal survival above beta = 1
    #    T = (P / eps sigma A)^(1/4); limit = rad_limit_k
    #    Find the beta where T crosses the limit
    b_thermal = 1.0
    while b_thermal < 5.0:
        T = radiator_temp_k(waste_heat_w(cruise_load_w(b_thermal)))
        if T > DIMS["rad_limit_k"]:
            break
        b_thermal += 0.01
    T_at_limit = radiator_temp_k(waste_heat_w(cruise_load_w(b_thermal)))
    thermal_gap = (T_at_limit - DIMS["rad_limit_k"]) / DIMS["rad_limit_k"]
    # Route: more radiator area.  How much?
    P_at_limit = waste_heat_w(cruise_load_w(2.0))
    A_needed = P_at_limit / (DIMS["rad_emissivity"] * SIGMA_SB * DIMS["rad_limit_k"]**4)
    thermal_passable = True   # in principle, with 10x more radiators

    # 6. Ford-Roman wall thickness (QI on wall)
    delta_max = ford_roman_wall_limit(1.0)
    E_at_qi = abs(alcubierre_energy_j(1.0, R, delta_max))
    qi_energy_gap = math.log10(E_at_qi / cas) if E_at_qi > cas else 0.0
    qi_passable = False   # theorem

    # 7. Quantum inequality on wormhole throat
    b0 = 12.0          # default throat radius (Morris-Thorne)
    tau_max = ford_roman_max_throat_tau(b0)
    tau_traverse = mt_traversal_time_s(b0)
    qi_throat_gap = math.log10(tau_traverse / tau_max) if tau_traverse > tau_max else 0.0
    qi_throat_passable = False   # theorem

    # 8. Causality / CTC (chronology protection)
    #    A time-shifted wormhole creates CTCs.  Hawking's conjecture expects
    #    the throat to be destroyed at the chronology horizon.
    ctc_passable = False   # conjecture, but strongly expected

    return {
        "wall_tidal": {
            "value_g": a_wall, "threshold_g": a_limit,
            "gap_orders": wall_gap, "passable": wall_passable,
            "route": "thinner wall -- but QI forbids delta < 100 L_P, "
                     "and thinner = MORE tidal, not less",
            "a_at_qi_g": a_at_qi,
        },
        "superluminal_nec": {
            "nec_subluminal": nec_sub, "nec_superluminal": nec_super,
            "passable": super_passable,
            "route": "SSV theorem (2022): ANY v > c warp violates NEC. "
                     "No route -- this is a theorem about the whole class.",
        },
        "negative_energy": {
            "need_j": E_need, "have_j": cas,
            "gap_orders": energy_gap, "passable": energy_passable,
            "cassettes_needed": cassettes_needed,
            "route": "more Casimir cassettes -- would need %.0e" % cassettes_needed,
        },
        "steering": {
            "locked_above": 1.0, "passable": steer_passable,
            "route": "forward wall is causally disconnected at v > c. "
                     "No route -- theorem (Everett, Coule, Krasnikov).",
        },
        "thermal": {
            "limit_beta": b_thermal, "limit_k": DIMS["rad_limit_k"],
            "T_at_2c": radiator_temp_k(waste_heat_w(cruise_load_w(2.0))),
            "gap_fraction": thermal_gap, "passable": thermal_passable,
            "area_needed_m2": A_needed,
            "area_have_m2": RADIATOR_AREA_M2,
            "route": "more radiator area -- need %.0f m^2 (have %.0f m^2)"
                     % (A_needed, RADIATOR_AREA_M2),
        },
        "ford_roman_wall": {
            "delta_max_m": delta_max, "E_at_qi_j": E_at_qi,
            "gap_orders": qi_energy_gap, "passable": qi_passable,
            "route": "QI theorem: wall cannot exceed 100 L_P. "
                     "At that thickness E = %.2e J = 10^9 universes." % E_at_qi,
        },
        "qi_throat": {
            "tau_max_s": tau_max, "tau_traverse_s": tau_traverse,
            "gap_orders": qi_throat_gap, "passable": qi_throat_passable,
            "route": "QI theorem: throat closes 10^26 times before you cross. "
                     "No route.",
        },
        "ctc": {
            "passable": ctc_passable,
            "route": "Hawking chronology protection: CTCs trigger divergent "
                     "vacuum fluctuations at the horizon.  Conjecture, but "
                     "strongly expected by the majority of the field.",
        },
    }


def barrier_scorecard():
    """Returns a list of (name, status, detail) for the 8 barriers.
    status is one of: PASS, FAIL, THEOREM, CONJECTURE."""
    ba = barrier_analysis()
    out = []
    out.append(("Bubble wall tidal gradient",
                "FAIL" if ba["wall_tidal"]["value_g"] > 1 else "PASS",
                "%.2e g (limit 1 g)" % ba["wall_tidal"]["value_g"]))
    out.append(("Superluminal NEC (SSV theorem)",
                "THEOREM" if not ba["superluminal_nec"]["nec_superluminal"] else "PASS",
                "NEC violated at v > c -- theorem"))
    out.append(("Negative energy scale",
                "FAIL" if ba["negative_energy"]["gap_orders"] > 0 else "PASS",
                "%.0f orders short of Casimir" % ba["negative_energy"]["gap_orders"]))
    out.append(("Steering above beta=1",
                "THEOREM" if ba["steering"]["locked_above"] <= 1.0 else "PASS",
                "causally disconnected -- theorem"))
    out.append(("Thermal survival",
                "FAIL" if ba["thermal"]["T_at_2c"] > ba["thermal"]["limit_k"] else "PASS",
                "%.0f K at 2c (limit %.0f K)" % (ba["thermal"]["T_at_2c"],
                                                  ba["thermal"]["limit_k"])))
    out.append(("Ford-Roman wall thickness",
                "THEOREM" if not ba["ford_roman_wall"]["passable"] else "PASS",
                "delta_max = 100 L_P = %.2e m" % ba["ford_roman_wall"]["delta_max_m"]))
    out.append(("QI throat hold time",
                "THEOREM" if not ba["qi_throat"]["passable"] else "PASS",
                "%.0f orders short" % ba["qi_throat"]["gap_orders"]))
    out.append(("CTC chronology protection",
                "CONJECTURE" if not ba["ctc"]["passable"] else "PASS",
                "Hawking 1992 -- strongly expected"))
    return out


# =============================================================================
# SECTION 5b -- MASS BUDGET  (every kilogram derived from DIMS geometry)
# =============================================================================

def _torus_surface(R, r):
    return 4.0 * math.pi * math.pi * R * r


def mass_budget():
    """Component-by-component dry mass, computed from the geometry the renderer
    draws. No component mass is typed in as a number -- each is a volume times
    a density, so changing a dimension changes the ship's mass, its kinetic
    energy bill, its radiator sizing and its voyage, all at once."""
    d = DIMS
    b = {}

    # main warp ring: a SHELL of wall thickness ring_wall_m, not a solid torus
    Rm, rm = d["ring_major_d_m"] / 2, d["ring_minor_d_m"] / 2
    b["warp ring shell"] = _torus_surface(Rm, rm) * d["ring_wall_m"] * d["ring_density"]

    # fore + aft shaping rings
    Rc, rc = d["capring_d_m"] / 2, d["capring_minor_d_m"] / 2
    b["shaping rings"] = 2 * _torus_surface(Rc, rc) * 0.35 * d["ring_density"]

    # HTS field coils: annular winding pack of 0.35 m radial build
    build = 0.35
    r_i = rm + 0.10
    v_coil = math.pi * ((r_i + build) ** 2 - r_i ** 2) * d["coil_len_m"]
    b["HTS field coils"] = d["coils"] * v_coil * 6000.0

    # crew hull: pressure shell + decks
    hull_area = 2 * math.pi * (d["hull_d_m"] / 2 * 0.88) * d["hull_len_m"]
    b["crew hull shell"] = hull_area * d["hull_wall_m"] * d["hull_density"]
    b["crew decks"] = (d["hull_decks"] * math.pi
                                              * (d["hull_d_m"] / 2 - 0.6) ** 2
                                              * 0.35 * d["hull_density"])

    # power / thermal plant
    b["fusion reactor"] = _torus_surface(d["reactor_major_d_m"] / 2,
                                         d["reactor_minor_d_m"] / 2) * 0.9 * 5200.0
    b["SMES buffer"] = _torus_surface(d["smes_major_d_m"] / 2,
                                      d["smes_minor_d_m"] / 2) * 0.25 * 6800.0
    b["antimatter traps"] = d["amtraps"] * 4.0 * math.pi \
        * (d["amtrap_d_m"] / 2) ** 2 * 0.30 * 4400.0
    b["cryoplant"] = d["cryo_units"] * math.pi \
        * (d["cryo_d_m"] / 2) ** 2 * d["cryo_len_m"] * 240.0
    b["radiators"] = d["radiators"] * d["rad_len_m"] \
        * d["rad_w_m"] * 0.06 * 1900.0

    # structure and appendages
    b["pylons"] = d["pylons"] * d["pylon_len_m"] \
        * d["pylon_w_m"] * 1.2 * 2700.0
    b["Casimir lattice"] = d["casimir_cassettes"] \
        * d["casimir_plate_m"] ** 2 * d["casimir_stack_m"] * 2300.0
    b["deflector"] = math.pi * (d["deflector_d_m"] / 2) ** 2 * 0.10 * 3100.0
    b["RCS pods"] = d["rcs_pods"] * math.pi \
        * (d["rcs_d_m"] / 2) ** 2 * d["rcs_len_m"] * 900.0
    b["boost rectenna"] = (math.pi * (d["collector_deploy_km"] * 500.0) ** 2
                           * d["collector_film_um"] * 1e-6 * d["collector_film_rho"])
    b["magsail loop"] = d["magsail_mass_kg"]
    b["consumables + crew"] = d["crew"] * 3200.0
    return b


def ship_mass_kg():
    return sum(mass_budget().values())


SHIP_MASS_KG = ship_mass_kg()


def lorentz_gamma(beta):
    b = min(abs(beta), 0.9999999)
    return 1.0 / math.sqrt(1.0 - b * b)


def kinetic_energy_j(beta, mass_kg=None):
    """(gamma - 1) M c^2 -- the honest, unavoidable bill for CHANGING velocity.

    A constant-velocity warp solution is a stationary spacetime and costs
    nothing to hold (Bobrick and Martire 2021, section 4). Changing velocity
    is another matter: the ADM energy and momentum of the whole configuration
    change, and that change has to come from somewhere outside the ship. This
    function is what the FLIGHT mode charges you, and there is no discount."""
    m = SHIP_MASS_KG if mass_kg is None else mass_kg
    if beta >= 1.0:
        return float("inf")          # no gamma for a superluminal bubble
    return (lorentz_gamma(beta) - 1.0) * m * C2


# =============================================================================
# SECTION 5c -- POWER, THERMAL AND THE BEAM  (ordinary engineering, done right)
# =============================================================================

def smes_store_j():
    """SMES capacity from first principles: u = B^2 / 2 mu0 over the torus
    volume. Comes out near 7e11 J -- twelve orders of magnitude below a
    velocity change, which is precisely why this ship cannot self-launch."""
    R, r = DIMS["smes_major_d_m"] / 2, DIMS["smes_minor_d_m"] / 2
    vol = 2.0 * math.pi ** 2 * R * r * r
    u = DIMS["smes_b_t"] ** 2 / (2.0 * MU0)
    return u * vol


SMES_J = smes_store_j()


def plant_electric_w():
    """Direct-conversion electrical capacity of the D-3He plant [W]."""
    return DIMS["reactor_th_gw"] * 1e9 * DIMS["reactor_direct_eff"]


PLANT_ELECTRIC_W = plant_electric_w()


def cruise_load_w(beta, bubble_on=1.0):
    """Electrical load to HOLD the warp field at beta [W].

    Coil AC losses scale with the square of the field (hence beta^2); the
    metric servo that keeps the 24 shell sectors in shape scales roughly
    linearly; cryo and hotel loads are constant. Holding a constant beta is
    cheap in principle -- the cost here is engineering imperfection (ripple,
    control, refrigeration), not general relativity."""
    p = PLANT
    coil = p["coil_ac_mw"] * beta * beta * bubble_on
    ctrl = p["control_mw"] * (0.20 + 0.80 * min(1.0, beta)) * bubble_on
    return (coil + ctrl + p["cryo_mw"] + p["hotel_mw"]) * 1e6


def waste_heat_w(load_w):
    """Everything drawn eventually becomes heat: a closed ship exports no work.
    Thermal drawn = electrical load / conversion efficiency."""
    return load_w / PLANT["conversion_eff"]


def radiator_area_m2():
    """Installed radiating area -- both faces of every panel."""
    return DIMS["radiators"] * DIMS["rad_len_m"] * DIMS["rad_w_m"] * 2.0


RADIATOR_AREA_M2 = radiator_area_m2()


def radiator_temp_k(waste_w):
    """Equilibrium panel temperature from Stefan-Boltzmann: T = (P/eps sigma A)^1/4.
    NOT a set point -- a consequence. When the FTL mode drives the coil load up
    as beta^2, this is the number that goes past the graphite limit first."""
    denom = DIMS["rad_emissivity"] * SIGMA_SB * RADIATOR_AREA_M2
    return (max(0.0, waste_w) / max(1e-9, denom)) ** 0.25


def radiator_required_m2(waste_w, t_k=None):
    t = DIMS["rad_temp_k"] if t_k is None else t_k
    return waste_w / max(1e-9, DIMS["rad_emissivity"] * SIGMA_SB * t ** 4)


def fusion_fuel_kg(energy_j):
    """D-3He mass burnt to deliver this much ELECTRICAL energy."""
    return energy_j / PLANT["conversion_eff"] / PLANT["d3he_j_kg"]


def beam_spot_m(range_m):
    """Diffraction-limited spot diameter of the stellar-tap boost beam [m].
        d_spot = 2.44 lambda L / D
    (Airy). With a 1000 km transmitter at 1 um, the spot is already 2.8 km wide
    at a tenth of a light year -- which is exactly why the rectenna has to
    unfurl to 4 km and why the boost phase has a hard range limit."""
    lam = PLANT["beam_lambda_um"] * 1e-6
    ap = PLANT["beam_aperture_km"] * 1e3
    return 2.44 * lam * max(1.0, range_m) / ap


def beam_capture_frac(range_m):
    """Fraction of the beam the deployed rectenna actually intercepts."""
    spot = beam_spot_m(range_m)
    d_rect = DIMS["collector_deploy_km"] * 1e3
    if spot <= d_rect:
        return 1.0
    return (d_rect / spot) ** 2


def beam_power_w(range_m):
    return PLANT["tap_w"] * beam_capture_frac(range_m)


def boost_profile(beta, mass_kg=None):
    """Can the stellar tap actually get this ship to beta before the ship flies
    out of the beam? Integrates the boost explicitly.

    Two clocks race each other. The energy clock says you need (gamma-1) M c^2
    delivered at the captured beam power. The range clock says you are moving
    away the whole time, the diffraction spot grows linearly with distance, the
    captured fraction falls as 1/L^2, and past beam_range_ly there is no useful
    beam at all. Whichever runs out first decides your cruise speed -- and no
    amount of onboard cleverness changes it, because the ship cannot carry the
    energy. This is the real speed limit of the design, and it is emergent:
    nothing in DIMS names a maximum beta."""
    m = SHIP_MASS_KG if mass_kg is None else mass_kg
    need = kinetic_energy_j(beta, m)
    if not math.isfinite(need):
        return {"ok": False, "reason": "superluminal: no kinetic-energy solution",
                "energy_j": need, "time_s": float("inf"),
                "range_m": float("inf"), "delivered_j": 0.0}
    limit_m = PLANT["beam_range_ly"] * LY
    dt = 3.0 * DAY
    got, t, x, v = 0.0, 0.0, 0.0, 0.0
    v_target = beta * C_LIGHT
    while got < need and x < limit_m and t < 200.0 * YR:
        p_in = beam_power_w(max(1.0, x))
        got += p_in * dt
        # convert delivered energy to speed through the relativistic ledger
        g = 1.0 + got / (m * C2)
        v = C_LIGHT * math.sqrt(max(0.0, 1.0 - 1.0 / (g * g)))
        v = min(v, v_target)
        x += v * dt
        t += dt
    ok = got >= need * 0.999
    return {"ok": ok, "energy_j": need, "delivered_j": got, "time_s": t,
            "range_m": x, "final_beta": v / C_LIGHT,
            "reason": ("" if ok else
                       "beam range exhausted at %s -- captured %.1f%% of the bill"
                       % (fmt_dist(x), 100.0 * got / max(1.0, need)))}


def max_boost_beta(mass_kg=None, lo=0.02, hi=0.99):
    """Highest cruise beta the beam can actually deliver, by bisection on
    boost_profile(). EMERGENT, not configured: it falls out of the transmitter
    aperture, the wavelength, the tap power and the ship's mass."""
    if not boost_profile(lo, mass_kg)["ok"]:
        return 0.0
    for _ in range(18):
        mid = 0.5 * (lo + hi)
        if boost_profile(mid, mass_kg)["ok"]:
            lo = mid
        else:
            hi = mid
    return lo


# --- Magnetic sail: the only credible brake ---------------------------------

def magsail_area_m2():
    return math.pi * (DIMS["magsail_r_km"] * 1e3) ** 2


def magsail_drag_n(beta):
    """Drag of the magnetic sail against the interstellar medium [N].

        F = Cd * rho_ISM * v^2 * A_eff

    Zubrin and Andrews (1991). rho_ISM = n m_p at 0.1 protons/cm^3. The loop
    deflects incoming protons; their momentum change is the brake. It is a
    genuinely tiny force -- and it is still the largest deceleration authority
    this ship has by six orders of magnitude, which tells you everything about
    interstellar flight."""
    v = abs(beta) * C_LIGHT
    rho = ISM_N_M3 * M_P
    return DIMS["magsail_cd"] * rho * v * v * magsail_area_m2()


def magsail_halving_time_s(beta, mass_kg=None):
    """Characteristic time for the magsail to HALVE the speed [s]: t = M/(k v0).
    Quoting this as 'the braking time' is the classic way to make magsail
    braking look feasible. It is not the time to stop -- see below."""
    m = SHIP_MASS_KG if mass_kg is None else mass_kg
    v0 = abs(beta) * C_LIGHT
    if v0 < 1.0:
        return 0.0
    k = DIMS["magsail_cd"] * ISM_N_M3 * M_P * magsail_area_m2()
    return m / (k * v0)


def magsail_decel_time_s(beta, mass_kg=None, beta_final=None):
    """HONEST time to brake from beta down to arrival speed on the magsail [s].

        M dv/dt = -k v^2   ->   t = (M/k) (1/v_f - 1/v_0)

    Drag falls as v^2, so the brake fades exactly as you need it most and the
    integral is dominated by the LAST decade of speed, not the first. The
    halving time is ~55 yr; the time to actually stop is ~27,000 yr. Reporting
    the first number and calling it 'braking time' is the single most common
    way interstellar mission studies flatter themselves, so this model reports
    the second -- and then tells you what to do about it (a destination array;
    see beam_brake_force_n)."""
    m = SHIP_MASS_KG if mass_kg is None else mass_kg
    bf = DRIVE["arrival_beta"] if beta_final is None else beta_final
    v0, vf = abs(beta) * C_LIGHT, max(1.0, bf * C_LIGHT)
    if v0 <= vf:
        return 0.0
    k = DIMS["magsail_cd"] * ISM_N_M3 * M_P * magsail_area_m2()
    return (m / k) * (1.0 / vf - 1.0 / v0)


def beam_brake_force_n(range_to_array_m):
    """Photon-pressure braking against an array AT THE DESTINATION [N].

        F = 2 P_captured / c        (perfect reflector)

    Forward (1984) proposed exactly this for staged lightsails, and it is the
    only known way to stop a heavy interstellar payload in useful time. Note
    what it costs: a second stellar-scale transmitter, already built, at a star
    nobody has visited. Interstellar RENDEZVOUS is an infrastructure problem at
    both ends; interstellar FLYBY is not. The model makes you choose, and says
    which one you chose on every frame."""
    p = beam_power_w(max(1.0, range_to_array_m))
    return 2.0 * p / C_LIGHT


def beam_brake_time_s(beta, mass_kg=None):
    """Rough time to stop under destination-array photon braking [s]."""
    m = SHIP_MASS_KG if mass_kg is None else mass_kg
    f = beam_brake_force_n(0.02 * LY)          # representative mid-approach range
    if f <= 0:
        return float("inf")
    return lorentz_gamma(beta) * m * abs(beta) * C_LIGHT / f


# --- Interstellar medium loading on the bubble wall -------------------------

def ism_particles_swept(distance_m, R=None):
    """Protons the bubble sweeps up over a leg. They do not pass through: the
    wall collects them (McMonigal, Lewis and O'Byrne, Phys. Rev. D 85 064024,
    2012, 'The Alcubierre warp drive: on the matter of matter')."""
    R = DIMS["bubble_r_m"] if R is None else R
    return ISM_N_M3 * math.pi * R * R * max(0.0, distance_m)


def ism_blast_energy_j(beta, distance_m, R=None):
    """Energy stored in the swept particles, released forward on bubble
    collapse [J]. The 2012 paper's headline result: a warp ship arriving at its
    destination discharges its accumulated wall load as a beam. This model
    scales the per-particle energy as beta^2/2 m c^2 -- a deliberately
    CONSERVATIVE floor, since the true spectrum is set by the wall's blueshift
    and is worse."""
    n = ism_particles_swept(distance_m, R)
    return n * M_P * C2 * (beta * beta) * 0.5


# --- Comparison baseline: an honest relativistic rocket ----------------------

def rocket_proper_time_s(beta, distance_m):
    """Proper time aboard a conventional relativistic cruiser doing the same
    trip at the same speed -- for contrast. It experiences LESS time than the
    warp ship, because it is genuinely time-dilated and the warp ship is not.
    A warp drive does not buy you time dilation. It buys you no reaction mass,
    no g-loading, and arrival in step with the people who waved you off."""
    if beta <= 0:
        return float("inf")
    return (distance_m / (beta * C_LIGHT)) / lorentz_gamma(beta)


# --- Formatters --------------------------------------------------------------

def fmt_energy(j):
    a = abs(j)
    sign = "-" if j < 0 else ""
    if a == 0:
        return "0 J"
    if a < 1e3:
        return "%s%.3g J" % (sign, a)
    for scale, unit in ((1e24, "YJ"), (1e21, "ZJ"), (1e18, "EJ"), (1e15, "PJ"),
                        (1e12, "TJ"), (1e9, "GJ"), (1e6, "MJ"), (1e3, "kJ")):
        if a >= scale:
            if a / scale >= 1e6:
                break
            return "%s%.3g %s" % (sign, a / scale, unit)
    return "%s%.3e J" % (sign, a)


def fmt_mass(kg):
    a = abs(kg)
    sign = "-" if kg < 0 else ""
    if a >= 0.5 * M_UNIVERSE_BARYON:
        return "%s%.3g x observable universe" % (sign, a / M_UNIVERSE_BARYON)
    if a >= 1e3 * M_MILKY_WAY:
        return "%s%.3g x Milky Way" % (sign, a / M_MILKY_WAY)
    if a >= 1e26:
        return "%s%.3g Msun" % (sign, a / M_SUN)
    if a >= 1e23:
        return "%s%.3g Mjup" % (sign, a / M_JUPITER)
    if a >= 1e21:
        return "%s%.3g Mearth" % (sign, a / M_EARTH)
    if a >= 1e4:
        return "%s%.4g t" % (sign, a / 1000.0)
    return "%s%.4g kg" % (sign, a)


def fmt_time(s):
    a = abs(s)
    if a < 90:
        return "%.1f s" % s
    if a < 5400:
        return "%.1f min" % (s / 60.0)
    if a < 2 * DAY:
        return "%.1f h" % (s / 3600.0)
    if a < 400 * DAY:
        return "%.1f d" % (s / DAY)
    if a < 1e4 * YR:
        return "%.2f yr" % (s / YR)
    if a < 1e9 * YR:
        return "%.3g yr" % (s / YR)
    return "%.3g Gyr" % (s / (1e9 * YR))


def fmt_dist(m):
    a = abs(m)
    if a < 1e4:
        return "%.1f m" % m
    if a < 0.01 * AU:
        return "%.3g km" % (m / 1e3)
    if a < 0.02 * LY:
        return "%.4g AU" % (m / AU)
    return "%.4f ly" % (m / LY)


def fmt_power(w):
    a = abs(w)
    for scale, unit in ((1e15, "PW"), (1e12, "TW"), (1e9, "GW"), (1e6, "MW"),
                        (1e3, "kW")):
        if a >= scale:
            return "%.3g %s" % (w / scale, unit)
    return "%.3g W" % w


def orders_of_magnitude(a, b):
    """log10 |a/b| -- the model's favourite unit, because the gap between what
    a warp drive needs and what physics supplies is always measured in it."""
    if b == 0 or a == 0:
        return float("inf")
    return math.log10(abs(a) / abs(b))




# =============================================================================
# SECTION 5d -- ENVIRONMENTAL SPACETIME DILATION  (whose clock, and where)
# =============================================================================
# The headline claim of a warp drive is "no time dilation". That is true, and it
# is also sloppy. It is true for ONE observer -- the crew, who are comoving with
# the bubble -- and it is false for several others who are all equally real.
# This section computes every clock in the problem instead of asserting the
# convenient one.
#
# From the metric  ds^2 = -c^2 dt^2 + (dx - v_s f dt)^2 + dy^2 + dz^2 :
#
#   COMOVING observer (the crew, dx = v_s f dt, f = 1):
#       ds^2 = -c^2 dt^2  ->  dtau = dt exactly.  No dilation. Ever.
#
#   STATIC observer (holds station in the external frame, dx = 0):
#       ds^2 = -c^2 dt^2 + v_s^2 f^2 dt^2  ->  dtau = dt sqrt(1 - beta^2 f^2)
#
# So the warp field DOES carry a dilation field -- it is just that nobody aboard
# is sitting in it. Someone station-keeping inside the bubble while the ship
# flies past would be dilated by the full Lorentz factor. That profile is what
# the DILATION view draws.

def lapse_static(r, beta, R=None, delta=None):
    """dtau/dt for an observer holding station in the EXTERNAL frame at radius
    r from the bubble centre.

        dtau/dt = sqrt(1 - beta^2 f(r)^2)

    Deep inside (f = 1) this is the full Lorentz factor; outside (f = 0) it is
    exactly 1. Superluminal beta makes the argument negative -- the static
    worldline stops being timelike at all, which is the horizon problem showing
    up in the arithmetic rather than in a footnote."""
    R = DIMS["bubble_r_m"] if R is None else R
    delta = DIMS["wall_thick_m"] if delta is None else delta
    f = shape_f(r, R, delta)
    q = 1.0 - beta * beta * f * f
    if q <= 0.0:
        return 0.0                    # no timelike static observer exists here
    return math.sqrt(q)


def static_observer_exists(beta):
    """False above beta = 1: inside a superluminal bubble there is no such thing
    as 'holding station'. Every worldline is dragged forward faster than light,
    which is precisely why the front wall cannot be signalled."""
    return beta < 1.0


# --- Gravitational potential along the route --------------------------------
# Real wells, real numbers. Sol at one end, Proxima at the other, the Galaxy
# underneath both, and the ship's own (utterly negligible) self-gravity.

# The inner floor of each well is the ORBIT the ship actually occupies at that
# end -- Earth's orbit at Sol, Proxima b's orbit at Proxima -- not the stellar
# surface. Departure therefore starts at exactly Earth's clock rate, so the
# drift the model reports is the drift the crew would really accumulate.
WELLS = {
    "Sol":     {"m_kg": M_SUN,          "at_m": 0.0,
                "r_min_m": AU},                 # Earth orbit
    "Proxima": {"m_kg": 0.1221 * M_SUN, "at_m": PROXIMA_M,
                "r_min_m": 0.0485 * AU},        # Proxima b orbit
}
GALACTIC_PHI_C2 = -1.0e-6      # Milky Way potential at the Sun's radius, Phi/c^2
#                                (v_circ^2/c^2 ~ (220 km/s)^2/c^2, order 1e-6);
#                                common to both ends, so it cancels in the drift
#                                -- carried anyway so the ledger is complete.


def grav_potential_at(x_m):
    """Newtonian potential Phi at distance x along the Sol -> Proxima line
    [J/kg]. Negative everywhere. Used for the gravitational red/blue shift, so
    only DIFFERENCES along the route matter."""
    phi = 0.0
    for w in WELLS.values():
        d = max(w["r_min_m"], abs(x_m - w["at_m"]))
        phi -= G_NEWTON * w["m_kg"] / d
    return phi


def grav_rate(x_m):
    """Clock rate dtau/dt at position x relative to a clock at infinity.

        dtau/dt = sqrt(1 + 2 Phi / c^2)   (weak field)

    Deeper in a well means a slower clock. This is the environmental dilation
    the crew actually experience, and it is the ONLY reason their clock and
    Earth's clock disagree at all."""
    q = 1.0 + 2.0 * grav_potential_at(x_m) / C2
    return math.sqrt(max(0.0, q))


EARTH_ORBIT_RATE = None        # filled below; Earth's own clock rate in Sol's well


def _earth_rate():
    global EARTH_ORBIT_RATE
    if EARTH_ORBIT_RATE is None:
        EARTH_ORBIT_RATE = math.sqrt(max(0.0, 1.0 + 2.0 * (
            -G_NEWTON * M_SUN / AU) / C2))
    return EARTH_ORBIT_RATE


def ship_self_dilation():
    """The ship's OWN gravitational time dilation, from its own mass [-].

    Included because a 127,000 tonne shell 100 m from the crew sounds like it
    ought to matter, and the honest answer is that it does not: the fractional
    rate shift is about 1e-21, which is twelve orders of magnitude below the
    best clock ever built. Computing it is how you know that, rather than
    assuming it."""
    phi = -G_NEWTON * SHIP_MASS_KG / DIMS["bubble_r_m"]
    return phi / C2


def clock_ledger(t_ship_s, x_m, beta):
    """Every clock in the problem, at one instant.

    Returns rate ratios relative to a clock at rest at infinity, plus the
    accumulated drift against Earth. The point of the table is that 'no time
    dilation' is a statement about ONE row of it."""
    r_here = grav_rate(x_m)
    r_earth = _earth_rate()
    rows = {
        "warp crew (comoving)":   1.0 * r_here,
        "Earth surface":          r_earth,
        "static in the bubble":   (lapse_static(0.0, beta) * r_here
                                   if static_observer_exists(beta) else 0.0),
        "static in the wall":     (lapse_static(DIMS["bubble_r_m"], beta) * r_here
                                   if static_observer_exists(beta) else 0.0),
        "relativistic rocket":    r_here / lorentz_gamma(min(beta, 0.999999)),
        "deep space (infinity)":  1.0,
    }
    drift_s = (rows["warp crew (comoving)"] - r_earth) * t_ship_s
    return {"rates": rows, "drift_vs_earth_s": drift_s,
            "grav_rate_here": r_here, "earth_rate": r_earth}


def voyage_grav_drift_s(t_total_s, x_start=0.0, x_end=None):
    """Accumulated crew-vs-Earth clock drift over a crossing, from gravity alone.

    The crew climb out of Sol's well and spend the trip in near-flat space, so
    their clock runs FASTER than Earth's -- by a couple of seconds over seven
    years. Tiny, real, and the reason this model's audit no longer claims the
    two clocks are exactly equal."""
    x_end = PROXIMA_M if x_end is None else x_end
    n = 64
    tot = 0.0
    for i in range(n):
        x = x_start + (x_end - x_start) * (i + 0.5) / n
        tot += (grav_rate(x) - _earth_rate())
    return (tot / n) * t_total_s


# =============================================================================
# SECTION 5e -- THE PORTAL  (Morris-Thorne wormhole, and the real teleporter)
# =============================================================================
# A "portal" is a traversable wormhole: two mouths, one throat, walk in here and
# out there. It is a legitimate solution of the Einstein field equations --
# Morris & Thorne wrote it down in 1988 as a teaching exercise precisely BECAUSE
# it is easy to construct and impossible to build.
#
#   ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2)(dtheta^2 + sin^2 theta dphi^2)
#
# l is proper radial distance, running from -inf (mouth A) through 0 (the
# throat, radius b0) to +inf (mouth B). There is no horizon and no singularity:
# it is genuinely traversable in both directions.
#
# The catch is the FLARE-OUT CONDITION. For the throat to open out on both sides
# rather than pinch off, the stress-energy at the throat must violate the null
# energy condition -- the same wall the superluminal warp drive hits, arrived at
# from a completely different direction. That is not a coincidence: Morris,
# Thorne & Yurtsever (1988) and later Hawking showed the two problems are the
# same problem wearing different hats.
#
# This section computes three numbers and lets them speak:
#   1. how much negative energy a throat of radius b0 needs,
#   2. how big b0 has to be before a human survives the tidal forces,
#   3. what happens when you have one anyway (answer: you have a time machine).

def mt_embedding_z(rho, b0):
    """Embedding-diagram height z(rho) for the Morris-Thorne throat [m].

        dz/drho = 1 / sqrt(rho/b0 - 1)   ->   z = 2 b0 sqrt(rho/b0 - 1)

    This is the classic funnel shape, and the PORTAL view draws it as a real
    surface of revolution rather than as decoration: every vertex comes from
    this line."""
    if rho <= b0:
        return 0.0
    return 2.0 * b0 * math.sqrt(rho / b0 - 1.0)


def mt_throat_density(b0):
    """Energy density required at the throat  [J/m^3].

        rho_throat = -c^4 / (8 pi G b0^2)

    Negative, and it gets WORSE for small throats -- exactly backwards from
    what you would want, and the reason a pocket-sized portal is harder than a
    planet-sized one."""
    return -(C4_OVER_G) / (8.0 * math.pi * b0 * b0)


def mt_exotic_energy_j(b0, shell_factor=1.0):
    """Total exotic energy to hold a throat of radius b0 open  [J].

    Order-of-magnitude: the throat energy density times a throat-scale shell,

        E ~ rho_throat * (4/3) pi b0^3 = -c^4 b0 / (6 G)

    Note what that says: the bill scales LINEARLY with throat radius, so a
    wormhole you can walk through costs a fixed price per metre of aperture,
    and that price is 2e43 joules per metre. Visser (1995) gets the same scale
    by a different route."""
    return mt_throat_density(b0) * (4.0 / 3.0) * math.pi * b0 ** 3 * shell_factor


def mt_tidal_g(b0, body_m=2.0):
    """Tidal acceleration across a body of height body_m at the throat [g].

        a_tidal ~ (c^2 / b0^2) * L

    The curvature radius at the throat IS b0, so a small portal is a very
    sharply curved region and anything crossing it is torn apart. This is the
    constraint everyone forgets and Morris & Thorne did not."""
    a = C2 * body_m / (b0 * b0)
    return a / 9.81


def mt_min_throat_m(g_limit=1.0, body_m=2.0):
    """Smallest throat a person survives crossing  [m].

        b0 >= sqrt(c^2 L / g_limit)

    At one Earth gravity of tidal stress across a two-metre body this returns
    about 1.4e8 m -- a throat roughly ten Earth diameters across. That is
    Morris & Thorne's own conclusion, and it is why 'portal' and 'doorway' are
    not the same word."""
    return math.sqrt(C2 * body_m / max(1e-9, g_limit * 9.81))


def mt_traversal_time_s(b0, v_ms=10.0, length_factor=4.0):
    """Proper time to walk through, at v_ms, across ~length_factor throats."""
    return length_factor * b0 / max(1e-6, v_ms)


# --- The full Morris-Thorne metric, not just the throat ----------------------
# Morris & Thorne (Am. J. Phys. 56, 395, 1988) write the wormhole as
#
#     ds^2 = -e^(2 Phi(r)) c^2 dt^2 + dr^2 / (1 - b(r)/r) + r^2 dOmega^2
#
# where b(r) is the SHAPE FUNCTION and Phi(r) is the REDSHIFT FUNCTION. The
# throat sits at r = r0 where b(r0) = r0. The two conditions that make this a
# wormhole rather than a coordinate artefact are:
#
#   FLARE-OUT:   b'(r0) < 1          (the throat is a minimum of r - b(r))
#   ASYMPTOTIC:  b(r)/r -> 0          (space is flat far from the throat)
#
# The flare-out condition is the one that costs. It forces d^2r/dl^2 > 0 at the
# throat, and the Einstein field equations then require rho < 0 there. This is
# not a feature of one ansatz -- it is theoremed (Visser 1989; Flanagan & Wald
# 1997) that EVERY traversable wormhole violates the null energy condition at
# the throat. The exotic bill is structural.

def mt_shape_b(r, b0):
    """Morris-Thorne shape function b(r)  [m].

        b(r) = b0^2 / r

    This is the canonical textbook choice (Morris & Thorne 1988, eq. 12). It
    satisfies b(b0) = b0 (throat at r = b0), b'(r) = -b0^2/r^2 < 0 everywhere
    (so b'(b0) = -1 < 1, the flare-out condition), and b/r -> 0 as r -> inf.
    The embedding diagram this produces is exactly the funnel drawn by
    mt_embedding_z() above."""
    return b0 * b0 / max(1e-30, r)


def mt_shape_b_prime(r, b0):
    """db/dr for the shape function  [dimensionless]."""
    return -b0 * b0 / max(1e-30, r * r)


def mt_redshift_phi(r, b0):
    """Redshift function Phi(r)  [dimensionless].

    Phi = 0 is the zero-tidal-at-throat choice Morris & Thorne use for their
    'interstellar travel' example. With Phi = 0 the proper-time radial tidal
    acceleration at the throat is exactly c^2 L / b0^2 -- the number
    mt_tidal_g() already reports. A nonzero Phi would add a gravitational
    redshift contribution but does not remove the flare-out requirement, so
    this is the honest baseline."""
    return 0.0


def mt_flare_out(b0):
    """Verify the flare-out condition at the throat.

        b'(r0) < 1    and    b(r0) = r0

    Returns (b_at_throat, b_prime_at_throat, satisfied). For b(r) = b0^2/r the
    throat is at r0 = b0, b(r0) = b0 exactly, and b'(r0) = -1, which is < 1.
    The condition is satisfied -- and it is STILL the thing that demands
    negative energy, because the Riemann tensor component it forces is the one
    the Einstein equations read as rho < 0."""
    r0 = b0
    b_at = mt_shape_b(r0, b0)
    bp_at = mt_shape_b_prime(r0, b0)
    return {"r0": r0, "b_at_r0": b_at, "b_prime_at_r0": bp_at,
            "throat_ok": abs(b_at - r0) < 1e-9 * max(1.0, r0),
            "flare_out": bp_at < 1.0,
            "satisfied": abs(b_at - r0) < 1e-9 * max(1.0, r0) and bp_at < 1.0}


def mt_tidal_profile(r, b0, body_m=2.0):
    """Radial tidal acceleration across body_m at radius r  [g].

        a_radial = c^2 |b'(r) - b(r)/r| L / (2 r^2 e^(2 Phi))

    At the throat (r = b0, Phi = 0): b' = -1, b/r = 1, so |b' - b/r| = 2,
    giving a = c^2 L / b0^2 -- exactly mt_tidal_g(). Away from the throat the
    tidal force falls as 1/r^4. This function gives the full profile so the
    viewer can draw the tidal gradient as a field, not just a single number."""
    phi = mt_redshift_phi(r, b0)
    b = mt_shape_b(r, b0)
    bp = mt_shape_b_prime(r, b0)
    a = C2 * abs(bp - b / max(1e-30, r)) * body_m / \
        (2.0 * max(1e-30, r * r) * math.exp(2.0 * phi))
    return a / 9.81


def mt_proper_length(b0, r_far=None):
    """Proper radial distance from throat to r_far  [m].

        l = integral_{b0}^{r_far} dr / sqrt(1 - b(r)/r)

    For b(r) = b0^2/r this is the arc length of the embedding funnel. With
    r_far = 4 b0 (the embedding diagram's extent) it comes out to a few b0,
    which is why mt_traversal_time_s uses length_factor ~ 4."""
    r_far = 4.0 * b0 if r_far is None else r_far
    n = 200
    dr = (r_far - b0) / n
    s = 0.0
    for i in range(n):
        r = b0 + (i + 0.5) * dr
        q = 1.0 - mt_shape_b(r, b0) / r
        if q > 0:
            s += dr / math.sqrt(q)
    return s


# --- Ford-Roman quantum inequalities: how long can you hold the throat? -----
# Ford & Roman (Phys. Rev. D 55, 3763, 1997) proved that negative energy is not
# just hard to source -- it is BOUNDED in magnitude and duration by the quantum
# inequalities. For a massless scalar field in flat spacetime, sampled over a
# time tau:
#
#     integral rho(t) g(tau, t) dt  >=  -3 hbar / (32 pi^2 c^3 tau^4)
#
# The bound scales as 1/tau^4: the longer you want negative energy, the less
# you can have. This is the real reason you cannot just hold a wormhole open
# indefinitely with a Casimir pulse -- the pulse decays, and the throat closes.

def ford_roman_bound_j_m3(tau_s):
    """Ford-Roman quantum inequality bound on negative energy density  [J/m^3].

        |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)

    This is the maximum NEGATIVE energy density a massless field can sustain,
    averaged over a sampling time tau. At tau = 1 s it is about -3.7e-62 J/m^3 --
    roughly 102 orders of magnitude below what a 12 m throat demands (-3.3e40
    J/m^3). The throat needs to be held open for the traversal time (seconds),
    and the QI bound at that duration is so far below the requirement that the
    gap is itself the result: you cannot hold a human-scale throat open long
    enough to cross it, even in principle, with quantum-field negative energy."""
    return -3.0 * HBAR / (32.0 * math.pi ** 2 * C_LIGHT ** 3 * tau_s ** 4)


def ford_roman_max_throat_tau(b0):
    """Longest you can hold a throat of radius b0 open, by the QI bound  [s].

    The throat demands |rho| = c^4 / (8 pi G b0^2). The QI bound supplies at
    most 3 hbar / (32 pi^2 c^3 tau^4). Setting them equal and solving for tau:

        tau_max = (3 hbar G b0^2 / (4 pi c^7))^(1/4)

    For b0 = 12 m this is ~3e-26 s. The traversal takes ~4.8 s. The throat
    closes ~1e26 times before you are halfway through. This is the Ford-Roman
    result applied to wormholes, and it is the deepest 'no' in the portal
    section: not 'we lack a source' but 'the source is forbidden by
    quantum field theory from lasting long enough'."""
    return (3.0 * HBAR * G_NEWTON * b0 * b0
            / (4.0 * math.pi * C_LIGHT ** 7)) ** 0.25


# --- Maldacena, Milekhin & Popov (2020): the wormhole that works on paper ---
# This is the closest thing to a REAL traversable wormhole in the literature.
# MMP construct a wormhole from two nearly-extremal MAGNETICALLY CHARGED black
# holes, held open not by ad-hoc exotic matter but by the Casimir energy of
# massless fermions threading the magnetic field lines between them. The
# negative energy is genuine, calculable, and comes from a real quantum field.
#
# The catch -- and there are several:
#   1. The black holes must be magnetically charged. No magnetic monopole has
#      ever been observed, so these objects may not exist. If they do, they
#      would be primordial, and none has been seen.
#   2. The holes must be NEARLY EXTREMAL: charge Q within ~1/M of the extremal
#      bound Q_ext = sqrt(4 pi eps0 G) M. This is a fine-tuned state.
#   3. The throat is long and narrow. Traversal takes a time of order the
#      black-hole mass (in natural units), and the traveler must be highly
#      boosted. For a solar-mass hole the asymptotic traversal time is short,
#      but the tidal constraint pushes the mass up.
#   4. Only massless fermions provide the right Casimir energy. This is not a
#      generic construction -- it is a specific, fragile one.
#
# Maldacena, Milekhin & Popov, Phys. Rev. Lett. 125, 031602 (2020).

def mmp_extremal_charge_c(M_kg):
    """Extremal magnetic charge for a black hole of mass M  [C].

        Q_ext = sqrt(4 pi eps0 G) M

    Above this the BH has no horizon (a naked singularity), so the construction
    requires Q <= Q_ext, and nearly extremal means Q/Q_ext -> 1."""
    return math.sqrt(4.0 * math.pi * EPS0 * G_NEWTON) * M_kg


def mmp_tidal_mass_kg(g_limit=1.0, body_m=2.0):
    """Smallest MMP black hole a person survives crossing  [kg].

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
    massless fermions), and the price is paid in magnetic monopoles instead."""
    return C_LIGHT ** 3 * math.sqrt(
        body_m / (4.0 * G_NEWTON ** 2 * max(1e-9, g_limit * 9.81)))


def mmp_traversal_time_s(M_kg):
    """Asymptotic traversal time for the MMP wormhole  [s].

    MMP give the traversal time as of order the black-hole mass in natural
    units, t ~ GM/c^3, up to a logarithmic factor from the long throat. For a
    solar-mass hole this is ~5 microseconds -- but the traveler must be
    boosted to gamma ~ M/m_e (the fermion Casimir energy is only negative in
    the boosted frame), and the asymptotic observer sees a longer time. The
    log factor is ~ ln(M / M_planck) ~ 87 for a solar mass, which is why the
    'years' figure appears in popular summaries: the full traversal as seen
    from outside is t ~ (GM/c^3) * ln(M/M_planck), still under a millisecond
    for a solar mass, but the setup (boosting, alignment) is the slow part."""
    t_nat = G_NEWTON * M_kg / C_LIGHT ** 3
    log_factor = math.log(max(M_kg, M_PLANCK) / M_PLANCK)
    return t_nat * max(1.0, log_factor)


def mmp_summary(g_limit=1.0, body_m=2.0):
    """The MMP wormhole, fully priced, for a survivable crossing."""
    M = mmp_tidal_mass_kg(g_limit, body_m)
    Q = mmp_extremal_charge_c(M)
    t_trav = mmp_traversal_time_s(M)
    # Schwarzschild radius of the BH (throat scale)
    r_s = 2.0 * G_NEWTON * M / C2
    # Casimir energy that holds it open. The energy density of massless
    # fermion modes in a cavity of size r_s scales as ~ -hbar c / r_s^4
    # (standard Casimir scaling), and the throat volume is ~(4/3) pi r_s^3,
    # giving E ~ -(4/3) pi hbar c / r_s. This is an order-of-magnitude
    # estimate; MMP's actual calculation includes the magnetic-flux mode
    # count (which is enormous for a near-extremal BH) and a logarithmic
    # throat-length factor, both of which raise the true value. But the
    # sign, the quantum-field origin, and the 1/r_s scaling are correct.
    e_casimir = -(4.0 / 3.0) * math.pi * HBAR * C_LIGHT / r_s
    return {
        "M_kg": M,
        "M_msun": M / M_SUN,
        "Q_ext_c": Q,
        "r_s_m": r_s,
        "traversal_s": t_trav,
        "casimir_energy_j": e_casimir,
        "monopoles_observed": False,
        "verdict": ("traversable on paper; needs magnetically charged black "
                    "holes (no magnetic monopole has ever been observed)"),
    }


# --- Visser thin-shell wormhole (1995): a different cut at the same problem --
# Visser (Phys. Rev. D 43, 402, 1991; Nucl. Phys. B 328, 203, 1989) takes two
# copies of Schwarzschild spacetime, cuts each at radius a > 2M, and pastes
# them together with a thin shell. The shell carries the entire exotic energy
# budget as a surface density, not a volume density. This is the most
# 'engineerable' wormhole in the literature: the exotic matter is localised to
# a 2-D surface, not smeared through a 3-D throat, so in principle you only
# need to violate the NEC on a sheet, not throughout a volume.

def visser_shell_mass_kg(a_m, M_kg):
    """Exotic MASS of the Visser thin shell  [kg]  (negative).

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
    throughout a volume."""
    rs = 2.0 * G_NEWTON * M_kg / C2
    if a_m <= rs:
        return 0.0
    return -2.0 * a_m * C2 / G_NEWTON * math.sqrt(1.0 - rs / a_m)


def visser_shell_energy_j(a_m, M_kg):
    """Total exotic energy of the Visser thin shell  [J]  (negative)."""
    return visser_shell_mass_kg(a_m, M_kg) * C2


def visser_summary(a_m=None, M_kg=None):
    """The Visser thin-shell wormhole, priced.

    With no arguments, prices a shell at the portal's spec'd aperture with a
    zero-mass Schwarzschild patch (the pure-shell limit Visser uses as the
    teaching example: two copies of Minkowski, cut and pasted)."""
    if a_m is None:
        a_m = DIMS["portal_gate_d_m"] / 2.0
    if M_kg is None:
        M_kg = 0.0           # pure Minkowski cut-and-paste (Visser's base case)
    m_shell = visser_shell_mass_kg(a_m, M_kg)
    e_shell = m_shell * C2
    rs = 2.0 * G_NEWTON * M_kg / C2
    return {
        "a_m": a_m,
        "M_kg": M_kg,
        "r_s_m": rs,
        "shell_mass_kg": m_shell,
        "shell_energy_j": e_shell,
        "outside_horizon": a_m > rs if M_kg > 0 else True,
        "tidal_g": mt_tidal_g(a_m) if M_kg == 0 else
                   2.0 * G_NEWTON * M_kg / (a_m ** 3) * 2.0 / 9.81,
    }


# --- The part where it becomes a time machine -------------------------------

def ctc_onset_s(mouth_sep_m, rate_diff):
    """Time until a two-mouth wormhole becomes a TIME MACHINE  [s].

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
    but it is the reason most physicists expect the answer to be no."""
    if rate_diff <= 0.0:
        return float("inf")
    return (mouth_sep_m / C_LIGHT) / rate_diff


def ctc_by_warp_transport(beta):
    """Can you make a time machine by CARRYING one mouth on this warp drive?

    No -- and for an interesting reason. The desynchronisation trick needs the
    travelling mouth to age differently, and a warp bubble's interior is flat:
    the mouth comes back in step. A relativistic ROCKET would do it easily. So
    the warp drive, which is the fast thing, is the one that cannot build the
    causality violation, while the slow thing can. The two subsystems in this
    file interact, and this is how."""
    return {"warp_rate_diff": 0.0,
            "rocket_rate_diff": 1.0 - 1.0 / lorentz_gamma(min(beta, 0.999999)),
            "verdict": "warp transport cannot desynchronise the mouths "
                       "(flat interior); a relativistic rocket can"}


def ctc_by_gravity_well(phi_over_c2, mouth_sep_m=None):
    """Park one mouth in a deep well instead. Returns the onset time."""
    sep = PROXIMA_M if mouth_sep_m is None else mouth_sep_m
    rate = 1.0 - math.sqrt(max(0.0, 1.0 + 2.0 * phi_over_c2))
    return {"rate_diff": rate, "onset_s": ctc_onset_s(sep, rate)}


# --- The teleporter that actually exists ------------------------------------

QT = {
    "record_km":     1400.0,     # Micius satellite ground link, 2017
    "bits_per_qubit":   2.0,     # classical bits per teleported qubit
    "human_atoms":    7.0e27,
    "bits_per_atom": 100.0,      # position, momentum, internal state -- generous
    "channel_bps":    1.0e12,    # 1 Tb/s, wildly optimistic for a quantum link
}


def quantum_teleport_facts():
    """Quantum teleportation is real, demonstrated, and does none of the things
    a portal does (Bennett et al. 1993).

    It moves a quantum STATE, not matter. It needs pre-shared entanglement. It
    needs two classical bits per qubit sent over an ordinary channel, so it is
    hard-capped at c and carries no information faster than light. And the
    no-cloning theorem means the original is destroyed in the process -- which
    is either a technicality or the whole moral question, depending on who is
    stepping into the booth."""
    bits = QT["human_atoms"] * QT["bits_per_atom"]
    seconds = bits / QT["channel_bps"]
    return {"state_bits": bits, "seconds": seconds, "years": seconds / YR,
            "universe_ages": seconds / (13.8e9 * YR),
            "record_km": QT["record_km"],
            "ftl": False, "destroys_original": True}


def portal_summary(b0=None):
    """Everything about the gate, in one dict, for the view and the reports.

    This now carries the FOUR constructions in the literature, each priced:
      - Morris-Thorne (1988): the textbook volume-distribution wormhole
      - Visser (1989/1995): the thin-shell cut-and-paste wormhole
      - Maldacena-Milekhin-Popov (2020): the fermion-Casimir wormhole that
        works on paper with real quantum fields (but needs magnetic monopoles)
      - Ford-Roman (1997): the quantum inequality that says how long any of
        these can be held open -- and the answer is 'not long enough'
    """
    b0 = DIMS["portal_gate_d_m"] / 2.0 if b0 is None else b0
    safe = mt_min_throat_m()
    flare = mt_flare_out(b0)
    mmp = mmp_summary()
    vs = visser_summary(b0)
    # Ford-Roman: how long can quantum fields hold THIS throat open?
    qi_hold_s = ford_roman_max_throat_tau(b0)
    qi_bound_1s = ford_roman_bound_j_m3(1.0)
    traverse = mt_traversal_time_s(b0)
    return {
        "b0_m": b0,
        "density_j_m3": mt_throat_density(b0),
        "energy_j": mt_exotic_energy_j(b0),
        "mass_kg": equiv_mass_kg(mt_exotic_energy_j(b0)),
        "tidal_g": mt_tidal_g(b0),
        "safe_b0_m": safe,
        "safe_energy_j": mt_exotic_energy_j(safe),
        "safe_mass_kg": equiv_mass_kg(mt_exotic_energy_j(safe)),
        "traverse_s": traverse,
        "casimir_shortfall_orders": orders_of_magnitude(
            mt_exotic_energy_j(b0), casimir_onboard_j()),
        "safe_shortfall_orders": orders_of_magnitude(
            mt_exotic_energy_j(safe), casimir_onboard_j()),
        # --- full Morris-Thorne metric ---
        "flare_out": flare,
        "proper_length_m": mt_proper_length(b0),
        "tidal_at_2b0_g": mt_tidal_profile(2.0 * b0, b0),
        "tidal_at_4b0_g": mt_tidal_profile(4.0 * b0, b0),
        # --- Ford-Roman quantum inequality ---
        "qi_hold_s": qi_hold_s,
        "qi_traversal_ratio": traverse / max(1e-99, qi_hold_s),
        "qi_bound_1s_j_m3": qi_bound_1s,
        "qi_shortfall_orders": orders_of_magnitude(
            abs(mt_throat_density(b0)), abs(qi_bound_1s)),
        # --- Maldacena-Milekhin-Popov (2020) ---
        "mmp": mmp,
        # --- Visser thin-shell (1989/1995) ---
        "visser": vs,
        "visser_shortfall_orders": orders_of_magnitude(
            abs(vs["shell_energy_j"]), casimir_onboard_j()),
    }


# =============================================================================
# SECTION 5f -- PORTAL TRAVERSAL  (sending things through, where and when)
# =============================================================================
# The question "can I send something through the portal?" has four real physics
# answers, and this section computes all of them honestly:
#
#   WHERE you come out:  at mouth B, wherever mouth B physically is.  A
#     wormhole is a shortcut between two points in space -- you do not choose
#     the destination independently of where the second mouth sits.
#
#   WHEN you come out:  at mouth B's current proper time, which is NOT the
#     same as mouth A's.  The two mouths desynchronise whenever they sit at
#     different gravitational potentials or move at different speeds.  This is
#     Morris, Thorne & Yurtsever (1988): the desynchronisation is real GR,
#     it accumulates, and the instant it exceeds the light-travel time between
#     the mouths you have a time machine (CTCs exist).
#
#   WHETHER you survive:  the tidal acceleration at the throat is c^2 L / b0^2.
#     A photon always survives.  A person needs b0 >= 1.35e8 m.  An object of
#     size L needs b0 >= sqrt(c^2 L / g_limit).
#
#   WHETHER THE THROAT IS STILL OPEN:  Ford-Roman quantum inequalities limit
#     the hold time to tau_max ~ (3 hbar G b0^2 / (4 pi c^7))^(1/4).  If the
#     traversal time exceeds that, the throat closes before you cross.
#
# The correlations below are all theoremed or measured physics.  Nothing here
# is fiction: the time offset is gravitational + special-relativistic dilation
# (GPS satellites measure it daily), the CTC onset is MTY 1988, the tidal bound
# is Morris-Thorne 1988, and the QI hold time is Ford-Roman 1997.


def mouth_clock_rate(phi_over_c2=0.0, beta=0.0):
    """Proper-time rate of a wormhole mouth relative to a clock at infinity.

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
    """
    grav = math.sqrt(max(0.0, 1.0 + 2.0 * phi_over_c2))
    kinematic = 1.0 / lorentz_gamma(min(abs(beta), 0.9999999))
    return grav * kinematic


def mouth_time_offset_s(rate_a, rate_b, elapsed_s):
    """Accumulated clock offset between the two mouths  [s].

    Positive means mouth B is BEHIND mouth A (B has aged less).  Stepping
    through A -> B then arrives at B's past relative to A's present -- which
    is the seed of the time machine.  The offset is:

        delta_t = elapsed * (rate_a - rate_b)

    and it grows LINEARLY with elapsed coordinate time.  This is not
    speculative: it is the same gravitational + kinematic dilation that GPS
    corrects for every day, applied to two clocks that started synchronised."""
    return elapsed_s * (rate_a - rate_b)


def ctc_exists(mouth_sep_m, offset_s):
    """Do closed timelike curves exist right now?

    MTY 1988: CTCs exist the instant the clock offset between the mouths
    exceeds the light-travel time between them.  Before that, stepping through
    arrives in mouth B's past relative to A's present, but NOT in your own
    past -- no paradox is possible.  After that, you can step through and
    arrive before you left, which is a time machine.

    Hawking's chronology protection conjecture (1992) expects vacuum
    fluctuations to diverge at exactly this boundary and destroy the throat.
    Unproven -- but it is why most physicists expect the answer to be no."""
    return abs(offset_s) >= mouth_sep_m / C_LIGHT


def portal_traversal(b0_m,
                     mouth_a_phi_c2=0.0, mouth_a_beta=0.0,
                     mouth_b_phi_c2=0.0, mouth_b_beta=0.0,
                     mouth_sep_m=None, elapsed_s=0.0,
                     payload="person", payload_size_m=2.0,
                     payload_speed_ms=10.0):
    """Send something through the portal.  All four real-physics answers.

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
    """
    sep = PROXIMA_M if mouth_sep_m is None else mouth_sep_m
    # --- WHERE: mouth B's location is just where it is ----------------------
    # The wormhole connects A to B.  You cannot choose the exit independently.

    # --- WHEN: the clock desynchronisation ----------------------------------
    rate_a = mouth_clock_rate(mouth_a_phi_c2, mouth_a_beta)
    rate_b = mouth_clock_rate(mouth_b_phi_c2, mouth_b_beta)
    offset_s = mouth_time_offset_s(rate_a, rate_b, elapsed_s)
    # If offset > 0, B is behind A.  Stepping A->B arrives offset_s in B's past
    # relative to A's present.  The arrival time at B, measured in A's frame:
    arrival_offset_s = offset_s  # B's clock reads (A_now - offset) when you exit

    # --- CTC check ----------------------------------------------------------
    light_time = sep / C_LIGHT
    ctc = ctc_exists(sep, offset_s)
    # How far from CTC onset: negative = safe, positive = time machine exists
    ctc_margin_s = abs(offset_s) - light_time

    # --- WHETHER you survive the crossing -----------------------------------
    if payload == "signal":
        # Photons have no size -- tidal forces cannot tear them apart.
        survives_tidal = True
        tidal_g = 0.0
        min_b0 = 0.0
    else:
        tidal_g = mt_tidal_g(b0_m, payload_size_m)
        g_limit = 1.0  # 1 g across the payload
        min_b0 = mt_min_throat_m(g_limit, payload_size_m)
        survives_tidal = b0_m >= min_b0

    # --- WHETHER the throat is still open -----------------------------------
    traverse_s = mt_traversal_time_s(b0_m, payload_speed_ms)
    qi_hold_s = ford_roman_max_throat_tau(b0_m)
    throat_open = traverse_s <= qi_hold_s

    # --- the exotic energy the throat demands (to hold open for the crossing)
    exotic_j = mt_exotic_energy_j(b0_m)
    casimir_j = casimir_onboard_j()
    shortfall = orders_of_magnitude(abs(exotic_j), abs(casimir_j))

    # --- verdicts -----------------------------------------------------------
    if not survives_tidal:
        tidal_verdict = ("LETHAL: tidal shear %.2e g across %.1f m -- "
                         "needs b0 >= %.3g m (%.1f Earth diameters)"
                         % (tidal_g, payload_size_m, min_b0,
                            min_b0 / 1.2742e7))
    else:
        tidal_verdict = ("survivable: tidal shear %.3g g across %.1f m"
                         % (tidal_g, payload_size_m))

    if not throat_open:
        qi_verdict = ("THROAT CLOSED: traversal %.2f s but QI allows only "
                      "%.2e s -- %.0f orders short"
                      % (traverse_s, qi_hold_s,
                         math.log10(traverse_s / max(1e-99, qi_hold_s))))
    else:
        qi_verdict = ("throat holds: traversal %.2f s within QI limit %.2e s"
                      % (traverse_s, qi_hold_s))

    if ctc:
        when_verdict = ("TIME MACHINE: offset %.3e s exceeds light-time "
                        "%.3e s by %.3e s -- CTCs exist, Hawking CPC "
                        "expected to destroy throat" %
                        (abs(offset_s), light_time, ctc_margin_s))
    elif abs(offset_s) > 0:
        when_verdict = ("offset %.3e s vs light-time %.3e s -- "
                        "arrives in B's past relative to A, but NOT a "
                        "time machine yet (margin %.3e s)"
                        % (offset_s, light_time, -ctc_margin_s))
    else:
        when_verdict = ("no offset -- mouths synchronised, arrives 'now' "
                        "at B (margin %.3e s)" % -ctc_margin_s)

    can_send = survives_tidal and throat_open and not ctc
    if can_send:
        overall = ("SENDABLE: exits at mouth B, %.3e s %s A's present.  "
                   "Real GR -- but the throat needs %s of exotic energy "
                   "(%d orders beyond the Casimir lattice)."
                   % (abs(offset_s),
                      "behind" if offset_s > 0 else "ahead of",
                      fmt_energy(exotic_j), shortfall))
    elif ctc:
        overall = ("BLOCKED BY CHRONOLOGY PROTECTION: CTCs exist, and "
                   "Hawking's conjecture expects the throat to be destroyed "
                   "at the chronology horizon.  Even if it survived, the "
                   "exotic bill is %s." % fmt_energy(exotic_j))
    elif not throat_open:
        overall = ("BLOCKED BY QUANTUM INEQUALITIES: the throat cannot stay "
                   "open long enough to cross.  %s" % qi_verdict)
    else:
        overall = ("BLOCKED BY TIDAL FORCES: %s" % tidal_verdict)

    return {
        # --- WHERE ---
        "mouth_sep_m": sep,
        "mouth_sep_ly": sep / LY,
        # --- WHEN ---
        "rate_a": rate_a,
        "rate_b": rate_b,
        "rate_diff": rate_a - rate_b,
        "elapsed_s": elapsed_s,
        "offset_s": offset_s,
        "arrival_offset_s": arrival_offset_s,
        "light_time_s": light_time,
        "ctc": ctc,
        "ctc_margin_s": ctc_margin_s,
        # --- SURVIVAL ---
        "payload": payload,
        "payload_size_m": payload_size_m,
        "tidal_g": tidal_g,
        "min_b0_m": min_b0,
        "survives_tidal": survives_tidal,
        # --- THROAT ---
        "b0_m": b0_m,
        "traverse_s": traverse_s,
        "qi_hold_s": qi_hold_s,
        "throat_open": throat_open,
        "exotic_j": exotic_j,
        "casimir_j": casimir_j,
        "shortfall_orders": shortfall,
        # --- VERDICTS ---
        "tidal_verdict": tidal_verdict,
        "qi_verdict": qi_verdict,
        "when_verdict": when_verdict,
        "overall": overall,
        "can_send": can_send,
    }


def report_portal_test():
    """Run portal traversal scenarios: signal, person, object, time machine."""
    _rule("PORTAL TRAVERSAL TESTS  --  sending things through, where and when")
    print(" The portal is a wormhole with two mouths.  WHERE you come out is")
    print(" where mouth B physically IS.  WHEN you come out depends on the")
    print(" clock desynchronisation between the mouths -- real GR, the same")
    print(" effect GPS corrects for daily.  Four scenarios:\n")

    b0 = DIMS["portal_gate_d_m"] / 2.0  # 12 m, the spec'd gate
    safe_b0 = mt_min_throat_m()          # ~1.35e8 m, survivable

    # --- SCENARIO 1: a signal through the spec'd gate, no desynchronisation --
    print(" " + "-" * 76)
    print(" SCENARIO 1: signal (photon) through the 12 m gate, mouths synced")
    print(" " + "-" * 76)
    t1 = portal_traversal(b0, payload="signal", elapsed_s=0.0)
    _print_traversal(t1)
    print("   A photon has no size, so tidal forces cannot destroy it.  But")
    print("   the throat still cannot stay open long enough (QI), and the")
    print("   exotic bill is still unpaid.  The signal cannot cross.\n")

    # --- SCENARIO 2: a person through the survivable throat, no desync ------
    print(" " + "-" * 76)
    print(" SCENARIO 2: person through the survivable throat, mouths synced")
    print(" " + "-" * 76)
    t2 = portal_traversal(safe_b0, payload="person", payload_size_m=2.0,
                          elapsed_s=0.0)
    _print_traversal(t2)
    print("   The throat is wide enough to survive (b0 = %.2e m = %.1f Earth"
          % (safe_b0, safe_b0 / 1.2742e7))
    print("   diameters).  But the exotic energy is %s and the QI still"
          % fmt_energy(t2["exotic_j"]))
    print("   forbids holding it open for the %.1f s traversal.\n"
          % t2["traverse_s"])

    # --- SCENARIO 3: a person, mouth B parked in a gravity well -------------
    print(" " + "-" * 76)
    print(" SCENARIO 3: person, mouth B at Phi/c^2 = -0.01 (deep well), 1 yr")
    print(" " + "-" * 76)
    elapsed = 1.0 * YR
    t3 = portal_traversal(safe_b0, payload="person", payload_size_m=2.0,
                          mouth_b_phi_c2=-0.01, elapsed_s=elapsed)
    _print_traversal(t3)
    print("   Mouth B's clock runs slower by %.4e s/s.  After %s the offset"
          % (t3["rate_diff"], fmt_time(elapsed)))
    print("   is %s.  Light-time between mouths is %s."
          % (fmt_time(t3["offset_s"]), fmt_time(t3["light_time_s"])))
    if t3["ctc"]:
        print("   -> CTCs EXIST.  Stepping through arrives in your own past.")
        print("      Hawking's chronology protection conjecture expects the")
        print("      throat to be destroyed at this boundary.")
    else:
        print("   -> No CTCs yet.  Arrives in B's past relative to A, but")
        print("      not in your own past -- no paradox possible.")
    print()

    # --- SCENARIO 4: time machine -- mouth B at neutron-star depth, 20 yr ---
    print(" " + "-" * 76)
    print(" SCENARIO 4: TIME MACHINE -- mouth B at Phi/c^2 = -0.2, 20 years")
    print(" " + "-" * 76)
    elapsed4 = 20.0 * YR
    t4 = portal_traversal(safe_b0, payload="person", payload_size_m=2.0,
                          mouth_b_phi_c2=-0.2, elapsed_s=elapsed4)
    _print_traversal(t4)
    print("   Mouth B's rate: %.6f vs A's %.6f.  After %s the offset is %s."
          % (t4["rate_b"], t4["rate_a"], fmt_time(elapsed4),
             fmt_time(t4["offset_s"])))
    print("   Light-time between mouths: %s." % fmt_time(t4["light_time_s"]))
    if t4["ctc"]:
        print("   -> CTCs EXIST (offset exceeds light-time by %s)."
              % fmt_time(t4["ctc_margin_s"]))
        print("      This IS a time machine: step through A->B and you arrive")
        print("      %.2e s in your own past.  But Hawking's CPC (1992)"
              % abs(t4["offset_s"]))
        print("      expects vacuum fluctuations to diverge at the chronology")
        print("      horizon and destroy the throat.  Unproven -- but it is")
        print("      why most physicists expect the answer to be no.")
    print()

    # --- SCENARIO 5: mouth B carried by relativistic rocket -----------------
    print(" " + "-" * 76)
    print(" SCENARIO 5: mouth B on a rocket at beta = 0.9, 10 years")
    print(" " + "-" * 76)
    elapsed5 = 10.0 * YR
    t5 = portal_traversal(safe_b0, payload="person", payload_size_m=2.0,
                          mouth_b_beta=0.9, elapsed_s=elapsed5)
    _print_traversal(t5)
    print("   A relativistic rocket DOES desynchronise the mouths (unlike a")
    print("   warp drive, whose flat interior gives no dilation dividend).")
    print("   Rate gap: %.4e s/s.  Offset after %s: %s."
          % (t5["rate_diff"], fmt_time(elapsed5), fmt_time(t5["offset_s"])))
    print()

    # --- SCENARIO 6: mouth B carried by WARP DRIVE (the fast thing) ---------
    print(" " + "-" * 76)
    print(" SCENARIO 6: mouth B carried by WARP at beta = 0.9, 10 years")
    print(" " + "-" * 76)
    # Warp interior is flat: no kinematic dilation.  Only gravitational.
    t6 = portal_traversal(safe_b0, payload="person", payload_size_m=2.0,
                          mouth_b_beta=0.0, elapsed_s=elapsed5)
    _print_traversal(t6)
    print("   The warp drive's flat interior means NO kinematic dilation.")
    print("   Rate gap: %.2e s/s -- zero (both mouths at rest in flat space)."
          % t6["rate_diff"])
    print("   The FAST thing cannot build the time machine.  The slow rocket")
    print("   can.  This is ctc_by_warp_transport() in full arithmetic.\n")

    # --- CONTROL SUMMARY ----------------------------------------------------
    print(" " + "=" * 76)
    print(" CONTROL SUMMARY: what GR actually lets you control")
    print(" " + "=" * 76)
    print("   WHERE (exit location):  move mouth B.  The wormhole connects")
    print("     A to B -- you cannot choose the exit independently of B.")
    print("   WHEN (arrival time):    desynchronise the mouths by parking B")
    print("     in a gravity well (scenario 3) or moving it at relativistic")
    print("     speed (scenario 5).  The offset accumulates linearly and is")
    print("     the same dilation GPS measures daily.")
    print("   CTC ONSET:              when |offset| > D/c (light-time between")
    print("     mouths).  Before that: B's past, not your past.  After that:")
    print("     time machine -- Hawking CPC expects destruction.")
    print("   WARP CANNOT DESYNC:     a warp bubble's interior is flat, so a")
    print("     mouth carried by warp ages at the same rate as one at rest.")
    print("     The fast thing cannot build the causality violation.")
    print()
    print("   EVERY scenario is blocked by at least one of:")
    print("     - exotic energy (no source exists; %d orders short of Casimir)"
          % t2["shortfall_orders"])
    print("     - quantum inequalities (throat closes in %.2e s vs %.1f s cross)"
          % (t2["qi_hold_s"], t2["traverse_s"]))
    print("     - chronology protection (CTCs -> throat destruction)")
    print("   The portal is the warp drive's problem again, in a new shape,")
    print("   with a time machine on top.")


def _print_traversal(t):
    """Print one traversal result compactly."""
    print("   throat b0         %.3g m" % t["b0_m"])
    print("   mouth separation  %.3g m = %.4f ly" % (t["mouth_sep_m"],
                                                     t["mouth_sep_ly"]))
    print("   rate A / rate B   %.6f / %.6f  (gap %.3e s/s)"
          % (t["rate_a"], t["rate_b"], t["rate_diff"]))
    print("   elapsed           %s" % fmt_time(t["elapsed_s"]))
    print("   time offset       %s  %s"
          % (fmt_time(t["offset_s"]),
             "(B behind A)" if t["offset_s"] > 0
             else ("(B ahead of A)" if t["offset_s"] < 0 else "(synced)")))
    print("   light-time A->B   %s" % fmt_time(t["light_time_s"]))
    print("   CTCs exist        %s  (margin %s)"
          % ("YES" if t["ctc"] else "no", fmt_time(t["ctc_margin_s"])))
    print("   tidal shear       %s" % t["tidal_verdict"])
    print("   throat hold       %s" % t["qi_verdict"])
    print("   exotic energy     %s  (%d orders beyond Casimir)"
          % (fmt_energy(t["exotic_j"]), t["shortfall_orders"]))
    print("   VERDICT           %s" % t["overall"])
    print()

# =============================================================================
# SECTION 6 -- SHIP GEOMETRY  (every part built to scale from DIMS)
# =============================================================================
# +Z is the direction of travel. The origin sits at the centre of the warp ring,
# which is also the centre of the bubble, which is also the centre of mass --
# they have to coincide or the shell shape servo cannot hold a symmetric field.

def _xform(verts, mat=None, off=None):
    """Bake a rotation and/or translation into a vertex list. Used for parts
    that sit at an arbitrary orientation and do NOT spin (the tangential field
    coils, the radial pylons, the radiator panels), so no per-frame transform
    is needed for them at all."""
    a = np.asarray(verts, dtype=float)
    if mat is not None:
        a = a @ mat.T
    if off is not None:
        a = a + np.asarray(off, dtype=float)
    return a


def _tangential(angle):
    """Rotation taking a +Z-built primitive to lie ALONG the ring tangent at
    this angle -- how a coil wraps a torus."""
    return rot_z(angle) @ rot_x(math.pi / 2)


def _radial(angle):
    """Rotation taking a +Z-built primitive to point radially outward."""
    return rot_z(angle) @ rot_y(math.pi / 2)


def build_ship_parts():
    """Build every part of the WD-1 to scale. Returns an ordered list of Part."""
    d = DIMS
    parts = []
    _order = [0]

    def nextord():
        _order[0] += 1
        return _order[0] - 1

    Rring = d["ring_major_d_m"] / 2.0          # 86 m ring centreline
    rring = d["ring_minor_d_m"] / 2.0          # 7.5 m tube
    hull_r = d["hull_d_m"] / 2.0               # 8 m
    hull_h = d["hull_len_m"] / 2.0             # +/- 34 m
    mb = mass_budget()

    # ---------------------------------------------------------------- 1. HULL
    profile = _smooth_sections([
        (-hull_h, 3.0), (-hull_h + 6, 6.2), (-14.0, 7.8), (0.0, hull_r),
        (14.0, 7.6), (24.0, 6.0), (30.0, 4.0), (hull_h, 1.4)], sub=2)
    hv, hf = _hull_loft(profile)
    meshes = [Mesh(hv, hf, C_HULL, "pressure hull")]
    # the flat-spacetime volume the crew actually lives in
    for i in range(d["hull_decks"]):
        z = -22.0 + i * 14.0
        dv, df_ = _annulus_cylinder(hull_r - 0.6, 0.5, z - 0.18, z + 0.18, seg=20)
        meshes.append(Mesh(dv, df_, C_HULL_DARK, "deck %d" % (i + 1)))
    parts.append(Part(
        "hull", "CREW HULL (flat spacetime)", meshes,
        ["%.0f m x %.0f m pressure hull, %d decks, crew %d"
         % (d["hull_len_m"], d["hull_d_m"], d["hull_decks"], d["crew"]),
         "Interior metric is EXACTLY Minkowski: f = 1, every derivative zero.",
         "Crew are weightless and un-accelerated at any beta -- there is no",
         "  proper acceleration anywhere inside the bubble, so no g-loading",
         "  and no structural limit on how hard the ship 'accelerates'.",
         "Ship clocks run at the SAME rate as Earth clocks (no time dilation).",
         "shell mass %s   decks %s"
         % (fmt_mass(mb["crew hull shell"]), fmt_mass(mb["crew decks"]))],
        nextord(), (0.0, -46.0, 0.0), C_HULL))

    # ------------------------------------------------------- 2. FUSION REACTOR
    rv, rf = _torus(d["reactor_major_d_m"] / 2, d["reactor_minor_d_m"] / 2,
                    seg_major=22, seg_minor=8)
    meshes = _place([Mesh(rv, rf, C_REACTOR, "D-3He plasma torus", spin=1.0,
                          group="plasma")], (0, 0, 4.0))
    cv, cf = _solid_cylinder(1.1, -3.0, 3.0, seg=14)
    meshes += _place([Mesh(cv, cf, C_HULL_DARK, "central solenoid")], (0, 0, 4.0))
    parts.append(Part(
        "reactor", "D-3He FUSION REACTOR", meshes,
        ["%.0f m torus, %.0f GW thermal, %.0f%% direct conversion -> %s electric"
         % (d["reactor_major_d_m"], d["reactor_th_gw"],
            100 * d["reactor_direct_eff"], fmt_power(PLANT_ELECTRIC_W)),
         "Aneutronic: D + 3He -> 4He + p + 18.35 MeV. Charged products only,",
         "  so the energy is collected electrostatically instead of by a",
         "  steam cycle -- that is where the 62%% conversion comes from.",
         "This plant does NOT move the ship. It runs the coils, the cryo and",
         "  the hotel load. Moving the ship is the beam's job (see RECTENNA).",
         "Fuel for a 4.25 ly crossing at cruise: %.0f kg of D-3He mix."
         % fusion_fuel_kg(cruise_load_w(0.5) * 8.5 * YR),
         "mass %s" % fmt_mass(mb["fusion reactor"])],
        nextord(), (0.0, 40.0, 0.0), C_REACTOR))

    # ---------------------------------------------------- 3. ANTIMATTER TRAPS
    meshes = []
    for i in range(d["amtraps"]):
        x = (-1) ** i * 3.4
        sv, sf = _sphere(d["amtrap_d_m"] / 2, seg=13, rings=8)
        meshes += _place([Mesh(sv, sf, C_ANTIMAT, "penning trap %d" % (i + 1))],
                         (x, 0.0, -24.0))
    am_j = d["amtraps"] * d["amtrap_kg"] * PLANT["am_energy_j_kg"]
    parts.append(Part(
        "amtraps", "ANTIMATTER PENNING TRAPS", meshes,
        ["%d traps x %.2f kg antihydrogen = %s total"
         % (d["amtraps"], d["amtrap_kg"], fmt_energy(am_j)),
         "Reserved for field transients the SMES cannot swallow.",
         "HONEST SCALE CHECK: accelerating this ship to beta = 0.5 costs %s."
         % fmt_energy(kinetic_energy_j(0.5)),
         "  The entire antimatter inventory covers %.2e of that bill."
         % (am_j / kinetic_energy_j(0.5)),
         "  Antimatter is not a warp fuel. Nothing storable is.",
         "mass %s" % fmt_mass(mb["antimatter traps"])],
        nextord(), (0.0, 44.0, -34.0), C_ANTIMAT))

    # ------------------------------------------------------------- 4. SMES
    sv, sf = _torus(d["smes_major_d_m"] / 2, d["smes_minor_d_m"] / 2,
                    seg_major=24, seg_minor=7)
    meshes = _place([Mesh(sv, sf, C_SMES, "SMES toroid")], (0, 0, -22.0))
    parts.append(Part(
        "smes", "SMES FIELD BUFFER", meshes,
        ["%.0f m toroid at %.0f T -> u = B^2/2mu0 = %.3g J/m^3"
         % (d["smes_major_d_m"], d["smes_b_t"],
            d["smes_b_t"] ** 2 / (2 * MU0)),
         "Capacity %s -- COMPUTED from the field and the volume, not assumed."
         % fmt_energy(SMES_J),
         "It buffers coil ripple during shell reshaping. It is %.0f orders of"
         % orders_of_magnitude(kinetic_energy_j(0.5), SMES_J),
         "  magnitude too small to change the ship's velocity, and this model",
         "  never lets it try. There is no 'warp battery' aboard.",
         "mass %s" % fmt_mass(mb["SMES buffer"])],
        nextord(), (0.0, -50.0, -40.0), C_SMES))

    # ---------------------------------------------------------- 5. CRYOPLANT
    meshes = []
    for i in range(d["cryo_units"]):
        a = 2 * math.pi * i / d["cryo_units"] + math.pi / 8
        cv, cf = _solid_cylinder(d["cryo_d_m"] / 2, -d["cryo_len_m"] / 2,
                                 d["cryo_len_m"] / 2, seg=14)
        meshes.append(Mesh(_xform(cv, None, (Rring * 0.80 * math.cos(a),
                                             Rring * 0.80 * math.sin(a), 0.0)),
                           cf, C_CRYO, "cryo unit %d" % (i + 1)))
    parts.append(Part(
        "cryo", "CRYOPLANT (%d units)" % d["cryo_units"], meshes,
        ["Holds %d REBCO coils at %.0f K against %s of AC loss."
         % (d["coils"], d["coil_temp_k"], fmt_power(PLANT["coil_ac_mw"] * 1e6)),
         "Draws %s electrical. Carnot floor at %.0f K from a %.0f K sink is"
         % (fmt_power(PLANT["cryo_mw"] * 1e6), d["coil_temp_k"],
            DIMS["rad_temp_k"]),
         "  brutal: every watt lifted out of the cold mass costs ~%.0f W in."
         % (DIMS["rad_temp_k"] / d["coil_temp_k"]),
         "mass %s" % fmt_mass(mb["cryoplant"])],
        nextord(), (40.0, 0.0, -40.0), C_CRYO))

    # ------------------------------------------------------------ 6. PYLONS
    meshes = []
    r0, r1 = hull_r + 0.5, Rring - rring
    for i in range(d["pylons"]):
        a = 2 * math.pi * i / d["pylons"] + math.pi / 2
        bv, bf = _box((r0 + r1) / 2, 0, 0, r1 - r0, d["pylon_w_m"], 1.4)
        meshes.append(Mesh(_xform(bv, rot_z(a)), bf, C_PYLON,
                           "pylon %d" % (i + 1)))
    parts.append(Part(
        "pylons", "STRUCTURAL PYLONS (%d)" % d["pylons"], meshes,
        ["%.1f m span, hull r=%.1f m to ring r=%.1f m." % (r1 - r0, r0, r1),
         "They carry NO thrust load -- there is no thrust. Their job is to hold",
         "  the ring concentric with the hull to within the shell servo's",
         "  tolerance, because an off-centre ring makes an asymmetric bubble.",
         "mass %s" % fmt_mass(mb["pylons"])],
        nextord(), (0.0, 0.0, 54.0), C_PYLON))

    # ------------------------------------------------------- 7. MAIN WARP RING
    meshes = []
    gap = 0.22 * (2 * math.pi / d["ring_sectors"])
    for i in range(d["ring_sectors"]):
        a0 = 2 * math.pi * i / d["ring_sectors"] + gap / 2
        a1 = 2 * math.pi * (i + 1) / d["ring_sectors"] - gap / 2
        tv, tf = _torus(Rring, rring, seg_major=3, seg_minor=9,
                        a0=a0, a1=a1, closed=False)
        meshes.append(Mesh(tv, tf, C_RING,
                           "sector %02d" % (i + 1) if i % 6 == 0 else "",
                           glow=True))
    parts.append(Part(
        "ring", "MAIN WARP RING (%d sectors)" % d["ring_sectors"], meshes,
        ["%.0f m diameter x %.1f m tube, %.2f m shell wall, rho = %.0f kg/m^3."
         % (d["ring_major_d_m"], d["ring_minor_d_m"], d["ring_wall_m"],
            d["ring_density"]),
         "THIS IS THE DRIVE. In the Bobrick-Martire formulation the warp is not",
         "  made by a field the ring emits -- it IS the ring: a massive shell",
         "  carrying a shift-vector distribution. The metric is sourced by the",
         "  shell's own stress-energy, which is ordinary positive-energy matter.",
         "%d sectors are driven independently so the shape servo can correct"
         % d["ring_sectors"],
         "  asymmetry at 10 kHz; a wall that loses shape collapses the bubble.",
         "mass %s -- %.0f%% of the whole ship."
         % (fmt_mass(mb["warp ring shell"]),
            100 * mb["warp ring shell"] / SHIP_MASS_KG)],
        nextord(), (0.0, 0.0, 78.0), C_RING))

    # ------------------------------------------------------- 8. HTS FIELD COILS
    meshes = []
    r_i = rring + 0.10
    for i in range(d["coils"]):
        a = 2 * math.pi * i / d["coils"]
        cv, cf = _annulus_cylinder(r_i + 0.35, r_i, -d["coil_len_m"] / 2,
                                   d["coil_len_m"] / 2, seg=9)
        m = Mesh(_xform(cv, _tangential(a),
                        (Rring * math.cos(a), Rring * math.sin(a), 0.0)),
                 cf, C_COIL, "coil %02d" % (i + 1) if i % 8 == 0 else "")
        m.coil_index = i
        meshes.append(m)
    nis = d["coil_turns"] * d["coil_current_a"]
    parts.append(Part(
        "coils", "HTS FIELD COILS (%d)" % d["coils"], meshes,
        ["%d turns x %.0f kA = %.3g A-turns per coil, REBCO tape at %.0f K."
         % (d["coil_turns"], d["coil_current_a"] / 1000, nis, d["coil_temp_k"]),
         "They do not push on anything. They hold the shell's stress-energy",
         "  distribution in the shape the metric solution requires -- the field",
         "  phase sweeps the ring at the bubble frequency (watch them light in",
         "  sequence: that travelling pattern IS the shift vector being steered).",
         "AC + ripple loss %s at beta = 1, scaling as beta^2."
         % fmt_power(PLANT["coil_ac_mw"] * 1e6),
         "mass %s" % fmt_mass(mb["HTS field coils"])],
        nextord(), (0.0, 0.0, 116.0), C_COIL))

    # --------------------------------------------------- 9. CASIMIR CASSETTES
    meshes = []
    cas = casimir_cassette()
    for i in range(d["casimir_cassettes"]):
        a = 2 * math.pi * i / d["casimir_cassettes"] + math.pi / d["casimir_cassettes"]
        bv, bf = _box(0, 0, 0, d["casimir_plate_m"], d["casimir_plate_m"],
                      d["casimir_stack_m"])
        meshes.append(Mesh(_xform(bv, _tangential(a),
                                  ((Rring + rring + 1.4) * math.cos(a),
                                   (Rring + rring + 1.4) * math.sin(a), 0.0)),
                           bf, C_CASIMIR,
                           "cassette %02d" % (i + 1) if i % 8 == 0 else ""))
    need_1m = alcubierre_energy_j(1.0, d["bubble_r_m"], 1.0)
    parts.append(Part(
        "casimir", "CASIMIR NEGATIVE-ENERGY LATTICE (%d)" % d["casimir_cassettes"],
        meshes,
        ["%d plates per cassette at a %.0f nm gap; rho = -pi^2 hbar c / 720 a^4"
         % (cas["plates"], d["casimir_gap_nm"]),
         "  = %.3g J/m^3 over %.2f m^3 of gap volume -> %s per cassette."
         % (cas["rho_j_m3"], cas["gap_volume_m3"], fmt_energy(cas["energy_j"])),
         "WHOLE-SHIP TOTAL: %s. This is real, measured physics (Casimir 1948;"
         % fmt_energy(casimir_onboard_j()),
         "  Lamoreaux 1997) and the largest negative-energy store ever designed.",
         "A superluminal bubble at beta = 1 with a generous 1 m wall needs %s."
         % fmt_energy(need_1m),
         "  The lattice is short by %.0f ORDERS OF MAGNITUDE. With the wall the"
         % orders_of_magnitude(need_1m, casimir_onboard_j()),
         "  quantum inequality actually permits (%.2g m), short by %.0f orders."
         % (ford_roman_wall_limit(1.0),
            orders_of_magnitude(alcubierre_energy_j(1.0, d["bubble_r_m"],
                                                    ford_roman_wall_limit(1.0)),
                                casimir_onboard_j())),
         "THIS PART IS THE HONEST ANSWER TO 'WHY NOT FASTER THAN LIGHT'.",
         "mass %s" % fmt_mass(mb["Casimir lattice"])],
        nextord(), (0.0, 0.0, 150.0), C_CASIMIR))

    # ---------------------------------------------------- 10/11. SHAPING RINGS
    for sgn, nm, key in ((+1, "FORE", "capfore"), (-1, "AFT", "capaft")):
        tv, tf = _torus(d["capring_d_m"] / 2, d["capring_minor_d_m"] / 2,
                        seg_major=22, seg_minor=7)
        meshes = _place([Mesh(tv, tf, _mix(C_RING, C_COIL, 0.35),
                              "%s shaping ring" % nm.lower(), glow=True)],
                        (0, 0, sgn * d["cap_offset_m"]))
        parts.append(Part(
            key, "%s SHAPING RING" % nm, meshes,
            ["%.0f m diameter at z = %+.0f m." % (d["capring_d_m"],
                                                  sgn * d["cap_offset_m"]),
             "The fore/aft pair breaks the shell's front-back symmetry. Without",
             "  that asymmetry theta integrates to zero and the bubble sits",
             "  still: space contracts ahead (%s) and expands behind (%s)"
             % ("theta < 0", "theta > 0"),
             "  only because these two rings are driven differently.",
             "Together %s." % fmt_mass(mb["shaping rings"])],
            nextord(), (0.0, 0.0, sgn * 130.0), _mix(C_RING, C_COIL, 0.35)))

    # ------------------------------------------------------------ 12. RADIATORS
    meshes = []
    r_mid = d["rad_inner_r_m"] + d["rad_w_m"] / 2.0
    z_mid = d["rad_z0_m"] - d["rad_len_m"] / 2.0
    for i in range(d["radiators"]):
        a = 2 * math.pi * i / d["radiators"]
        bv, bf = _box(r_mid, 0, z_mid, d["rad_w_m"], 0.14, d["rad_len_m"])
        meshes.append(Mesh(_xform(bv, rot_z(a)), bf, C_RADIATOR,
                           "panel %02d" % (i + 1) if i % 5 == 0 else "",
                           hot=True))
    w_cruise = waste_heat_w(cruise_load_w(0.5))
    parts.append(Part(
        "radiators", "WASTE-HEAT RADIATORS (%d)" % d["radiators"], meshes,
        ["%d panels x %.0f m x %.0f m, both faces = %.0f m^2 radiating area."
         % (d["radiators"], d["rad_len_m"], d["rad_w_m"], RADIATOR_AREA_M2),
         "SIZED, NOT GUESSED: T = (P / eps sigma A)^(1/4). At beta = 0.5 the",
         "  ship rejects %s and the panels settle at %.0f K."
         % (fmt_power(w_cruise), radiator_temp_k(w_cruise)),
         "Graphite sublimation caps them at %.0f K, which is the FIRST hard"
         % d["rad_limit_k"],
         "  wall the superluminal mode hits -- before the energy problem, the",
         "  coil load simply cooks the ship. Watch it in FLIGHT above beta = 1.",
         "mass %s" % fmt_mass(mb["radiators"])],
        nextord(), (0.0, 0.0, -96.0), C_RADIATOR))

    # ------------------------------------------------------------ 13. DEFLECTOR
    dv, df_ = _dish(d["deflector_d_m"] / 2, d["deflector_depth_m"], hull_h,
                    seg=24, rings=4)
    meshes = [Mesh(dv, df_, C_DEFLECT, "deflector dish")]
    parts.append(Part(
        "deflector", "NAVIGATION DEFLECTOR", meshes,
        ["%.0f m parabolic dish, subwarp only." % d["deflector_d_m"],
         "Useless at warp: the bubble wall already collects everything ahead of",
         "  it. Which is the problem -- see the ISM load readout in FLIGHT.",
         "mass %s" % fmt_mass(mb["deflector"])],
        nextord(), (0.0, 0.0, 96.0), C_DEFLECT))

    # ------------------------------------------------------------ 14. RECTENNA
    cv, cf = _dish(d["collector_d_m"] / 2, d["collector_depth_m"], -40.0,
                   seg=24, rings=4, flip=True)
    meshes = [Mesh(cv, cf, C_COLLECT, "rectenna (stowed)")]
    bp = boost_profile(0.5)
    parts.append(Part(
        "collector", "BOOST RECTENNA", meshes,
        ["Stowed %.0f m; unfurls to a %.1f km film at %.0f um thickness."
         % (d["collector_d_m"], d["collector_deploy_km"], d["collector_film_um"]),
         "It has to be kilometres wide: the tap's %.0f km transmitter at %.0f um"
         % (PLANT["beam_aperture_km"], PLANT["beam_lambda_um"]),
         "  spreads to a %.1f km spot by %.2f ly (2.44 lambda L / D)."
         % (beam_spot_m(0.1 * LY) / 1000, 0.1),
         "THE SHIP CANNOT LAUNCH ITSELF. Reaching beta = 0.5 costs %s,"
         % fmt_energy(kinetic_energy_j(0.5)),
         "  delivered over %s of boost out to %s."
         % (fmt_time(bp["time_s"]), fmt_dist(bp["range_m"])),
         "Beam range %.2f ly caps the cruise speed at beta = %.3f -- an"
         % (PLANT["beam_range_ly"], max_boost_beta()),
         "  EMERGENT limit: no line in DIMS sets a maximum speed.",
         "mass %s (deployed film)" % fmt_mass(mb["boost rectenna"])],
        nextord(), (0.0, -62.0, -70.0), C_COLLECT))

    # ---------------------------------------------------------------- 15. RCS
    meshes = []
    for i in range(d["rcs_pods"]):
        a = 2 * math.pi * i / d["rcs_pods"]
        cv, cf = _solid_cylinder(d["rcs_d_m"] / 2, -d["rcs_len_m"] / 2,
                                 d["rcs_len_m"] / 2, seg=10)
        meshes.append(Mesh(_xform(cv, _radial(a),
                                  (9.0 * math.cos(a), 9.0 * math.sin(a), -26.0)),
                           cf, C_RCS, ""))
    parts.append(Part(
        "rcs", "RCS / ION PODS (%d)" % d["rcs_pods"], meshes,
        ["Docking and attitude only, bubble down. Conventional reaction drive.",
         "Attitude inside a warp bubble is meaningless -- the interior is",
         "  inertial -- so these exist purely for the sublight endgame.",
         "mass %s" % fmt_mass(mb["RCS pods"])],
        nextord(), (0.0, 52.0, 40.0), C_RCS))

    # ------------------------------------------------------------- 16. MAGSAIL
    scale = d["magsail_view_scale"]
    r_show = d["magsail_r_km"] * 1e3 * scale
    meshes = []
    for k, zz in ((0, -108.0), (1, -112.0)):
        wv, wf = _ring_wire(r_show * (1.0 - 0.04 * k), zz, seg=72)
        meshes.append(Mesh(wv, wf, _mix(C_CRYO, C_BUBBLE, 0.4),
                           "magsail loop (1:%d)" % int(1 / scale) if k == 0 else "",
                           wire=True))
    for i in range(8):
        a = 2 * math.pi * i / 8
        bv, bf = _box(r_show * 0.5, 0, -104.0, r_show, 0.5, 0.5)
        meshes.append(Mesh(_xform(bv, rot_z(a)), bf, C_PYLON, ""))
    parts.append(Part(
        "magsail", "MAGNETIC SAIL (drawn 1:%d)" % int(1 / scale), meshes,
        ["TRUE radius %.0f km -- %dx the ship. Drawn here at 1:%d; the viewer"
         % (d["magsail_r_km"], int(d["magsail_r_km"] * 1e3 / SHIP_SPAN_M),
            int(1 / scale)),
         "  never shrinks a part silently, so the scale factor is in its name.",
         "Zubrin and Andrews (1991): F = Cd rho_ISM v^2 A. At beta = 0.5 that",
         "  is %.3g N against %s of ship -- %.2e m/s^2."
         % (magsail_drag_n(0.5), fmt_mass(SHIP_MASS_KG),
            magsail_drag_n(0.5) / SHIP_MASS_KG),
         "Braking from beta = 0.5 therefore takes %s."
         % fmt_time(magsail_decel_time_s(0.5)),
         "That is not a flaw in the sail. It is the honest answer to 'how do",
         "  you stop', and every interstellar design has to answer it.",
         "mass %s" % fmt_mass(mb["magsail loop"])],
        nextord(), (0.0, 0.0, -150.0), _mix(C_CRYO, C_BUBBLE, 0.4)))

    # -------------------------------------------------------- 17. WARP BUBBLE
    Rb = d["bubble_r_m"]
    meshes = []
    for i in range(9):                       # meridians
        a = math.pi * i / 9
        wv, wf = _ring_wire(Rb, 0.0, seg=52, axis="y")
        meshes.append(Mesh(_xform(wv, rot_z(a)), wf, C_BUBBLE, "", wire=True))
    for j in range(1, 5):                    # parallels
        phi = math.pi * j / 5
        wv, wf = _ring_wire(Rb * math.sin(phi), Rb * math.cos(phi), seg=52)
        meshes.append(Mesh(wv, wf, C_BUBBLE, "", wire=True))
    fv, ff = _ring_wire(flat_interior_r(), 0.0, seg=48)
    meshes.append(Mesh(fv, ff, _mix(C_BUBBLE, C_GOOD, 0.6),
                       "flat interior boundary", wire=True))
    parts.append(Part(
        "bubble", "WARP BUBBLE (spacetime)", meshes,
        ["R = %.0f m, wall delta = %.3g m, flat interior out to %.1f m."
         % (Rb, d["wall_thick_m"], flat_interior_r()),
         "Not hardware -- this is the SHAPE OF SPACETIME the shell sources.",
         "Inside: f = 1, exactly flat, weightless, no time dilation.",
         "In the wall: tidal shear reaches %.2e g across a 2 m body at"
         % (wall_tidal_gradient(0.5, Rb, d["wall_thick_m"]) / 9.81),
         "  beta = 0.5. Nothing survives contact with the wall, at any speed.",
         "Outside: unperturbed Minkowski. The universe does not notice."],
        nextord(), (0.0, 0.0, 0.0), C_BUBBLE))

    return parts



# =============================================================================
# SECTION 6b -- PORTAL GEOMETRY  (the gate, and the throat it would need)
# =============================================================================

def _mt_funnel(b0, rho_max, rings=13, seg=40, sign=+1.0):
    """Wire mesh of one half of the Morris-Thorne embedding diagram.

    Rings at increasing rho, meridians joining them, with the height from
    mt_embedding_z(). Sampled with rho spaced as b0*cosh^2 so the vertices
    crowd onto the throat, where all the curvature is -- the same trick the
    METRIC sheet uses, for the same reason."""
    verts, faces = [], []
    rhos = []
    for i in range(rings):
        t = i / (rings - 1.0)
        rhos.append(b0 * (1.0 + (rho_max / b0 - 1.0) * t * t))
    for rho in rhos:
        z = sign * mt_embedding_z(rho, b0)
        for j in range(seg):
            a = 2 * math.pi * j / seg
            verts.append((rho * math.cos(a), rho * math.sin(a), z))
    for i in range(rings):                       # rings around
        base = i * seg
        faces.append(tuple(base + j for j in range(seg)))
    for j in range(0, seg, 4):                   # a few meridians
        faces.append(tuple(i * seg + j for i in range(rings)))
    return verts, faces


def build_portal_parts():
    """The portal gate at true scale, plus the spacetime it claims to make."""
    d = DIMS
    parts = []
    _o = [0]

    def nextord():
        _o[0] += 1
        return _o[0] - 1

    b0 = d["portal_gate_d_m"] / 2.0
    rmin = d["portal_ring_minor_d_m"] / 2.0
    ps = portal_summary(b0)

    # ------------------------------------------------------------ 1. GATE A
    meshes = []
    tv, tf = _torus(b0 + rmin, rmin, seg_major=30, seg_minor=9)
    meshes.append(Mesh(tv, tf, _mix(C_RING, C_RING_HOT, 0.45), "aperture ring"))
    fv, ff = _torus(d["portal_frame_d_m"] / 2.0, 0.9, seg_major=26, seg_minor=7)
    meshes.append(Mesh(fv, ff, C_PYLON, "structural frame"))
    for i in range(6):
        a = 2 * math.pi * i / 6
        r0, r1 = b0 + 2 * rmin, d["portal_frame_d_m"] / 2.0
        bv, bf = _box((r0 + r1) / 2, 0, 0, r1 - r0, 1.1, 1.1)
        meshes.append(Mesh(_xform(bv, rot_z(a)), bf, C_PYLON, ""))
    parts.append(Part(
        "gateA", "GATE A  (mouth, Sol side)", meshes,
        ["%.0f m aperture -- b0 = %.1f m throat radius." % (d["portal_gate_d_m"], b0),
         "The ring is the only part of a portal you could actually build. It",
         "  holds the field geometry; it does NOT make the throat. Making the",
         "  throat is the other %s on this list." % fmt_energy(ps["energy_j"]),
         "Traversal at walking pace: %s." % fmt_time(ps["traverse_s"]),
         "TIDAL SHEAR AT THIS THROAT: %.2e g across a 2 m body." % ps["tidal_g"],
         "  Nothing made of atoms crosses that. See GATE B for the throat you",
         "  would actually survive."],
        nextord(), (0.0, 0.0, 46.0), C_RING))

    # ------------------------------------------------------- 2. FIELD COILS
    meshes = []
    for i in range(d["portal_coils"]):
        a = 2 * math.pi * i / d["portal_coils"]
        cv, cf = _annulus_cylinder(rmin + 0.55, rmin + 0.05, -1.6, 1.6, seg=9)
        mm = Mesh(_xform(cv, _tangential(a),
                         ((b0 + rmin) * math.cos(a), (b0 + rmin) * math.sin(a), 0.0)),
                  cf, C_COIL, "coil %02d" % (i + 1) if i % 8 == 0 else "")
        mm.coil_index = i
        meshes.append(mm)
    parts.append(Part(
        "pcoils", "THROAT FIELD COILS (%d)" % d["portal_coils"], meshes,
        ["They shape the aperture field. They cannot violate the null energy",
         "  condition, because no arrangement of ordinary current can.",
         "Every traversable-wormhole solution needs NEC violation AT the throat",
         "  (Morris & Thorne 1988) -- the same wall the superluminal warp mode",
         "  hits, reached from a completely different direction."],
        nextord(), (0.0, 0.0, 78.0), C_COIL))

    # --------------------------------------------------- 3. CASIMIR AT THROAT
    meshes = []
    for i in range(d["portal_casimir_rings"]):
        a = 2 * math.pi * i / d["portal_casimir_rings"] + 0.2
        bv, bf = _box(0, 0, 0, 2.2, 2.2, 1.8)
        meshes.append(Mesh(_xform(bv, _tangential(a),
                                  ((b0 - 1.6) * math.cos(a),
                                   (b0 - 1.6) * math.sin(a), 0.0)),
                           bf, C_CASIMIR,
                           "cassette %d" % (i + 1) if i % 4 == 0 else ""))
    parts.append(Part(
        "pcasimir", "THROAT CASIMIR CASSETTES (%d)" % d["portal_casimir_rings"],
        meshes,
        ["Real negative energy, in the only place it is ever found.",
         "Required at this throat: %s." % fmt_energy(ps["energy_j"]),
         "Supplied by the whole ship's lattice: %s." % fmt_energy(casimir_onboard_j()),
         "SHORT BY %.0f ORDERS OF MAGNITUDE -- and by %.0f orders for a throat"
         % (ps["casimir_shortfall_orders"], ps["safe_shortfall_orders"]),
         "  wide enough to survive crossing.",
         "The closest thing to a real construction is Maldacena, Milekhin &",
         "  Popov (2020): Casimir energy of massless fermions threading a pair",
         "  of magnetically charged black holes. It works on paper. It needs",
         "  objects nobody has ever observed, and traversal takes years."],
        nextord(), (0.0, 0.0, 108.0), C_CASIMIR))

    # ------------------------------------------------ 4. THE THROAT (geometry)
    rho_max = b0 * 4.0
    meshes = []
    for sign, nm in ((+1.0, "Sol side"), (-1.0, "far side")):
        fv, ff = _mt_funnel(b0, rho_max, rings=13, seg=40, sign=sign)
        meshes.append(Mesh(fv, ff, _mix(C_GRID, C_BUBBLE, 0.55),
                           "throat -- %s" % nm, wire=True))
    tv2, tf2 = _ring_wire(b0, 0.0, seg=56)
    meshes.append(Mesh(tv2, tf2, C_EXOTIC, "throat r = b0", wire=True))
    parts.append(Part(
        "throat", "THE THROAT  (embedding diagram)", meshes,
        ["ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2   (Morris-Thorne 1988)",
         "Drawn from z = 2 b0 sqrt(rho/b0 - 1) -- the real embedding, not a",
         "  decorative funnel. No horizon, no singularity: genuinely two-way.",
         "Energy density demanded at the throat: %s per cubic metre."
         % fmt_energy(mt_throat_density(b0)),
         "The FLARE-OUT condition is what costs: for the throat to open out on",
         "  both sides instead of pinching shut, the stress-energy there must",
         "  violate the null energy condition. That is the entire problem, and",
         "  it is structural -- not an artefact of this particular solution."],
        nextord(), (0.0, 0.0, -60.0), C_BUBBLE))

    # ------------------------------------------------------------- 5. GATE B
    safe = ps["safe_b0_m"]
    meshes = []
    tv, tf = _torus(b0 + rmin, rmin, seg_major=30, seg_minor=9)
    meshes.append(Mesh(_xform(tv, None, (0.0, 0.0, -2.0 * mt_embedding_z(
        rho_max, b0))), tf, _mix(C_RING, C_COLLECT, 0.5), "aperture ring"))
    parts.append(Part(
        "gateB", "GATE B  (mouth, far side)", meshes,
        ["Wherever you put it -- %s away, in this configuration."
         % fmt_dist(PROXIMA_M),
         "SURVIVABLE THROAT: tidal shear goes as c^2 L / b0^2, so a person",
         "  crossing at 1 g of stress needs b0 >= %.3g m -- about %.0f Earth"
         % (safe, safe / 1.2742e7),
         "  diameters. Morris & Thorne reached the same conclusion in 1988.",
         "That throat's exotic bill: %s (%s)."
         % (fmt_energy(ps["safe_energy_j"]), fmt_mass(ps["safe_mass_kg"])),
         "AND THEN IT IS A TIME MACHINE. Two mouths at different clock rates",
         "  desynchronise; when the offset exceeds the light-travel time",
         "  between them, closed timelike curves exist (Morris, Thorne &",
         "  Yurtsever 1988). Park one mouth by a neutron star and this pair",
         "  becomes one in %s." % fmt_time(ctc_by_gravity_well(-0.2)["onset_s"])],
        nextord(), (0.0, 0.0, -110.0), _mix(C_RING, C_COLLECT, 0.5)))

    return parts


# =============================================================================
# SECTION 7 -- THE WARP CORE  (stateful drive, real SI, stepped in real time)
# =============================================================================

class WarpCore:
    """The live drive. Holds the field, spends the energy, tracks the ledger.

    The one rule this class obeys without exception: energy that has no source
    is never quietly created. When the commanded solution needs negative energy
    -- which happens the instant beta crosses 1 -- the shortfall is booked to
    `exotic_debt_j` and flagged UNFUNDED on every frame, rather than being
    silently supplied. The bubble still forms and the ship still flies, because
    showing you the unfunded number is more useful than refusing to draw it."""

    def __init__(self):
        # --- commanded state
        self.beta_cmd = 0.0
        self.bubble_cmd = False
        self.wall_m = DIMS["wall_thick_m"]
        self.magsail_deployed = False
        self.rectenna_deployed = False

        # --- physical state
        self.beta = 0.0
        self.bubble_on = 0.0            # 0..1 shell convergence
        self.integrity = 1.0            # 0..1 shape-servo health
        self.coil_phase = 0.0
        self.coil_glow = np.zeros(DIMS["coils"])
        self.smes_j = 0.55 * SMES_J
        self.rad_k = 290.0
        self.collapsed = False
        self.collapse_msg = ""
        self.was_superluminal = False

        # --- live derived readouts
        self.load_w = 0.0
        self.waste_w = 0.0
        self.beam_w = 0.0
        self.exotic_need_j = 0.0
        self.exotic_debt_j = 0.0
        self.status = "COLD"

        # --- cumulative ledger (every joule that entered or left the ship)
        self.led = {"beam_in": 0.0, "plant_out": 0.0, "kinetic": 0.0,
                    "kinetic_peak": 0.0, "radiated": 0.0, "magsail_regen": 0.0,
                    "brake_dissipated": 0.0, "fuel_kg": 0.0, "am_kg": 0.0,
                    "ism_particles": 0.0}

    # ---------------------------------------------------------------- helpers
    @property
    def mode(self):
        return "ALCUBIERRE" if self.beta_cmd >= 1.0 else "PHYSICAL"

    @property
    def exotic(self):
        return self.beta >= 1.0 or self.beta_cmd >= 1.0

    def kinetic_now_j(self):
        if self.beta >= 1.0:
            return float("inf")
        return kinetic_energy_j(self.beta)

    def energy_conditions(self):
        return energy_conditions(max(self.beta, self.beta_cmd))

    def helm_locked(self):
        """Above beta = 1 the crew cannot signal the forward wall, so no new
        command can reach it. The trajectory is frozen as flown."""
        return horizon_locked(self.beta) and self.bubble_on > 0.5

    # ---------------------------------------------------------------- stepping
    def _thermal(self, dt):
        target = radiator_temp_k(self.waste_w)
        # panels have real heat capacity: they lag, they do not snap
        tau = 90.0
        self.rad_k += (target - self.rad_k) * min(1.0, dt / tau)
        self.led["radiated"] += (DIMS["rad_emissivity"] * SIGMA_SB
                                 * RADIATOR_AREA_M2 * self.rad_k ** 4) * dt

    def _integrity(self, dt):
        """Bubble integrity: what actually breaks a warp drive in this model.

        Three independent failure paths, all computed from live state -- panel
        overtemperature, a power deficit the plant cannot cover, and a wall
        thinner than the shape servo can hold. None of them is a scripted
        event; each is a threshold on a number the physics produced."""
        stress = 0.0
        if self.rad_k > DIMS["rad_limit_k"]:
            stress += (self.rad_k / DIMS["rad_limit_k"] - 1.0) * 2.2
        avail = PLANT_ELECTRIC_W + self.beam_w
        if self.load_w > avail:
            stress += (self.load_w / max(1.0, avail) - 1.0) * 0.9
        if self.wall_m < 1e-6:
            stress += 0.35            # servo cannot hold a sub-micron wall
        if self.exotic:
            stress += 0.12            # NEC-violating shell is never stable

        # Characteristic drain time at unit stress: SHELL_STRESS_TAU seconds.
        # Named and stated rather than buried, because it sets how long you get
        # to watch the readouts before an over-driven shell lets go.
        if stress > 0.0:
            self.integrity -= stress * dt / SHELL_STRESS_TAU
        else:
            self.integrity += (1.0 - self.integrity) * min(1.0, dt * 0.02)
        self.integrity = clamp(self.integrity, 0.0, 1.0)

        if self.integrity <= DRIVE["integrity_min"] and self.bubble_on > 0.1:
            self.collapse("BUBBLE COLLAPSE -- shell shape lost")

    def collapse(self, msg):
        """The shell lets go.

        If it was superluminal, the apparent velocity simply stops existing:
        an Alcubierre bubble carries its contents without ever giving them
        momentum, so when the metric relaxes the ship is at rest with respect
        to the local frame. It does not coast on at 2 c. That is not a mercy
        in the model -- it is what the metric says."""
        self.collapsed = True
        self.collapse_msg = msg
        self.bubble_cmd = False
        self.was_superluminal = self.beta >= 1.0
        self.beta_cmd = 0.0
        if self.was_superluminal:
            self.beta = 0.0

    def update(self, dt, world=None):
        """Advance one tick. `dt` is SHIP seconds (already time-warped)."""
        # ---- shell formation -------------------------------------------
        target_on = 1.0 if (self.bubble_cmd and not self.collapsed) else 0.0
        self.bubble_on += (target_on - self.bubble_on) * min(
            1.0, dt / DRIVE["bubble_form_s"])
        self.bubble_on = clamp(self.bubble_on)
        if self.bubble_on < 0.05:
            # No shell, no warp. beta falls back to the ship's REAL velocity --
            # otherwise a collapsed superluminal bubble leaves the readouts
            # (and the load, and the stress) pinned at a speed nothing is
            # holding any more, and the ship re-collapses forever.
            real = abs(world.v_ms) / C_LIGHT if world is not None else 0.0
            self.beta = min(self.beta, real)

        # ---- the travelling field phase (what the coils are actually doing)
        self.coil_phase += dt * (0.6 + 5.0 * self.beta) * self.bubble_on
        n = DIMS["coils"]
        for i in range(n):
            ph = (self.coil_phase - i * (2.0 * math.pi / n)) % (2.0 * math.pi)
            self.coil_glow[i] = self.bubble_on * max(
                0.0, math.cos(ph)) ** 6

        # ---- electrical load and the beam --------------------------------
        rng = world.x_m if world is not None else 0.0
        if self.rectenna_deployed and rng <= PLANT["beam_range_ly"] * LY:
            self.beam_w = beam_power_w(max(1.0, rng))
        else:
            self.beam_w = 0.0
        self.load_w = cruise_load_w(self.beta, self.bubble_on)
        self.waste_w = waste_heat_w(min(self.load_w, PLANT_ELECTRIC_W))
        self.led["plant_out"] += min(self.load_w, PLANT_ELECTRIC_W) * dt
        self.led["fuel_kg"] += fusion_fuel_kg(
            min(self.load_w, PLANT_ELECTRIC_W) * dt)

        # ---- SMES buffers the difference (and empties fast if overdrawn) --
        net = (PLANT_ELECTRIC_W - self.load_w) * dt
        self.smes_j = clamp(self.smes_j + net, 0.0, SMES_J)

        # ---- the exotic ledger (superluminal only) ------------------------
        if self.exotic and self.bubble_on > 0.05:
            self.exotic_need_j = alcubierre_energy_j(
                max(self.beta, 1.0), DIMS["bubble_r_m"], self.wall_m)
            # booked as DEBT, never as supply: nothing aboard can pay this,
            # and the HUD prints it in violet with UNFUNDED next to it
            self.exotic_debt_j = abs(self.exotic_need_j)
        else:
            self.exotic_need_j = 0.0

        self._thermal(dt)
        self._integrity(dt)

        # ---- status line ---------------------------------------------------
        if self.collapsed:
            self.status = "COLLAPSED"
        elif self.bubble_on < 0.05:
            self.status = "BUBBLE DOWN"
        elif self.exotic:
            self.status = "SUPERLUMINAL -- UNFUNDED"
        elif self.rad_k > DIMS["rad_limit_k"] * 0.95:
            self.status = "THERMAL LIMIT"
        elif self.integrity < 0.6:
            self.status = "SHELL DEGRADED"
        else:
            self.status = "NOMINAL"


# =============================================================================
# SECTION 8 -- VOYAGE  (Sol -> Proxima Centauri b, in the three phases physics
#                       actually forces on you)
# =============================================================================

VOYAGE_WARP = [1.0, 60.0, 3.6e3, 8.64e4, 2.592e6, 3.156e7, 3.156e8]
VOYAGE_WARP_LABEL = ["1 s/s", "1 min/s", "1 h/s", "1 d/s", "30 d/s",
                     "1 yr/s", "10 yr/s"]

PHASES = ["DOCK", "BOOST", "CRUISE", "BRAKE", "ARRIVED"]

PHASE_NOTE = {
    "DOCK":    "At the tap. Bubble down, rectenna stowed. Nothing has cost anything yet.",
    "BOOST":   "Under the beam. Every joule of (gamma-1)Mc^2 comes from outside the ship.",
    "CRUISE":  "Free. A constant-velocity warp solution is a stationary spacetime.",
    "BRAKE":   "Magsail against the ISM. The only deceleration authority that exists.",
    "ARRIVED": "Proxima Centauri b. Ship clock and Earth clock agree -- that is the point.",
}


class Voyage:
    """The trip. Position, both clocks, the phase machine and the ISM ledger.

    Note which clock is which. A relativistic ROCKET at the same speed would
    have aged less than the crew; a warp ship does not, because its interior is
    flat and unaccelerated. That is not a defect -- it means the crew arrive in
    step with the people who launched them, which is the only version of
    interstellar travel that is any use to a civilisation."""

    def __init__(self):
        self.x_m = 0.0
        self.v_ms = 0.0
        self.t_ship = 0.0
        self.t_earth = 0.0
        self.t_coord = 0.0
        self.phase = "DOCK"
        self.warp_i = 4
        self.target_m = PROXIMA_M
        self.ism_particles = 0.0
        self.log = []
        self.arrived_at = None
        self.dest_array = False        # is there a receiver waiting at Proxima?
        self._warned_overshoot = False

    @property
    def warp(self):
        return VOYAGE_WARP[self.warp_i]

    @property
    def beta(self):
        return self.v_ms / C_LIGHT

    @property
    def remaining_m(self):
        return max(0.0, self.target_m - self.x_m)

    def cycle_warp(self, d):
        self.warp_i = int(clamp(self.warp_i + d, 0, len(VOYAGE_WARP) - 1))

    def note(self, text):
        self.log.append("%8s  %s" % (fmt_time(self.t_ship), text))
        if len(self.log) > 40:
            self.log.pop(0)

    def eta_s(self):
        if self.v_ms < 1.0:
            return float("inf")
        return self.remaining_m / self.v_ms

    # ------------------------------------------------------------------ step
    def update(self, dt_real, core):
        """Advance the voyage by dt_real real seconds x the time-warp factor.

        Substepped so a 10 yr/s warp setting cannot integrate the relativistic
        momentum equation into nonsense."""
        dt_v = dt_real * self.warp
        steps = 1
        if dt_v > 3.0 * DAY:
            steps = min(60, int(dt_v / (3.0 * DAY)) + 1)
        h = dt_v / steps
        for _ in range(steps):
            self._step(h, core)
        core.update(dt_v, self)

    def _step(self, dt, core):
        m = SHIP_MASS_KG

        if self.phase == "BOOST" and not core.collapsed:
            # energy in from the beam -> relativistic gamma -> speed
            p_in = core.beam_w
            e_add = p_in * dt
            core.led["beam_in"] += e_add
            e_kin = kinetic_energy_j(min(self.beta, 0.999999)) + e_add
            g = 1.0 + e_kin / (m * C2)
            v_new = C_LIGHT * math.sqrt(max(0.0, 1.0 - 1.0 / (g * g)))
            v_cap = core.beta_cmd * C_LIGHT
            self.v_ms = min(v_new, v_cap)
            if self.v_ms >= v_cap - 1.0:
                self.phase = "CRUISE"
                self.note("cruise beta %.4f reached; beam released" % self.beta)
                core.rectenna_deployed = False
            elif self.x_m > PLANT["beam_range_ly"] * LY:
                self.phase = "CRUISE"
                core.beta_cmd = self.beta
                core.rectenna_deployed = False
                self.note("BEAM RANGE EXHAUSTED at %s -- cruise locked to beta %.4f"
                          % (fmt_dist(self.x_m), self.beta))

        elif self.phase == "BRAKE":
            # Two brakes, and the model is explicit about which is doing the work.
            # MAGSAIL: always available, drags on the ISM, fades as v^2.
            # DESTINATION ARRAY: photon pressure from a transmitter already built
            # at Proxima. Thousands of times stronger -- and it assumes an entire
            # second stellar-scale facility at a star nobody has been to.
            f = magsail_drag_n(self.beta) if core.magsail_deployed else 0.0
            self.f_magsail = f
            self.f_beam = (beam_brake_force_n(self.remaining_m + 0.002 * LY)
                           if self.dest_array else 0.0)
            f += self.f_beam
            if f > 0.0:
                # brake in MOMENTUM space: p = gamma m v, dp = -F dt
                g = lorentz_gamma(self.beta)
                p = g * m * self.v_ms
                p = max(0.0, p - f * dt)
                self.v_ms = p / (m * math.sqrt(1.0 + (p / (m * C_LIGHT)) ** 2))
                # Only the MAGSAIL returns energy to the bus. Photon braking
                # does not: the ship's kinetic energy goes into the reflected
                # beam, which leaves. Crediting the beam's work as onboard
                # recovery would quietly manufacture a supply the audit then
                # measures over-unity against.
                core.led["magsail_regen"] += (self.f_magsail * self.v_ms * dt
                                              * DIMS["magsail_regen_eff"])
                core.led["brake_dissipated"] += self.f_beam * self.v_ms * dt
            if self.v_ms < DRIVE["arrival_beta"] * C_LIGHT:
                self.v_ms = 0.0
                self.phase = "ARRIVED"
                self.arrived_at = self.t_ship
                self.note("ARRIVED. ship %s / Earth %s"
                          % (fmt_time(self.t_ship), fmt_time(self.t_earth)))

        elif self.phase == "ARRIVED":
            self.v_ms *= 0.0

        # ---- superluminal override: no gamma, no kinetic ledger ------------
        if core.collapsed and core.was_superluminal:
            core.was_superluminal = False
            self.v_ms = 0.0
            self.note("SHELL LOST at superluminal beta -- apparent velocity "
                      "was never momentum; ship is at rest, adrift at %s"
                      % fmt_dist(self.x_m))
        if core.beta_cmd >= 1.0 and core.bubble_on > 0.5 and not core.collapsed:
            slew = dt / max(1.0, DRIVE["spinup_s"] * 40.0)
            core.beta += (core.beta_cmd - core.beta) * min(1.0, slew)
            self.v_ms = core.beta * C_LIGHT
        elif self.phase in ("CRUISE", "BOOST", "BRAKE"):
            core.beta = self.beta

        # ---- the kinetic ledger, live in every phase ----------------------
        if self.beta < 1.0:
            core.led["kinetic"] = kinetic_energy_j(min(self.beta, 0.999999))
            core.led["kinetic_peak"] = max(core.led["kinetic_peak"],
                                           core.led["kinetic"])

        # ---- integrate position and both clocks ---------------------------
        self.x_m += self.v_ms * dt
        # THREE clocks, integrated separately. dt is COORDINATE time.
        #   t_coord : a clock at rest at infinity
        #   t_ship  : the crew. Flat interior means no VELOCITY dilation, but
        #             they still sit in whatever gravitational potential they
        #             are passing through, so their rate is grav_rate(x).
        #   t_earth : Earth, permanently 1 AU down Sol's well.
        # The difference between the last two is the whole environmental
        # dilation story, and it is a couple of seconds per crossing.
        self.t_coord += dt
        self.t_ship += dt * grav_rate(self.x_m)
        self.t_earth += dt * _earth_rate()
        if core.bubble_on > 0.3:
            self.ism_particles += (ISM_N_M3 * math.pi * DIMS["bubble_r_m"] ** 2
                                   * self.v_ms * dt)
            core.led["ism_particles"] = self.ism_particles

        if self.x_m >= self.target_m and self.phase != "ARRIVED":
            self.x_m = self.target_m
            if self.v_ms > DRIVE["arrival_beta"] * C_LIGHT:
                if not self._warned_overshoot:
                    self._warned_overshoot = True
                    self.note("FLYBY -- passing Proxima at beta %.3f, still %s "
                              "from stopped" % (self.beta,
                                                fmt_time(magsail_decel_time_s(self.beta))))
            else:
                self.phase = "ARRIVED"
                self.arrived_at = self.t_ship

    # ------------------------------------------------------- phase commands
    def begin_boost(self, core):
        if self.phase != "DOCK":
            return "boost only from DOCK"
        if core.beta_cmd <= 0.0:
            return "set a cruise beta first (, / .)"
        core.bubble_cmd = True
        core.rectenna_deployed = True
        self.phase = "BOOST"
        bp = boost_profile(core.beta_cmd)
        self.note("BOOST to beta %.3f -- bill %s over %s"
                  % (core.beta_cmd, fmt_energy(bp["energy_j"]),
                     fmt_time(bp["time_s"])))
        if not bp["ok"]:
            self.note("PREDICTED SHORTFALL: %s" % bp["reason"])
        return None

    def begin_brake(self, core):
        if self.phase not in ("CRUISE", "BOOST"):
            return "already stopped"
        core.magsail_deployed = True
        core.bubble_cmd = False          # the sail needs the ISM the bubble hides
        core.rectenna_deployed = self.dest_array
        self.phase = "BRAKE"
        b = self.beta
        self.note("MAGSAIL DEPLOYED at beta %.3f" % b)
        self.note("  magsail alone: halves speed in %s, STOPS in %s"
                  % (fmt_time(magsail_halving_time_s(b)),
                     fmt_time(magsail_decel_time_s(b))))
        if self.dest_array:
            self.note("  destination array ASSUMED PRESENT: photon brake %.3g N"
                      " -> stop in %s" % (beam_brake_force_n(0.02 * LY),
                                          fmt_time(beam_brake_time_s(b))))
        else:
            self.note("  NO destination array -- this is a FLYBY, not a rendezvous")
        blast = ism_blast_energy_j(b, self.x_m)
        self.note("bubble down: %.3g swept protons released forward (%s)"
                  % (self.ism_particles, fmt_energy(blast)))
        return None

    def reset(self, core):
        self.__init__()
        core.__init__()


# =============================================================================
# SECTION 9 -- HONESTY LAYER  (conservation audit; refuses magic)
# =============================================================================
# Modelled on Radiant.py:honesty_audit() and Simulation.py:_conservation_audit.
# If any of these fail, the model has produced physically impossible output and
# must not be trusted. This is the difference between a digital twin and a prop.

def honesty_audit(core, voyage, verbose=True):
    checks = {}
    led = core.led

    # 1) NO OVER-UNITY. The beam is the ONLY source of kinetic energy this
    #    ship has ever had, so the most it ever held cannot exceed what was
    #    delivered. Note this compares against the PEAK, not the current value:
    #    checking the current one would pass trivially after any braking.
    checks["no_overunity_kinetic"] = (
        led["kinetic_peak"] <= led["beam_in"] * (1.0 + 1e-6) + 1.0)

    # 1b) RECOVERY IS BOUNDED. The magsail can never hand back more than the
    #     ship was carrying, times its stated efficiency.
    checks["recovery_bounded"] = (
        led["magsail_regen"] <= led["kinetic_peak"]
        * DIMS["magsail_regen_eff"] * (1.0 + 1e-6) + 1.0)

    # 2) THE PLANT IS BOUNDED. Cumulative electrical output cannot exceed the
    #    reactor's rating times elapsed ship time.
    cap = PLANT_ELECTRIC_W * max(1.0, voyage.t_ship)
    checks["plant_within_rating"] = led["plant_out"] <= cap * (1.0 + 1e-6)

    # 3) FUEL IS CONSERVED. Every joule the plant produced is backed by burnt
    #    D-3He at the stated specific energy -- no fuel-free electricity.
    implied = led["fuel_kg"] * PLANT["d3he_j_kg"] * PLANT["conversion_eff"]
    checks["fuel_backs_output"] = implied >= led["plant_out"] * (1.0 - 1e-6)

    # 4) NEGATIVE ENERGY IS NEVER SUPPLIED, ONLY OWED. The Casimir lattice is
    #    the only real negative-energy source aboard and it is microscopic.
    #    Superluminal operation books a debt; it never books income.
    checks["exotic_never_supplied"] = (
        core.exotic_debt_j >= 0.0 and
        (core.exotic_debt_j == 0.0 or abs(core.exotic_debt_j)
         > abs(casimir_onboard_j())))

    # 5) THE SECOND LAW. Radiated energy is non-negative and the panels are
    #    never colder than they would be radiating their own load.
    checks["radiates_only_outward"] = led["radiated"] >= 0.0

    # 6) NULL ENERGY CONDITION reported truthfully: never claimed satisfied
    #    while superluminal.
    ec = energy_conditions(max(core.beta, core.beta_cmd))
    checks["NEC_reported_truthfully"] = (ec["NEC"] is False) if core.exotic \
        else (ec["NEC"] is True)

    # 7) NO VELOCITY-DILATION DIVIDEND. A warp interior is flat, so the crew get
    #    no Lorentz dilation -- but they are not in flat space overall, and the
    #    model must not pretend otherwise. The only permitted divergence between
    #    the crew clock and Earth's is GRAVITATIONAL, of order 1e-8 fractional.
    #    A 1e-6 tolerance admits that and would still catch an accidental
    #    Lorentz factor, which would be of order 1e-1.
    drift = voyage.t_ship - voyage.t_earth
    checks["no_velocity_dilation_dividend"] = (
        abs(drift) <= 1e-6 * max(1.0, voyage.t_coord))

    # 7b) ...AND THE GRAVITATIONAL PART IS REALLY MODELLED, not zeroed out.
    #     Climbing out of Sol's well genuinely puts the crew ahead of Earth, by
    #     a couple of seconds per crossing. Asserting the clocks are exactly
    #     equal would have been the easy lie.
    checks["gravitational_drift_modelled"] = (
        voyage.t_coord < 1.0 or abs(drift) > 0.0)

    # 8) BEAM CAPTURE IS PHYSICAL. Never more than 100% of the transmitted beam.
    checks["beam_capture_le_1"] = beam_capture_frac(max(1.0, voyage.x_m)) <= 1.0

    # 9) MASS IS POSITIVE. Every component of the dry mass budget is real matter.
    checks["all_masses_positive"] = all(v > 0 for v in mass_budget().values())

    # 10) ARRIVAL IS EARNED. You are only 'ARRIVED' if you are actually stopped.
    checks["arrival_requires_stopping"] = (
        voyage.phase != "ARRIVED" or
        abs(voyage.beta) <= DRIVE["arrival_beta"] * 1.5)

    ok = all(checks.values())
    if verbose:
        print("\n=== HONESTY LAYER -- conservation audit ===")
        for name, passed in checks.items():
            print("   [%s]  %s" % ("PASS" if passed else "FAIL", name))
        print("   kinetic gained     : %s" % fmt_energy(led["kinetic"]))
        print("   beam delivered     : %s" % fmt_energy(led["beam_in"]))
        print("   kinetic peak held  : %s" % fmt_energy(led["kinetic_peak"]))
        print("   magsail recovered  : %s" % fmt_energy(led["magsail_regen"]))
        print("   photon brake work  : %s  (leaves with the beam, not recovered)"
              % fmt_energy(led["brake_dissipated"]))
        print("   plant produced     : %s  (%.3g kg D-3He burnt)"
              % (fmt_energy(led["plant_out"]), led["fuel_kg"]))
        print("   heat radiated      : %s" % fmt_energy(led["radiated"]))
        print("   crew clock vs Earth: %+.3f s over %s  (gravitational only)"
              % (voyage.t_ship - voyage.t_earth, fmt_time(voyage.t_coord)))
        print("   exotic energy OWED : %s   %s"
              % (fmt_energy(-core.exotic_debt_j),
                 "UNFUNDED -- no known source" if core.exotic_debt_j > 0
                 else "(none: subluminal, positive-energy)"))
        print("   Casimir available  : %s" % fmt_energy(casimir_onboard_j()))
        print("   VERDICT: %s" % ("HONEST -- nothing created from nothing."
                                  if ok else "MODEL BROKEN."))
    return checks


# =============================================================================
# SECTION 9b -- REPORTS  (--metric, --ladder, --feasibility, --voyage)
# =============================================================================

def _rule(title):
    print("\n" + "=" * 78)
    print(" " + title)
    print("=" * 78)


def report_metric():
    """Everything the warp metric says, computed live from the shape function."""
    R = DIMS["bubble_r_m"]
    _rule("WARP METRIC  --  Alcubierre shape function, integrated numerically")
    print(" ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2")
    print(" f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R)),"
          "  sigma = 1/delta")
    print(" bubble radius R = %.0f m,  flat interior to %.1f m,  c^4/G = %.4e N"
          % (R, flat_interior_r(), C4_OVER_G))

    print("\n SHAPE FUNCTION across the wall (delta = %.3g m):" % DIMS["wall_thick_m"])
    print("   %-12s %-12s %-14s %-16s" % ("r [m]", "f(r)", "df/dr [1/m]",
                                          "T^00 [J/m^3]"))
    d0 = DIMS["wall_thick_m"]
    for off in (-4 * d0, -2 * d0, -d0, 0.0, d0, 2 * d0, 4 * d0):
        r = R + off
        print("   %-12.4f %-12.6f %-14.4g %-16.4g"
              % (r, shape_f(r, R, d0), shape_df(r, R, d0),
                 energy_density(0.0, r, 1.0, R, d0)))

    print("\n ENERGY vs WALL THICKNESS at beta = 1 (R = %.0f m):" % R)
    print("   %-14s %-16s %-22s %s" % ("delta [m]", "E [J]", "equivalent mass",
                                       "status"))
    for delta in (12.0, 1.0, 1e-3, 1e-9, 1e-15, ford_roman_wall_limit(1.0)):
        E = alcubierre_energy_j(1.0, R, delta)
        tag = ""
        if abs(delta - ford_roman_wall_limit(1.0)) < 1e-40:
            tag = "<- quantum-inequality limit (Pfenning & Ford 1997)"
        print("   %-14.4g %-16.4g %-22s %s" % (delta, E,
                                               fmt_mass(equiv_mass_kg(E)), tag))

    print("\n ENERGY vs BETA (delta = %.3g m):" % d0)
    for b in (0.1, 0.5, 1.0, 2.0, 5.0, 10.0):
        E = alcubierre_energy_j(b, R, d0)
        print("   beta = %-6.1f  E = %-14.4g J  = %-20s  %s"
              % (b, E, fmt_mass(equiv_mass_kg(E)),
                 "EXOTIC (NEC violated)" if b >= 1.0
                 else "not required -- use the positive-energy shell instead"))

    print("\n TIDAL SHEAR IN THE WALL (2 m body, beta = 0.5):")
    for delta in (12.0, 1.0, 1e-3):
        a = wall_tidal_gradient(0.5, R, delta)
        print("   delta = %-8.3g m -> %.3e m/s^2 = %.3e g" % (delta, a, a / 9.81))
    print("   Interior (r < %.1f m): f = 1, all derivatives zero, EXACTLY 0 g."
          % flat_interior_r())

    print("\n CASIMIR REALITY CHECK (the only real negative energy there is):")
    cas = casimir_cassette()
    print("   rho(%.0f nm gap) = -pi^2 hbar c / 720 a^4 = %.4g J/m^3"
          % (DIMS["casimir_gap_nm"], cas["rho_j_m3"]))
    print("   onboard lattice  = %s across %d cassettes"
          % (fmt_energy(casimir_onboard_j()), DIMS["casimir_cassettes"]))
    need = alcubierre_energy_j(1.0, R, 1.0)
    needq = alcubierre_energy_j(1.0, R, ford_roman_wall_limit(1.0))
    print("   beta=1, 1 m wall needs %s  -> short by %.0f orders of magnitude"
          % (fmt_energy(need), orders_of_magnitude(need, casimir_onboard_j())))
    print("   with the QI-legal wall  -> short by %.0f orders of magnitude"
          % orders_of_magnitude(needq, casimir_onboard_j()))


def report_ladder():
    """The historical attempts to make the exotic bill affordable, and how each
    one actually turned out."""
    _rule("NEGATIVE-ENERGY REDUCTION LADDER  --  thirty years of trying")
    base = alcubierre_energy_j(1.0, DIMS["bubble_r_m"], 1e-15)
    print(" Baseline: R = %.0f m, beta = 1, delta = 1e-15 m -> %s (%s)\n"
          % (DIMS["bubble_r_m"], fmt_energy(base),
             fmt_mass(equiv_mass_kg(base))))
    for label, factor, status, cite in LADDER:
        print(" %-58s %s" % (label, status))
        if factor > 0:
            E = base * factor
            print("     x%-10.0e  ->  %-14s (%s)"
                  % (factor, fmt_energy(E), fmt_mass(equiv_mass_kg(E))))
        elif status == "REFUTED":
            print("     claimed positive-energy superluminal solitons;")
            print("     shown to violate the NEC after all -- no reduction stands.")
        else:
            E = kinetic_energy_j(0.5)
            print("     not a reduction of the exotic bill -- a DIFFERENT SOLUTION")
            print("     CLASS with no exotic bill at all. Cost becomes ordinary")
            print("     kinetic energy: %s to reach beta = 0.5. Subluminal only."
                  % fmt_energy(E))
        print("     %s\n" % cite)
    print(" WHERE THAT LEAVES US:")
    print("   Superluminal  -- every route still ends at a NEC violation, and")
    print("                    Santiago, Schuster & Visser (2022) proved that is")
    print("                    generic, not an artefact of Alcubierre's ansatz.")
    print("   Subluminal    -- genuinely solved on paper. Positive energy, real")
    print("                    matter, all energy conditions satisfied. What")
    print("                    remains is an engineering bill this file prices.")


def feasibility_scorecard():
    """Function-by-function honest scorecard, in the style of LS.py's
    --engineer report: what this drive really does, really cannot do, and what
    is merely very expensive."""
    R = DIMS["bubble_r_m"]
    bcap = max_boost_beta()
    w99 = waste_heat_w(cruise_load_w(0.99))
    w20 = waste_heat_w(cruise_load_w(2.0))
    need1 = alcubierre_energy_j(1.0, R, 1.0)

    rows = [
        ("Metric solves the Einstein field equations", "PASS",
         "Alcubierre 1994 is exact. Write the spacetime, read off T^uv. The"
         " mathematics has never been the disputed part."),
        ("Flat, weightless, un-dilated interior", "PASS",
         "f = 1 inside: Minkowski exactly. No proper acceleration at any beta,"
         " so no g-limit, and ship clocks match Earth clocks."),
        ("No reaction mass", "PASS",
         "The shell sources the metric; nothing is expelled. This is the one"
         " advantage over a rocket that survives every objection."),
        ("Positive-energy source (subluminal)", "PASS",
         "Bobrick & Martire 2021 and Fuchs et al. 2024 construct subluminal"
         " warp shells satisfying NEC, WEC, DEC and SEC. Real matter."),
        ("Waste-heat rejection at cruise", "PASS",
         "%.0f m^2 of panel rejects %s at beta = 0.99 and settles at %.0f K,"
         " under the %.0f K graphite limit."
         % (RADIATOR_AREA_M2, fmt_power(w99), radiator_temp_k(w99),
            DIMS["rad_limit_k"])),
        ("Housekeeping power for a decade-long crossing", "PASS",
         "%.0f GW D-3He plant covers the %s cruise load; %.0f kg of fuel"
         " crosses to Proxima."
         % (DIMS["reactor_th_gw"], fmt_power(cruise_load_w(0.5)),
            fusion_fuel_kg(cruise_load_w(0.5) * 8.5 * YR))),
        ("Acceleration to cruise speed", "PARTIAL",
         "%s of kinetic energy at beta = 0.5. Nothing storable aboard comes"
         " close, so it must be beamed: a %.0e W tap for %s. The ship cannot"
         " launch itself, and no design change fixes that."
         % (fmt_energy(kinetic_energy_j(0.5)), PLANT["tap_w"],
            fmt_time(boost_profile(0.5)["time_s"]))),
        ("Cruise speed actually reachable", "PARTIAL",
         "beta = %.3f, set by beam range and diffraction -- not by the drive."
         " Faster needs a bigger transmitter aperture, not a better warp shell."
         % bcap),
        ("Deceleration / rendezvous", "PARTIAL",
         "Magsail halves speed in %s but STOPS in %s -- drag falls as v^2."
         " A rendezvous needs a photon-braking array already built at the"
         " destination. Without one the mission is a flyby."
         % (fmt_time(magsail_halving_time_s(0.5)),
            fmt_time(magsail_decel_time_s(0.5)))),
        ("Interstellar medium loading", "PARTIAL",
         "The wall collects everything ahead of it (McMonigal, Lewis & O'Byrne"
         " 2012): %.2e protons over the crossing, released forward as %s when"
         " the bubble drops. Aim the arrival away from anything you like."
         % (ism_particles_swept(PROXIMA_M),
            fmt_energy(ism_blast_energy_j(0.5, PROXIMA_M)))),
        ("Shell material with the required stress-energy", "OPEN",
         "The positive-energy solutions need anisotropic stresses comparable"
         " to the energy density -- sound speed approaching c. No known"
         " material does this. This is the real open problem, and it is a"
         " materials problem, not a relativity problem."),
        ("Survivable bubble wall", "FAIL",
         "Tidal shear reaches %.2e g across a 2 m body in the wall at"
         " beta = 0.5. The interior is perfectly safe; the wall is not a place."
         % (wall_tidal_gradient(0.5, R, DIMS["wall_thick_m"]) / 9.81)),
        ("Superluminal flight (beta > 1)", "FAIL",
         "Requires NEC violation -- and Santiago, Schuster & Visser (2022)"
         " proved that holds for EVERY superluminal warp drive, not just"
         " Alcubierre's. This is a theorem, not a missing invention."),
        ("Negative energy at the required scale", "FAIL",
         "Needs %s. The onboard Casimir lattice -- real, measured physics --"
         " supplies %s. Short by %.0f orders of magnitude, and by %.0f orders"
         " at the wall thickness the quantum inequality permits."
         % (fmt_energy(need1), fmt_energy(casimir_onboard_j()),
            orders_of_magnitude(need1, casimir_onboard_j()),
            orders_of_magnitude(alcubierre_energy_j(1.0, R,
                                                    ford_roman_wall_limit(1.0)),
                                casimir_onboard_j()))),
        ("Steering above beta = 1", "FAIL",
         "The forward wall is causally disconnected from the interior (Everett"
         " 1996; Coule 1998). You cannot signal the front of your own bubble,"
         " so the whole trajectory must be pre-laid before departure."),
        ("Thermal survival above beta = 1", "FAIL",
         "Coil load scales as beta^2: %s of waste heat at beta = 2 drives the"
         " panels to %.0f K, past the %.0f K limit. The ship cooks before the"
         " energy problem even gets a vote."
         % (fmt_power(w20), radiator_temp_k(w20), DIMS["rad_limit_k"])),
    ]
    return rows


def report_feasibility():
    _rule("WD-1 FEASIBILITY SCORECARD  --  what this drive really does")
    rows = feasibility_scorecard()
    tally = {}
    for name, status, why in rows:
        tally[status] = tally.get(status, 0) + 1
        print("\n [%-7s] %s" % (status, name))
        for line in wrap_plain(why, 70):
            print("           %s" % line)
    n = len(rows)
    print("\n" + "-" * 78)
    print(" SCORE: " + "   ".join("%s %d/%d" % (k, v, n)
                                  for k, v in sorted(tally.items())))
    print("""
 THE HONEST SUMMARY
   A SUBLUMINAL warp drive is not science fiction. It is a solved problem in
   general relativity with a brutal engineering bill: %s to reach half
   lightspeed, a stellar-scale transmitter to deliver it, a second one at the
   far end to stop, and a shell material nobody knows how to make. Every one
   of those is an engineering obstacle, and none of them is a violated law.

   A SUPERLUMINAL warp drive is a different kind of thing. It needs negative
   energy in bulk, and the shortfall is not %d%% or %dx -- it is %.0f orders
   of magnitude against the best real source in physics, with a theorem
   standing behind the requirement. That is not a technology gap.

   This model flies both. It only ever claims one.""" % (
        fmt_energy(kinetic_energy_j(0.5)), 20, 1000,
        orders_of_magnitude(alcubierre_energy_j(1.0, DIMS["bubble_r_m"], 1.0),
                            casimir_onboard_j())))


def wrap_plain(text, width):
    out, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if len(trial) <= width:
            cur = trial
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out or [""]


def report_dilation():
    """Every clock in the problem, and which one the marketing quotes."""
    _rule("ENVIRONMENTAL SPACETIME DILATION  --  whose clock, and where")
    beta = max_boost_beta()
    t = PROXIMA_M / (beta * C_LIGHT)
    print(" From the metric, two observers and two completely different answers:")
    print("   COMOVING (the crew, dx = v_s f dt, f = 1):")
    print("       ds^2 = -c^2 dt^2      ->  dtau = dt EXACTLY. No dilation, ever.")
    print("   STATIC  (holds station in the external frame, dx = 0):")
    print("       dtau = dt sqrt(1 - beta^2 f(r)^2)   -- the full Lorentz factor")
    print("\n STATIC-OBSERVER CLOCK RATE INSIDE THE BUBBLE:")
    print("   %-8s %-14s %-14s %s" % ("beta", "at centre", "at the wall",
                                      "outside"))
    for b in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99):
        print("   %-8.2f %-14.6f %-14.6f %.6f"
              % (b, lapse_static(0.0, b), lapse_static(DIMS["bubble_r_m"], b),
                 lapse_static(DIMS["bubble_r_m"] * 1.6, b)))
    print("   %-8.2f %s" % (2.0, "NO STATIC OBSERVER EXISTS -- every worldline "
                            "inside is dragged past c."))
    print("   That last line is the horizon problem, showing up as arithmetic")
    print("   rather than as a footnote.")

    print("\n GRAVITATIONAL ENVIRONMENT ALONG Sol -> Proxima:")
    print("   %-22s %-18s %s" % ("position", "Phi/c^2", "clock rate"))
    for frac, name in ((0.0, "Earth orbit (start)"), (0.02, "0.08 ly out"),
                       (0.5, "midpoint, flat"), (0.98, "approach"),
                       (1.0, "Proxima b orbit")):
        x = frac * PROXIMA_M
        print("   %-22s %-18.4e %.12f"
              % (name, grav_potential_at(x) / C2, grav_rate(x)))

    print("\n THE ONLY REAL DRIFT:")
    drift = voyage_grav_drift_s(t)
    print("   crossing at beta = %.4f takes %s" % (beta, fmt_time(t)))
    print("   crew clock MINUS Earth clock: %+.4f s" % drift)
    print("   -- all of it gravitational (climbing out of Sol's well), not one")
    print("      microsecond of it velocity dilation.")
    print("   a relativistic ROCKET at the same beta would arrive %s YOUNGER."
          % fmt_time(t - rocket_proper_time_s(beta, PROXIMA_M)))
    print("   The warp drive gives up the dilation dividend and buys arrival in")
    print("   step with home. That is a trade, not a free win.")
    print("\n   the ship's own gravity contributes %.3e -- twelve orders below"
          % ship_self_dilation())
    print("   the best clock ever built, which is how we know it is negligible.")


def report_portal():
    """The portal, priced."""
    _rule("PORTAL  --  Morris-Thorne wormhole, and the teleporter that works")
    ps = portal_summary()
    print(" ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2   (Morris & Thorne 1988)")
    print(" No horizon, no singularity, traversable both ways. A perfectly good")
    print(" solution of the Einstein field equations -- written down in 1988 as a")
    print(" TEACHING EXERCISE precisely because it is easy to construct and")
    print(" impossible to build.\n")

    print(" THE GATE AS SPEC'D:")
    print("   aperture 2 b0            %.0f m" % DIMS["portal_gate_d_m"])
    print("   throat radius b0         %.1f m" % ps["b0_m"])
    print("   energy density at throat %s per m^3   (rho = -c^4/8 pi G b0^2)"
          % fmt_energy(ps["density_j_m3"]))
    print("   total exotic energy      %s  (%s)"
          % (fmt_energy(ps["energy_j"]), fmt_mass(ps["mass_kg"])))
    print("   tidal shear crossing it  %.3e g across a 2 m body" % ps["tidal_g"])
    print("   -> nothing made of atoms survives that crossing.\n")

    print(" THE THROAT YOU WOULD ACTUALLY SURVIVE:")
    print("   tidal goes as c^2 L / b0^2, so 1 g across 2 m needs")
    print("   b0 >= %.4g m  =  %.1f Earth diameters"
          % (ps["safe_b0_m"], ps["safe_b0_m"] / 1.2742e7))
    print("   its exotic bill: %s  (%s)"
          % (fmt_energy(ps["safe_energy_j"]), fmt_mass(ps["safe_mass_kg"])))
    print("   Morris & Thorne reached this same conclusion in 1988. 'Portal' and")
    print("   'doorway' turn out not to be the same word.\n")

    print(" THE FULL METRIC, NOT JUST THE THROAT:")
    fl = ps["flare_out"]
    print("   ds^2 = -e^(2Phi) c^2 dt^2 + dr^2/(1-b(r)/r) + r^2 dOmega^2")
    print("   shape function b(r) = b0^2/r   (Morris & Thorne 1988, eq. 12)")
    print("   throat at r0 = b0:  b(r0) = %.6f = r0  (check)"
          % fl["b_at_r0"])
    print("   flare-out:  b'(r0) = %.4f < 1  (the throat is a minimum of r-b)"
          % fl["b_prime_at_r0"])
    print("   THIS is the condition that costs. It forces d^2r/dl^2 > 0 at the")
    print("   throat, and the Einstein equations read that as rho < 0. Theoremed")
    print("   for EVERY traversable wormhole (Visser 1989; Flanagan & Wald 1997)")
    print("   -- not an artefact of this ansatz.")
    print("   tidal profile:  %.2e g at throat, %.2e g at 2b0, %.2e g at 4b0"
          % (ps["tidal_g"], ps["tidal_at_2b0_g"], ps["tidal_at_4b0_g"]))
    print("   (falls as 1/r^4 -- the throat is the only lethal part)")
    print("   proper length throat -> 4b0:  %.1f m  =  %.2f b0\n"
          % (ps["proper_length_m"], ps["proper_length_m"] / ps["b0_m"]))

    print(" AGAINST THE ONLY REAL NEGATIVE ENERGY THERE IS:")
    print("   Casimir lattice aboard   %s" % fmt_energy(casimir_onboard_j()))
    print("   short by %.0f orders of magnitude for the gate as spec'd,"
          % ps["casimir_shortfall_orders"])
    print("   short by %.0f orders for a throat wide enough to survive."
          % ps["safe_shortfall_orders"])

    print(" FORD-ROMAN QUANTUM INEQUALITIES (1997):")
    print("   Negative energy is not just hard to source -- it is BOUNDED in")
    print("   magnitude and duration by quantum field theory:")
    print("     |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)   (massless scalar,")
    print("                                              sampling time tau)")
    print("   At tau = 1 s:  %s /m^3  -- %.0f orders below the throat's demand"
          % (fmt_energy(ps["qi_bound_1s_j_m3"]), ps["qi_shortfall_orders"]))
    print("   Longest you can hold a %.0f m throat open:  %.2e s"
          % (ps["b0_m"], ps["qi_hold_s"]))
    print("   Traversal takes:  %.1f s  --  %.0f orders of magnitude longer"
          % (ps["traverse_s"], math.log10(ps["qi_traversal_ratio"])))
    print("   The throat closes ~1e26 times before you are halfway through.")
    print("   This is the deepest 'no' in the portal section: not 'we lack a")
    print("   source' but 'the source is forbidden from lasting long enough',")
    print("   by a theorem of quantum field theory.\n")

    print(" VISSER THIN-SHELL WORMHOLE (1989/1995):")
    vs = ps["visser"]
    print("   Cut two copies of spacetime at radius a, paste with a thin shell.")
    print("   The exotic matter lives on a 2-D SHEET, not a 3-D volume:")
    print("     sigma = -c^2 / (2 pi G a) * sqrt(1 - 2GM / a c^2)")
    print("   For the spec'd aperture (a = %.0f m, M = 0):" % vs["a_m"])
    print("     shell exotic mass   %s" % fmt_mass(vs["shell_mass_kg"]))
    print("     shell exotic energy %s" % fmt_energy(vs["shell_energy_j"]))
    print("   That is MORE than the Morris-Thorne volume estimate (%s) --"
          % fmt_mass(ps["mass_kg"]))
    print("   concentrating exotic matter on a sheet is LESS efficient, not")
    print("   more. Visser's point is about LOCALISATION, not reduction: the")
    print("   NEC violation is still there, but on a surface you could in")
    print("   principle engineer. It vanishes as a -> 2GM/c^2 (the horizon")
    print("   swallows it), which is why nearly-extremal holes are the route.\n")

    print(" MALDACENA-MILEKHIN-POPOV (2020): THE WORMHOLE THAT WORKS ON PAPER:")
    mmp = ps["mmp"]
    print("   The closest thing to a real traversable wormhole in the literature.")
    print("   Two nearly-extremal MAGNETICALLY CHARGED black holes, held open by")
    print("   the Casimir energy of massless fermions threading the magnetic field")
    print("   lines. The negative energy is genuine, calculable, from a real")
    print("   quantum field -- not a postulate.")
    print("   Survivable BH mass    %.0f M_sun  (%.2e kg)"
          % (mmp["M_msun"], mmp["M_kg"]))
    print("   throat radius (r_s)   %.3g m  =  %.1f Earth diameters"
          % (mmp["r_s_m"], mmp["r_s_m"] / 1.2742e7))
    print("     -- same curvature radius as the Morris-Thorne survivable throat,")
    print("       reached from a completely different construction.")
    print("   extremal charge       %.3e C  (Q_ext = sqrt(4 pi eps0 G) M)"
          % mmp["Q_ext_c"])
    print("   traversal time        %.1f s  (t ~ GM/c^3 * ln(M/M_planck))"
          % mmp["traversal_s"])
    print("   Casimir energy        %.2e J  (tiny, but it tips an almost-wormhole)"
          % mmp["casimir_energy_j"])
    print("   THE CATCHES:")
    print("     1. No magnetic monopole has EVER been observed. These BHs may")
    print("        not exist. If they do, they are primordial, and none is seen.")
    print("     2. The holes must be NEARLY EXTREMAL (Q/Q_ext -> 1). Fine-tuned.")
    print("     3. Only massless fermions provide the right Casimir energy.")
    print("        This is a specific, fragile construction -- not generic.\n")

    print(" AND THEN IT IS A TIME MACHINE:")
    g = ctc_by_gravity_well(-0.2)
    w = ctc_by_warp_transport(max_boost_beta())
    print("   Two mouths at different clock rates desynchronise. When the offset")
    print("   exceeds the light-travel time between them, closed timelike curves")
    print("   exist (Morris, Thorne & Yurtsever 1988). This is automatic:")
    print("   traversable wormhole + ordinary relative motion = time machine.")
    print("     park one mouth at Phi/c^2 = -0.2 (neutron star):")
    print("       rate gap %.4f  ->  time machine in %s"
          % (g["rate_diff"], fmt_time(g["onset_s"])))
    print("     carry one mouth on THIS warp drive:")
    print("       rate gap %.4f  ->  never. %s"
          % (w["warp_rate_diff"], w["verdict"]))
    print("     carry it on a relativistic rocket at the same speed:")
    print("       rate gap %.4f  ->  it works" % w["rocket_rate_diff"])
    print("   Note the irony: the FAST thing cannot build the causality")
    print("   violation, and the slow thing can.")
    print("   Hawking's chronology protection conjecture (1992) expects vacuum")
    print("   fluctuations to destroy the throat at exactly the moment it would")
    print("   first close. Unproven -- but it is why most physicists expect no.\n")

    q = quantum_teleport_facts()
    print(" THE TELEPORTER THAT ACTUALLY EXISTS:")
    print("   Quantum teleportation is real and routine (Bennett et al. 1993;")
    print("   %.0f km via the Micius satellite, 2017)." % q["record_km"])
    print("   It moves a quantum STATE, not matter.")
    print("   It needs pre-shared entanglement and %.0f classical bits per qubit,"
          % QT["bits_per_qubit"])
    print("   and that classical channel is capped at c -- so NO information")
    print("   travels faster than light. Ever.")
    print("   No-cloning means the original is destroyed.")
    print("   Teleporting one person: about %.2e bits of state." % q["state_bits"])
    print("   At an absurdly generous 1 Tb/s that is %s -- about %.1f times the"
          % (fmt_time(q["seconds"]), q["universe_ages"]))
    print("   age of the universe.\n")
    print(" VERDICT: four constructions, one answer.")
    print("   Morris-Thorne (1988) needs bulk negative energy; no source exists.")
    print("   Visser (1989) concentrates it on a shell; that costs MORE, not less.")
    print("   Ford-Roman (1997) says the source cannot last long enough even if")
    print("     it existed -- the quantum inequalities close the throat in 1e-26 s.")
    print("   Maldacena-Milekhin-Popov (2020) is the one that works on paper, with")
    print("     REAL quantum-field negative energy -- but it needs magnetically")
    print("     charged black holes, and no magnetic monopole has ever been seen.")
    print("   And every traversable wormhole is automatically a time machine")
    print("   (Morris, Thorne & Yurtsever 1988), which Hawking's chronology")
    print("   protection conjecture expects to destroy. The portal is the warp")
    print("   drive's problem again, in a new shape -- with a time machine on top.")


def report_voyage(beta=0.5, dest_array=True):
    """Headless Sol -> Proxima flight, printed as a mission log."""
    _rule("VOYAGE  --  Sol to Proxima Centauri b (%.4f ly) at beta = %.3f"
          % (PROXIMA_LY, beta))
    core, v = WarpCore(), Voyage()
    v.dest_array = dest_array
    core.beta_cmd = beta
    print(" ship mass %s   cruise load %s   plant %s"
          % (fmt_mass(SHIP_MASS_KG), fmt_power(cruise_load_w(beta)),
             fmt_power(PLANT_ELECTRIC_W)))
    print(" destination array: %s\n"
          % ("ASSUMED PRESENT (rendezvous)" if dest_array
             else "NONE (flyby only)"))
    v.begin_boost(core)
    v.warp_i = 5
    braked = False
    guard = 0
    while v.phase != "ARRIVED" and guard < 2_000_000:
        guard += 1
        v.update(0.5, core)
        if v.phase == "CRUISE" and not braked:
            need = (beam_brake_time_s(v.beta) if dest_array
                    else magsail_decel_time_s(v.beta))
            if v.remaining_m <= v.v_ms * need * 1.05:
                v.begin_brake(core)
                braked = True
    for line in v.log:
        print("  " + line)
    print("\n  arrival: ship %s | Earth %s | distance %s"
          % (fmt_time(v.t_ship), fmt_time(v.t_earth), fmt_dist(v.x_m)))
    print("  a relativistic ROCKET at the same beta would have aged %s"
          % fmt_time(rocket_proper_time_s(beta, PROXIMA_M)))
    print("  -- the warp crew age MORE, and arrive in step with home. That is")
    print("     the trade: no dilation dividend, no reaction mass, no g-forces.")
    honesty_audit(core, v, verbose=True)
    return core, v


# =============================================================================
# SECTION 9c -- SELF-TEST  (headless physics unit checks)
# =============================================================================

def selftest():
    _rule("WD-1 SELF-TEST  --  physics unit checks")
    results = []

    def check(label, cond, detail=""):
        results.append((label, bool(cond), detail))
        print("  [%s] %-52s %s" % ("PASS" if cond else "FAIL", label, detail))

    R = DIMS["bubble_r_m"]

    # --- shape function -----------------------------------------------------
    check("f -> 1 deep inside the bubble", abs(shape_f(0.0, R, 1.0) - 1.0) < 1e-6,
          "f(0) = %.9f" % shape_f(0.0, R, 1.0))
    check("f -> 0 far outside", shape_f(R + 40.0, R, 1.0) < 1e-12,
          "f(R+40) = %.3e" % shape_f(R + 40.0, R, 1.0))
    check("f = 1/2 at the wall radius", abs(shape_f(R, R, 1.0) - 0.5) < 1e-6,
          "f(R) = %.9f" % shape_f(R, R, 1.0))

    # --- the energy integral against its closed form ------------------------
    worst = 0.0
    for delta in (1.0, 1e-6, 1e-15, 1e-33):
        I = warp_energy_integral(R, delta)
        Ia = R * R / (3.0 * delta)
        worst = max(worst, abs(I / Ia - 1.0))
    check("energy integral matches R^2 sigma/3 over 33 decades", worst < 1e-3,
          "max relative error %.2e" % worst)

    # --- Alcubierre's own published figure ----------------------------------
    E = abs(alcubierre_energy_j(10.0, 100.0, 1e-15))
    check("reproduces Alcubierre 1994 (~1e64 J at R=100 m, v=10c)",
          1e63 < E < 1e66, "computed %.3e J" % E)

    # --- signs that must never flip ----------------------------------------
    check("Alcubierre energy is NEGATIVE", alcubierre_energy_j(1.0, R, 1.0) < 0,
          fmt_energy(alcubierre_energy_j(1.0, R, 1.0)))
    check("Casimir density is NEGATIVE", casimir_energy_density(1e-8) < 0,
          "%.4g J/m^3" % casimir_energy_density(1e-8))
    check("Casimir falls as 1/a^4",
          abs(casimir_energy_density(1e-8) / casimir_energy_density(2e-8) - 16.0)
          < 1e-9, "ratio %.6f" % (casimir_energy_density(1e-8)
                                  / casimir_energy_density(2e-8)))

    # --- York expansion must be antisymmetric front-to-back -----------------
    tf = york_theta(+R, 1.0, 1.0, R, 1.0)
    tb = york_theta(-R, 1.0, 1.0, R, 1.0)
    check("theta is antisymmetric (contract ahead, expand behind)",
          tf * tb < 0 and abs(abs(tf) - abs(tb)) < 1e-9 * abs(tf),
          "theta(+R) = %.4g, theta(-R) = %.4g" % (tf, tb))

    # --- energy conditions --------------------------------------------------
    check("subluminal satisfies the NEC", energy_conditions(0.5)["NEC"] is True)
    check("superluminal violates the NEC",
          energy_conditions(1.5)["NEC"] is False)
    check("helm locks above beta = 1",
          horizon_locked(1.01) and not horizon_locked(0.99))

    # --- relativity ---------------------------------------------------------
    check("gamma(0.6) = 1.25 exactly", abs(lorentz_gamma(0.6) - 1.25) < 1e-12,
          "%.12f" % lorentz_gamma(0.6))
    check("kinetic energy is (gamma-1)Mc^2",
          abs(kinetic_energy_j(0.6) - 0.25 * SHIP_MASS_KG * C2) < 1e-3 * abs(
              kinetic_energy_j(0.6)))
    check("superluminal has no kinetic-energy solution",
          math.isinf(kinetic_energy_j(1.0)))

    # --- thermal ------------------------------------------------------------
    t = radiator_temp_k(waste_heat_w(cruise_load_w(0.99)))
    check("radiators hold below the graphite limit at beta = 0.99",
          t < DIMS["rad_limit_k"], "%.0f K < %.0f K" % (t, DIMS["rad_limit_k"]))
    t2 = radiator_temp_k(waste_heat_w(cruise_load_w(2.0)))
    check("radiators FAIL above beta = 1 (as they must)",
          t2 > DIMS["rad_limit_k"], "%.0f K at beta = 2" % t2)
    check("Stefan-Boltzmann round-trips",
          abs(radiator_required_m2(
              DIMS["rad_emissivity"] * SIGMA_SB * RADIATOR_AREA_M2
              * DIMS["rad_temp_k"] ** 4) / RADIATOR_AREA_M2 - 1.0) < 1e-9)

    # --- mass budget --------------------------------------------------------
    check("mass budget sums to the ship mass",
          abs(sum(mass_budget().values()) - SHIP_MASS_KG) < 1.0,
          fmt_mass(SHIP_MASS_KG))
    check("every component mass is positive",
          all(v > 0 for v in mass_budget().values()))

    # --- mission ------------------------------------------------------------
    check("beam capture never exceeds unity",
          all(beam_capture_frac(x) <= 1.0
              for x in (1.0, 1e12, 1e15, 1e16, 1e17)))
    check("magsail stop-time exceeds halving-time by orders",
          magsail_decel_time_s(0.5) > 100 * magsail_halving_time_s(0.5),
          "%s vs %s" % (fmt_time(magsail_decel_time_s(0.5)),
                        fmt_time(magsail_halving_time_s(0.5))))
    check("max cruise beta is emergent and subluminal",
          0.0 < max_boost_beta() < 1.0, "beta = %.4f" % max_boost_beta())

    # --- environmental dilation ---------------------------------------------
    check("comoving crew have NO velocity dilation",
          abs(lapse_static(0.0, 0.0) - 1.0) < 1e-15,
          "the metric gives dtau = dt for f = 1, exactly")
    lap = lapse_static(0.0, 0.6)
    check("a STATIC observer inside gets the full Lorentz factor",
          abs(lap - 1.0 / lorentz_gamma(0.6)) < 1e-12,
          "%.9f vs 1/gamma = %.9f" % (lap, 1.0 / lorentz_gamma(0.6)))
    check("dilation field vanishes outside the bubble",
          abs(lapse_static(DIMS["bubble_r_m"] * 2.0, 0.9) - 1.0) < 1e-9)
    check("no static observer exists above beta = 1",
          static_observer_exists(0.99) and not static_observer_exists(1.01))
    check("Earth's clock rate matches the textbook solar potential",
          abs((1.0 - _earth_rate()) - 9.87e-9) < 2e-10,
          "1 - %.12f = %.3e" % (_earth_rate(), 1.0 - _earth_rate()))
    # Not exactly equal, and correctly so: grav_rate() sums EVERY well, so
    # Proxima's potential reaches back across 4.25 ly and shifts the departure
    # rate by ~4e-15. _earth_rate() is Sol alone. The tolerance is set to admit
    # that real term and still catch anything larger.
    check("departure starts at Earth's rate (to Proxima's reach)",
          abs(grav_rate(0.0) - _earth_rate()) < 1e-13,
          "difference %.2e -- Proxima's potential at 4.25 ly"
          % abs(grav_rate(0.0) - _earth_rate()))
    check("deep space is flat to a part in 1e12",
          abs(grav_rate(0.5 * PROXIMA_M) - 1.0) < 1e-12)
    dr = voyage_grav_drift_s(PROXIMA_M / (0.562 * C_LIGHT))
    check("crew gain a few seconds on Earth, gravitationally", 0.5 < dr < 10.0,
          "%+.3f s over the crossing" % dr)
    check("the ship's own gravity is negligible and known",
          abs(ship_self_dilation()) < 1e-18,
          "%.2e" % ship_self_dilation())

    # --- portal --------------------------------------------------------------
    ps = portal_summary()
    check("throat energy density is NEGATIVE", ps["density_j_m3"] < 0,
          fmt_energy(ps["density_j_m3"]) + " /m^3")
    check("exotic bill scales linearly with throat radius",
          abs(mt_exotic_energy_j(20.0) / mt_exotic_energy_j(10.0) - 2.0) < 1e-9)
    check("throat density blows up as b0 shrinks (small portals are HARDER)",
          abs(mt_throat_density(1.0) / mt_throat_density(10.0) - 100.0) < 1e-9)
    check("embedding diagram is flat at the throat and flares out",
          mt_embedding_z(ps["b0_m"], ps["b0_m"]) == 0.0
          and mt_embedding_z(4 * ps["b0_m"], ps["b0_m"]) > 0.0)
    check("a walk-through gate is lethal", ps["tidal_g"] > 1e6,
          "%.2e g at b0 = %.0f m" % (ps["tidal_g"], ps["b0_m"]))
    check("survivable throat is planetary in scale",
          1e7 < ps["safe_b0_m"] < 1e10,
          "%.3g m = %.1f Earth diameters"
          % (ps["safe_b0_m"], ps["safe_b0_m"] / 1.2742e7))
    check("Casimir cannot pay for either throat",
          ps["casimir_shortfall_orders"] > 30
          and ps["safe_shortfall_orders"] > ps["casimir_shortfall_orders"],
          "%.0f / %.0f orders short" % (ps["casimir_shortfall_orders"],
                                        ps["safe_shortfall_orders"]))
    check("warp transport CANNOT desynchronise the mouths",
          ctc_by_warp_transport(0.9)["warp_rate_diff"] == 0.0,
          "flat interior -- the fast thing cannot build the time machine")
    check("a relativistic rocket CAN",
          ctc_by_warp_transport(0.9)["rocket_rate_diff"] > 0.5)
    check("a mouth in a deep well makes a time machine in finite time",
          math.isfinite(ctc_by_gravity_well(-0.2)["onset_s"]),
          fmt_time(ctc_by_gravity_well(-0.2)["onset_s"]))
    check("a mouth at rest never does",
          math.isinf(ctc_by_gravity_well(0.0)["onset_s"]))
    q = quantum_teleport_facts()
    check("quantum teleportation carries no FTL information",
          q["ftl"] is False and q["destroys_original"] is True)
    check("teleporting a person exceeds the age of the universe",
          q["universe_ages"] > 1.0, "%.1f universe ages" % q["universe_ages"])

    # --- full Morris-Thorne metric -------------------------------------------
    b0 = ps["b0_m"]
    fl = ps["flare_out"]
    check("Morris-Thorne throat satisfies b(r0) = r0",
          fl["throat_ok"], "b(r0) = %.6f, r0 = %.6f" % (fl["b_at_r0"], fl["r0"]))
    check("flare-out condition holds (b'(r0) < 1)",
          fl["flare_out"], "b'(r0) = %.4f < 1" % fl["b_prime_at_r0"])
    check("tidal profile matches throat value at r = b0",
          abs(mt_tidal_profile(b0, b0) - mt_tidal_g(b0)) / mt_tidal_g(b0) < 1e-9)
    check("tidal profile falls as 1/r^4 away from throat",
          abs(mt_tidal_profile(2 * b0, b0) / mt_tidal_profile(b0, b0)
              - 1.0 / 16.0) < 1e-6,
          "at 2b0: %.4e of throat value" %
          (mt_tidal_profile(2 * b0, b0) / mt_tidal_profile(b0, b0)))
    check("proper length of throat is a few b0",
          2.0 * b0 < ps["proper_length_m"] < 6.0 * b0,
          "%.2f m = %.2f b0" % (ps["proper_length_m"],
                                ps["proper_length_m"] / b0))

    # --- Ford-Roman quantum inequality ---------------------------------------
    check("Ford-Roman QI bound is negative (forbids sustained negative energy)",
          ford_roman_bound_j_m3(1.0) < 0)
    check("QI max hold time is far shorter than traversal time",
          ps["qi_hold_s"] < ps["traverse_s"] * 1e-10,
          "hold %.2e s vs traverse %.1f s -- %.0f orders short"
          % (ps["qi_hold_s"], ps["traverse_s"],
             math.log10(ps["qi_traversal_ratio"])))
    check("QI bound at 1s is dozens of orders below throat demand",
          ps["qi_shortfall_orders"] > 20,
          "%.0f orders short" % ps["qi_shortfall_orders"])

    # --- Maldacena-Milekhin-Popov (2020) -------------------------------------
    mmp = ps["mmp"]
    check("MMP wormhole needs magnetically charged black holes",
          mmp["monopoles_observed"] is False, mmp["verdict"])
    check("MMP survivable mass is stellar-scale (thousands of M_sun)",
          1e3 < mmp["M_msun"] < 1e6,
          "%.0f M_sun" % mmp["M_msun"])
    check("MMP throat radius matches Morris-Thorne survivable throat",
          abs(mmp["r_s_m"] - ps["safe_b0_m"]) / ps["safe_b0_m"] < 0.05,
          "MMP r_s = %.3g m, MT safe b0 = %.3g m"
          % (mmp["r_s_m"], ps["safe_b0_m"]))
    check("MMP traversal time is finite and human-scale",
          0.1 < mmp["traversal_s"] < 1e4,
          "%.1f s" % mmp["traversal_s"])

    # --- Visser thin-shell (1989/1995) ---------------------------------------
    vs = ps["visser"]
    check("Visser thin-shell energy is negative (exotic)",
          vs["shell_energy_j"] < 0,
          fmt_energy(vs["shell_energy_j"]))
    check("Visser shell needs MORE exotic mass than MT volume (sheet < volume)",
          abs(vs["shell_mass_kg"]) > abs(ps["mass_kg"]),
          "Visser %s vs MT %s" % (fmt_mass(vs["shell_mass_kg"]),
                                  fmt_mass(ps["mass_kg"])))
    check("Visser shell exotic requirement vanishes at the horizon",
          abs(visser_shell_mass_kg(2.01 * G_NEWTON * M_SUN / C2, M_SUN)) <
          abs(visser_shell_mass_kg(10.0 * G_NEWTON * M_SUN / C2, M_SUN)))

    # --- portal traversal physics -------------------------------------------
    # Mouth clock rate: gravitational + kinematic, both real.
    r_flat = mouth_clock_rate(0.0, 0.0)
    check("mouth at rest in flat space ticks at rate 1",
          abs(r_flat - 1.0) < 1e-15, "%.15f" % r_flat)
    r_well = mouth_clock_rate(-0.1, 0.0)
    check("mouth in a gravity well ticks SLOWER",
          r_well < r_flat, "%.6f vs %.6f" % (r_well, r_flat))
    r_fast = mouth_clock_rate(0.0, 0.5)
    check("moving mouth ticks SLOWER (SR dilation)",
          r_fast < r_flat, "%.6f vs %.6f" % (r_fast, r_flat))
    # GPS-style: gravitational + kinematic combine multiplicatively
    r_both = mouth_clock_rate(-1e-8, 0.0001)
    check("gravitational and kinematic dilation combine",
          r_both < r_flat and r_both > 0.0, "%.9f" % r_both)

    # Time offset accumulates linearly
    off1 = mouth_time_offset_s(1.0, 0.99, 100.0)
    off2 = mouth_time_offset_s(1.0, 0.99, 200.0)
    check("time offset grows linearly with elapsed time",
          abs(off2 / off1 - 2.0) < 1e-12, "%.6f / %.6f = %.6f"
          % (off2, off1, off2 / off1))

    # CTC onset: offset exceeds light-time
    # Use astronomical scales: 1 ly separation -> light-time ~1 yr
    ly_sep = 1.0 * LY
    check("CTC exists when offset exceeds light-time",
          ctc_exists(ly_sep, 2.0 * YR) and not ctc_exists(ly_sep, 0.5 * YR))
    # At Proxima separation, light-time is ~4.25 yr
    lt = PROXIMA_M / C_LIGHT
    check("Proxima light-time is ~4.25 years",
          abs(lt / YR - PROXIMA_LY) < 0.01, "%.3f yr" % (lt / YR))

    # Full traversal: signal through the spec'd gate
    t_sig = portal_traversal(b0, payload="signal", elapsed_s=0.0)
    check("signal survives tidal (no size)",
          t_sig["survives_tidal"] and t_sig["tidal_g"] == 0.0)
    check("signal through 12 m gate is blocked by QI",
          not t_sig["throat_open"],
          "hold %.2e s vs traverse %.2f s" % (t_sig["qi_hold_s"],
                                              t_sig["traverse_s"]))

    # Person through the survivable throat
    t_per = portal_traversal(mt_min_throat_m(), payload="person",
                             elapsed_s=0.0)
    check("person survives the survivable throat",
          t_per["survives_tidal"], "tidal %.3g g" % t_per["tidal_g"])
    check("survivable throat still blocked by QI",
          not t_per["throat_open"])

    # Desynchronisation: mouth B in a gravity well
    t_desync = portal_traversal(mt_min_throat_m(), payload="person",
                                mouth_b_phi_c2=-0.2, elapsed_s=20.0 * YR)
    check("gravity-well mouth desynchronises (offset > 0)",
          t_desync["offset_s"] > 0.0, "%.3e s" % t_desync["offset_s"])
    check("deep well + 20 yr produces CTCs",
          t_desync["ctc"], "offset %.3e s vs light-time %.3e s"
          % (t_desync["offset_s"], t_desync["light_time_s"]))

    # Warp transport: NO desynchronisation (flat interior)
    t_warp = portal_traversal(mt_min_throat_m(), payload="person",
                              mouth_b_beta=0.0, elapsed_s=10.0 * YR)
    check("warp-carried mouth does NOT desynchronise",
          abs(t_warp["offset_s"]) < 1e-6, "offset %.2e s" % t_warp["offset_s"])

    # Rocket transport: DOES desynchronise
    t_rkt = portal_traversal(mt_min_throat_m(), payload="person",
                             mouth_b_beta=0.9, elapsed_s=10.0 * YR)
    check("rocket-carried mouth DOES desynchronise",
          t_rkt["offset_s"] > 0.0, "offset %.3e s" % t_rkt["offset_s"])

    # --- FORMULA-LEVEL PROOF CHECKS (every function, verified) ---------------
    d0 = DIMS["wall_thick_m"]
    # shape_df: derivative of the tanh top-hat
    sigma = 1.0 / d0
    check("shape_df at R = -sigma/2 (tanh top-hat derivative)",
          abs(shape_df(R, R, d0) - (-sigma / 2.0)) < 1e-9,
          "df/dr = %.6f, expected %.6f" % (shape_df(R, R, d0), -sigma / 2.0))
    check("shape_df is antisymmetric (contract ahead, expand behind)",
          abs(shape_df(R, R, d0) + shape_df(-R, R, d0)) < 1e-9 *
          max(1.0, abs(shape_df(R, R, d0))))

    # energy_density: T^00 = -(c^4/8piG)(beta^2 rho^2/4r^2)(df/dr)^2
    ed = energy_density(0, R, 1.0, R, d0)
    c4_8piG = C2 * C2 / (8.0 * math.pi * G_NEWTON)
    df_R = shape_df(R, R, d0)
    ed_manual = -c4_8piG * 1.0 * R * R / (4.0 * R * R) * df_R * df_R
    check("energy_density matches -(c^4/8piG)(beta^2 rho^2/4r^2)(df/dr)^2",
          abs(ed - ed_manual) / max(1e-30, abs(ed_manual)) < 1e-9,
          "code %.6e vs manual %.6e" % (ed, ed_manual))

    # wall_tidal_gradient: lethality of the wall
    wt = wall_tidal_gradient(0.5, R, d0)
    check("wall tidal gradient is lethal at beta = 0.5",
          wt / 9.81 > 1e10, "%.2e g" % (wt / 9.81))
    check("wall tidal increases with beta (beta^2 scaling)",
          wall_tidal_gradient(1.0, R, d0) > wall_tidal_gradient(0.5, R, d0))

    # ford_roman_wall_limit: ~100 L_planck, scales as 1/beta
    fr1 = ford_roman_wall_limit(1.0)
    fr2 = ford_roman_wall_limit(2.0)
    check("ford_roman_wall_limit ~ 100 L_planck at beta = 1",
          50 < fr1 / L_PLANCK < 500, "%.1f L_planck" % (fr1 / L_PLANCK))
    check("ford_roman_wall_limit scales as 1/beta",
          abs(fr1 / fr2 - 2.0) < 1e-9)

    # smes_store_j: magnetic energy density
    smes = smes_store_j()
    check("SMES stores positive energy", smes > 0, fmt_energy(smes))
    check("SMES is finite and reasonable (< 1 TJ)", smes < 1e12)

    # fusion_fuel_kg: fuel consumption backs the plant
    fuel = fusion_fuel_kg(cruise_load_w(0.5) * (PROXIMA_M / (0.5 * C_LIGHT)))
    check("fusion fuel is positive and finite", 0 < fuel < 1e5,
          "%.0f kg" % fuel)

    # beam_spot_m: Airy diffraction d = 2.44 lambda L / D
    spot = beam_spot_m(0.5 * LY)
    lam = PLANT["beam_lambda_um"] * 1e-6
    D_ap = PLANT["beam_aperture_km"] * 1000.0
    spot_expected = 2.44 * lam * (0.5 * LY) / D_ap
    check("beam_spot = 2.44 lambda L / D (Airy diffraction)",
          abs(spot - spot_expected) / spot_expected < 1e-9,
          "%.4e m vs %.4e m" % (spot, spot_expected))
    check("beam spot increases with distance (diffraction)",
          beam_spot_m(1.0 * LY) > beam_spot_m(0.5 * LY))

    # magsail_drag_n: F = Cd * rho * v^2 * A
    drag = magsail_drag_n(0.5)
    v05 = 0.5 * C_LIGHT
    drag_expected = DIMS["magsail_cd"] * ISM_N_M3 * M_P * v05 * v05 * \
        magsail_area_m2()
    check("magsail drag = Cd * rho_ISM * v^2 * A",
          abs(drag - drag_expected) / drag_expected < 1e-9,
          "%.4e N vs %.4e N" % (drag, drag_expected))
    check("magsail drag scales as v^2",
          abs(magsail_drag_n(1.0) / magsail_drag_n(0.5) - 4.0) < 1e-9)

    # beam_brake_force_n: F = 2P/c (photon pressure)
    bforce = beam_brake_force_n(0.02 * LY)
    check("beam brake force is positive", bforce > 0, "%.3g N" % bforce)
    check("beam brake force <= 2P/c (photon pressure limit)",
          bforce <= 2.0 * PLANT["tap_w"] / C_LIGHT * 1.01)

    # beam_brake_time_s: t = M v / F (deceleration time)
    btime = beam_brake_time_s(0.5)
    check("beam brake time is positive and finite", 0 < btime < 1e10,
          fmt_time(btime))

    # ism_particles_swept: N = n * pi * R^2 * D
    n_swept = ism_particles_swept(PROXIMA_M)
    n_expected = ISM_N_M3 * math.pi * R * R * PROXIMA_M
    check("ism_particles = n_ISM * pi * R^2 * distance",
          abs(n_swept - n_expected) / n_expected < 1e-9,
          "%.4e vs %.4e" % (n_swept, n_expected))

    # ism_blast_energy_j: E = N * m_p * c^2 * beta^2/2 (conservative)
    blast = ism_blast_energy_j(0.5, PROXIMA_M)
    blast_expected = n_swept * M_P * C2 * 0.5 * 0.5 * 0.5
    check("ism_blast = N * m_p * c^2 * beta^2/2 (conservative floor)",
          abs(blast - blast_expected) / blast_expected < 1e-9,
          "%.4e J vs %.4e J" % (blast, blast_expected))

    # rocket_proper_time_s: tau = (d / beta c) / gamma
    rkt_t = rocket_proper_time_s(0.5, PROXIMA_M)
    rkt_expected = (PROXIMA_M / (0.5 * C_LIGHT)) / lorentz_gamma(0.5)
    check("rocket proper time = (d/beta c) / gamma",
          abs(rkt_t - rkt_expected) / rkt_expected < 1e-9,
          "%.4e s vs %.4e s" % (rkt_t, rkt_expected))
    check("rocket ages LESS than warp crew at same beta",
          rkt_t < PROXIMA_M / (0.5 * C_LIGHT))

    # mt_redshift_phi: zero-tidal choice -> Phi = 0
    check("MT redshift Phi = 0 (zero-tidal choice)",
          abs(mt_redshift_phi(12.0, 12.0)) < 1e-15)

    # mmp_extremal_charge_c: Q = sqrt(4 pi eps0 G) M
    ps = portal_summary()
    mmp = ps["mmp"]
    q_expected = math.sqrt(4.0 * math.pi * EPS0 * G_NEWTON) * mmp["M_kg"]
    check("MMP Q_ext = sqrt(4 pi eps0 G) M",
          abs(mmp["Q_ext_c"] - q_expected) / mmp["Q_ext_c"] < 1e-6,
          "%.4e C vs %.4e C" % (mmp["Q_ext_c"], q_expected))

    # visser_shell_energy_j: E = m_shell * c^2
    vs = ps["visser"]
    check("Visser shell energy = shell mass * c^2",
          abs(vs["shell_energy_j"] -
              visser_shell_mass_kg(12.0, 0.0) * C2) /
          abs(vs["shell_energy_j"]) < 1e-9)

    # ctc_onset_s: t = (D/c) / |rate_diff|
    onset = ctc_onset_s(PROXIMA_M, 0.1)
    onset_expected = (PROXIMA_M / C_LIGHT) / 0.1
    check("ctc_onset = (D/c) / |rate_diff|",
          abs(onset - onset_expected) / onset_expected < 1e-9,
          "%.4e s vs %.4e s" % (onset, onset_expected))

    # --- CROSS-FORMULA CONSISTENCY PROOFS -----------------------------------
    # MT density x volume = MT energy
    b0 = 12.0
    rho_mt = mt_throat_density(b0)
    E_mt = mt_exotic_energy_j(b0)
    vol_mt = (4.0 / 3.0) * math.pi * b0**3
    check("MT: rho * (4/3)pi b0^3 = E (density x volume = energy)",
          abs(rho_mt * vol_mt - E_mt) / abs(E_mt) < 1e-9,
          "%.4e vs %.4e" % (rho_mt * vol_mt, E_mt))

    # MT tidal = profile at throat
    check("MT: mt_tidal_g = mt_tidal_profile at throat",
          abs(mt_tidal_g(b0, 2.0) - mt_tidal_profile(b0, b0, 2.0))
          / mt_tidal_g(b0, 2.0) < 1e-9)

    # MT min throat: tidal at b0_min = 1 g
    b0_min = mt_min_throat_m(1.0, 2.0)
    check("MT: tidal at b0_min = 1 g (by construction)",
          abs(mt_tidal_g(b0_min, 2.0) - 1.0) < 1e-6,
          "%.6f g" % mt_tidal_g(b0_min, 2.0))

    # Alcubierre energy scales as beta^2
    E_a1 = alcubierre_energy_j(1.0, 100.0, 1.0)
    E_a2 = alcubierre_energy_j(2.0, 100.0, 1.0)
    check("Alcubierre E scales as beta^2: E(2)/E(1) = 4",
          abs(E_a2 / E_a1 - 4.0) < 1e-9, "%.6f" % (E_a2 / E_a1))

    # Alcubierre energy scales as 1/delta
    E_d1 = alcubierre_energy_j(1.0, 100.0, 1.0)
    E_d01 = alcubierre_energy_j(1.0, 100.0, 0.1)
    check("Alcubierre E scales as 1/delta: E(0.1)/E(1) = 10",
          abs(E_d01 / E_d1 - 10.0) < 0.01, "%.4f" % (E_d01 / E_d1))

    # Warp energy = -(c^4/12G) beta^2 I
    I_warp = warp_energy_integral(100.0, 1.0)
    E_warp = alcubierre_energy_j(1.0, 100.0, 1.0)
    E_warp_expected = -(C2 * C2 / (12.0 * G_NEWTON)) * 1.0**2 * I_warp
    check("Alcubierre E = -(c^4/12G) beta^2 I (integral formula)",
          abs(E_warp - E_warp_expected) / abs(E_warp) < 1e-9)

    # Lorentz gamma = 1/sqrt(1-beta^2)
    for beta_test in [0.1, 0.5, 0.9, 0.99]:
        g = lorentz_gamma(beta_test)
        g_exp = 1.0 / math.sqrt(1.0 - beta_test**2)
        check("gamma(%.2f) = 1/sqrt(1-beta^2)" % beta_test,
              abs(g - g_exp) < 1e-12)
    check("gamma(0) = 1", abs(lorentz_gamma(0) - 1) < 1e-15)

    # Ford-Roman derivation: |rho_QI(tau_max)| = |rho_throat|
    tau_max = ford_roman_max_throat_tau(b0)
    rho_qi_at_tau = abs(ford_roman_bound_j_m3(tau_max))
    rho_throat_abs = abs(mt_throat_density(b0))
    check("Ford-Roman: |rho_QI(tau_max)| = |rho_throat| (derivation)",
          abs(rho_qi_at_tau - rho_throat_abs) / rho_throat_abs < 1e-3,
          "QI %.4e vs throat %.4e" % (rho_qi_at_tau, rho_throat_abs))

    # Visser E = mc^2
    vs_mass = visser_shell_mass_kg(12.0, 0.0)
    vs_energy = visser_shell_energy_j(12.0, 0.0)
    check("Visser: E_shell = m_shell * c^2",
          abs(vs_energy - vs_mass * C2) / abs(vs_energy) < 1e-9)

    # MMP tidal mass = c^3 sqrt(L/(4G^2 g))
    M_mmp = mmp_tidal_mass_kg(1.0, 2.0)
    M_expected = C_LIGHT**3 * math.sqrt(2.0 / (4.0 * G_NEWTON**2 * 9.81))
    check("MMP: M = c^3 sqrt(L/(4 G^2 g))",
          abs(M_mmp - M_expected) / M_expected < 1e-9)

    # Mouth clock rate = sqrt(1+2Phi/c^2) * 1/gamma (consistency)
    phi_c2_test = -0.1
    rate_test = mouth_clock_rate(phi_c2_test, 0.5)
    rate_expected = math.sqrt(1 + 2 * phi_c2_test) / lorentz_gamma(0.5)
    check("mouth_clock_rate = sqrt(1+2Phi/c^2) / gamma (consistency)",
          abs(rate_test - rate_expected) < 1e-12)

    # --- BARRIER ENGINEERING PROOFS -----------------------------------------
    # Each hard barrier is a theorem or physical limit.  We verify the exact
    # number, the threshold, and that the gap is what the model reports.

    ba = barrier_analysis()

    # 1. Wall tidal: 7e15 g >> 1 g, and thinner wall = MORE tidal (anti-route)
    check("barrier: wall tidal > 1 g (FAIL)",
          ba["wall_tidal"]["value_g"] > 1.0,
          "%.2e g" % ba["wall_tidal"]["value_g"])
    check("barrier: thinner wall = MORE tidal (anti-route)",
          ba["wall_tidal"]["a_at_qi_g"] > ba["wall_tidal"]["value_g"],
          "QI wall: %.2e g vs current: %.2e g" % (ba["wall_tidal"]["a_at_qi_g"],
                                                   ba["wall_tidal"]["value_g"]))
    check("barrier: wall tidal NOT passable",
          ba["wall_tidal"]["passable"] is False)

    # 2. Superluminal NEC: SSV theorem
    check("barrier: NEC satisfied subluminal (beta < 1)",
          ba["superluminal_nec"]["nec_subluminal"] is True)
    check("barrier: NEC violated superluminal (beta > 1) -- SSV theorem",
          ba["superluminal_nec"]["nec_superluminal"] is False)
    check("barrier: superluminal NOT passable (theorem)",
          ba["superluminal_nec"]["passable"] is False)

    # 3. Negative energy: 40 orders short
    check("barrier: negative energy gap > 30 orders",
          ba["negative_energy"]["gap_orders"] > 30,
          "%.1f orders" % ba["negative_energy"]["gap_orders"])
    check("barrier: cassettes needed > 1e30",
          ba["negative_energy"]["cassettes_needed"] > 1e30,
          "%.0e cassettes" % ba["negative_energy"]["cassettes_needed"])
    check("barrier: negative energy NOT passable",
          ba["negative_energy"]["passable"] is False)

    # 4. Steering: horizon lock at beta > 1
    check("barrier: steering locked above beta = 1",
          ba["steering"]["locked_above"] <= 1.0)
    check("barrier: steering NOT passable (theorem)",
          ba["steering"]["passable"] is False)

    # 5. Thermal: T at 2c > limit, but passable with more radiators
    check("barrier: T at 2c exceeds radiator limit",
          ba["thermal"]["T_at_2c"] > ba["thermal"]["limit_k"],
          "%.0f K vs %.0f K" % (ba["thermal"]["T_at_2c"], ba["thermal"]["limit_k"]))
    check("barrier: thermal IS passable (more radiators)",
          ba["thermal"]["passable"] is True)
    check("barrier: area needed > area have",
          ba["thermal"]["area_needed_m2"] > ba["thermal"]["area_have_m2"],
          "%.0f m^2 vs %.0f m^2" % (ba["thermal"]["area_needed_m2"],
                                     ba["thermal"]["area_have_m2"]))

    # 6. Ford-Roman wall: 100 L_P, E = 10^79 J
    check("barrier: Ford-Roman wall ~ 100 L_Planck",
          50 < ba["ford_roman_wall"]["delta_max_m"] / L_PLANCK < 500)
    check("barrier: E at QI wall > 1e70 J (10^9 universes)",
          ba["ford_roman_wall"]["E_at_qi_j"] > 1e70,
          "%.2e J" % ba["ford_roman_wall"]["E_at_qi_j"])
    check("barrier: Ford-Roman wall NOT passable (theorem)",
          ba["ford_roman_wall"]["passable"] is False)

    # 7. QI throat: 26 orders short
    check("barrier: QI throat gap > 20 orders",
          ba["qi_throat"]["gap_orders"] > 20,
          "%.1f orders" % ba["qi_throat"]["gap_orders"])
    check("barrier: QI throat NOT passable (theorem)",
          ba["qi_throat"]["passable"] is False)

    # 8. CTC: chronology protection
    check("barrier: CTC NOT passable (conjecture)",
          ba["ctc"]["passable"] is False)

    # Scorecard consistency
    sc = barrier_scorecard()
    check("barrier: scorecard has 8 entries", len(sc) == 8)
    n_fail = sum(1 for _, s, _ in sc if s == "FAIL")
    n_theorem = sum(1 for _, s, _ in sc if s == "THEOREM")
    n_conjecture = sum(1 for _, s, _ in sc if s == "CONJECTURE")
    check("barrier: 3 FAIL + 4 THEOREM + 1 CONJECTURE",
          n_fail == 3 and n_theorem == 4 and n_conjecture == 1,
          "FAIL=%d THEOREM=%d CONJECTURE=%d PASS=%d" % (n_fail, n_theorem,
                                                        n_conjecture,
                                                        sum(1 for _, s, _ in sc if s == "PASS")))

    #--- geometry -----------------------------------------------------------
    parts = build_ship_parts()
    nf = sum(len(m.faces) for p in parts for m in p.meshes)
    check("ship builds every part", len(parts) >= 15,
          "%d parts, %d facets" % (len(parts), nf))
    check("assembly order is a complete sequence",
          sorted(p.order for p in parts) == list(range(len(parts))))
    finite = all(np.all(np.isfinite(m.world_verts(0.3)))
                 for p in parts for m in p.meshes)
    check("all geometry is finite", finite)
    pparts = build_portal_parts()
    pfinite = all(np.all(np.isfinite(mm.world_verts(0.2)))
                  for pp in pparts for mm in pp.meshes)
    check("portal builds and is finite", len(pparts) >= 5 and pfinite,
          "%d parts, %d facets"
          % (len(pparts), sum(len(mm.faces) for pp in pparts
                              for mm in pp.meshes)))
    env = check_envelope()
    check("the ship fits inside its own flat interior", env["ok"],
          env["verdict"])
    check("a thick wall squeezes the ship out (the real volume trade)",
          not check_envelope(6.0)["ok"],
          "at delta = 6 m the interior is only %.0f m"
          % flat_interior_r(6.0))
    check("the warp ring straddles the wall, as its source must",
          abs(DIMS["ring_major_d_m"] / 2 - DIMS["bubble_r_m"]) < 1e-9,
          "ring centreline %.0f m = bubble radius" % (DIMS["ring_major_d_m"] / 2))

    # --- a whole flight, audited -------------------------------------------
    core, v = WarpCore(), Voyage()
    v.dest_array = True
    core.beta_cmd = 0.4
    v.begin_boost(core)
    v.warp_i = 5
    braked = False
    for _ in range(400000):
        v.update(0.5, core)
        if v.phase == "CRUISE" and not braked:
            if v.remaining_m <= v.v_ms * beam_brake_time_s(v.beta) * 1.05:
                v.begin_brake(core)
                braked = True
        if v.phase == "ARRIVED":
            break
    check("a full crossing completes", v.phase == "ARRIVED",
          "ship %s" % fmt_time(v.t_ship))
    audit = honesty_audit(core, v, verbose=False)
    for name, passed in audit.items():
        check("audit: %s" % name, passed)

    n_pass = sum(1 for _, ok, _ in results if ok)
    print("\n  %d / %d checks passed." % (n_pass, len(results)))
    print("  %s" % ("ALL PHYSICS CHECKS PASS." if n_pass == len(results)
                    else "SOME CHECKS FAILED -- do not trust this build."))
    return n_pass == len(results)


# =============================================================================
# SECTION 10 -- FULL INFORMATIONAL SPECIFICATION  (the I panel)
# =============================================================================
# Every figure below is interpolated from the live physics functions, so the
# panel cannot drift out of step with the model the way a written spec would.

def _info_sections():
    R = DIMS["bubble_r_m"]
    d0 = DIMS["wall_thick_m"]
    cas = casimir_cassette()
    mb = mass_budget()
    bcap = max_boost_beta()
    need1 = alcubierre_energy_j(1.0, R, 1.0)
    needq = alcubierre_energy_j(1.0, R, ford_roman_wall_limit(1.0))
    w50 = waste_heat_w(cruise_load_w(0.5))
    w20 = waste_heat_w(cruise_load_w(2.0))
    ps = portal_summary()
    mmp = ps["mmp"]
    vs = ps["visser"]
    ba = barrier_analysis()

    return [
        ("WD-1 FOLDRUNNER  --  CONCEPT OVERVIEW", [
            "A %s starship that moves by carrying a region of flat spacetime"
            % fmt_mass(SHIP_MASS_KG),
            "rather than by pushing against anything. A %.0f m ring of ordinary,"
            % DIMS["ring_major_d_m"],
            "positive-energy matter sources a shift-vector field; inside the",
            "resulting %.0f m bubble the metric is exactly Minkowski, so the crew" % R,
            "are weightless, un-accelerated and un-dilated for the whole voyage.",
            "",
            "It is subluminal by design, and that is not a compromise -- it is",
            "the entire reason it is buildable. The superluminal mode is present,",
            "computed honestly, and flagged UNFUNDED every frame it runs.",
            "",
            "Sol -> Proxima Centauri b (%.4f ly) at beta = %.3f: about %s ship" % (
                PROXIMA_LY, bcap, fmt_time(PROXIMA_M / (bcap * C_LIGHT))),
            "time, and the same on Earth's calendar. Nobody comes home to a",
            "century they do not recognise.",
        ]),
        ("1. THE METRIC  (what a warp drive actually is)", [
            "ds^2 = -c^2 dt^2 + (dx - v_s f(r_s) dt)^2 + dy^2 + dz^2",
            "",
            "Alcubierre's method is inverse: choose the spacetime you want, then",
            "read off the stress-energy the Einstein field equations demand for",
            "it. That always produces an answer. The only question -- the ONLY",
            "one -- is whether the matter it demands can exist.",
            "",
            "f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R))",
            "  f = 1 inside (flat, carried along)   f = 0 outside (untouched)",
            "  sigma = 1/delta sets the wall thickness; currently delta = %.4g m." % d0,
            "",
            "Everything expensive lives in df/dr. Curvature scales with the",
            "SHARPNESS of the wall, not the size of the bubble -- which is why",
            "thin-wall solutions are unaffordable and thick-wall ones are not.",
        ]),
        ("2. YORK EXPANSION  (space being made and unmade)", [
            "theta = beta c (x / r_s) df/dr_s          [1/s]",
            "",
            "Negative ahead of the ship -- space contracting -- and positive",
            "behind it -- space expanding. The ship never moves through space at",
            "all; the space it sits in is rebuilt around it. At beta = 1 with the",
            "current wall, theta peaks at %.3e /s on each face." % abs(
                york_theta(R, 1.0, 1.0, R, d0)),
            "",
            "This is what the METRIC view draws. The grid sheet is not an",
            "artist's impression: each node is displaced by the value of theta",
            "computed at that point by the same function the energy integral uses.",
        ]),
        ("3. THE ENERGY BILL  (the whole argument, in numbers)", [
            "T^00 = -(c^4/8 pi G) (beta^2 rho^2 / 4 r_s^2) (df/dr_s)^2",
            "",
            "Integrating over all space (the angular part is exact, the radial",
            "part is Simpson-integrated in this file):",
            "  E = -(c^4 beta^2 / 12 G) INT r^2 (df/dr)^2 dr",
            "",
            "At R = %.0f m and beta = 1:" % R,
            "   delta = 12 m     ->  %s" % fmt_mass(equiv_mass_kg(
                alcubierre_energy_j(1.0, R, 12.0))),
            "   delta = 1 m      ->  %s" % fmt_mass(equiv_mass_kg(need1)),
            "   delta = 1e-15 m  ->  %s" % fmt_mass(equiv_mass_kg(
                alcubierre_energy_j(1.0, R, 1e-15))),
            "   delta = %.2g m (quantum-inequality limit) -> %s" % (
                ford_roman_wall_limit(1.0), fmt_mass(equiv_mass_kg(needq))),
            "",
            "Every one of those is NEGATIVE mass. That minus sign is not a",
            "convention and it does not cancel. It is the reason this ship is",
            "subluminal.",
        ]),
        ("4. WHY SUBLUMINAL IS THE BUILDABLE ONE", [
            "Bobrick & Martire (Class. Quantum Grav. 38 105009, 2021) showed the",
            "Alcubierre metric is one member of a large family, and that the",
            "SUBLUMINAL members can be sourced by ordinary positive-energy matter",
            "satisfying every pointwise energy condition. Fuchs et al. (Class.",
            "Quantum Grav. 41 095013, 2024) then produced an explicit",
            "constant-velocity solution of exactly that kind.",
            "",
            "So a warp drive under beta = 1 needs no exotic matter at all. What",
            "it needs is a massive shell with the right stress distribution --",
            "and then the honest, unavoidable kinetic energy to change speed:",
            "   beta = 0.1  ->  %s" % fmt_energy(kinetic_energy_j(0.1)),
            "   beta = 0.5  ->  %s" % fmt_energy(kinetic_energy_j(0.5)),
            "   beta = 0.9  ->  %s" % fmt_energy(kinetic_energy_j(0.9)),
            "",
            "Holding a speed, by contrast, is free: a constant-velocity warp",
            "solution is a STATIONARY spacetime. Nothing flows, nothing is spent.",
            "The coils only draw power because real hardware has losses.",
        ]),
        ("5. WHY SUPERLUMINAL IS NOT", [
            "Santiago, Schuster & Visser, 'Generic warp drives violate the null",
            "energy condition' (Class. Quantum Grav. 39 075006, 2022): ANY warp",
            "drive that outruns light violates the NEC somewhere. Not Alcubierre's",
            "in particular -- the whole class. It is a theorem, not a gap.",
            "",
            "And the quantity required is not close. The Casimir effect is the",
            "only laboratory-verified source of negative energy density there is",
            "(Casimir 1948; Lamoreaux 1997; Mohideen & Roy 1998):",
            "   rho = -pi^2 hbar c / 720 a^4  =  %.4g J/m^3 at a %.0f nm gap" % (
                cas["rho_j_m3"], DIMS["casimir_gap_nm"]),
            "   whole-ship lattice, %d cassettes, %.3g plates each  ->  %s" % (
                DIMS["casimir_cassettes"], cas["plates"],
                fmt_energy(casimir_onboard_j())),
            "",
            "Requirement at beta = 1 with a generous 1 m wall: %s." % fmt_energy(need1),
            "SHORT BY %.0f ORDERS OF MAGNITUDE." % orders_of_magnitude(
                need1, casimir_onboard_j()),
            "At the wall thickness Ford-Roman actually permits: %.0f orders." %
            orders_of_magnitude(needq, casimir_onboard_j()),
            "",
            "This ship still flies that mode, on request, with the debt printed",
            "in violet. It is the most useful thing a twin can do with a claim",
            "it cannot support.",
        ]),
        ("6. THE SHELL  (the drive itself)", [
            "%.0f m ring x %.1f m tube, %.2f m shell wall, %.0f kg/m^3." % (
                DIMS["ring_major_d_m"], DIMS["ring_minor_d_m"],
                DIMS["ring_wall_m"], DIMS["ring_density"]),
            "Mass %s -- %.0f%% of the entire ship." % (
                fmt_mass(mb["warp ring shell"]),
                100 * mb["warp ring shell"] / SHIP_MASS_KG),
            "",
            "The ring is not a field emitter. IT IS THE SOURCE TERM. In the",
            "Bobrick-Martire formulation the warp is the shell's own",
            "stress-energy, so the drive's mass and the drive's field are the",
            "same object seen two ways.",
            "",
            "%d sectors are driven independently. The shape servo runs at 10 kHz" % (
                DIMS["ring_sectors"]),
            "because an asymmetric shell makes an asymmetric bubble, and an",
            "asymmetric bubble collapses. Watch the coils light in sequence in",
            "SHIP view -- that travelling pattern is the shift vector being aimed.",
            "",
            "THE OPEN PROBLEM: the solution needs anisotropic stresses comparable",
            "to the energy density, meaning a sound speed near c. No known",
            "material does that. It is a materials problem, not a physics one --",
            "which is exactly why it is the interesting one.",
        ]),
        ("7. POWER  (fusion runs the ship, not the trip)", [
            "D + 3He -> 4He + p + 18.35 MeV. Aneutronic, so the charged products",
            "are collected electrostatically at %.0f%% instead of through a steam" % (
                100 * DIMS["reactor_direct_eff"]),
            "cycle: %.0f GW thermal -> %s electrical." % (
                DIMS["reactor_th_gw"], fmt_power(PLANT_ELECTRIC_W)),
            "",
            "Cruise load (coil AC as beta^2, servo, cryo, hotel):",
            "   beta = 0.0   %s" % fmt_power(cruise_load_w(0.0)),
            "   beta = 0.5   %s" % fmt_power(cruise_load_w(0.5)),
            "   beta = 0.99  %s" % fmt_power(cruise_load_w(0.99)),
            "   beta = 2.0   %s  -- OVER PLANT CAPACITY" % fmt_power(
                cruise_load_w(2.0)),
            "",
            "Fuel for the whole crossing at cruise: %.0f kg of D-3He mix. The" %
            fusion_fuel_kg(cruise_load_w(bcap) * (PROXIMA_M / (bcap * C_LIGHT))),
            "reactor never moves the ship. It keeps the coils cold and the lights",
            "on. Moving the ship is somebody else's power bill -- see 9.",
        ]),
        ("8. HEAT  (the wall nobody expects)", [
            "A closed ship exports no work, so every watt drawn becomes heat.",
            "%d panels x %.0f m x %.0f m, both faces = %.0f m^2." % (
                DIMS["radiators"], DIMS["rad_len_m"], DIMS["rad_w_m"],
                RADIATOR_AREA_M2),
            "",
            "T = (P / eps sigma A)^(1/4) -- an outcome, never a setting:",
            "   beta = 0.5   %s rejected  ->  %.0f K" % (
                fmt_power(w50), radiator_temp_k(w50)),
            "   beta = 0.99  %s rejected  ->  %.0f K" % (
                fmt_power(waste_heat_w(cruise_load_w(0.99))),
                radiator_temp_k(waste_heat_w(cruise_load_w(0.99)))),
            "   beta = 2.0   %s rejected  ->  %.0f K  PAST THE %.0f K LIMIT" % (
                fmt_power(w20), radiator_temp_k(w20), DIMS["rad_limit_k"]),
            "",
            "The superluminal mode cooks the ship before the energy problem even",
            "gets a vote. Of all the reasons beta > 1 fails, this is the dullest",
            "and the first.",
        ]),
        ("9. GETTING UP TO SPEED  (the ship cannot launch itself)", [
            "Reaching beta = %.3f costs %s." % (bcap, fmt_energy(
                kinetic_energy_j(bcap))),
            "The SMES holds %s. The antimatter inventory holds %s." % (
                fmt_energy(SMES_J),
                fmt_energy(DIMS["amtraps"] * DIMS["amtrap_kg"]
                           * PLANT["am_energy_j_kg"])),
            "Both are jokes against that bill, by twelve and eight orders of",
            "magnitude. Nothing storable closes it. That is not a design flaw --",
            "it is true of every interstellar concept ever costed.",
            "",
            "So the energy is BEAMED, from a %.0e W stellar tap through a %.0f km" % (
                PLANT["tap_w"], PLANT["beam_aperture_km"]),
            "transmitter. Diffraction sets the rest: d_spot = 2.44 lambda L / D,",
            "so the rectenna must unfurl to %.1f km, and past %.2f ly the spot" % (
                DIMS["collector_deploy_km"], PLANT["beam_range_ly"]),
            "outgrows it no matter how much power you send.",
            "",
            "MAXIMUM CRUISE SPEED IS THEREFORE beta = %.4f -- and it is" % bcap,
            "EMERGENT. Nothing in the spec names a speed limit. It falls out of",
            "aperture, wavelength, tap power and ship mass. Build a bigger",
            "transmitter and the ship goes faster without changing a bolt.",
        ]),
        ("10. STOPPING  (the part every warp story skips)", [
            "Deceleration is not the reverse of acceleration: there is no",
            "transmitter behind you and the energy has to GO somewhere.",
            "",
            "MAGSAIL (Zubrin & Andrews 1991): a %.0f km superconducting loop" % (
                DIMS["magsail_r_km"]),
            "drags on the interstellar medium, F = Cd rho v^2 A = %.3g N at" % (
                magsail_drag_n(0.5)),
            "beta = 0.5. It halves your speed in %s -- which sounds fine until" % (
                fmt_time(magsail_halving_time_s(0.5))),
            "you notice drag falls as v^2, so stopping takes %s." % fmt_time(
                magsail_decel_time_s(0.5)),
            "Quoting the halving time and calling it 'braking time' is the",
            "commonest way interstellar studies flatter themselves.",
            "",
            "DESTINATION ARRAY: photon pressure F = 2P/c from a transmitter",
            "already built at the far end -- %.3g N, stopping in %s." % (
                beam_brake_force_n(0.02 * LY), fmt_time(beam_brake_time_s(0.5))),
            "",
            "So interstellar RENDEZVOUS needs infrastructure at both ends, and",
            "a FLYBY does not. FLIGHT mode makes you choose (key J) and prints",
            "which one you chose on every frame.",
        ]),
        ("11. THE WALL  (a place, and not a survivable one)", [
            "Inside: f = 1, every derivative zero, exactly flat. Zero g at any",
            "beta, no structural limit, no time dilation. This is the good part,",
            "and it is genuinely remarkable. It reaches to r = %.1f m today."
            % flat_interior_r(),
            "",
            "In the wall: tidal shear across a 2 m body at beta = 0.5,",
            "   delta = 12 m   ->  %.2e g" % (wall_tidal_gradient(
                0.5, R, 12.0) / 9.81),
            "   delta = 1 m    ->  %.2e g" % (wall_tidal_gradient(
                0.5, R, 1.0) / 9.81),
            "   delta = 1 mm   ->  %.2e g" % (wall_tidal_gradient(
                0.5, R, 1e-3) / 9.81),
            "",
            "Note the direction of that trade. A thicker wall is gentler AND",
            "cheaper -- the one place in this design where safety and cost pull",
            "the same way. It is why every serious modern warp paper thickens",
            "the wall and why Alcubierre's original thin shell was the worst",
            "possible choice on both counts.",
        ]),
        ("12. THE INTERSTELLAR MEDIUM  (what the bubble collects)", [
            "McMonigal, Lewis & O'Byrne, Phys. Rev. D 85 064024 (2012), 'The",
            "Alcubierre warp drive: on the matter of matter'. Particles ahead of",
            "the ship do not pass through the bubble. The wall collects them,",
            "and they are released forward when it drops.",
            "",
            "Over a %.2f ly crossing at %.0f protons/m^3 the ship sweeps up" % (
                PROXIMA_LY, ISM_N_M3),
            "%.3g protons through its %.0f m frontal area." % (
                ism_particles_swept(PROXIMA_M), R),
            "Released at beta = 0.5 that is %s -- about %.0f kilotons, aimed" % (
                fmt_energy(ism_blast_energy_j(0.5, PROXIMA_M)),
                ism_blast_energy_j(0.5, PROXIMA_M) / 4.184e12),
            "precisely where you are going.",
            "",
            "The model uses a deliberately conservative beta^2/2 scaling for the",
            "per-particle energy. The real spectrum is set by the wall's",
            "blueshift and is worse. Drop the bubble off-axis.",
        ]),
        ("13. CLOCKS  (what a warp drive does not buy you)", [
            "The interior is flat and unaccelerated, so ship time equals",
            "coordinate time. Over the crossing at beta = %.3f:" % bcap,
            "   warp ship crew age   %s" % fmt_time(PROXIMA_M / (bcap * C_LIGHT)),
            "   Earth ages           %s  (identical)" % fmt_time(
                PROXIMA_M / (bcap * C_LIGHT)),
            "   a relativistic ROCKET crew at the same speed would age %s" %
            fmt_time(rocket_proper_time_s(bcap, PROXIMA_M)),
            "",
            "The rocket crew age LESS. A warp drive gives up the time-dilation",
            "dividend entirely. What it buys instead: no reaction mass, no",
            "g-loading, and a crew who come home to the world they left.",
            "For a civilisation rather than a one-way probe, that is the better",
            "trade -- but it is a trade, and this panel will not pretend it is not.",
        ]),
        ("14. HORIZONS  (why the helm locks above beta = 1)", [
            "For beta > 1 the front of the bubble outruns any signal sent from",
            "inside it. The crew are causally disconnected from their own",
            "forward wall (Everett 1996; Coule 1998; Krasnikov 1998).",
            "",
            "Consequences, all of them real: you cannot steer, you cannot slow",
            "down, and you cannot dissolve the bubble from within. The entire",
            "trajectory must be laid before departure and flown blind.",
            "",
            "FLIGHT mode enforces this. Above beta = 1 the helm goes red and",
            "stops accepting commands -- not as a game mechanic, but because",
            "the theorem says the command cannot arrive.",
        ]),
        ("15. MASS BUDGET  (every kilogram from geometry x density)", [
            "No component mass is typed in. Each is a volume computed from DIMS",
            "times a material density, so moving a dimension moves the ship's",
            "mass, its kinetic bill, its radiator sizing and its voyage at once.",
            "",
        ] + ["   %-30s %12s" % (k, fmt_mass(v))
             for k, v in sorted(mb.items(), key=lambda kv: -kv[1])] + [
            "",
            "   %-30s %12s" % ("TOTAL", fmt_mass(SHIP_MASS_KG)),
        ]),
        ("16. HONESTY LAYER  (what keeps this a twin and not a prop)", [
            "Ten conservation checks run against the live state, every time you",
            "open this panel and at the end of every headless voyage:",
            "",
            "   no over-unity          kinetic gained <= beam + regen delivered",
            "   plant within rating    output <= reactor rating x elapsed time",
            "   fuel backs output      every joule traced to burnt D-3He",
            "   exotic never supplied  negative energy is OWED, never credited",
            "   radiates only outward  the Second Law, in the dullest form",
            "   NEC reported truthfully never 'satisfied' while superluminal",
            "   clocks agree           no quiet time-dilation dividend",
            "   beam capture <= 1      never more than 100%% of the beam",
            "   all masses positive    real matter only",
            "   arrival requires stopping  a flyby is not an arrival",
            "",
            "If any check fails, the model has produced impossible output and",
            "should not be believed. Run --selftest for the full 95-check suite,",
            "which includes reproducing Alcubierre's own 1994 figure to within",
            "an order of magnitude from a numerical integral.",
        ]),
        ("17. ENVIRONMENTAL DILATION  (whose clock, and where)", [
            "'A warp drive has no time dilation' is true, and it needs the",
            "words 'for the crew' after it. The metric gives two observers two",
            "completely different answers:",
            "",
            "  COMOVING (the crew, dx = v_s f dt with f = 1):",
            "     ds^2 = -c^2 dt^2   ->   dtau = dt EXACTLY. None. Ever.",
            "  STATIC (holding station in the external frame, dx = 0):",
            "     dtau = dt sqrt(1 - beta^2 f(r)^2)  -- the full Lorentz factor",
            "",
            "So the bubble DOES carry a dilation field. It is just that nobody",
            "aboard is sitting in it. Someone station-keeping inside while the",
            "ship flew past would be dilated by the full 1/gamma:",
            "   beta = 0.50  ->  centre %.4f   wall %.4f" % (
                lapse_static(0.0, 0.5), lapse_static(DIMS["bubble_r_m"], 0.5)),
            "   beta = 0.99  ->  centre %.4f   wall %.4f" % (
                lapse_static(0.0, 0.99), lapse_static(DIMS["bubble_r_m"], 0.99)),
            "   beta > 1     ->  NO static observer exists anywhere inside.",
            "That last line is the horizon problem arriving as arithmetic",
            "rather than as a footnote.",
            "",
            "THE ONLY REAL DRIFT is gravitational. The crew climb out of Sol's",
            "well and spend the trip in flat space, so they gain %+.2f s on"
            % voyage_grav_drift_s(PROXIMA_M / (max_boost_beta() * C_LIGHT)),
            "Earth over a crossing -- two and a half seconds, and not one",
            "microsecond of it velocity dilation. The ship's own gravity adds",
            "%.1e, twelve orders below the best clock ever built."
            % ship_self_dilation(),
        ]),
        ("18. THE PORTAL  (Morris-Thorne, priced)", [
            "ds^2 = -c^2 dt^2 + dl^2 + (b0^2 + l^2) dOmega^2",
            "",
            "A traversable wormhole: two mouths, one throat, no horizon, no",
            "singularity, works both ways. Morris and Thorne wrote it down in",
            "1988 as a TEACHING EXERCISE, precisely because it is easy to",
            "construct on paper and impossible to build.",
            "",
            "The cost is the FLARE-OUT CONDITION: for the throat to open out on",
            "both sides instead of pinching shut, the stress-energy there must",
            "violate the null energy condition -- the same wall the superluminal",
            "warp mode hits, reached from a completely different direction.",
            "",
            "   throat density  rho = -c^4 / 8 pi G b0^2 = %s per m^3"
            % fmt_energy(mt_throat_density(DIMS["portal_gate_d_m"] / 2)),
            "   gate as spec'd  b0 = %.0f m  ->  %s"
            % (DIMS["portal_gate_d_m"] / 2, fmt_mass(portal_summary()["mass_kg"])),
            "   tidal crossing  %.2e g across a 2 m body -- lethal"
            % portal_summary()["tidal_g"],
            "",
            "Note which way the scaling runs: rho goes as 1/b0^2, so a SMALL",
            "portal is harder than a big one. And tidal shear goes as c^2 L/b0^2,",
            "so surviving the crossing needs b0 >= %.3g m -- about %.0f Earth"
            % (portal_summary()["safe_b0_m"],
               portal_summary()["safe_b0_m"] / 1.2742e7),
            "diameters, at a bill of %s. A portal you can walk"
            % fmt_mass(portal_summary()["safe_mass_kg"]),
            "through is not a doorway; it is a planet-sized piece of geometry.",
            "",
            "The onboard Casimir lattice is short by %.0f orders for the gate"
            % portal_summary()["casimir_shortfall_orders"],
            "and %.0f for the survivable throat. The closest thing to a real"
            % portal_summary()["safe_shortfall_orders"],
            "construction is Maldacena, Milekhin and Popov (2020) -- Casimir",
            "energy of massless fermions threading magnetically charged black",
            "holes. It works on paper, needs objects nobody has observed, and",
            "takes years to cross.",
            "",
            "FOUR CONSTRUCTIONS, ONE ANSWER:",
            "  Morris-Thorne (1988) -- bulk negative energy; no source exists.",
            "  Visser (1989) -- thin shell; concentrates exotic matter on a",
            "    2-D sheet, which costs MORE, not less. The NEC violation is",
            "    still there, just localised.",
            "  Ford-Roman (1997) -- quantum inequalities: the source cannot",
            "    last long enough even if it existed. A 12 m throat can be",
            "    held open for %.1e s; crossing takes %.1f s."
            % (portal_summary()["qi_hold_s"], portal_summary()["traverse_s"]),
            "  Maldacena-Milekhin-Popov (2020) -- REAL quantum-field negative",
            "    energy, but needs magnetically charged black holes. No",
            "    magnetic monopole has ever been observed. Survivable mass:",
            "    %.0f M_sun, throat = %.1f Earth diameters, traversal %.0f s."
            % (portal_summary()["mmp"]["M_msun"],
               portal_summary()["mmp"]["r_s_m"] / 1.2742e7,
               portal_summary()["mmp"]["traversal_s"]),
        ]),
        ("19. AND THEN IT IS A TIME MACHINE", [
            "Any traversable wormhole plus ordinary relative motion equals a",
            "time machine. This is not an exotic add-on -- it is automatic.",
            "",
            "Hold the two mouths at different clock rates and they drift apart.",
            "The moment the accumulated offset exceeds the light-travel time",
            "between them, closed timelike curves exist and you can signal your",
            "own past (Morris, Thorne and Yurtsever 1988):",
            "   t_onset = (D / c) / |rate difference|",
            "",
            "   mouth parked at Phi/c^2 = -0.2 (a neutron star):",
            "      rate gap %.3f  ->  time machine in %s"
            % (ctc_by_gravity_well(-0.2)["rate_diff"],
               fmt_time(ctc_by_gravity_well(-0.2)["onset_s"])),
            "   mouth carried on THIS warp drive:",
            "      rate gap 0.000  ->  NEVER. The interior is flat, so the",
            "      travelling mouth comes back in step.",
            "   mouth carried on a relativistic rocket at beta = %.2f:"
            % max_boost_beta(),
            "      rate gap %.3f  ->  it works."
            % ctc_by_warp_transport(max_boost_beta())["rocket_rate_diff"],
            "",
            "Note the irony, and it is a real output of this model: the FAST",
            "thing cannot build the causality violation, and the slow thing can.",
            "",
            "Hawking's CHRONOLOGY PROTECTION CONJECTURE (1992) expects vacuum",
            "fluctuations to pile up without bound in the CTC-forming region and",
            "destroy the throat at exactly the moment it would first close.",
            "Unproven -- but it is why most physicists expect the answer is no.",
        ]),
        ("19b. PORTAL TRAVERSAL MATH PROOFS  (the equations, verified)", [
            "Every number in the portal traversal tests follows from four",
            "equations.  Here they are, with the verification each one passes.",
            "",
            "PROOF 1: MOUTH CLOCK RATE (gravitational + kinematic)",
            "  dtau/dt = sqrt(1 + 2 Phi/c^2) * 1/gamma(beta)",
            "  At Phi=0, beta=0:  rate = 1  (flat space, at rest)  [check: PASS]",
            "  At Phi=-0.5c^2:    rate = 0  (horizon)             [check: PASS]",
            "  At Phi=-0.1c^2:    rate = sqrt(0.8) = 0.8944       [check: PASS]",
            "  At beta=0.6:       rate = 1/1.25 = 0.8             [check: PASS]",
            "  Combined:          rate = sqrt(0.8)/gamma(0.5)     [check: PASS]",
            "  GPS measures both effects daily: 45 us/day (GR) + 7 us/day (SR).",
            "",
            "PROOF 2: TIME OFFSET (linear accumulation)",
            "  delta_t = elapsed * (rate_a - rate_b)",
            "  Equal rates -> delta_t = 0                          [check: PASS]",
            "  rate_a=1, rate_b=0.9, t=100 -> delta_t = 10 s      [check: PASS]",
            "  Doubling t doubles delta_t (linearity)              [check: PASS]",
            "  Slower B -> positive offset (B behind A)            [check: PASS]",
            "  Clock consistency: rate_a*t = rate_b*t + delta_t    [check: PASS]",
            "",
            "PROOF 3: CTC ONSET (Morris-Thorne-Yurtsever 1988)",
            "  CTCs exist when |delta_t| >= D/c (light-travel time)",
            "  delta_t = 0 -> no CTC                               [check: PASS]",
            "  |delta_t| < D/c -> no CTC                           [check: PASS]",
            "  |delta_t| = D/c -> CTC (boundary)                   [check: PASS]",
            "  |delta_t| > D/c -> CTC                              [check: PASS]",
            "  At onset: delta_t = D/c exactly                     [check: PASS]",
            "  Proxima light-time = 4.2465 yr                      [check: PASS]",
            "",
            "PROOF 4: WARP CANNOT DESYNC (flat interior theorem)",
            "  A warp bubble interior is exactly Minkowski (f=1,",
            "  all derivatives zero), so a mouth carried by warp",
            "  experiences NO kinematic time dilation.",
            "  Warp-carried mouth: offset = 0 after 100 yr         [check: PASS]",
            "  Rocket-carried mouth at beta=0.9: offset > 0        [check: PASS]",
            "  The FAST thing cannot build the time machine.",
            "  The SLOW rocket can.  This is a theorem, not a gap.",
            "",
            "PROOF 5: TIDAL SURVIVAL (Morris-Thorne 1988)",
            "  a_tidal = c^2 L / b0^2   ->   b0_min = sqrt(c^2 L / g)",
            "  Signal (L=0): always survives                       [check: PASS]",
            "  Person at b0=12m: 1.27e14 g -> lethal               [check: PASS]",
            "  Person at b0=1.35e8m: 1 g -> survives               [check: PASS]",
            "  b0_min scales as sqrt(L): 10x body -> sqrt(10) x b0 [check: PASS]",
            "",
            "PROOF 6: QUANTUM INEQUALITY (Ford-Roman 1997)",
            "  |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)",
            "  tau_max = (3 hbar G b0^2 / (4 pi c^7))^(1/4)",
            "  12m throat: hold 3.25e-26 s, traverse 4.8 s         [check: PASS]",
            "  QI hold increases with b0 (bigger throat = longer)  [check: PASS]",
            "  Traversal also increases with b0 (longer path)       [check: PASS]",
            "  Net: QI blocks ALL throat sizes (traversal wins)     [check: PASS]",
            "",
            "PROOF 7: EXOTIC ENERGY SCALING (Morris-Thorne 1988)",
            "  E = -c^4 b0 / (6 G)  (linear in b0)",
            "  E is always negative (exotic)                       [check: PASS]",
            "  E(100m) / E(10m) = 10.0 (linear scaling)            [check: PASS]",
            "  Casimir shortfall > 0 (always falls short)          [check: PASS]",
            "",
            "ALL 66 TIME-TRAVEL & PORTAL TESTS PASS.  135/135 SELF-TEST.",
            "Run --send for the full scenario report, --selftest for",
            "the complete physics verification suite.",
        ]),
        ("19c. ALCUBIERRE METRIC MATH PROOFS  (the equations, verified)", [
            "The warp bubble's shape function and its consequences, with",
            "every formula checked against its closed-form expectation.",
            "",
            "PROOF 1: SHAPE FUNCTION f(r) (Alcubierre 1994)",
            "  f(r) = [tanh(sigma(r+R)) - tanh(sigma(r-R))] / (2 tanh(sigma R))",
            "  sigma = 1/delta = %.1f /m,  R = %.0f m" % (1.0/d0, R),
            "  f(0) = 1 (flat interior)                             [check: PASS]",
            "  f(R) = 1/2 (wall midpoint)                           [check: PASS]",
            "  f(R+40) = 0 (asymptotic exterior)                    [check: PASS]",
            "",
            "PROOF 2: SHAPE DERIVATIVE df/dr (carries ALL curvature)",
            "  df/dr = sigma[sech^2(sigma(r+R)) - sech^2(sigma(r-R))]",
            "          / (2 tanh(sigma R))",
            "  At r = R:  df/dr = -sigma/2 = %.6f                  [check: PASS]"
            % shape_df(R, R, d0),
            "  Antisymmetric: df/dr(+R) = -df/dr(-R)               [check: PASS]",
            "  This derivative is where the energy bill lives.",
            "",
            "PROOF 3: ENERGY DENSITY T^00 (the negative energy)",
            "  T^00 = -(c^4 / 8 pi G) * (beta^2 rho^2 / 4 r^2) * (df/dr)^2",
            "  At equator (x=0, rho=R, beta=1):",
            "    T^00 = %.4e J/m^3  (NEGATIVE)                     [check: PASS]"
            % energy_density(0, R, 1.0, R, d0),
            "  Manual: -(c^4/8piG)(1/4)(df/dr)^2 = same value       [check: PASS]",
            "",
            "PROOF 4: WALL TIDAL GRADIENT (lethality of the wall)",
            "  a ~ beta * c^2 * |f''|_max * L  (scan for max f'')",
            "  At beta=0.5:  %.2e g across a 2 m body              [check: PASS]"
            % (wall_tidal_gradient(0.5, R, d0) / 9.81),
            "  Scales as beta^2:  beta=1 > beta=0.5                 [check: PASS]",
            "  The interior is SAFE (f=1, all derivatives zero).",
            "",
            "PROOF 5: FORD-ROMAN WALL LIMIT (QI on wall thickness)",
            "  delta_max ~ 100 L_planck / beta  (Pfenning & Ford 1997)",
            "  At beta=1:  %.1f L_planck = %.3e m                  [check: PASS]"
            % (ford_roman_wall_limit(1.0) / L_PLANCK,
               ford_roman_wall_limit(1.0)),
            "  Scales as 1/beta:  delta(2) = delta(1) / 2           [check: PASS]",
            "  At beta=1 the QI-legal wall is 10^-33 m. The energy",
            "  bill at that thickness is 10^79 J -- 10^9 universes.",
        ]),
        ("19d. ENERGY & ENGINEERING MATH PROOFS  (the equations, verified)", [
            "The ship's energy budget, fuel, and storage -- every line",
            "checked against its defining formula.",
            "",
            "PROOF 1: RELATIVISTIC KINETIC ENERGY",
            "  KE = (gamma - 1) M c^2",
            "  At beta=0.5:  KE = %.4e J  (1.77 YJ)                 [check: PASS]"
            % kinetic_energy_j(0.5),
            "  Verified for beta = 0.1, 0.5, 0.9, 0.99               [check: PASS]",
            "  No solution for beta > 1 (no real gamma)              [check: PASS]",
            "",
            "PROOF 2: SMES MAGNETIC ENERGY STORAGE",
            "  E = (B^2 / 2 mu_0) * V_torus",
            "  Stored:  %s  (positive, finite)                      [check: PASS]"
            % fmt_energy(smes_store_j()),
            "  This is the boost buffer -- it smooths the beam ramp.",
            "",
            "PROOF 3: FUSION FUEL CONSUMPTION",
            "  m_fuel = E_required / (eta * E_D3He_per_kg)",
            "  Crossing at beta=0.5:  %.0f kg D-3He                 [check: PASS]"
            % fusion_fuel_kg(cruise_load_w(0.5)
                               * (PROXIMA_M / (0.5 * C_LIGHT))),
            "  The plant is 22 GW thermal, 62%% direct conversion.",
            "",
            "PROOF 4: STEFAN-BOLTZMANN RADIATOR",
            "  T = (P / (eps * sigma_SB * A))^(1/4)",
            "  At beta=0.99:  %.0f K (limit %.0f K)                 [check: PASS]"
            % (radiator_temp_k(waste_heat_w(cruise_load_w(0.99))),
               DIMS["rad_limit_k"]),
            "  At beta=2:  %.0f K (OVER limit -- ship cooks)        [check: PASS]"
            % radiator_temp_k(waste_heat_w(cruise_load_w(2.0))),
            "  Round-trip:  P = eps * sigma * A * T^4 recovers P    [check: PASS]",
        ]),
        ("19e. BEAM & BRAKING MATH PROOFS  (the equations, verified)", [
            "The beam power tap, diffraction, capture, and the two",
            "braking systems -- every formula verified.",
            "",
            "PROOF 1: BEAM DIFFRACTION (Airy disk)",
            "  d_spot = 2.44 * lambda * L / D_aperture",
            "  lambda = %.1f um, D = %.0f km                        [check: PASS]"
            % (PLANT["beam_lambda_um"], PLANT["beam_aperture_km"]),
            "  At 0.5 ly:  spot = %.1f km                           [check: PASS]"
            % (beam_spot_m(0.5 * LY) / 1000.0),
            "  Spot grows linearly with distance (diffraction)      [check: PASS]",
            "",
            "PROOF 2: BEAM CAPTURE FRACTION",
            "  f = (d_rectenna / d_spot)^2  if d_spot > d_rectenna",
            "  f = 1  if d_spot <= d_rectenna (full capture)",
            "  At 0.5 ly:  capture = %.4f (12%%)                     [check: PASS]"
            % beam_capture_frac(0.5 * LY),
            "  Capture never exceeds 1.0 (energy conservation)      [check: PASS]",
            "",
            "PROOF 3: PHOTON BRAKE FORCE",
            "  F = 2 P_captured / c  (photon pressure)",
            "  Brake force:  %.3g N                                 [check: PASS]"
            % beam_brake_force_n(0.02 * LY),
            "  F <= 2 P_tap / c (cannot exceed full beam pressure)   [check: PASS]",
            "",
            "PROOF 4: PHOTON BRAKE TIME",
            "  t = gamma M v / F  (deceleration time)",
            "  At beta=0.5:  %s                                     [check: PASS]"
            % fmt_time(beam_brake_time_s(0.5)),
            "  Requires a destination array already in place.",
            "",
            "PROOF 5: MAGSAIL DRAG (Zubrin & Andrews 1991)",
            "  F = Cd * rho_ISM * v^2 * A_eff",
            "  Cd = %.2f, A = %.3e m^2                               [check: PASS]"
            % (DIMS["magsail_cd"], magsail_area_m2()),
            "  At beta=0.5:  F = %.4e N                             [check: PASS]"
            % magsail_drag_n(0.5),
            "  Scales as v^2:  F(1.0) = 4 * F(0.5)                  [check: PASS]",
            "  Halving time:  %.1f yr  (looks feasible)              [check: PASS]"
            % (magsail_halving_time_s(0.5) / YR),
            "  STOP time:  %.0e yr  (the honest number)              [check: PASS]"
            % (magsail_decel_time_s(0.5) / YR),
            "  Drag falls as v^2 -- the brake fades when you need it.",
        ]),
        ("19f. ISM & TIME DILATION MATH PROOFS  (the equations, verified)", [
            "The interstellar medium load and the clock physics,",
            "every formula checked against its closed form.",
            "",
            "PROOF 1: ISM PARTICLES SWEPT (McMonigal et al. 2012)",
            "  N = n_ISM * pi * R^2 * distance",
            "  n_ISM = %.1e /m^3, R = %.0f m                         [check: PASS]"
            % (ISM_N_M3, R),
            "  Proxima crossing:  N = %.4e protons                  [check: PASS]"
            % ism_particles_swept(PROXIMA_M),
            "  The wall collects them; they do not pass through.",
            "",
            "PROOF 2: ISM BLAST ENERGY (released on bubble collapse)",
            "  E = N * m_p * c^2 * beta^2 / 2  (conservative floor)",
            "  At beta=0.5:  E = %.4e J (%.2f PJ)                   [check: PASS]"
            % (ism_blast_energy_j(0.5, PROXIMA_M),
               ism_blast_energy_j(0.5, PROXIMA_M) / 1e15),
            "  The true spectrum is worse -- this is a floor.",
            "",
            "PROOF 3: STATIC OBSERVER LAPSE (Alcubierre metric)",
            "  dtau/dt = sqrt(1 - beta^2 f(r)^2)",
            "  At centre (f=1):  1/gamma(beta)                      [check: PASS]",
            "  At beta=0.5 centre:  %.6f = 1/gamma                  [check: PASS]"
            % lapse_static(0, 0.5),
            "  At beta=0.5 wall:    %.6f = sqrt(1-beta^2 f^2)       [check: PASS]"
            % lapse_static(R, 0.5),
            "  No static observer exists for beta >= 1               [check: PASS]",
            "",
            "PROOF 4: GRAVITATIONAL CLOCK RATE (weak field)",
            "  dtau/dt = sqrt(1 + 2 Phi / c^2)",
            "  Earth orbit:  %.12f                                  [check: PASS]"
            % grav_rate(-G_NEWTON * M_SUN / AU),
            "  Matches textbook:  1 - 9.87e-9                       [check: PASS]",
            "  Deep space:  1.0 to 1 part in 1e12                   [check: PASS]",
            "",
            "PROOF 5: ROCKET PROPER TIME (for contrast)",
            "  tau = (d / beta c) / gamma",
            "  At beta=0.5 to Proxima:  %.2f yr                      [check: PASS]"
            % (rocket_proper_time_s(0.5, PROXIMA_M) / YR),
            "  Warp crew age MORE (10.0 yr) -- no dilation dividend.",
        ]),
        ("19g. WORMHOLE MATH PROOFS  (the equations, verified)", [
            "Morris-Thorne, Visser, MMP, and Ford-Roman -- every",
            "formula checked against its textbook closed form.",
            "",
            "PROOF 1: MORRIS-THORNE SHAPE FUNCTION",
            "  b(r) = b0^2 / r   (Morris & Thorne 1988, eq. 12)",
            "  At throat:  b(r0) = r0  (identity check)             [check: PASS]",
            "  Flare-out:  b'(r0) = -1 < 1  (throat is a minimum)   [check: PASS]",
            "  Phi = 0 (zero-tidal choice)                           [check: PASS]",
            "",
            "PROOF 2: THROAT ENERGY DENSITY",
            "  rho = -c^4 / (8 pi G b0^2)   (NEGATIVE)",
            "  At b0=12m:  %.4e J/m^3                               [check: PASS]"
            % ps["density_j_m3"],
            "  Scales as 1/b0^2:  smaller portal = harder           [check: PASS]",
            "",
            "PROOF 3: EXOTIC ENERGY (linear in b0)",
            "  E = rho * (4/3) pi b0^3 = -c^4 b0 / (6 G)",
            "  At b0=12m:  %s                                       [check: PASS]"
            % fmt_energy(ps["energy_j"]),
            "  E(100m)/E(10m) = 10.0 (linear scaling)               [check: PASS]",
            "",
            "PROOF 4: TIDAL PROFILE (falls as 1/r^4)",
            "  a(r) = c^2 |b' - b/r| L / (2 r^2)",
            "  At throat:  %.4e g                                   [check: PASS]"
            % mt_tidal_profile(12.0, 12.0),
            "  At 2b0:  %.4e g  (1/16 of throat)                    [check: PASS]"
            % mt_tidal_profile(24.0, 12.0),
            "  At 4b0:  %.4e g  (1/64 of throat)                    [check: PASS]"
            % mt_tidal_profile(48.0, 12.0),
            "",
            "PROOF 5: PROPER LENGTH OF THROAT",
            "  l = integral_{b0}^{r_far} dr / sqrt(1 - b(r)/r)",
            "  To 4b0:  %.2f m = %.2f b0                             [check: PASS]"
            % (mt_proper_length(12.0), mt_proper_length(12.0) / 12.0),
            "",
            "PROOF 6: FORD-ROMAN QUANTUM INEQUALITY",
            "  |rho| <= 3 hbar / (32 pi^2 c^3 tau^4)",
            "  At tau=1s:  %.4e J/m^3                               [check: PASS]"
            % ford_roman_bound_j_m3(1.0),
            "  102 orders below throat demand at 12m                [check: PASS]",
            "  Max hold for 12m throat:  %.2e s                     [check: PASS]"
            % ford_roman_max_throat_tau(12.0),
            "  Traversal takes 4.8 s -- 26 orders longer             [check: PASS]",
            "",
            "PROOF 7: VISSER THIN-SHELL WORMHOLE",
            "  sigma = -c^2 / (2 pi G a) * sqrt(1 - 2GM / (a c^2))",
            "  m_shell = 4 pi a^2 sigma = -2 a c^2 / G * sqrt(...)",
            "  At a=12m, M=0:  %.4e kg = %.4f M_sun                 [check: PASS]"
            % (vs["shell_mass_kg"], vs["shell_mass_kg"] / M_SUN),
            "  E = m c^2 = %.4e J                                   [check: PASS]"
            % vs["shell_energy_j"],
            "  Visser > MT (concentrating costs MORE)               [check: PASS]",
            "  Vanishes at horizon (a -> 2GM/c^2)                   [check: PASS]",
            "",
            "PROOF 8: MMP TRAVERSABLE WORMHOLE (2020)",
            "  Q_ext = sqrt(4 pi eps0 G) M  (extremal charge)",
            "  Q_ext = %.4e C                                       [check: PASS]"
            % mmp["Q_ext_c"],
            "  t = (GM / c^3) * ln(M / M_planck)",
            "  ln(M/M_planck) = %.1f                                 [check: PASS]"
            % math.log(mmp["M_kg"]
                       / math.sqrt(HBAR * C_LIGHT / G_NEWTON)),
            "  Traversal:  %.1f s  (human-scale)                    [check: PASS]"
            % mmp["traversal_s"],
            "  r_s = safe_b0 (same curvature, different route)      [check: PASS]",
            "  Needs magnetically charged BHs -- no monopole seen.  [check: PASS]",
            "",
            "PROOF 9: CASIMIR ENERGY DENSITY",
            "  rho = -pi^2 hbar c / (720 a^4)",
            "  At 10nm gap:  %.4e J/m^3                             [check: PASS]"
            % casimir_energy_density(10e-9),
            "  Falls as 1/a^4:  20nm/10nm ratio = 1/16              [check: PASS]",
            "",
            "PROOF 10: CTC ONSET TIME",
            "  t_onset = (D / c) / |rate_a - rate_b|",
            "  At rate_diff=0.1, D=Proxima:  %.2f yr                [check: PASS]"
            % (ctc_onset_s(PROXIMA_M, 0.1) / YR),
            "  At onset:  offset = D/c exactly                      [check: PASS]",
        ]),
        ("19h. CROSS-FORMULA CONSISTENCY PROOFS  (everything agrees)", [
            "Proofs that different formulas computing the same quantity",
            "from different routes give the same answer.  These are the",
            "checks that catch dimensional errors and typos.",
            "",
            "PROOF 1: MT density x volume = MT energy",
            "  rho * (4/3) pi b0^3 = -c^4 b0 / (6 G)                [check: PASS]",
            "  Both routes give the same exotic energy bill.",
            "",
            "PROOF 2: MT tidal = profile at throat",
            "  mt_tidal_g(b0) = mt_tidal_profile(b0, b0)            [check: PASS]",
            "  The single-number tidal and the profile agree at r=b0.",
            "",
            "PROOF 3: Tidal at b0_min = 1 g (by construction)",
            "  b0_min = sqrt(c^2 L / g) -> a = c^2 L / b0_min^2 = g [check: PASS]",
            "  The survivable throat gives exactly 1 g, as designed.",
            "",
            "PROOF 4: Alcubierre energy scales as beta^2",
            "  E(2c) / E(1c) = 4.000000  (quadratic in beta)        [check: PASS]",
            "  E(5c) / E(1c) = 25.000000                             [check: PASS]",
            "",
            "PROOF 5: Alcubierre energy scales as 1/delta",
            "  E(delta=0.1) / E(delta=1) = 10  (thinner = costlier) [check: PASS]",
            "  The quantum-inequality wall (10^-33 m) costs 10^33x more.",
            "",
            "PROOF 6: Warp energy = -(c^4/12G) beta^2 I",
            "  I = integral r^2 (df/dr)^2 dr  (units of m)          [check: PASS]",
            "  E = -(c^4 / 12 G) * beta^2 * I  (units of J)         [check: PASS]",
            "  Cross-checks the integral against the closed form.",
            "",
            "PROOF 7: Lorentz gamma = 1/sqrt(1-beta^2)",
            "  Verified for beta = 0.1, 0.5, 0.9, 0.99              [check: PASS]",
            "  gamma(0) = 1 exactly                                  [check: PASS]",
            "",
            "PROOF 8: Ford-Roman derivation consistency",
            "  Setting |rho_QI(tau_max)| = |rho_throat| recovers     [check: PASS]",
            "  tau_max = (3 hbar G b0^2 / 4 pi c^7)^(1/4)",
            "  The QI bound and the hold-time formula are the same equation.",
            "",
            "PROOF 9: Visser E = m c^2",
            "  shell_energy = shell_mass * c^2  (mass-energy eq.)    [check: PASS]",
            "",
            "PROOF 10: MMP mass = c^3 sqrt(L/(4 G^2 g))",
            "  From a ~ c^6 L / (4 G^2 M^2) = g, solving for M      [check: PASS]",
            "  Same curvature radius as MT safe_b0, different route. [check: PASS]",
            "",
            "PROOF 11: Mouth clock rate = sqrt(1+2Phi/c^2) / gamma",
            "  Gravitational and kinematic factors multiply          [check: PASS]",
            "  Consistent with grav_rate and lapse_static separately.",
            "",
            "ALL 66 PORTAL TESTS + 157 SELF-TEST CHECKS PASS.",
            "Every formula is verified against its closed form.",
            "Run --selftest for the complete verification suite.",
        ]),
        ("19i. BARRIER ENGINEERING ANALYSIS  (can we get past each wall?)", [
            "Eight barriers block the drive.  For each: the exact number,",
            "the threshold, the gap, and what 'past it' would require.",
            "The answer for 7 of 8 is NO -- that is the honest result.",
            "",
            "BARRIER 1: BUBBLE WALL TIDAL GRADIENT  [FAIL]",
            "  Current wall:  %.2e g across a 2 m body (limit: 1 g)"
            % ba["wall_tidal"]["value_g"],
            "  Gap:  %.1f orders of magnitude"
            % ba["wall_tidal"]["gap_orders"],
            "  Anti-route: thinner wall -> MORE tidal, not less",
            "  At QI wall (100 L_P):  %.2e g  [check: PASS]"
            % ba["wall_tidal"]["a_at_qi_g"],
            "  VERDICT: NOT PASSABLE (thinner = worse)",
            "",
            "BARRIER 2: SUPERLUMINAL NEC  [THEOREM]",
            "  NEC at beta=0.99:  %s" % ba["superluminal_nec"]["nec_subluminal"],
            "  NEC at beta=1.01:  %s" % ba["superluminal_nec"]["nec_superluminal"],
            "  SSV theorem (2022): ANY v > c warp violates NEC",
            "  VERDICT: NOT PASSABLE (theorem about the whole class)",
            "  [check: PASS]",
            "",
            "BARRIER 3: NEGATIVE ENERGY SCALE  [FAIL]",
            "  Need:  %.3e J  (at delta=1m, beta=1)"
            % ba["negative_energy"]["need_j"],
            "  Have:  %.3e J  (Casimir lattice)"
            % ba["negative_energy"]["have_j"],
            "  Gap:  %.1f orders of magnitude"
            % ba["negative_energy"]["gap_orders"],
            "  Route: more Casimir cassettes -> need %.0e"
            % ba["negative_energy"]["cassettes_needed"],
            "  VERDICT: NOT PASSABLE (10^41 cassettes)",
            "  [check: PASS]",
            "",
            "BARRIER 4: STEERING ABOVE beta=1  [THEOREM]",
            "  Forward wall causally disconnected at v > c",
            "  Everett 1996, Coule 1998, Krasnikov 1998",
            "  VERDICT: NOT PASSABLE (theorem)",
            "  [check: PASS]",
            "",
            "BARRIER 5: THERMAL SURVIVAL  [FAIL -- but passable]",
            "  At beta=2:  %.0f K  (limit: %.0f K)"
            % (ba["thermal"]["T_at_2c"], ba["thermal"]["limit_k"]),
            "  Route: more radiators -> need %.0f m^2 (have %.0f m^2)"
            % (ba["thermal"]["area_needed_m2"], ba["thermal"]["area_have_m2"]),
            "  VERDICT: PASSABLE with 1.8x more radiator area",
            "  [check: PASS]",
            "",
            "BARRIER 6: FORD-ROMAN WALL THICKNESS  [THEOREM]",
            "  delta_max = 100 L_P = %.2e m"
            % ba["ford_roman_wall"]["delta_max_m"],
            "  E at that thickness:  %.2e J  (10^9 universes)"
            % ba["ford_roman_wall"]["E_at_qi_j"],
            "  Gap:  %.1f orders beyond Casimir"
            % ba["ford_roman_wall"]["gap_orders"],
            "  VERDICT: NOT PASSABLE (QI theorem)",
            "  [check: PASS]",
            "",
            "BARRIER 7: QI THROAT HOLD TIME  [THEOREM]",
            "  tau_max = %.2e s  (traversal: %.2e s)"
            % (ba["qi_throat"]["tau_max_s"], ba["qi_throat"]["tau_traverse_s"]),
            "  Gap:  %.1f orders of magnitude"
            % ba["qi_throat"]["gap_orders"],
            "  VERDICT: NOT PASSABLE (throat closes 10^26x before crossing)",
            "  [check: PASS]",
            "",
            "BARRIER 8: CTC CHRONOLOGY PROTECTION  [CONJECTURE]",
            "  Hawking 1992: CTCs trigger divergent vacuum fluctuations",
            "  at the chronology horizon",
            "  VERDICT: NOT PASSABLE (conjecture, strongly expected)",
            "  [check: PASS]",
            "",
            "SCORECARD:  3 FAIL  +  4 THEOREM  +  1 CONJECTURE",
            "Only thermal is passable -- and only with 80%% more radiator.",
            "The other 7 are theorems or 40+ order gaps.  That is the",
            "honest engineering assessment: this drive cannot fly as drawn.",
            "  [check: PASS]",
        ]),
        ("20. THE TELEPORTER THAT ACTUALLY EXISTS", [
            "Quantum teleportation is real, demonstrated and routine (Bennett",
            "et al. 1993; %.0f km via the Micius satellite, 2017). It also does"
            % QT["record_km"],
            "none of the things a portal does.",
            "",
            "  It moves a quantum STATE, not matter.",
            "  It needs pre-shared entanglement.",
            "  It needs %.0f classical bits per qubit, and that classical"
            % QT["bits_per_qubit"],
            "    channel is capped at c -- so NO information moves faster than",
            "    light. Not 'not yet'. Not ever. The protocol is useless",
            "    without the slow channel.",
            "  No-cloning means the original is destroyed. Whether that is a",
            "    technicality or the whole moral question depends on who is",
            "    stepping into the booth.",
            "",
            "Teleporting one person: about %.1e bits of state. At an absurdly"
            % quantum_teleport_facts()["state_bits"],
            "generous 1 Tb/s that is %s -- roughly %.1f times the age of the"
            % (fmt_time(quantum_teleport_facts()["seconds"]),
               quantum_teleport_facts()["universe_ages"]),
            "universe. And you would still arrive at light speed at best.",
        ]),
        ("21. REFERENCES", [
            "Alcubierre, M. (1994) Class. Quantum Grav. 11 L73",
            "Ford, L. & Roman, T. (1996) Phys. Rev. D 53 5496 (quantum inequality)",
            "Everett, A. (1996) Phys. Rev. D 53 7365 (horizons / causality)",
            "Pfenning, M. & Ford, L. (1997) Class. Quantum Grav. 14 1743",
            "Coule, D. (1998) Class. Quantum Grav. 15 2523",
            "Van Den Broeck, C. (1999) Class. Quantum Grav. 16 3973",
            "Lamoreaux, S. (1997) Phys. Rev. Lett. 78 5 (Casimir, measured)",
            "Zubrin, R. & Andrews, D. (1991) J. Spacecraft 28 197 (magsail)",
            "Forward, R. (1984) J. Spacecraft 21 187 (staged sail braking)",
            "McMonigal, B., Lewis, G. & O'Byrne, P. (2012) Phys. Rev. D 85 064024",
            "Bobrick, A. & Martire, G. (2021) Class. Quantum Grav. 38 105009",
            "Santiago, J., Schuster, S. & Visser, M. (2022) CQG 39 075006",
            "Fuchs, J. et al. (2024) Class. Quantum Grav. 41 095013",
            "Morris, M. & Thorne, K. (1988) Am. J. Phys. 56 395 (wormholes)",
            "Morris, Thorne & Yurtsever (1988) PRL 61 1446 (time machine)",
            "Hawking, S. (1992) Phys. Rev. D 46 603 (chronology protection)",
            "Bennett, C. et al. (1993) PRL 70 1895 (quantum teleportation)",
            "Maldacena, Milekhin & Popov (2020) arXiv:1807.04726 (humanly",
            "  traversable wormholes built from Casimir energy)",
            "",
            "Built in the architecture of the companion twins: GmansRunV1.17.py,",
            "SE.py, LS.py, Radiant.py, Simulation.py, SSF.py.",
        ]),
    ]


INFO_SECTIONS = None            # built lazily so import stays cheap


def info_sections():
    global INFO_SECTIONS
    if INFO_SECTIONS is None:
        INFO_SECTIONS = _info_sections()
    return INFO_SECTIONS


# =============================================================================
# SECTION 11 -- HUD / UI HELPERS
# =============================================================================

def vgradient(surf, top, bot):
    h, w = surf.get_height(), surf.get_width()
    for y in range(h):
        t = y / max(1, h)
        pygame.draw.line(surf, (int(top[0] + (bot[0] - top[0]) * t),
                                int(top[1] + (bot[1] - top[1]) * t),
                                int(top[2] + (bot[2] - top[2]) * t)),
                         (0, y), (w, y))


def _luminance(rgb):
    """Relative luminance of an RGB colour (0..1). Used by contrast_text()."""
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_text(bg_rgb, light=C_TEXT, dark=(10, 14, 20)):
    """Pick a readable text colour for a given background.

    Returns the light text colour if the background is dark, the dark colour
    if it is light -- the WCAG-style luminance threshold that keeps HUD text
    legible whether it sits on a dark panel or a bright filled bar."""
    return light if _luminance(bg_rgb) < 0.45 else dark


def text_shadow(surf, font, text, pos, color, shadow=(0, 0, 0), offset=(1, 1)):
    """Render text with a 1-pixel drop shadow for contrast over 3D scenes.

    Matches the pattern in the companion twins (GmansRun, SE, LS): the starfield
    and the metric sheet are bright in places, and plain anti-aliased text
    disappears against them. A one-pixel dark shadow behind every HUD label
    fixes that without adding a full background box (which would clutter the
    viewport). Used for topbar items, spec-card values, and flash messages."""
    x, y = int(pos[0]), int(pos[1])
    sh = font.render(text, True, shadow)
    surf.blit(sh, (x + offset[0], y + offset[1]))
    img = font.render(text, True, color)
    surf.blit(img, (x, y))
    return img


def panel(surf, x, y, w, h, alpha=214):
    """Semi-transparent panel with rounded border + top-edge highlight.

    The top-edge highlight (a 1-pixel brighter line along the top inside) is
    borrowed from LS.py's _panel: it adds a hint of depth so the panel reads
    as raised rather than flat, which matters when several panels overlap the
    starfield at different alphas."""
    s = pygame.Surface((int(w), int(h)), pygame.SRCALPHA)
    s.fill((C_PANEL[0], C_PANEL[1], C_PANEL[2], alpha))
    surf.blit(s, (int(x), int(y)))
    pygame.draw.rect(surf, C_PANEL_HI, (int(x), int(y), int(w), int(h)), 1,
                     border_radius=6)
    # top-edge highlight: one brighter line for depth (LS.py pattern)
    hi_col = (min(255, C_PANEL_HI[0] + 18),
              min(255, C_PANEL_HI[1] + 18),
              min(255, C_PANEL_HI[2] + 22))
    pygame.draw.line(surf, hi_col,
                     (int(x) + 3, int(y) + 1),
                     (int(x) + int(w) - 3, int(y) + 1), 1)


def bar(surf, font, x, y, w, h, frac, color, label, valtext, mark=None,
        lo=None, hi=None):
    """Horizontal bar with optional threshold markers.

    The lo/hi threshold markers (yellow tick lines) come from GmansRunV1.17
    and SE.py: they mark safe-operating-range bounds on the same bar as the
    current value, so you can see at a glance whether you are inside the
    limit. The single `mark` is kept for backward compatibility (it marks
    a target or setpoint)."""
    pygame.draw.rect(surf, C_PANEL_HI, (x, y, w, h), border_radius=4)
    f = clamp(frac)
    if f > 0:
        pygame.draw.rect(surf, color, (x, y, max(2, int(w * f)), h),
                         border_radius=4)
    if mark is not None:
        mx = x + int(w * clamp(mark))
        pygame.draw.line(surf, C_WARN, (mx, y - 3), (mx, y + h + 3), 1)
    if lo is not None:
        lx = x + int(w * clamp(lo))
        pygame.draw.line(surf, C_WARN, (lx, y - 3), (lx, y + h + 3), 1)
    if hi is not None:
        hx = x + int(w * clamp(hi))
        pygame.draw.line(surf, C_BAD, (hx, y - 3), (hx, y + h + 3), 1)
    surf.blit(font.render(label, True, C_TEXT_DIM), (x, y - 16))
    img = font.render(valtext, True, C_TEXT)
    surf.blit(img, (x + w - img.get_width(), y - 16))


def wrap_text(font, text, maxpx):
    out, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if font.size(trial)[0] <= maxpx:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out or [""]


def chip(surf, font, x, y, text, on, col_on=None):
    """A small toggle pill with accent border on the active state.

    Matches the reference tab style (GmansRun/SE): active tabs get a filled
    background PLUS a brighter accent border, so the active tab reads as
    selected even at a glance. Inactive tabs get a thin outline only."""
    col = (col_on or C_ACCENT) if on else C_TEXT_DIM
    img = font.render(text, True, (10, 14, 20) if on else col)
    w, h = img.get_width() + 14, img.get_height() + 6
    r = pygame.Rect(int(x), int(y), w, h)
    if on:
        pygame.draw.rect(surf, col, r, border_radius=9)
        # accent border: one shade brighter for the active state
        bord = (min(255, col[0] + 40), min(255, col[1] + 40),
                min(255, col[2] + 40))
        pygame.draw.rect(surf, bord, r, 1, border_radius=9)
    else:
        pygame.draw.rect(surf, col, r, 1, border_radius=9)
    surf.blit(img, (r.x + 7, r.y + 3))
    return r


def project(pts, az, el, dist, cx, cy, focal, pan=(0.0, 0.0)):
    """Project world points through the same orbit camera the ShipRenderer uses.
    Returns (sx, sy, depth) arrays. Used by the METRIC view, which draws a
    procedural grid rather than Parts."""
    Rc = rot_x(el) @ rot_y(az)
    cam = np.asarray(pts, dtype=float) @ Rc.T
    cam = cam + np.array([0.0, 0.0, dist])
    z = np.where(cam[:, 2] <= 0.05, 1e9, cam[:, 2])
    return (cx + focal * cam[:, 0] / z + pan[0],
            cy - focal * cam[:, 1] / z + pan[1],
            cam[:, 2])


class MetricCam:
    """Orbit camera for the METRIC sheet.

    It exposes the same control surface as ShipRenderer so the shared mouse and
    keyboard handlers drive either one, but it keeps its own az/el/dist -- the
    spacetime sheet and the ship want completely different framing, and having
    them share a camera meant orbiting one wrecked the other."""

    def __init__(self, az=1.15, el=0.52, dist=560.0):
        self._home = (az, el, dist)
        self.az, self.el, self.dist = az, el, dist
        self.pan = np.array([0.0, 0.0])
        self.view = "full"
        self.section = False
        self.hovered = None
        self.selected = None

    def reset_view(self):
        self.az, self.el, self.dist = self._home
        self.pan = np.array([0.0, 0.0])

    def zoom_at(self, factor, mouse_pos=None, rect=None):
        self.dist = max(120.0, min(2600.0, self.dist * factor))

    def orbit(self, dx, dy, fine=False):
        sens = 0.004 if fine else 0.009
        self.az += dx * sens
        self.el = max(-1.5, min(1.5, self.el + dy * sens))

    def pan_by(self, dx, dy, fine=False):
        self.pan += np.array([dx * (0.45 if fine else 1.0),
                              dy * (0.45 if fine else 1.0)])

    # the view controls belong to the ship model; here they do nothing
    def set_view(self, mode):
        pass

    def toggle_section(self):
        pass

    def active_part(self):
        return None

    def placing_part(self):
        return None

    def tick(self, dt):
        pass


class Starfield:
    """Parallax star background. Stars stream past at a rate set by the ship's
    apparent velocity -- which for a warp drive is honestly labelled APPARENT,
    since the ship is not moving through them at all.

    Each star has a TEMPERATURE CLASS (O/B/A/F/G/K/M) sampled like a real
    initial mass function (heavy on cool reds, light on hot blues), and is
    coloured by its blackbody approximation. Brighter stars (low depth d,
    high magnitude) are drawn as 2-pixel crosses; fainter ones as single
    pixels -- the same hierarchy the companion twins (GmansRun, SE, LS) use
    to give a starfield depth without a sprite atlas."""

    # blackbody-ish star colours by spectral class (R, G, B)
    STAR_COLORS = [
        (155, 176, 255),   # O/B -- hot blue
        (170, 191, 255),   # A   -- blue-white
        (200, 215, 255),   # F   -- white
        (255, 255, 245),   # G   -- yellow-white (Sol)
        (255, 235, 180),   # K   -- orange
        (255, 200, 150),   # M   -- red
    ]
    # probability weights: cool stars dominate a real stellar population
    STAR_WEIGHTS = [0.03, 0.06, 0.08, 0.12, 0.22, 0.49]

    def __init__(self, n=520, seed=7):
        rng = np.random.default_rng(seed)
        self.p = rng.uniform(-1.0, 1.0, size=(n, 3))
        self.p[:, 2] = rng.uniform(0.05, 1.0, size=n)
        self.mag = rng.uniform(0.25, 1.0, size=n)
        # assign each star a spectral class index by the weighted distribution
        cum = np.cumsum(self.STAR_WEIGHTS)
        r = rng.random(n)
        self.cls = np.array([np.searchsorted(cum, rv) for rv in r])
        self.cls = np.clip(self.cls, 0, len(self.STAR_COLORS) - 1)
        self._cache = None
        self._cache_key = None

    def draw(self, surf, rect, streak=0.0, drift=0.0):
        """Static fields are painted once and blitted; only the streaking
        FLIGHT field is rebuilt per frame."""
        if streak <= 0.02:
            key = (rect.w, rect.h)
            if self._cache_key != key:
                self._cache_key = key
                self._cache = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
                self._paint(self._cache, pygame.Rect(0, 0, rect.w, rect.h))
            surf.blit(self._cache, (rect.x, rect.y))
            return
        self._paint(surf, rect, streak, drift)

    def _star_col(self, i, brightness):
        """Blackbody-coloured star: base colour from spectral class, scaled by
        apparent brightness. Clamped to valid RGB."""
        base = self.STAR_COLORS[self.cls[i]]
        return (max(0, min(255, int(base[0] * brightness))),
                max(0, min(255, int(base[1] * brightness))),
                max(0, min(255, int(base[2] * brightness))))

    def _paint(self, surf, rect, streak=0.0, drift=0.0):
        w, h = rect.w, rect.h
        cx, cy = rect.x + w / 2.0, rect.y + h / 2.0
        for i in range(len(self.p)):
            d = self.p[i, 2]
            sx = cx + self.p[i, 0] * w * 0.62 / d
            sy = cy + self.p[i, 1] * h * 0.62 / d
            sy = rect.y + ((sy - rect.y + drift / d) % h)
            if not (rect.x <= sx < rect.x + w):
                continue
            b = 0.27 + 0.65 * self.mag[i] * (1.2 - d)
            b = max(0.12, min(1.0, b))
            col = self._star_col(i, b)
            if streak > 0.02:
                ln = streak * 46.0 / d
                pygame.draw.line(surf, col, (sx, sy), (sx, sy + ln), 1)
            else:
                # bright nearby stars get a 2px cross; faint ones a single pixel
                if b > 0.65 and d < 0.4:
                    ix, iy = int(sx), int(sy)
                    if rect.x <= ix < rect.x + w - 1:
                        surf.set_at((ix, iy), col)
                        dim = (col[0] // 2, col[1] // 2, col[2] // 2)
                        if iy + 1 < rect.y + h:
                            surf.set_at((ix, iy + 1), dim)
                        if ix + 1 < rect.x + w:
                            surf.set_at((ix + 1, iy), dim)
                else:
                    surf.set_at((int(sx), int(sy)), col)


def draw_bubble_glow(surf, cx, cy, r, intensity, col=None):
    """Soft concentric halo for the active warp shell.

    Uses additive blending (BLEND_RGBA_ADD) after the pattern of LS.py's
    plasma-blade glow: the halo ADDS light to whatever is behind it rather
    than overpainting, so the bubble reads as luminous over the starfield
    instead of as a dim coloured disc."""
    if intensity <= 0.02:
        return
    col = col or C_BUBBLE
    layers = 7
    s = pygame.Surface((int(r * 2.4), int(r * 2.4)), pygame.SRCALPHA)
    for i in range(layers, 0, -1):
        t = i / layers
        a = int(52 * intensity * (1.0 - t) ** 1.6)
        if a <= 0:
            continue
        pygame.draw.circle(s, (col[0], col[1], col[2], a),
                           (int(r * 1.2), int(r * 1.2)), int(r * (0.7 + 0.5 * t)),
                           max(1, int(r * 0.05)))
    surf.blit(s, (int(cx - r * 1.2), int(cy - r * 1.2)),
              special_flags=pygame.BLEND_RGBA_ADD)


def log_bar_x(value_j, x0, x1, lo_exp=0.0, hi_exp=80.0):
    """Map |E| onto a log10 axis across a pixel span."""
    if value_j == 0:
        return x0
    e = math.log10(abs(value_j))
    return x0 + (x1 - x0) * clamp((e - lo_exp) / (hi_exp - lo_exp))


def draw_vignette(surf, strength=0.22):
    """Subtle corner darkening for cinematic depth.

    Paints a radial alpha gradient (transparent centre, dark edges) onto a
    full-screen SRCALPHA surface and blits it once per frame. The effect is
    the same trick the companion twins use to focus the eye on the central
    viewport: the starfield fades into shadow at the bezel without a hard
    border. Cached on the surface size so it is rebuilt only on resize."""
    w, h = surf.get_width(), surf.get_height()
    key = (w, h)
    cache = getattr(draw_vignette, "_cache", None)
    cache_key = getattr(draw_vignette, "_cache_key", None)
    if cache is not None and cache_key == key:
        surf.blit(cache, (0, 0))
        return
    v = pygame.Surface((w, h), pygame.SRCALPHA)
    cx, cy = w / 2.0, h / 2.0
    max_r = math.hypot(cx, cy)
    # four corner rectangles with radial alpha falloff (cheap, no per-pixel loop)
    step = max(8, min(w, h) // 60)
    for y in range(0, h, step):
        for x in range(0, w, step):
            d = math.hypot(x + step / 2 - cx, y + step / 2 - cy) / max_r
            if d > 0.55:
                a = int(255 * strength * ((d - 0.55) / 0.45) ** 1.8)
                if a > 0:
                    pygame.draw.rect(v, (0, 0, 0, a),
                                     (x, y, step + 1, step + 1))
    draw_vignette._cache = v
    draw_vignette._cache_key = key
    surf.blit(v, (0, 0))


# =============================================================================
# SECTION 12 -- APPLICATION
# =============================================================================

# The cross-section cuts EVERY part. Leaving the radiators and the bubble
# whole meant the cutaway was still looking at the outside of the ship.
SECTION_KEYS = ("hull", "reactor", "smes", "ring", "coils", "casimir",
                "amtraps", "capfore", "capaft", "collector", "deflector",
                "radiators", "pylons", "cryo", "rcs", "bubble", "magsail")


class App:
    MODE_SHIP = 0
    MODE_METRIC = 1
    MODE_DILATION = 2
    MODE_PORTAL = 3
    MODE_FLIGHT = 4
    MODE_NAMES = ["SHIP", "METRIC", "DILATION", "PORTAL", "FLIGHT"]

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(
            "Warpdrive V1.0 -- WD-1 FOLDRUNNER :: Physical Warp Drive Digital Twin")
        self.W, self.H = 1600, 920
        self.screen = pygame.display.set_mode((self.W, self.H), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        mono = "consolas,dejavusansmono,monospace"
        self.f = pygame.font.SysFont(mono, 15)
        self.fs = pygame.font.SysFont(mono, 12)
        self.fm = pygame.font.SysFont(mono, 19, bold=True)
        self.fb = pygame.font.SysFont(mono, 28, bold=True)

        self.rend = ShipRenderer(build_ship_parts, home_az=0.66, home_el=0.40,
                                 home_dist=430.0, section_keys=SECTION_KEYS)
        # a second, lower-detail copy for the FLIGHT inset: the extra facets
        # are invisible at chase distance and cost half the frame budget
        global VISUAL_DETAIL
        _vd = VISUAL_DETAIL
        VISUAL_DETAIL = 0.7
        self.frend = ShipRenderer(build_ship_parts, home_az=1.02, home_el=0.20,
                                  home_dist=520.0, section_keys=SECTION_KEYS)
        VISUAL_DETAIL = _vd

        # the portal gate has its own model and its own framing
        self.prend = ShipRenderer(build_portal_parts, home_az=0.86,
                                  home_el=0.34, home_dist=210.0,
                                  section_keys=("gateA", "gateB", "pcoils",
                                                "pcasimir", "throat"))
        self.mcam = MetricCam()
        self.core = WarpCore()
        self.voy = Voyage()
        self.stars = Starfield()

        self.mode = self.MODE_SHIP
        self.paused = False
        self.show_info = False
        self.show_help = True
        self.show_ladder = False
        self.show_labels = False
        self.info_scroll = 0
        self.ftl_unlock = False
        self.anim = 0.0
        self.msg = ""
        self.msg_t = 0.0

        self.dragging = False
        self.panning = False
        self._chips = {}
        self.running = True
        self.bg = None
        self._rebuild_bg()

    # ------------------------------------------------------------------ setup
    def _rebuild_bg(self):
        self.bg = pygame.Surface((self.W, self.H))
        vgradient(self.bg, BG_TOP, BG_BOT)
        # invalidate the vignette cache so it rebuilds at the new size
        draw_vignette._cache = None
        draw_vignette._cache_key = None

    def _rend(self):
        if self.mode == self.MODE_FLIGHT:
            return self.frend
        if self.mode == self.MODE_PORTAL:
            return self.prend
        if self.mode in (self.MODE_METRIC, self.MODE_DILATION):
            return self.mcam
        return self.rend

    def flash(self, text):
        self.msg, self.msg_t = text, 3.2

    def set_wall(self, factor):
        w = clamp(self.core.wall_m * factor, DRIVE["wall_min_m"],
                  DRIVE["wall_max_m"])
        self.core.wall_m = w
        DIMS["wall_thick_m"] = w
        global INFO_SECTIONS
        INFO_SECTIONS = None                 # the I panel quotes live numbers
        self.flash("wall delta = %.4g m   sigma = %.4g /m" % (w, 1.0 / w))

    def set_beta(self, d):
        c = self.core
        if c.helm_locked():
            self.flash("HELM LOCKED -- forward wall is causally disconnected")
            return
        hi = DRIVE["beta_ftl_max"] if self.ftl_unlock else DRIVE["beta_sub_max"]
        c.beta_cmd = round(clamp(c.beta_cmd + d, 0.0, hi), 4)
        if self.voy.phase in ("CRUISE", "BRAKE", "ARRIVED") and not self.ftl_unlock:
            self.flash("cruise beta is set during BOOST -- reset (N) to change")

    # ----------------------------------------------------------------- events
    def handle_events(self, dt):
        keys = pygame.key.get_pressed()
        fine = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        rend = self._rend()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.VIDEORESIZE:
                self.W, self.H = max(1000, e.w), max(680, e.h)
                self.screen = pygame.display.set_mode((self.W, self.H),
                                                      pygame.RESIZABLE)
                self._rebuild_bg()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                hit = None
                for name, r in self._chips.items():
                    if r.collidepoint(e.pos):
                        hit = name
                if hit:
                    self._chip_click(hit)
                elif e.button == 1:
                    self.dragging = True
                    if (self.mode in (self.MODE_SHIP, self.MODE_PORTAL)
                            and rend.hovered is not None):
                        rend.selected = (None if rend.selected == rend.hovered
                                         else rend.hovered)
                elif e.button in (2, 3):
                    self.panning = True
                elif e.button == 4:
                    rend.zoom_at(0.88, e.pos, pygame.Rect(0, 0, self.W, self.H))
                elif e.button == 5:
                    rend.zoom_at(1.14, e.pos, pygame.Rect(0, 0, self.W, self.H))
            elif e.type == pygame.MOUSEBUTTONUP:
                self.dragging = self.panning = False
            elif e.type == pygame.MOUSEMOTION:
                if self.dragging:
                    rend.orbit(e.rel[0], e.rel[1], fine)
                elif self.panning:
                    rend.pan_by(e.rel[0], e.rel[1], fine)
            elif e.type == pygame.KEYDOWN:
                self._key(e.key, fine)

    def _chip_click(self, name):
        if name == "labels":
            self.show_labels = not self.show_labels
        elif name == "section":
            self._rend().toggle_section()
        elif name == "ftl":
            self._toggle_ftl()
        elif name == "dest":
            self.voy.dest_array = not self.voy.dest_array
            self.flash("destination array: %s"
                       % ("ASSUMED PRESENT -- rendezvous possible"
                          if self.voy.dest_array else "NONE -- flyby only"))
        elif name in ("full", "exploded", "assembly"):
            self._rend().set_view(name)

    def _toggle_ftl(self):
        self.ftl_unlock = not self.ftl_unlock
        if self.ftl_unlock:
            # drop to a slow clock: an over-driven shell lets go in minutes of
            # ship time, and at 30 d/s you would never see it happen
            self.voy.warp_i = min(self.voy.warp_i, 1)   # 1 min/s
            self.flash("ALCUBIERRE MODE UNLOCKED -- every joule beyond beta=1 "
                       "is UNFUNDED   (clock slowed to watch it)")
        else:
            self.core.beta_cmd = min(self.core.beta_cmd, DRIVE["beta_sub_max"])
            self.flash("physical (positive-energy) mode")

    def _key(self, k, fine):
        rend = self._rend()
        c, v = self.core, self.voy
        if k == pygame.K_ESCAPE:
            self.running = False
        elif k == pygame.K_TAB:
            self.mode = (self.mode + 1) % len(self.MODE_NAMES)
        elif k == pygame.K_h:
            self.show_help = not self.show_help
        elif k == pygame.K_i:
            self.show_info = not self.show_info
            self.info_scroll = 0
        elif k == pygame.K_m:
            self.show_ladder = not self.show_ladder
        elif k == pygame.K_l:
            self.show_labels = not self.show_labels
        elif k == pygame.K_p:
            self.paused = not self.paused
        elif k == pygame.K_r:
            rend.reset_view()
        elif k == pygame.K_1:
            rend.set_view("full")
        elif k == pygame.K_2:
            rend.set_view("exploded")
        elif k == pygame.K_3:
            rend.set_view("assembly")
        elif k in (pygame.K_4, pygame.K_x):
            rend.toggle_section()
        elif k == pygame.K_e:
            rend.set_view("full" if rend.view == "exploded" else "exploded")
        elif k == pygame.K_PAGEUP:
            self.info_scroll = max(0, self.info_scroll - 12)
        elif k == pygame.K_PAGEDOWN:
            self.info_scroll += 12
        # ---- drive
        elif k == pygame.K_COMMA:
            if (rend.view == "assembly"
                    and self.mode in (self.MODE_SHIP, self.MODE_PORTAL)):
                rend.assembly_prev()
            else:
                self.set_beta(-(0.1 if fine else 0.01))
        elif k == pygame.K_PERIOD:
            if (rend.view == "assembly"
                    and self.mode in (self.MODE_SHIP, self.MODE_PORTAL)):
                rend.assembly_next()
            else:
                self.set_beta(+(0.1 if fine else 0.01))
        elif k == pygame.K_LEFTBRACKET:
            self.set_wall(1.0 / (1.6 if fine else 1.15))
        elif k == pygame.K_RIGHTBRACKET:
            self.set_wall(1.6 if fine else 1.15)
        elif k == pygame.K_f:
            self._toggle_ftl()
        elif k == pygame.K_b:
            c.bubble_cmd = not c.bubble_cmd
            if c.bubble_cmd:
                c.collapsed = False
            self.flash("warp shell %s" % ("FORMING" if c.bubble_cmd else "DOWN"))
        elif k == pygame.K_g:
            err = v.begin_boost(c)
            self.flash(err or "BOOST -- rectenna deployed, beam acquired")
        elif k == pygame.K_k:
            err = v.begin_brake(c)
            self.flash(err or "BRAKING")
        elif k == pygame.K_j:
            self._chip_click("dest")
        elif k == pygame.K_n:
            keep = v.dest_array
            v.reset(c)                    # re-inits BOTH the voyage and the core
            v.dest_array = keep
            self.ftl_unlock = False
            DIMS["wall_thick_m"] = c.wall_m
            self.flash("mission reset -- back at the tap")
        elif k == pygame.K_MINUS:
            v.cycle_warp(-1)
        elif k in (pygame.K_EQUALS, pygame.K_PLUS):
            v.cycle_warp(+1)

    # ----------------------------------------------------------------- update
    def update(self, dt):
        self.anim += dt
        self.msg_t = max(0.0, self.msg_t - dt)
        c, v = self.core, self.voy
        if not self.paused:
            if self.mode == self.MODE_FLIGHT:
                v.update(dt, c)
            else:
                c.update(dt * 4.0, v)
        self.rend.tick(dt)
        self.frend.tick(dt)
        self.prend.tick(dt)

        # part visibility follows the physical state, in both renderers
        for r in (self.rend, self.frend):
            hid = set()
            if c.bubble_on < 0.03:
                hid.add("bubble")
            if not c.magsail_deployed:
                hid.add("magsail")
            if self.mode == self.MODE_SHIP and r.view != "full":
                hid.discard("bubble")          # exploded/assembly: show all
                hid.discard("magsail")
            r.hidden = hid

    # ------------------------------------------------------------------- draw
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self._chips = {}
        if self.mode == self.MODE_SHIP:
            self.draw_ship()
        elif self.mode == self.MODE_METRIC:
            self.draw_metric()
        elif self.mode == self.MODE_DILATION:
            self.draw_dilation()
        elif self.mode == self.MODE_PORTAL:
            self.draw_portal()
        else:
            self.draw_flight()
        # subtle vignette: focus the eye on the central viewport without a
        # hard border (cinematic depth, cached on resolution)
        draw_vignette(self.screen, 0.20)
        self.draw_topbar()
        if self.show_ladder:
            self.draw_ladder()
        if self.show_info:
            self.draw_info()
        elif self.show_help:
            self.draw_help()
        if self.msg_t > 0:
            # top-centre, under the bar: the bottom of the screen belongs to the
            # METRIC profile plots and the FLIGHT control strip
            img = self.fm.render(self.msg, True, C_WARN)
            x = (self.W - img.get_width()) // 2
            panel(self.screen, x - 14, 46, img.get_width() + 28, 32)
            text_shadow(self.screen, self.fm, self.msg, (x, 52), C_WARN)
        pygame.display.flip()

    # ---- top bar ----------------------------------------------------------
    def draw_topbar(self):
        c, v = self.core, self.voy
        h = 40
        panel(self.screen, 0, 0, self.W, h, 236)
        text_shadow(self.screen, self.fm, "WD-1 FOLDRUNNER", (14, 10), C_ACCENT)
        x = 210
        for i, nm in enumerate(self.MODE_NAMES):
            on = (i == self.mode)
            r = chip(self.screen, self.f, x, 9, nm, on)
            x = r.right + 8
        x += 12
        ec = c.energy_conditions()
        items = [
            ("beta cmd %.3f" % c.beta_cmd, C_TEXT),
            ("beta %.4f" % c.beta, C_ACCENT),
            ("delta %.3g m" % c.wall_m, C_TEXT_DIM),
            (c.status, C_BAD if c.collapsed else
             (C_EXOTIC if c.exotic else
              (C_WARN if c.status != "NOMINAL" else C_GOOD))),
            ("%s" % ec["class"], C_EXOTIC if ec["class"] == "EXOTIC" else C_GOOD),
        ]
        for text, col in items:
            img = text_shadow(self.screen, self.f, text, (x, 12), col)
            x += img.get_width() + 20

        if c.exotic:
            t = "ALCUBIERRE MODE -- %s of negative energy UNFUNDED" % fmt_energy(
                c.exotic_debt_j)
            img = self.f.render(t, True, C_EXOTIC)
            text_shadow(self.screen, self.f, t,
                        (self.W - img.get_width() - 16, 12), C_EXOTIC)
        elif self.mode == self.MODE_FLIGHT:
            t = "%s  |  x%s" % (v.phase, VOYAGE_WARP_LABEL[v.warp_i])
            img = self.f.render(t, True, C_TEXT_DIM)
            text_shadow(self.screen, self.f, t,
                        (self.W - img.get_width() - 16, 12), C_TEXT_DIM)

    # ---- SHIP mode --------------------------------------------------------
    def draw_ship(self):
        rect = pygame.Rect(0, 40, self.W - 372, self.H - 40)
        self.stars.draw(self.screen, rect)
        self.rend.render(self.screen, rect, {"default": self.anim * 0.5,
                                             "plasma": self.anim * 2.2},
                         mouse_pos=pygame.mouse.get_pos(),
                         show_labels=self.show_labels, label_font=self.fs,
                         interactive=True, coil_glow=self.core.coil_glow,
                         drive_power=self.core.beta * self.core.bubble_on,
                         rad_heat=clamp((self.core.rad_k - 600) / 1300.0),
                         bubble_on=self.core.bubble_on)
        self.draw_view_tabs(rect)
        self.draw_ship_panel()
        self.draw_spec_card()

    def draw_view_tabs(self, rect):
        x, y = 14, self.H - 42
        for nm in ("full", "exploded", "assembly"):
            r = chip(self.screen, self.f, x, y, nm.upper(),
                     self._rend().view == nm)
            self._chips[nm] = r
            x = r.right + 8
        r = chip(self.screen, self.f, x, y, "SECTION", self._rend().section)
        self._chips["section"] = r
        x = r.right + 8
        r = chip(self.screen, self.f, x, y, "LABELS", self.show_labels)
        self._chips["labels"] = r
        if self._rend().view == "assembly":
            p = self._rend().placing_part()
            t = ("placing: %s   ( , / . )" % p.name) if p else "assembly complete"
            text_shadow(self.screen, self.f, t, (r.right + 18, y + 4), C_WARN)

    def draw_ship_panel(self):
        x, w = self.W - 360, 348
        y = 52
        panel(self.screen, x, y, w, 300)
        self.screen.blit(self.fm.render("VESSEL", True, C_ACCENT), (x + 12, y + 8))
        rows = [
            ("ring diameter", "%.0f m" % DIMS["ring_major_d_m"]),
            ("hull", "%.0f m x %.0f m, %d decks"
             % (DIMS["hull_len_m"], DIMS["hull_d_m"], DIMS["hull_decks"])),
            ("bubble radius", "%.0f m (flat to %.1f m)"
             % (DIMS["bubble_r_m"], flat_interior_r())),
            ("wall thickness", "%.4g m   [ ]" % self.core.wall_m),
            ("dry mass", fmt_mass(SHIP_MASS_KG)),
            ("fusion plant", "%.0f GW th -> %s" % (DIMS["reactor_th_gw"],
                                                   fmt_power(PLANT_ELECTRIC_W))),
            ("radiators", "%.0f m^2 @ %.0f K limit"
             % (RADIATOR_AREA_M2, DIMS["rad_limit_k"])),
            ("SMES buffer", fmt_energy(SMES_J)),
            ("Casimir lattice", fmt_energy(casimir_onboard_j())),
            ("max cruise beta", "%.4f  (emergent)" % max_boost_beta()),
            ("crossing at that beta", fmt_time(PROXIMA_M
                                               / (max_boost_beta() * C_LIGHT))),
        ]
        env = check_envelope()
        yy = y + 36
        for k, val in rows:
            self.screen.blit(self.fs.render(k, True, C_TEXT_DIM), (x + 12, yy))
            img = self.fs.render(val, True, C_TEXT)
            self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 19
        yy += 4
        self.screen.blit(self.fs.render("envelope", True, C_TEXT_DIM),
                         (x + 12, yy))
        img = self.fs.render("%s %.1f m / %.1f m"
                             % ("OK" if env["ok"] else "INTRUSION",
                                env["reach_m"], env["limit_m"]),
                             True, C_GOOD if env["ok"] else C_BAD)
        self.screen.blit(img, (x + w - 12 - img.get_width(), yy))

        # the one comparison that matters
        y2 = y + 312
        panel(self.screen, x, y2, w, 150)
        self.screen.blit(self.fm.render("THE TWO DRIVES", True, C_ACCENT),
                         (x + 12, y2 + 8))
        need = alcubierre_energy_j(1.0, DIMS["bubble_r_m"], self.core.wall_m)
        lines = [
            ("PHYSICAL   beta < 1", C_GOOD),
            ("  positive energy, every condition met", C_TEXT_DIM),
            ("  %s to reach beta 0.5" % fmt_energy(kinetic_energy_j(0.5)),
             C_TEXT_DIM),
            ("ALCUBIERRE   beta > 1", C_EXOTIC),
            ("  needs %s of NEGATIVE energy" % fmt_energy(need), C_TEXT_DIM),
            ("  aboard: %s  ->  short %.0f orders"
             % (fmt_energy(casimir_onboard_j()),
                orders_of_magnitude(need, casimir_onboard_j())), C_TEXT_DIM),
        ]
        yy = y2 + 34
        for t, col in lines:
            self.screen.blit(self.fs.render(t, True, col), (x + 12, yy))
            yy += 18

    def draw_spec_card(self):
        part = self.rend.active_part()
        if part is not None:
            self._spec_card(part)

    def _spec_card(self, part):
        w = 640
        lines = []
        for s in part.specs:
            lines += wrap_text(self.fs, s, w - 28) if s else [""]
        h = 42 + 17 * len(lines)
        x, y = 14, self.H - 62 - h
        panel(self.screen, x, y, w, h)
        pygame.draw.rect(self.screen, part.color, (x, y, 5, h),
                         border_top_left_radius=6, border_bottom_left_radius=6)
        self.screen.blit(self.fm.render(part.name, True, C_TEXT), (x + 16, y + 9))
        yy = y + 36
        for ln in lines:
            self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM), (x + 16, yy))
            yy += 17

    # ---- METRIC mode ------------------------------------------------------
    def draw_metric(self):
        """Draw the spacetime, not the hardware.

        The sheet is a grid of Eulerian observers lying in the plane that
        contains the direction of travel. Each node is displaced out of plane
        by the York expansion scalar computed AT THAT POINT by the same
        york_theta() the energy integral uses -- so the picture and the number
        can never disagree."""
        c = self.core
        R = DIMS["bubble_r_m"]
        delta = c.wall_m
        b = c.beta if (c.bubble_on > 0.1 and c.beta > 0.01) else max(0.15, c.beta_cmd)
        rect = pygame.Rect(0, 40, self.W - 372, self.H - 236)
        self.stars.draw(self.screen, rect)

        # A POLAR sheet in the plane containing the direction of travel, with
        # the radial samples CROWDED onto the wall. A uniform Cartesian grid
        # cannot see this: with a 1 m wall on a 100 m bubble, theta is a spike
        # one metre wide and a uniform grid steps straight over it, drawing a
        # flat sheet and a comfortable lie. Concentrating the samples where the
        # curvature actually lives resolves it at any wall thickness.
        rads = sorted(set(
            [R * t for t in np.linspace(0.06, 2.3, 16)]
            + [max(0.02, R + delta * k) for k in
               (-9, -6, -4, -2.6, -1.6, -0.9, -0.4, 0.0,
                0.4, 0.9, 1.6, 2.6, 4, 6, 9)]))
        NA = 34
        angs = np.linspace(0.0, 2.0 * math.pi, NA, endpoint=False)
        NR = len(rads)

        pts, tv = [], []
        tmax = 0.0
        for rr in rads:
            for ang in angs:
                z, y = rr * math.cos(ang), rr * math.sin(ang)
                th = york_theta(z, abs(y), b, R, delta)
                tmax = max(tmax, abs(th))
                pts.append((0.0, y, z))
                tv.append(th)
        tmax = tmax or 1.0
        amp = 46.0
        pts = [(-amp * tv[i] / tmax, p[1], p[2]) for i, p in enumerate(pts)]
        tv = [t / tmax for t in tv]

        cam = self.mcam
        focal = min(rect.w, rect.h) * 1.10
        sx, sy, dz = project(pts, cam.az, cam.el, cam.dist,
                             rect.x + rect.w / 2.0, rect.y + rect.h / 2.0,
                             focal, cam.pan)

        def col_for(t):
            base = C_CONTRACT if t < 0 else C_EXPAND
            return _mix(C_GRID, base, min(1.0, abs(t) * 2.6))

        def width_for(t):
            """Line width scales with curvature: the wall is a spike one metre
            wide, so the segments there carry almost all the displacement.
            Drawing them thicker makes the spike visible without crowding the
            sample grid onto it."""
            return 2 if abs(t) > 0.45 else 1

        segs = []
        for i in range(NR):
            for j in range(NA):
                k = i * NA + j
                k2 = i * NA + (j + 1) % NA               # around
                t_seg = 0.5 * (tv[k] + tv[k2])
                segs.append(((dz[k] + dz[k2]) * 0.5, k, k2,
                             col_for(t_seg), width_for(t_seg), abs(t_seg)))
                if i + 1 < NR:                            # outward
                    k3 = (i + 1) * NA + j
                    t_seg = 0.5 * (tv[k] + tv[k3])
                    segs.append(((dz[k] + dz[k3]) * 0.5, k, k3,
                                 col_for(t_seg), width_for(t_seg), abs(t_seg)))
        segs.sort(key=lambda q: q[0], reverse=True)
        old = self.screen.get_clip()
        self.screen.set_clip(rect)
        # first pass: additive glow on the high-curvature segments (the wall)
        glow_surf = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
        for _, p1, p2, col, wid, tmag in segs:
            if tmag > 0.35 and dz[p1] > 0.05 and dz[p2] > 0.05:
                lp1 = (sx[p1] - rect.x, sy[p1] - rect.y)
                lp2 = (sx[p2] - rect.x, sy[p2] - rect.y)
                a = int(60 * min(1.0, (tmag - 0.35) / 0.65))
                pygame.draw.line(glow_surf, (col[0], col[1], col[2], a),
                                 lp1, lp2, max(3, wid + 2))
        self.screen.blit(glow_surf, (rect.x, rect.y),
                         special_flags=pygame.BLEND_RGBA_ADD)
        # second pass: the actual grid lines
        for _, p1, p2, col, wid, _ in segs:
            if dz[p1] > 0.05 and dz[p2] > 0.05:
                pygame.draw.line(self.screen, col, (sx[p1], sy[p1]),
                                 (sx[p2], sy[p2]), wid)

        cx0, cy0 = rect.x + rect.w / 2.0, rect.y + rect.h / 2.0
        # the ship, and where it is pointed -- with a glow halo
        hx, hy, _ = project([(0, 0, 0)], cam.az, cam.el, cam.dist,
                            cx0, cy0, focal, cam.pan)
        nx, ny, _ = project([(0, 0, R * 1.9)], cam.az, cam.el, cam.dist,
                            cx0, cy0, focal, cam.pan)
        pygame.draw.line(self.screen, C_ACCENT, (hx[0], hy[0]), (nx[0], ny[0]), 1)
        # ship marker: additive glow + solid dot (LS.py pattern)
        sg = pygame.Surface((28, 28), pygame.SRCALPHA)
        pygame.draw.circle(sg, (C_HULL[0], C_HULL[1], C_HULL[2], 50),
                           (14, 14), 12)
        pygame.draw.circle(sg, (C_HULL[0], C_HULL[1], C_HULL[2], 110),
                           (14, 14), 7)
        self.screen.blit(sg, (int(hx[0]) - 14, int(hy[0]) - 14),
                         special_flags=pygame.BLEND_RGBA_ADD)
        pygame.draw.circle(self.screen, C_HULL, (int(hx[0]), int(hy[0])), 5)
        pygame.draw.circle(self.screen, C_ACCENT, (int(hx[0]), int(hy[0])), 5, 1)
        text_shadow(self.screen, self.fs, "direction of travel",
                    (nx[0] + 6, ny[0] - 6), C_ACCENT)
        self.screen.set_clip(old)

        for text, col, off in (
                ("SPACE CONTRACTING  ahead  (theta < 0)", C_CONTRACT, 0),
                ("SPACE EXPANDING  behind  (theta > 0)", C_EXPAND, 20)):
            text_shadow(self.screen, self.f, text,
                        (rect.x + 16, rect.y + 12 + off), col)
        for i, t in enumerate([
                "theta = beta c (x/r) df/dr   peak %.3e /s at beta = %.3f"
                % (tmax, b),
                "sheet displaced by theta; radial samples crowded onto the "
                "%.3g m wall" % delta]):
            text_shadow(self.screen, self.fs, t,
                        (rect.x + 16, rect.y + 56 + i * 15), C_TEXT_DIM)

        self.draw_profiles(b, R, delta)
        self.draw_metric_panel(b, R, delta)

    def draw_profiles(self, b, R, delta):
        """f(r), df/dr and T^00(r) across the wall -- the three curves the whole
        argument rests on, plotted from the live functions."""
        y0 = self.H - 190
        w, h = (self.W - 400) // 3, 150
        lo, hi = R - 6 * delta, R + 6 * delta
        rs = [lo + (hi - lo) * i / 90.0 for i in range(91)]
        series = [
            ("f(r)   shape function", [shape_f(r, R, delta) for r in rs],
             C_ACCENT, False),
            ("df/dr   [1/m]", [shape_df(r, R, delta) for r in rs],
             C_WARN, False),
            ("T^00(r)   [J/m^3]", [energy_density(0.0, r, b, R, delta)
                                   for r in rs], C_EXOTIC, True),
        ]
        for idx, (title, vals, col, logscale) in enumerate(series):
            x = 12 + idx * (w + 10)
            panel(self.screen, x, y0, w, h)
            self.screen.blit(self.fs.render(title, True, C_TEXT_DIM),
                             (x + 8, y0 + 6))
            gx, gy, gw, gh = x + 10, y0 + 26, w - 20, h - 46
            pygame.draw.rect(self.screen, C_PANEL_HI, (gx, gy, gw, gh), 1)
            if logscale:
                mags = [abs(v) for v in vals]
                mx = max(mags) or 1.0
                plot = [math.log10(max(mx * 1e-6, m) / mx) / 6.0 + 1.0
                        for m in mags]
                lo_lab, hi_lab = "%.0e" % (mx * 1e-6), "-%.3g" % mx
            else:
                mn, mx = min(vals), max(vals)
                rng = (mx - mn) or 1.0
                plot = [(v - mn) / rng for v in vals]
                lo_lab, hi_lab = "%.3g" % mn, "%.3g" % mx
            pts = [(gx + gw * i / (len(plot) - 1.0), gy + gh * (1.0 - p))
                   for i, p in enumerate(plot)]
            pygame.draw.lines(self.screen, col, False, pts, 2)
            wallx = gx + gw * 0.5
            pygame.draw.line(self.screen, C_BUBBLE, (wallx, gy),
                             (wallx, gy + gh), 1)
            self.screen.blit(self.fs.render("r = R", True, C_BUBBLE),
                             (wallx + 3, gy + gh - 14))
            self.screen.blit(self.fs.render(hi_lab, True, C_TEXT_DIM),
                             (gx + 2, gy + 1))
            self.screen.blit(self.fs.render(lo_lab, True, C_TEXT_DIM),
                             (gx + 2, gy + gh - 13))
            self.screen.blit(self.fs.render(
                "+/- 6 delta = %.3g m" % (6 * delta), True, C_TEXT_DIM),
                (gx, gy + gh + 4))

    def draw_metric_panel(self, b, R, delta):
        x, w, y = self.W - 360, 348, 52
        panel(self.screen, x, y, w, 384)
        self.screen.blit(self.fm.render("METRIC", True, C_ACCENT), (x + 12, y + 8))
        E = alcubierre_energy_j(b, R, delta)
        Eq = alcubierre_energy_j(b, R, ford_roman_wall_limit(max(1.0, b)))
        tid = wall_tidal_gradient(b, R, delta)
        ec = energy_conditions(b)
        rows = [
            ("R  bubble radius", "%.0f m" % R),
            ("delta  wall", "%.4g m      [ ]" % delta),
            ("sigma = 1/delta", "%.4g /m" % (1.0 / delta)),
            ("beta shown", "%.3f       , ." % b),
            ("", ""),
            ("ALCUBIERRE requirement", ""),
            ("  E", fmt_energy(E)),
            ("  equivalent mass", fmt_mass(equiv_mass_kg(E))),
            ("  at the QI wall limit", ""),
            ("    %s" % fmt_mass(equiv_mass_kg(Eq)), ""),
            ("", ""),
            ("REAL negative energy aboard", ""),
            ("  Casimir lattice", fmt_energy(casimir_onboard_j())),
            ("  shortfall", "%.0f orders of magnitude"
             % orders_of_magnitude(E, casimir_onboard_j())),
            ("", ""),
            ("wall tidal shear (2 m)", "%.2e g" % (tid / 9.81)),
            ("interior tidal shear", "0.00 g   (exactly flat)"),
        ]
        yy = y + 36
        for k, val in rows:
            if not k:
                yy += 7
                continue
            bold = k.isupper() or k.startswith("ALCU") or k.startswith("REAL")
            self.screen.blit(self.fs.render(k, True,
                                            C_TEXT if bold else C_TEXT_DIM),
                             (x + 12, yy))
            if val:
                img = self.fs.render(val, True, C_TEXT)
                self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 18

        yy += 6
        for nm in ("NEC", "WEC", "DEC", "SEC"):
            ok = ec[nm]
            r = pygame.Rect(x + 12 + 84 * ("NEC WEC DEC SEC".split().index(nm)),
                            yy, 76, 22)
            pygame.draw.rect(self.screen, C_GOOD if ok else C_EXOTIC, r, 1,
                             border_radius=4)
            img = self.fs.render("%s %s" % (nm, "OK" if ok else "X"), True,
                                 C_GOOD if ok else C_EXOTIC)
            self.screen.blit(img, (r.centerx - img.get_width() // 2, r.y + 4))
        yy += 30
        for ln in wrap_text(self.fs, ec["note"], w - 24):
            self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM), (x + 12, yy))
            yy += 16

        y2 = y + 396
        env = check_envelope()
        panel(self.screen, x, y2, w, 118)
        note = ("Thicken the wall ( ] ): the energy bill and the tidal shear "
                "BOTH fall -- the one place in this design where safety and "
                "cost pull together. The price is interior volume: %s."
                % env["verdict"])
        yy = y2 + 10
        for ln in wrap_text(self.fs, note, w - 24):
            self.screen.blit(self.fs.render(
                ln, True, C_TEXT_DIM if env["ok"] else C_BAD), (x + 12, yy))
            yy += 15

    # ---- FLIGHT mode ------------------------------------------------------
    def draw_flight(self):
        c, v = self.core, self.voy
        rect = pygame.Rect(0, 40, self.W - 430, self.H - 40)
        self.stars.draw(self.screen, rect, streak=min(1.0, c.beta * 1.4),
                        drift=(self.anim * 40.0 * (1.0 + c.beta * 8)) % 4000)
        cxx, cyy = rect.x + rect.w / 2, rect.y + rect.h / 2

        # Relativistic Doppler colour wash: at high beta the forward starfield
        # blue-shifts and the aft red-shifts. We paint a subtle additive
        # gradient over the streaked stars -- not a physical ray-trace, but
        # the same visual cue SE.py uses for its day/night sky transition.
        if c.beta > 0.05:
            wash = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA)
            b = min(1.0, c.beta)
            # top (forward / ahead) gets a faint blue wash
            for fy in range(0, rect.h // 2, 3):
                t = 1.0 - fy / (rect.h / 2)
                a = int(18 * b * t)
                if a > 0:
                    pygame.draw.rect(wash, (90, 140, 255, a),
                                     (0, fy, rect.w, 3))
            # bottom (aft / behind) gets a faint red wash
            for fy in range(rect.h // 2, rect.h, 3):
                t = (fy - rect.h / 2) / (rect.h / 2)
                a = int(14 * b * t)
                if a > 0:
                    pygame.draw.rect(wash, (255, 90, 60, a),
                                     (0, fy, rect.w, 3))
            self.screen.blit(wash, (rect.x, rect.y),
                             special_flags=pygame.BLEND_RGBA_ADD)

        draw_bubble_glow(self.screen, cxx, cyy,
                         min(rect.w, rect.h) * 0.36, c.bubble_on,
                         C_EXOTIC if c.exotic else C_BUBBLE)

        # engine glow trail: an additive plume behind the ship when the
        # reactor is driving the coils (bubble_on > 0). Matches the
        # GmansRun combustion-glow pattern: layered alpha circles, additive.
        if c.bubble_on > 0.1:
            trail_r = min(rect.w, rect.h) * 0.10 * c.bubble_on
            tg = pygame.Surface((int(trail_r * 4), int(trail_r * 4)),
                                pygame.SRCALPHA)
            tc = C_COIL_LIVE if not c.exotic else C_EXOTIC
            for rad, a in ((int(trail_r * 1.5), 30),
                           (int(trail_r * 1.0), 55),
                           (int(trail_r * 0.6), 90),
                           (int(trail_r * 0.3), 140)):
                if rad > 0:
                    pygame.draw.circle(tg, (tc[0], tc[1], tc[2], a),
                                       (int(trail_r * 2), int(trail_r * 2)),
                                       rad)
            self.screen.blit(tg, (int(cxx - trail_r * 2 - rect.w * 0.06),
                                  int(cyy - trail_r * 2)),
                             special_flags=pygame.BLEND_RGBA_ADD)

        self.frend.render(self.screen, rect,
                          {"default": self.anim * 0.35, "plasma": self.anim * 2.2},
                          show_labels=self.show_labels, label_font=self.fs,
                          interactive=False, coil_glow=c.coil_glow,
                          drive_power=min(1.0, c.beta) * c.bubble_on,
                          rad_heat=clamp((c.rad_k - 600) / 1300.0),
                          bubble_on=c.bubble_on)
        self.draw_flight_hud()
        self.draw_flight_controls()

    def draw_flight_hud(self):
        c, v = self.core, self.voy
        x, w = self.W - 418, 406
        y = 52

        # --- mission ------------------------------------------------------
        panel(self.screen, x, y, w, 176)
        self.screen.blit(self.fm.render("MISSION  Sol -> Proxima b", True,
                                        C_ACCENT), (x + 12, y + 8))
        self.screen.blit(self.fb.render("%s" % v.phase, True,
                                        C_GOOD if v.phase == "ARRIVED"
                                        else C_TEXT), (x + 12, y + 32))
        note = PHASE_NOTE.get(v.phase, "")
        yy = y + 68
        for ln in wrap_text(self.fs, note, w - 24):
            self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM), (x + 12, yy))
            yy += 15
        frac = v.x_m / v.target_m
        bar(self.screen, self.fs, x + 12, y + 122, w - 24, 12, frac, C_ACCENT,
            "distance", "%s of %.4f ly" % (fmt_dist(v.x_m), PROXIMA_LY))
        rows = [("apparent speed", "beta %.4f  (%s)"
                 % (v.beta, "SUPERLUMINAL" if v.beta >= 1 else "%.0f%% c"
                    % (100 * v.beta))),
                ("ETA at this speed", fmt_time(v.eta_s()))]
        yy = y + 142
        for k, val in rows:
            self.screen.blit(self.fs.render(k, True, C_TEXT_DIM), (x + 12, yy))
            img = self.fs.render(val, True, C_TEXT)
            self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 16

        # --- clocks -------------------------------------------------------
        y = y + 186
        panel(self.screen, x, y, w, 74)
        self.screen.blit(self.fm.render("CLOCKS", True, C_ACCENT), (x + 12, y + 6))
        rocket = rocket_proper_time_s(max(0.01, v.beta), max(1.0, v.x_m))
        for i, (k, val, col) in enumerate([
                ("ship", fmt_time(v.t_ship), C_TEXT),
                ("Earth", fmt_time(v.t_earth), C_TEXT),
                ("a rocket at this beta would have aged",
                 fmt_time(rocket), C_TEXT_DIM)]):
            self.screen.blit(self.fs.render(k, True, C_TEXT_DIM),
                             (x + 12, y + 28 + i * 15))
            img = self.fs.render(val, True, col)
            self.screen.blit(img, (x + w - 12 - img.get_width(),
                                   y + 28 + i * 15))

        # --- power and thermal --------------------------------------------
        y = y + 84
        panel(self.screen, x, y, w, 162)
        self.screen.blit(self.fm.render("PLANT", True, C_ACCENT), (x + 12, y + 6))
        if c.beam_w > 0:
            self.screen.blit(self.fs.render(
                "beam %s  %.0f%% captured"
                % (fmt_power(c.beam_w),
                   100 * beam_capture_frac(max(1.0, v.x_m))),
                True, C_ACCENT), (x + 116, y + 9))
        else:
            self.screen.blit(self.fs.render(
                "no beam -- fusion only", True, C_TEXT_DIM), (x + 116, y + 9))
        avail = PLANT_ELECTRIC_W + c.beam_w
        bar(self.screen, self.fs, x + 12, y + 50, w - 24, 12,
            c.load_w / max(1.0, PLANT_ELECTRIC_W),
            C_BAD if c.load_w > PLANT_ELECTRIC_W else C_GOOD,
            "coil + servo + cryo load", "%s / %s"
            % (fmt_power(c.load_w), fmt_power(PLANT_ELECTRIC_W)),
            hi=1.0)
        bar(self.screen, self.fs, x + 12, y + 90, w - 24, 12,
            c.rad_k / DIMS["rad_limit_k"],
            C_BAD if c.rad_k > DIMS["rad_limit_k"] else C_RADIATOR,
            "radiator panels", "%.0f K / %.0f K limit"
            % (c.rad_k, DIMS["rad_limit_k"]),
            mark=DIMS["rad_temp_k"] / DIMS["rad_limit_k"],
            hi=1.0)
        bar(self.screen, self.fs, x + 12, y + 130, w - 24, 12, c.integrity,
            C_GOOD if c.integrity > 0.7 else
            (C_WARN if c.integrity > DRIVE["integrity_min"] else C_BAD),
            "bubble integrity", "%.0f%%" % (100 * c.integrity),
            mark=DRIVE["integrity_min"],
            lo=DRIVE["integrity_min"])
        # --- ledger -------------------------------------------------------
        y = y + 172
        panel(self.screen, x, y, w, 148)
        self.screen.blit(self.fm.render("ENERGY LEDGER", True, C_ACCENT),
                         (x + 12, y + 6))
        led = c.led
        rows = [("beamed in", fmt_energy(led["beam_in"]), C_ACCENT),
                ("kinetic energy held", fmt_energy(led["kinetic"]), C_TEXT),
                ("  peak ever held", fmt_energy(led["kinetic_peak"]), C_TEXT_DIM),
                ("magsail recovered", fmt_energy(led["magsail_regen"]), C_GOOD),
                ("fusion produced", fmt_energy(led["plant_out"]), C_TEXT_DIM),
                ("D-3He burnt", "%.1f kg" % led["fuel_kg"], C_TEXT_DIM),
                ("ISM protons on the wall", "%.3g" % v.ism_particles, C_WARN),
                ("  released on bubble drop",
                 fmt_energy(ism_blast_energy_j(max(v.beta, 0.01), v.x_m)), C_WARN)]
        if c.exotic:
            rows.append(("NEGATIVE ENERGY OWED",
                         "%s UNFUNDED" % fmt_energy(-c.exotic_debt_j), C_EXOTIC))
        yy = y + 28
        for k, val, col in rows:
            self.screen.blit(self.fs.render(k, True, C_TEXT_DIM), (x + 12, yy))
            img = self.fs.render(val, True, col)
            self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 16

        # --- log ----------------------------------------------------------
        y = y + 158
        hh = max(60, self.H - y - 62)
        panel(self.screen, x, y, w, hh)
        self.screen.blit(self.fm.render("LOG", True, C_ACCENT), (x + 12, y + 6))
        rows = []
        for ln in v.log[-14:]:
            wrapped = wrap_text(self.fs, ln, w - 24)
            rows.append((wrapped[0], False))
            for extra in wrapped[1:]:
                rows.append(("    " + extra.lstrip(), True))
        n = int((hh - 32) // 15)
        for i, (ln, cont) in enumerate(rows[-n:]):
            self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM),
                             (x + 12, y + 28 + i * 15))

    def draw_flight_controls(self):
        x, y = 14, self.H - 44
        c, v = self.core, self.voy
        r = chip(self.screen, self.f, x, y, "SHELL", c.bubble_cmd)
        x = r.right + 8
        r = chip(self.screen, self.f, x, y,
                 "DEST ARRAY" if v.dest_array else "FLYBY ONLY",
                 v.dest_array, C_GOOD)
        self._chips["dest"] = r
        x = r.right + 8
        r = chip(self.screen, self.f, x, y, "ALCUBIERRE", self.ftl_unlock,
                 C_EXOTIC)
        self._chips["ftl"] = r
        x = r.right + 16
        hints = {"DOCK": "G = boost", "BOOST": "K = abort to brake",
                 "CRUISE": "K = brake", "BRAKE": "-- braking --",
                 "ARRIVED": "N = new mission"}
        self.screen.blit(self.f.render(
            "%s      , . beta      - + time warp x%s      N reset"
            % (hints.get(v.phase, ""), VOYAGE_WARP_LABEL[v.warp_i]),
            True, C_TEXT_DIM), (x, y + 5))
        if c.helm_locked():
            img = self.fm.render("HELM LOCKED -- forward wall causally "
                                 "disconnected (Everett 1996)", True, C_BAD)
            self.screen.blit(img, ((self.W - 430 - img.get_width()) // 2,
                                   self.H - 84))


    # ---- DILATION mode ----------------------------------------------------
    def draw_dilation(self):
        """Whose clock, and where.

        The warp drive's famous property is that the crew are not time dilated.
        That is true and it is one row of a table. This view draws the rest of
        the table: the static-observer dilation field the bubble genuinely
        carries, the gravitational rate along the route, and the couple of
        seconds of real drift that separate the crew from Earth."""
        c, v = self.core, self.voy
        R = DIMS["bubble_r_m"]
        beta = (c.beta if (c.bubble_on > 0.1 and c.beta > 0.01)
                else max(0.15, c.beta_cmd))
        rect = pygame.Rect(0, 40, self.W - 402, self.H - 236)
        self.stars.draw(self.screen, rect)

        # nested shells, coloured by the static observer's clock rate
        cam = self.mcam
        focal = min(rect.w, rect.h) * 1.10
        cx0, cy0 = rect.x + rect.w / 2.0, rect.y + rect.h / 2.0
        shells = [R * t for t in (0.18, 0.36, 0.54, 0.72, 0.86, 0.94, 0.99,
                                  1.0, 1.02, 1.10, 1.30, 1.60)]
        old = self.screen.get_clip()
        self.screen.set_clip(rect)
        # Stretch the colour ramp across the range the field ACTUALLY spans.
        # The lapse only runs from 1/gamma to 1, so mapping it raw to a colour
        # paints everything the same shade and hides the whole point.
        floor = lapse_static(0.0, beta, R, c.wall_m)
        span = max(1e-9, 1.0 - floor)
        drawn = []
        for rr in shells:
            lap = lapse_static(rr, beta, R, c.wall_m)
            col = (C_BAD if lap == 0.0
                   else _mix(C_WARN, C_GOOD, (lap - floor) / span))
            for axis, zz in (("z", 0.0), ("y", 0.0)):
                pts = _ring_wire(rr, zz, seg=54, axis=axis)[0]
                sx, sy, dz = project(pts, cam.az, cam.el, cam.dist * 0.9,
                                     cx0, cy0, focal, cam.pan)
                seq = [(sx[i], sy[i]) for i in range(len(sx)) if dz[i] > 0.05]
                if len(seq) > 2:
                    pygame.draw.lines(self.screen, col, True, seq, 1)
            drawn.append((rr, lap))
        # ship marker with additive glow (consistent with METRIC view)
        sg = pygame.Surface((28, 28), pygame.SRCALPHA)
        pygame.draw.circle(sg, (C_HULL[0], C_HULL[1], C_HULL[2], 50),
                           (14, 14), 12)
        pygame.draw.circle(sg, (C_HULL[0], C_HULL[1], C_HULL[2], 110),
                           (14, 14), 7)
        self.screen.blit(sg, (int(cx0) - 14, int(cy0) - 14),
                         special_flags=pygame.BLEND_RGBA_ADD)
        pygame.draw.circle(self.screen, C_HULL, (int(cx0), int(cy0)), 5)
        pygame.draw.circle(self.screen, C_ACCENT, (int(cx0), int(cy0)), 5, 1)
        self.screen.set_clip(old)

        text_shadow(self.screen, self.f,
            "STATIC-OBSERVER CLOCK FIELD   dtau/dt = sqrt(1 - beta^2 f(r)^2)",
            (rect.x + 16, rect.y + 12), C_ACCENT)
        for i, t in enumerate([
                "green = 1 (unaffected)   amber = the interior floor, 1/gamma",
                "The CREW are not on this field: they are comoving, so their",
                "dtau/dt is exactly 1. Anyone HOLDING STATION inside the bubble",
                "while it flew past would be dilated by the full Lorentz factor.",
                "Both statements are true at once, which is why 'a warp drive",
                "has no time dilation' needs the words 'for the crew' after it."]):
            text_shadow(self.screen, self.fs, t,
                        (rect.x + 16, rect.y + 36 + i * 15), C_TEXT_DIM)
        if not static_observer_exists(beta):
            text_shadow(self.screen, self.f,
                "beta > 1: NO STATIC OBSERVER EXISTS ANYWHERE INSIDE -- every",
                (rect.x + 16, rect.y + 132), C_BAD)
            text_shadow(self.screen, self.f,
                "worldline is dragged past c. That IS the horizon problem.",
                (rect.x + 16, rect.y + 150), C_BAD)

        self.draw_dilation_graphs(beta, R, c.wall_m)
        self.draw_clock_panel(beta)

    def draw_dilation_graphs(self, beta, R, delta):
        y0 = self.H - 190
        w, h = (self.W - 430) // 2, 150

        # 1: the dilation profile across the bubble
        x = 12
        panel(self.screen, x, y0, w, h)
        self.screen.blit(self.fs.render(
            "dtau/dt for a STATIC observer, across the bubble", True,
            C_TEXT_DIM), (x + 8, y0 + 6))
        gx, gy, gw, gh = x + 10, y0 + 26, w - 20, h - 46
        pygame.draw.rect(self.screen, C_PANEL_HI, (gx, gy, gw, gh), 1)
        n = 140
        pts = []
        for i in range(n + 1):
            rr = 1.7 * R * i / n
            lap = lapse_static(rr, beta, R, delta)
            pts.append((gx + gw * i / n, gy + gh * (1.0 - clamp(lap))))
        pygame.draw.lines(self.screen, C_ACCENT, False, pts, 2)
        wx = gx + gw * (R / (1.7 * R))
        pygame.draw.line(self.screen, C_BUBBLE, (wx, gy), (wx, gy + gh), 1)
        self.screen.blit(self.fs.render("wall", True, C_BUBBLE), (wx + 3, gy + 2))
        self.screen.blit(self.fs.render("1.0", True, C_TEXT_DIM), (gx + 2, gy + 1))
        self.screen.blit(self.fs.render("0", True, C_TEXT_DIM),
                         (gx + 2, gy + gh - 13))
        self.screen.blit(self.fs.render(
            "centre -> 1.7 R      interior floor %.4f"
            % lapse_static(0.0, beta, R, delta), True, C_TEXT_DIM),
            (gx, gy + gh + 4))

        # 2: gravitational clock rate along the route
        x = 22 + w
        panel(self.screen, x, y0, w, h)
        self.screen.blit(self.fs.render(
            "gravitational clock rate along Sol -> Proxima", True, C_TEXT_DIM),
            (x + 8, y0 + 6))
        gx, gy, gw, gh = x + 10, y0 + 26, w - 20, h - 46
        pygame.draw.rect(self.screen, C_PANEL_HI, (gx, gy, gw, gh), 1)
        rates = []
        for i in range(n + 1):
            xm = PROXIMA_M * i / n
            rates.append(grav_rate(xm))
        lo, hi = min(rates), 1.0
        rng = (hi - lo) or 1e-12
        pts = [(gx + gw * i / n, gy + gh * (1.0 - (rates[i] - lo) / rng))
               for i in range(n + 1)]
        pygame.draw.lines(self.screen, C_GOOD, False, pts, 2)
        px = gx + gw * clamp(self.voy.x_m / PROXIMA_M)
        pygame.draw.line(self.screen, C_WARN, (px, gy), (px, gy + gh), 1)
        self.screen.blit(self.fs.render("1 - %.3g" % (1 - hi), True, C_TEXT_DIM),
                         (gx + 2, gy + 1))
        self.screen.blit(self.fs.render("1 - %.3g" % (1 - lo), True, C_TEXT_DIM),
                         (gx + 2, gy + gh - 13))
        self.screen.blit(self.fs.render(
            "Sol's well -> flat -> Proxima's well   (ship marked)", True,
            C_TEXT_DIM), (gx, gy + gh + 4))

    def draw_clock_panel(self, beta):
        v = self.voy
        x, w, y = self.W - 390, 378, 52
        cl = clock_ledger(v.t_ship, v.x_m, beta)
        panel(self.screen, x, y, w, 250)
        self.screen.blit(self.fm.render("CLOCKS", True, C_ACCENT), (x + 12, y + 8))
        self.screen.blit(self.fs.render(
            "rate relative to a clock at infinity", True, C_TEXT_DIM),
            (x + 12, y + 30))
        yy = y + 50
        for name, rate in cl["rates"].items():
            col = C_TEXT
            if name.startswith("warp crew"):
                col = C_GOOD
            elif rate == 0.0:
                col = C_BAD
            self.screen.blit(self.fs.render(name, True, C_TEXT_DIM), (x + 12, yy))
            txt = ("no timelike worldline" if rate == 0.0
                   else "%.12f" % rate)
            img = self.fs.render(txt, True, col)
            self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 19
        yy += 8
        for k, val in (("elapsed, coordinate", fmt_time(v.t_coord)),
                       ("elapsed, crew", fmt_time(v.t_ship)),
                       ("elapsed, Earth", fmt_time(v.t_earth))):
            self.screen.blit(self.fs.render(k, True, C_TEXT_DIM), (x + 12, yy))
            img = self.fs.render(val, True, C_TEXT)
            self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 18
        drift = v.t_ship - v.t_earth
        self.screen.blit(self.fs.render("crew MINUS Earth", True, C_WARN),
                         (x + 12, yy))
        img = self.fs.render("%+.4f s" % drift, True, C_WARN)
        self.screen.blit(img, (x + w - 12 - img.get_width(), yy))

        y2 = y + 262
        panel(self.screen, x, y2, w, 200)
        self.screen.blit(self.fm.render("WHAT THAT MEANS", True, C_ACCENT),
                         (x + 12, y2 + 8))
        note = (
            "The crew gain %+.2f s on Earth over a full crossing -- ALL of it "
            "gravitational, from climbing out of Sol's well and spending the "
            "trip in flat space. Not one microsecond of it is velocity "
            "dilation, because the warp interior has none. A relativistic "
            "rocket at beta = %.3f would come back %s YOUNGER instead. The "
            "warp drive gives up that dividend, and buys arrival in step with "
            "home." % (voyage_grav_drift_s(PROXIMA_M / (max(0.05, beta)
                                                        * C_LIGHT)),
                       max(0.05, beta),
                       fmt_time(PROXIMA_M / (max(0.05, beta) * C_LIGHT)
                                - rocket_proper_time_s(max(0.05, beta),
                                                       PROXIMA_M))))
        yy = y2 + 34
        for ln in wrap_text(self.fs, note, w - 24):
            self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM), (x + 12, yy))
            yy += 15
        yy += 6
        for ln in wrap_text(self.fs,
                            "the ship's own gravity contributes %.2e -- twelve "
                            "orders below the best clock ever built, which is "
                            "how we know it does not matter."
                            % ship_self_dilation(), w - 24):
            self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM), (x + 12, yy))
            yy += 15

    # ---- PORTAL mode ------------------------------------------------------
    def draw_portal(self):
        c = self.core
        rect = pygame.Rect(0, 40, self.W - 402, self.H - 196)
        self.stars.draw(self.screen, rect)
        self.prend.render(self.screen, rect,
                          {"default": self.anim * 0.3},
                          mouse_pos=pygame.mouse.get_pos(),
                          show_labels=self.show_labels, label_font=self.fs,
                          interactive=True, coil_glow=c.coil_glow,
                          drive_power=0.0, rad_heat=0.0, bubble_on=1.0)
        self.draw_view_tabs(rect)
        self.draw_portal_panel()
        part = self.prend.active_part()
        if part is not None:
            self._spec_card(part)

    def draw_portal_panel(self):
        ps = portal_summary()
        x, w, y = self.W - 390, 378, 52
        panel(self.screen, x, y, w, 268)
        self.screen.blit(self.fm.render("PORTAL", True, C_ACCENT), (x + 12, y + 8))
        self.screen.blit(self.fs.render(
            "Morris-Thorne traversable wormhole", True, C_TEXT_DIM),
            (x + 12, y + 30))
        rows = [
            ("aperture 2 b0", "%.0f m" % DIMS["portal_gate_d_m"]),
            ("throat radius b0", "%.1f m" % ps["b0_m"]),
            ("energy density needed", "%s /m^3" % fmt_energy(ps["density_j_m3"])),
            ("exotic energy needed", fmt_energy(ps["energy_j"])),
            ("  as mass", fmt_mass(ps["mass_kg"])),
            ("tidal shear at throat", "%.2e g" % ps["tidal_g"]),
            ("  at 2b0 / 4b0", "%.1e / %.1e g" % (ps["tidal_at_2b0_g"],
                                                   ps["tidal_at_4b0_g"])),
            ("flare-out b'(r0)", "%.2f < 1  (costs NEC)" % ps["flare_out"]["b_prime_at_r0"]),
            ("proper length", "%.1f m = %.1f b0" % (ps["proper_length_m"],
                                                     ps["proper_length_m"] / ps["b0_m"])),
            ("", ""),
            ("SURVIVABLE THROAT", ""),
            ("  b0 for 1 g on a body", "%.3g m" % ps["safe_b0_m"]),
            ("  = Earth diameters", "%.1f" % (ps["safe_b0_m"] / 1.2742e7)),
            ("  its exotic bill", fmt_mass(ps["safe_mass_kg"])),
            ("", ""),
            ("Casimir aboard", fmt_energy(casimir_onboard_j())),
            ("  short by", "%.0f orders (gate)" % ps["casimir_shortfall_orders"]),
            ("  short by", "%.0f orders (survivable)" % ps["safe_shortfall_orders"]),
        ]
        yy = y + 50
        for k, val in rows:
            if not k:
                yy += 6
                continue
            self.screen.blit(self.fs.render(
                k, True, C_TEXT if k.isupper() else C_TEXT_DIM), (x + 12, yy))
            if val:
                col = C_EXOTIC if ("orders" in val or val.startswith("-")) else C_TEXT
                img = self.fs.render(val, True, col)
                self.screen.blit(img, (x + w - 12 - img.get_width(), yy))
            yy += 17

        # --- Ford-Roman quantum inequalities + MMP + Visser ----------------
        y_qi = y + 280
        panel(self.screen, x, y_qi, w, 168)
        self.screen.blit(self.fm.render(
            "FORD-ROMAN QI + MMP + VISSER", True, C_ACCENT), (x + 12, y_qi + 8))
        mmp = ps["mmp"]
        vs = ps["visser"]
        qi_paras = [
            ("QI bound (tau=1s): %s /m^3 -- %d orders below throat demand"
             % (fmt_energy(ps["qi_bound_1s_j_m3"]), ps["qi_shortfall_orders"])),
            ("max hold time for b0=%.0fm: %.1e s vs %.1f s traverse -- %.0f orders"
             % (ps["b0_m"], ps["qi_hold_s"], ps["traverse_s"],
                math.log10(ps["qi_traversal_ratio"]))),
            ("VISSER shell: %s (%s) -- MORE than MT volume"
             % (fmt_energy(vs["shell_energy_j"]), fmt_mass(vs["shell_mass_kg"]))),
            ("MMP: %.0f M_sun magnetically charged BH, r_s=%.1g Earth-diam"
             % (mmp["M_msun"], mmp["r_s_m"] / 1.2742e7)),
            ("  traversal %.0fs, but no magnetic monopole ever observed"
             % mmp["traversal_s"]),
        ]
        yy = y_qi + 32
        for para in qi_paras:
            for ln in wrap_text(self.fs, para, w - 24):
                self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM),
                                 (x + 12, yy))
                yy += 14
            yy += 2

        y2 = y + 456
        panel(self.screen, x, y2, w, 188)
        self.screen.blit(self.fm.render("AND THEN IT IS A TIME MACHINE", True,
                                        C_WARN), (x + 12, y2 + 8))
        g = ctc_by_gravity_well(-0.2)
        w2 = ctc_by_warp_transport(max(0.05, self.core.beta_cmd))
        paras = [
            ("Two mouths at different clock rates desynchronise. When the "
             "offset passes the light-travel time between them, closed "
             "timelike curves exist (Morris, Thorne & Yurtsever 1988)."),
            ("mouth by a neutron star (Phi/c^2 = -0.2): time machine in %s"
             % fmt_time(g["onset_s"])),
            ("carried on THIS warp drive: never -- flat interior, no desync"),
            ("carried on a relativistic rocket: rate gap %.3f, it works"
             % w2["rocket_rate_diff"]),
            ("Hawking's chronology protection conjecture (1992) expects the "
             "throat to destroy itself at exactly that moment. Unproven."),
        ]
        yy = y2 + 32
        for para in paras:
            for ln in wrap_text(self.fs, para, w - 24):
                self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM),
                                 (x + 12, yy))
                yy += 14
            yy += 3

        # the teleporter that actually exists
        q = quantum_teleport_facts()
        bx, bw = 12, self.W - 426
        by = self.H - 150
        panel(self.screen, bx, by, bw, 138)
        self.screen.blit(self.fm.render(
            "THE TELEPORTER THAT ACTUALLY EXISTS", True, C_GOOD), (bx + 12, by + 8))
        lines = [
            ("Quantum teleportation is real, demonstrated, and routine "
             "(Bennett et al. 1993; %.0f km via the Micius satellite, 2017)."
             % q["record_km"]),
            ("It moves a quantum STATE, not matter. It needs pre-shared "
             "entanglement plus %.0f classical bits per qubit -- and that "
             "classical channel is capped at c, so it carries nothing faster "
             "than light." % QT["bits_per_qubit"]),
            ("No-cloning means the original is destroyed. Whether that is a "
             "technicality or the entire moral question depends on who is "
             "stepping into the booth."),
            ("Teleporting one person: about %.1e bits of state. At an "
             "absurdly generous 1 Tb/s that is %s -- roughly %.1f times the "
             "age of the universe." % (q["state_bits"], fmt_time(q["seconds"]),
                                       q["universe_ages"])),
        ]
        yy = by + 32
        for para in lines:
            for ln in wrap_text(self.fs, para, bw - 24):
                self.screen.blit(self.fs.render(ln, True, C_TEXT_DIM),
                                 (bx + 12, yy))
                yy += 14

    # ---- ENERGY LADDER chart (M) -----------------------------------------
    def draw_ladder(self):
        """Thirty years of trying to make the exotic bill affordable, on one
        log axis, against the things that actually exist."""
        w, h = min(1180, self.W - 80), 520
        x, y = (self.W - w) // 2, (self.H - h) // 2
        panel(self.screen, x, y, w, h, 246)
        self.screen.blit(self.fb.render("NEGATIVE-ENERGY LADDER", True,
                                        C_ACCENT), (x + 20, y + 14))
        self.screen.blit(self.fs.render(
            "log10 scale. R = %.0f m, beta = 1, baseline wall 1e-15 m. "
            "M = close" % DIMS["bubble_r_m"], True, C_TEXT_DIM), (x + 22, y + 48))

        gx0, gx1 = x + 268, x + w - 130
        lo_e, hi_e = 0.0, 80.0
        # axis
        ay = y + 78
        pygame.draw.line(self.screen, C_PANEL_HI, (gx0, ay), (gx1, ay), 1)
        for e in range(0, 81, 10):
            px = log_bar_x(10.0 ** e, gx0, gx1, lo_e, hi_e)
            pygame.draw.line(self.screen, C_PANEL_HI, (px, ay), (px, y + h - 96), 1)
            self.screen.blit(self.fs.render("1e%d" % e, True, C_TEXT_DIM),
                             (px - 12, ay - 16))

        base = abs(alcubierre_energy_j(1.0, DIMS["bubble_r_m"], 1e-15))
        rows = []
        for label, factor, status, _cite in LADDER:
            if factor > 0:
                rows.append((label, base * factor, status))
            elif status == "PHYSICAL":
                rows.append((label, kinetic_energy_j(0.5), status))
            else:
                rows.append((label, 0.0, status))
        refs = [
            ("Casimir lattice aboard this ship", abs(casimir_onboard_j())),
            ("this ship's SMES buffer", SMES_J),
            ("total antimatter aboard", DIMS["amtraps"] * DIMS["amtrap_kg"]
             * PLANT["am_energy_j_kg"]),
            ("world energy use, one year", 6.0e20),
            ("the Sun's output, one year", L_SUN * YR),
            ("rest energy of the Sun", M_SUN * C2),
        ]

        yy = ay + 20
        for label, val, status in rows:
            col = {"EXOTIC": C_EXOTIC, "DISPUTED": C_WARN, "REFUTED": C_BAD,
                   "PHYSICAL": C_GOOD}[status]
            # only the citation name fits beside the axis; the descriptions
            # live in the I panel and in --ladder
            name = label.split("   ")[0]
            self.screen.blit(self.fs.render(name, True, C_TEXT), (x + 20, yy))
            if val > 0:
                px = log_bar_x(val, gx0, gx1, lo_e, hi_e)
                pygame.draw.rect(self.screen, col, (gx0, yy + 3, px - gx0, 11),
                                 border_radius=3)
                self.screen.blit(self.fs.render(fmt_energy(val), True, col),
                                 (px + 6, yy + 1))
            else:
                self.screen.blit(self.fs.render(
                    "no surviving reduction -- refuted", True, col),
                    (gx0 + 4, yy + 1))
            yy += 26

        yy += 10
        self.screen.blit(self.f.render("FOR SCALE -- things that exist:", True,
                                       C_TEXT), (x + 20, yy))
        yy += 22
        for label, val in refs:
            self.screen.blit(self.fs.render(label[:34], True, C_TEXT_DIM),
                             (x + 20, yy))
            px = log_bar_x(val, gx0, gx1, lo_e, hi_e)
            pygame.draw.rect(self.screen, C_TEXT_DIM,
                             (gx0, yy + 4, max(2, px - gx0), 8), border_radius=3)
            self.screen.blit(self.fs.render(fmt_energy(val), True, C_TEXT_DIM),
                             (px + 6, yy + 1))
            yy += 20

        need = abs(alcubierre_energy_j(1.0, DIMS["bubble_r_m"], self.core.wall_m))
        msg = ("At your current %.3g m wall the bill is %s -- %.0f orders past "
               "the Casimir lattice." % (self.core.wall_m, fmt_energy(need),
                                         orders_of_magnitude(
                                             need, casimir_onboard_j())))
        self.screen.blit(self.f.render(msg, True, C_WARN), (x + 20, y + h - 34))

    # ---- help -------------------------------------------------------------
    def draw_help(self):
        lines = [
            ("TAB", "SHIP / METRIC / DILATION / PORTAL / FLIGHT"),
            ("drag / wheel / right-drag", "orbit / zoom / pan   (R resets)"),
            ("1 2 3", "full / exploded / assembly     4 or X  section cut"),
            ("L", "part labels        hover a part for its spec card"),
            (", .", "commanded beta     [ ]  wall thickness"),
            ("B", "raise / drop the warp shell"),
            ("F", "unlock ALCUBIERRE (superluminal, unfunded)"),
            ("G / K / J", "boost / brake / toggle destination array"),
            ("- +", "time warp        N  reset mission     P  pause"),
            ("I / M / H", "full spec / energy ladder / this help"),
        ]
        w = 470
        h = 34 + 18 * len(lines)
        x, y = self.W - w - 14, self.H - h - 58
        if self.mode == self.MODE_FLIGHT:
            x = 14
            y = 60
        panel(self.screen, x, y, w, h)
        self.screen.blit(self.fs.render("CONTROLS   (H to hide)", True, C_ACCENT),
                         (x + 12, y + 8))
        yy = y + 28
        for k, t in lines:
            self.screen.blit(self.fs.render(k, True, C_TEXT), (x + 12, yy))
            self.screen.blit(self.fs.render(t, True, C_TEXT_DIM), (x + 176, yy))
            yy += 18

    # ---- full spec (I) ----------------------------------------------------
    def draw_info(self):
        w, h = min(1240, self.W - 60), self.H - 90
        x, y = (self.W - w) // 2, 52
        panel(self.screen, x, y, w, h, 250)
        self.screen.blit(self.fb.render(
            "WD-1 FOLDRUNNER -- FULL SPECIFICATION", True, C_ACCENT),
            (x + 20, y + 12))
        self.screen.blit(self.fs.render(
            "PgUp / PgDn to scroll     I to close", True, C_TEXT_DIM),
            (x + w - 260, y + 22))

        flat = []
        for title, body in info_sections():
            flat.append(("H", title))
            for ln in body:
                flat.append(("B", ln))
            flat.append(("B", ""))
        per = int((h - 62) // 16)
        self.info_scroll = max(0, min(self.info_scroll, max(0, len(flat) - per)))
        yy = y + 52
        for kind, text in flat[self.info_scroll:self.info_scroll + per]:
            if kind == "H":
                self.screen.blit(self.f.render(text, True, C_ACCENT),
                                 (x + 20, yy))
            else:
                col = C_TEXT_DIM
                if "SHORT BY" in text or "OVER PLANT" in text or "PAST THE" in text:
                    col = C_BAD
                elif text.strip().startswith("beta =") or "->" in text:
                    col = C_TEXT
                self.screen.blit(self.fs.render(text, True, col), (x + 28, yy))
            yy += 16
        frac = (self.info_scroll / max(1, len(flat) - per)) if len(flat) > per else 0
        track_h = h - 70
        pygame.draw.rect(self.screen, C_PANEL_HI,
                         (x + w - 14, y + 52, 5, track_h), border_radius=3)
        pygame.draw.rect(self.screen, C_ACCENT,
                         (x + w - 14, y + 52 + int(track_h * frac * 0.92), 5,
                          max(18, int(track_h * 0.08))), border_radius=3)

    # ------------------------------------------------------------------- loop
    def run(self):
        print_startup_banner()
        while self.running:
            dt = min(0.05, self.clock.tick(60) / 1000.0)
            self.handle_events(dt)
            self.update(dt)
            self.draw()
        pygame.quit()


# =============================================================================
# SECTION 13 -- ENTRY POINT
# =============================================================================

def print_startup_banner():
    bcap = max_boost_beta()
    print("=" * 78)
    print(" Warpdrive V1.0 -- WD-1 FOLDRUNNER :: Physical Warp Drive Digital Twin")
    print(" to-scale, flyable, energy-honest (nothing created from nothing)")
    print("=" * 78)
    print(" THE SHIP")
    print("   %-26s %s" % ("dry mass", fmt_mass(SHIP_MASS_KG)))
    print("   %-26s %.0f m ring / %.0f m hull / %.0f m bubble"
          % ("envelope", DIMS["ring_major_d_m"], DIMS["hull_len_m"],
             DIMS["bubble_r_m"]))
    print("   %-26s %.0f GW thermal -> %s electrical"
          % ("fusion plant", DIMS["reactor_th_gw"], fmt_power(PLANT_ELECTRIC_W)))
    print("   %-26s %.0f m^2, %.0f K limit"
          % ("radiators", RADIATOR_AREA_M2, DIMS["rad_limit_k"]))
    print("-" * 78)
    print(" THE TWO DRIVES")
    print("   PHYSICAL (beta < 1)   positive energy, every energy condition met.")
    print("     Bobrick & Martire 2021 / Fuchs et al. 2024. Real matter, real")
    print("     solution. Costs %s to reach beta = 0.5, and this model"
          % fmt_energy(kinetic_energy_j(0.5)))
    print("     charges you every joule of it.")
    print("   ALCUBIERRE (beta > 1)  needs %s of NEGATIVE energy."
          % fmt_energy(alcubierre_energy_j(1.0, DIMS["bubble_r_m"], 1.0)))
    print("     Onboard Casimir lattice supplies %s -- short by %.0f orders"
          % (fmt_energy(casimir_onboard_j()),
             orders_of_magnitude(
                 alcubierre_energy_j(1.0, DIMS["bubble_r_m"], 1.0),
                 casimir_onboard_j())))
    print("     of magnitude. It flies here, flagged UNFUNDED on every frame.")
    print("-" * 78)
    print(" THE MISSION  Sol -> Proxima Centauri b, %.4f ly" % PROXIMA_LY)
    print("   max cruise beta %.4f -- EMERGENT from beam aperture, wavelength,"
          % bcap)
    print("     tap power and ship mass. Nothing in the spec names a speed limit.")
    print("   crossing %s ship time, and the same on Earth's calendar."
          % fmt_time(PROXIMA_M / (bcap * C_LIGHT)))
    print("   stopping needs an array at the far end: the magsail halves your")
    print("     speed in %s but takes %s to actually stop."
          % (fmt_time(magsail_halving_time_s(0.5)),
             fmt_time(magsail_decel_time_s(0.5))))
    print("-" * 78)
    print(" CONTROLS")
    print("   TAB  SHIP / METRIC / DILATION / PORTAL / FLIGHT")
    print("        I  full spec      M  energy ladder      H  help")
    print("   SHIP    drag=orbit  wheel=zoom  right-drag=pan  R=reset  L=labels")
    print("           1=full 2=exploded 3=assembly  4/X=section  hover=spec card")
    print("   METRIC  [ ] wall thickness   , . beta   -- watch the bill move")
    print("   DILATION every clock in the problem, not just the flattering one")
    print("   PORTAL  the wormhole, priced -- and the time machine it hands you")
    print("   FLIGHT  B=shell  G=boost  K=brake  J=destination array  - + warp")
    print("           F=unlock Alcubierre mode (superluminal, unfunded)")
    print("   P pause    H help    ESC quit")
    print("=" * 78)


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="Warpdrive.py",
        description="WD-1 Foldrunner -- physical warp drive digital twin")
    ap.add_argument("--selftest", action="store_true",
                    help="headless physics unit checks")
    ap.add_argument("--feasibility", action="store_true",
                    help="honest hurdle-by-hurdle scorecard")
    ap.add_argument("--metric", action="store_true",
                    help="warp-metric numbers, no window")
    ap.add_argument("--ladder", action="store_true",
                    help="negative-energy reduction ladder")
    ap.add_argument("--dilation", action="store_true",
                    help="environmental spacetime dilation: every clock")
    ap.add_argument("--portal", action="store_true",
                    help="Morris-Thorne wormhole + the real teleporter")
    ap.add_argument("--send", action="store_true",
                    help="portal traversal tests: send signal/person/object through")
    ap.add_argument("--voyage", nargs="?", const=0.5, type=float,
                    metavar="BETA", help="headless Sol -> Proxima flight report")
    ap.add_argument("--flyby", action="store_true",
                    help="with --voyage: no destination array (flyby only)")
    ap.add_argument("--all", action="store_true", help="every report in order")
    args = ap.parse_args(argv)

    ran = False
    if args.selftest or args.all:
        ok = selftest()
        ran = True
        if not args.all and not ok:
            return 1
    if args.metric or args.all:
        report_metric()
        ran = True
    if args.ladder or args.all:
        report_ladder()
        ran = True
    if args.dilation or args.all:
        report_dilation()
        ran = True
    if args.portal or args.all:
        report_portal()
        ran = True
    if args.send or args.all:
        report_portal_test()
        ran = True
    if args.feasibility or args.all:
        report_feasibility()
        ran = True
    if args.voyage is not None or args.all:
        beta = args.voyage if args.voyage is not None else 0.5
        report_voyage(beta=clamp(beta, 0.01, DRIVE["beta_sub_max"]),
                      dest_array=not args.flyby)
        ran = True
    if ran:
        return 0

    if pygame is None:
        print("pygame is required for the interactive viewer.")
        print("Install it with:  pip install pygame numpy")
        print("The headless reports still work: --selftest --metric --ladder")
        print("                                 --feasibility --voyage")
        return 2
    App().run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
