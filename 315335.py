import numpy as np
import pandas as pd
import itertools

# Морфологічні параметри
morph_params = {
    'Investment Level': ['High', 'Medium', 'Low'],
    'Market Condition': ['Growing', 'Stable', 'Declining'],
    'Competition Level': ['Strong', 'Moderate', 'Weak'],
    'Internal Resources': ['Sufficient', 'Limited', 'Critical']
}

# Створимо всі можливі комбінації факторів (морфологічний простір)
scenarios = list(itertools.product(*morph_params.values()))

# Перетворимо ці сценарії в DataFrame для зручності
scenario_df = pd.DataFrame(scenarios, columns=morph_params.keys())

# Виведемо кілька перших сценаріїв
print("Морфологічний простір можливих сценаріїв:")
print(scenario_df.head())

# Матриця впливу факторів на ймовірність сценаріїв (Cross Impact Analysis)
# У прикладі візьмемо просту випадкову матрицю, яка може бути розширена або адаптована для реальних даних.
# Наприклад, матриця може враховувати взаємозв'язки між ринком, інвестиціями та конкуренцією.

# Фактори, що впливають на сценарії
factors = ['Economy', 'Investment', 'Competition', 'Internal Resources', 'Market Demand']
num_scenarios = len(scenario_df)

# Випадкова матриця впливу факторів на сценарії (розширте цю матрицю реальними даними)
factor_impact_matrix = np.random.rand(len(factors), num_scenarios)

# Перетворимо в DataFrame
factor_impact_df = pd.DataFrame(factor_impact_matrix, index=factors, columns=range(num_scenarios))

# Виведемо матрицю впливу факторів на сценарії
print("\nМатриця впливу факторів на сценарії (Cross Impact Analysis):")
print(factor_impact_df)

# Початкові ймовірності для кожного сценарію (можуть бути оцінені експертно)
initial_probabilities = np.random.rand(num_scenarios)
initial_probabilities /= initial_probabilities.sum()  # нормалізуємо ймовірності

# Враховуємо вплив факторів на ймовірність сценаріїв
factor_influence = factor_impact_matrix.sum(axis=0)  # сума впливів на кожен сценарій
final_probabilities = initial_probabilities * factor_influence

# Нормалізуємо ймовірності
final_probabilities /= final_probabilities.sum()

# Додаємо ймовірності до таблиці сценаріїв
scenario_df['Probability'] = final_probabilities

print("\nЙмовірності для кожного сценарію:")
print(scenario_df[['Investment Level', 'Market Condition', 'Competition Level', 'Internal Resources', 'Probability']])

# Знайдемо сценарій з найбільшою ймовірністю
most_likely_scenario = scenario_df.loc[scenario_df['Probability'].idxmax()]

print("\nНайбільш ймовірний сценарій:")
print(most_likely_scenario)

# Візуалізація ймовірностей сценаріїв
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
scenario_df['Probability'].plot(kind='bar')
plt.title('Ймовірність сценаріїв')
plt.xlabel('Сценарії')
plt.ylabel('Ймовірність')
plt.show()