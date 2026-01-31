## Why

The current `examples/` directory conflates student code files with project structure. As the tutorial series grows, we need separate spaces for student-facing code and teacher-facing guidance materials. This separation enables teachers to have lesson plans, learning objectives, and teaching notes alongside each student exercise.

## What Changes

- **BREAKING**: Rename `examples/` directory to `students/`
- Add new `teachers/` directory for lesson guide markdown files
- Create `teachers/1-hello.md` with teaching notes for the first lesson
- Establish naming convention: student files (`1-hello.py`) pair with teacher guides (`1-hello.md`)

## Capabilities

### New Capabilities
- `teacher-lesson-guides`: Markdown files in `teachers/` directory containing learning objectives, teaching notes, discussion prompts, and extension activities for each lesson

### Modified Capabilities
<!-- No existing specs to modify -->

## Impact

- `examples/1-hello.py` moves to `students/1-hello.py`
- New `teachers/` directory created
- Future lessons follow pattern: `students/N-name.py` + `teachers/N-name.md`
- Documentation (AGENTS.md) needs updating to reflect new directory structure
