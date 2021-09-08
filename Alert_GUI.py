__author__ = 'Ahmet Mete Erol'
__date__ = '07/09/2021'
__license__ = 'Apache License 3.0'

import tkinter as tk
from tkinter import *
from main import *

# Select product type section

ws = Tk()
ws.title('Choose the product type')
ws.geometry('400x300')
ws.config(bg='#F2B90C')


def display_selected(choice):
    choice = variable.get()
    print(choice)


products = ['KVC', '32"Inches LCD Display', 'Filter', 'Workstation']

# setting variable for Integers
variable = StringVar()
variable.set(products[3])

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *products,
    command=lambda: [
        display_selected(), root.destroy()]
)

# ürün türünü seçerken isim, ilk adet ve tarih de girilsin
# ordan da girilen değerler class'ların içine değer olarak girsin
# mesela:
# isim = entry(blabla)
# tarih = entry(blabla)
# SIUC(isim,adet,tarih).IsUnnecassaryStockage diye giderim


# positioning widget
dropdown.pack(expand=True)

# infinite loop

ws.mainloop()


root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing model_name and Arrival_date
model_name_var = tk.StringVar()
arriv_date_var = tk.StringVar()


# defining a function that will
# get the model_name and Arrival_date and
# print them on the screen
def submit():

    model_name = model_name_var.get()
    Arrival_date = arriv_date_var.get()

    print("The model name is : " + model_name)
    print("The Arrival date is : " + Arrival_date)

    model_name_var.set("")
    arriv_date_var.set("")


# creating a label for
# model_name using widget Label
model_name_label = tk.Label(
    root, text='Model no:', font=('calibre', 10, 'bold'))

# creating a entry for input
# model_name using widget Entry
model_name_entry = tk.Entry(root, textvariable=model_name_var,
                            font=('calibre', 10, 'normal'))

# creating a label for Arrival_date
passw_label = tk.Label(root, text='First Arrival Time:',
                       font=('calibre', 10, 'bold'))

# creating a entry for Arrival_date
passw_entry = tk.Entry(root, textvariable=arriv_date_var,
                       font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=lambda: [
                    submit(), root.destroy()])          # by using this syntaxe, we could command two functions in one Button

# placing the label and entry in
# the required position using grid
# method
model_name_label.grid(row=0, column=0)
model_name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()


# Python 3.x code
# Imports

master = Tk()

master.title("YALTES STORAGE INFO WINDOW")

# Creating Frames Section
canvas = Canvas(master, height=450, width=850)
canvas.pack()

up_frame = Frame(master, bg='#add8e6')
up_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

down_left_frame = Frame(master, bg='#add8e6')
down_left_frame.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

down_right_frame = Frame(master, bg='#add8e6')
down_right_frame.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

# Product Type Layer Section
product_type_tag = Label(up_frame, bg='#add8e6',
                         text="Product Type:", font="Verdana 12 bold")
product_type_tag.pack(padx=10, pady=10, side=LEFT)

# variable.get usage aims to get prompted value on Option Menu
Product_model_name = Label(up_frame, bg='#add8e6',
                           text=variable.get(), font="Verdana 12 bold")
Product_model_name.pack(padx=10, pady=10, expand=True)

Unnecessary_Storage = Label(
    down_right_frame, bg='#add8e6', text='Unnecessary Usage of Warehouse?', font="Verdana 11 bold")
Unnecessary_Storage.pack(padx=10, pady=10, anchor=NW)

Under_limit_Sit_Label = Label(
    down_left_frame, bg='#add8e6', text='Our Stockage is' + '\n' + 'under the minimum limit?', font="Verdana 9 bold")
Under_limit_Sit_Label.pack(padx=10, pady=10, anchor=N)


# # Unnecessary_Storage_actual_case_label = Label(down_right_frame, bg='#add8', text=str(Product(str(variable.get())).UnnecessaryStorage())   # I tried to get the data from entry label
# # but it has to be prompted for example KVM1's inputs
# def send_alert_box(product_model_name):
#     if Limit_checkers.KVM_checker(product_model_name):
#         KVM_alert_box = messagebox.showwarning(
#             "KVM Alert", "Your KVM's are going down below the limit.")
#         KVM_alert_box

#     elif Limit_checkers.Display_checker(product_model_name):
#         Display_alert_box = messagebox.showwarning(
#             '32"-LCD Display Alert', 'Your 32"-LCD Display are going down below the limit.')
#         Display_alert_box

#     elif Limit_checkers.Filter_checker(product_model_name):
#         Filter_alert_box = messagebox.showwarning(
#             "Filter Alert", "Your Filters are going down below the limit.")
#         Filter_alert_box

#     elif Limit_checkers.Workstation_checker(product_model_name):
#         WS_alert_box = messagebox.showwarning(
#             "Workstation Alert", "Your Workstations are going down below the limit.")
#         WS_alert_box


# def Unneccessary_Storage_Alert_Box(product):
#     if Product.UnnecessaryStorage(product):
#         messagebox.showinfo("Unnecessary Storage",
#                             "Your product is going to rot in the storage!")


# def Welcoming_Box():

#     # Converting date object to string for user
#     todays_date_str = datetime.today().strftime("%d/%m/%Y")
#     today_day_str = datetime.today().strftime("%A")
#     str = 'Welcome! Today is '


""" Yapılması gerekenler --->
 kullanıcıdan gelen inputları class'larda çalıştırabilmek
"""

KVM1 = KVM(0, '14/12/2020')
WS1 = Workstation(5, '12/08/2021')

print(KVM1.UnnecessaryStorage())

master.mainloop()
