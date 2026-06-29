import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

data = pd.read_csv(r"F:\vs code\Training\T_P1\datasets\10_Property_stolen_and_recovered.csv")

df_2010 = data[data['Year'] == 2010][['Area_Name', 'Cases_Property_Stolen', 'Cases_Property_Recovered']].copy()
top_theft_states = df_2010.sort_values(by='Cases_Property_Stolen', ascending=False).head(10)

ax = sns.barplot(
    x='Area_Name', 
    y='Cases_Property_Stolen', 
    data=top_theft_states, 
    palette='flare',
    hue='Area_Name',
    legend=False
)

plt.title('Top 10 Indian States by Property Theft Cases (Year: 2010)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('State / Union Territory', fontsize=11, labelpad=10)
plt.ylabel('Total Cases Registered', fontsize=11)
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()