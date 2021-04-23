import copy

# method to rotate a face clockwise 90 degrees.
# Each tile on the face is replaced by one one two positions down, in a clockwise manner


def rotate_target_face_clockwise(rubiks_cube_layout, ynum, xnum):
    # method to rotate a face clockwise 90 degrees.
    # Each tile on the face is replaced by one one two positions down, in a clockwise manner

    # saves values that will be replaced to be used further down
    placeholder_values = [rubiks_cube_layout[ynum-1]
                          [xnum-1], rubiks_cube_layout[ynum][xnum-1]]
    rubiks_cube_layout[ynum-1][xnum -
                               1] = copy.deepcopy(rubiks_cube_layout[ynum+1][xnum-1])
    rubiks_cube_layout[ynum][xnum -
                             1] = copy.deepcopy(rubiks_cube_layout[ynum+1][xnum])
    rubiks_cube_layout[ynum+1][xnum -
                               1] = copy.deepcopy(rubiks_cube_layout[ynum+1][xnum+1])
    rubiks_cube_layout[ynum +
                       1][xnum] = copy.deepcopy(rubiks_cube_layout[ynum][xnum+1])
    rubiks_cube_layout[ynum+1][xnum +
                               1] = copy.deepcopy(rubiks_cube_layout[ynum-1][xnum+1])
    rubiks_cube_layout[ynum][xnum +
                             1] = copy.deepcopy(rubiks_cube_layout[ynum-1][xnum])
    rubiks_cube_layout[ynum-1][xnum] = copy.deepcopy(placeholder_values[1])
    rubiks_cube_layout[ynum-1][xnum+1] = copy.deepcopy(placeholder_values[0])
    return rubiks_cube_layout


def rotate_target_face_anticlockwise(rubiks_cube_layout, ynum, xnum):
    # method to rotate a tile anticlockwise 90 degrees
    # Each tile on the face is replaced by one one two positions down, in an anticlockwise manner

    # saves values that will be replaced to be used further down
    placeholder_values = [rubiks_cube_layout[ynum-1]
                          [xnum-1], rubiks_cube_layout[ynum-1][xnum]]
    rubiks_cube_layout[ynum-1][xnum -
                               1] = copy.deepcopy(rubiks_cube_layout[ynum-1][xnum+1])
    rubiks_cube_layout[ynum -
                       1][xnum] = copy.deepcopy(rubiks_cube_layout[ynum][xnum+1])
    rubiks_cube_layout[ynum-1][xnum +
                               1] = copy.deepcopy(rubiks_cube_layout[ynum+1][xnum+1])
    rubiks_cube_layout[ynum][xnum +
                             1] = copy.deepcopy(rubiks_cube_layout[ynum+1][xnum])
    rubiks_cube_layout[ynum+1][xnum +
                               1] = copy.deepcopy(rubiks_cube_layout[ynum+1][xnum-1])
    rubiks_cube_layout[ynum +
                       1][xnum] = copy.deepcopy(rubiks_cube_layout[ynum][xnum-1])
    rubiks_cube_layout[ynum+1][xnum-1] = copy.deepcopy(placeholder_values[0])
    rubiks_cube_layout[ynum][xnum-1] = copy.deepcopy(placeholder_values[1])
    return rubiks_cube_layout


def rotate_front_face_90_degrees_clockwise(rubiks_cube_layout):
    # saves values that will be replaced to be used further down
    placeholder_value = copy.deepcopy(rubiks_cube_layout[2])

    # bottom cells on top face take values of the righmost cells of the left face
    rubiks_cube_layout[2][0] = copy.deepcopy(rubiks_cube_layout[5][2])
    rubiks_cube_layout[2][1] = copy.deepcopy(rubiks_cube_layout[4][2])
    rubiks_cube_layout[2][2] = copy.deepcopy(rubiks_cube_layout[3][2])

    # righmost cells on left face take values of the top cells of the down face
    rubiks_cube_layout[5][2] = copy.deepcopy(rubiks_cube_layout[6][2])
    rubiks_cube_layout[4][2] = copy.deepcopy(rubiks_cube_layout[6][1])
    rubiks_cube_layout[3][2] = copy.deepcopy(rubiks_cube_layout[6][0])

    # topmost cells on down face take values of the left cells of the right face
    rubiks_cube_layout[6][0] = copy.deepcopy(rubiks_cube_layout[5][6])
    rubiks_cube_layout[6][1] = copy.deepcopy(rubiks_cube_layout[4][6])
    rubiks_cube_layout[6][2] = copy.deepcopy(rubiks_cube_layout[3][6])

    # left cells of the right face take old values of bottom cells of top face that where saved to placeholders
    rubiks_cube_layout[3][6] = copy.deepcopy(placeholder_value[0])
    rubiks_cube_layout[4][6] = copy.deepcopy(placeholder_value[1])
    rubiks_cube_layout[5][6] = copy.deepcopy(placeholder_value[2])

    rubiks_cube_layout = rotate_target_face_clockwise(rubiks_cube_layout, 4, 4)
    return rubiks_cube_layout


