import numpy as np

def compute_kendell(experts):
    rank_matrix = [[0 for i in range(len(experts))] for _ in range(len(experts[0]))]
    rank_matrix_eta = [[len(experts[0]) - j for _ in range(len(experts))] for j in range(len(experts[0]))]
    all_elements = sorted(experts[0])

    for i in range(len(experts)):
        for j in range(len(experts[i])):
            rank_matrix[j][i] = len(experts[i]) - experts[i].index(all_elements[j])

    rank_matrix = np.array(rank_matrix)
    rank_matrix_eta = np.array(rank_matrix_eta)

    disp_rank_matrix_eta = ((rank_matrix_eta.sum(axis=-1) - rank_matrix_eta.sum(axis=-1).mean())**2).sum() / (len(experts[0]) - 1)
    disp_rank_matrix =  ((rank_matrix.sum(axis=-1) - rank_matrix.sum(axis=-1).mean())**2).sum() / (len(experts[0]) - 1)

    print(disp_rank_matrix)
    print(disp_rank_matrix_eta)

    return disp_rank_matrix / disp_rank_matrix_eta

def task():
    expert_A = ["O1","O2","O3"]
    expert_B = ["O1","O3","O2"]
    expert_C = ["O1","O3","O2"] 
    
    experts = [expert_A, expert_B, expert_C]

    res = compute_kendell(experts)
    print(res)

if __name__ == "__main__":
    task()
