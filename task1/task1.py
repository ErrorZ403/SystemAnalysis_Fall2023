import json
import argparse

def read_graph(file_path):
    with open(file_path, 'r') as jfile:
        data = json.load(jfile)

    for vertice in data:
        print(f"Вершина: {vertice} \t Список соседей: {' '.join(data[vertice])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filepath')

    args = parser.parse_args()

    read_graph(args.filepath)