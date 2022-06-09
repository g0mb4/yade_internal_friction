particle_mat = FrictMat(young=particle_Young_modulus,
                   poisson=particle_Poisson_s_ratio,
                   density=particle_clump_density,
                   frictionAngle=particle_friction_angle)

O.materials.append(particle_mat)

steel = FrictMat(young=steel_Young_modulus,
                 poisson=steel_Poisson_s_ratio,
                 density=steel_density,
                 frictionAngle=steel_friction_angle)
O.materials.append(steel)