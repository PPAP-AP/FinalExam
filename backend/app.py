from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(host='db', dbname='research_db', user='admin', password='secret')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/myresearch')
def myresearch():
    cursor.execute("SELECT id, title, pdf_url FROM references")
    refs = cursor.fetchall()
    return render_template('myresearch.html', references=refs)

@app.route('/reference', methods=['GET', 'POST'])
def reference():
    if request.method == 'POST':
        title = request.form['title']
        pdf_url = request.form['pdf_url']
        cursor.execute("INSERT INTO references (title, pdf_url) VALUES (%s, %s)", (title, pdf_url))
        conn.commit()
        return redirect('/myresearch')
    cursor.execute("SELECT id, title, pdf_url FROM references")
    refs = cursor.fetchall()
    return render_template('reference.html', references=refs)

@app.route('/reference/delete/<int:id>')
def delete_reference(id):
    cursor.execute("DELETE FROM references WHERE id = %s", (id,))
    conn.commit()
    return redirect('/reference')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
