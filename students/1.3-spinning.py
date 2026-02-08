# === LESSON 1.1: Forward Motion ===
# Robot concept: Making the robot move forward for a set duration
# Python concept: Function calls, arguments, comments

# Move forward at speed 50 (try values from 0 to 100)
theta.robot_goms(RXDirection.Forward, 50, 2000)
theta.robot_stop(RXStopMode.Brake)

# === LESSON 1.2: Reverse Motion ===
# Robot concept: Making the robot move backward
# Python concept: Enums (named values), changing function arguments

theta.robot_goms(RXDirection.Reverse, 50, 2000)
theta.robot_stop(RXStopMode.Brake)

# === LESSON 1.3: Spinning ===
# Robot concept: Making the robot spin in place (left or right)
# Python concept: Comparing similar functions, different enum types

theta.robot_rotatems(RXRobotDirection.Left, 50, 1000)
theta.robot_stop(RXStopMode.Brake)

theta.robot_rotatems(RXRobotDirection.Right, 50, 1000)
theta.robot_stop(RXStopMode.Brake)
