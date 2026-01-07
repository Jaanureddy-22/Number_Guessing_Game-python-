import random


print(".........WELCOME TO NUMBER GUESSING GAME🎮🔢......")


def number_guess(randomnum,number):
    if randomnum == number:
        print(randomnum," || ",number,".......😀🎊")
        print("YOU WON THE GAME....🏆")
        print("Congratulations..........'🎉🎊")
        print("...🎊🎊🎉🎉🥳🥳")
    else:
        print("YOU LOST THE GAME....!😕")
        print("the number was: ",randomnum)
        


print("Hint: The number lies in between 1-10 ") 



def display():
    randomnum=random.randint(1,10)
    number=(input("ENTER YOUR GUESSED NUMBER: "))
    if not number.isdigit():
        print("Please,Enter a valid number!")
        return 
    number=int(number)    
    number_guess(randomnum,number)
    

display()
playAgain='Y'
games_played=1
while playAgain =='Y':
    playAgain=input("Do you wanna play again(Y/N)..").upper()
    if playAgain == 'Y':
        display()
        games_played += 1
print("No.of games you played was: ",games_played)
print("THANK YOU.....😊")





