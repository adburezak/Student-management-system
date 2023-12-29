from sqlite3 import *

conn = connect('super7.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE STUDENT2(
                first_name text,
                last_name text,
                ID  integer primary key,
                gender char,
                department text,
                course text,
                assignment integer,
                mid_exam integer,
                final_exam,
                total_mark,
                grade text
      )''')

conn.commit()
conn.close()
