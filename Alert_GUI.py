# Python 3.x code
# Imports
import tkinter
from tkinter import messagebox
from main import *
# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()


def send_alert_box(product_name):
    if Limit_checkers.KVM_checker(product_name):
        KVM_alert_box = messagebox.showwarning(
            "KVM Alert", "Your KVM's are going down below the limit.")
        KVM_alert_box

    elif Limit_checkers.Display_checker(product_name):
        Display_alert_box = messagebox.showwarning(
            '32"-LCD Display Alert', 'Your 32"-LCD Display are going down below the limit.')
        Display_alert_box

    elif Limit_checkers.Filter_checker(product_name):
        Filter_alert_box = messagebox.showwarning(
            "Filter Alert", "Your Filters are going down below the limit.")
        Filter_alert_box

    elif Limit_checkers.Workstation_checker(product_name):
        WS_alert_box = messagebox.showwarning(
            "Workstation Alert", "Your Workstations are going down below the limit.")
        WS_alert_box


def Unneccessary_Storage_Alert_Box(product):
    if Product.UnnecessaryStorage(product):
        messagebox.showinfo("Unnecessary Storage",
                            "Your product is going to rot in the storage!")


KVM1 = KVM(0, '14/12/2020')
WS1 = Workstation(5, '12/08/2021')

send_alert_box(WS1)         # sadece Workstationlara geçmiyor !!

root.mainloop()
