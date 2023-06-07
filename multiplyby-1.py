# -*- coding: utf-8 -*-
"""
Created on Sun May 21 15:01:58 2023

@author: rohan
"""

import csv

def multiply_column(csv_file, column_index):
    rows = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    for row in rows:
        try:
            value = float(row[column_index])
            row[column_index] = str(value * -1)
        except ValueError:
            # Skip rows with non-numeric values in the specified column
            pass

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Example usage
csv_file = 'doping.csv'  # Replace with the path to your CSV file
column_index = 0  # The column index to multiply by -1 (0-based index)

multiply_column(csv_file, column_index)
