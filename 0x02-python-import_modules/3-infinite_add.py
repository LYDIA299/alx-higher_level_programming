#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arr_size = len(sys.argv) - 1
    sum = 0
    for i in range(arr_size):
        sum += int(sys.argv[i + 1])

    print("{}".format(sum))
