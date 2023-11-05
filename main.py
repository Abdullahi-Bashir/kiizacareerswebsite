from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')
  # return send_from_directory('home.html', 'styles.css')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
