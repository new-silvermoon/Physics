# Physics Simulations

A comprehensive collection of interactive, 3D physics simulations written in Python using the `vpython` library. This project serves as an educational tool to visualize and understand fundamental physical principles through mechanics, electromagnetism, and astrophysics.

## Simulations

### 1. Simple Harmonic Motion
This simulation models the classic physics problem of a driven, damped pendulum.
- **Physics**: Solves the differential equation for a pendulum with damping and a periodic driving force.
- **Visuals**: Displays the moving pendulum bob, a real-time graph of angle $\theta$ vs. time, and a phase space plot of angular velocity $\omega$ vs. angle $\theta$.
- **Key Concepts**: Resonance, damping, phase space trajectories.
- [Wiki: Simple Harmonic Motion](https://en.wikipedia.org/wiki/Simple_harmonic_motion)

### 2. Faraday's Law
A visualization of electromagnetic induction based on Faraday's Law.
- **Physics**: Demonstrates how a time-varying magnetic field induces a curling electric field.
- **Visuals**: Shows a central magnetic field vector changing over time and the resulting circular electric field vectors at observation points around it.
- **Key Concepts**: Magnetic flux, electromotive force (EMF), Maxwell's equations.
- [Wiki: Faraday's Law](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction)

### 3. Projectile Motion
A 3D kinematic simulation of a projectile launched into the air.
- **Physics**: Calculates the trajectory of a particle under the influence of uniform gravity.
- **Visuals**: A yellow projectile leaves a motion trail as it arcs through 3D space and impacts the green ground plane.
- **Key Concepts**: Kinematics, vectors, parabolic trajectories.
- [Wiki: Projectile Motion](https://en.wikipedia.org/wiki/Projectile_motion)

### 4. Solar System
An N-body gravity simulation of our Solar System.
- **Physics**: Uses Newton's Law of Universal Gravitation to calculate forces between all bodies (Sun, 8 planets, and the Moon) in every time step.
- **Visuals**: Renders the Sun and planets with approximate relative colors and orbital distances (radii not to scale for visibility). Includes the Earth-Moon system.
- **Key Concepts**: N-body problem, orbital mechanics, gravitational attraction.
- [Wiki: Orbit](https://en.wikipedia.org/wiki/Orbit)

## Setup

1.  **Clone the repository**.
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main application to select and launch a simulation via a command-line interface:

```bash
python main.py
```

Follow the on-screen menu to choose a simulation:
- Enter `1` to `4` to launch a specific simulation.
- Enter `5` to exit the program.
- You can also press `Ctrl+C` at any time to quit a running simulation.

