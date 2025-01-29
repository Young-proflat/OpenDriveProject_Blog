from flask import Flask
from flask_restx import Api, fields
from config import DevConfig
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from project import project_ns
# from user import user_ns
# from flask_login import LoginManager

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    JWTManager(app)

    # Create API instance
    api = Api(app, doc='/docs')

    # Add namespaces to the API
    api.add_namespace(project_ns)  # Use the Namespace object here
    # api.add_namespace(user_ns)     # Use the Namespace object here

    # Example models (if needed for documentation)
    user_model = api.model(
        "users",
        {
            "id": fields.Integer(),
            "username": fields.String(),
            "email": fields.String(),
            "password": fields.String(),
            "role": fields.String(),
            "created_at": fields.Integer()
        }
    )

    requester_model = api.model(
        "requester",
        {
            "id": fields.Integer(),
            "status": fields.String(),
            "requester_id": fields.Integer(),
            "project_id": fields.Integer(),
            "requested_at": fields.String()
        }
    )

    # Shell context for CLI
    @app.shell_context_processor
    def make_shell_content():
        return {
            "db": db,
            "Project": Project,
            "User": User
        }

    return app
