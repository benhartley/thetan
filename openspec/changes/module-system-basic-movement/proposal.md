## Why

The current single-lesson approach (`1-hello.py`, `2-turns.py`, etc.) doesn't support progressive skill-building where students incrementally add to their code. A module system with cumulative lessons (`1.1`, `1.2`, etc.) allows each lesson to build on the previous one, reinforcing concepts while introducing new ones.

Additionally, we should assume students have limited Python experience. Each module should teach both the relevant Theta Robot APIs *and* foundational Python concepts appropriate to that module's complexity level.

## What Changes

- **BREAKING**: Restructure from flat lesson files to `module.lesson` naming (e.g., `1.1-forward.py`, `1.2-reverse.py`)
- Move current `students/1-hello.py` to become Lesson 1.1
- Create Module 1 "Basic Movement" with 5 progressive lessons covering all movement APIs
- Update teacher guides to match the new `module.lesson` structure
- Each lesson file in a given module contains all code from previous module lessons plus new content (cumulative)

### Module 1: Basic Movement - Lesson Plan

Each lesson introduces both robot capabilities and Python fundamentals:

| Lesson | Robot Topic | Python Concepts | API Functions |
|--------|-------------|-----------------|---------------|
| 1.1 | Forward Motion | Function calls, arguments, comments | `robotGoms()`, `robotStop()` |
| 1.2 | Reverse Motion | Enums/named values, changing arguments | `RXDirection.Reverse` |
| 1.3 | Spinning | More enums, comparing similar functions | `robotRotatems()`, `RXRobotDirection` |
| 1.4 | Sequences | Program flow, sequential execution | Multiple function calls |
| 1.5 | Speed Control | Numbers, experimenting with values | Speed parameter variations |

## Capabilities

### New Capabilities

- `module-lesson-structure`: Defines the hierarchical module.lesson file organization, naming conventions, and cumulative code approach where each lesson builds on previous lessons
- `basic-movement-module`: Specification for Module 1 content covering forward, reverse, spinning, sequences, and speed control using Theta motor APIs. Includes Python learning objectives (function calls, arguments, enums, sequential execution) alongside robot concepts

### Modified Capabilities

- `teacher-lesson-guides`: Existing spec needs delta to support module.lesson naming and add module overview sections

## Impact

- **File structure**: `students/` directory changes from flat to module-based naming
- **Teacher guides**: `teachers/` directory follows same module.lesson pattern
- **Existing content**: `students/1-hello.py` and `teachers/1-hello.md` will be migrated to `1.1-*` format
- **AGENTS.md**: Directory conventions section needs updating for new structure
