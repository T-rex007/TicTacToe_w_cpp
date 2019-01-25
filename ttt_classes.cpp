/*Author:Tyrel Cadogan
  Email:shaqc777@yahoo.com
  Frame work for tictactoe game*/
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
    void printPosition(int row, int column);
    void play(char ox );
    void printBoard();
    bool fourToWin(char ox);
    bool isPlaceEmpty(int row, int column);
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
void Tictactoe::printPosition(int row, int column){
    std::cout<<gameBoard[row][column];
}

bool Tictactoe::isPlaceEmpty(int row, int column){
    // This function determines whether a player has played in the position or not.
    bool check = true;
    if(gameBoard[row][column] =='x'){
        check =false;
    } 
    else if(gameBoard[row][column]=='o'){
        check = false;
    }
    else{
        check = true;
    }
    return check;
}
void Tictactoe::play(char ox){
    /*Play your position on board*/
    int row;
    int column;
    std::cin>>row;
    std::cin>>column;
    if(isPlaceEmpty(row, column) ==true){
        if(ox =='x'){
            gameBoard[row][column]= ox;
            printBoard();
        }
        else if(ox == 'o'){
            gameBoard[row][column]= ox;
            printBoard();
        }
        else {
            std::cout<<"-Error: Wrong character.\n";
            std::cout<<"-Please Use 'o' or 'x' \n";
        }
    }
    else{
        std::cout<<"-This position is already Taken\n"; 
    }
}
void Tictactoe::printBoard(){
    std::cout<<std::endl;
    for(int row = 0; row<4;row++){
        std::cout<<std::setw(5);
        for(int column =0 ;column<4;column++){
            std::cout<<gameBoard[row][column]<<std::setw(5);
        }
        std::cout<<std::endl;
    }
    std::cout<<std::endl;
}
bool Tictactoe::fourToWin(char ox){
    bool checkList[4] = {checkRow(gameBoard , ox ), checkColumn(gameBoard , ox ),
     checkLeadDiagonal(gameBoard , ox ), checkNonLeadDiagonal(gameBoard , ox )};
    std::cout<<checkList[0];
    std::cout<<checkList[1];
    bool check = true;
    for(int i = 0;i<4; i++ ){
        if(checkList[i] == true){
            check = true;
            break;
        }
        else if(checkList[i] == false){
            check = false;
        } 
    }
    return check;
    
}



