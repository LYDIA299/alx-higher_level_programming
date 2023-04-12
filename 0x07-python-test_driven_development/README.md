## 0x07. Python - Test-driven development
This enables you to test the functionality of your code during developement
There are two ways to test your code in python
1) using doctest
2) using unittest

### doctest
doctest tests source code by running examples embedded in the documentation and
verifying that they produce the expected results.
It works by parsing the help text to find examples, running them, then comparing
the output text against the expected value.

### unittest
Unittest test case runners allow more options when running tests, like reporting
test statistics such as tests that passed and failed.