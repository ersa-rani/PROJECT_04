def main():
    numbers: list[int] = [1, 2, 3, 4]  # Original list

    for i in range(len(numbers)):
        numbers[i] *= 2  # Double each element in place

    print(numbers)  # Output: [2, 4, 6, 8]


if __name__ == '__main__':
    main()
