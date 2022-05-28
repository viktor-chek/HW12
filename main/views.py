from flask import Blueprint, render_template, request
import functions
import logging

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="basic.log")


@main_blueprint.route("/") #Представление главной страницы
def main_page():
    return render_template("index.html")

         
@main_blueprint.route("/search")  #Представление страницы поиска
def search_page():
    s = request.args.get("s", None)
    search_request = functions.get_posts(s.lower())
    logging.info("Запрос на поиск поста")
    return render_template("post_list.html", search=search_request, s=s)
