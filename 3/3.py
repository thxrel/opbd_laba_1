from tkinter import *
class Frame(Tk):
    def __init__(self):
        super().__init__()
        self.title('Shisha')
        self.configure(bg='#78DBE2')
        self.geometry("198x80")
        self.lbl = Label(text="", width=150)
        self.e1 = Entry(width=150, justify=CENTER)
        color = {'#ff0000': 'Красный',
               '#ff7d00': 'Оранжевый',
               '#ffff00': 'Желтый',
               '#00ff00': 'Зеленый',
               '#007dff': 'Голубой',
               '#0000ff': 'Синий',
               '#7d00ff': 'Фиолетовый'}
        for colour in color.keys():
            func = lambda c=colour, ruc=color[colour]: self.onclick(c, ruc)
            b = Button( fg='white', bd=10 ,command=func, bg=colour, width=1,
height=1, )
            self.lbl.pack()
            self.e1.pack()
            b.pack(side='left',  expand=True)
    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour
if __name__ == '__main__':
    root = Frame()
    root.mainloop()
