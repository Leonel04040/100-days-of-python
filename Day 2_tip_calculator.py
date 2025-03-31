#math operations using f-strings, round, int, float
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip1=tip/100
bill1=tip1*bill+bill
result=(bill1/people)
print(f"Each person will pay $ {round(result,2)}")
