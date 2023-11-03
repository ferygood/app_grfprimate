from flask import Flask, render_template
from tfprimate.getInfo import ncbi_summary

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    gene_data = []
    gene_info = None #initialize first to avoid UnboundLocalError

    gene_info = ncbi_summary(gene_data[0][3]) if gene_data else None

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
    app.run(debug=True, port=8000, host='0.0.0.0')
    