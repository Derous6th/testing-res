from flask import Flask
from controllers.homeController import home
app = Flask(__name__, static_url_path ='/')
app.register_blueprint(home)
app.run(debug=True)