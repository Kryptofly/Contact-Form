from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Message: {message}')
        return 'Form submitted!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
