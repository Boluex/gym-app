import psycopg2
import psycopg2.extras as ext
import os


def run_sql(sql, values=None):
    results = []
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host")
        )
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)

        if cur.description:  # SELECT or RETURNING
            results = cur.fetchall()

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error:", error)
    finally:
        if conn:
            conn.close()
    return results
