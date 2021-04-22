# print([['w'], ['w'], ['w']], '\n',
#       [['w'], ['w'], ['w']], '\n',
#       [['w'], ['w'], ['w']], '\n',
#       [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], [
#           'r'], ['r'], ['r'], ['b'], ['b'], ['b']], '\n',
#       [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], [
#           'r'], ['r'], ['r'], ['b'], ['b'], ['b']], '\n',
#       [['o'], ['o'], ['o'], ['g'], ['g'], ['g'], [
#           'r'], ['r'], ['r'], ['b'], ['b'], ['b']], '\n',
#       [['y'], ['y'], ['y']], '\n',
#       [['y'], ['y'], ['y']], '\n',
#       [['y'], ['y'], ['y']], '\n'
#       )
import copy


def rubiksCube():
    original = [[['w'], ['w'], ['w']],
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
    placeholder_value = []
    print(original)
    user_input = str(input('Please choose:'))
    while user_input != 'stop':
        if user_input == 'f':
            placeholder_value = copy.deepcopy(original[2])
            self_rotation_placeholder = original[3][3]
            # colours on back take values of colours on left
            original[2][0] = copy.deepcopy(original[5][2])
            original[2][1] = copy.deepcopy(original[4][2])
            original[2][2] = copy.deepcopy(original[3][2])
            # colours on left take values of colours on bottom
            original[5][2] = copy.deepcopy(original[6][2])
            original[4][2] = copy.deepcopy(original[6][1])
            original[3][2] = copy.deepcopy(original[6][0])
            # colours on bottom take values of colours on right
            original[6][0] = copy.deepcopy(original[5][6])
            original[6][1] = copy.deepcopy(original[4][6])
            original[6][2] = copy.deepcopy(original[3][6])
            # colours on right take values of colours on top
            original[3][6] = copy.deepcopy(placeholder_value[0])
            original[4][6] = copy.deepcopy(placeholder_value[1])
            original[5][6] = copy.deepcopy(placeholder_value[2])
            # rotate the values of the front
            original[3][3] = copy.deepcopy(original[5][3])
            original[4][3] = copy.deepcopy(original[5][4])
            original[5][3] = copy.deepcopy(original[5][5])
            original[5][4] = copy.deepcopy(original[4][5])
            original[5][5] = copy.deepcopy(original[3][5])
            original[4][5] = copy.deepcopy(original[3][4])
            original[3][4] = copy.deepcopy(original[4][3])
            original[3][5] = copy.deepcopy(self_rotation_placeholder)

        elif user_input == "r*":
            placeholder_value = [copy.deepcopy(original[0][2]), copy.deepcopy(
                original[1][2]), copy.deepcopy(original[2][2])]
            self_rotation_placeholder = original[3][6]
            # colours on top take values of colours on right
            original[0][2] = copy.deepcopy(original[5][9])
            original[1][2] = copy.deepcopy(original[4][9])
            original[2][2] = copy.deepcopy(original[3][9])
            # colours on back take values of colours on bottom
            original[3][9] = copy.deepcopy(original[8][2])
            original[4][9] = copy.deepcopy(original[7][2])
            original[5][9] = copy.deepcopy(original[6][2])
            # colours on bottom take values of colours on front
            original[8][2] = copy.deepcopy(original[5][5])
            original[7][2] = copy.deepcopy(original[4][5])
            original[6][2] = copy.deepcopy(original[3][5])
            # colours on front take values of colours on top
            original[5][5] = placeholder_value[2]
            original[4][5] = placeholder_value[1]
            original[3][5] = placeholder_value[0]
            # rotate the values of the right
            original[4][8] = copy.deepcopy(original[5][7])
            original[5][7] = copy.deepcopy(original[4][6])
            original[4][6] = copy.deepcopy(original[3][7])
            original[3][6] = copy.deepcopy(original[3][8])
            original[3][7] = copy.deepcopy(original[4][7])
            original[3][8] = copy.deepcopy(original[5][8])
            original[5][8] = copy.deepcopy(original[5][6])
            original[5][6] = copy.deepcopy(self_rotation_placeholder)

        for i in range(len(original)):
            line = ''
            if i < 3 or i > 5:
                line += "       "
            for j in range(len(original[i])):
                line += (str(original[i][j][0]) + ' ')
                if j == 2 or j == 5 or j == 8:
                    line += ' '
            print(line, end='\n')

        user_input = str(input('Please choose:'))

    pass


rubiksCube()
