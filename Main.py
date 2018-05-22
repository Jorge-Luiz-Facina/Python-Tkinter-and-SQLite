from package.database.Bank import BankInfo
from tkinter import ttk, Tk, Button, Label, END
from tkinter.scrolledtext import ScrolledText
from package.support.Support import SupportInfo

class Main:

    def __init__(self):
        global window
        global text_description
        global combo

        window = Tk()
        window.config(background="#ADD8E6")
        window.title("INFOS")
        window.geometry("900x500+100+10")

        button_newInfo = Button(window, width=10, text="NewInfo", command=self.buttonNewInfo)
        button_newInfo.place(x=200, y=50)

        button_update = Button(window, width=10, text="Update", command=self.buttonUpdate, background="#D4664c")
        button_update.place(x=680, y=50)

        button_delete = Button(window, width=10, text="Delete", command=self.buttonDelete, background="#E90000")
        button_delete.place(x=780, y=50)

        button_selectInfo = Button(window, width=10, text="Confirm", command=self.buttonSelectInfo)
        button_selectInfo.place(x=580, y=50)

        button_exit = Button(window, width=10, text="Quit", command=self.buttonExit)
        button_exit.place(x=820, y=0)

        text_description = ScrolledText(window, width=106, height=21)
        text_description.place(x=10, y=150)

        combo = ttk.Combobox(window, width=40, height=34)
        combo.place(x=300, y=50)
        combo['values'] = (BankInfo.getNames(None))

        label_description = Label(window, text="Descricao", width=10, height=1, background="#ADD8E6")
        label_description.place(x=400, y=120)

        label_infos = Label(window, text="Infos", width=10, height=1, background="#ADD8E6")
        label_infos.place(x=400, y=25)

        window.mainloop()

    def buttonNewInfo(*args):
        BankInfo.insert(None, combo.get(), SupportInfo.formatText(text_description.get(0.0, END)))
        combo['values'] = (BankInfo.getNames(None))

    def buttonUpdate(*args):
        BankInfo.update(None, combo.get(), text_description.get(0.0, END))

    def buttonDelete(*args):
        BankInfo.delete(None, combo.get())
        combo['values'] = (BankInfo.getNames(None))

    def buttonSelectInfo(*args):
        text_description.delete('0.0', '100.0')
        text_description.insert(END,BankInfo.getDescription(None, combo.get()))

    def buttonExit(*args):
        BankInfo.close(None)
        window.destroy()

gui = Main()


