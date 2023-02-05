import os
from threading import Thread
from flask import Flask, render_template
app = Flask(__name__,template_folder="Templates")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    bot.run(token)    
    stay()
def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False, debug=True)
def stay():
    thread = Thread(target=run)
    thread.start()
