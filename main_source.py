from flask import Flask, request, render_template,jsonify
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
    patient_id = request.form['patient_id']
    patient_name = request.form['patient_name']
    cause = request.form['cause']
    patient_age = request.form['patient_age']
    doctor_name = request.form['doctor_name']
    contact = request.form['contact']
    k7=str(date.today())
    a=f"insert into patientadmit(pid,pname,cause,age,dname,contact,admitted)values('{patient_id}','{patient_name}','{cause}','{patient_age}','{doctor_name}','{contact}','{k7}');"
    cur.execute(a)
    cnx.commit()
    cur.close()
    cnx.close()
    return render_template('final.html')
    return jsonify(success=True)

@app.route('/patientdischarg')
def patientdischarg():
    return render_template('patientdischarg.html')

@app.route('/submits', methods=['POST'])
def submits():
    patient_id = request.form['patient_id']
    patient_name = request.form['patient_name']
    k=f"select * from patientadmit where pid={patient_id};"
    cur.execute(k)
    lk=[]
    k7=str(date.today())
    for i in cur:
        lk.append(i)
    ls=lk[0]
    k=f"insert into patientdischarge(pid,pname,cause,age,dname,contact,admitted,discharge)values('{ls[0]}','{ls[1]}','{ls[2]}','{ls[3]}','{ls[4]}','{ls[5]}','{ls[6]}','{k7}');"
    cur.execute(k)
    k=f"delete from patientadmit where pid='{patient_id}' and pname='{patient_name}';"
    cur.execute(k)
    cnx.commit()
    cur.close()
    cnx.close()
    return render_template('final.html')
    return jsonify(success=True)
l=[]
q='select * from doctors;'
cur.execute(q)
for i in cur:
    l.append(i)
l1=[]
q='select * from patientadmit;'
cur.execute(q)
for i in cur:
    l1.append(i)
l2=[]
q='select * from patientdischarge;'
cur.execute(q)
for i in cur:
    l2.append(i)
@app.route('/doctors')
def doctors():
    return render_template('doctors.html',details=l)
@app.route('/patientadmit')
def patientadmit():
    return render_template('patientadmit.html',details=l1)
@app.route('/patientdischarge')
def patientdischarge():
    return render_template('patientdischarge.html',details=l2)

if __name__ == '__main__':
    app.run(debug=True,port=5501)
