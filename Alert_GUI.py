# This is the GUI Section which uses mainly main.py and csv_example.py

__author__ = 'Ahmet Mete Erol'
__copyright__ = "Copyright (c) 2021 Besiktas Istanbul Turkey"
__date__ = '07/09/2021 10:44'

# importing libraries
import tkinter as tk
from tkinter import *
from main import *
from csv_example import *


# Select product type window section

First_Window = Tk()
First_Window.title('Choose the product type')
First_Window.geometry('400x300')
First_Window.config(bg='#F2B90C')


def display_selected(choice):
    choice = variable_product_type.get()
    print(choice)


products = ['KVC', '32"Inches LCD Display', 'Filter', 'Workstation']

# to hold variables from the GUIs'
variable_product_type = StringVar()
# At the begining, user will see first element of the list on the menu.
variable_product_type.set(products[0])

# creating widget
dropdown = OptionMenu(
    First_Window,
    variable_product_type,
    *products,
    command=display_selected
)
# positioning widget
dropdown.pack(expand=True)

ok_btn = tk.Button(First_Window, text='OK', command=First_Window.destroy)
ok_btn.pack(anchor=S)

# ürün türünü seçerken isim, ilk adet ve tarih de girilsin
# ordan da girilen değerler class'ların içine değer olarak girsin
# mesela:
# isim = entry(blabla)
# tarih = entry(blabla)
# SIUC(isim,adet,tarih).IsUnnecassaryStockage diye giderim


# infinite loop

First_Window.mainloop()

# Submit widget section
second_window = tk.Tk()
second_window.title("Enter Model Part No and Arrival Date")
# setting the windoFirst_Window size
second_window.geometry("600x400")

# declaring string variable_product_type
# for storing model_name and Arrival_date
model_id_var = StringVar()
arriv_date_var = StringVar()

# print(model_id_var.get())
model_id_var.set("1234")
arriv_date_var.set("07/09/2021")

# defining a function that will
# get the model_name and Arrival_date and
# print them on the screen

global model_name


def submit():
    model_name = model_id_var.get()
    # Arrival_date = arriv_date_var.get()

    print("The model name is : " + model_name)
    # print("The Arrival date is : " + Arrival_date)

    # model_id_var.set("")
    # arriv_date_var.set("")


# creating a label for
# model_name using widget Label
model_id_name = tk.Label(
    second_window, text='Model no:', font=('calibre', 10, 'bold'))

# creating a entry for input
# model_name using widget Entry
model_id_entry = Entry(second_window, text=model_id_var,
                       font=('calibre', 10, 'normal'))

# # creating a label for Arrival_date
passw_label = tk.Label(second_window, text='First Arrival Time:',
                       font=('calibre', 10, 'bold'))

# # creating a entry for Arrival_date
passw_entry = tk.Entry(second_window, text=arriv_date_var,
                       font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(second_window, text='Submit', command=lambda: [
    submit(), second_window.destroy()])          # by using this syntaxe, we could command two functions in one Button

# placing the label and entry in
# the required position using grid
# method
model_id_name.grid(row=0, column=0)
model_id_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
second_window.mainloop()

"""3rd Window Section"""
third_window = Tk()
third_window.title("YALTES STORAGE INFO WINDOW")

# Creating Frames Section
canvas = Canvas(third_window, height=450, width=850)
canvas.pack()

up_frame = Frame(third_window, bg='#add8e6')
up_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

down_left_frame = Frame(third_window, bg='#add8e6')
down_left_frame.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

down_right_frame = Frame(third_window, bg='#add8e6')
down_right_frame.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

# Product Type Layer Section
product_type_label = Label(up_frame, bg='#add8e6',
                           text="Product Type:", font="Verdana 12 bold").pack(padx=10, pady=10, side=LEFT)

# variable_product_type.get usage aims to get prompted value on Option Menu
Product_model_name = Label(up_frame, bg='#add8e6',
                           text=variable_product_type.get(), font="Verdana 12 bold").pack(padx=10, pady=10, side=LEFT)

product_type_id = Label(up_frame, bg='#add8e6',
                        text=model_id_var.get(), font="Verdana 12").pack(padx=10, pady=10, side=RIGHT)

product_type_frame = Label(
    up_frame, bg='#add8e6', text='Product ID:', font="Verdana 12 bold")
product_type_frame.pack(padx=10, pady=10, side=RIGHT)

Unnecessary_Storage_label = Label(
    down_right_frame, bg='#add8e6', text='Unnecessary Usage of Warehouse?', font="Verdana 11 bold")
Unnecessary_Storage_label.pack(padx=10, pady=10, anchor=NW)


def get_is_unnecessary():
    # print("variable_product_type.get() ===> ", variable_product_type.get())
    # print("arriv_date_var.get() ===> ",  arriv_date_var.get())
    # print("Product(variable_product_type.get(), arriv_date_var.get()).UnnecessaryStorage() ===> ",
    #       Product(variable_product_type.get(), arriv_date_var.get()).UnnecessaryStorage())

    if Product(variable_product_type.get(), arriv_date_var.get()).UnnecessaryStorage() == True:
        Unnecessary_Storage_Situation = Label(
            down_right_frame, bg='#add8e6', fg="green", text='NO', font="Verdana 13 bold").pack(padx=10, pady=10, expand=True)
    else:
        Unnecessary_Storage_Situation = Label(
            down_right_frame, bg='#add8e6', fg="red", text='YES', font="Verdana 13 bold").pack(padx=10, pady=10, expand=True)


Unnecessary_Storage_Situation = Label(
    down_right_frame, bg='#add8e6', fg="red", text=get_is_unnecessary(), font="Verdana 13 bold").pack(padx=10, pady=10, expand=True)


Under_limit_Sit_Label = Label(
    down_left_frame, bg='#add8e6', text='Our Stockage is' + '\n' + 'under the minimum limit?', font="Verdana 9 bold").pack(padx=10, pady=10, anchor=N)


""" Yapılması gerekenler --->
kullanıcıdan gelen inputları class'larda çalıştırabilmek
"""

third_window.mainloop()
