from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

app = Flask(__name__)

  
app.secret_key = 'a'

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nxt90748;PWD=u6RJ1WLjgi2XiLHR",' ',' ')
print(conn)
print("connection success")

@app.route('/home')
def home():
    return render_template('')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)