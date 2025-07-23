import matplotlib.pyplot as plt
days="x"
temperature="y"
days=['Suaturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
temperature=[30,35,29,37,38,36,40]
plt.plot(days,temperature,marker="x",linestyle="--",color="r")
plt.title("Temprture")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()