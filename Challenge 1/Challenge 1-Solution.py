import pandas as pd
import numpy as np
def Sudoko_solver(S_arr, X, Y, num):
    for i in range(9):
        if S_arr[X][i] == num:
            return False
    for i in range(9):
        if S_arr[i][Y] == num:
            return False
    startX = X - X % 3
    startY = Y - Y % 3
    for i in range(3):
        for j in range(3):
            if S_arr[i + startX][j + startY] == num:
                return False
    return True
def Suduko_parser(S_arr, X, Y):
    if (X == 8 and Y == 9):
        return True
    if Y == 9:
        X += 1
        Y = 0
    if S_arr[X][Y] > 0:
        return Suduko_parser(S_arr, X, Y + 1)
    for num in range(1, 10, 1): 
        if Sudoko_solver(S_arr, X, Y, num):
            S_arr[X][Y] = num
            if Suduko_parser(S_arr, X, Y + 1):
                return True
        S_arr[X][Y] = 0
    return False
def Solver(input_fileName):
    grid = pd.read_csv(input_fileName, header=None)
    grid.replace(to_replace= ' ',value=0,inplace=True)
    grid = grid.astype("int")
    grid_array = grid.to_numpy()
    if(Suduko_parser(grid_array, 0, 0)):
        df = pd.DataFrame(grid_array)
        df.to_csv('sudoko_solution.csv',header=None,index=None)
    else:
        print("No solution exist")