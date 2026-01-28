# RepoGym-RL Demo: Measurable Results

This demo showcases the quantifiable nature of the RepoGym-RL environment using a string utility bugfix task.

## Baseline Metrics
- **Initial Task**: `kebab_to_camel` conversion (Buggy).
- **Test Status**: 1/1 FAILED.
- **Initial Reward**: -1.0 (Functional penalty for failing tests).

## Improvement Action
- **Agent Action**: `write_file` with corrected logic using string slicing and capitalization.
- **Static Quality Bonus**: +0.0214 (Reward based on improved Maintainability Index).

## Final Metrics
- **Final Test Status**: 1/1 PASSED.
- **Functional Reward**: +1.0.
- **Total trajectory length**: 3 steps.

## Verification
The demo confirms that the environment successfully:
1. Detects and punishes logic errors through unit tests.
2. Identifies and rewards code quality improvements via static analysis.
3. Provides a direct, measurable signal for agent success.
