readParamsFromTable(particle_radius_param = 0.006)  # nopep8
# readParamsFromTable() needs it
from yade.params.table import *  # nopep8

particle_clump_density = 2600   # kg m^-3
particle_Young_modulus = 5e5    # Pa
particle_Poisson_s_ratio = 0.4   # -
particle_friction_angle= .5  # -
particle_radius = particle_radius_param  # m

gravitational_acceleration = 9.81  # m s^2
lift_velocity = 0.1     # m s^-1

steel_density = 7800   # kg m^-3
steel_Young_modulus = 2.1e8  # Pa
steel_Poisson_s_ratio = 0.3  # -
steel_friction_angle= 0.52  # -

particle_sample_height = 0.4  # m
tray_radius = 0.05   # m
