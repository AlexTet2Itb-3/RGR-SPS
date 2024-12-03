import pandas as pd
import numpy as np

# Устанавливаем случайное семя для воспроизводимости
np.random.seed(42)

# Генерация данных
num_employees = 100  # Количество сотрудников
departments = ['Производство', 'Продажи', 'Маркетинг', 'Финансы', 'HR']
positions = ['Менеджер', 'Специалист', 'Директор', 'Аналитик', 'Рабочий']

# Создаем DataFrame
data = {
    'employee_id': range(1, num_employees + 1),
    'name': [f'Сотрудник {i}' for i in range(1, num_employees + 1)],
    'department': np.random.choice(departments, num_employees),
    'position': np.random.choice(positions, num_employees),
    'salary': np.random.randint(30000, 150000, num_employees),  # Зарплата от 30k до 150k
    'experience_years': np.random.randint(1, 21, num_employees)  # Опыт от 1 до 20 лет
}

df = pd.DataFrame(data)

# Сохраняем в CSV файл
df.to_csv('udobreniya_salary_data.csv', index=False)

print("Данные по оплате труда компании 'Удобрения' успешно сгенерированы и сохранены в 'udobreniya_salary_data.csv'.")