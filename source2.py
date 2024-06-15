from flask import Flask,request,render_template
import mysql.connector as sql
from datetime import date
cnx = sql.connect(host='127.0.0.1', user='root', password='Elango@7666', port='3306', database='dbms')
cur=cnx.cursor()
app=Flask(__name__)
@app.route('/patientinput')
def index():
    return render_template('patientinput.html')

@app.route('/submit', methods=['POST'])
def submit():
    pid = request.form['patient_id']
    patient_name = request.form['patient_name']
    cause = request.form['cause']
    patient_age = request.form['patient_age']
    doctor_name = request.form['doctor_name']
    contact = request.form['contact']
    k7=str(date.today())
    a=f"insert into patientadmit(pid,pname,cause,age,dname,contact,admitted)values('{pid}','{patient_name}','{cause}','{patient_age}','{doctor_name}','{contact}','{k7}');"
    cur.execute(a)
    cnx.commit()
    cur.close()
    cnx.close()
    response = ("Success")

    return response
if __name__=='__main__':
    app.run(debug=True,port=5501)