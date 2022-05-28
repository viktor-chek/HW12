from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import add_blueprint

UPLOAD_FOLDER = "uploads"


app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(add_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
