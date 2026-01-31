Never commit to git - a human will always review your work and commit once happy

## Project Context: Theta Robot Tutorials

This project creates tutorial examples for the **Theta robot** by 4tronix/Robotixlab, programmed using **Microsoft MakeCode for micro:bit**.

### What is MakeCode?

MakeCode is a block-based and text-based programming environment for micro:bit. It supports:
- **Blocks**: Visual drag-and-drop programming
- **JavaScript/TypeScript**: Text-based programming
- **Python**: MakeCode Python (NOT standard CPython)

**Important**: MakeCode Python is a subset designed for the micro:bit. It has different libraries and syntax from standard Python. Code runs on the micro:bit hardware, not on a PC.

### Theta Robot Library

The Theta robot uses the `theta` MakeCode extension. Documentation:
- Package page: https://makecode.microbit.org/pkg/4tronix/Theta
- GitHub source: https://github.com/4tronix/Theta
- **Local reference**: `reference/theta.ts` - Full source code of the MakeCode package with all available functions, enums, and documentation comments

#### Key API Functions

**Movement:**
```python
theta.robotGo(RXDirection.Forward, 60)           # Move forever at speed 0-100
theta.robotGoms(RXDirection.Reverse, 100, 2000)  # Move for milliseconds
theta.robotRotate(RXRobotDirection.Left, 70)     # Spin in place
theta.robotRotatems(RXRobotDirection.Right, 50, 400)  # Spin for milliseconds
```

**Stopping:**
```python
theta.robotStop(RXStopMode.Coast)  # Slow coast to stop
theta.robotStop(RXStopMode.Brake)  # Rapid brake stop
```

**Individual motors:**
```python
theta.motorMove(RXMotor.Left, RXDirection.Forward, 40)
theta.motorMove(RXMotor.Right, RXDirection.Forward, 70)
theta.motorMove(RXMotor.Both, RXDirection.Forward, 60)
```

**Motor bias (correct veering):**
```python
theta.motorBias(RXRobotDirection.Left, 5)   # Bias left by 5%
theta.motorBias(RXRobotDirection.Right, 15) # Bias right by 15%
```

**Sonar (optional sensor):**
```python
theta.readSonar(RXPingUnit.Centimeters)
theta.readSonar(RXPingUnit.Inches)
theta.readSonar(RXPingUnit.MicroSeconds)
```

**FireLeds (14 RGB LEDs):**
```python
theta.ledsColor(0x00FF00)           # Set all to green (hex)
theta.ledsColor(RXColors.Green)     # Set all to green (enum)
theta.ledClear()                    # Clear all
theta.setPixel(3, 0xff0000)         # Set LED 3 to red
theta.ledRainbow(True)              # Rainbow pattern
theta.ledBrightness(100)            # Set brightness (0-255, default 40)
theta.ledShift(False)               # Shift LEDs
theta.ledRotate(True)               # Rotate LEDs
theta.setUpdateMode(RXMode.Manual)  # Manual or Auto update mode
theta.convertRGB(50, 100, 200)      # Create color from RGB values
```

#### Enums

- `RXDirection`: `Forward`, `Reverse`
- `RXRobotDirection`: `Left`, `Right`
- `RXStopMode`: `Coast`, `Brake`
- `RXMotor`: `Left`, `Right`, `Both`
- `RXPingUnit`: `Centimeters`, `Inches`, `MicroSeconds`
- `RXColors`: `Red`, `Green`, `Blue`, etc.
- `RXMode`: `Manual`, `Auto`

### Important Rules for Examples

- DO NOT invent or guess API functions - always refer to the documentation above or `reference/theta.ts`
- Student code files go in `students/` directory with naming like `1-hello.py`, `2-turns.py`, etc.
- Teacher guides go in `teachers/` directory with matching names like `1-hello.md`, `2-turns.md`, etc.
- MakeCode Python doesn't need imports - `theta` and enums are globally available
- LSP errors about undefined `theta` are expected (code runs on micro:bit, not PC)
- Speed values are 0-100, durations are in milliseconds

## Issue Tracking with bd (beads)

**IMPORTANT**: This project uses **bd (beads)** for ALL issue tracking. Do NOT use markdown TODOs, task lists, or other tracking methods.

