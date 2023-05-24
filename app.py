from flask import Flask, render_template, request
from pymsaviz import MsaViz


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/alignment', methods=['GET', 'POST'])
def alignment():
    if request.method == 'POST':
        gene = request.form['gene']
        if gene == "ELOA3DP":
            img_path = "example_aln.png"
        return render_template('alignment.html', fig_obj=img_path)
    
    # If the request method is GET, render the form
    return render_template('alignment.html')


@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)