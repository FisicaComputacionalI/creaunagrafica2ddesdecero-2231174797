import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [7.66,7,7.5,8,7,9]
plt.plot(x, y, 'b-.')
plt.xlabel('semestre')
plt.ylabel('promedio')
plt.savefig('temp3.png')
