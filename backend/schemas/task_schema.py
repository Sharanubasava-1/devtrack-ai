from flask_marshmallow import Marshmallow
from marshmallow import fields
from models.task_model import Task

ma = Marshmallow()

class TaskSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str()
    priority = fields.Str()
    deadline = fields.DateTime()
    risk_level = fields.Str()
    complexity = fields.Str()
    ai_warning = fields.Str()

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
