import sys
from pendulum import simple_harmonic_motion
from electricity_magnetism import faradayslaw
from mechanics import projectile_motion
from gravity import solar_system

def main():
    try:
        while True:
            print("\nPhysics Simulations")
            print("1. Simple Harmonic Motion")
            print("2. Faraday's Law")
            print("3. Projectile Motion")
            print("4. Solar System")
            print("5. Exit")
            
            choice = input("Enter choice (1-5): ")
            
            if choice == '1':
                try:
                    simple_harmonic_motion.run()
                except Exception as e:
                    print(f"Error running simulation: {e}")
            elif choice == '2':
                try:
                    faradayslaw.run()
                except Exception as e:
                    print(f"Error running simulation: {e}")
            elif choice == '3':
                try:
                    projectile_motion.run()
                except Exception as e:
                    print(f"Error running simulation: {e}")
            elif choice == '4':
                try:
                    solar_system.run()
                except Exception as e:
                    print(f"Error running simulation: {e}")
            elif choice == '5':
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
