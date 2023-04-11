from collections import Counter

board = [["B", "W", "B", "W", "B"],
         ["W", "W", "W", "W", "W"],
         ["B", "W", "W", "W", "B"],
         ["W", "W", "W", "W", "W"],
         ["B", "W", "B", "W", "B"]]

empty = dict(sum(map(Counter, board), Counter()))

print(empty.get("x"))

[['B', 'L', 'B', 'L', 'B'],
 ['O', 'L', 'L', 'L', 'L'],
 ['B', 'O', 'L', 'L', 'B'],
 ['L', 'L', 'L', 'O', 'L'],
 ['B', 'L', 'B', 'L', 'B']]
