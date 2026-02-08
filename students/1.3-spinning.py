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
