import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")




# Path of the file to read
brawl = pd.read_csv("../input/")

brawl.head()







# Path of the file to read
brawl = pd.read_csv("../input/##########.csv")
brawl.head()






sns.scatterplot(x=brawl['K/D R 5'], y=brawl['AVG DMG'])




import matplotlib.pyplot as plt
import numpy as np

volts_wire = pd.read_excel("../input/length-wire/VoltsWires.xlsx")
x=volts_wire['Length of Wire (cm)']
y=volts_wire['Average Potential difference across wire (V)']

plt.scatter(x, y)

z = np.polyfit(x, y, 2)
p = np.poly1d(z)

plt.plot(x, p(x))

plt.title("Length of Wire vs Potential Difference across wire")
plt.xlabel("Length of Wire (cm)")
plt.ylabel("Average Potential difference across wire (V)")
plt.show()