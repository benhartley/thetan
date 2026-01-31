## Context

The project currently has an `examples/` directory containing MakeCode Python files for Theta robot tutorials. With only one example (`1-hello.py`), this is the ideal time to restructure before more content is added. Teachers using these tutorials need accompanying guidance materials that don't belong in the same directory as student code.

## Goals / Non-Goals

**Goals:**
- Clean separation between student code and teacher materials
- Consistent naming convention that pairs student files with teacher guides
- Create a template for teacher lesson guides that can scale with the series

**Non-Goals:**
- Changing the content of existing student code files
- Creating a complex build system or tooling around the directories
- Adding assessment or grading functionality

## Decisions

- **Directory naming**: Use `students/` and `teachers/` (not `learners/instructors/` or `code/guides/`)
  - Rationale: Clear, simple terms that match educational context. "Students" and "teachers" are universally understood.

- **File naming convention**: Match student and teacher files by prefix (e.g., `1-hello.py` ↔ `1-hello.md`)
  - Rationale: Easy to find pairs, natural ordering by lesson number, no need for a manifest file.

- **Teacher guide format**: Markdown with sections for objectives, notes, discussion, and extensions
  - Rationale: Markdown is readable in GitHub, easy to edit, and converts to other formats if needed.

## Risks / Trade-offs

- **Risk**: Breaking existing references to `examples/` → Update AGENTS.md documentation as part of this change
- **Risk**: Teachers might want different guide formats → Keep initial template simple and iterate based on feedback
- **Trade-off**: Separate directories mean navigating between files → Accepted for cleaner organization; IDE features help with navigation
