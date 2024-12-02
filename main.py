import pandas as pd
import numpy as np

# Генерация случайных оценок от 2 до 5 для 10 учеников и 5 предметов
np.random.seed(42)  # Фиксируем seed для воспроизводимости
data = {
    'Ученик': [f'Ученик {i}' for i in range(1, 11)],
    'Математика': np.random.randint(2, 6, 10),
    'Русский язык': np.random.randint(2, 6, 10),
    'Литература': np.random.randint(2, 6, 10),
    'Биология': np.random.randint(2, 6, 10),
    'Физика': np.random.randint(2, 6, 10)
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Сохраняем данные в CSV-файл
file_path = "student_scores.csv"  # Имя файла
df.to_csv(file_path, index=False)

# Считываем данные из CSV-файла
df_from_csv = pd.read_csv(file_path)

# Вывод первых нескольких строк DataFrame
print("Данные об оценках учеников из CSV:")
print(df_from_csv.head())

# Средняя оценка по каждому предмету
average_scores = df_from_csv.iloc[:, 1:].mean()
print("\nСредняя оценка по каждому предмету:")
print(average_scores)

# Медианная оценка по каждому предмету
median_scores = df_from_csv.iloc[:, 1:].median()
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Q1, Q3 и IQR для математики
Q1_math = df_from_csv['Математика'].quantile(0.25)
Q3_math = df_from_csv['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")
print(f"IQR для математики: {IQR_math}")

# Стандартное отклонение по каждому предмету
std_deviation = df_from_csv.iloc[:, 1:].std()
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)
