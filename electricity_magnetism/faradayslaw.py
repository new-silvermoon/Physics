from vpython import *
import numpy as np

"""
Faraday's law of induction (briefly, Faraday's law) is a basic law of electromagnetism predicting how a magnetic field will interact with an electric circuit to produce an electromotive force (EMF)—a phenomenon known as electromagnetic induction.
"""

MagnetAxis = vector(1, 0, 0)  # Orientation of the magnet, in (x,y,z) components.


def setup_magnet_field(time):
    bx = cos(time)
    by = 0
    bz = 0
    # Combine components into a vector and return.
    return vector(bx, by, bz)


observation_points = []
radius = 1  # Radius of circle of observation points.
for theta in np.arange(0, 3 * pi, 0.5):
    observation_points.append(radius * vector(0, radius * cos(theta), radius * sin(theta)))
    observation_points.append(radius * vector(0.1, radius * cos(theta), radius * sin(theta)))
    observation_points.append(0.75 * radius * vector(0.2, radius * cos(theta), radius * sin(theta)))
    observation_points.append(radius * vector(-0.1, radius * cos(theta), radius * sin(theta)))
    observation_points.append(radius * vector(-0.2, radius * cos(theta), radius * sin(theta)))

magnetic_field = arrow(pos=vector(0, 0, 0), axis=setup_magnet_field(0), visible=True, color=color.magenta)

electric_field_vectors = []  # List of arrows to depict electric field.
for Point in observation_points:
    electric_field_vectors.append(arrow(pos=Point, axis=vector(0, 0, 0), color=color.cyan))

dt = 0.01  # Time step between animation frames.
prev_dt = 0  # Previous dt value
time = 0  # Time starts at 0.
ScaleFactor = 1.2e-1



text(text="magenta - magnetic field",
     height=0.1,
     pos=vector(1, -1, 0),
     color=color.magenta)

text(text="cyan - electric field",
     height=0.1,
     pos=vector(1, -1.2, 0),
     color=color.cyan)


def animation_action(b):
    global dt, prev_dt
    if b.text == 'Pause':
        prev_dt = dt
        dt = 0
        b.text = 'Play'
    else:
        dt = prev_dt
        b.text = 'Pause'
    return


PauseButton = button(text='Pause', bind=animation_action)

while True:
    rate(0.5 / dt)
    if PauseButton.text == 'Pause':
        magnetic_field.axis = setup_magnet_field(time)  # Update magnetic field vector.
        # Update electric field vectors.
        BDeriv = (setup_magnet_field(time + dt) - setup_magnet_field(time - dt)) / (2 * dt)
        for FieldHere in electric_field_vectors:
            rhat = hat(FieldHere.pos)
            Ehat = rhat.cross(hat(BDeriv))
            FieldHere.axis = ScaleFactor * mag(BDeriv) * 2 / mag(FieldHere.pos) * Ehat
        time = time + dt  # Update time.
