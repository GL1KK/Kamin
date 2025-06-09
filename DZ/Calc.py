import tkinter


def event(b: str):
    # print(b)
    if b.isdigit() or b == ".":
        global memory
        memory += b
        display.insert(tkinter.END, b)
    elif b in "+/-*=":
        # print(type(eval("5/12")))
        # print(history.cget("text"))
        if history.cget("text")[-1] in "+/-*=" and display.get() == "":
            history.configure(text=history.cget("text")[:-1] + b)
        else:
            expression = history.cget("text") + display.get()
            data = eval(expression)
            history.configure(text=str(data) + b)
            display.delete(0, tkinter.END)
            
            # Сохраняем в файл
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"{expression}={data}\n")
    elif b == "CE":
        display.delete(0, tkinter.END)
    elif b == "DEL":
        current = display.get()
        display.delete(0, tkinter.END)
        display.insert(0, current[:-1])


memory = ""
C_C = "#ecc6d9"
C_N = "#f9ecf2"
BTNS = (("%", C_C), ("CE", C_C), ("%", C_C), ("DEL", C_C),
        ("1/x", C_C), ("x^2", C_C), ("x^0.5", C_C), ("/", C_C),
        ("7", C_N), ("8", C_N), ("9", C_N), ("*", C_C),
        ("4", C_N), ("5", C_N), ("6", C_N), ("-", C_C),
        ("1", C_N), ("2", C_N), ("3", C_N), ("+", C_C),
        ("+-", C_C), ("0", C_N), (".", C_C), ("=", "#993366")
        )

w = tkinter.Tk()
w.title("bul-bul-karasiki")
w.geometry("+600+200")
history = tkinter.Label(text=" ", font=("Impact", 13))
history.grid(row=0, column=0, columnspan=4)
display = tkinter.Entry(font=("Impact", 37), justify="right")
display.grid(row=1, column=0, columnspan=4)
r = 2
c = 0
for btn, clr in BTNS:
    go = lambda x=btn: event(x)
    (tkinter.Button(text=btn, bg=clr, width=8, height=1,
                    font=("Impact", 23), command=go).
     grid(row=r, column=c))
    c += 1
    if c == 4:
        c = 0
        r += 1

tkinter.mainloop()