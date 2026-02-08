## Context

Currently, lesson files are named with a simple numeric prefix (`1-hello.py`, `2-turns.py`). This flat structure doesn't convey lesson relationships or support cumulative learning within a topic area.

The project teaches children to code using the Theta Robot with MakeCode Python. Students are assumed to have limited Python experience, so lessons must introduce both robot APIs and Python fundamentals progressively.

**Current state:**
- `students/1-hello.py` - standalone lesson
- `teachers/1-hello.md` - matching teacher guide
- Flat naming with no module grouping

## Goals / Non-Goals

**Goals:**
- Establish a module.lesson naming convention (e.g., `1.1-forward.py`)
- Create Module 1 with 5 cumulative lessons covering basic movement
- Each lesson teaches both a robot concept and a Python concept
- Lessons within a module build on each other (lesson N contains code from lessons 1 through N-1)
- Teacher guides follow the same naming pattern

**Non-Goals:**
- Creating modules beyond Module 1 (future work)
- Implementing sensors, LEDs, or other non-movement features
- Creating a module overview/index page (keep it simple for now)
- Automated testing of lesson code

## Decisions

### 1. File naming: `M.L-name.py` format

**Decision:** Use `module.lesson-kebab-name.py` format (e.g., `1.1-forward.py`, `1.2-reverse.py`)

**Alternatives considered:**
- Nested directories (`module1/lesson1.py`) - Rejected: adds complexity, harder to see progression at a glance
- Underscore separator (`1_1_forward.py`) - Rejected: dots better convey hierarchy
- Just numbers (`1.1.py`) - Rejected: names aid discoverability and intent

**Rationale:** The dot separator clearly shows module.lesson relationship while keeping all files in a single directory for easy browsing. The kebab-case name after the number aids understanding.

### 2. Cumulative code within modules

**Decision:** Each lesson file contains all code from previous lessons in that module, plus new code for the current lesson.

**Alternatives considered:**
- Imports from previous lessons - Rejected: MakeCode Python doesn't support inter-file imports like standard Python
- Separate "starter" and "complete" files - Rejected: doubles file count, confusing for students

**Rationale:** Students see their program grow. They can run any lesson file independently. Teachers can show progression by comparing files.

### 3. Code organization within lesson files

**Decision:** Use comment sections to delineate code from different lessons:
```python
# === LESSON 1.1: Forward Motion ===
<code from 1.1>

# === LESSON 1.2: Reverse Motion ===
<new code for 1.2>
```

**Rationale:** Clear visual separation helps students identify what's new vs. what they've seen before.

### 4. Dual learning objectives per lesson

**Decision:** Each lesson explicitly teaches one robot concept and one Python concept.

**Rationale:** Students with no Python background need scaffolding. Pairing "what the robot does" with "how Python expresses it" reinforces both.

### 5. Teacher guide structure

**Decision:** Teacher guides follow the same `M.L-name.md` naming and include both robot and Python learning objectives.

**Rationale:** Consistency between student and teacher files. Teachers need to know both dimensions they're teaching.

## Risks / Trade-offs

**[Risk] Cumulative files get long by lesson 5** → Mitigation: Module 1 is simple movement only; 5 lessons will be ~30-50 lines total. Future modules may need different strategies.

**[Risk] Students confused by seeing "old" code** → Mitigation: Clear section comments and teacher guidance to explain the cumulative approach.

**[Trade-off] Breaking change to existing structure** → Accepted: Only one lesson exists currently (`1-hello.py`), so migration impact is minimal.

**[Trade-off] Single directory may get crowded with many modules** → Accepted for now: Cross that bridge when we have 3+ modules. Could revisit nested directories later.
