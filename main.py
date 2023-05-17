import tkinter
from time import strftime

top = tkinter.Tk()
top.title('Clock')
top.resizable(0,0)

def time():
    sting = strftime("%H:%M:%S %p")
    clockTime.config(text=sting)
    clockTime.after(1000,time)

clockTime = tkinter.Label(
    top,
    font=(
        'courier new',
        45,
    ),
    background='black',
    foreground='white'
)
clockTime.pack(anchor="center")
time()
top.mainloop()