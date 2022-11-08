#
# Author: Michael Denenberg
# Description: This program accepts string inputs of plot type
#              and plot instructions to print a simple defined
#              graph either horizontally or vertically.
#

mode = input('Enter plotter mode:\n')
while mode != 'horizontal' and mode != 'vertical':
    mode = input('Enter stock plotter mode:\n')

plot = input('Enter plot input string:\n')
while len(plot) % 2 != 0:
    plot = input('Enter stock plot input string:\n')


add = None
pos = 0
pos_set = []
for char in plot:
    if char == 'u':
        add = True
    elif char == 'd':
        add = False
    else:
        if add:
            pos += int(char)
        elif not add:
            pos -= int(char)
        pos_set.append(pos)


def horizontal(plot):
    print('#' * (len(pos_set) + 4))
    for x in range(8, -9, -1):
        print('# ', end='')
        for pos in pos_set:
            if pos == x:
                print('*', end='')
            else:
                print(' ', end='')
        print(' #')
    print('#' * (len(pos_set) + 4))


def vertical(plot):
    print('#' * 19)  # -8
    for pos in pos_set:
        print('#' + ' ' * (pos + 8) + '*' + ' ' * (8 - pos) + '#')
    print('#' * 19)


if mode == 'vertical':
    vertical(plot)
else:
    horizontal(plot)
