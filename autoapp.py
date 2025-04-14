# -*- coding: utf-8 -*-

from api.app import create_app

app = create_app()

@app.route("/test")
def hello_world():
    return "<p>I am a chinese 000!</p>"

