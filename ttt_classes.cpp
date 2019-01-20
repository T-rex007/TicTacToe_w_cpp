#include <iostream>
#include <iomanip>
#include <string>
#include "ttt_function.cpp"

class Tictactoe
{
private:
    char gameBoard[4][4];
public:
    Tictactoe();
    void play(int row, int column, char ox );
    void printBoard();
    bool fourToWin();
};

Tictactoe::Tictactoe()
{
    for(int row = 0; row<4;row++){
        std::cout<<std::setw(5);
        for(int column =0 ;column<4;column++){
            gameBoard[row][column] = '-';
            std::cout<<gameBoard[row][column]<<std::setw(5);
        }
        std::cout<<std::endl;
    }
}
void Tictactoe::play(int row, int column, char ox){
    if(ox =='x'){
        gameBoard[row][column]= ox;
        printBoard();
    }
    else if(ox == 'o'){
        gameBoard[row][column]= ox;
        printBoard();
    }
    else {
        std::cout<<"-Error: Wrong character.";
        std::cout<<"-Please Use 'o' or 'x' ";
    }
}
void Tictactoe::printBoard(){
    std::cout<<std::endl;
    for(int row = 0; row<4;row++){
        std::cout<<std::setw(5);
        for(int column =0 ;column<4;column++){
            gameBoard[row][column] = '-';
            std::cout<<gameBoard[row][column]<<std::setw(5);
        }
        std::cout<<std::endl;
    }
    std::cout<<std::endl;
}
bool Tictactoe::fourToWin(char ox){
    bool 

}



