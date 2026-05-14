<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#__docusaurus_skipToContent_fallback)
On this page
Write implementation plans: bite-sized tasks, paths, code.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/software-development/writing-plans`  |  
| Version  | `1.1.0`  |  
| Author  | Hermes Agent (adapted from obra/superpowers)  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `planning`, `design`, `implementation`, `workflow`, `documentation`  |  
| Related skills  |  [`subagent-driven-development`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development), [`test-driven-development`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-test-driven-development), [`requesting-code-review`](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-requesting-code-review)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Writing Implementation Plans
## Overview[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#overview "Direct link to Overview")
Write comprehensive implementation plans assuming the implementer has zero context for the codebase and questionable taste. Document everything they need: which files to touch, complete code, testing commands, docs to check, how to verify. Give them bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.
Assume the implementer is a skilled developer but knows almost nothing about the toolset or problem domain. Assume they don't know good test design very well.
**Core principle:** A good plan makes implementation obvious. If someone has to guess, the plan is incomplete.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#when-to-use "Direct link to When to Use")
**Always use before:**
  * Implementing multi-step features
  * Breaking down complex requirements
  * Delegating to subagents via subagent-driven-development


**Don't skip when:**
  * Feature seems simple (assumptions cause bugs)
  * You plan to implement it yourself (future you needs guidance)
  * Working alone (documentation matters)


## Bite-Sized Task Granularity[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#bite-sized-task-granularity "Direct link to Bite-Sized Task Granularity")
**Each task = 2-5 minutes of focused work.**
Every step is one action:
  * "Write the failing test" — step
  * "Run it to make sure it fails" — step
  * "Implement the minimal code to make the test pass" — step
  * "Run the tests and make sure they pass" — step
  * "Commit" — step


**Too big:**

```
### Task 1: Build authentication system[50 lines of code across 5 files]
```

**Right size:**

```
### Task 1: Create User model with email field[10 lines, 1 file]### Task 2: Add password hash field to User[8 lines, 1 file]### Task 3: Create password hashing utility[15 lines, 1 file]
```

## Plan Document Structure[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#plan-document-structure "Direct link to Plan Document Structure")
### Header (Required)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#header-required "Direct link to Header \(Required\)")
Every plan MUST start with:

```
# [Feature Name] Implementation Plan>**For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.**Goal:** [One sentence describing what this builds]**Architecture:** [2-3 sentences about approach]**Tech Stack:** [Key technologies/libraries]---
```

### Task Structure[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#task-structure "Direct link to Task Structure")
Each task follows this format:

```
### Task N: [Descriptive Name]**Objective:** What this task accomplishes (one sentence)**Files:**- Create: `exact/path/to/new_file.py`- Modify: `exact/path/to/existing.py:45-67` (line numbers if known)- Test: `tests/path/to/test_file.py`**Step 1: Write failing test**```pythondef test_specific_behavior():    result = function(input)    assert result == expected```**Step 2: Run test to verify failure**Run: `pytest tests/path/test.py::test_specific_behavior -v`Expected: FAIL — "function not defined"**Step 3: Write minimal implementation**```pythondef function(input):    return expected```**Step 4: Run test to verify pass**Run: `pytest tests/path/test.py::test_specific_behavior -v`Expected: PASS**Step 5: Commit**```bashgit add tests/path/test.py src/path/file.pygit commit -m "feat: add specific feature"```
```

## Writing Process[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#writing-process "Direct link to Writing Process")
### Step 1: Understand Requirements[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-1-understand-requirements "Direct link to Step 1: Understand Requirements")
Read and understand:
  * Feature requirements
  * Design documents or user description
  * Acceptance criteria
  * Constraints


### Step 2: Explore the Codebase[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-2-explore-the-codebase "Direct link to Step 2: Explore the Codebase")
Use Hermes tools to understand the project:

```
# Understand project structuresearch_files("*.py", target="files", path="src/")# Look at similar featuressearch_files("similar_pattern", path="src/", file_glob="*.py")# Check existing testssearch_files("*.py", target="files", path="tests/")# Read key filesread_file("src/app.py")
```

### Step 3: Design Approach[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-3-design-approach "Direct link to Step 3: Design Approach")
Decide:
  * Architecture pattern
  * File organization
  * Dependencies needed
  * Testing strategy


### Step 4: Write Tasks[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-4-write-tasks "Direct link to Step 4: Write Tasks")
Create tasks in order:
  1. Setup/infrastructure
  2. Core functionality (TDD for each)
  3. Edge cases
  4. Integration
  5. Cleanup/documentation


### Step 5: Add Complete Details[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-5-add-complete-details "Direct link to Step 5: Add Complete Details")
For each task, include:
  * **Exact file paths** (not "the config file" but `src/config/settings.py`)
  * **Complete code examples** (not "add validation" but the actual code)
  * **Exact commands** with expected output
  * **Verification steps** that prove the task works


### Step 6: Review the Plan[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-6-review-the-plan "Direct link to Step 6: Review the Plan")
Check:
  * Tasks are sequential and logical
  * Each task is bite-sized (2-5 min)
  * File paths are exact
  * Code examples are complete (copy-pasteable)
  * Commands are exact with expected output
  * No missing context
  * DRY, YAGNI, TDD principles applied


### Step 7: Save the Plan[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-7-save-the-plan "Direct link to Step 7: Save the Plan")

```
mkdir-p docs/plans# Save plan to docs/plans/YYYY-MM-DD-feature-name.mdgitadd docs/plans/git commit -m"docs: add implementation plan for [feature]"
```

## Principles[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#principles "Direct link to Principles")
### DRY (Don't Repeat Yourself)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#dry-dont-repeat-yourself "Direct link to DRY \(Don't Repeat Yourself\)")
**Bad:** Copy-paste validation in 3 places **Good:** Extract validation function, use everywhere
### YAGNI (You Aren't Gonna Need It)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#yagni-you-arent-gonna-need-it "Direct link to YAGNI \(You Aren't Gonna Need It\)")
**Bad:** Add "flexibility" for future requirements **Good:** Implement only what's needed now

```
# Bad — YAGNI violationclassUser:def__init__(self, name, email):        self.name = name        self.email = email        self.preferences ={}# Not needed yet!        self.metadata ={}# Not needed yet!# Good — YAGNIclassUser:def__init__(self, name, email):        self.name = name        self.email = email
```

### TDD (Test-Driven Development)[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#tdd-test-driven-development "Direct link to TDD \(Test-Driven Development\)")
Every task that produces code should include the full TDD cycle:
  1. Write failing test
  2. Run to verify failure
  3. Write minimal code
  4. Run to verify pass


See `test-driven-development` skill for details.
### Frequent Commits[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#frequent-commits "Direct link to Frequent Commits")
Commit after every task:

```
gitadd[files]git commit -m"type: description"
```

## Common Mistakes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#common-mistakes "Direct link to Common Mistakes")
### Vague Tasks[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#vague-tasks "Direct link to Vague Tasks")
**Bad:** "Add authentication" **Good:** "Create User model with email and password_hash fields"
### Incomplete Code[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#incomplete-code "Direct link to Incomplete Code")
**Bad:** "Step 1: Add validation function" **Good:** "Step 1: Add validation function" followed by the complete function code
### Missing Verification[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#missing-verification "Direct link to Missing Verification")
**Bad:** "Step 3: Test it works" **Good:** "Step 3: Run `pytest tests/test_auth.py -v`, expected: 3 passed"
### Missing File Paths[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#missing-file-paths "Direct link to Missing File Paths")
**Bad:** "Create the model file" **Good:** "Create: `src/models/user.py`"
## Execution Handoff[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#execution-handoff "Direct link to Execution Handoff")
After saving the plan, offer the execution approach:
**"Plan complete and saved. Ready to execute using subagent-driven-development — I'll dispatch a fresh subagent per task with two-stage review (spec compliance then code quality). Shall I proceed?"**
When executing, use the `subagent-driven-development` skill:
  * Fresh `delegate_task` per task with full context
  * Spec compliance review after each task
  * Code quality review after spec passes
  * Proceed only when both reviews approve


## Remember[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#remember "Direct link to Remember")

```
Bite-sized tasks (2-5 min each)Exact file pathsComplete code (copy-pasteable)Exact commands with expected outputVerification stepsDRY, YAGNI, TDDFrequent commits
```

**A good plan makes implementation obvious.**
  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#when-to-use)
  * [Bite-Sized Task Granularity](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#bite-sized-task-granularity)
  * [Plan Document Structure](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#plan-document-structure)
    * [Header (Required)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#header-required)
    * [Task Structure](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#task-structure)
  * [Writing Process](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#writing-process)
    * [Step 1: Understand Requirements](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-1-understand-requirements)
    * [Step 2: Explore the Codebase](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-2-explore-the-codebase)
    * [Step 3: Design Approach](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-3-design-approach)
    * [Step 4: Write Tasks](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-4-write-tasks)
    * [Step 5: Add Complete Details](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-5-add-complete-details)
    * [Step 6: Review the Plan](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-6-review-the-plan)
    * [Step 7: Save the Plan](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#step-7-save-the-plan)
  * [Principles](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#principles)
    * [DRY (Don't Repeat Yourself)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#dry-dont-repeat-yourself)
    * [YAGNI (You Aren't Gonna Need It)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#yagni-you-arent-gonna-need-it)
    * [TDD (Test-Driven Development)](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#tdd-test-driven-development)
    * [Frequent Commits](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#frequent-commits)
  * [Common Mistakes](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#common-mistakes)
    * [Vague Tasks](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#vague-tasks)
    * [Incomplete Code](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#incomplete-code)
    * [Missing Verification](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#missing-verification)
    * [Missing File Paths](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#missing-file-paths)
  * [Execution Handoff](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-writing-plans#execution-handoff)


