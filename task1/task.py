#Task 1

import csv
import argparse

def read_csv(file_path, row, column):
    counter = 0
    with open(file_path, 'r') as table:
        csvreader = csv.reader(table)
        for rowt in csvreader:
            if counter == row:
                try:
                    return rowt[column]
                except:
                    raise Exception('index out of range')
            
            counter += 1

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filepath')
    parser.add_argument('-r', '--row', type=int)
    parser.add_argument('-c', '--column', type=int)

    args = parser.parse_args()
    answer = read_csv(args.filepath, args.row, args.column)

    print(answer)
