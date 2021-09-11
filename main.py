# This is the main Section which for GUI

__author__ = 'Ahmet Mete Erol'
__copyright__ = "Copyright (c) 2021 Besiktas Istanbul Turkey"
__date__ = '07/09/2021 10:44'


'''
This is the backhand function for Graphical User Interface
(GUI) which aims to alert user about storage situations such as
    - Unnecessary Usage of Storage
    - Product delivery and afterward supply dimminution or augmentation
    - With the 2nd function, this function aims to alert user if the product is under limit
For these purposes it's defined in class format.
'''

# We need to import datetime to know current time
from datetime import datetime, timedelta


class Product(object):
    '''This class represents the products which had been purchased and been stored from Yaltes.'''

    # initial function
    def __init__(self, quantity, arrivel_Time):
        self.quantity = quantity
        self.arrival_time = arrivel_Time

    def UnnecessaryStorage(self):
        """Takes string values from his class and returns a boolean value if there is a situation for unnecessary storage for a product """
        delta_day = datetime.today() - \
            datetime.strptime(self.arrival_time, '%d/%m/%Y')

        # print(type(self.arrival_time))
        # print(type(datetime.today))

        if delta_day < timedelta(days=90):
            return True
        else:
            return False

    def Supplied2Storage(self, quantity_added):
        """This module serves to change our product quantity."""
        # we add the quantity so the all quantity augments
        self.quantity = quantity_added + self.quantity
        print(
            f"Old quantity: {self.quantity - quantity_added}, new quantity: {self.quantity}.")

    def Supplied2Montage(self, quantity_minued):
        """This module serves to change our product quantity."""

        # we remove the quantity so the all quantity diminishes
        self.quantity = self.quantity - quantity_minued
        print(f"{quantity_minued} piece had been transferred to montage.")
        print(
            f"Old quantity at warehouse: {self.quantity + quantity_minued}, new quantity at warehouse: {self.quantity}.")


class KVM(Product):
    'This a product class which is unique to KVMs'

    # This init function is needed to inheritance the main class
    def __init__(self, quantity, arrivel_Time):
        Product.__init__(self, quantity, arrivel_Time)

# As each product's limit is different, we need to redefine modules.
    def IsUnderLimit(self):
        """Returns a boolean value if the quantity """
        limit = 10

        if self.quantity < limit:
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

        if self.quantity < limit:
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

        if self.quantity < limit:
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

        if self.quantity < limit:
            return True
        else:
            return False
