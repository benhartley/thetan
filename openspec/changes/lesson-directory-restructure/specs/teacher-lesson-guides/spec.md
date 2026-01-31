## ADDED Requirements

### Requirement: Teacher lesson guide structure
Each lesson SHALL have a corresponding teacher guide markdown file in the `teachers/` directory with a filename matching the student file (e.g., `1-hello.md` for `1-hello.py`).

#### Scenario: Guide file naming convention
- **WHEN** a student lesson file exists at `students/N-name.py`
- **THEN** a corresponding teacher guide SHALL exist at `teachers/N-name.md`

### Requirement: Learning objectives section
Each teacher guide SHALL include a "Learning Objectives" section listing what students will learn from the lesson.

#### Scenario: Objectives are present
- **WHEN** a teacher opens a lesson guide
- **THEN** they see a bulleted list of specific, measurable learning objectives

### Requirement: Teaching notes section
Each teacher guide SHALL include a "Teaching Notes" section with guidance for instructors on how to present the lesson.

#### Scenario: Notes provide teaching guidance
- **WHEN** a teacher reads the teaching notes
- **THEN** they find tips on pacing, common student mistakes, and key points to emphasize

### Requirement: Discussion prompts section
Each teacher guide SHALL include a "Discussion Prompts" section with questions to engage students.

#### Scenario: Prompts encourage student thinking
- **WHEN** a teacher uses the discussion prompts
- **THEN** they have open-ended questions that help students reflect on what they learned

### Requirement: Extension activities section
Each teacher guide SHALL include an "Extension Activities" section with optional challenges for advanced students.

#### Scenario: Extensions provide additional challenges
- **WHEN** a student finishes the main lesson early
- **THEN** the teacher can assign extension activities from the guide

### Requirement: API reference section
Each teacher guide SHALL include an "API Reference" section listing the Theta library functions used in the lesson, with brief descriptions and links to the source.

#### Scenario: Functions are documented with source references
- **WHEN** a teacher wants to understand or explain a function used in the lesson
- **THEN** they find a list of functions with descriptions and line references to `reference/theta.ts`

#### Scenario: Related functions are suggested
- **WHEN** a teacher wants to suggest variations or extensions
- **THEN** they find related Theta API functions that could be explored
