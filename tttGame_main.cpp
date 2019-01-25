#include <string>
#include "ttt_classes.cpp"

int main(){ 
    std::cout<<"-Hello Guys! Welcome to the ultimate game of TicTac and Toe\n";
    std::cout<<"-This Game will Use either 'o' or 'x' to play\n";
    std::cout<<"-Player 1 will use 'o' and player2 will use 'x' ";
    std::cout<<"-This game of Tictactoe will be played on a 4x4 gameboard\n";
    std::cout<<" to play in any position on the board type in the index(row then column.\n";
    char player1 = 'o';
    char player2 = 'x';
    bool gamePlay = true;
    Tictactoe game;
    
    while(gamePlay ==true){

        std::cout<<"-Player 1's turn. Your symbol is '" <<player1<<"'\n";
        game.play(player1);
        
        if(game.fourToWin(player1)==true){
            std::cout<<"-Player 1 wins!\n";
            break;
        }

        std::cout<<"-Player 2's turn. Your symbol is '"<<player2<<"'\n";
        game.play(player2);

        if(game.fourToWin(player2)==true){
            std::cout<<"\n-Player 2 wins!\n";
            break;
        }
        
    }
    return 0; 
}