# %%
import math
import pandas as pd

alpha = math.pi / 120
theta = math.pi * 2 / 3
beta_data = [0.0, math.pi / 4, math.pi / 2, math.pi * 3 / 4, math.pi, math.pi * 5 / 4, math.pi * 3 / 2, math.pi * 7 / 4]
n_mile = 1852
distance_data = [0.0, 0.3 * n_mile, 0.6 * n_mile, 0.9 * n_mile, 1.2 * n_mile, 1.5 * n_mile, 1.8 * n_mile, 2.1 * n_mile]

# %%
delta_data = []
depth_data = []
for beta in beta_data:
    tan_delta = math.tan(alpha) * abs(math.sin(beta))
    # print("tan value: ",tan_delta)
    # print("angle: ",math.atan(tan_delta))
    delta_data.append(math.atan(tan_delta))

    list = []
    for distance in distance_data:
        depth = 120 + distance * math.cos(beta) * math.tan(alpha)
        list.append(depth)
    depth_data.append(list)

# %%
width_data = []
index = 0
for beta in beta_data:
    index = beta_data.index(beta)
    d_list = depth_data[index]
    w_list = []
    for depth in d_list:
        width = (2 * depth * math.cos(delta_data[index]) * math.sin(theta)) / (
                    math.cos(theta) + math.cos(2 * delta_data[index]))
        w_list.append(width)
    width_data.append(w_list)

# %%
result_data = pd.DataFrame(width_data)
result_data.to_excel('q2_result.xlsx', index=False)
