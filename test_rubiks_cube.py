import pytest
from rubiks_cube import *


def test_rotate_face_clockwise():
    test_cube = [[['w'], ['w'], ['w']], [['w'], ['w'], ['w']], [['o'], ['o'], ['o']], [['o'], ['o'], ['y'], ['g'], ['g'], ['g'], ['w'], ['r'], ['r'], ['b'], ['b'], ['b']], [['o'], ['o'], ['y'], ['g'], ['g'], [
        'g'], ['w'], ['r'], ['r'], ['b'], ['b'], ['b']], [['o'], ['o'], ['y'], ['g'], ['g'], ['g'], ['w'], ['r'], ['r'], ['b'], ['b'], ['b']], [['r'], ['r'], ['r']], [['y'], ['y'], ['y']], [['y'], ['y'], ['y']]]
    comparator_cube = [[['w'], ['w'], ['w']], [['w'], ['w'], ['w']], [['o'], ['o'], ['o']], [['o'], ['o'], ['y'], ['g'], ['g'], ['g'], ['w'], ['r'], ['r'], ['b'], ['b'], ['b']], [['o'], ['o'], ['y'], ['g'], ['g'], [
        'g'], ['w'], ['r'], ['r'], ['b'], ['b'], ['b']], [['o'], ['o'], ['y'], ['g'], ['g'], ['g'], ['w'], ['r'], ['r'], ['b'], ['b'], ['b']], [['r'], ['r'], ['r']], [['y'], ['y'], ['y']], [['y'], ['y'], ['y']]]
    assert rotate_target_face_clockwise(test_cube, 4, 4) == comparator_cube


def test_rotate_front_face_90_degrees_clockwise():
    pass


def test_rotate_right_face_90_degrees_anticlockwise():
    pass


def test_rotate_top_face_90_degrees_clockwise():
    pass


def test_rotate_back_face_90_degrees_anticlockwise():
    test_cube = [[['w'], ['w'], ['w']], [['w'], ['w'], ['w']], [['w'], ['w'], ['w']], [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], ['r'], ['r'], ['r'], ['b'], ['b'], ['b']], [['o'], ['o'], ['o'], ['g'], ['g'], [
        'g'], ['r'], ['r'], ['r'], ['b'], ['b'], ['b']], [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], ['r'], ['r'], ['r'], ['b'], ['b'], ['b']], [['y'], ['y'], ['y']], [['y'], ['y'], ['y']], [['y'], ['y'], ['y']]]
    comparator_cube = [[['o'], ['o'], ['o']], [['w'], ['w'], ['w']], [['w'], ['w'], ['w']], [['y'], ['o'], ['o'], ['g'], ['g'], ['g'], ['r'], ['r'], ['w'], ['b'], ['b'], ['b']], [['y'], ['o'], ['o'], ['g'], ['g'], [
        'g'], ['r'], ['r'], ['w'], ['b'], ['b'], ['b']], [['y'], ['o'], ['o'], ['g'], ['g'], ['g'], ['r'], ['r'], ['w'], ['b'], ['b'], ['b']], [['y'], ['y'], ['y']], [['y'], ['y'], ['y']], [['r'], ['r'], ['r']]]
    assert rotate_back_face_90_degrees_anticlockwise(
        test_cube) == comparator_cube


def test_rotate_left_face_90_degrees_clockwise():
    pass


def test_rotate_down_face_90_degrees_anticlockwise():
    pass


def test_print_rubiks_cube_layout():
    pass
