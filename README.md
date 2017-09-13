# orbit-determination
Orbit determination methods.

## Planned functionality:
This package will include functionality to calculate orbital maneuvers of a satellite give some initial orbit. Initial functionality will assume Hohmann Transfers for orbital raises/lowers.

I'd like to plot the satellite ground track on a 2d map.

### Classical Orbital Elements
1. _semimajor axis:_ describes the size of the ellipse
1. _inclination:_ the angle between the angular momentum vector and the unit vector in the Z-direction
1. _right ascension of the ascending node:_ the angle from the vernal equinox to the ascending node. The _ascending node_ is the point where the satellite passes through the equitorial plane moving from south to north. Right ascension is measured as a right-handed rotation about the pole, __Z__.
1. _argument of perigee:_ the angle from the ascending node ot the eccentricity vector measured in the direction of the satellite's motion. the _eccentricity vector_ points from the center of the Earth to perigee with a magnitude equal to the eccentricity of the orbit
1. _true anomaly:_ the angle from the eccentricity vector to the satellite position vector, measured in the direction of satellite motion. Alternately, we could use _time since perigee passage,_ __T__.


## Keplar's Equations

Keplars equations describe the motion of planets in elliptical orbits, however expressing them in terms of time requires some manipulation. The equations need to be iteratively solved. Stumpff functions can be used to combine the Keplar equations into a single universal equation as a function of time. 
