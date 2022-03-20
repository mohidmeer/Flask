from BiopythonModule import ProcessFasta
from DnaComparison  import  GenReport
import os
import time
from flask import Flask, flash, render_template, redirect, url_for, request, session
from database import Database
from uuid import uuid4
import numpy as np
import csv
# from faker import Faker
def make_unique(string):
    ident = uuid4().__str__()[:9]
    return f"{ident}-{string}"

                                                                                                                                                    # fake=Faker()
                                                                                                                                                    # db = Database()
                                                                                                                                                    # con=db.connect()
                                                                                                                                                    # cursor = con.cursor()
 
                                                                                                                                                    # for x in range (30):                                                                                                                                   #     cursor.execute("INSERT INTO customers (name,phone,address) VALUES(%s, %s, %s)", (fake.name(),fake.phone_number(),fake.address()))                                                                                                                                                  #     con.commit()
app = Flask(__name__)
app.secret_key = os.urandom(12)
db = Database()

@app.route('/comp')
def comp():
    data = db.readcomp(None)
    return render_template('Comparator.html',data=data)
app.config['DNA_UPLOADS']='C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\DnaTextFiles'
@app.route('/dnaprocess',methods=['POST','GET'])
def DnaPro():
    if request.method == 'POST' and request.files and request.form['save']:
        # FILES SECTION 😒😒 👀
        SeqA=request.files['SeqA']
        SeqB=request.files['SeqB']
        SeQAFilename= make_unique(SeqA.filename)
        SeQBFilename= make_unique(SeqB.filename)
        SeqA.save(os.path.join(app.config['DNA_UPLOADS'],SeQAFilename))
        SeqB.save(os.path.join(app.config['DNA_UPLOADS'],SeQBFilename))
        SeqAPath=os.path.join(app.config['DNA_UPLOADS'],SeQAFilename)
        SeqBPath=os.path.join(app.config['DNA_UPLOADS'],SeQBFilename)
        report=GenReport(SeqAPath,SeqBPath)
        if db.insertDnaText(request.form['name'],SeqAPath,SeqBPath,report):
            time.sleep(4)
            flash("Your Files Have Been Uploaded")
        else:
            flash("Cannot Upload Fles")
        return redirect(url_for('comp'))
    else:
        return redirect(url_for('comp'))
@app.route('/deletecom/<int:id>/')
def compDelete(id):
    if request.method == 'POST' or request.method == 'GET':

        if db.deletecom(id):
            flash('Files have been deleted')

        else:
            flash('Files Cannot be deleted')

        session.pop('delete', None)

        return redirect(url_for('comp'))
    else:
        return redirect(url_for('comp'))
@app.route('/showpcom/<int:id>/')
def showcomp(id):
    data = db.readcomp(id);
    # FOR IMAGE PATH WE SORTED ARRAY
    path=data[0][4]
    # FOR EXTRATING NAME FROM PATHS
    Report=os.path.basename(path)
    p= url_for('static',filename='DnaReports/'+Report)
    return render_template('ShowReport.Html',p=p)
    










# LANDING PAGE FOR WEBSITTE
@app.route('/')
def index():
    data = db.read(None)
    return render_template('index.html', data = data)


@app.route('/bio')
def Bio():
    data=db.readbio(None)
    return render_template('Bio.html',data = data )


# ADD NEW RECORD PAGE
@app.route('/add/')
def add():
    return render_template('add.html')

app.config['IMAGE_UPLOADS']="C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\img"
# ADD NEW RECORD PAGE
@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():

    if request.method == 'POST' and request.files and request.form['save']:
        # IMAGE SECTION 😒😒 👀
        image=request.files['image']
        imagename= make_unique(image.filename)
        image.save(os.path.join(app.config["IMAGE_UPLOADS"],imagename))
        x=os.path.join(app.config["IMAGE_UPLOADS"],imagename)
        #FORM SECTION 
        if db.insert(request.form,x):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


# UPDATE REROUTE
@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)


#UPDATE POST REQUEST
@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))



# DELETE RECORD ROUTE
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)


# DELETE RECORD POST REQUEST
@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


@app.route('/showpro/<int:id>/')
def showpr(id):
    data = db.read(id);
    # FOR IMAGE PATH WE SORTED ARRAY
    path=data[0][4]
    # FOR EXTRATING NAME FROM PATHS
    pic=os.path.basename(path)
    p= url_for('static',filename='img/'+pic)
    
    return render_template('pro.html', data = data , p = p)
    
app.config['FASTA_UPLOADS']='C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\fasta'
app.config['CSV_UPLOADS']='C:\\Users\\mohid\\Desktop\\FLASK\\dev\\static\\csv'
@app.route('/subfasta', methods = ['POST', 'GET'])
def uploadfasta():
    if request.method == 'POST' and request.files['fasta'] and request.form['save']:
        # IMAGE SECTION 😒😒 👀
        file=request.files['fasta']
        fastaname= make_unique(file.filename)
        file.save(os.path.join(app.config["FASTA_UPLOADS"],fastaname))
        FastaFilePath=os.path.join(app.config["FASTA_UPLOADS"],fastaname)
        CsvFilePath=ProcessFasta(FastaFilePath)
        time.sleep(4)
        # FORM SECTION 
        if db.insertFasta(request.form['name'],FastaFilePath,CsvFilePath):
            
            flash("Your File Has Been Uploaded")
            
        else:
            flash("Try Again")

        return redirect(url_for('Bio'))
    else:
        return redirect(url_for('Bio'))  
    
@app.route('/showprob/<int:id>/')
def showb(id):
    data = db.readbio(id);
    path=data[0][3]
    print(path)
    with open(path) as csvfile:
      csdata = list(csv.reader(csvfile))
    #   print(csdata)
    return render_template('Btab.html', csdata = csdata )

@app.route('/deleteb/<int:id>', methods = ['POST','GET'])
def delet(id):
    if request.method == 'POST' or request.method == 'GET':

        if db.deleteb(id):
            flash('A File has been deleted')

        else:
            flash('A File can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('Bio'))
    else:
        return redirect(url_for('Bio'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')




if __name__ == '__main__':
    
    app.run(debug=True,)
