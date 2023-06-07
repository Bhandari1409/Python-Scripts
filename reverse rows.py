# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:51:41 2023

@author: rohan
"""

import csv

def reverse_csv_rows(csv_file):
    rows = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    reversed_rows = rows[::-1]  # Reverse the order of rows

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reversed_rows)

# Example usage
csv_file = 'ac_ElecField_Y.csv'  # Replace with the path to your CSV file

reverse_csv_rows(csv_file)
print("CSV file rows reversed and updated successfully.")
