import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_olympic = pd.read_csv('olympic_athletes.csv')
print(df_olympic)

df_summer = df_olympic[df_olympic['Season'] == 'Summer']
avg_data = df_summer.drop_duplicates(subset=['Name', 'Sex', 'Year'], keep='first').groupby(['Sex','Year']).mean().reset_index().dropna()
male_avg_data = avg_data[avg_data['Sex'].str.contains('M')]
female_avg_data = avg_data[avg_data['Sex'].str.contains('F')]
std = df_summer.drop_duplicates(subset=['Name', 'Sex', 'Year'], keep='first').groupby(['Sex','Year']).std().reset_index().dropna()
male_std = std[std['Sex'].str.contains('M')]
male_std = male_std['Height']
female_std = std[std['Sex'].str.contains('F')]
female_std = female_std['Height']
female_std
fig, ax = plt.subplots(figsize=(7,5))
sns.lineplot(x = 'Year', y = 'Height', data = avg_data, hue = 'Sex', linewidth=1.5,palette=['r', 'b'], ax=ax, errorbar = 'sd')
sns.despine()
ax.set_ylim(140, 200)
handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order],loc='lower left', framealpha=0)
#ax.legend(loc='lower left', framealpha=0)
ax.set_xlabel('Year',fontsize=12)
ax.set_ylabel('Height(cm)',fontsize=12)
ax.set_title('Average Olympian Height (+/- std dev) in the Summer Olympics',fontsize=12)
plt.show()