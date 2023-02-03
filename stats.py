import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('jan.csv')

profits = df['Max Open Profit (C)']
losses = df['Max Open Loss (C)']
real_profit_or_loss = df['Profit/Loss (C)']
real_profit_or_loss2 = [int(x) for x in df['Profit/Loss (C)']]


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




#print(sum(loss[:-1]) + sum(profit[:-1]))

def total_result(stats):
    result = 0
    for tick in stats[:-1]:
        result += tick
    return result

#print(total_result(losses))

def sum_total_result_list():
    result_list = []
    res = 0
    for profit, loss in zip (profits, losses):
        res += profit + loss
        result_list.append(res)
    return  result_list


#print(sum_total_result_list())
def chart():
    y = sum_total_result_list()
    x = [x for x in range(len(y))]
    plt.plot(x, y)
    plt.show()

def check_sl(sl=6):
    result = 0
    result_list = []
    for profit, loss in zip(real_profit_or_loss2[:-1], losses[:-1]):
        if loss <= -sl:
            result += -sl
        else:
            result += profit
        result_list.append(result)
    return  result

def best_sl(r=20):
    for sl in range(r):
        print(sl, check_sl(sl))

def check_tp(tp=10):
    result = 0
    result_list = []
    for profit, loss in zip(profits[:-1], losses[:-1]):
        if profit >= tp:
            result += tp
        else:
            result += loss
    return result

def best_tp(r=30):
    for tp in range(r):
        print(tp, check_tp(tp))

def check_tp_and_sl(tp=13, sl=6):
    result = 0
    result_list = []
    for profit, loss in zip(profits[:-1], losses[:-1]):
        if profit >= tp and loss <= -sl:
            result += tp
        else:
            result += -sl
        print(profit, loss, tp, -sl, result)

def best_tp_and_sl(p,l):
    for tp in range(p):
        for sl in range(l):
            print (f'tp is {tp}, sl is {sl}, result is {check_tp_and_sl(tp, sl)}')
        print('\n')

check_tp_and_sl(15,20)