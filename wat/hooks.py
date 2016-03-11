from flask import url_for
from wat import app

def static(path):
    return url_for('static', filename=path)

@app.context_processor
def context_processor():
    return dict(static=static)
