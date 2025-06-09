from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_caching import Cache
from app.routes import Route
from flask_marshmallow import Marshmallow
from app.config.config_cache import cache_config

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
cache = Cache()

def create_app() -> Flask:
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    marshmallow.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config=cache_config)

    route = Route()
    route.init_app(app)
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app