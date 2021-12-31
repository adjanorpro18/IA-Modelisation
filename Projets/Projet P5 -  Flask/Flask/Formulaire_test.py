
# creation de la page  Helo Word


from flask import Flask, render_template, request
import mysql.connector as mariadb
import pandas as pd
import numpy as np
from PIL import Image
import pickle

app = Flask(__name__)

conn = mariadb.connect(host='localhost', user='root', password='')
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS flask_db")
cur.execute("USE flask_db")

#model = pickle.load(open('model.py/trained_digits.sav', 'rb'))



# Définition de la route pour la page d'accueil(1)

@app.route("/")
def home():
  return render_template("home.html", message="Flask_App!")

# Définition de la route pour la seconde page (3)

@app.route("/second")
def secondPage():
  return render_template("second_page.html")

#route d'affichage du formualire   (4)

@app.route('/register')
def testForm():
  return render_template("test_formulaire.html")

# Définition de la route pour soulmettre le formulaire en methode POST (4 et 5)

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

    
  

# Faire une page /utilisateurs-inscrits qui permet de lister tous les noms d'utilisateurs présents dans la base de donnée.(6)
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


#Affichage du formulaire de rechargement du fichier dataframe (7)

@app.route('/file')
def fileForm():
  return render_template("file.html")

#Faire une page avec Flask qui affiche les statistiques de base d'un dataframe que l'utilisateur aurait chargé grâce à un formulaire

@app.route('/data', methods=['POST', 'GET'])
def dataFile():
  if request.method == 'POST':
    datafile = request.files['file_data']
      
      
  # Chargement de la dataframe chargée dans le projet et le stocker dans une variable
    #print(type(datafile))
  
  df = pd.read_csv(datafile)
  stats = df.describe()
 
  
  return render_template("data.html", tables=[stats.to_html(classes='data')], titles=stats.index)


# Charger un modèle entrainé sur MNIST et afficher la prédiction du modèle lorsque le user charge une image via un formulaire.(8)

@app.route('/image')
def imageForm():
  return render_template("image.html")

  # recuperre l'image chargé par l'utilisateur

from PIL import Image 


@app.route('/image', methods=['POST','GET'])
def imageModel():
  if request.method == 'POST':
    imagefile = request.files['image_file']
    
    #reconversion du fichier image 
  
    npimage = Image.open(imagefile)
    im = np.array(npimage)[:,:]
    
    model = pickle.load(open('trained_digits.sav', 'rb'))
    result= model.predict(im)
    return render_template("image.html", images = result)

  
  

    


#Lancement de la page au moment du demarrage de l'application

if __name__ == "__main__":
  app.run(debug=True)
