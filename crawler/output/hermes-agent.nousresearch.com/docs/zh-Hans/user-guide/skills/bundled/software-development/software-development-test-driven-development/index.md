<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development -->

本页总览
TDD: enforce RED-GREEN-REFACTOR, tests before code.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/software-development/test-driven-development`  |  
| Version  | `1.1.0`  |  
| Author  | Hermes Agent (adapted from obra/superpowers)  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `testing`, `tdd`, `development`, `quality`, `red-green-refactor`  |  
| Related skills  |  [`systematic-debugging`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/software-development/software-development-systematic-debugging), [`writing-plans`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/software-development/software-development-writing-plans), [`subagent-driven-development`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/software-development/software-development-subagent-driven-development)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Test-Driven Development (TDD)
## Overview[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#overview "Overview的直接链接")
Write the test first. Watch it fail. Write minimal code to pass.
**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.
**Violating the letter of the rules is violating the spirit of the rules.**
## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#when-to-use "When to Use的直接链接")
**Always:**
  * New features
  * Bug fixes
  * Refactoring
  * Behavior changes


**Exceptions (ask the user first):**
  * Throwaway prototypes
  * Generated code
  * Configuration files


Thinking "skip TDD just this once"? Stop. That's rationalization.
## The Iron Law[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#the-iron-law "The Iron Law的直接链接")

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.
**No exceptions:**
  * Don't keep it as "reference"
  * Don't "adapt" it while writing tests
  * Don't look at it
  * Delete means delete


Implement fresh from tests. Period.
## Red-Green-Refactor Cycle[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#red-green-refactor-cycle "Red-Green-Refactor Cycle的直接链接")
### RED — Write Failing Test[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#red--write-failing-test "RED — Write Failing Test的直接链接")
Write one minimal test showing what should happen.
**Good test:**

```
deftest_retries_failed_operations_3_times():    attempts =0defoperation():nonlocal attempts        attempts +=1if attempts <3:raise Exception('fail')return'success'    result = retry_operation(operation)assert result =='success'assert attempts ==3
```

Clear name, tests real behavior, one thing.
**Bad test:**

```
deftest_retry_works():    mock = MagicMock()    mock.side_effect =[Exception(), Exception(),'success']    result = retry_operation(mock)assert result =='success'# What about retry count? Timing?
```

Vague name, tests mock not real code.
**Requirements:**
  * One behavior per test
  * Clear descriptive name ("and" in name? Split it)
  * Real code, not mocks (unless truly unavoidable)
  * Name describes behavior, not implementation


### Verify RED — Watch It Fail[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#verify-red--watch-it-fail "Verify RED — Watch It Fail的直接链接")
**MANDATORY. Never skip.**

```
# Use terminal tool to run the specific testpytest tests/test_feature.py::test_specific_behavior -v
```

Confirm:
  * Test fails (not errors from typos)
  * Failure message is expected
  * Fails because the feature is missing


**Test passes immediately?** You're testing existing behavior. Fix the test.
**Test errors?** Fix the error, re-run until it fails correctly.
### GREEN — Minimal Code[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#green--minimal-code "GREEN — Minimal Code的直接链接")
Write the simplest code to pass the test. Nothing more.
**Good:**

```
defadd(a, b):return a + b  # Nothing extra
```

**Bad:**

```
defadd(a, b):    result = a + b    logging.info(f"Adding {a} + {b} = {result}")# Extra!return result
```

Don't add features, refactor other code, or "improve" beyond the test.
**Cheating is OK in GREEN:**
  * Hardcode return values
  * Copy-paste
  * Duplicate code
  * Skip edge cases


We'll fix it in REFACTOR.
### Verify GREEN — Watch It Pass[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#verify-green--watch-it-pass "Verify GREEN — Watch It Pass的直接链接")
**MANDATORY.**

```
# Run the specific testpytest tests/test_feature.py::test_specific_behavior -v# Then run ALL tests to check for regressionspytest tests/ -q
```

Confirm:
  * Test passes
  * Other tests still pass
  * Output pristine (no errors, warnings)


**Test fails?** Fix the code, not the test.
**Other tests fail?** Fix regressions now.
### REFACTOR — Clean Up[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#refactor--clean-up "REFACTOR — Clean Up的直接链接")
After green only:
  * Remove duplication
  * Improve names
  * Extract helpers
  * Simplify expressions


Keep tests green throughout. Don't add behavior.
**If tests fail during refactor:** Undo immediately. Take smaller steps.
### Repeat[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#repeat "Repeat的直接链接")
Next failing test for next behavior. One cycle at a time.
## Why Order Matters[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#why-order-matters "Why Order Matters的直接链接")
**"I'll write tests after to verify it works"**
Tests written after code pass immediately. Passing immediately proves nothing:
  * Might test the wrong thing
  * Might test implementation, not behavior
  * Might miss edge cases you forgot
  * You never saw it catch the bug


Test-first forces you to see the test fail, proving it actually tests something.
**"I already manually tested all the edge cases"**
Manual testing is ad-hoc. You think you tested everything but:
  * No record of what you tested
  * Can't re-run when code changes
  * Easy to forget cases under pressure
  * "It worked when I tried it" ≠ comprehensive


Automated tests are systematic. They run the same way every time.
**"Deleting X hours of work is wasteful"**
Sunk cost fallacy. The time is already gone. Your choice now:
  * Delete and rewrite with TDD (high confidence)
  * Keep it and add tests after (low confidence, likely bugs)


The "waste" is keeping code you can't trust.
**"TDD is dogmatic, being pragmatic means adapting"**
TDD IS pragmatic:
  * Finds bugs before commit (faster than debugging after)
  * Prevents regressions (tests catch breaks immediately)
  * Documents behavior (tests show how to use code)
  * Enables refactoring (change freely, tests catch breaks)


"Pragmatic" shortcuts = debugging in production = slower.
**"Tests after achieve the same goals — it's spirit not ritual"**
No. Tests-after answer "What does this do?" Tests-first answer "What should this do?"
Tests-after are biased by your implementation. You test what you built, not what's required. Tests-first force edge case discovery before implementing.
## Common Rationalizations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#common-rationalizations "Common Rationalizations的直接链接")  
| Excuse  | Reality  |  
| --- | --- |  
| "Too simple to test"  | Simple code breaks. Test takes 30 seconds.  |  
| "I'll test after"  | Tests passing immediately prove nothing.  |  
| "Tests after achieve same goals"  | Tests-after = "what does this do?" Tests-first = "what should this do?"  |  
| "Already manually tested"  | Ad-hoc ≠ systematic. No record, can't re-run.  |  
| "Deleting X hours is wasteful"  | Sunk cost fallacy. Keeping unverified code is technical debt.  |  
| "Keep as reference, write tests first"  | You'll adapt it. That's testing after. Delete means delete.  |  
| "Need to explore first"  | Fine. Throw away exploration, start with TDD.  |  
| "Test hard = design unclear"  | Listen to the test. Hard to test = hard to use.  |  
| "TDD will slow me down"  | TDD faster than debugging. Pragmatic = test-first.  |  
| "Manual test faster"  | Manual doesn't prove edge cases. You'll re-test every change.  |  
| "Existing code has no tests"  | You're improving it. Add tests for the code you touch.  |  
## Red Flags — STOP and Start Over[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#red-flags--stop-and-start-over "Red Flags — STOP and Start Over的直接链接")
If you catch yourself doing any of these, delete the code and restart with TDD:
  * Code before test
  * Test after implementation
  * Test passes immediately on first run
  * Can't explain why test failed
  * Tests added "later"
  * Rationalizing "just this once"
  * "I already manually tested it"
  * "Tests after achieve the same purpose"
  * "Keep as reference" or "adapt existing code"
  * "Already spent X hours, deleting is wasteful"
  * "TDD is dogmatic, I'm being pragmatic"
  * "This is different because..."


**All of these mean: Delete code. Start over with TDD.**
## Verification Checklist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#verification-checklist "Verification Checklist的直接链接")
Before marking work complete:
  * Every new function/method has a test
  * Watched each test fail before implementing
  * Each test failed for expected reason (feature missing, not typo)
  * Wrote minimal code to pass each test
  * All tests pass
  * Output pristine (no errors, warnings)
  * Tests use real code (mocks only if unavoidable)
  * Edge cases and errors covered


Can't check all boxes? You skipped TDD. Start over.
## When Stuck[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#when-stuck "When Stuck的直接链接")  
| Problem  | Solution  |  
| --- | --- |  
| Don't know how to test  | Write the wished-for API. Write the assertion first. Ask the user.  |  
| Test too complicated  | Design too complicated. Simplify the interface.  |  
| Must mock everything  | Code too coupled. Use dependency injection.  |  
| Test setup huge  | Extract helpers. Still complex? Simplify the design.  |  
## Hermes Agent Integration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#hermes-agent-integration "Hermes Agent Integration的直接链接")
### Running Tests[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#running-tests "Running Tests的直接链接")
Use the `terminal` tool to run tests at each step:

```
# RED — verify failureterminal("pytest tests/test_feature.py::test_name -v")# GREEN — verify passterminal("pytest tests/test_feature.py::test_name -v")# Full suite — verify no regressionsterminal("pytest tests/ -q")
```

### With delegate_task[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#with-delegate_task "With delegate_task的直接链接")
When dispatching subagents for implementation, enforce TDD in the goal:

```
delegate_task(    goal="Implement [feature] using strict TDD",    context="""    Follow test-driven-development skill:    1. Write failing test FIRST    2. Run test to verify it fails    3. Write minimal code to pass    4. Run test to verify it passes    5. Refactor if needed    6. Commit    Project test command: pytest tests/ -q    Project structure: [describe relevant files]    """,    toolsets=['terminal','file']
```

### With systematic-debugging[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#with-systematic-debugging "With systematic-debugging的直接链接")
Bug found? Write failing test reproducing it. Follow TDD cycle. The test proves the fix and prevents regression.
Never fix bugs without a test.
## Testing Anti-Patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#testing-anti-patterns "Testing Anti-Patterns的直接链接")
  * **Testing mock behavior instead of real behavior** — mocks should verify interactions, not replace the system under test
  * **Testing implementation details** — test behavior/results, not internal method calls
  * **Happy path only** — always test edge cases, errors, and boundaries
  * **Brittle tests** — tests should verify behavior, not structure; refactoring shouldn't break them


## Final Rule[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#final-rule "Final Rule的直接链接")

```
Production code → test exists and failed firstOtherwise → not TDD
```

No exceptions without the user's explicit permission.
  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#when-to-use)
  * [The Iron Law](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#the-iron-law)
  * [Red-Green-Refactor Cycle](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#red-green-refactor-cycle)
    * [RED — Write Failing Test](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#red--write-failing-test)
    * [Verify RED — Watch It Fail](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#verify-red--watch-it-fail)
    * [GREEN — Minimal Code](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#green--minimal-code)
    * [Verify GREEN — Watch It Pass](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#verify-green--watch-it-pass)
    * [REFACTOR — Clean Up](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#refactor--clean-up)
  * [Why Order Matters](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#why-order-matters)
  * [Common Rationalizations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#common-rationalizations)
  * [Red Flags — STOP and Start Over](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#red-flags--stop-and-start-over)
  * [Verification Checklist](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#verification-checklist)
  * [Hermes Agent Integration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#hermes-agent-integration)
    * [Running Tests](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#running-tests)
    * [With delegate_task](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#with-delegate_task)
    * [With systematic-debugging](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#with-systematic-debugging)
  * [Testing Anti-Patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/software-development/software-development-test-driven-development#testing-anti-patterns)


