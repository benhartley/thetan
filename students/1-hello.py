# 1-hello.py - Your First Theta Robot Program!
# This example makes your robot move forward, then stop.

# --- MOVEMENT SECTION ---
# Move forward at speed 50 (try values from 0 to 100)
# The robot will move for 2000 milliseconds (2 seconds)
theta.robotGoms(RXDirection.Forward, 50, 2000)

# Stop the robot with braking (stops quickly)
theta.robotStop(RXStopMode.Brake)

# --- EXPERIMENT! ---
# Try these changes and see what happens:
#   - Change speed from 50 to 30 or 80
#   - Change duration from 2000 to 1000 or 5000 (milliseconds)
#   - Try moving in reverse: RXDirection.Reverse
#   - Try coasting to a stop: RXStopMode.Coast
