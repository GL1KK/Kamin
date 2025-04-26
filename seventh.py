# 1 (во втором блоке) задание
import sys, os

def get_month(month_number):
    season = {"1": "зима", "2": "зима", "12": "зима",
               "3": "весна", "4": "весна", "5": "весна", 
               "6": "лето","7": "лето", "8": "лето", 
               "9": "осень", "10": "осень", "11": "осень"
        }
    if month_number in season:
        print(season[month_number])
    else:
        print("Че то не то братик(")
        os.execv(sys.executable, [sys.executable] + sys.argv)
def main():
    print("Введите номер месяца")
    month_number = input()
    get_month(month_number)

if __name__ == "__main__":
    main()