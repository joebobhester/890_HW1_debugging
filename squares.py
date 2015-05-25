print('\n\nI am going to draw a square.\n')

def square():
    size = input('How large should the square be? (Please enter an integer from 1 to 30.)\n\n')
    if int(size) >= 1 and int(size) <= 30:
        print('\n\nOK, here is that square:\n\n')
        return size
    else:
        print('\n "' + size + '" is not a valid integer.\n')
        print('Please input a valid integer.')
        return square()


############################################################################
#                                                                          #
# NOTE: The code above this comment is correct.                            #
#       Do not modify any code above this comment.                         #
#                                                                          #
############################################################################

def row():
    width = int(size_wide) * 2 + 1
    bar = '-' ** width
    print('+ bar +')

def sides(size_high)
    height = int(size_high) * 2 + 1
    spaces = heigth * ' '
    print('|' + 'spaces' + '|')
    
def print_square():
    size == square()
    row(size)
    for x in range(int(size)):  # This line is correct. Don't edit.
        sides(size)             # This line is correct. Don't edit.
    row(size)
    print(\n\n)

print_square(size)


