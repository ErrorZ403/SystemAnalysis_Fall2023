'''
    '1'       I     Ученый совет
     | 
    '2'       II    Ректор
    / \
  '3'  '4'    III   Директора институтов
  / \
'5' '6'       IV    Кафедры

Матрица смежности:
1,0,1,0,0,0,0
2,1,0,1,1,0,0
3,0,1,0,0,1,1
4,0,1,0,0,0,0
5,0,0,1,0,0,0
6,0,0,1,0,0,0

Список ребер:
1,2
2,3
2,4
3,5
3,6

Метрики: 
1. Выделяем элементы графа и связи (ребра). И используем их для метрик
2. Надо посчитать количество видов отношений, в которые он вступает
- Пусть количество элеметнтов n = 6. 
- Пусть количнство отношений m = 5
- r = {r1, r2, ..., rm}: 
> r1 - 'я начальник' (родитель), 
> r2 - 'я подчиненный' (ребенок), 
> r3 - 'у моего подчиненного есть подчиненный' (внуки)
> r4 - 'у моего начальника есть начальник' (прародители)
> r5 - 'соподчение' (детей >1)

1) граф -> csv
2) посчитать для элемента количество вхождений в типа в отношений (n x m)
'''

import csv
import argparse

def _read_graph_from_csv(filepath):
    dict = {}
    with open(filepath, 'r') as table:
        csvreader = csv.reader(table)
        for row in csvreader:
            #print(row)
            if row[0] not in dict:
                dict[row[0]] = row[1:]
            else:
                dict[row[0]].extend(row[1])

    return dict

def _get_keys(graph):
    all_keys = []
    for key in graph:
        if key not in all_keys:
            all_keys.append(key)
        for elem in graph[key]:
            if elem not in all_keys:
                all_keys.append(elem)
    
    return all_keys, len(all_keys)

def _compute_matrix(graph, ln):
    matrix = [[0 for _ in range(ln)] for _ in range(ln)]
    
    for k in graph:
        for v in graph[k]:
            matrix[int(k) - 1][int(v) - 1] = 1
            matrix[int(v) - 1][int(k) - 1] = -1

    return matrix

def make_csv(matrix, file_name='task_res.csv'):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in matrix:
            writer.writerow(row)
        

def task(filename):
    graph = _read_graph_from_csv(filename)
    _, ln = _get_keys(graph)
    matrix = _compute_matrix(graph, ln)

    result = [[0 for _ in range(5)] for _ in range(ln)]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result[i][0] += 1
                for index, value in enumerate(matrix[j]):
                    if value == 1:
                        result[i][2] += 1
            if matrix[i][j] == -1:
                result[i][1] += 1
                for index, value in enumerate(matrix[j]):
                    if value == -1:
                        result[i][3] += 1
                    if value == 1 and index != i:
                        result[i][4] += 1
    make_csv(result)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filepath')

    args = parser.parse_args()

    task(args.filepath)