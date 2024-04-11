from flask import Flask

def create_app():
    app = Flask(__name__)
    
    with open("secret_key.txt", 'r') as file:
        secret_key = file.read().strip() 
    app.config["SECRET_KEY"] = secret_key
    
    return app