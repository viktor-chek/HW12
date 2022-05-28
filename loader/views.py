from flask import Blueprint, render_template, request
import logging
from functions import save_in_json, check_upload

logging.basicConfig(filename="basic.log")

add_blueprint = Blueprint("add_blueprint", __name__, template_folder="templates")


@add_blueprint.route("/post", methods=["GET", "POST"])  #Представление страницы с загрузкой поста
def add_post():
    return render_template("post_form.html")


@add_blueprint.route("/upload", methods=["POST"])  # Вьюшка информирующая о загрузке или не закгрузке поста
def page_upload():
    try:
        file = request.files.get("picture")
        filename = file.filename
        if check_upload(filename):
            file.save(f"uploads/{filename}")
            text_content = request.form.get("content")
            data = save_in_json(filename, text_content)
            if not data:
                return """
                <link rel="stylesheet" href="../static/style.css">
                <h1 align="center">Что-то пошло не так</h1>
                """
            return render_template("post_uploaded.html", data=data)
        else:
            logging.info("Не правильный формат загрузки файла")
            return """
            <link rel="stylesheet" href="../static/style.css">
            <h1 align="center">Ошибка загрузки</h1>
            <h5 align = "center">Файл не соответствует поддерживаемому формату (jpg, jpeg,png)</h5>
            """

    except PermissionError:
        logging.exception("Ошибка при загрузке файла (Файл не найден)")
        return """
                <link rel="stylesheet" href="../static/style.css">
                <h1 align="center">Ошибка загрузки</h1>
                <h5 align = "center">Файл для загрузки не найден</h5>
                """
