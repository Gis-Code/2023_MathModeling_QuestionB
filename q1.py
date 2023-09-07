# %%
import math
import pandas as pd

alpha = math.pi / 120
theta = math.pi * 2 / 3
distance = [-800, -600, -400, -200, 0, 200, 400, 600, 800]
depth_list = []


# %%
def width_calculate(d):
    depth = 70 - (d * math.tan(alpha))
    depth_list.append(depth)
    width = depth * math.sin(theta / 2) * ((1 / math.cos(theta / 2 + alpha)) + (1 / math.cos(theta / 2 - alpha)))
    return width


# %%
result_width = []
for d_data in distance:
    w = width_calculate(d_data)
    result_width.append(w)

print("Width data:", result_width)


# %%
def duplication_calculate():
    var = (200 * math.cos(theta / 2)) / (math.cos(theta / 2 - alpha))
    return var


def coverage_calculate(var, w):
    return 1 - var / w


# %%
coverage_list = []
for d_data in distance:
    cov = coverage_calculate(duplication_calculate(), width_calculate(d_data))
    coverage_list.append(cov)

print("Coverage data:", coverage_list)

# %%
depth_list = depth_list[:9]

# %%
result = [depth_list, result_width, coverage_list]
result_data = pd.DataFrame(result)
result_data.to_excel('q1_result.xlsx', index=False)
