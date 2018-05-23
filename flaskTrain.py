from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(len(username))
    print(password)
    print(len(password))
    error = None
    if len(username) < 5:
        error = 'Username must be at least 5 characters'
    if len(password) < 6:
        error = 'Password must be at least 8 characters'
    elif not any(c.isupper() for c in password):
        error = 'Your password needs at least 1 capital'
    if error is not None:
        return jsonify({'r': 1, 'error': error})
    return jsonify({'r': 0, 'rs': password})



if __name__ == '__main__':
    app.run(debug=True)
