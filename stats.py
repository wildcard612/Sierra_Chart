import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('jan.csv')

profits = df['Max Open Profit (C)']
losses = df['Max Open Loss (C)']


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

#loss2 = loss.drop(loss.index[-1])


#print(sum(loss[:-1]) + sum(profit[:-1]))

def total_result(stats):
    result = 0
    for tick in stats[:-1]:
        result += tick
    return result

print(total_result(losses))
def total_result_list():
    result_list = []
    for profit, loss in profits, losses:
        x = profit + loss

print(total_result_list())