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

    def __init__(self, model_id, arrivel_Time):
        self.model_id = model_id
        self.arrival_time = arrivel_Time

    def UnnecessaryStorage(self):

        delta_day = datetime.today() - \
            datetime.strptime(self.arrival_time, '%d/%m/%Y')

        # print(type(self.arrival_time))
        # print(type(datetime.today))

        if delta_day < timedelta(days=90):
            return True
        else:
            return False

    def Supplied2Storage(self, model_id_added):
        # we add the model_id so the all model_id augments
        self.model_id = model_id_added + self.model_id
        print(
            f"Old model_id: {self.model_id - model_id_added}, new model_id: {self.model_id}.")

    def Supplied2Montage(self, model_id_minued):
        # we remove the model_id so the all model_id diminishes
        self.model_id = self.model_id - model_id_minued
        print(f"{model_id_minued} piece had been transferred to montage.")
        print(
            f"Old model_id at warehouse: {self.model_id + model_id_minued}, new model_id at warehouse: {self.model_id}.")


class KVM(Product):
    'This class is unique to KVMs'

    # This init function is needed to inheritance the main class
    def __init__(self, model_id, arrivel_Time):
        Product.__init__(self, model_id, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 10

        if self.model_id < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class Workstation(Product):
    'This class is unique to Workstation'

    def __init__(self, model_id, arrivel_Time):
        Product.__init__(self, model_id, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 20

        if self.model_id < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class LCD_32_Display(Product):
    'This class is unique to 32"LCD Display'

    def __init__(self, model_id, arrivel_Time):
        Product.__init__(self, model_id, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 10

        if self.model_id < limit:               # This function returns True to check limit situation
            return True
        else:
            return False


class Filter(Product):
    'This class is unique to filters'

    def __init__(self, model_id, arrivel_Time):
        Product.__init__(self, model_id, arrivel_Time)

    def IsUnderLimit(self):
        # It's needless to define the limit inside of function
        limit = 100

        if self.model_id < limit:               # This function returns True to check limit situation
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
