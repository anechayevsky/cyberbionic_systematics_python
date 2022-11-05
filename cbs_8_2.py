import numpy as np


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def main():
    print('  #   a**2  a**3')
    for i in np.arange(-5, 5.5, 0.5):
        print(f'{i}  {square(i)}  {cube(i)}')


if __name__ == '__main__':
    main()
