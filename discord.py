from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hello!'

if __name__ == "__main__":
    app.run(port=9000)
