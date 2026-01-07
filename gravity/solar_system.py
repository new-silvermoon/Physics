from vpython import *

def run():
    """Run the Solar System simulation."""
    scene.range = 3e11  # Increased range to see outer planets (though still zoomed in for inner ones)
    scene.title = "Solar System (Not to scale)"
    
    # Constants
    G = 6.7e-11
    
    # Sun
    sun = sphere(pos=vector(0,0,0), radius=1e10, color=color.yellow, mass=2e30)
    sun.v = vector(0,0,0)
    
    # Data: name, distance from sun (m), radius (m), color, mass (kg), velocity (m/s)
    planets_data = [
        {"name": "Mercury", "dist": 5.79e10, "radius": 2.4e9, "color": color.gray(0.5), "mass": 3.3e23, "v": 47400},
        {"name": "Venus", "dist": 1.08e11, "radius": 6.0e9, "color": color.orange, "mass": 4.87e24, "v": 35000},
        {"name": "Earth", "dist": 1.50e11, "radius": 6.4e9, "color": color.blue, "mass": 5.97e24, "v": 29800},
        {"name": "Mars", "dist": 2.28e11, "radius": 3.4e9, "color": color.red, "mass": 6.42e23, "v": 24100},
        {"name": "Jupiter", "dist": 7.78e11, "radius": 7.1e10, "color": color.orange, "mass": 1.90e27, "v": 13100},
        {"name": "Saturn", "dist": 1.43e12, "radius": 6.0e10, "color": color.yellow, "mass": 5.68e26, "v": 9700},
        {"name": "Uranus", "dist": 2.87e12, "radius": 2.6e10, "color": color.cyan, "mass": 8.68e25, "v": 6800},
        {"name": "Neptune", "dist": 4.50e12, "radius": 2.5e10, "color": color.blue, "mass": 1.02e26, "v": 5400}
    ]
    
    bodies = [sun]
    earth_obj = None
    
    # Create Planets
    for data in planets_data:
        planet = sphere(pos=vector(data["dist"], 0, 0), radius=data["radius"], color=data["color"], mass=data["mass"], make_trail=True)
        planet.v = vector(0, data["v"], 0)
        bodies.append(planet)
        if data["name"] == "Earth":
            earth_obj = planet

    # Create Moon
    # Moon distance from Earth is ~3.84e8 m.
    # Scaled up for visibility perhaps, or just realistic. Let's try realistic relative to Earth but Earth is already huge.
    # Earth radius is 6.4e9 (in this sim). 3.84e8 is smaller than the radius! 
    # The simulation uses "Not to scale" radii. 
    # Let's place the moon at a visible distance relative to the Earth's visual size.
    # Earth radius = 5e9 (sim value was 5e9, updated to 6.4e9 above).
    # Let's put moon at 1.5e10 from Earth.
    moon_dist = 4e10 # exaggerated distance
    moon = sphere(pos=earth_obj.pos + vector(moon_dist, 0, 0), radius=1.7e9, color=color.white, mass=7.35e22, make_trail=True)
    # Moon velocity: Earth v + orbital v (~1022 m/s). 
    moon.v = earth_obj.v + vector(0, 1022 * 5, 0) # speed up moon for visibility
    bodies.append(moon)
    
    dt = 3600 * 4 # 4 hours step (reduced from 24h for moon stability)
    
    label(pos=vector(0, 3e11, 0), text="Press 'Ctrl+C' to exit", height=20)

    while True:
        rate(200) # Faster rate to compensate for smaller dt
        scene.center = sun.pos # Keep sun centered? Or simplify and keep origin centered.
        # Actually, let's just keep origin centered.
        
        # Calculate forces
        for i, body in enumerate(bodies):
            body.a = vector(0,0,0)
            for j, other in enumerate(bodies):
                if i != j:
                    r = other.pos - body.pos
                    # F = G * m1 * m2 / r^2
                    # a = F / m1 = G * m2 / r^2
                    acc = G * other.mass * r.norm() / mag2(r)
                    body.a = body.a + acc
        
        # Update motion
        for body in bodies:
            body.v = body.v + body.a * dt
            body.pos = body.pos + body.v * dt

if __name__ == "__main__":
    run()
