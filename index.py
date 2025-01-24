# pip install requests beautifulsoup4 lxml fake_headers

import requests
from bs4 import BeautifulSoup

response = requests.get('https://habr.com/ru/articles/')
print (response.request.headers)

# Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

# URL страницы с новыми статьями
URL = 'https://habr.com/ru/articles/'  # Замените на нужный вам URL

# Получаем страницу
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем статьи
articles = soup.find_all('article')  # Предполагаем, что статьи находятся в теге <article>

# Список для подходящих статей
matching_articles = []

# Перебираем статьи
for article in articles:
    # Извлекаем заголовок, дату и ссылку
    title = article.find('h2')  # Предполагаем, что заголовок находится в теге <h2>
    date = article.find('time')  # Предполагаем, что дата находится в теге <time>
    link = article.find('a', href=True)  # Предполагаем, что ссылка находится в теге <a>
    
    if title and date and link:
        title_text = title.get_text()
        date_text = date.get('datetime')  # Получаем дату в формате ISO
        link_url = link['href']
        
        # Проверяем наличие ключевых слов в заголовке или описании
        if any(keyword.lower() in title_text.lower() for keyword in KEYWORDS):
            matching_articles.append(f"{date_text} – {title_text} – {link_url}")

# Выводим подходящие статьи
for article in matching_articles:
    print(article)