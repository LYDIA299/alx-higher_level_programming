#!/usr/bin/python3

""" N queens puzzle."""

def main():
    """N queens puzzle."""

    arr = sys.argv

    if arr != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    if not isinstance(int(arr[1]), int):
        print('N must be a number')
        sys.exit(1)

    if int(arr[1]) < 4:
        print('N must be at least 4')
        sys.exit(1)



if __name__ == '__main__':
    import sys
    main()
