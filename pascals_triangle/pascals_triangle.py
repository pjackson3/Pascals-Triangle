import os
import sys
from math import factorial


def get_iterations():
    if len(sys.argv) == 2:
        return int(sys.argv[1])
    if os.isatty(sys.stdout.fileno()):
        return int(input("How many iterations? "))
    return int(input())

def binomial_theorem(n: int, k: int) -> int:
    return factorial(n)//(factorial(n-k+1)*factorial(k-1))

def print_result(triangle, iterations):
    for index, i in enumerate(triangle):
        res_str = ' '.join(i)
        if os.isatty(sys.stdout.fileno()):
            print(res_str.center(os.get_terminal_size().columns))
        else:
            print(res_str)

def calc_triangle(iterations):
    triangle = []
    for i in range(iterations):
        triangle.append([])
        for j in range(i+1):
            triangle[i].append(str(binomial_theorem(i, j+1)))
    return triangle

def main():
    iterations = get_iterations()
    triangle = calc_triangle(iterations)
    print_result(triangle, iterations)

if __name__ == '__main__':
    main()
