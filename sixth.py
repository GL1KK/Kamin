# 6 задание
import sys, os

def main():
    print("Введите четырехзначное число")

    try:
        a = int(input())
        print(a)
    except Exception as e:
        print(f"Ошибочка {e}")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    if 999 < a < 10000:
        a = list(map(int, list(str(a))))
        
        max = max(a)
        min = min(a)
        min_index = a.index(min)
        max_index = a.index(max)
        a.remove(max)
        a.remove(min)
        a.insert(min_index, max)
        a.insert(max_index, min)
    else:
        print("Ненене не пойдет давай еще разок")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    print(a)

if __name__ == "__main__":
    main()