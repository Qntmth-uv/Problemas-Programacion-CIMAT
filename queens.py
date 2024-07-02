import numpy as np


#METAHEURISTCAS
queen = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0]]


def local_search(board, choques):
    mut_choques = 99
    while mut_choques >= choques: 
        randomVal = np.random.randint(0, 8, 2)
        Pos = board[randomVal[0]].index(1)
        board[randomVal[0]][Pos] = 0
        board[randomVal[0]][randomVal[1]] = 1
        mut_choques = columnAttack(board) + Attack(board)
    return board 
        

def perturbacion(board):
    randomRows = np.random.randint(0, 8, size=3).tolist()
    for row in randomRows:
        queenPos = board[row].index(1)
        turnoff  = np.random.randint(0, 8)
        while queenPos == turnoff:
            turnoff  = np.random.randint(0, 8)
        board[row][queenPos] = 0
        board[row][turnoff] = 1
    return board


def printAsmatrix(board):
    for i in board:
        print(i)
    return


def columnAttack(board):
    fullfillColumns = set()
    for row in board:
        pos_col = row.index(1)
        if pos_col not in fullfillColumns:
            fullfillColumns.add(pos_col)
    if fullfillColumns.__len__() != 8:
        return 0
    else:
        return 8-fullfillColumns.__len__()
    

def Attack(board):
    coord = [(i,board[i].index(1)) for i in range(0,8)]
    def cruxSearch(board, cord: tuple):
        choques = 0
        for w in cord:
            for i in range(0, 8):
                try:
                    val = board[w[0]+i][w[1]+i]
                except IndexError:
                    break
                else:
                    if val == 1:
                        choques += 1
                    else: pass

        for w in cord:
            for i in range(0, 8):
                try:
                    val = board[w[0]-i][w[1]-i]
                except IndexError:
                    pass
                else:
                    if val == 1:
                        choques += 1
                    else: pass

        for w in cord:
            for i in range(0, 8):
                try:
                    val = board[w[0]+i][w[1]-i]
                except IndexError:
                    break
                else:
                    if val == 1:
                        choques += 1
                    else: pass
        for w in cord:
            for i in range(0, 8):
                try:
                    val = board[w[0]-i][w[1]+i]
                except IndexError:
                    pass
                else:
                    if val == 1:
                        choques += 1
                    else: pass
        if choques == 0:
            return 0
        else:
            return choques
    result = cruxSearch(board, coord)
    return result


ThereIsAnAttack = Attack(queen)
ThereIsAnAttackC = columnAttack(queen)

        
def findingAQueen(board, temperature, temperature_min, cooling_rate):
    attacks_original = 1
    while not attacks_original == 0:
        max_tem = temperature
        iter = 0
        while temperature > temperature_min:
            iter += 1
            ThereIsAnAttack_original = Attack(board)
            ThereIsAnAttackC_original = columnAttack(board)
            attacks_original = ThereIsAnAttack_original + ThereIsAnAttackC_original
            board = perturbacion(board[:])
            board_altered = local_search(board[:], attacks_original)
            ThereIsAnAttack_alt = Attack(board_altered)
            ThereIsAnAttackC_alt = columnAttack(board_altered)
            attacks_altered = ThereIsAnAttack_alt + ThereIsAnAttackC_alt
            print("Original: "+ str(attacks_original) + ", Alterado: " + str(attacks_altered))
            delta = attacks_altered - attacks_original
            if delta <= 0:
                board = board_altered
            else:
                dice = np.random.random()
                if dice < np.exp(-(delta/iter)):
                    board = board_altered
                else: pass
            temperature *= cooling_rate
        temperature = max_tem
    return board


x = findingAQueen(queen, 64, 2, 0.1)
printAsmatrix(x)
#printAsmatrix(perturbacion(queen))
#print(ThereIsAnAttack)
#print(ThereIsAnAttackC)
#printAsmatrix(mutacion(queen))