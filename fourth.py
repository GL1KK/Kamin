# 4 задание

def main():
    a = 0
    b = 2
    c = 5

    list = [a, b, c]

    a += b

    b = c - list[0] - b

    c += list[0] + list[1]

    print(a, b, c)

if __name__ == "__main__":
    main()