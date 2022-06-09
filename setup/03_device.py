from yade import geom, pack

device_cyl_segments_number = 20
device_inner_diameter = 0.05
device_height = 0.2
device_plate_width = 0.1

device_moving = []
device_moving_cylinder = geom.facetCylinder(
    center=(0, 0, device_height / 2),
    radius=device_inner_diameter / 2,
    height=device_height,
    wallMask=4,
    segmentsNumber=device_cyl_segments_number,
    wire=True,
    color=(0.5, 0.5, 0.5))

for f in device_moving_cylinder:
    f.state.mass = 1
    device_moving.append(f)

device_moving_id = O.bodies.appendClumped(device_moving)[0]
O.bodies[device_moving_id].state.blockedDOFs = "XYZxyz"
O.bodies[device_moving_id].material = steel

device_fixed = []
device_tray = geom.facetCylinder(center=(0, 0, 0),
                                 radius=tray_radius,
                                 wallMask=1,
                                 height=0,
                                 wire=False,
                                 segmentsNumber=64,
                                 color=(0.5, 0.5, 0.5))

for f in device_tray:
    f.state.mass = 1
    device_fixed.append(f)

device_fixed_plate_id = O.bodies.append(device_fixed)[0]
O.bodies[device_fixed_plate_id].state.blockedDOFs = 'XYZxyz'
O.bodies[device_fixed_plate_id].material = steel
