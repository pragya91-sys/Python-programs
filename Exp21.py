m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

board = []
print("Enter board:")
for _ in range(m):
    board.append(list(input().split()))

word = input("Enter word: ")

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = "#"

        found = (dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or
                 dfs(i, j+1, k+1) or dfs(i, j-1, k+1))

        board[i][j] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False

print("Output:", exist(board, word))