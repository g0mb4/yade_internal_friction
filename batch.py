
exec(open("./setup/01_parameters.py").read())
exec(open("./setup/02_materials.py").read())
exec(open("./setup/03_device.py").read())
exec(open("./setup/04_particles.py").read())
exec(open("./setup/05_engine.py").read())

O.run()
O.wait()
