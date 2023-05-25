from flask import Flask, render_template, request
import psycopg
from psycopg import sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        gene = request.form['gene_name']

        # establish a connection
        with psycopg.connect("dbname=tfprimate user=postgres password=yao123") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("""
                    SELECT EnsemblID, GeneName, Hsap 
                    FROM primateGRFs
                    WHERE lower(GeneName) = lower(%s)"""), [gene] 
                )

                gene_data = cur.fetchall()
                conn.commit()
    
        if not gene_data:
            message = "Sorry. The request of transcription factor is not found in the database."
            return render_template('search.html', message=message)

        return render_template('search.html', gene_data=gene_data)
    
    return render_template('search.html')

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
    app.run(debug=True)