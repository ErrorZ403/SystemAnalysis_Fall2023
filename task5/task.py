import json
import numpy as np

'''
Метод согласования кластеризованных ранжировок

A = [1 < {2, 3} < 4 < {5, 6, 7} < 8 < 9 < 10]
B = [{1, 2} < {3, 4, 5} < 6 < 7 < 9 < {8, 10}]
C = [3 < {1, 4} < 2 < 6 < {5, 7, 8} < {9, 10}]
'''

def read_json(file):
    with open(file, 'r') as f:
        a = json.load(f)
    
    return a

def make_matrix_from_expert(expert_list):
    expert_list_indexes = []
    expert_list_flatten = []
    position = 0
    for cluster in expert_list:
        if isinstance(cluster, int):
            cluster = [cluster]
        for value in cluster:
            expert_list_indexes.append(position)
            expert_list_flatten.append(value)
        position += 1
            
    matrix = [[0 for _ in range(len(expert_list_flatten))] for _ in range(len(expert_list_flatten))]

    for i in range(len(expert_list_indexes)):
        for j in range(len(expert_list_indexes)):
            if expert_list_indexes[expert_list_flatten.index(i + 1)] <= expert_list_indexes[expert_list_flatten.index(j + 1)]:
                matrix[i][j] = 1

    return matrix

def get_kernel_of_nonequal(matrix_1, matrix_2):
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)

    kernel = np.multiply(matrix_1, matrix_2)
    kernel_T = np.multiply(matrix_1.T, matrix_2.T)

    kernel_res = np.logical_or(kernel, kernel_T).astype(np.int32)
    result = []
    
    for i in range(len(kernel_res)):
        for j in range(len(kernel_res[i])):
            if kernel_res[i][j] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in result:
                    result.append(pair)

    print(result)
    return result

def _in_kernel(value, kernel):
    for cluster in kernel:
        if value in cluster:
            return (True, cluster)
    return (False, [])

def make_experted_res(expert_1, expert_2, kernel):
    result = []
    #print(kernel)

    for i in range(len(expert_1)):
        if isinstance(expert_1[i], int): 
            expert_1[i] = [expert_1[i]]
        for value in expert_1[i]:
            flag, cluster = _in_kernel(value, kernel)
            if flag:
                if cluster not in result:
                    result.append(cluster)
            else:
                result.append(value)

    print(result)

def task():
    expert_A = [1,[2,3],4,[5,6,7],8,9,10] #read_json(r'D:\SystemAnalysis_Fall2023\task5\Ранжировка  A.json')
    expert_B = [[1,2],[3,4,5],6,7,9,[8,10]] #read_json(r'D:\SystemAnalysis_Fall2023\task5\Ранжировка  B.json')
    expert_C = [3,[1,4],2,6,[5,7,8],[9,10]] #read_json(r'D:\SystemAnalysis_Fall2023\task5\Ранжировка  C.json')
    matrix_A = make_matrix_from_expert(expert_A)
    matrix_B = make_matrix_from_expert(expert_B)
    matrix_C = make_matrix_from_expert(expert_C)
    kernel_AB = get_kernel_of_nonequal(matrix_A, matrix_B)
    kernel_BC = get_kernel_of_nonequal(matrix_B, matrix_C)
    kernel_AC = get_kernel_of_nonequal(matrix_A, matrix_C)

    make_experted_res(expert_A, expert_B, kernel_AB)
    make_experted_res(expert_B, expert_C, kernel_BC)
    make_experted_res(expert_A, expert_C, kernel_AC)

if __name__ == '__main__':
    task()