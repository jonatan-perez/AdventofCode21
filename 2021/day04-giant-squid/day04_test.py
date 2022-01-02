import pytest
import day04_problem1
import day04_problem2

with open("2021/day04-giant-squid/test_input.txt") as f:
    input = [line.replace("\n", "") for line in f]
    numbers_drawn = [int(i) for i in input[0].split(",")]

boards = day04_problem1.makeBoards(input)
def test_problem1():
    assert day04_problem1.playBingo(numbers_drawn, boards) == 4512

def test_problem2():
    assert day04_problem2.playBingo(numbers_drawn, boards) == 1924