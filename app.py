from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
	rows = []
	conn = sqlite3.Connection('hello.db', check_same_thread=False)
	curr = conn.cursor()
	rows0 = curr.execute('select * from hellotbl')
	for row in rows0:
		rows.append(row)
	conn.close()
	return render_template('index.html', rows=rows)

@app.route('/getcode', methods=['POST'])
def recieve():
	if request.method == 'POST':
		conn = sqlite3.Connection('hello.db', check_same_thread=False)
		name = request.form.get('name')
		college = request.form.get('college')
		curr = conn.cursor()
		curr.execute('''
			CREATE TABLE IF NOT EXISTS hellotbl (name TEXT, college TEXT);
			''')
		curr.execute('''
			INSERT INTO hellotbl VALUES (?,?);
			''',  (name, college))
		conn.commit()
		conn.close()
	return redirect(url_for('index'))



if __name__ == '__main__':
	app.run(debug=True)