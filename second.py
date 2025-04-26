# 2 задание
import sys, os

def main():
    print("Введите число: ")
    try:
        a = int(input())
        if a <= 5000:
            print("Нельзя)")
            os.execv(sys.executable, [sys.executable] + sys.argv)
    except Exception as e:
        print(f"Ошибочка){e}")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    a = list(map(int, list(str(a))))
    b = int("".join(map(str, a)))
    if a[-1] and a[-2] != 0:
        result = b - (a[-1] ** 2) * (a[-2] ** 2)
        print(f"Результат: {result}")
    else:
        print(f"Результат: {b - (a[0] ** 2)}")

if __name__ == "__main__":
    main()