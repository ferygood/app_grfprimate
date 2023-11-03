from flask import Flask, render_template, request
from tfprimate.getInfo import ncbi_summary

app = Flask(__name__)
app.static_url_path = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    gene_data = []
    gene_info = None #initialize first to avoid UnboundLocalError

    return render_template('search.html', gene_data=gene_data, gene_info=gene_info)

@app.route('/alignment')
def alignment():
    return render_template('alignment.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    