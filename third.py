# 3 задание

from random import randint

def main():
    a = randint(-100, 100)
    if -10 < a < 10:
        print(a+5)
    else:
        print(a-10)
    
if __name__ == "__main__":
    main()