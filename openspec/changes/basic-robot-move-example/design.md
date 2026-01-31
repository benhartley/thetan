## Context

This change adds a basic example to the Theta Robot tutorial series. The example demonstrates simple forward movement using the existing Theta library, with educational comments to help students understand the code.

## Goals / Non-Goals

**Goals:**
- Provide a simple, working example of robot movement
- Include comments explaining each part of the code
- Encourage experimentation by suggesting value changes

**Non-Goals:**
- Implement advanced robot behaviors or control logic
- Modify the Theta library itself
- Add complex features like obstacle avoidance

## Decisions

- **File Location**: Place the example in the standard examples directory following existing naming conventions
- **Library Usage**: Use the standard Theta library functions for motor control as documented
- **Comment Style**: Use clear, student-friendly language in comments

## Risks / Trade-offs

- **Risk**: Students might modify values in ways that damage hardware → Mitigation: Include warnings about safe value ranges in comments
- **Risk**: Example might be too simple for advanced students → Mitigation: This is the "first example", can add more complex ones later