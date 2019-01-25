/*Author: Tyrel Cadogan
  Email: shaqc777@yahoo.com/tyrel.cadogan@my.uwi.edu
*/
bool checkLeadDiagonal(char board[4][4], char ox);
bool checkNonLeadDiagonal(char board[4][4], char ox);
bool checkRow(char board[4][4], char ox);
bool checkColumn(char board[4][4], char ox);


bool checkRow(char board[4][4], char ox){
    bool check = true;
    for(int i= 0; i<4;i++){
        check = true;
        for(int j =0;j<4; j++){
            if(board[i][j] != ox){
                check = false;
                break;
            }
            else{
                //Do Nothing
            }
        
        }
        if(check == true){
            break;
        
        }
    }
    return check;
}

bool checkColumn(char board[4][4], char ox){
    bool check =true;
    for(int i= 0; i<4;i++){
        check = true;
        for(int j =0;j<4; j++){
            if(board[j][i] != ox){
                check = false;
                break;
            }
            else{
                //Do Nothing
            }
        
        }
        if(check == true){
            break;
        
        }
    }
    return check;
}

bool checkLeadDiagonal(char board[4][4], char ox){
    //Leading Diagonal
    bool check = true;
    for(int i =0;i<4;i++){
        if(board[i][i] != ox){
            check = false;
            break;
        }
        else{
            //Do Nothing
        }
    }
    return check;
}
bool checkNonLeadDiagonal(char board[4][4], char ox){
    int row = 0;
    int column =3;
    int check = true;
    while(row<4){
        if(board[row][column] !=ox){
            check = false;
            break;
        }
        row = row +1;
        column = column -1;

    }
    return check;
}