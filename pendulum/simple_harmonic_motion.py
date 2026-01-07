from vpython import *


def run():
    """Run the Simple Harmonic Motion simulation."""
    
    scene.range = 2
    scene.title = "Simple Harmonic Motion"
    
    """In mechanics and physics, simple harmonic motion is a special type of periodic motion where the restoring force on 
    the moving object is directly proportional to the object's displacement magnitude and acts towards the object's 
    equilibrium position. It results in an oscillation which, if uninhibited by friction or any other dissipation of 
    energy, continues indefinitely. """

    ''' Physical constants '''
    mass = 1.0  # mass of the pendulum
    gravity = 9.8  # magnitude of gravitational field
    length = 0.25 * gravity  # length of the pendulum
    damping = 0.1  # damping coefficient
    pi = 3.14159265359
    
    """Initial values for execution"""
    time = 0.0
    tmax = 300
    dt = 0.005
    theta = 0.5
    theta_dot = -0.02

    graph(x=200, y=400)
    fdvstime = gcurve(color=color.red)

    def calculate_sec_derv_theta(theta, first_derv_theta, time):
        """
        Calculates second derivative of theta
        :param theta:
        :param first_derv_theta:
        :param time:
        :return:
        """

        #  fd = 0.0 ## Uncomment if you're taking out driving force!

        # Calculate driving force
        period = pi / 2.0
        #  fd = 5.0*cos(6.28*time/period)

        if abs(time % period) < period / 2.0:
            fd = 5.0
        else:
            fd = -5.0

        fdvstime.plot(pos=(time, fd))

        #  Calculating the second derivative
        sec_derv_theta = -gravity / length * sin(theta) - damping * first_derv_theta + fd
        return sec_derv_theta

    graph(x=0, y=0, title='theta vs. time')
    thetavstime = gcurve(color=color.green)
    graph(x=500, y=400, title='thetadot vs. theta')
    thetadotvstheta = gcurve(color=color.green)
    canvas(x=800, y=0)
    bob = sphere(pos=vector(length * sin(theta), -length * cos(theta), 0), radius=length / 10.0, color=color.cyan)
    rod = cylinder(pos=vector(0, 0, 0), axis=bob.pos, radius=bob.radius * 0.1)
    rod_reference = cylinder(pos=vector(0, 0, 0), axis=bob.pos, radius=bob.radius * 0.1, color=color.red, opacity=0.25)

    while time < tmax:
        rate(100)
        theta_dot = theta_dot + calculate_sec_derv_theta(theta, theta_dot, time) * dt
        theta = theta + theta_dot * dt
        time = time + dt
        bob.pos = vector(length * sin(theta), -length * cos(theta), 0)
        rod.axis = bob.pos
        thetavstime.plot(pos=(time, theta))
        thetadotvstheta.plot(pos=(theta, theta_dot))


if __name__ == "__main__":
    run()
