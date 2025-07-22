from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/residential')
def residential():
    return render_template('residential.html')

@app.route('/commercial')
def commercial():
    return render_template('commercial.html')

@app.route('/renovation')
def renovation():
    return render_template('renovation.html')

if __name__ == '__main__':
    app.run(debug=True)