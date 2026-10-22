Lecture 8 – Fixing a Buggy Python Script

Project Description

This project demonstrates testing and debugging a Python program using AI guidance and Python unittest.

Files

- "student_utils.py" – Contains functions to calculate averages, check passing marks, and assign grades.
- "test_student_utils.py" – Contains nine unit tests to check the program's correctness.
- "bug_notes.md" – Records the bugs, causes, and fixes.
- "audit.md" – Records the code review and remaining test gaps.

Bugs Fixed

1. Corrected the average calculation to divide by the number of marks.
2. Changed the passing condition to ">= 40".
3. Checked the Distinction grade before the lower grade conditions.

How to Run the Tests

Run this command in Google Colab:

"!python test_student_utils.py"

Testing Process

- RED: Tests reveal bugs in the original program.
- FIX: Correct the code without changing the tests.
- GREEN: Run the same nine tests again to confirm they pass.

Final Result

The goal is for all nine tests to pass after the corrections.
