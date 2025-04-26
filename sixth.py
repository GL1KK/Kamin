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
        
        max_val = max(a)
        min_val = min(a)
        min_index = a.index(min_val)
        max_index = a.index(max_val)
        a.remove(max_val)
        a.remove(min_val)
        a.insert(min_index, max_val)
        a.insert(max_index, min_val)
        result = int(''.join(map(str, a)))
        print(result)
    else:
        print("Ненене не пойдет давай еще разок")
        os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == "__main__":
    main()