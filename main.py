a = "Scissor"
c = "Rock"
b = "Paper"


r = input("choose weapon 1: ")
r1 = input("choose weapon 2: ")

if r == "a" and r1 == "b" or r == "b" and r1 == "a":
    print("won rock")
elif r == "c" and r1 == "b" or r == "b" and r1 == "c":
    print("won paper")
elif r == "a" and r1 == "c" or r == "c" and r1 == "a":
    print("won scissor")
