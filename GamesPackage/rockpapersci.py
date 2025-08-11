#Rock paper scissor
import random 
import enum
import inquirer
from rich import print

class Options(enum.Enum):
	ROCK=1
	PAPER=2
	SCISSOR = 3
	def compare(self,other):
		if self.value == other.value:
			return 0
		# Rock:1 beats Scissor:3, Scissor:3 beats Paper:2, Paper:2 beats Rock:1
		elif other.value == (self.value+1)%3:
			return -1
		else:
			return 1
	def __str__(self):
		return self.name.capitalize()
		
options = [Options.ROCK,Options.PAPER,Options.SCISSOR]
def play():
	listOut=inquirer.list_input("Choose your option",choices=options,default=Options.ROCK)
	user_choice = options[listOut-1]
	computer = random.choice(options)
	print(f"Computer chose {computer}\nYou chose {user_choice}")
	res = user_choice.compare(computer)
	if res == 0:
		print("[bold yellow]It's a tie![/bold yellow]")
	elif res > 0:
		print("[bold green]You win![/bold green]")
	else:
		print("[bold red]You lose![/bold red]")