def rotate_right_face_90_degrees_anticlockwise(rubiks_cube_layout):
    # saves values that will be replaced to be used further down
    placeholder_value = [copy.deepcopy(rubiks_cube_layout[0][2]), copy.deepcopy(
        rubiks_cube_layout[1][2]), copy.deepcopy(rubiks_cube_layout[2][2])]

    # righmost cells on top face take values of the left cells of the back face
    rubiks_cube_layout[0][2] = copy.deepcopy(rubiks_cube_layout[5][9])
    rubiks_cube_layout[1][2] = copy.deepcopy(rubiks_cube_layout[4][9])
    rubiks_cube_layout[2][2] = copy.deepcopy(rubiks_cube_layout[3][9])

    # left cells of the back face take values of right cells of bottom face
    rubiks_cube_layout[3][9] = copy.deepcopy(rubiks_cube_layout[8][2])
    rubiks_cube_layout[4][9] = copy.deepcopy(rubiks_cube_layout[7][2])
    rubiks_cube_layout[5][9] = copy.deepcopy(rubiks_cube_layout[6][2])

    # right cells of bottom face take values of right cells of front face
    rubiks_cube_layout[8][2] = copy.deepcopy(rubiks_cube_layout[5][5])
    rubiks_cube_layout[7][2] = copy.deepcopy(rubiks_cube_layout[4][5])
    rubiks_cube_layout[6][2] = copy.deepcopy(rubiks_cube_layout[3][5])

    # right cells of the front face take old values of right cells of top face that where saved to placeholders
    rubiks_cube_layout[5][5] = placeholder_value[2]
    rubiks_cube_layout[4][5] = placeholder_value[1]
    rubiks_cube_layout[3][5] = placeholder_value[0]

    rubiks_cube_layout = rotate_target_face_anticlockwise(
        rubiks_cube_layout, 4, 7)
    return rubiks_cube_layout


def rotate_top_face_90_degrees_clockwise(rubiks_cube_layout):
    # saves values that will be replaced to be used further down
    placeholder_value = copy.deepcopy(rubiks_cube_layout[3][:3])

    # the loop replaces the top cells of the left, front, right faces with the cell 3 index ahead
    for i in range(9):
        rubiks_cube_layout[3][i] = copy.deepcopy(rubiks_cube_layout[3][i+3])

    # top cells of the back face take old values of top cells of left face that where saved to placeholders
    rubiks_cube_layout[3][9:] = placeholder_value

    rubiks_cube_layout = rotate_target_face_clockwise(rubiks_cube_layout, 1, 1)
    return rubiks_cube_layout


def rotate_back_face_90_degrees_anticlockwise(rubiks_cube_layout):
    # saves values that will be replaced to be used further down
    placeholder_values = copy.deepcopy(rubiks_cube_layout[0])

    # top cells of top face take values of left cells of left face
    rubiks_cube_layout[0][0] = copy.deepcopy(rubiks_cube_layout[5][0])
    rubiks_cube_layout[0][1] = copy.deepcopy(rubiks_cube_layout[4][0])
    rubiks_cube_layout[0][2] = copy.deepcopy(rubiks_cube_layout[3][0])

    # colours on left take colours of bottom
    # left cells of left face take values of bottom cells of down face
    rubiks_cube_layout[3][0] = copy.deepcopy(rubiks_cube_layout[8][0])
    rubiks_cube_layout[4][0] = copy.deepcopy(rubiks_cube_layout[8][1])
    rubiks_cube_layout[5][0] = copy.deepcopy(rubiks_cube_layout[8][2])

    # bottom cells of down face take values of right cells of right face
    rubiks_cube_layout[8][0] = copy.deepcopy(rubiks_cube_layout[5][8])
    rubiks_cube_layout[8][1] = copy.deepcopy(rubiks_cube_layout[4][8])
    rubiks_cube_layout[8][2] = copy.deepcopy(rubiks_cube_layout[3][8])

    # right cells of the right face take old values of top cells of top face that where saved to placeholders
    rubiks_cube_layout[3][8] = copy.deepcopy(placeholder_values[0])
    rubiks_cube_layout[4][8] = copy.deepcopy(placeholder_values[1])
    rubiks_cube_layout[5][8] = copy.deepcopy(placeholder_values[2])

    rubiks_cube_layout = rotate_target_face_anticlockwise(
        rubiks_cube_layout, 4, 10)
    return rubiks_cube_layout


