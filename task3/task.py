'''
Задание: оценить разнообразие системы с помощью подсчета энтропии
На вход: csv-строку с прошлого задания. Выход: величина энтропии графа с предыдущего задания

Подсчет энтропии: p_21 = l_21 / (n - 1), где n = 6
H_i = - sum(p_ij * log(p_ij)) for j = 1 to k, где k - кол-во отношений
'''

import csv
import argparse
import math

def _read_relation_matrix_from_csv(filepath):
    matrix = []
    with open(filepath, 'r') as table:
        csvreader = csv.reader(table)
        for row in csvreader:
            matrix.append(row)

    return matrix

def _compute_probability_matrix(matrix):
    prob_matrix = []
    n = len(matrix)
    for row in matrix:
        temp_probs = []
        for value in row:
            temp_probs.append(float(value) / (n - 1))

        prob_matrix.append(temp_probs)

    return prob_matrix

def _compute_entropy_for_row(prob_matrix):
    entropies = []

    for row in prob_matrix:
        h = 0.0
        for value in row:
            if value != 0.0:
                h += -1 * value * math.log2(value)
        
        entropies.append(h)
    
    return entropies

def task(filename):
    matrix = _read_relation_matrix_from_csv(filename)
    prob_matrix = _compute_probability_matrix(matrix)
    #print(prob_matrix)
    entropies = _compute_entropy_for_row(prob_matrix)

    entropy = 0.0
    for value in entropies:
        entropy += value

    return entropy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filepath')

    args = parser.parse_args()

    res = task(args.filepath)
    print(res)
