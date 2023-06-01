/****************************************************************** 
This is to certify that this project is my own work, based on my personal efforts in studying and applying the 
concepts learned. I have constructed the functions and their respective algorithms 
and corresponding code by myself. The program was run, tested, and debugged by my own efforts. I further 
certify that I have not copied in part or whole or otherwise plagiarized the work of other students and/or 
persons.  
 
Orrin Landon T. Uy, DLSU ID# 12111287 
******************************************************************/ 
/*
	Description : A text-based game based on Animal Crossing: New Horizons where the user buys turnips and tries to sell them for profit (heavy rng involved)
	Programmed by : Orrin Landon T. Uy S20A
	Last Modified: January 27, 2022
	Version: <4.0>
	[Acknowledgements: https://www.geeksforgeeks.org/generating-random-number-range-c/
	https://www.tutorialspoint.com/c_standard_library/c_function_getchar.htm
	https://www.geeksforgeeks.org/use-fflushstdin-c/#:~:text=fflush()%20is%20typically%20used,case%20of%20file%20output%20stream).
*/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>

/*This function prints the game description*/
void about()
{
	printf("\n-------------------------------------------------------\n\n");	
	printf("About the game:\n\n");
	printf("This is a text-based game based on the Nintendo Switch\n");
	printf("game Animal Crossing New Horizons. \n");
	printf("\nHere, players will go on a 20 week journey to become\n");
	printf("the next millionaire. Will you be the next Beff Jezos\n");
	printf("or will you go broke? Play the game to find out!\n");
}
/*This function prints the game objectives*/
void obj()
{
	printf("\n-------------------------------------------------------\n\n");
	printf("Objectives of the game:\n\n");
	printf("To clear the game, you must earn 1,000,000 bells.\n");
	printf("You will start with a capital of 5,000 bells\n");
	printf("\nand you will have 20 weeks to reach 1 million bells.\n");
}
/*This function prints information about the core gameplay*/
void currency()
{
	printf("\n-------------------------------------------------------\n\n");
	printf("About the currency:\n\n");
	printf("The main currency featured in this game is called bells.\n");
	printf("To earn bells, you must sell turnips for profit.\n");
	printf("You can buy turnips every Sunday from Daisy Mae.\n");
	printf("Turnip price may vary from 90-110 bells.\n");
	printf("You are only allowed to buy turnips in stacks of 10.\n");	
	printf("To earn a profit, turnips can be sold from Monday to Friday\n");
	printf("in Nook's Cranny. However, due to the ever-fluctuating\n");
	printf("turnip economy, turnip price may vary slightly by the day\n");
	printf("and perhaps even greatly by the week.\n");
}
/*This function prints information about the turnip expiration*/
void expiry()
{
	printf("\n-------------------------------------------------------\n\n");
	printf("Turnip expiration:\n\n");
	printf("Remember, turnips are perishable!\n");
	printf("They will expire after one week and can no longer be sold.\n");
	printf("Since every week starts on a Sunday and ends on Saturday,\n");
	printf("you will have until Saturday to sell all of your remaining\n");
	printf("turnips before they go bad.");
	printf("Be sure to sell all your turnips for the week!\n");
}
/*This function displays your bell balance
@param *nBells ------ is the amount of Bells the player has*/
void balance(int *nBells)
{
	printf("\nBells owned: %d\n", *nBells);
}
/*This function asks the user for the specific tutorial section they wish to access*/
void mainTutor()
{
	int nLearn = 0;
	while(nLearn != 9)
	{
		nLearn = 0;
		printf("\n-------------------------------------------------------\n");
		printf("\nWhat would you like to learn about?\n");
		printf("1 - About the game\n");
		printf("2 - Objective of the game\n");
		printf("3 - How to play\n");
		printf("4 - Turnip expiration\n");
		printf("9 - Exit tutorial\n");
		printf("...\n");
		printf("\n-------------------------------------------------------\n\n");
		
		scanf("%d", &nLearn);
		fflush(stdin);
		switch(nLearn)
		{
			case 1: about(); break;
			case 2: obj(); break;
			case 3: currency(); break;
			case 4: expiry(); break;
			case 9: printf("\n-------------------------------------------------------\n\n"); printf("Exiting tutorial...\n"); break;
			default: printf("\n-------------------------------------------------------\n\n"); printf("\nInvalid input, please try again.\n\n");  break;
		}
	}
}
/*This function asks if the user wishes to proceed with the tutorial*/
void tutor()
{
	char cTutor;
	while (cTutor != 'n' && cTutor != 'y' && cTutor != 'Y' && cTutor !='N')
	{	
		printf("Start tutorial? (Y/N)\nYour Choice:");
		scanf(" %c", &cTutor);
		fflush(stdin);
		switch(cTutor)
		{
			case 'Y' :
				mainTutor(); break;
			case 'y' :
				mainTutor(); break;
			case 'n' :
				printf("\n-------------------------------------------------------\n\n");
				printf("Skipping tutorial...\n"); break;
			case 'N' :
				printf("\n-------------------------------------------------------\n\n");
				printf("Skipping tutorial...\n"); break;
			default:
				printf("\n-------------------------------------------------------\n\n");
				printf("Invalid input, please try again.\n");
				printf("\n-------------------------------------------------------\n\n"); break;
		}
	}
}
/*This function asks the user if they want to play easy mode
@returns -------- 1 if player wants to play in easy mode 
				  0 if not*/
