import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.DataFrame({'Høyde':
                   [173, 178, 153, 175, 167, 155, 161, 164, 177, 157, 162, 165, 172, 165, 170, 167, 185, 170, 178, 185, 175, 183, 182],
                   'Skonummer':
                   [42, 45, 37, 39, 40, 37, 39, 38, 40, 36, 38, 38, 40, 39, 39, 39, 42, 40, 43, 43, 43, 45, 43]})

df.plot.scatter(x='Høyde', y='Skonummer')


sb.lmplot(x='Høyde',y='Skonummer',data=df, fit_reg=True)



plt.show()
