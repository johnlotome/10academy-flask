from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return "<h1>This is the homepage</h1>"

@app.route('/about',methods = ['GET'])
def about():
    title = 'About Page'
    return render_template('about.html',title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3333,debug=True)

