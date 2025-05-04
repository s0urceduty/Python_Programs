# Clock_Metadata

# Recording time data and statistical metadata to .csv files.

# Copyright (c) 2023, Sourceduty
# This software is free and open-source; anyone can redistribute it and/or modify it.

import csv
import time
import pandas as pd
from datetime import datetime, timedelta
import os


data_file_path = 'data.csv'
statistics_file_path = 'statistics.csv'

def save_to_csv(file_path, data):
    with open(file_path, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

def append_to_statistics_csv(data):
    with open(statistics_file_path, 'a', newline='') as stats_file:
        csvwriter = csv.writer(stats_file)
        csvwriter.writerow(data)

def calculate_statistics(start_time, end_time,noOfObservations):
    return [start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'), str(noOfObservations)]

def main():
    start_time = datetime.now()
    print(f'Time_Data')
    count=0
    while True:
        current_time = datetime.now()
        print(f'The current date and time is {current_time.strftime("%Y-%m-%d %H:%M:%S")}')
        save_to_csv(data_file_path, [current_time.strftime('%Y-%m-%d %H:%M:%S')])
        time.sleep(1) 
        
        if (current_time - start_time) >= timedelta(seconds=120):
            count+=1
            stats = pd.read_csv('data.csv')
            statistics_data = calculate_statistics(start_time, current_time,len(stats))
            if not os.path.exists(statistics_file_path):
                append_to_statistics_csv(['Starting time', 'Ending time', 'Total time measurements'])
            append_to_statistics_csv(statistics_data)
            start_time = current_time
            end = (current_time + timedelta)
            exit()
            
if __name__ == '__main__':
    main()
