import math
def chocolate_bar_affordability_caculator (total_money, bar_price): # set a function with two paramaters
    number=math.floor(int(total_money)/int(bar_price))  # math.floor to achieve round number
    change=int(total_money) - (int(number) * int(bar_price)) # round number * price to achieve the change
    return number, change
# example
total_money = input('please input the total money')
bar_price = input('please input the price') 
number,change = chocolate_bar_affordability_caculator (total_money, bar_price)
# output with print text
text= 'you can buy {} bars of chocolate'
text2='your change will be {}'
number = str(number)
change = str(change)
print(text.format(number))
print(text2.format(change))