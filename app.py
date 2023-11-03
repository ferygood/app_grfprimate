import os
from flask import Flask, render_template, Blueprint
from tfprimate.getInfo import ncbi_summary

configuration = dict(
    development = dict(
        ENV='development',
        APPLICATION_ROOT='/',
    ),
    production=dict(
        ENV='production',
        APPLICATION_ROOT='/grfprimate/',
    ),
)

# get configuration based on environment
config_key = os.getenv('FLASK_CONFIG', 'production')
config_dict = configuration[config_key]
app = Flask(__name__, static_url_path=config_dict['APPLICATION_ROOT'])
app.config.update(config_dict)
bp = Blueprint('myapp', __name__)

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

app.register_blueprint(bp, url_prefix=app.config['APPLICATION_ROOT'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    