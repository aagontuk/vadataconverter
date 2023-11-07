# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:21:06 2022

@author: tasni
"""

import pandas as pd
import argparse
import sys

def convert(in_file, sht_name, out_file):
    df = pd.read_csv(in_file)
    df = df[['icd10', 'sex', 'age']]

    df['icd10'].fillna('Unknown', inplace=True)
    df['sex'].fillna('Unknown', inplace=True)
    
    age_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 1000]

    # Generate lebels
    age_labels = []
    for i in range(0, len(age_bins) - 2):
        age_labels.append('{}-{} Year'.format(age_bins[i], age_bins[i+1] - 1))
    age_labels.append('95+ Year')

    # Create a new column for each age label
    df['<1 Year'] = 0
    for label in age_labels:
        df[label] = 0  # Initialize with 0

    # Assign 1 to the corresponding age label column based on the Age of the entry
    for index, row in df.iterrows():
        age = row['age']
        if pd.notna(age):  # Check if 'Age' is not NaN
            for i, label in enumerate(age_labels):
                if age <= 0:
                    df.at[index, '<1 Year'] = 1
                if age_bins[i] <= age < age_bins[i + 1]:
                    df.at[index, label] = 1
                    break
        else:
            df.at[index, 'Unknown'] = 1  # Assign to 'unknown' if 'Age' is NaN

    grouped = df.groupby(['icd10', 'sex']).sum().reset_index()
    grouped = grouped.drop('age', axis=1)

    # grouped.to_csv("output_file.csv", index=False)
    grouped.to_excel(out_file, sheet_name=sht_name, index=False)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert VA Data")
    parser.add_argument('--input-file', type=str, required=True, help='Provide input file to convert')
    parser.add_argument('--sheet-name', type=str, help='Name of the sheet for excel file')
    parser.add_argument('--output-file', type=str, required=True, help='Provide output file name')

    args = parser.parse_args()
    input_file = args.input_file
    sheet_name = args.sheet_name
    output_file = args.output_file
    
    convert(input_file, sheet_name, output_file)