int easymode()
{
	char cMode;
	printf("\n-------------------------------------------------------\n\n");
	printf("Enable easy mode? (Y/N)\nYour Choice:");
	scanf(" %c", &cMode);
	fflush(stdin);
	
	while (cMode != 'n' && cMode != 'y' && cMode != 'Y' && cMode !='N')
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Invalid input, please try again.\n");
		printf("\n-------------------------------------------------------\n\n");
		printf("Enable easy mode? (Y/N)\n");
		scanf(" %c", &cMode);
		fflush(stdin);
	}
	if (cMode == 'N' || cMode == 'n')
		return 0;
	else 
		return 1;
}
/*This function identifies the trend based on the random number generated
and calculates a random sell price following the trend
@param nTurnipTrend --- number signifying which trend will occur
@param nTurnipBuy ----- cost of the turnips on the Sunday of that week
@return nSell --------- the resulting turnip price for that day*/
int trend(int nTurnipTrend, int nTurnipBuy)
{
	/*1 avg trend
	2 awesome trend
	3 bad trend*/
	int nSell = 0, nAvgTrnd;
	nAvgTrnd = nTurnipBuy * 1.05;
	nAvgTrnd = (int)nAvgTrnd;
	
	if (nTurnipTrend == 1)
		nSell = rand() % (nAvgTrnd - 80 + 1) + 80;
	else if (nTurnipTrend == 2)
		nSell = rand() % (nTurnipBuy * 3 - nTurnipBuy + 1) + nTurnipBuy;
	else 
		nSell = rand() % (nTurnipBuy - 20 + 1) + 20;
		
	return nSell;
}
/*This function prints the day and week
@param *nDay ----- day number (0-6)
@param *nWeek ---- week number (1-20)*/
void whatDay(int *nDay, int *nWeek)
{
	switch (*nDay)
	{
		case 0: printf("Sun"); break;
		case 1: printf("Mon"); break;
		case 2: printf("Tues"); break;
		case 3: printf("Wednes"); break;
		case 4: printf("Thurs"); break;
		case 5: printf("Fri"); break;
		case 6: printf("Satur"); break;
		default: printf("Error\n\n"); break;
	}
	printf("day, WEEK %d\n\n", *nWeek);	
}
/*This function asks the player if they are sure they want to skip the day
@param cSure ------- the player's choice to move on to the next day (Y/N)
@returns cSure*/
int nextDay(char cSure)
{
	printf("\n-------------------------------------------------------\n");
	printf("\nTommy: Are you sure you want to leave?\n");
	printf("Tommy: We will be closing soon! ...soon! (Y/N)\nYour Choice:");
	scanf(" %c", &cSure);
	fflush(stdin);
	
	while (cSure != 'n' && cSure != 'N' && cSure != 'y' && cSure != 'Y')
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Timmy: I didn't quite hear you can you say that again?\n");
		scanf(" %c", &cSure);
		fflush(stdin);
	}
	switch (cSure)
	{
		case 'y':
			printf("\n-------------------------------------------------------\n\n");
			printf("Proceeding to the next day...\n");
			break;
		case 'Y':
			printf("\n-------------------------------------------------------\n\n");
			printf("Proceeding to the next day...\n");
			break;
		case 'n':
			break;
		case 'N':
			break;
		default:
			printf("\n-------------------------------------------------------\n\n");
			printf("Error, resuming game.\n");
			break;
	}
	return cSure;
}
/*This function asks the player if they are sure they won't buy any turnips
@param cSure ------- player choice to move on to the next day (Y/Y)
@returns cSure*/
int daisySkip (char cSure)
{
	printf("\n-------------------------------------------------------\n\n");
	printf("Daisy Mae: Are ya sure ya want nothin'?\n");
	printf("Daisy Mae: These turnips are the best in the market! (Y/N)\nYour Choice:");
	scanf(" %c", &cSure);
	fflush(stdin);
	
	while (cSure != 'n' && cSure != 'N' && cSure != 'y' && cSure != 'Y')
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Daisy Mae: Sorry, I didn't quite hear that could ya say that again?\n");
		scanf(" %c", &cSure);
		fflush(stdin);
	}
	switch (cSure)
	{
		case 'y':
			printf("\n-------------------------------------------------------\n\n");
			printf("Proceeding to the next day...\n");
			break;
		case 'Y':
			printf("\n-------------------------------------------------------\n\n");
			printf("Proceeding to the next day...\n");
			break;
		case 'n':
			break;
		case 'N':
			break;
		default:
			printf("\n-------------------------------------------------------\n\n");
			printf("Error, resuming game.\n");
			break;
	}
	return cSure;	
}
/*This function exits or resumes the game
@param cSure ------ player's choice if they want to end the game or not
@param *nWeek ----- week number, used to end the game
@param *nDay ------ Day of the week, used to end the game
@returns cSure*/
int exitgame(char cSure, int *nWeek, int *nDay)
{
	printf("\n-------------------------------------------------------\n");
	printf("\nAre you sure? Progress will not be saved. (Y/N)\nYour choice:");
	scanf(" %c", &cSure);
	fflush(stdin);
	switch(cSure)
	{
		case 'y':
			printf("\n-------------------------------------------------------\n\n");
			printf("Ending game...\n");
			*nWeek = 21;
			*nDay = 7;
			break;
		case 'Y':
			printf("\n-------------------------------------------------------\n\n");
			printf("Ending game...\n");
			*nWeek = 21;
			*nDay = 7;
			break;
		case 'n':
			printf("\n-------------------------------------------------------\n\n");
			printf("Resuming game...\n");
			break;
		case 'N':
			printf("\n-------------------------------------------------------\n\n");
			printf("Resuming game...\n");
			break;
		default:
			printf("\n-------------------------------------------------------\n\n");
			printf("Invalid input, resuming game...\n");
			cSure = '*';
			break;
	}
	return cSure;
}
/*This function prints the goodbye flavor text for selling and corrects parameters affected by selling
@param *nBells -------- player owned bells
@param nTotal --------- total buying price of turnips
@param *nturnipsOwn --- number of player owned turnips
@param nStacks -------- number of stacks the player wishes to buy*/
void successBuy(int *nBells, int nTotal, int *nTurnipsOwn, int nStacks)
{
	if (nTotal == 0)
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Daisy Mae: This opportunity's quite hard to come by.\n");
		printf("Daisy Mae: See ya next Sunday then...\n");
	}
	else 
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Daisy Mae: Turnips, turnips! Watch 'em rise! Try to earn a nice surprise!\n");
		printf("Daisy Mae: Thanks very much for the buy, see ya next time!\n");
		*nBells -= nTotal;
		*nTurnipsOwn = nStacks * 10;
	}
	printf("\n-------------------------------------------------------\n\n");
	printf("Proceeding to the next day...\n");	
}
/*This function prints the goodbye flavor text for selling and corrects parameters affected by selling
@param *nBells --------player owned bells
@param nTotal -------- total selling price of turnips
@param *nTurnipsOwn -- number of player owned turnips
@param nStacks ------- number of stacks the player wishes to sell*/
void successSell(int *nBells, int nTotal, int *nTurnipsOwn, int nStacks)
{
	if (nTotal == 0)
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Tommy: This opportunity's quite hard to come by.\n");
		printf("Tommy: See you again! ...again!\n");
	}
	else
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Tommy: Thank you for your business!\n");
		printf("Timmy: Pleasure doing business! ...business!\n");
		*nBells += nTotal;
		*nTurnipsOwn = *nTurnipsOwn - (nStacks * 10);
	}
	printf("\n-------------------------------------------------------\n\n");
	printf("Proceeding to the next day...\n");
}
/*This function checks if player input is valid and asks for second input if not
@param cSure -------- player input yes/no
@param *nBells ------ player owned bells
@param nTotal ------- total price of turnips player wants to buy
@param *nTurnipsOwn-- number of turnips owned by the player
@param nStacks ------ number stacks the player wishes to buy
@returns cSure*/
int confirmBuy(char cSure, int *nBells, int nTotal, int *nTurnipsOwn, int nStacks)
{
	while (cSure != 'n' && cSure != 'N' && cSure != 'y' && cSure != 'Y')
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Invalid input, please try again.\n");
		scanf(" %c", &cSure);
		fflush(stdin);
	}
	switch(cSure)
	{
		case 'y':
			successBuy(nBells, nTotal, nTurnipsOwn, nStacks);
			break;
		case 'Y':
			successBuy(nBells, nTotal, nTurnipsOwn, nStacks);
			break;
		case 'n':
			break;
		case 'N':
			break;
	}	
	return cSure;
}
/*This function checks if player input is valid and asks for second input if not
@param cSure ------- player input yes/no
@param *nBells ----- player owned bells
@param nTotal ------ total price of turnips player wants to sell
@param *nTurnipsOwn- number of turnips owned by the player
@param nStacks ----- number stacks the player wishes to sell
@returns cSure*/
int confirmSell(char cSure, int *nBells, int nTotal, int *nTurnipsOwn, int nStacks)
{
	while (cSure != 'n' && cSure != 'N' && cSure != 'y' && cSure != 'Y')
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Invalid input, please try again.\nYour choice: ");
		scanf(" %c", &cSure);
		fflush(stdin);
	}	
	switch(cSure)
	{
		case 'n': 
			break;
		case 'N': 
			break;
		case 'y': 
			successSell(nBells, nTotal, nTurnipsOwn, nStacks);
			break;
		case 'Y': 
			successSell(nBells, nTotal, nTurnipsOwn, nStacks);
			break;
		default:
			break;
	}
	return cSure;
}
/*This function checks if the player input for turnips stacks to sell is valid and asks for another input if not
@param *nTurnipsOwn --- player owned turnips
@param nStacks -------- number of stacks the player wants to sell
@returns nStacks*/
int isValidSell(int *nTurnipsOwn, int nStacks)
{
	while (*nTurnipsOwn < nStacks * 10 || nStacks < 0)
	{
	printf("\n-------------------------------------------------------\n\n");
	printf("Tommy: I'm sorry, you don't have enough turnips for this.\n");
	printf("Tommy: How many do you want to sell? ...to sell?\nYour choice: ");
	scanf("%d", &nStacks);
	fflush(stdin);
	}
	return nStacks;
}
/*This function checks if the player input for turnip stacks to buy is valid and asks for another input if not
@param *nBells ----- player owned bells
@param nStacks ---- number of stacks the player wants to buy
@param nTurnipBuy - price of one turnip
@returns nTotal --- total price of turnips the player wants to buy*/
int isValidBuy(int *nBells, int *nStacks, int nTurnipBuy)
{
	int nTotal;
	nTotal = *nStacks * 10 * nTurnipBuy;
	while (nTotal > *nBells || nTotal < 0)
	{
		fflush(stdin);
		printf("\n-------------------------------------------------------\n\n");
		printf("Daisy Mae: Sorry, ya don't have enough bells for this.\n");	
		printf("Daisy Mae: So, how many stacks do ya want?\nYour choice:");
		scanf("%d", nStacks);
		fflush(stdin);
		nTotal = *nStacks * 10 * nTurnipBuy;
	}
	return nTotal;
}
/*This function handles the selling process for the day
@param *nBells ----------- amount of bells the player owns
@param *nTurnipsOwn ------ amount of turnips owned by the player
@param nSell ------------- selling price of one turnip
@returns cSure ----------- player decision to move on to the next day via Y/N */
int sellTurnips(int *nBells, int *nTurnipsOwn, int nSell)
{
	int nStacks, nTotal;
	char cSure;
	printf("\n-------------------------------------------------------\n\n");
	printf("Tommy: How many do you want to sell? ... to sell?\nYour choice: ");
	scanf("%d", &nStacks);
	fflush(stdin);
	nStacks = isValidSell(nTurnipsOwn, nStacks);	
	nTotal = nStacks * 10 * nSell;
	if (nTotal == 0)
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Timmy: That looks like nothing! ...nothing!\n");
		printf("Timmy: Are you sure you want to skip for today? (Y/N)\nYour choice: ");
	}
	else 
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Timmy: I can buy these %d turnips from you for a total of %d bells. Sound good? (Y/N)\nYour choice: ", nStacks *10, nTotal);
	}
	scanf(" %c", &cSure);
	fflush(stdin);
	
	cSure = confirmSell(cSure, nBells, nTotal, nTurnipsOwn, nStacks);
	
	return cSure;
}
/*This function handles the selling process for the day
@param *nBells ----------- amount of bells the player owns
@param *nTurnipsOwn ------ amount of turnips owned by the player
@param nTurnipBuy -------- buying price of one turnip
@param nSell ------------- selling price of one turnip
@returns cSure ----------- player decision to move on to the next day via Y/N */
int buyTurnips(int *nBells, int *nTurnipsOwn, int nTurnipBuy)
{
	int nStacks, nTotal;
	char cSure;
	printf("\n-------------------------------------------------------\n\n");
	printf("Daisy Mae: Great! How many should I put you down for?\n");
	printf("Daisy Mae: Again, They're %d bells each, but we sell in bundles of 10.\n", nTurnipBuy);
	printf("Your choice: ");
	scanf("%d", &nStacks);
	fflush(stdin);
	nTotal = isValidBuy(nBells, &nStacks, nTurnipBuy);
	if (nTotal == 0)
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Daisy Mae: That's a whole lotta nothin' ain't it?\n");
		printf("Daisy Mae: Are ya sure ya want nothin'? (Y/N)\nYour choice:");
	}
	else
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Daisy Mae: Alright, so %d turnips comes to... %d Bells. Does that sound OK to you? (Y/N)\nYour choice:", nStacks*10, nTotal);
	}
	scanf(" %c", &cSure);
	fflush(stdin);			
	cSure = confirmBuy(cSure, nBells, nTotal, nTurnipsOwn, nStacks);
	return cSure;
}
/*This function checks if player input for buy/sell, cancel, exit game is valid or not
Asks for new input if invalid
@param nAction ----- player input for action
@returns nAction*/
int isValidAction(int nAction)
{
	while (nAction != 1 && nAction != 2 && nAction != 9)
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Invalid input, please try again.\n");
		printf("\n-------------------------------------------------------\n\n");
		scanf("%d", &nAction);
		fflush(stdin);
	}
	return nAction;
}
/*This function prints the flavor text for the beginning of Sunday
@param *nDay -------- day number
@param *nWeek ------- week number
@param nTurnipBuy --- buying price for each turnip
@param *nBells ------ number of player owned bells*/
void SundayHello(int *nDay, int *nWeek, int nTurnipBuy, int *nBells)
{
	int nPPower;
	nPPower = *nBells / nTurnipBuy / 10;
	printf("\n-------------------------------------------------------\n\n");
	whatDay(nDay, nWeek);
	printf("Daisy Mae: I've got turnips a-plenty fresh from Sow Joan's Stalk Market.\n");
	printf("Daisy Mae: Wanna buy 'em for %d Bells each?\n", nTurnipBuy);
	balance(nBells);
	printf("*You can buy %d stacks of turnips*\n", nPPower);
	printf("\n-------------------------------------------------------\n\n");
	printf("What will you do?\n");
	printf("1 - I'll buy some.\n");
	printf("2 - I don't need any. (Skips to next week)\n");
	printf("9 - Exit game (Progress will not be saved!)\n");	
}
/*This function prints the flavor text for the beginning of a weekday
@param *nDay --------- day number
@param *nWeek -------- week number
@param nSell --------- selling price of a turnip
@param *nTurnipsOwn--- number of turnips owned
@param nTurnipBuy ---- the price the player payed for each turnip
@param *nBells ------- player owned bells*/
void WeekdayHello(int *nDay, int *nWeek, int nSell, int *nTurnipsOwn, int nTurnipBuy, int *nBells)
{
	printf("\n-------------------------------------------------------\n\n");
	whatDay(nDay, nWeek);
	printf("Timmy: Welcome! ...welcome! What do you need today?\n");
	printf("Timmy: The current price for turnips is %d bells per turnip!\n\n", nSell);
	printf("Turnips owned: %d turnips\n", *nTurnipsOwn);
	printf("Turnips bought for %d bells", nTurnipBuy);
	balance(nBells);
	printf("\nWhat will you do?\n");
	printf("1 - I want to sell!\n");
	printf("2 - See you later. (Skips to next day)\n");
	printf("9 - Exit game (Progress will not be saved!)\n");
}
/*This function asks the player for their action for the day. This function is called
on weekdays
@param *nBells ------ pointer for total number of bells owned by the player
@param nSell -------- selling price of the turnips for the day
@param *nWeek ------- week number
@param *nTurnipsOwn - pointer for the amount of player owned turnips
@param *nDay -------- day number (0 - sun, 6- sat)
@param nTurnipBuy --- buying price for each turnip*/
void playerchoice(int *nBells, int nSell, int * nWeek, int * nTurnipsOwn, int * nDay, int nTurnipBuy)
{
	int nAction;
	char cSure = '*';
	
	if (*nTurnipsOwn >= 10)
	{	
		while (cSure != 'Y' && cSure != 'y')
		{
			nAction = 0;
			WeekdayHello(nDay, nWeek, nSell, nTurnipsOwn, nTurnipBuy, nBells);
			printf("Your choice: ");
			scanf("%d", &nAction);
			fflush(stdin);
			
			nAction = isValidAction(nAction);
			
			switch(nAction)
			{
				case 1:
					cSure = sellTurnips(nBells, nTurnipsOwn, nSell);
					break;
				case 2:
					cSure = nextDay(cSure);
					break;
				case 9:
					cSure = exitgame(cSure, nWeek, nDay);
					break;
		 		default:
		 			printf("Error, resuming game.");
					break;
			}
		}
	}
	else 
	{
		*nDay = 7;
		printf("\nUnfortunately, you have run out of turnips to sell for the week.\n");
		printf("Proceeding to the next week...\n");
	}
}
/*This function asks the player for their action for the day. This function is called
on Sundays
@param *nBells ------- pointer for total number of bells owned by the player
@param nTurnipBuy --- buying price for one turnip
@param *nTurnipsOwn - amount of player owned turnips
@param *nWeek ------- Week counter
@param *nDay -------- Day number (0 - Sunday, 6- Saturday)*/
void Sunday(int *nBells, int nTurnipBuy, int * nTurnipsOwn, int * nWeek, int * nDay)
{
	int nAction;
	char cSure = '*';
	while (cSure != 'y' && cSure != 'Y')
	{
		nAction = 0;
		SundayHello(nDay, nWeek, nTurnipBuy, nBells);
	
		printf("Your choice: ");
		scanf("%d", &nAction);
		fflush(stdin);
		
		nAction = isValidAction(nAction); 
		
		switch(nAction)
		{
			case 1:
				cSure = buyTurnips(nBells, nTurnipsOwn, nTurnipBuy);
				break;
			case 2:
				cSure = daisySkip(cSure);
				break;
	 		case 9:
	 			cSure = exitgame(cSure, nWeek, nDay);
			 default:
				break;
		}
	}
}
/*This function prints the day and week number and finalizes player owned
bells for a day
@param nBells -------- amount of Bells the player has
@param *nWeek -------- week number
@param nTurnipTrend -- number signifying which trend will occur for the week
@param nTurnipBuy ---- price of the turnips on the Sunday of that week
@param *nTurnipsOwn -- number of turnips owned by the player
@param *nDay --------- day number ( 0- Sunday, 6 - Saturday)*/
void days(int *nBells, int *nWeek, int nTurnipTrend, int nTurnipBuy, int *nTurnipsOwn, int *nDay)
{
	int nSell;  
	if (*nDay == 0)
		Sunday(nBells, nTurnipBuy, nTurnipsOwn, nWeek, nDay);
	else 
	{
		nSell = trend(nTurnipTrend, nTurnipBuy);
		playerchoice(nBells, nSell, nWeek, nTurnipsOwn, nDay, nTurnipBuy);
	}
}
/*This function checks if the player has had a streak of bad/average trends and enables a pity that turns the trend to awesome
if player has had said streak
@param *nPity --------- pity counter
@param nTrend --------- Sell price trend for the week (1 - avg, 2- awesome, 3 - bad)
@returns -------------- nTrend if pity hasn't been reached
						2 if pity has been reached*/
