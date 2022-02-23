import matplotlib.pyplot as plt
Кандидаты = ['blue','orange', 'green', 'red','purple']
labels = ['А', 'Б', 'В','Г','Д']
#СТОЛБЧАТЫЕ
x = [1, 2, 3, 4, 5]
y = [16,18,	20,	22,	24]
sp = plt.subplot(231)
sp.bar(x, y, color=Кандидаты, edgecolor='k', tick_label=labels)
sp.grid(True, axis='y')
plt.title(r'Результаты опросов за месяц до выборов')
plt.xlabel('Кандидаты')

x = [1, 2, 3, 4, 5]
y = [20, 20,	18,	22,	20]
sp = plt.subplot(232)
sp.bar(x, y, color=Кандидаты, edgecolor='k', tick_label=labels)
sp.grid(True, axis='y')
plt.title(r'Результаты опросов за неделю до выборов')
plt.xlabel('Кандидаты')

x = [1, 2, 3, 4, 5]
y = [24,	22,	20,	18,	16]
sp = plt.subplot(233)
sp.bar(x, y, color=Кандидаты, edgecolor='k', tick_label=labels)
sp.grid(True, axis='y')
plt.title(r'Экзитполл')
plt.xlabel('Кандидаты')



#КРУГОВЫЕ
sp = plt.subplot(234)
data = [16,18,	20,	22,	24]
sp.pie(data, labels=('А', 'Б', 'В', 'Г', 'Д'),colors = ['blue','orange', 'green', 'red','purple'])
sp = plt.subplot(235)
data = [20, 20,	18,	22,	20]
sp.pie(data, labels=('А', 'Б', 'В', 'Г', 'Д'),colors = ['blue','orange', 'green', 'red','purple'])
sp = plt.subplot(236)
data = [24,	22,	20,	18,	16]
sp.pie(data, labels=('А', 'Б', 'В', 'Г', 'Д'),colors = ['blue','orange', 'green', 'red','purple'])
plt.show()
