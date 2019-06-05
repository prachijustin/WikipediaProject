from flask import Flask, render_template, request
from wikipedia import * 

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        word = request.form.get('word')
        wiki_page = page(word)  
        try:       
            title = wiki_page.title
            url = wiki_page.url
            summary = wiki_page.summary 
        except exceptions as e:
            summary = e.options
        return render_template('index.html', title = title, url = url, summary = summary)
           


if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)
