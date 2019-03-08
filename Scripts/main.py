from Scripts.bank.bankController import BankController
from tkinter import ttk, Tk, Button, Label, END
from tkinter.scrolledtext import ScrolledText
from Scripts.support.textManipulation import TextManipulation

maroon = "#800000"
white = "#FFFFFF"

class Main:

    def __init__(self):
        BankController.create_database(None)
        global window
        global text_description
        global combo

        window = Tk()
        window.config(background="#ADD8E6")
        window.title("INFOS")
        window.geometry("900x500+100+10")

        button_newInfo = Button(window, width=10, text="New Info", command=self.buttonNewInfo, background="#3CB371", foreground=white, activebackground=maroon, activeforeground=white)
        button_newInfo.place(x=150, y=50)

        button_update = Button(window, width=10, text="Update", command=self.buttonUpdate, background="#1E90FF", foreground="#F0F8FF", activebackground=maroon, activeforeground=white)
        button_update.place(x=630, y=50)

        button_delete = Button(window, width=10, text="Delete", command=self.buttonDelete, background="#FF6347", foreground="#F0F8FF", activebackground=maroon, activeforeground=white)
        button_delete.place(x=730, y=50)

        button_selectInfo = Button(window, width=10, text="Confirm", command=self.buttonSelectInfo, activebackground=maroon, activeforeground=white)
        button_selectInfo.place(x=530, y=50)

        button_exit = Button(window, width=10, text="Quit", command=self.buttonExit, background="#696969", foreground="#FFFFFF", activebackground=maroon, activeforeground=white)
        button_exit.place(x=820, y=0)

        text_description = ScrolledText(window, width=106, height=21)
        text_description.place(x=10, y=150)

        combo = ttk.Combobox(window, width=40, height=34)
        combo.place(x=250, y=50)
        combo['values'] = (BankController.getNames(None))

        label_description = Label(window, text="DESCRIPTION", width=10, height=1, background="#ADD8E6")
        label_description.place(x=400, y=120)

        label_infos = Label(window, text="INFOS", width=10, height=1, background="#ADD8E6")
        label_infos.place(x=350, y=25)

        window.mainloop()

    def buttonNewInfo(self):
        BankController.insert(None, combo.get(), TextManipulation.formatText(text_description.get(0.0, END)))
        combo['values'] = (BankController.getNames(None))

    def buttonUpdate(self):
        BankController.update(None, combo.get(), text_description.get(0.0, END))

    def buttonDelete(self):
        BankController.delete(None, combo.get())
        combo['values'] = (BankController.getNames(None))

    def buttonSelectInfo(self):
        text_description.delete('0.0', '100.0')
        text_description.insert(END,BankController.getDescription(None, combo.get()))

    def buttonExit(self):
        BankController.close(None)
        window.destroy()

gui = Main()


