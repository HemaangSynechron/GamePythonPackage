from rich import print
import inquirer,os
from tabulate import tabulate
from time import sleep
from enum import Enum
import random

secret = ""
def generate_secret():
	global secret
	while len(secret) != 4:
		newInt = str(random.randint(0, 9))
		if newInt not in secret:
			secret += newInt
	print(f"[blue]Secret number is: {secret}[/blue]") 


def play():
	global secret
	if len(secret) == 0:
		generate_secret()
	noCows = 0
	noBulls = 0
	while noBulls<4:
		noCows = 0
		noBulls = 0
		guess = input("Enter a 4 digit number: ")
		
		if len(guess) != 4 or not guess.isdigit():
			print("[red]Please enter a valid 4 digit number.[/red]")
			continue
		csecret:list[str|None] = list(secret)
		for i in range(4):
			if guess[i] == csecret[i]:
				noBulls += 1
				csecret[i] = None
		for i in range(4):
			if guess[i] in csecret:
				noCows += 1

		print(f"[green]Cows:[/green][yellow] {noCows}[/yellow], [green]Bulls:[/green][yellow] {noBulls}[/yellow]")
	print(f"[green]Congratulations! You guessed the number {secret}[/green]")