import requests
import json 

#response = requests.get('https://gitlab.grokhotov.ru/hr/yii-test-vacancy/-/raw/master/books.json')
#
#response_json = json.loads(response.text)
#
#for books in response_json:
#    if books['categories'] == []:
#        books['categories'] = ['new']
#    print(books['title'],books['categories'])
import os

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test2.settings")

# Загружаем приложение Django
import django
django.setup()

# Импортируем необходимые модели после настройки окружения Django
from mysire.models import Books

response = requests.get('https://gitlab.grokhotov.ru/hr/yii-test-vacancy/-/raw/master/books.json')

response_json = json.loads(response.text)

for book_data in response_json:
    title = book_data['title']
    categories = book_data['categories']
    
    # Если список категорий пуст, задаем значение ['new']
    if not categories:
        categories = ['new']
    
    # Создаем или обновляем экземпляр модели Books
    book, _ = Books.objects.update_or_create(
        titles=title,
        defaults={
            'categories': json.dumps(categories)  # Сохраняем список категорий в виде JSON-строки в базе данных
        }
    )

    print(f'Книга "{book.titles}" с категориями "{json.loads(book.categories)}" сохранена в базу данных.')

#def resp():
#    if (
#        response.status_code != 204 and
#        response.headers["content-type"].strip().startswith("application/json")
#    ):
#        try:
#            return response.json()
#        except json.decoder.JSONDecodeError:
#            print('The string does NOT contain valid JSON')
#
#resp()

