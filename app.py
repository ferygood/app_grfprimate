from flask import Flask, render_template, request
import psycopg
from psycopg import sql
from tfprimate.getInfo import ncbi_summary # wait for database have ensemblID to ENTREZ


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    gene_data = []

    if request.method=='POST':
        gene = request.form['gene_name']

        #establish a connection
        with psycopg.connect('dbname=tfprimate user=postgres password=yao123') as conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("""
                    SELECT EnsemblID, GeneName, Hsap
                    FROM primateGRFs
                    WHERE lower(GeneName) = lower(%s) OR lower(EnsemblID) = lower(%s)"""), [gene, gene]
                )

                gene_data = cur.fetchall()
                conn.commit()

        if not gene_data:
            message="Your request cannot be found in the database. <br>Please check if you type the correct name or id for transcription factors."
            return render_template('search.html', message=message)
    return render_template('search.html', gene_data=gene_data)

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
    from waitress import serve
    serve(app, host="0.0.0.0", port=8070)
    #app.run(debug=True)