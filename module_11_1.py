import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd

url = 'https://api.worldbank.org/v2/country/RUS/indicator/SP.POP.TOTL?date=2000:2023&format=json'

responce = requests.get(url)

if responce.status_code == 200:
    data = responce.json()

    population_data = data[1]
    df = pd.DataFrame(population_data)

    # pprint(population_data)
    df = df[['date', 'value']]
    df.columns = ['Year', 'Population']
    df['Year'] = df['Year'].astype(int)
    df = df.sort_values(by='Year').reset_index(drop=True)
    year = list(df.Year)
    population = list(df.Population)
else:
    print("Ошибка при получении данных:", responce.status_code)

fig = plt.figure(layout='constrained', facecolor='#6699cc')
fig.suptitle('Plots')

sfig1, sfig2, sfig3 = fig.subfigures(3, 1)

sfig1.set_facecolor('#6699cc')
sfig2.set_facecolor('#6699cc')
sfig3.set_facecolor('#6699cc')

sfig1.suptitle('Population of Russian Federation')
ax1 = sfig1.subplots()
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')
ax1.plot(year, population, color='red')

pie1 = np.random.uniform(0, 1, 4)
pie2 = np.random.uniform(0, 1, 8)

sfig2.suptitle('Random data')
ax2 = sfig2.subplots(1, 2, sharey=True)
ax2[0].set_title('Pie 1')
ax2[1].set_title('Pie 2')
ax2[0].pie(pie1)
ax2[1].pie(pie2)

data = np.random.normal(0, 1, 100)

sfig3.suptitle('Hist')
ax3 = sfig3.subplots()
ax3.hist(data, bins=50, color='red', edgecolor='black')

ax3.set_xlabel('Values')
ax3.set_ylabel('Frequency')
plt.show()
