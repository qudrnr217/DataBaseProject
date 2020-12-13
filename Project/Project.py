import sqlite3
from flask import Flask, render_template, request


 
app = Flask(__name__)
 

@app.route("/")
@app.route("/home")
def home():
   
    return render_template('home.html')

@app.route("/Client", methods=['GET','POST'])
def Client():
    db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    db.row_factory = sqlite3.Row
    if request.method == 'POST':
        db.execute(
            'Insert into Client values(?,?,?,?,?);',
            (request.form['Phone Number'],request.form['Experience'],
            request.form['Have Many'], request.form['Age'],
            request.form['Location'])
        )
        db.commit()

        # items = db.execute(
        #     'select *'
        #     ' from Pet'
        # ).fetchall()

        # Pet_output = ""
        # for item in items :
        #     Pet_output += item['Pet_Number']
        #     Pet_output += item['Species']
        #     Pet_output += item['Age']
        #     Pet_output += item['Sex']
        #     Pet_output += item['Center_Number'] 

        db.close()
        return render_template('Pet.html')
    else:
    # Client_items = db.execute(
    #     'select Phone_Number, Experience, Have_many, C_age, C_location'
    #     ' from Client'
    # ).fetchall()
   
    # Client_output = ""

    # for item in Client_items:
    #     Client_output += item['Phone_Number']
    #     Client_output += item['Experience']
    #     Client_output += item['Have_many']
    #     Client_output += item['C_age']
    #     Client_output += item['C_location']  

        db.close()

    return render_template('Client.html')

@app.route("/Center")
def Center():
    db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    db.row_factory = sqlite3.Row
    if request.method == 'POST':
        db.execute(
            'Insert into Center values(?,?,?,?,?);',
            (request.form['Center_Number'],request.form['Location'],
            request.form['Many_Pet'], request.form['Grade'],
            request.form['Pet_Hospital'])
        )
        db.commit()     

        db.close() 
        return render_template('Center.html')
    else :

        LastNumber_item = db.execute(
            'select Center_Number '
            ' from (select Center_Number from Center order by Center_Number desc limit 1)'
            ' order by Center_Number asc'
        ).fetchone()
    
        LastNumber = ord(LastNumber_item['Center_Number'])-47  
        # Center_items = db.execute(
        #     'select Center_Number, Location, Many_Pet, Grade, Pet_Hospital'
        #     ' from Center'
        # ).fetchall()
    
        # Center_output = ""

        # for item in Center_items:
        #     Center_output += item['Center_Number']
        #     Center_output += item['Location']
        #     Center_output += item['Many_Pet']
        #     Center_output += item['Grade']
        #     Center_output += item['Pet_Hospital']
        
        db.close()

    return render_template('Center.html', LastNumber=LastNumber)
 
@app.route("/OK")
def OK():
    return render_template('OK.html')

@app.route("/Pet")
def Pet():
    return render_template('Pet.html')
if __name__ == "__main__":
    app.debug=True
    app.run(host='127.0.0.1',port=5001)
    