import sqlite3

conn = sqlite3.connect('redcloud.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS MainDB(project TEXT, keyword TEXT, info TEXT)')

"""def data_entry():
	c.execute("INSERT INTO mainDB VALUES('project1', 'nmap', 'data data data data')")
	conn.commit()
	c.close()
	conn.close()
"""

create_table()
