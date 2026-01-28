# Phase 3 Plan 1: Action Space Schemas Summary

**Defined structured tool-call schemas using Pydantic.**

## Accomplishments

- Created `src/repogym/actions.py`.
- Implemented Pydantic models for `ListFiles`, `ReadFile`, `WriteFile`, `RunTests`, and `RunCommand`.
- Established a discriminated union `Action` for type-safe parsing of JSON tool-calls.
- Verified schema serialization and validation.

## Files Created/Modified

- `src/repogym/actions.py` - Action schema definitions.

## Decisions Made

- Use `Literal` for command names to enable discriminated union parsing in Pydantic.
- Include an `ActionWrapper` to simplify JSON parsing of the union type.

## Issues Encountered

- None.

## Next Step

Ready for 03-02-PLAN.md: Action dispatcher implementation.
