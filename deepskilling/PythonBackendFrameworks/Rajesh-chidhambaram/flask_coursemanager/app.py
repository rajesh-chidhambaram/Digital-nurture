from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprints
    from courses.routes import courses_bp
    app.register_blueprint(courses_bp)

    # Global Error Handler
    @app.errorhandler(404)
    def not_found(error):
        return {
            "error": "Resource not found"
        }, 404

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)