### Why bd?

- Dependency-aware: Track blockers and relationships between issues
- Git-friendly: Auto-syncs to JSONL for version control
- Agent-optimized: JSON output, ready work detection, discovered-from links
- Prevents duplicate tracking systems and confusion

### Quick Start

**Check for ready work:**

```bash
bd ready --json
```

**Create new issues:**

```bash
bd create "Issue title" -t bug|feature|task -p 0-4 --json
bd create "Issue title" -p 1 --deps discovered-from:bd-123 --json
bd create "Subtask" --parent <epic-id> --json  # Hierarchical subtask (gets ID like epic-id.1)
```

**Claim and update:**

```bash
bd update bd-42 --status in_progress --json
bd update bd-42 --priority 1 --json
```

**Complete work:**

```bash
bd close bd-42 --reason "Completed" --json
```

### Issue Types

- `bug` - Something broken
- `feature` - New functionality
- `task` - Work item (tests, docs, refactoring)
- `epic` - Large feature with subtasks
- `chore` - Maintenance (dependencies, tooling)

### Priorities

- `0` - Critical (security, data loss, broken builds)
- `1` - High (major features, important bugs)
- `2` - Medium (default, nice-to-have)
- `3` - Low (polish, optimization)
- `4` - Backlog (future ideas)

### Workflow for AI Agents

1. **Check ready work**: `bd ready` shows unblocked issues
2. **Claim your task**: `bd update <id> --status in_progress`
3. **Work on it**: Implement, test, document
4. **Discover new work?** Create linked issue:
   - `bd create "Found bug" -p 1 --deps discovered-from:<parent-id>`
5. **Complete**: `bd close <id> --reason "Done"`
6. **Commit together**: Always commit the `.beads/issues.jsonl` file together with the code changes so issue state stays in sync with code state

### Auto-Sync

bd automatically syncs with git:

- Exports to `.beads/issues.jsonl` after changes (5s debounce)
- Imports from JSONL when newer (e.g., after `git pull`)
- No manual export/import needed!

### GitHub Copilot Integration

If using GitHub Copilot, also create `.github/copilot-instructions.md` for automatic instruction loading.
Run `bd onboard` to get the content, or see step 2 of the onboard instructions.

### MCP Server (Recommended)

If using Claude or MCP-compatible clients, install the beads MCP server:

```bash
pip install beads-mcp
```

Add to MCP config (e.g., `~/.config/claude/config.json`):

```json
{
  "beads": {
    "command": "beads-mcp",
    "args": []
  }
}
```

Then use `mcp__beads__*` functions instead of CLI commands.

### Managing AI-Generated Planning Documents

AI assistants often create planning and design documents during development:

- PLAN.md, IMPLEMENTATION.md, ARCHITECTURE.md
- DESIGN.md, CODEBASE_SUMMARY.md, INTEGRATION_PLAN.md
- TESTING_GUIDE.md, TECHNICAL_DESIGN.md, and similar files

**Best Practice: Use a dedicated directory for these ephemeral files**

**Recommended approach:**

- Create a `history/` directory in the project root
- Store ALL AI-generated planning/design docs in `history/`
- Keep the repository root clean and focused on permanent project files
- Only access `history/` when explicitly asked to review past planning

**Example .gitignore entry (optional):**

```
# AI planning documents (ephemeral)
history/
```

**Benefits:**

- Clean repository root
- Clear separation between ephemeral and permanent documentation
- Easy to exclude from version control if desired
- Preserves planning history for archeological research
- Reduces noise when browsing the project

### CLI Help

Run `bd <command> --help` to see all available flags for any command.
For example: `bd create --help` shows `--parent`, `--deps`, `--assignee`, etc.

### Important Rules

- Use bd for ALL task tracking
- Always use `--json` flag for programmatic use
- Link discovered work with `discovered-from` dependencies
- Check `bd ready` before asking "what should I work on?"
- Store AI planning docs in `history/` directory
- Run `bd <cmd> --help` to discover available flags
- Do NOT create markdown TODO lists
- Do NOT use external issue trackers
- Do NOT duplicate tracking systems
- Do NOT clutter repo root with planning documents

For more details, see README.md and QUICKSTART.md.
