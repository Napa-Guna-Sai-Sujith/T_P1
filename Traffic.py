import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

data = pd.read_csv(r"F:\vs code\Training\T_P1\datasets\Road.csv")

weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_accidents = data.groupby(['Day_of_week', 'Accident_severity'])['Number_of_casualties'].sum().reset_index()

ax = sns.barplot(
    x='Day_of_week', 
    y='Number_of_casualties', 
    hue='Accident_severity',
    data=df_accidents, 
    order=weekday_order,
    palette='viridis'
)

plt.title('Distribution of Accident Casualties Across Weekdays by Severity', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Day of the Week', fontsize=11)
plt.ylabel('Aggregate Number of Casualties', fontsize=11)
plt.xticks(rotation=30)
plt.legend(title='Accident Severity', frameon=True)

plt.tight_layout()
plt.show()