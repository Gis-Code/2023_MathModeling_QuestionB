# %%
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt

depth_dataFrame = pd.read_excel('appendix.xlsx')
depth_data = depth_dataFrame.values

# %%
# depth_data=py.delete(depth_data,0,axis=0)
depth_data = py.delete(depth_data, 0, axis=1)
depth_data[0, 0] = 0.0

# %%
x_coordinate = depth_data[0, :]
y_coordinate = depth_data[:, 0]

# %%
x_cor = x_coordinate.tolist()
y_cor = y_coordinate.tolist()

# %%
del x_cor[0]
del y_cor[0]

# %%
presicion = 2
x = [round(num, presicion) for num in x_cor]
y = [round(num, presicion) for num in y_cor]

# %%
X,Y=py.meshgrid(x,y)

# %%
depth_data = py.delete(depth_data, 0, axis=0)
depth_data = py.delete(depth_data, 0, axis=1)
# %%
negated=[[-n for n in row]for row in depth_data]

# %%
plt.figure(figsize=(10,7.5))
contours=plt.contour(X,Y,negated,cmap='Blues_r')
plt.clabel(contours,inline=True,fontsize=8,colors='black')
plt.xlabel('From_W_to_E(NM)')
plt.ylabel('From_S_to_N(NM)')
plt.title('Ocean_floor(M)')
plt.contourf(x,y,negated,cmap='Blues_r',alpha=0.75)
plt.colorbar(shrink=0.8)
plt.grid(True)
plt.show()