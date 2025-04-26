# 1 задание
import sys, os

def calculation():
    print("Введите первое число:")
    try:
        a = int(input())
    except Exception as e:
        print(f"Возникла ошибка: {e}")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    print("Введите второе число:")
    try:
        b = int(input())
        result = a ** (2 * b) - b ** (2 * a)
    except Exception as e:
        print(f"Возникла ошибка: {e}")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    print(f"Результат: {result}")
def main():
    calculation()

if __name__ == "__main__":
    main()