from flask import Flask, render_template

app = Flask('test', template_folder='./templates/')


@app.route('/')
def home():
    return "hello world 2!"


@app.route('/template/')
def template():
    return render_template('templates/home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
