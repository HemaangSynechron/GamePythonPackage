from rich import print
import random

def play(secret_num:int = random.randint(1, 100),low:int = 1, high:int = 100,max_attempts:int = 7):
	cn = -1
	attempt = max_attempts
	while cn!=secret_num and attempt>0:
		print(f"[bold]Attempt:{max_attempts-attempt+1}/{max_attempts}\nEnter your guess (1-100):[/bold]",end="")
		cn = int(input())
		if cn < secret_num:
			print("[bold yellow]Too low![/bold yellow]")
		elif cn > secret_num:
			print("[bold red]Too high![/bold red]")
		else:
			print("[bold green]Congratulations! You guessed it![/bold green]")
		attempt -= 1
	if cn != secret_num:
		print(f"[bold red]You ran out of attempts! The secret number was {secret_num}.[/bold red]")