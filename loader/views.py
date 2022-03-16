from flask import Blueprint, render_template, request
import logging

from main.utils import PostsHandler
from exceptions import DataLayerError, PictureWrongTypeError
from loader.utils import save_uploaded_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename="basic.log", level=logging.INFO)

@loader_blueprint.route('/post')
def create_new_post_page():
    return render_template("post_form.html")

@loader_blueprint.route('/post', methods=['POST'])
def create_new_post_from_user_data_page():

    picture = request.files.get("picture", None)
    content = request.form.get("content", None)
    posts_handler = PostsHandler("posts.json")


    if not picture or not content:
        logging.info("Данные не загружены")
        return "Данные не загружены"

    try:
        picture_path = save_uploaded_picture(picture)
    except PictureWrongTypeError:
        logging.info("Неверный тип файла")
        return "Неверный тип файла"
    except FileNotFoundError:
        return "Файл не сохранен, неверный путь"

    picture_url = "/"+picture_path

    post_object = {"pic": picture_url, "content": content}

    try:
        posts_handler.add_post(post_object)
    except DataLayerError:
        return "Добавить пост не удалось"

    return render_template("post_uploaded.html", picture_url=picture_url, content=content)
