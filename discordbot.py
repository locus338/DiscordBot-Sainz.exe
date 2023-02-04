import os
from threading
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello!'

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    bot.run(token)    
    stay()
import Thread
def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False, debug=True)
def stay():
    thread = Thread(target=run)
    thread.start()
