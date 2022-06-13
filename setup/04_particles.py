from yade import pack
import math

particle_clump_offset = particle_radius * .1
particle_clump = pack.SpherePack(
    [
        ((0, 0, 0), particle_radius),
        ((particle_clump_offset, 0, 0), particle_radius)
    ]
)

clump_coord = (tray_radius / 2) / math.cos(math.pi / 4)

cloud = pack.SpherePack()
cloud.makeClumpCloud((-clump_coord, -clump_coord, 0.001),
                        (clump_coord, clump_coord, particle_sample_height),
                        [particle_clump])
particles_id = cloud.toSimulation(material=particle_mat)