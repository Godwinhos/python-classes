print("weekly allowance = 2000\n")

weekly_allowance = 2000

#money for books
money_spent_on_books = 400
weekly_allowance -= 400
print(f"money spent on books is 400, and now my weekly allwance is {weekly_allowance}")

#money recovered from my room
money_found = 100
weekly_allowance += 100
print(f"money recover in my room = 100, now the weekly allowance is {weekly_allowance}")

#money for snacks
money_for_snacks = 250
weekly_allowance -= 250
print(f"money for snacks = 250 and the weekly allowance is {weekly_allowance}")

#gave 25% to my siblings
percent = 25/100
percent *= weekly_allowance
weekly_allowance -= percent
print(f" gave 25% to my siblings, the weekly_allowance is {weekly_allowance}")

# one third of whhat is left for data
one_third = 1/3
one_third *= weekly_allowance
weekly_allowance -= one_third
print(f" one third for data and the weekly allowance is {weekly_allowance}")

#split the remaining into tithe and savings
tithe_and_savings =1/2
tithe_and_savings *= weekly_allowance
weekly_allowance -= tithe_and_savings
print(f"tithe and savins takes 1/2 of weekly allwance, the weekly allowance is {weekly_allowance}")

#calculate what remains now
weekly_allowance %= 100
print(f"what is left as miscellanous in my weekly allwance is,{weekly_allowance}")
