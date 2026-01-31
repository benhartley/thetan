## ADDED Requirements

### Requirement: Basic Robot Movement Example
The system SHALL provide a basic Python example demonstrating how to make the Theta robot move forward using the Theta library, including explanatory comments for each code section and prompts encouraging students to experiment with different values.

#### Scenario: Successful Forward Movement
- **WHEN** the example code is run on a Theta robot
- **THEN** the robot moves forward for the specified duration at the specified speed

#### Scenario: Code Comments Provide Guidance
- **WHEN** a student views the example code
- **THEN** each major section has a comment explaining its purpose

#### Scenario: Encouragement for Experimentation
- **WHEN** a student views the example code
- **THEN** there are comments suggesting specific values to change and observe the effects

### Requirement: Theta Library Integration
The example SHALL properly import and use the Theta library functions for motor control.

#### Scenario: Library Import
- **WHEN** the example is loaded
- **THEN** it imports the necessary Theta modules without errors

#### Scenario: Motor Control Usage
- **WHEN** the example executes the movement command
- **THEN** it uses Theta library functions to set motor speeds and directions