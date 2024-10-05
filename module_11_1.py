import requests
import pandas as pd
import numpy as np

# Библиотека requests:
print('Библиотека requests:')

# URL для запроса
url = "https://requests.readthedocs.io/en/latest/index.html"

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Вывод полученных данных в консоль
    print(response.text)
else:
    print("Ошибка при получении данных:", response.status_code)
print('----------------------------------')

# Библиотека pandas:
print('Библиотека pandas:')

# Чтение данных из файла
data = pd.read_csv('text.txt', delimiter=' ')

# Пример анализа данных - подсчет количества строк и столбцов
num_rows = data.shape[0] + 1 # количество строк
num_cols = data.shape[1] # количество столбцов

# Пример анализа данных - получение описательных статистик
statistics = data.describe()

# Вывод результатов в консоль
print('Количество строк:', num_rows)
print('Количество столбцов:', num_cols)
print(statistics)
print('----------------------')

# Библиотека numpy:
print('Библиотека numpy:')

# Создание массива чисел
arr = np.array([1, 2, 3, 4, 5])

# Математические операции с массивом
sum_arr = np.sum(arr)  # Сумма всех элементов
mean_arr = np.mean(arr)  # Среднее значение
max_arr = np.max(arr)  # Максимальное значение
min_arr = np.min(arr)  # Минимальное значение
sqrt_arr = np.sqrt(arr)  # Квадратный корень каждого элемента

# Вывод результатов в консоль
print("Сумма: ", sum_arr)
print("Среднее значение: ", mean_arr)
print("Максимальное значение: ", max_arr)
print("Минимальное значение: ", min_arr)
print("Квадратный корень: ", sqrt_arr)