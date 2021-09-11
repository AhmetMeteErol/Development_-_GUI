# This is the file for pick quantity data from csv
__author__ = 'Ahmet Mete Erol'
__copyright__ = "Copyright (c) 2021 Besiktas Istanbul Turkey"
__date__ = '07/09/2021 10:44'

import csv

row_index_of_arriv_date = 2
row_index_of_quantity = 1  # because index 0 = id number
row_index_of_id = 0


def arriv_date_csv_reader(product_id):
    """Reads the csv file and returns the date of arrival"""

    with open('C:\\Users\\meteo\\Desktop\\Development\\YALTES\\YALTES_Stockage_Sample.csv', 'r') as csv_file:
        csv_reader_object = csv.reader(csv_file)

        if csv.Sniffer().has_header:
            next(csv_reader_object)

        for row in csv_reader_object:
            arriv_date = row[row_index_of_arriv_date]
            product_id_in_csv = row[row_index_of_quantity-1]

            if product_id == product_id_in_csv:
                return arriv_date


# print(arriv_date_csv_reader("KVM6"))


def read_csv(product_id):
    """reads the csv file and returns the quantity of the selected product."""

    with open('C:\\Users\\meteo\\Desktop\\Development\\YALTES\\YALTES_Stockage_Sample.csv', 'r') as csv_file:
        csv_reader_object = csv.reader(csv_file)

        if csv.Sniffer().has_header:
            next(csv_reader_object)

        for row in csv_reader_object:
            int_quantity = int(row[row_index_of_quantity])
            product_id_in_csv = row[row_index_of_id]
            # print(product_id_in_csv)
            # we want to find prompted product_id's quantity
            if product_id == product_id_in_csv:
                return int_quantity


# print(quantity_csv_reader("KVM6"))


def write_on_csv(var1, var2, var3):
    """Writes prompted values with arguments to CSV file."""

    with open('C:\\Users\\meteo\\Desktop\\Development\\YALTES\\YALTES_Stockage_Sample.csv', 'a', newline='') as csv_file_to_write:
        product_writer = csv.writer(
            csv_file_to_write)
        product_writer.writerow([var1, var2, var3])
    print(var1, var2, var3)


# write_on_csv("KCV8", "42", "23/04/2020")
