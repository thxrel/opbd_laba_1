from tkinter import *


def trace_func(var, index, mode):
    label.config(text=v.get())


from tkinter import Tk, Label, Radiobutton, Frame, W, LEFT, RIGHT, StringVar

values = {"Тема": "+4 6767676767",
          "Андрей": "+4 8738873639",
          "Степан": "+4 1112111611"}

root = Tk()
frame = Frame(root)
v = StringVar()
v.trace_add("write", lambda var, index, mode: label.config(text=v.get()))
for (text, value) in values.items():
    rb = Radiobutton(frame, text=text, value=value, indicatoron=0,
                     width=20, height=3, variable=v)
    rb.pack(anchor=W)
frame.pack(side=LEFT)
label = Label(root, text="bbb", width=20)
label.pack(side=RIGHT, padx=10)
v.set(values["Тема"])
root.mainloop()
