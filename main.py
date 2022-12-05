from flask import Flask
appl=Flask(__name__)
@appl.route("/")
def hello():
    return "Hello world!"
@appl.route("/harry")
def helo():
    return "Hellovvvfdgfd world!"

appl.run()