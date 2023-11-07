'''
    Бросаются две игральные кости - 36 событий
    Всего уникальных сумм - 11, Всего уникальных произведений - 18
    событие A - сумма значения гранец
    событие B - произведение значения граней
    Если A=3, то B=3 v 4


    Задание 1 - написать алгоритм, который построит матрицу AB
'''

import math

def get_values_matrix():
    values_sum = []
    values_prod = []

    for i in range(1, 7):
        for j in range(1, 7):
            sum_ij = i + j
            prod_ij = i * j
            values_sum.append(sum_ij)
            values_prod.append(prod_ij)
    
    values_sum = list(set(values_sum))
    values_prod = list(set(values_prod))
    
    # print(values_sum)
    # print(values_prod)
    
    matrix = [[0 for _ in range(len(values_prod))] for _ in range(len(values_sum))]

    for i in range(1, 7):
        for j in range(1, 7):
            sum_ij = i + j
            prod_ij = i * j
            matrix[values_sum.index(sum_ij)][values_prod.index(prod_ij)] += 1
    
    # for i in range(len(matrix)):
    #     print(matrix[i])

    return matrix

def get_prob_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] /= 36
            #matrix[i][j] = round(matrix[i][j], 2)
    
    # for i in range(len(matrix)):
    #     print(matrix[i])
    
    return matrix

def compute_single_entropy(matrix, by='row'):
    entropy = 0.0
    
    if by == 'row':
        for i in range(len(matrix)):
            h = 0.0
            for value in matrix[i]:
                if value != 0.0:
                    h += value

            h = -1 * h * math.log2(h)
            entropy += h
    
    elif by == 'column':
        for i in range(len(matrix[0])):
            h = 0.0
            for j in range(len(matrix)):
                if matrix[j][i] != 0.0:
                    h += matrix[j][i]
            
            h = -1 * h * math.log2(h)
            entropy += h
    
    return entropy

def compute_joint_entropy(matrix):
    entropy = 0.0
    for i in range(len(matrix)):
        h = 0.0
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0.0:
                h += -1 * matrix[i][j] * math.log2(matrix[i][j])
        entropy += h

    return entropy

def compute_conditional_entropy(matrix, prob_matrix):
    prob_matrix_cond = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            prob_matrix_cond[i][j] = matrix[i][j] / sum(matrix[i])

    entropy = 0.0
    for i in range(len(prob_matrix_cond)):
        h_si = 0.0
        for j in range(len(prob_matrix_cond[i])):
            if prob_matrix_cond[i][j] != 0.0:
                h_si += -1 * prob_matrix_cond[i][j] * math.log2(prob_matrix_cond[i][j])
        h = h_si * sum(prob_matrix[i])
        entropy += h

    return entropy

def task():
    matrix = get_values_matrix()

    prob_matrix = get_prob_matrix(matrix)
    
    entropy_A = compute_single_entropy(prob_matrix, by='row')
    entropy_B = compute_single_entropy(prob_matrix, by='column')

    entropy_AB = compute_joint_entropy(prob_matrix)

    entropy_B_A = compute_conditional_entropy(matrix, prob_matrix)

    return entropy_A, entropy_B, entropy_AB, entropy_B_A

if __name__ == '__main__':
    task()