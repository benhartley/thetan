## MODIFIED Requirements

### Requirement: Teacher lesson guide structure
Each lesson SHALL have a corresponding teacher guide markdown file in the `teachers/` directory with a filename matching the student file using the module.lesson naming convention (e.g., `1.1-forward.md` for `1.1-forward.py`).

#### Scenario: Guide file naming convention
- **WHEN** a student lesson file exists at `students/M.L-name.py`
- **THEN** a corresponding teacher guide SHALL exist at `teachers/M.L-name.md`

### Requirement: Learning objectives section
Each teacher guide SHALL include a "Learning Objectives" section listing both robot learning objectives and Python learning objectives.

#### Scenario: Objectives are present
- **WHEN** a teacher opens a lesson guide
- **THEN** they see a bulleted list of specific, measurable learning objectives covering both robot and Python concepts

#### Scenario: Dual objectives clearly separated
- **WHEN** reading the learning objectives
- **THEN** robot objectives and Python objectives are clearly labeled or grouped

## ADDED Requirements

### Requirement: Module overview in first lesson guide

The first lesson guide of each module (e.g., `1.1-forward.md`) SHALL include a brief module overview section.

#### Scenario: Module overview content
- **WHEN** a teacher opens the first lesson guide of a module
- **THEN** they see an overview of what the entire module covers and how lessons build on each other

### Requirement: Prior lesson recap

For lessons after the first in a module, the teacher guide SHALL include a "Prior Lessons Recap" section summarizing what students learned previously.

#### Scenario: Recap helps continuity
- **WHEN** teaching lesson 1.3
- **THEN** the teacher guide summarizes key concepts from lessons 1.1 and 1.2

#### Scenario: First lesson has no recap
- **WHEN** teaching lesson 1.1 (first in module)
- **THEN** there is no prior lessons recap section

### Requirement: Python concept teaching notes

Each teacher guide SHALL include specific guidance for teaching the Python concept introduced in that lesson.

#### Scenario: Python pedagogy included
- **WHEN** teaching a lesson that introduces enums (e.g., 1.2)
- **THEN** the teaching notes explain how to introduce the concept of named values to beginners
