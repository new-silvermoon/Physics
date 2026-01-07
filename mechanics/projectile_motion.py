from vpython import *

def run():
    """Run the Projectile Motion simulation."""
    scene.range = 50
    scene.title = "Projectile Motion"
    
    # Ground
    ground = box(pos=vector(0, -1, 0), size=vector(100, 2, 20), color=color.green)
    
    # Ball
    ball = sphere(pos=vector(-40, 2, 0), radius=1, color=color.yellow, make_trail=True)
    
    # Initial conditions
    v0 = 30
    angle = 45 * pi / 180
    ball.v = vector(v0 * cos(angle), v0 * sin(angle), 0)
    
    g = vector(0, -9.8, 0)
    dt = 0.01
    
    # Run simulation
    while ball.pos.y >= 0:
        rate(100)
        ball.v = ball.v + g * dt
        ball.pos = ball.pos + ball.v * dt
        
    label(pos=vector(0, 20, 0), text="Click to restart", height=20)
    scene.waitfor('click')

if __name__ == "__main__":
    run()
