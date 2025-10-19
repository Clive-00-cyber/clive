#include <iostream>
using namespace std;

char board[3][3] = {{'1','2','3'}, {'4','5','6'}, {'7','8','9'}};
char currentPlayer = 'X';

void drawBoard() {
    system("cls");  // Clear screen (for Windows)
    cout << "Tic-Tac-Toe\n";
    for(int i=0; i<3; i++) {
        cout << " " << board[i][0] << " | " << board[i][1] << " | " << board[i][2] << endl;
        if(i < 2) cout << "-----------\n";
    }
}

bool checkWin() {
    // Check rows and columns
    for(int i=0; i<3; i++) {
        if(board[i][0] == board[i][1] && board[i][1] == board[i][2]) return true;
        if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) return true;
    }
    // Check diagonals
    if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) return true;
    if(board[0][2] == board[1][1] && board[1][1] == board[2][0]) return true;
    return false;
}

bool checkDraw() {
    for(int i=0; i<3; i++)
        for(int j=0; j<3; j++)
            if(isdigit(board[i][j])) return false;
    return true;
}

int main() {
    int choice;
    bool gameOver = false;

    do {
        drawBoard();
        cout << "Player " << currentPlayer << ", enter position (1-9): ";
        cin >> choice;

        int row = (choice-1)/3;
        int col = (choice-1)%3;

        if(choice <1 || choice >9 || !isdigit(board[row][col])) {
            cout << "Invalid move! Try again.\n";
            continue;
        }

        board[row][col] = currentPlayer;
       
        if(checkWin()) {
            drawBoard();
            cout << "Player " << currentPlayer << " wins!\n";
            gameOver = true;
        } else if(checkDraw()) {
            drawBoard();
            cout << "It's a draw!\n";
            gameOver = true;
        }
       
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';

    } while(!gameOver);

    return 0;
}