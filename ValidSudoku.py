# runtime: 39ms

# board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
board =[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]


nestD = {}
rowD = {}
colD = {}
flag = True
for i in range(0,9):
    nestD[i] = {}
    colD[i] = {}
    rowD[i] = {}
count = 0


for i in range(0,9):
    for j in range(0,9):
        # count += 1
        if board[i][j] in nestD[int(i/3)*3 + int(j/3)] and board[i][j] != ".":
            nestD[int(i/3)*3 + int(j/3)][board[i][j]] += 1
            if nestD[int(i/3)*3 + int(j/3)][board[i][j]] > 1:
                flag = False
        elif board[i][j] != ".":
            nestD[int(i/3)*3 + int(j/3)][board[i][j]] = 1



        if board[j][i] in colD[i] and board[j][i] != ".":
            colD[i][board[j][i]] += 1
            if colD[i][board[j][i]] > 1:
                flag = False
        elif board[j][i] != ".":
            colD[i][board[j][i]] = 1

        if board[i][j] in rowD[i] and board[i][j] != ".":
            rowD[i][board[i][j]] += 1
            if rowD[i][board[i][j]] > 1:
                flag = False
        elif board[i][j] != ".":
            rowD[i][board[i][j]] = 1

        

        
        

print("nestD: ", nestD)
# print(nestD)
print("colD: ", colD)
print("rowD: ", rowD)
print(flag)