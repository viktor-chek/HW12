import logging
import json
from json import JSONDecodeError


logging.basicConfig(filename="basic.log", encoding="utf-8", level=logging.DEBUG)


def get_posts(search):   
    """Ищет вхождение подстроки в постах и возвращает список постов. 
Обрабатывает исключение если нет доступа к json файлу"""
    content = []
    try:
        with open("posts.json", encoding="utf-8") as file:
            data = json.load(file)
        for item in data:
            if search in item["content"].lower():
                content.append(item)
        return content
    except FileNotFoundError:
        logging.exception("Ошибка доступа к JSON файлу")
    except JSONDecodeError:
        logging.exception("Файл не удается преобразовать JSON")


def save_in_json(pic, text):
    """Добавляет пост в в файл с данными."""
    dict_temp = {"pic": f"uploads/{pic}", "content": text}
    try:
        with open("posts.json", encoding="utf-8") as f:
            all_data = json.load(f)
            all_data.append(dict_temp)
            with open("posts.json", "w", encoding="utf-8") as outfile:
                json.dump(all_data, outfile, ensure_ascii=False, indent=2)
                return all_data[-1]
    except FileNotFoundError:
        logging.exception("Ошибка доступа к JSON файлу")
        return False
    except JSONDecodeError:
        logging.exception("Файл не удается преобразовать JSON")


def check_upload(file):
    """Проверяет с нужным ли расширением загруженный файл"""
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', ""}
    extension = file.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False
