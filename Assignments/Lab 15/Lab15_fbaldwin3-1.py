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

plt.style.use("dark_background")
figure, graph = plt.subplots()
plt.plot(x_values, y_values, color = "red", linewidth = 5)
graph.set_title("Circle", fontsize = 20)
graph.set_xlabel("X-axis", fontsize = 14)
graph.set_ylabel("Y-axis", fontsize = 14)

plt.show()