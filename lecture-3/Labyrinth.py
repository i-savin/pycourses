# coding: utf
# Обход лабиринта
# Ввести заданный построчно лабиринт размером N×N. Каждая из N строк ввода содержит 
# N символов: «.» — проходимый участок и «#» — непроходимый. 
# Левый верхний и правый нижний участки лабиринта проходимы. 
# С одного проходимого участка можно попасть на соседний либо по вертикали, 
# либо по горизонтали. Проверить, можно ли попасть из левого верхнего участка 
# в правый нижний, и вывести YES, если можно, и NO, если нельзя.
# Input:
#  ...........
# .#.###.###.
# .#...#...#.
# .#.#####.#.
# .#.....#.#.
# ##.###.###.
# .....#.#.#.
# .#.###.#.##
# .#...#.#...
# ##.#.###.##
# ...#.......
# Output:
#  YES

import sys;

maze = [];

first_line = raw_input();
maze.append(first_line);
for i in range(len(first_line) - 1):
    maze.append(raw_input());
		
N = len(maze);

if maze[0][0] == '#':
    print 'NO';
    sys.exit();

plan = [(0,0)];
visited = [];


while (len(plan) != 0):
    current = plan.pop();
    i,j = current;
    if i == N - 1 and j == N - 1:
        if maze[i][j] == '.':
            print 'YES';
            break;
    if i + 1 < len(maze):
        if maze[i+1][j] == '.' and (i+1,j) not in visited:
            plan.append((i+1,j));
    if i - 1 >= 0:
        if maze[i-1][j] == '.' and (i-1,j) not in visited:
            plan.append((i-1,j));
    if j + 1 < len(maze):
        if maze[i][j+1] == '.' and ((i,j+1)) not in visited:
            plan.append((i,j+1));
    if j - 1 >= 0:
        if maze[i][j-1] == '.' and ((i,j-1)) not in visited:
            plan.append((i,j-1));
    visited.append(current);

else:
    print 'NO';