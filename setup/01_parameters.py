readParamsFromTable(particle_friction_angle_param=0.5)
from yade.params.table import * 

particle_radius = 0.001         # m

particle_clump_density = 2600   # kg m^-3
particle_Young_modulus = 5e5    # Pa
particle_Poisson_s_ratio = 0.4  # -
particle_friction_angle = particle_friction_angle_param

gravitational_acceleration = 9.81  # m s^2
lift_velocity = 0.1     # m s^-1

steel_density = 7800   # kg m^-3
steel_Young_modulus = 2.1e8  # Pa
steel_Poisson_s_ratio = 0.3  # -
steel_friction_angle= 0.52  # -

particle_sample_height = 40 * particle_radius  # m
tray_radius = 25 * particle_radius   # m

print(f"particle_radius={particle_radius}")
print(f"particle_friction_angle={particle_friction_angle}")
