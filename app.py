from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "monkeys are great")
    return f'I think, {escape(name)}!'