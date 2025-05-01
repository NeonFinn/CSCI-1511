import matplotlib.pyplot as plt
import math

x_values = []
y_values = []

for degree in range (361):
    radians = math.radians(degree)
    x = math.cos(radians)
    y = math.sin(radians)

    x_values.append(x)
    y_values.append(y)

plt.plot(x_values, y_values, color = "red", linewidth = 5)
plt.title("Circle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()