# Tests

Each exercise supplies the unit tests and a Make build recipe.
You provide the implementation.

Each test file is meant to link against your implementation to provide a console executable that runs the tests.
Running the test executable prints messages for each failing test and reports a non-zero exit status when tests fail.

To work through an exercise:
* Create the initial build with Make
* For each unit test:
  * Remove the `TEST_IGNORE()` line.
  * Satisfy any compile errors to make the test fail.
  * Implement just enough to make the test pass.
  * Refactor your implementation to enhance readability, reduce duplication, etc.
