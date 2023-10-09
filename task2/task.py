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

def read_graph_from_csv(filepath):
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
    
    return all_keys

def count_types(graph, all_keys):
    answer = {}
    for key in all_keys:
        answer[key] = [0, 0, 0, 0, 0]

    q = [(list(graph.keys())[0], 0)]
    last_key = []
    last_deep = []

    while q:
        key, deep = q.pop(0)
        
        if last_key:
            if deep == last_deep:
                answer[key][4] += 1
                answer[last_key[last_deep]][4] += 1
            elif deep == 1:
                answer[key][1] += 1
            elif deep >= 2:
                answer[key][3] += 1
                answer[last_key][2] += 1
        
        
        if key in graph:
            answer[key][0] += len(graph[key])
        
        if key in graph:
            for elem in graph[key]:
                q.append((elem, deep+1))

        last_key.append(key)
        last_deep = deep

    print(answer)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filepath')

    args = parser.parse_args()

    graph = read_graph_from_csv(args.filepath)

    all_keys = _get_keys(graph)

    ans = count_types(graph, all_keys)