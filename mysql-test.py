from flask import Flask, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        #password = "password"
        db = "employees"

        self.con = pymysql.connect(host=host, user=user, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT id, first_name, last_name FROM employees LIMIT 50")
        result = self.cur.fetchall()
        return result

    def employee_detail(self, id):
        self.cur.execute("SELECT * FROM employees WHERE id = %s", id)
        result = self.cur.fetchall()
        return result
db = Database()

@app.route('/')
def employees():

    def db_query():
        #db = Database()
        emps = db.list_employees()

        return emps

    res = db_query()

    return render_template('employees.html', result=res, content_type='application/json')

@app.route('/employee_detail/<id>')
def employee_detail(id):
    res = db.employee_detail(id)
    return render_template('employee_detail.html', result=res, content_type='application/json')    
