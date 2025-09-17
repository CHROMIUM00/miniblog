import os
from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blogDB.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    auth.init_app(app)

    @app.route('/test1')
    def hello():
        return "nihao"

    from .article import ops
    app.register_blueprint(ops.post, url_prefix='/api/post')

    from . import auth
    app.register_blueprint(auth.auth, url_prefix='/api/auth')

    return app


if __name__ == "__main__":
    create_app().run()
