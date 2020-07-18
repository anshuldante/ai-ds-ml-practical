import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe with an x column containing values from -10 to 10
df = pd.DataFrame ({'x': range(-10, 11)})

# Add a y column by applying the solved equation to x
df['y'] = (3*df['x'] - 4) / 2

#Display the dataframe
print(df)

plt.plot(df['x'], df['y'], color='brown', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

df.