def rotate_left_face_90_degrees_clockwise(rubiks_cube_layout):
    # saves values that will be replaced to be used further down
    placeholder_values = [rubiks_cube_layout[3][11],
                          rubiks_cube_layout[4][11], rubiks_cube_layout[5][11]]

    # right cells of back face take values of left cells of down face
    rubiks_cube_layout[3][11] = copy.deepcopy(rubiks_cube_layout[8][0])
    rubiks_cube_layout[4][11] = copy.deepcopy(rubiks_cube_layout[7][0])
    rubiks_cube_layout[5][11] = copy.deepcopy(rubiks_cube_layout[6][0])

    # right cells of down face take values of left cells of front face
    rubiks_cube_layout[6][0] = copy.deepcopy(rubiks_cube_layout[3][3])
    rubiks_cube_layout[7][0] = copy.deepcopy(rubiks_cube_layout[4][3])
    rubiks_cube_layout[8][0] = copy.deepcopy(rubiks_cube_layout[5][3])

    # left cells of front face take values of left cells of top face
    rubiks_cube_layout[3][3] = copy.deepcopy(rubiks_cube_layout[0][0])
    rubiks_cube_layout[4][3] = copy.deepcopy(rubiks_cube_layout[1][0])
    rubiks_cube_layout[5][3] = copy.deepcopy(rubiks_cube_layout[2][0])

    # right cells of the top face take old values of right cells of back face that where saved to placeholders
    rubiks_cube_layout[0][0] = copy.deepcopy(placeholder_values[2])
    rubiks_cube_layout[1][0] = copy.deepcopy(placeholder_values[1])
    rubiks_cube_layout[2][0] = copy.deepcopy(placeholder_values[0])
    rubiks_cube_layout = rotate_target_face_clockwise(rubiks_cube_layout, 4, 1)
    return rubiks_cube_layout


def rotate_down_face_90_degrees_anticlockwise(rubiks_cube_layout):
    # saves values that will be replaced to be used further down
    placeholder_values = rubiks_cube_layout[5][:3]

    # iterates over 8 cells of line 5 of cube and replaces value of each cell with the value three cells ahead
    for i in range(len(rubiks_cube_layout[5])-3):
        rubiks_cube_layout[5][i] = rubiks_cube_layout[5][i+3]

    # bottom cells of back face take values of bottom cells of left face that where saved to placeholders
    rubiks_cube_layout[5][9:] = placeholder_values
    rubiks_cube_layout = rotate_target_face_anticlockwise(
        rubiks_cube_layout, 7, 1)
    return rubiks_cube_layout

# prints out rubiks cube in console in exploded view


def print_rubiks_cube_layout(rubiks_cube_layout):
    for i in range(len(rubiks_cube_layout)):
        line = ''
        if i < 3 or i > 5:
            line += "       "
        for j in range(len(rubiks_cube_layout[i])):
            line += (str(rubiks_cube_layout[i][j][0]) + ' ')
            if j == 2 or j == 5 or j == 8:
                line += ' '
        print(line, end='\n')

# messages to be displayed at start of function or if user enters an invalid input


def start_and_invalid_input_messages():
    print("Please enter a valid input and press enter:")
    print(" Enter f to rotate the front face clockwise 90 degrees")
    print(" Enter r* to rotate the right face anticlockwise 90 degrees")
    print(" Enter u to rotate the up face clockwise 90 degrees")
    print(" Enter b* to rotate the back face anticlockwise 90 degrees")
    print(" Enter l to rotate the left face clockwise 90 degrees")
    print(" Enter d* to rotate the down face anticlockwise 90 degrees")
    print(" Enter stop to exit")


def main():
    # the starting rubiks cube layout in the form of a matrix
    main_function_rubiks_cube = [[['w'], ['w'], ['w']],
                                 [['w'], ['w'], ['w']],
                                 [['w'], ['w'], ['w']],
                                 [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], [
                                     'r'], ['r'], ['r'], ['b'], ['b'], ['b']],
                                 [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], [
                                     'r'], ['r'], ['r'], ['b'], ['b'], ['b']],
                                 [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], [
                                     'r'], ['r'], ['r'], ['b'], ['b'], ['b']],
                                 [['y'], ['y'], ['y']],
                                 [['y'], ['y'], ['y']],
                                 [['y'], ['y'], ['y']]]

    # prints out layout
    print_rubiks_cube_layout(main_function_rubiks_cube)

    #  start messages displayed
    start_and_invalid_input_messages()

    # user can input a value
    user_input = str(input('Please enter a valid input and press enter:'))

    # loop exits when user inputs string "stop"
    while user_input != 'stop':

        if user_input == 'f':
            main_function_rubiks_cube = rotate_front_face_90_degrees_clockwise(
                main_function_rubiks_cube)

        elif user_input == "r*":
            main_function_rubiks_cube = rotate_right_face_90_degrees_anticlockwise(
                main_function_rubiks_cube)

        elif user_input == "u":
            main_function_rubiks_cube = rotate_top_face_90_degrees_clockwise(
                main_function_rubiks_cube)

        elif user_input == "b*":
            main_function_rubiks_cube = rotate_back_face_90_degrees_anticlockwise(
                main_function_rubiks_cube)

        elif user_input == "l":
            main_function_rubiks_cube = rotate_left_face_90_degrees_clockwise(
                main_function_rubiks_cube)

        elif user_input == "d*":
            main_function_rubiks_cube = rotate_down_face_90_degrees_anticlockwise(
                main_function_rubiks_cube)
        else:
            start_and_invalid_input_messages()

        print_rubiks_cube_layout(main_function_rubiks_cube)
        user_input = str(input('Please enter a valid input and press enter:'))


if __name__ == '__main__':
    main()
