def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def pattern2(n):
    for i in range(1, n + 1):
        for j in range(65, (i + 65)):
            print(chr(j), end=" ")
        print()


def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()


def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


def pattern5(n):
    for i in range(1, n + 1):
        for j in range(65, (i + 65) + 1):
            print(chr(i + 64), end=" ")
        print()


def pattern6(n):  # Edited from num pattern to * pattern
    for i in range(1, n + 1):
        for j in range(n, 0, -1):
            if j > i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()


def pattern7(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def pattern8(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print(j + n - i, end=" ")
        print()


def pattern9(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print(chr(j + 64), end=" ")
        print()


def pattern10(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print(chr(j + n - i + 64), end=" ")
        print()


def pattern11(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print("*", end="")
        for k in range(1, i):
            print("*", end="")
        print()


def pattern12(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print(i, end=" ")
        print()


def pattern13(n):
    for i in range(1, n + 1):
        print(end=" " * (n - i))
        for j in range(1, i + 1):
            print(chr(i + 64), end=" ")
        print()


def pattern14(n):
    for i in range(1, n + 1):
        for j in range(1, (n + 2) - i):
            print(j, end=" ")
        print()


def pattern15(n):
    for i in range(0, n):
        for j in range(n, i, -1):
            print(j, end=" ")
        print()


def pattern16(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(n + 1 - j, end=" ")
        print()


def pattern17(n):  # Copied 
    start = 1
    stop = 2
    for i in range(n):
        for j in range(1, stop):
            print(start, end=" ")
            start += 1
        print()
        stop += 1


def pattern18(n):
    for i in range(n, 0, -1):
        for j in range(1, n):
            print(chr(j + 64), end=" ")
        print()


def patternSpecial(n):  # i don't even know how i did this
    for i in range(1, n + 1):
        for j in range(i, (n - i) + i):
            print(j, end=" ")
        print()


if __name__ == "__main__":
    pattern6(5)
