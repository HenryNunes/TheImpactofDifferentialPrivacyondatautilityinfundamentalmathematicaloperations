import pandas as pd 
import matplotlib.pyplot as plt 

dados = pd.read_csv('data_output/noise.txt')

#print(dados.head())
#print(dados.shape)

serie = pd.Series(dados['m']) 


#print(dados.columns)
#print(dados["m"])


fig = plt.figure(figsize =(10, 7))
fig.suptitle('Sequences metric values', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)

# Creating plot
ax.boxplot(serie)
ax.set_ylabel('metric value')


# show plot
plt.show()

