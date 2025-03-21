def Thrust(thrustLevel, maxThrust, fuelLeft, fuelCapacity):
    if fuelLeft > 0 and 0 <= thrustLevel <= 1:
        thrustForce = thrustLevel * maxThrust  
        thrust = (thrustForce * fuelLeft) / fuelCapacity  
        fuelLeft = max(0, fuelLeft - thrustForce / 100)  
        return thrust, fuelLeft  
    return 0, fuelLeft  

def Velocity(currentVelocity, thrustForce, gravity, mass):
    return currentVelocity + (thrustForce / mass - gravity)

def Altitude(currentVelocity, currentAltitude):  
    return max(0, currentAltitude + currentVelocity)
