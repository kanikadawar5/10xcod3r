def numdig_to_array(num):
    arr = list(map(int, str(num)))
    print(arr)


def main():
    num = input()
    numdig_to_array(num)


main()
