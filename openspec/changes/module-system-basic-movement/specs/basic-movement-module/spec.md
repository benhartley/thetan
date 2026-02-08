## ADDED Requirements

### Requirement: Module 1 covers basic movement

Module 1 SHALL be titled "Basic Movement" and cover the fundamental Theta robot movement APIs.

#### Scenario: Module 1 scope
- **WHEN** completing Module 1
- **THEN** students can make the robot move forward, backward, spin left/right, and control speed

### Requirement: Module 1 lesson count

Module 1 SHALL contain exactly 5 lessons, numbered 1.1 through 1.5.

#### Scenario: All lessons present
- **WHEN** Module 1 is complete
- **THEN** files exist for lessons 1.1, 1.2, 1.3, 1.4, and 1.5

### Requirement: Lesson 1.1 Forward Motion

Lesson 1.1 SHALL introduce forward movement using `robotGoms()` and stopping with `robotStop()`.

**Robot concept:** Making the robot move forward for a set duration
**Python concept:** Function calls, arguments (parameters), comments

#### Scenario: Lesson 1.1 code content
- **WHEN** viewing `1.1-forward.py`
- **THEN** it contains a call to `theta.robotGoms(RXDirection.Forward, speed, duration)` and `theta.robotStop()`

#### Scenario: Lesson 1.1 Python learning
- **WHEN** teaching lesson 1.1
- **THEN** students learn what a function call is, how to pass arguments, and how to write comments

### Requirement: Lesson 1.2 Reverse Motion

Lesson 1.2 SHALL introduce reverse movement by changing the direction argument.

**Robot concept:** Making the robot move backward
**Python concept:** Enums/named values, changing function arguments

#### Scenario: Lesson 1.2 code content
- **WHEN** viewing `1.2-reverse.py`
- **THEN** it contains code from 1.1 plus a call using `RXDirection.Reverse`

#### Scenario: Lesson 1.2 Python learning
- **WHEN** teaching lesson 1.2
- **THEN** students learn that `RXDirection.Forward` and `RXDirection.Reverse` are named values (enums)

### Requirement: Lesson 1.3 Spinning

Lesson 1.3 SHALL introduce spinning/rotation using `robotRotatems()`.

**Robot concept:** Making the robot spin in place (left or right)
**Python concept:** Comparing similar functions, different enum types

#### Scenario: Lesson 1.3 code content
- **WHEN** viewing `1.3-spinning.py`
- **THEN** it contains code from 1.1-1.2 plus calls to `theta.robotRotatems()` with `RXRobotDirection.Left` or `Right`

#### Scenario: Lesson 1.3 Python learning
- **WHEN** teaching lesson 1.3
- **THEN** students understand that `robotRotatems()` is similar to `robotGoms()` but for rotation, and uses `RXRobotDirection` instead of `RXDirection`

### Requirement: Lesson 1.4 Sequences

Lesson 1.4 SHALL combine multiple movement commands to create a movement sequence/pattern.

**Robot concept:** Creating movement patterns (e.g., drive in a square)
**Python concept:** Program flow, sequential execution (code runs top to bottom)

#### Scenario: Lesson 1.4 code content
- **WHEN** viewing `1.4-sequences.py`
- **THEN** it contains multiple movement commands that together create a recognizable pattern

#### Scenario: Lesson 1.4 Python learning
- **WHEN** teaching lesson 1.4
- **THEN** students understand that Python executes commands in order from top to bottom

### Requirement: Lesson 1.5 Speed Control

Lesson 1.5 SHALL explore speed variations and their effects on robot movement.

**Robot concept:** Understanding speed values (0-100), fast vs. slow movement
**Python concept:** Numbers as values, experimenting with parameters

#### Scenario: Lesson 1.5 code content
- **WHEN** viewing `1.5-speed.py`
- **THEN** it demonstrates different speed values and their effects

#### Scenario: Lesson 1.5 Python learning
- **WHEN** teaching lesson 1.5
- **THEN** students understand that speed is a number from 0-100 and experiment with different values

### Requirement: Valid Theta API usage

All lesson files SHALL use only functions documented in the Theta library (`reference/theta.ts`).

#### Scenario: API correctness
- **WHEN** reviewing any lesson file
- **THEN** all `theta.*` function calls match the signatures in `reference/theta.ts`

#### Scenario: Movement API subset for Module 1
- **WHEN** completing Module 1
- **THEN** only these APIs are used: `robotGoms()`, `robotStop()`, `robotRotatems()`, and their related enums
