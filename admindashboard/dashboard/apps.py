from django.apps import AppConfig
from flask import Flask,render_template, request


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

app = Flask(__name__)
@app.route('/firstone')
def first():
    return(render_template("/templates/index.html"))

@app.route('/second')
def second():
    return(render_template("/templates/index.html"))

if __name__ == '__main__':
    app.run()
