🎯 **What:** The testing gap addressed was that the error handling in `_apply_levelup_hp_increase` for parsing `hit_dice` (handling `ValueError` and `IndexError`) was previously untested.
📊 **Coverage:** A new test case `test_levelup_invalid_hit_dice_logs_warning` was added to `CharacterLevelupTest`, ensuring that invalid hit dice formats trigger a warning log and do not crash the application or increment HP inappropriately.
✨ **Result:** Test coverage for `_apply_levelup_hp_increase` is now complete regarding exceptions parsing `hit_dice`, with 100% test pass rates across the suite.
