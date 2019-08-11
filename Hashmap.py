import numpy as np

a = np.zeros((10, 10))
a[2][3] = 1
a[3][2] = 1
a[5][4] = 1
a[5][1] = 1

visited = [0] * 10
print(visited)