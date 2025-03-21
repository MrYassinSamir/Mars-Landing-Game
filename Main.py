from physics import Thrust, Velocity, Altitude
from utils import Write, get_float_input


gravity = 3.73
mass = 150
maxThrust = 500
initialAltitude = 100
initialVelocity = 0
Fuel = 500
Fuel_Left = Fuel

Write("\nWelcome Captain to Mars!\n")
Write("\nWe should land safely or we will die!\n")
Write("\nYou should control the amount of fuel burning and the thrust force\n")
Write("\nLet's Land, Captain!!!\n")

IAltitude = initialAltitude
IVelocity = initialVelocity

print(f"\nVelocity = {IVelocity} m/sec \nAltitude = {IAltitude} m \nThrust = {maxThrust}\n")

while IAltitude > 0:
    if Fuel_Left > 0:
        print(f"\nVelocity = {IVelocity:.2f} m/s, Altitude = {IAltitude:.2f} m, Fuel Left = {Fuel_Left:.2f}\n")

        Fuel_Usage = get_float_input("How much fuel will you burn? ", 0, Fuel_Left)
        thrustLevel = get_float_input("Thrust Level (0 to 1): ", 0, 1)

        Fuel_Left = max(0, Fuel_Left - Fuel_Usage)
        
        thrust, Fuel_Left = Thrust(thrustLevel, maxThrust, Fuel_Left, Fuel)

        IVelocity = Velocity(IVelocity, thrust, gravity, mass)
        IAltitude = Altitude(IVelocity, IAltitude)
    
    else:  
        print("\nFuel is finished!!! You crashed, Captain!\n")
        break  

if IAltitude == 0:
    if abs(IVelocity) <= 2:
        print("\n✅ You landed safely!\n")
    else:
        print(f"\n💥 You crashed at {IVelocity:.2f} m/s!\n")
