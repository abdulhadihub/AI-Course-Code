# Define the dictionary of words
dictionary = ['START', 'NOTE', 'SAND', 'STONED']  # Add more words to the dictionary

# Define the board of letters

board = [
    ["M", "S", "E", "F"],
    ["R", "A", "T", "D"],
    ["L", "O", "N", "E"],
    ["K", "A", "F", "B"]
]
# Define directions for exploring neighboring cells (horizontally, vertically, diagonally)
directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
found_words = set()
def DFS_for_boogle(x,y,visited, current_word):
    
    #base case if the current word is in the dictionary
    if current_word in dictionary:
        found_words.add(current_word)
        return
    #if its not in the dictionary then we will explore its neighbors
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        #check if the new coordinates are in the board
        if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]):
            #check if the new coordinates are not visited
            if visited[new_x][new_y] == False:
                #mark the new coordinates as visited
                visited[new_x][new_y] = True
                #add the new letter to the current word
                current_word += board[new_x][new_y]
                #recursively call the function
                DFS_for_boogle(new_x, new_y, visited, current_word)
                #backtrack
                current_word = current_word[:-1]
                visited[new_x][new_y] = False
    return found_words


def find_words(board):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            visited[i][j] = True
            DFS_for_boogle(i, j, visited, board[i][j])
            visited[i][j] = False
    return found_words

find_words(board)