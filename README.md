# python-basics-25BCON1265

# Python Basics Programs

## About

This repository contains six basic Python programs created for
HW-05 of the Prompt Engineering course.

## Programs

1. Factorial - Calculates the factorial of a number.
2. Fibonacci - Generates Fibonacci numbers.
3. Structure - Demonstrates the use of a structure-like approach in Python.
4. Even Odd - Checks whether a number is even or odd.
5. Prime - Checks whether a number is prime.
6. Palindrome - Checks whether a number is a palindrome.

## How to Run

Make sure Python is installed on your computer.

Run a program using:

```bash
python factorial.py
python fibonacci.py
python structure.py
python even_odd.py
python prime.py
python palindrome.py

## Testing

The project uses Python's unittest framework for testing.

### Running Tests

Run the Session 8 tests with:

```bash
python -m unittest session\test_student_utils.py

Test Coverage

The tests cover:

Normal cases
Boundary cases
Edge cases
Incorrect behaviour identified from the specification

The specification-based test suite contains 9 tests.

RED → GREEN

The tests were first run against the buggy implementation and produced 3 failures and 1 error.

After fixing the identified bugs, all 9 tests passed successfully.

AI-Generated Tests

AI-generated tests were also reviewed and compared with the specification-based tests. Some AI-generated expected results reflected the behaviour of the buggy implementation, so the specification was used as the final reference for expected behaviour.
