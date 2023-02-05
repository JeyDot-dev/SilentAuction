from art import gavel_art, auction_art
from os import system, name

def clear() :
	if name == "nt":
		system("cls")
	else :
		system("clear")

auctionners = {}

print(f"{auction_art}{gavel_art}\nWelcome to the silent auction.\n")
input("You may press any key to continue...")
clear()
add = 1
while add :
	name = input("Please enter your name : ")
	money = int(input("How much are you willing to bid ? : "))
	clear()
	add = int(input('''Thank you for your participation.
Is there anyone else willing to participate ? (1.Yes, 2.No) : '''))
	if add == 2 :
		add = 0
	clear()
	auctionners[name] = money

winner = ''
highest = 0

for n in auctionners :
	if highest < auctionners[n] :
		winner = n
		highest = auctionners[n]

print(f"Congratulations, the winner of this auction is {winner} with a bid of {highest}$ !")
