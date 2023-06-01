
"""
    To decide whether this number is
"""

from math import sqrt


def is_prime():
    """
     Given a positive integer, check whether or not it is a prime number
    :return:
    """

    num = int(input("Please input a integer number: "))
    end = int(sqrt(num))
    prime_flag = True

    for x in range(2, end + 1):
        if num % x == 0:
            prime_flag = False
            break

    if prime_flag and num != 1:
        print("%d is a prime" % num)
    else:
        print('%d is not a prime' % num)


def row_triangle():
    row = int(input("Please input row number: "))
    for i in range(row):
        for _ in range(i+1):
            print('*', end='')

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2*i+1):
            print('*', end='')
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #is_prime()

    row_triangle()

