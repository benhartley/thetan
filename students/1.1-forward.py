# === LESSON 1.1: Forward Motion ===
# Robot concept: Making the robot move forward for a set duration
# Python concept: Function calls, arguments, comments

# Move forward at speed 50 (try values from 0 to 100)
# The robot will move for 2000 milliseconds (2 seconds)
theta.robot_go_ms(RxDirection.FORWARD, 50, 2000)

# Stop the robot with braking (stops quickly)
theta.robot_stop(RxStopMode.BRAKE)

# --- EXPERIMENT! ---
# Try these changes and see what happens:
#   - Change speed from 50 to 30 or 80
#   - Change duration from 2000 to 1000 or 5000 (milliseconds)
#   - Try coasting to a stop: RxStopMode.COAST
