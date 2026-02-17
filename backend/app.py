from flask import Flask
from flask_cors import CORS
from config import Config
from models.task_model import db
from routes.task_routes import task_bp
# from schemas.task_schema import ma # schema is initialized in schemas/task_schema.py but ma needs app? 
# Usually ma.init_app(app) is good practice but I didn't verify if I need it explicitly with the AutoSchema usage in flask-marshmallow without init.
from schemas.task_schema import ma

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
ma.init_app(app)

app.register_blueprint(task_bp, url_prefix='/api/tasks')

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return {"message": "DevTrack AI Backend is running"}

if __name__ == '__main__':
    app.run(debug=True)
