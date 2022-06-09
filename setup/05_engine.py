import os
from datetime import datetime
from enum import Enum
import math 

class State(Enum):
    INIT = 0
    LIFTING = 1
    WAITING = 2
    MEASURING = 3

O.engines = [
    ForceResetter(),
    InsertionSortCollider(
        [
            Bo1_Sphere_Aabb(),
            Bo1_Facet_Aabb()
        ]
    ),
    InteractionLoop(
        [
            Ig2_Sphere_Sphere_ScGeom6D(),
            Ig2_Facet_Sphere_ScGeom6D()
        ],
        [
            Ip2_FrictMat_FrictMat_FrictPhys(),
        ],
        [
            Law2_ScGeom_FrictPhys_CundallStrack(),
        ]
    ),
    NewtonIntegrator(damping=.4, gravity=(0, 0, -gravitational_acceleration)),
    DomainLimiter(lo=(-tray_radius , -tray_radius, 0), hi=(tray_radius, tray_radius, particle_sample_height), iterPeriod=10),
    PyRunner(command='startLiftingIfSteady()', iterPeriod=1),
    PyRunner(command='stopLifting()', iterPeriod=1),
    PyRunner(command='waitingForSteadyState()', iterPeriod=1),
    PyRunner(command='measuring()', iterPeriod=1),
]

O.dt = 0.2 * PWaveTimeStep()

state = State.INIT

def startLiftingIfSteady():
    global state

    if state != State.INIT:
        return

    if O.time < 1:
        return

    if unbalancedForce() > 0.2:
        return

    state = State.LIFTING
    O.bodies[device_moving_id].state.vel = (0, 0, lift_velocity)
    print("lifting started")

def stopLifting():
    global state

    if state != State.LIFTING:
        return

    if O.bodies[device_moving_id].state.pos[2] > device_height:
        O.bodies[device_moving_id].state.vel = (0, 0, 0)
        state = State.WAITING
        print("lifting stopped, waiting for steady state")

def waitingForSteadyState():
    global state

    if state != State.WAITING:
        return
    
    steady = True

    for b in O.bodies:
        if isinstance(b.shape, Sphere):

            speed = math.sqrt(b.state.vel[0] ** 2 + b.state.vel[1] ** 2 + b.state.vel[2] ** 2)

            if speed > 0.01:
                steady = False
                break
               
    if steady == False:
        return

    state = State.MEASURING
    print("steady state, measuring")

def measuring():
    global state

    if state != State.MEASURING:
        return

    pos_max = (0, 0, 0)
    for b in O.bodies:
        if isinstance(b.shape, Sphere):
            pos = b.state.pos

            if pos[2] > pos_max[2]:
                pos_max = pos
                
    print(f"pos_max = {pos_max}")

    with open("data.csv", "a") as f:
        now = datetime.now()
        d = now.strftime('%Y-%m-%d')
        t = now.strftime('%H:%M:%S')
        f.write(f"{d};{t};{pos_max[0]};{pos_max[1]};{pos_max[2]}\n")

    O.pause()
    