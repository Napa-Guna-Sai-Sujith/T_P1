import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

data = pd.read_csv(r"F:\vs code\Training\T_P1\datasets\cancer_data_dashboard.csv")

if data['diagnosis'].dtype == 'O':
    data['diagnosis'] = data['diagnosis'].map({'M': 'Malignant', 'B': 'Benign'}).fillna(data['diagnosis'])

sns.scatterplot(
    x='area_mean', 
    y='texture_mean', 
    hue='diagnosis', 
    data=data, 
    palette='Set1', 
    alpha=0.8, 
    s=70
)

plt.title('Tumor Analysis: Mean Area vs. Mean Texture by Diagnosis', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Mean Area ($mm^2$)', fontsize=11)
plt.ylabel('Mean Texture (Gray-scale Value)', fontsize=11)
plt.legend(title='Pathological Diagnosis', loc='upper right')

plt.tight_layout()
plt.show()