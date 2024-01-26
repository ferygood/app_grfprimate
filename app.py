from flask import Flask, render_template, request
import mysql.connector
from tfprimate.getInfo import ncbi_summary

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

db_config = {
        'host': '172.17.0.2',
        'user': 'root',
        'password': 'yao123',
        'database': 'grfprimate',
    }

@app.route('/search', methods=['GET', 'POST'])
def search():

    gene_data = None

    if request.method == 'POST':
        gene = request.form['gene_name']

        # establish a connection
        with mysql.connector.connect(**db_config) as conn:
            # Create a cursor
            with conn.cursor() as cursor:
                # Your SQL query
                query = """
                    SELECT primateGRFs.EnsemblID, primateGRFs.GeneName, primateGRFs.Hsap, GRFID.Entrezid
                    FROM primateGRFs
                    JOIN GRFID ON primateGRFs.EnsemblID = GRFID.EnsemblID
                    WHERE lower(primateGRFs.GeneName) = lower(%s) OR lower(primateGRFs.EnsemblID) = lower(%s)
                """

                # Execute the query with parameters
                cursor.execute(query, (gene, gene))

                # Fetch the results
                gene_data = cursor.fetchall()
    print(gene_data)
    if not gene_data:
        message = "Sorry. The request of gene regulatory factor is not found in the database."
        return render_template('search.html', message=message)
    
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
    