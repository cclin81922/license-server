import os
import sqlite3


dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = '%s/license.db' % dir_path

conn = sqlite3.connect(db_path)

c = conn.cursor()

t = (os.environ['SSL_CLIENT_S_DN_CN'],)
c.execute('UPDATE license SET counter = counter + 1 WHERE cn = ?', t)
conn.commit()

c.execute('SELECT pass, threshold, counter FROM license WHERE cn = ?', t)
r = c.fetchone()
print('[DEBUG] %s | %s | %s' % r)
_pass = r[0]
_threshold = r[1]
_counter = r[2]

conn.close()

if _counter <= _threshold:
    print('[INFO] %s' % _pass)
else:
    print('[INFO] =.=')
