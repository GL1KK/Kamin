# 5 задание

def main():
    a = [1, 3, 5]

    b = [2, 1, 8]

    c = [6, 3, 8]

    for i in a:
        if i in b and i in c:
            print("yes")
            break
        # от нас для более качественной программы)
        else:
            print("no")
            break
if __name__ == "__main__":
    main()