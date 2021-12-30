
# creation de la page  Helo Word

from flask import Flask, render_template, request, redirect
import mysql.connector as mariadb
import pandas as pd
import numpy as np
from flask import flash
from pandas.io.parsers import read_csv 



app = Flask(__name__)

conn = mariadb.connect(host='localhost', user='root', password='secret')
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS flask_db")
cur.execute("USE flask_db")




# Définition de la route pour la page d'accueil

@app.route("/")
def home():
  return render_template("home.html", message="Bienvenue sur Flask_App!")

# Définition de la route pour la seconde page 

@app.route("/second")
def secondPage():
  return render_template("second_page.html")

#route d'affichage du formualire

@app.route('/register')
def testForm():
  return render_template("test_formulaire.html")

# Définition de la route pour soulmettre le formulaire en methode POST

@app.route('/register', methods=['GET', 'POST'])
def register():
  if (request.method == 'POST'):
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    sexe = request.form['sexe']
    title = "Mr" if sexe == "Masculin" else "Mme" # ternaire pour tester la condition 
    pseudo = request.form['pseudo']
    cur.execute("CREATE DATABASE IF NOT EXISTS flask_db")
    cur.execute("USE flask_db")
    cur.execute("CREATE TABLE  IF NOT EXISTS Users(prenom VARCHAR(30) NOT NULL, nom VARCHAR(30) NOT NULL, sexe VARCHAR(15) NOT NULL, pseudo VARCHAR(20) NOT NULL UNIQUE )")
    cur.execute("INSERT INTO Users VALUES ('{}','{}','{}','{}')".format( firstname, lastname, sexe, pseudo))
    conn.commit()
    conn.close()
    cur.close()
    
    return render_template("form.html", message= f" Bonjour {title} {firstname} {lastname}, votre nom d'utilisateur est {pseudo} et vos informations ont été bien enregistrées ! ")
  else:
    return render_template("users.html")

    
  

# Affichage des données de la base de données
@app.route('/users', methods=['GET'])
def users():
  if request.method == 'GET' :
    #cur.execute("CREATE DATABASE IF NOT EXISTS flask_db")
    cur.execute("USE flask_db")
    cur.execute("SELECT * FROM Users")
    lignes = cur.fetchall()
    return render_template('users.html',rows=lignes) 
  else:
    return render_template("users.html", message=f"Pas d'utilisateur inscritss pour le moment !")


#Affichage du formulaire de rechargement du fichier dataframe

@app.route('/file')
def fileForm():
  return render_template("file.html")

#Faire une page avec Flask qui affiche les statistiques de base d'un dataframe que l'utilisateur aurait chargé grâce à un formulaire

@app.route('/data', methods=['POST', 'GET'])
def dataFile():
  if request.method == 'POST':
    #verifier si le fichier existe deja 
    #if 'datafile' not in request.files:
      #flash('Pas de fichier  existant !')
      #return redirect(request.url)
    
    # sinon on recharge le fichier
    datafile = request.files['file_data']
  
    #message si le fichier n'est pas bien charger
    #if datafile.filename == '':
      #flash("Merci de bien selectionner le fichier à charger")
      
    # Chargement de la dataframe dans le projet
    print(type(datafile))
  
  df = pd.read_csv(datafile)
  stats = df.describe()
 
  
  return render_template("data.html", tables=[stats.to_html(classes='data')], titles=stats.index)


#Lancement de la page au moment du demarrage de l'application

if __name__ == "__main__":
  app.run(debug=True)
