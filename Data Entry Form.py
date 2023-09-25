from tkinter import *
from tkinter import ttk
import tkcalendar

def transfer_text():
    text = fname_entry.get()  # Get the text from the entry field
    lname_label.config(text=text)  # Transfer the text to the second label
    #entry.delete(0, END)  # Clear the entry field

root = Tk()
root.title("Data Entry Form")
root.geometry("500x400")
root.config(bg="#4277d4")
root.resizable(FALSE,FALSE)

#title
title = Label(root, text="Data Entry Form", font="Calibre 20 bold ",bg="#4277d4")
title.grid(row=0, column=0, pady=10, columnspan=4)

#first_name
fname_label = Label(root, text="First Name ", padx=10,bg="#4277d4", font="Calibre 10 bold ")
fname_label.grid(row=1,column=0, sticky="w")

fname_entry = ttk.Entry(root, width=20)
fname_entry.grid(row=1, column=1)
fname_entry.bind('<Return>', lambda event: transfer_text())

#last_name
lname_label = Label(root, text="   Last Name ", padx=10,bg="#4277d4", font="Calibre 10 bold ")
lname_label.grid(row=1,column=2)

lname_entry = ttk.Entry(root, width=20)
lname_entry.grid(row=1, column=3)

#birth_data
birth_label = Label(root, text="Birth Date ", padx=10, pady=20,bg="#4277d4",font="Calibre 10 bold ")
birth_label.grid(row=2,column=1, sticky="w")

birth_entry = tkcalendar.DateEntry(root, width =20 )
birth_entry.grid(row=2, column=2,pady=5, columnspan=3, sticky="we")

#gender
gender_label = Label(root, text=" Gender ", padx=10, pady=20,bg="#4277d4",font="Calibre 10 bold ")
gender_label.grid(row=3,column=0, sticky="w")

gender = StringVar()
gender.set("none")
male = ttk.Radiobutton(root, text="Male", variable=gender, value= "Male")
male.grid(row=3, column=1 , pady=5 , sticky="w")

female = ttk.Radiobutton(root, text="Female", variable=gender, value= "Female")
female.grid(row=3, column=2 , pady=5 , sticky="w")

#country

country_label = Label(root, text=" Country ", padx=10, pady=20,bg="#4277d4",font="Calibre 10 bold ")
country_label.grid(row=4,column=0, sticky="w")

country_entry = ttk.Combobox(root, width=20, values=["Egypt", "USA", "Saudi Arabia" , "Syria", "USE", "Oman","Libya", "Qatar"])
country_entry.grid(row=4, column=1,pady=5, columnspan=3, sticky="we")

#address
address_label = Label(root, text=" Address ", padx=10, pady=20,bg="#4277d4",font="Calibre 10 bold ")
address_label.grid(row=5,column=0, sticky="nw")

address_entry = Text(root, width=20, height=5)
address_entry.grid(row=5, column=1,pady=5, columnspan=3, sticky="we")

#buttons
def record():
    firstname= fname_entry.get()
    lastname = lname_entry.get()
    gender_ = gender.get()
    birthdate = birth_entry.get()
    country = country_entry.get()
    address = address_entry.get("1.0", "end-1c")
    text = firstname + "," + lastname + "," + gender_ + "," + birthdate + "," + country + "," + address + "\n"
    with open(r"C:\Users\mega2\Desktop\youssef\Data form\file.csv", "a") as file :
        file.write(text)
    clear_all()

def clear_all():
    fname_entry.delete(0, "end")
    lname_entry.delete(0, "end")
    gender.set("none")
    birth_entry.delete(0,"end")
    country_entry.delete(0,"end")
    address_entry.delete("1.0", "end")
    fname_entry.focus_set()


save = ttk.Button(root, text="Save", command=record)
save.grid(row=6, column=1, padx=10, sticky="e", ipadx=10)

clear = ttk.Button(root, text="Clear", command=clear_all)
clear.grid(row=6, column=2, padx=10, sticky="w", ipadx=10 )

root.mainloop()