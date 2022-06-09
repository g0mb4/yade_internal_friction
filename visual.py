from yade import qt

exec(open("./setup/01_parameters.py").read())
exec(open("./setup/02_materials.py").read())
exec(open("./setup/03_device.py").read())
exec(open("./setup/04_particles.py").read())
exec(open("./setup/05_engine.py").read())

qt.View()

v = yade.qt.views()[0]

# to print the current camera parameters of the view.
# v.lookAt, v.viewDir, v.eyePosition, v.upVector 

v.lookAt, v.viewDir, v.eyePosition, v.upVector = (Vector3(-0.5202103833723141779,0.00316169161203007365,0.1096700540448581479),
 Vector3(-1.000000000000000222,2.220446049250313081e-16,2.220446049250313081e-16),
 Vector3(0.4797896166276859886,0.003161691612029851606,0.1096700540448579259),
 Vector3(0,-3.628430889079936605e-12,1.000000000000000222))
