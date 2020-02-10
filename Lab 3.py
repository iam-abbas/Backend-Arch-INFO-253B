from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    my_string1 = '''<h1>Hello!</h1><p>Congrats on building your own server!</p><br /></br /><a href="/page2">Go to the next page</a>'''
    return my_string1
@app.route('/page2')
def page2():
    my_string2= '''<h1>This is page 2!</h1><p>let us move to page three</p><br /></br /><a href="/page3">Go to the next page</a>'''
    return my_string2
@app.route('/page3')
def page3():
    my_string3 = '''<h1>This is page 3!</h1><p>And of end of our journey!</p>'''
    return my_string3

@app.route('/hello/<name>')
def hello_name(name):
    return '<h1>Hello '+name+'</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)