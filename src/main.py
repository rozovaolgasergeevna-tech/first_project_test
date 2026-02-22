print('Hello from repository test\!')

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

def print_author():
    # Читаем значение переменной AUTHOR
    author = os.getenv('AUTHOR')
    
    # Проверяем, найдено ли значение
    if author:
        print(f"Автор проекта: {author}")
    else:
        print("Переменная AUTHOR не найдена в .env файле")

# Для проверки работы функции
if __name__ == "__main__":
    print_author()
