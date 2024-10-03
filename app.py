from flask import Flask, render_template
from config import config

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/auth/login.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()











# @app.route('/about')
# def about():
#     return 'About Page Route'
#
# @app.route('/portfolio')
# def portfolio():
#     return 'Portfolio Page Route'
#
# @app.route('/contact')
# def contact():
#     return 'Contact Page Route'
#
# @app.route('/api')
# def api():
#     with open('data.json', mode='r') as my_file:
#         text = my_file.read()
#         return text