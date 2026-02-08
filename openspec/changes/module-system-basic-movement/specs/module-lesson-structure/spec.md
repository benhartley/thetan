## ADDED Requirements

### Requirement: Module-lesson file naming convention

Student code files SHALL use the naming pattern `M.L-name.py` where:
- `M` is the module number (1, 2, 3, ...)
- `L` is the lesson number within that module (1, 2, 3, ...)
- `name` is a kebab-case descriptive name for the lesson

#### Scenario: Valid lesson file names
- **WHEN** creating a new lesson file
- **THEN** the file MUST be named like `1.1-forward.py`, `1.2-reverse.py`, `2.1-lights.py`

#### Scenario: Files sorted correctly
- **WHEN** listing files alphabetically in the students directory
- **THEN** lessons appear in module order, then lesson order within each module

### Requirement: Teacher guide naming matches student files

Teacher guide files SHALL use the naming pattern `M.L-name.md` matching the corresponding student file.

#### Scenario: Matching names
- **WHEN** a student file `1.2-reverse.py` exists
- **THEN** its teacher guide MUST be named `1.2-reverse.md`

### Requirement: Cumulative code within modules

Each lesson file within a module SHALL contain all code from previous lessons in that module, plus the new code for the current lesson.

#### Scenario: Lesson 1.3 contains prior lessons
- **WHEN** viewing `1.3-spinning.py`
- **THEN** the file contains code from lessons 1.1 and 1.2, followed by new code for 1.3

#### Scenario: First lesson of module is standalone
- **WHEN** viewing the first lesson of any module (e.g., `1.1-forward.py`, `2.1-lights.py`)
- **THEN** the file contains only that lesson's code (no prior lessons to include)

### Requirement: Lesson section comments

Each lesson's code block within a file SHALL be preceded by a comment header identifying the lesson.

#### Scenario: Comment header format
- **WHEN** including code from lesson 1.2 in a later lesson file
- **THEN** it MUST be preceded by a comment like `# === LESSON 1.2: Reverse Motion ===`

#### Scenario: New lesson section clearly marked
- **WHEN** viewing a lesson file
- **THEN** the new content for that lesson is identifiable by its section header

### Requirement: Dual learning objectives per lesson

Each lesson SHALL have both a robot learning objective (what the robot does) and a Python learning objective (what programming concept is introduced).

#### Scenario: Lesson defines both objectives
- **WHEN** designing a lesson
- **THEN** both a "Robot Concept" and "Python Concept" MUST be specified

#### Scenario: Teacher guide covers both objectives
- **WHEN** a teacher guide is created for a lesson
- **THEN** it MUST include teaching notes for both the robot and Python concepts

### Requirement: Student files location

All student lesson files SHALL be placed in the `students/` directory at the repository root.

#### Scenario: New lesson placement
- **WHEN** creating lesson 1.4
- **THEN** the file is created at `students/1.4-sequences.py`

### Requirement: Teacher guides location

All teacher guide files SHALL be placed in the `teachers/` directory at the repository root.

#### Scenario: New guide placement
- **WHEN** creating a teacher guide for lesson 1.4
- **THEN** the file is created at `teachers/1.4-sequences.md`