int checkpity (int *nPity, int nTrend)
{
	/*Pity is reset when player gets an awesome trend*/
	
	/*1 avg trend
	2 awesome trend
	3 bad trend*/
	if (nTrend == 3)
		*nPity += 2;
	else if (nTrend == 1)
		*nPity += 1;
	else 
		*nPity = 0;
	
	/*To activate pity:
	2 bad trends in a row or
	5 avg trends in a row or
	1 bad trend + 2 avg trends in a row or
	1 bad trend then 1 avg trend then 1 bad trend*/	
	if (*nPity >= 4)
	{
		*nPity = 0;
		return 2;
	}
	else
	{
		return nTrend;
	}
}
/*This function prints the end game flavor text
@param nBells ------------- number of bells the player ended up with
@param nTurnipsSpoiled ---- number of unsold/spoiled turnips*/
void gameend(int nBells, int nTurnipsSpoiled)
{
	if (nBells >= 1000000)
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("Congratulations! You have reached the end.\n");
		printf("Through your perserverance throughout the 20 weeks,\n");
		printf("you have earned a total of %d bells!\n", nBells);
		printf("You are now a certified millionaire!\n");
		printf("\n-------------------------------------------------------\n\n");
	}
	else 
	{
		printf("\n-------------------------------------------------------\n\n");
		printf("\nYou have struggled these last 20 weeks...\n");
		printf("It has been a rough ride...\n");
		if (nTurnipsSpoiled != 0)
		{
			printf("You've couldn't sell %d turnips and they ended up spoiled.\n", nTurnipsSpoiled);
		}
		printf("Maybe it wasn't meant to be...\n");
		printf("In the end you were left with %d bells\n", nBells);
		printf("You couldn't become a millionaire like you were told you could...\n");
		printf("Maybe next time...");
		printf("...\n");
		printf("\nGAME OVER\n");
		printf("\n-------------------------------------------------------\n\n");
	}
}
int main()
{
	int nBells = 5000, nTurnipBuy, i, nTurnipTrend, nTurnipsOwn = 0, nTurnipsSpoiled = 0, nDay, nPity = 0;
	
	srand(time(0));
	printf("-------------------------------------------------------\n");
	printf("Welcome to Stalk Market Millionaire!\n\n");
	printf("\nCoded by Orrin Uy\n");
	printf("Based on the game 'Animal Crossing New Horizons'\n");
	printf("-------------------------------------------------------\n\n");


	/*start tutorial*/
	tutor();
	/*check if player wants easy mode*/
	if(easymode())
	{
		/*Week loop*/
		for (i = 1; i < 21; i++)
		{
			nTurnipBuy = rand() % (110 - 90 + 1) + 90;
			if (nTurnipsOwn >= 1 && i >= 2)
			{
				printf("\nYour %d turnips have spoiled and can no longer be sold.\n", nTurnipsOwn); 
				
				nTurnipsSpoiled +=nTurnipsOwn;
				
				printf("You have a total of %d spoiled turnips.\n", nTurnipsSpoiled);
			}
			nTurnipsOwn = 0;
			nTurnipTrend = rand() % (3 - 1 + 1) + 1;
			
			/*The next line enables easy mode*/	
			nTurnipTrend = checkpity(&nPity, nTurnipTrend);
			
			/*Day by day loop*/
			for (nDay = 0; nDay <= 6; nDay++)
			{
				days(&nBells, &i, nTurnipTrend, nTurnipBuy, &nTurnipsOwn, &nDay);
			}
			if (nBells < nTurnipBuy * 10)
			{
				i = 21;
			}
		}
		nTurnipsSpoiled += nTurnipsOwn;
	}
	else
	{
		for (i = 1; i < 21; i++)
		{
			nTurnipBuy = rand() % (110 - 90 + 1) + 90;
			if (nTurnipsOwn >= 1 && i >= 2)
			{
				printf("\nYour %d turnips have spoiled and can no longer be sold.\n", nTurnipsOwn); 
			
				nTurnipsSpoiled +=nTurnipsOwn;
				
				printf("You have a total of %d spoiled turnips.\n", nTurnipsSpoiled);
			}
			nTurnipsOwn = 0;
			nTurnipTrend = rand() % (3 - 1 + 1) + 1;	
				
			for (nDay = 0; nDay <= 6; nDay++)
			{
				days(&nBells, &i, nTurnipTrend, nTurnipBuy, &nTurnipsOwn, &nDay);
			}
			if (nBells < nTurnipBuy * 10)
			{
				i = 21;
			}
		}
		nTurnipsSpoiled += nTurnipsOwn;
		
	}
	gameend(nBells, nTurnipsSpoiled);
	printf("Press Enter to exit the game.");
	getchar();
	return 0;
}
