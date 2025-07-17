print("start capital = 10000")

start_capital = 10000
#for goods bought = 3500
start_capital -= 3500
print(f"after buying goods worth 3500, the new cpaital is {start_capital}")

#sold some items and made profit
item_sold = 2800
start_capital += 2800
print(f"after selling some goods and made a profit of 2800, the now capital is {start_capital}")

#for electricity
electricity_bill = 1200
start_capital -= 1200
print(f"after paying for electricity, the new capital is {start_capital}")

#increment by 20%
percent = 20/100
percent *= start_capital
start_capital += percent
print(f"after increments of 20%, the new capital is {start_capital}")

#bought new goods
goods_bought =1/2
goods_bought *= start_capital
start_capital -= goods_bought
print(f" after buying goods for half f the capital, the new capital is {start_capital}")

#lost one fifth of my current capital due to spoilage
spoilage = 1/5
spoilage *= start_capital
start_capital -= spoilage
print(f"lost 1/5 of my curreent capital due to spoilage, new captial is {start_capital}")

#share total capital into two
into_two_equal_part = 1/2
start_capital //= 2
print(f"start capital after sharing into two part is {start_capital}")

#after removing all 200 note
start_capital %= 200
print(f"start capital after taking off 200 note {start_capital}")
