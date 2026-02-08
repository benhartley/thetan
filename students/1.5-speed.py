# === LESSON 1.1: Forward Motion ===
# Robot concept: Making the robot move forward for a set duration
# Python concept: Function calls, arguments, comments

# Move forward at speed 50 (try values from 0 to 100)
theta.robot_go_ms(RxDirection.FORWARD, 50, 2000)
theta.robot_stop(RxStopMode.BRAKE)

# === LESSON 1.2: Reverse Motion ===
# Robot concept: Making the robot move backward
# Python concept: Enums (named values), changing function arguments

theta.robot_go_ms(RxDirection.REVERSE, 50, 2000)
theta.robot_stop(RxStopMode.BRAKE)

# === LESSON 1.3: Spinning ===
# Robot concept: Making the robot spin in place (left or right)
# Python concept: Comparing similar functions, different enum types

theta.robot_rotate_ms(RxRobotDirection.LEFT, 50, 1000)
theta.robot_stop(RxStopMode.BRAKE)

theta.robot_rotate_ms(RxRobotDirection.RIGHT, 50, 1000)
theta.robot_stop(RxStopMode.BRAKE)

# === LESSON 1.4: Sequences ===
# Robot concept: Combining movements to create patterns
# Python concept: Program flow - code runs from top to bottom

# A mini square (just 2 sides for brevity)
theta.robot_go_ms(RxDirection.FORWARD, 50, 1500)
theta.robot_stop(RxStopMode.BRAKE)
theta.robot_rotate_ms(RxRobotDirection.LEFT, 50, 400)
theta.robot_stop(RxStopMode.BRAKE)
theta.robot_go_ms(RxDirection.FORWARD, 50, 1500)
theta.robot_stop(RxStopMode.BRAKE)

# === LESSON 1.5: Speed Control ===
# Robot concept: How speed affects movement - fast vs slow
# Python concept: Numbers as values, experimenting with parameters

# Speed is a number from 0 to 100
# 0 = stopped, 100 = full speed
# Let's see what different speeds look like!

# SLOW: Careful and precise (speed 20)
theta.robot_go_ms(RxDirection.FORWARD, 20, 2000)
theta.robot_stop(RxStopMode.BRAKE)

# MEDIUM: A good balance (speed 50)
theta.robot_go_ms(RxDirection.FORWARD, 50, 2000)
theta.robot_stop(RxStopMode.BRAKE)

# FAST: Quick but harder to control (speed 80)
theta.robot_go_ms(RxDirection.FORWARD, 80, 2000)
theta.robot_stop(RxStopMode.BRAKE)

# Notice: same duration (2000ms) but different distances!
# Faster speed = further distance in the same time

# --- EXPERIMENT! ---
# Try these changes and observe:
#   - What's the slowest the robot will move? (Try speed 10, 5, 1)
#   - Is there a difference between speed 90 and 100?
#   - How does speed affect spinning? Try slow and fast rotations
#   - Use COAST instead of BRAKE at high speed - what happens?
