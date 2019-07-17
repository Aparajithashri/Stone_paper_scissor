import random
up=0
sp=0
t="y"
print("Enter the winning point:")
n=input()
while t!="n":
	while sp!=n and up!=n:
		print("\n\t\tSTONE...PAPER...SCISSOR GAME\n1.STONE\n2.PAPER\n3.SCISSOR\nCHOOSE YOUR OPTION\n")
		user=input()
		system=random.choice(['stone','paper','scissor'])
		if user=="1":
			print("You choose stone")
		elif user=="2":
			print("You choose paper")
		elif user=="3":
			print("You choose scissor")
		else:
                    print("Enter a valid number:")
                    user=input()
		print("System choose ",system)
		if (user=="1" and system=="paper") or (user=="2" and system=="scissor") or (user=="3" and system=="stone"):
			sp+=1
		elif (user=="1" and system=="scissor") or (user=="2" and system=="stone") or (user=="3" and system=="paper"):
			up+=1
		print("\nYour points:",up)
		print("\nSystem points:",sp)
		if sp==n:
			print("\nSystem WINS!\n")
		elif up==n:
			print("\nYou WINS!\n")
		elif sp==n and up==n:
			print("\nMatch DRAW!\n")
	sp=0
	up=0
	print("\nWant to try another game? click y or n.")
	t=input()
