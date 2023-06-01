#include <stdio.h>
#include <string.h>
#include <stdbool.h>
/*
R = {1, 2, 3, 4, 5, 6, 7}
C = {1, 2, 3, 4, 5}
all boxes P = { {1,1}, {1,2}, {1,3}, {1,4}, {1,5}, {2,1}, {2,2}, ..., {7,5}}
all same colored boxes S = { {1,1}, {1,3}, {1,5}, {2,2}, {2,4}, {3,1}, {3,3}, {3,5}, {4,2}, {4,4},
				   		   {5,1} {5,3}, {5,5}, {6,2}, {6,4}, {7,1}, {7,3}, {7,5}}

start point Beta pieces Y = { {1,1}, {1,3}, {1,5}, {2,2}, {2,4} }
start point Alpha pieces E = { {6,2}, {6,4}, {7,1}, {7,3}, {7,5} }

Free: {1,2}{1,4}
{2,1}{2,3}{2,5}
{3,1}{3,2}{3,3}{3,4}{3,5}
{4,1}{4,2}{4,3}{4,4}{4,5}
{5,1}{5,2}{5,3}{5,4}{5,5}
{6,1}{6,3}{6,5}
{7,2}{7,4}

B = {true, false}
*/

typedef struct{
	int x;
	int y;
	int dead;
} set;
/*InitVar() initializes the x and y values in the set passed to it
@param Set[] - Set to be initialized
@paran aTurn - identifier for whether the set is Alpha or Beta*/
void InitVar(set Set[], bool aTurn){
	int x, i = 0, y = 1; 
	
	if(aTurn)
		x = 7;
	else if (!aTurn)
		x = 1;	
	
	for (i = 0; i < 5; i++){
		Set[i].x = x;
		Set[i].y = y;
		Set[i].dead = 0;
		y++;
		if(x == 7 || x == 2)
			x--;
		else
			x++;	
	}
}
/*Initialize set Free*/
void InitFree(set Free[]){
	int x = 2, y = 1;
	
	for(int i = 0; i < 35; i++){
		if (i > 24){
			x = 0;
			y = 0;
			Free[i].dead = 0;
		}
		else
			Free[i].dead = 1;
		Free[i].x = x;
		Free[i].y = y;
		y++;
		if (y > 5){
			y = 1;
			x++;
		}
		if(x == 2 || x == 7)
			x--;
		else if((x == 1 || x == 6) && y != 1)
			x++;

	}
}
/*PrintBoard() prints the game on to the screen for a good visual experience and easier time playing
@param Alpha[] - Set Alpha
@param Beta[] - Set Beta*/
void PrintBoard(set Alpha[], set Beta[]){
	printf("       1       2       3       4       5       6       7\n");
	printf("   ---------------------------------------------------------\n");
	for (int i = 0; i < 5; i++){
		printf(" %d |", i+1);
		for (int j = 0; j < 7; j++){
			for (int k = 0; k < 5; k++){
				
				if (i+1 == Alpha[k].y && j+1 == Alpha[k].x && Alpha[k].dead == 0)
				{
					printf("   A   |");
				
					k = 5;
				}
				else if((i+1 == Beta[k].y && j+1 == Beta[k].x && Beta[k].dead == 0))
				{
					printf("   B   |");
					
					k = 5;
				}
				else if (k == 4)
					printf("       |");
			}
		}
		printf("\n   ---------------------------------------------------------\n");
	}
}
/*TakePiece() is the first step to moving a piece. This function asks the user which piece they want to move and checks if their input is valid
@param Set[] - The set of the current player whose turn it is
@param Free[] - set of all spaces not in sets Alpha and Beta
@param *i - the index denoting the location of (a,b) in Set[]
@param *a - the x coordinate of the piece that the player wants to move
@param *b - the y coordinate of the piece that the player wants to move
@param aTurn - used to check if it is player Alpha or Beta's turn to move
@returns 1 if the chosen location has a valid piece, 0 otherwise*/
int TakePiece(set Set[], set Free[], int *i, int *a, int *b, bool aTurn){
	int clear;
	*a = 0; *b = 0;
	while (*a < 1 || *a > 7){ //a is not in the domain
		printf("x: ");
		scanf("%d", a);
		while ((clear = getchar()) != '\n' && clear != EOF ){};//clear input buffer
		if((!aTurn && *a+1 == 8) || (aTurn && *a-1 == 0)){
			printf("You can't move units here\n");
			*a = 0;
		}
	}
	while (*b < 1 || *b > 5){// y is not in the range
		printf("\ny: ");
		scanf("%d", b);
		if(*b == 0){
			printf("Move canceled\n");
			return 0;
		}
		while ((clear = getchar()) != '\n' && clear != EOF ){};//clear input buffer
	}
	for(*i = 0; *i < 5; *i+=1){
		if(*a == Set[*i].x && *b == Set[*i].y && Set[*i].dead == 0){//(a,b) is a subset of Set and piece Set[*i] is is not dead
			return 1;
		}
	}
	printf("\nYou have no piece in that space\n");
	return 0;
}
/*MoveWhere() is the next step to moving a piece. This function asks the user where they want to move their chosen piece to
This function also checks if the coordinates they input is a valid move
@param Set[] - the set of the current player whose turn it is
@param a - the x coordinate of the piece the player wants to move
@param b - the y coordinate of the piece the player wants to move
@param *c - the x coordinate of the place the player wants to move their piece to
@param *d - the y coordinate of the place the player wants to  move their piece to
@param *ok - used to check if all inputs are valid and the game may proceed
@param aTurn - used to check if it is player Alpha or player Beta's turn
@returns 0 if the player chooses to cancel move (by setting c or d to 0) or if the player already has a piece in the target
coordinates, returns 1 if move is valid and final*/
int MoveWhere(set Set[], int a, int b, int *c, int *d, bool *ok, bool aTurn){
	int clear; //used to clear input buffer only
	*c = 0; *d = 0;
	if(aTurn){ //Get c
		do{
			printf("x: ");
			scanf("%d", c);
			while ((clear = getchar()) != '\n' && clear != EOF ){};//clear input buffer
			if (*c == 0){ //player can input 0 to cancel their choices
				printf("Move canceled\n");
				return 0;
			}
		} while (*c + 1 != a || *c < 0 ); //set cant move forward if they are at the end of the board
	}
	else if (!aTurn){
		do{
			printf("x: ");
			scanf("%d", c);	
			while ((clear = getchar()) != '\n' && clear != EOF ){};//clear input buffer
			if(*c == 0){
				printf("Move canceled\n");
				return 0;
			}
		} while (*c != a+1 || *c > 7); //set cant move forward when they are at the end of the board
	}
	printf("\n");
	do{ //Get d
		printf("y: ");
		scanf("%d:", d);
		while ((clear = getchar()) != '\n' && clear != EOF ){};//clear input buffer
		if(*d == 0){
			printf("Move canceled\n");
			return 0;
		}
	} while (((*d != b) && (*d != b+1) && (b != *d+1)) || (*d > 5 || *d < 1)); //&& area --- mp specs; || area - to prevent out of bounds play
	
	for (int j = 0; j < 5; j++){ //Check if move is valid
		if(*c == Set[j].x && *d == Set[j].y && Set[j].dead == 0) // spot is taken 
		{
			printf("\nYou already have a piece here\n");
			return 0;
		}
		else if ((j == 4) && (*c != Set[j].x || *d != Set[j].y || Set[j].dead != 0)) //spot is not taken
		{
			*ok=!*ok;
		}
	}
	return 1;
}
/*MovePiece() is the final step to moving a piece. This function checks if the move is an eat or a free space and
changes all relevant values in all relevant sets accordingly
@param SetPlay[] - is the set of the player in play
@param SetIdle[] - is the set of the player who is waiting for their turn
@param Free[] - is the free spaces on the board
@param a - is the x coordinate of the piece the player wants to move
@param b - is the y coordinate of the piece the player wants to move
@param c - is the x coordinate of the target location of the player
@param d - is the y coordiante of the target location of the player
@param i - is the index of (a,b) in SetPlay[]
@param ok - variable that controls if the game is ok to proceed or not
@param aTurn - used to check which player's turn it is
@returns ok*/
bool MovePiece(set SetPlay[], set SetIdle[], set Free[], int a, int b, int c, int d, int i, bool ok, bool *aTurn){	
	for (int j = 0; j < 35; j++){
		if (c == Free[j].x && d == Free[j].y){
			SetPlay[i].x = c; // (Beta/Alpha - prev) U next
			SetPlay[i].y = d;
			Free[j].x = a; //(Free - next)U prev
			Free[j].y = b;
			ok = !ok; //ok now false
			*aTurn = !*aTurn; //change turns
		}
	}
	if(ok){ //if previous loop did not find match
		for (int j = 0; j < 5; j++){
			if (c == SetIdle[j].x && d == SetIdle[j].y){ //if next is in SetIdle	
				if(c%2 == d%2){ //if (c,d) is in S
					SetIdle[j].dead = 1; //piece is eaten thus dead
					SetIdle[j].x = 0; 
					SetIdle[j].y = 0;
					SetPlay[i].x = c;
					SetPlay[i].y = d;
					
					for (int k = 0; k < 10; k++){ //New free spot on the board
						if (Free[k+25].dead == 0){
							Free[k+25].x = a;
							Free[k+25].y = b;
							Free[k+25].dead =1;
							k+=10; 
						}
					}
					*aTurn = !*aTurn; //aTurn change
				}
				ok = !ok;
			}
		}
	}
	return ok;
}
/*NetPlayerMove() prints the relevant text and calls the functions that control the player movement
@param Alpha[] - set Alpha
@param Beta[] - set Beta
@param Free[] - the space on the board that is not taken by Alpha[] or Beta[]
@param aTurn - used to check which player's turn it is
@param ok - used to signify if the game is clear to proceed
@returns aTurn*/ 
bool NextPlayerMove(set Alpha[], set Beta[], set Free[], bool aTurn, bool ok){
	int a, b, c, d, cont = 0, i;
	PrintBoard(Alpha, Beta);
	
	if(aTurn){
		printf("Player Alpha Turn\n");
		while (!ok){
			while (cont == 0){
				printf("\nChoose a piece to move\n");
				cont = TakePiece(Alpha, Free, &i, &a, &b, aTurn); //Get (a,b) - error checking also done
			}
			printf("\nWhere do you want to move it?\n");
			cont = MoveWhere(Alpha, a, b, &c, &d, &ok, aTurn); //Get (c,d) - error checking also done
		}
		while (ok){
			ok = MovePiece(Alpha, Beta, Free, a, b, c, d, i, ok, &aTurn); //process set move
		}
	}
	else if (!aTurn){
		printf("Player Beta Turn\n");
		while (!ok){
			while (cont == 0){
				printf("\nChoose a piece to move\n");
				cont = TakePiece(Beta, Free, &i, &a, &b, aTurn); //Get (a,b) - with error checking
			}
			printf("\nWhere do you want to move it?\n");
			cont = MoveWhere(Beta, a, b, &c, &d, &ok, aTurn); //Get (c,d) - with error checking
		}
		while (ok){
			ok = MovePiece(Beta, Alpha, Free, a, b, c, d, i, ok, &aTurn); //process set move
		}
	}
	return aTurn;
}
/*CountPieces() counts the number of pieces still alive held by the player
@param Set[] - is the Set whose number of pieces will be counted
@returns ctr - counter for how many pieces are still alive*/
int CountPieces(set Set[]){
	int ctr = 0;
	for(int i = 0; i < 5; i++)
	{
		if(Set[i].dead == 0)
			ctr++;
	}
	return ctr;
}
/*checkWin() checks win conditions as specified in the specs and includes a few scenarios that may happen due to how the game works
@param Set[] - is the set of the player who just made their move
@param SetIdle[] - set of the player who is waiting for their turn
@param over - signifies if the game is over or not
@param EnemyBase[] - set containing the locations of the enemy base that Set[] needs to be in to trigger one of the win conditions
@param OwnBase[] - set containing the locations of the base of the player who owns Set[] that SetIdle[] needs to be in to trigger one of the win conditions
@param aTurn - used to identify whose turn it is
@returns over
*/
bool checkWin(set Set[], set SetIdle[], bool over, set EnemyBase[], set OwnBase[], bool aTurn){
	int pcCtr, check = 0;
	for (int i = 0; i < 5; i++){
		if(SetIdle[i].dead == 1)
			check++;
	}
	if(check == 5){ //if all are dead
		over = !over;
		if(!aTurn){
			PrintBoard(SetIdle, Set);
			printf("\nBeta win\n");
		}
		else if (aTurn){
			PrintBoard(Set, SetIdle);
			printf("\nAlpha win\n");
		}
		return over;
	}
	else{ //if there are still pieces alive
		check = 0;
		pcCtr = CountPieces(Set); //count how many pieces alive
		for (int i = 0; i < 5; i++){ //check how many pieces have set up in the enemy base for the other win condition
			for(int j = 0; j<5; j++){ 
				if(Set[j].dead == 0 && Set[j].x == EnemyBase[i].x && Set[j].y == EnemyBase[i].y)
					check++;
			}
		}
		if (check == pcCtr){ //if all pieces are in the enemy base
			if(!aTurn){
				PrintBoard(SetIdle, Set);
				printf("\nBeta Win\n");
				}
			else if(aTurn){
				PrintBoard(Set, SetIdle);
				printf("\nAlpha Win\n");
			}
			over = !over;
			return over;
		}
		else{
			check = 0;
			pcCtr = CountPieces(SetIdle); //count how many pieces are still alive for the enemy
			for (int i = 0; i < 5; i++){ //happens when the last move player eats the enemy's last unit not stationed for win condition
				for(int j = 0; j<5; j++){ //check if all alive enemy units are in the last move player's base
					if(SetIdle[j].dead == 0 && SetIdle[j].x == OwnBase[i].x && SetIdle[j].y == OwnBase[i].y)
						check++;
				}
			}
			if(check == pcCtr){
				if(!aTurn){
					PrintBoard(SetIdle, Set);
					printf("\nAlpha Win\n");
				}
				else if(aTurn){
					PrintBoard(Set, SetIdle);
					printf("\nBeta Win\n");
				}
				over = !over;
				return over;
			}
			
		}
		for (int i = 0; i < 5; i++){
				if(!aTurn){ //checks if the player puts a piece at the wrong space on the end of the board (they cant move anymore)
					if(Set[i].dead == 0 && (Set[i].x + 1 == 8) && (Set[i].x%2 != Set[i].y%2)){
						over = !over;
						PrintBoard(SetIdle, Set);
						printf("Player Beta has a piece that can't move and does not satisfy a win condition\n");
						printf("\nAlpha Win\n");
						return over; //game ends because none of the win conditions can be satisfied for that player
					}
				}
				else if (aTurn){ //same as above
					if (Set[i]. dead == 0 && (Set[i].x - 1 == 0) && (Set[i].x%2 != Set[i].y%2)){
						over = !over;
						PrintBoard(Set, SetIdle);
						printf("Player Alpha has a piece that can't move and does not satisfy a win condition\n");
						printf("\nBeta Win\n");
						return over;
					}
				}
			}
	}
	return over;
}
int main(){
 	set Alpha[5], Beta[5], Y[5], E[5], Free[35];
 	 	
	bool over = false,
		 aTurn = true,
		 ok = false;
	
	/*Initialize the values in E, Y, and Free*/
	InitVar(E, aTurn);
	aTurn = !aTurn;
	InitVar(Y, aTurn);
	aTurn = !aTurn;
	InitFree(Free);
	//Alpha = E, Beta = Y
	for(int i = 0; i < 5; i++){
		Alpha[i] = E[i];
		Beta[i] = Y[i];
	}
	while (!over){
		aTurn = NextPlayerMove(Alpha, Beta, Free, aTurn, ok);
		if (!aTurn)
			over = checkWin(Alpha, Beta, over, Y, E, !aTurn);
		else if (aTurn)
			over = checkWin(Beta, Alpha, over, E, Y, !aTurn);
	}
	return 0;
}
