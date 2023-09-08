# %%
import math

import numpy as np

alpha = math.pi / 120
theta = math.pi * 2 / 3
n_mile = 1852
D_max = 110 + 2 * n_mile * math.tan(alpha)


# %%
def depth_calculate(distance):  # distance 表示当前位置到最西边的距离
    return D_max - distance * math.tan(alpha)


# %%
d0 = D_max * math.tan(math.pi / 3)

# %%
import sympy as sp


# def width_calculate(distance):
#     return (2 * depth_calculate(distance) * math.cos(alpha) * math.sin(theta)) / (math.cos(theta) + math.cos(2 * alpha))
#
#
# def coverage_calculate(difference, last_distance):
#     # different 表示两条侧线之间的距离
#     var = (difference * math.cos(theta / 2)) / (math.cos(theta / 2 + alpha))
#     cur_distance = difference + last_distance
#     return 1 - var / width_calculate(cur_distance)


# %%
def difference_inequality(last_distance):
    x = sp.symbols('x')
    var = 1 - ((x * math.cos(theta / 2)) / (math.cos(theta / 2 + alpha))) / (
            (2 * (D_max - (last_distance + x) * math.tan(alpha)) * math.cos(alpha) * math.sin(theta)) / (
            math.cos(theta) + math.cos(2 * alpha)))
    formula=sp.Eq(var,0.1)
    solution=sp.solve(formula,x)
    return solution

# %%
difference_list=[]
cur=d0
while sum(difference_list)<=7408:
    s=difference_inequality(cur)
    difference_list.append(s[0])
    cur+=s[0]
    depth = depth_calculate(sum(difference_list))
    x = (depth * math.sin(theta / 2)) / math.cos(theta / 2 - alpha)
    total = x + sum(difference_list)
    if total>=7408:
        break

# %%
difference_list.pop()
depth1 = depth_calculate(sum(difference_list))
x1 = (depth1 * math.sin(theta / 2)) / math.cos(theta / 2 - alpha)
total1 = x1 + sum(difference_list)

# %%
import pandas as pd
result=pd.DataFrame(difference_list)
result.to_excel('q3_result1.xlsx',index=False)

# %%
import matplotlib.pyplot as plt
# difference_list.reverse()
pos=[]
for i in range(len(difference_list)):
    pos.append(2*1852)
plt.bar(difference_list,pos)
plt.title('Survey_path')
plt.xlabel('Position_from_E_to_W')
plt.ylabel('From_S_to_N(M)')
plt.show()

