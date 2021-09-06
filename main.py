'''
This is the backhand function for Graphical User Interface
(GUI) which aims to alert user about storage situations such as
    - Unnecessary Usage of Storage
    - Product delivery and afterward supply dimminution or augmentation
    - With the 2nd function, this function aims to alert user if the product is under limit
'''


from datetime import date


class Product(object):
    '''This class represents the products which had been purchased and been stored from Yaltes.'''

    def __init__(self, quantity, arrivel_Time):
        self.quantity = quantity
        self.arrival_time = arrivel_Time

    def UnnecessaryStorage(self):
        # We need to import datetime to know current time
        from datetime import datetime, timedelta

        todays_date_str = datetime.today().strftime("%d/%m/%Y")
        today_day_str = datetime.today().strftime("%A")

        delta_day = datetime.today() - \
            datetime.strptime(self.arrival_time, '%d/%m/%Y')

        # print(type(self.arrival_time))
        # print(type(datetime.today))
        print("Today is " + todays_date_str + ", " + today_day_str)

        if delta_day < timedelta(days=90):
            return True
        else:
            return False

    def Supplied2Storage(self, quantity_added):
        # we add the quantity so the all quantity augments
        self.quantity = quantity_added + self.quantity
        print(
            f"Old quantity: {self.quantity - quantity_added}, new quantity: {self.quantity}.")

    def Supplied2Montage(self, quantity_minued):
        # we remove the quantity so the all quantity diminishes
        self.quantity = self.quantity - quantity_minued
        print(f"{quantity_minued} piece had been transferred to montage.")
        print(
            f"Old quantity at warehouse: {self.quantity + quantity_minued}, new quantity at warehouse: {self.quantity}.")


class KVM(Product):
    'This class is unique to KVMs'

    # This init function is needed to inheritance the main class
    def __init__(self, quantity, arrivel_Time):
        Product.__init__(self, quantity, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 10

        if self.quantity < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class Workstation(Product):
    'This class is unique to Workstation'

    def __init__(self, quantity, arrivel_Time):
        Product.__init__(self, quantity, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 20

        if self.quantity < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class LCD_32_Display(Product):
    'This class is unique to 32"LCD Display'

    def __init__(self, quantity, arrivel_Time):
        Product.__init__(self, quantity, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 10

        if self.quantity < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class Filter(Product):
    'This class is unique to filters'

    def __init__(self, quantity, arrivel_Time):
        Product.__init__(self, quantity, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 100

        if self.quantity < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class Limit_checkers():
    '''This class aims to gather all checker functions'''
    def KVM_checker(KVM_name):
        if KVM_name.IsUnderLimit():
            return True
        else:
            return False

    def Display_checker(Display_name):
        if Display_name.IsUnderLimit():
            return True
        else:
            return False

    def Filter_checker(Display_name):
        if Display_name.IsUnderLimit():
            return True
        else:
            return False

    def Workstation_checker(WS_name):
        if WS_name.IsUnderLimit():
            return True
        else:
            return False


# main içine main loop oluştur
