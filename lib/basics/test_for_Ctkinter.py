import tkinter as tk
import Ctkinter as Ctk


root = tk.Tk()
root.geometry('500x500')
label = Ctk.CLabel(root, bg='orange', size=(None, 30), text='Hallo I bin a Label', fg='black', font=('Sans', 12),
                 corner='round', max_rad=None, outline=('', 0), anchor='CENTRE', variable_text=False,
                 enter_hit=(False, None))
label.pack()

root.mainloop()
