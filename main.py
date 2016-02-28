from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data')
def data():
    # The first argument is the directory path where sample_data
    # exists. Eg send_from_directory('/home/xyz/downloads/', 'sample_data.txt')
    return send_from_directory('.', 'sample_data.txt')

if __name__ == '__main__':
    app.run()
