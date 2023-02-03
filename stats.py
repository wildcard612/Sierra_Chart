import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('jan.csv')

profit = df['Max Open Profit (C)']
loss = df['Max Open Loss (C)']

# y = 0
# for x in profit:
#     if x<=5:
#         y+=1
# print(y)
# print(len(profit))

def how_many_above(ticks, stats):
    result = 0
    for tick in stats:
        if tick > ticks:
            result += 1
    return result
def how_many_below(ticks, stats):
    result = 0
    for tick in stats:
        if tick < ticks:
            result += 1
    return result

# print(how_many_above(6, profit))
# print(how_many_below(6, profit))
#
# print(how_many_above(-6, loss))
# print(how_many_below(-6, loss))

def max_open_profit():
    y = 0
    for x in loss:
        y += x
        print(y)

print(max_open_profit())