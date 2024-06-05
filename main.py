#1. Пишем простой парсер. В итоге мы получим коллекцию со всеми рядами таблицы.
import requests
from bs4 import BeautifulSoup
url = "https://"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rows = soup.find_all("tr")
# tr - каждый ряд таблицы
# td - каждая ячейка внутри ряда таблицы
data = []

#2. Теперь нам нужно перебрать коллекцию. Используем цикл “for”.

for row in rows:
cols = row.find_all("td")
# Используем укороченный вариант цикла for
# Для удаления пробелов и других лишних символов используем функцию strip
cleaned_cols = [col.text.strip() for col in cols]
# Чтобы удалить пробелы, оставляем ()
# Чтобы удалить какие-то символы из начала и конца, пишем ('то-что-надо-удалить')
data.append(cleaned_cols)
# Функция append добавляет в список.
print(data)

# Также можно удалять символы из списка при помощи метода pop и других.
# Преобразуем данные (цены)
# Представим, что мы уже достали информацию из списков, и теперь у нас два списка, которые находятся внутри друг друга (вложенные списки, двумерные массивы).

data = [
['100', '200', '300']
['400', '500', '600']
]
# С сайта мы получаем именно списки.
numbers = []

#2. Используем функции float или int, чтобы преобразовать данные.

for row in data:
for text in row:
number = int(text)
numbers.append(number)
print(numbers)

# Чаще всего преобразования — это просто преобразование одного типа данных в другой.
# Отфильтруем данные — это можно делать через обычные условия.
# У нас также есть двумерный список, содержащий другие списки.

data = [
[100, 110, 120]
[400, 500, 600]
[150, 130, 140]
]
list = []

#Используем цикл for и условие:

for row in data:
for item in row:
if item > 190:
list.append(item)
print(list)

# Разрабатываем программу с учётом всего того, что мы изучили.
# Мы будем парсить данные с сайта https://tomsk.hh.ru/vacancies/programmist и сохранять их в csv-файл.

# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



# Инициализируем браузер
driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
# driver = webdriver.Chrome()



# В отдельной переменной указываем сайт, который будем просматривать
url = "https://tomsk.hh.ru/vacancies/programmist"



# Открываем веб-страницу
driver.get(url)



# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)



# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')



# Выводим вакансии на экран
print(vacancies)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []



# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for vacancy in vacancies:
   try:
   # Находим элементы внутри вакансий по значению
   # Находим названия вакансии
     title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
     # Находим названия компаний
     company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
     # Находим зарплаты
     salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
     # Находим ссылку с помощью атрибута 'href'
     link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except:
     print("произошла ошибка при парсинге")
     continue



# Вносим найденную информацию в список
parsed_data.append([title, company, salary, link])



# Закрываем подключение браузер
driver.quit()



# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
# Используем модуль csv и настраиваем запись данных в виде таблицы
# Создаём объект
writer = csv.writer(file)
# Создаём первый ряд
writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])

# Прописываем использование списка как источника для рядов таблицы
writer.writerows(parsed_data)

# Чтобы удобнее просмотреть результат, открываем файл через программу для чтения и редактирования таблиц.
# 9. Нажимаем на клавишу Enter.
