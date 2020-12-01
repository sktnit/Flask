from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    page = 'about'
    # use of templating engine
    return render_template('about.html', page__name=page)


app.run(debug=True)
