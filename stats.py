import pandas as pd
import matplotlib.pyplot as plt
from math import fabs

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

# def check_tp_and_sl(tp=13, sl=6):
#     result = 0
#     result_list = []
#     for profit, loss in zip(profits[:-1], losses[:-1]):
#
#         if profit < tp or loss <= -sl:
#             result += -sl
#         else:
#             result += tp
#         result_list.append(result)
#     return result_list
#
# def best_tp_and_sl(p,l):
#     for tp in range(p):
#         for sl in range(l):
#             print (f'tp is {tp}, sl is {sl}, result is {check_tp_and_sl(tp, sl)[-1]}')
#         print('\n')

# best_tp_and_sl(10,10)

#print(check_tp_and_sl(20,2))

def check_tp_and_sl(tp, sl):
    result = 0
    sle = 0
    tpki = 0
    rdd = 0
    max_result = 0
    for profit, loss in zip(profits, losses):

        if loss <= -sl:
            result -= sl
            sle += 1

        elif profit >= tp:
            result += tp
            tpki += 1

        if result > max_result:
            max_result = result
        dd = max_result - result

        if rdd < dd:
            rdd = dd
    return result, sle, tpki, rdd

def check_rev_tp_and_sl(tp, sl):
    result = 0
    sle = 0
    tpki = 0
    max_result = 0
    rdd = 0
    for profit, loss in zip(profits, losses):
        if profit >= tp:
            result -= tp
            sle += 1

        elif loss <= -sl:
            result += sl
            tpki +=1

        if result > max_result:
            max_result = result
        dd = max_result - result

        if rdd < dd:
            rdd = dd
    return result, sle, tpki, rdd

def best_tp_and_sl(p, l):
    max_result = float('-inf')
    best_tp, best_sl = 0, 0
    for tp in range(1, p+1):
        for sl in range(1, l+1):
            result = check_tp_and_sl(tp, sl)
            if result > max_result:
                max_result = result
                best_tp, best_sl = tp, sl
    return f'tp {best_tp}$, sl  {best_sl}$, res {max_result}$'

def best_tp_and_sl_rev(p, l):
    max_result = float('-inf')
    best_tp, best_sl = 0, 0
    for tp in range(1, p+1):
        for sl in range(1, l+1):
            result = check_rev_tp_and_sl(tp, sl)
            if result > max_result:
                max_result = result
                best_tp, best_sl = tp, sl
    return f'sl {best_tp}$, tp  {best_sl}$, res {max_result}$'

# print(best_tp_and_sl(50, 12))
# print(best_tp_and_sl_rev(35,12))

print(check_tp_and_sl(32,2))
print(check_rev_tp_and_sl(33,11))