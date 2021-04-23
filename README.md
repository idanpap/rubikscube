# Rubiks Cube

Rubiks Cube is a program that simulates a Rubik's cube and is delivered through the console

It is built using Python.

It offers basic functionality, with the user starting with a completed Rubik's cube and can perform the following actions:

- Rotate the front face clockwise 90 degrees
- Rotate the right face anti-clockwise 90 degrees
- Rotate the up face clockwise 90 degrees
- Rotate the back face anti-clockwise 90 degrees
- Rotate the left face clockwise 90 degrees
- Rotate the down face anti-clockwise 90 degrees

The program contains two files:

- The main file, named `rubiks_cube.py`, which runs the program and the file contaning tests, named `test_rubiks_cube.py`

## Installation

Navigate into the folder using the console.

Make sure you have [Python](https://www.python.org/) installed on your machine. You can do this by entering the following command in the console:

```bash
python --version
```

If you want to run all the tests, use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pytest](https://pypi.org/project/pytest/).

```bash
pip install pytest
```

and enter

```bash
pytest
```

into the console to run the tests.

## Usage

After navigating to the file containing the program on the console, please enter the following in order to run the program:

```bash
python3 rubiks_cube.py
```

You will presented with a prompt in the console to enter a specific input in order to manipulate the rubiks cube.

The rubik's cube is presented in the console in its exploded view. Each face contans 3 x 3 cells.

From left to right, as presented in the console, these are the faces and how they are referred to in the program:

```python
    top
left front right back
    bottom
```

The colours are represented by their initials:

- r = Red
- g = Green
- w = White
- b = Blue
- y = Yellow
- o = Orange

In order to use the program, these are the controls. Enter each value in the console and press enter and the updated cube will be printed to it:

- Rotate the front face clockwise 90 degrees

```bash
f
```

- Rotate the right face anti-clockwise 90 degrees

```bash
r*
```

- Rotate the up face clockwise 90 degrees

```bash
u
```

- Rotate the back face anti-clockwise 90 degrees

```bash
b*
```

- Rotate the left face clockwise 90 degrees

```bash
l
```

- Rotate the down face anti-clockwise 90 degrees

```bash
d*
```

- Stop the program

```bash
stop
```

- Any other input will print the instructions to the console.

## Questions

If you have any questions about this program, please contact me via the links on my profile.

Thank you!
