from flask import Flask, jsonify
import os
import pydsb



""" print(dsb.get_plans()[0]['url']) """
""" print(dsb.get_postings())
print(dsb.get_news()) """

app = Flask(__name__)

@app.route("/")
def help():
    return "Please provide username and password in the url. Example: https://dsb-notifier-api.up.railway.app/username/password. \n\n Sincerly, \n\n APUEM"

@app.route('/<string:usr>/<string:psw>')
def index(usr, psw):
    dsb = pydsb.PyDSB(usr, psw)
    return jsonify({'url': dsb.get_plans()[0]['url']})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
