# Advent of Code 2023

Attempts for the [Advent of Code](https://adventofcode.com/).

## [Problem 1](https://adventofcode.com/2023/day/1)
Part 1 is simple since it is only required to find the first digit and its index using

`i1, d1 = next((i, d) for i, d in enumerate(row) if d in digits).`

The last digit and index `i2, d2` are also found by reversing the string `row[::-1]`. The we check if `i1 == i2`, indicating that the digit is the same, and should **not** be double counted.

Part 2 is a rather convoluted way to replace the first occurrence of number in word-form to a digit. Care needs to be taken forcases such as `eightwo`. 
## [Problem 2](https://adventofcode.com/2023/day/2)
The trick here is taking the `maxmin` of the showings. The minimum number of red balls, is the maximum of thered  occurrences in all games.
## [Problem 3](https://adventofcode.com/2023/day/3)
Part 1 is easily solvable by using regex with

`found = any([re.search(r'[^\d|\\.]', data[i-z][start:end]) for z in [-1, 0, 1]]).`

We iterate each row and within each row, we iterate through all numbers. For instance we would iterate the row `....325....76...` once for `325` and once for `76`. For each iteration we check all adjacent symbols using the above code. The regex `[^\d|\\.]` matches non-numbers and non-periods, which only leaves  `*`.  

Part  2 is slightly more involved but ultimately the same concept. We also keep track of the number of adjacent numbers to cogs, since we only care about cogs with 2 adjacent numbers. 
## [Problem 4](https://adventofcode.com/2023/day/4)
After parsing the input data for part 1, the code is essentially the sum of the values of this line:

`sum(int(2**(len(v['winning'].intersection(v['showing']))-1)) for k, v in input.values())`
## [Problem 5](https://adventofcode.com/2023/day/5)
## [Problem 6](https://adventofcode.com/2023/day/6)
## [Problem 7](https://adventofcode.com/2023/day/7)
## [Problem 8](https://adventofcode.com/2023/day/8)
## [Problem 9](https://adventofcode.com/2023/day/9)
## [Problem 10](https://adventofcode.com/2023/day/10)
## [Problem 11](https://adventofcode.com/2023/day/11)
## [Problem 12](https://adventofcode.com/2023/day/12)
## [Problem 13](https://adventofcode.com/2023/day/13)
## [Problem 14](https://adventofcode.com/2023/day/14)
## [Problem 15](https://adventofcode.com/2023/day/15)
## [Problem 16](https://adventofcode.com/2023/day/16)

A dynamic programming, depth-first approach was taken to solve this problem. Whenever a split occurs, i.e. a horizontal beam collides with a | mirror, or a vertical beam collides with a - mirror, then the function is recursed twice for both beams. (Video illustration below)

[![Advent Of Code Problem 16](https://img.youtube.com/vi/r74SKH55auo/0.jpg)](https://www.youtube.com/watch?v=r74SKH55auo)

## [Problem 17](https://adventofcode.com/2023/day/17)

An application of Djikstra's pathfinding algorithm was used, where the state space is in the form of (position, direction).

![Advent Of Code Problem 17](https://github.com/DylanZammit/Advent-Of-Code-2023/blob/master/img/problem17_vis.png?raw=true)

## [Problem 17](https://adventofcode.com/2023/day/17)
## [Problem 18](https://adventofcode.com/2023/day/18)
## [Problem 19](https://adventofcode.com/2023/day/19)
## [Problem 20](https://adventofcode.com/2023/day/20)
## [Problem 21](https://adventofcode.com/2023/day/21)
## [Problem 22](https://adventofcode.com/2023/day/22)
## [Problem 23](https://adventofcode.com/2023/day/23)
## [Problem 24](https://adventofcode.com/2023/day/24)
## [Problem 25](https://adventofcode.com/2023/day/25)
