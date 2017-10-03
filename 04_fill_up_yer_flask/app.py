'''
Jennifer Yu 
HW #4: Fill Up Yer Flask
SoftDev Period 7 
2017-09-23
'''

#from app import app, db
from flask import Flask, abort, redirect

app = Flask(__name__)


@app.route('/')
def index():
    retStr  = "<h1>?</h1>"
    retStr += "Two roads diverged in a wood,<br>"
    retStr += "and I-- I took the one less traveled by,<br>"
    retStr += "And that has made all the difference.<br><br>"
    retStr += "How should we live our lives? <br>"
    retStr += 'Live it <a href = "/path1">purposefully. </a><br>'
    retStr += 'Live it <a href = "/path2">fearlessly.</a><br>'
    retStr += 'Live it <a href = "/path3">mindfully.</a> <br>'
    return retStr

@app.route('/path1')
def p1():
    return redirect('https://plato.stanford.edu/entries/life-meaning/')

@app.route('/path2')
def p2():
    return redirect('https://diana-goetsch.squarespace.com/blog-page/')


@app.route('/path3')
def p3():
    return redirect('http://www.metastatic.org/text/This%20is%20Water.pdf')

    
if __name__ == '__main__':
    app.debug = True
    
app.run()
