
# creation de la page  Helo Word

from flask import Flask, render_template, request
app = Flask(__name__)


# Définition de la route pour la page d'accueil

@app.route("/")
def hello():
  return render_template("home.html", message = "Hello World style is corrcet !")

# Définition de la route pour la seconde page 

@app.route("/second")
def secondPage():
  return render_template("second_page.html")

#route d a'ffichage du formualire

@app.route('/register')
def testForm():
  return render_template("test_formulaire.html")

# Définition de la route pour soulmettre le formulaire en methode POST

@app.route('/register', methods=['GET', 'POST'])
def register():
  firstname = request.form['firstname']
  lastname = request.form['lastname']
  sexe = request.form['sexe']
  title = "Mr" if sexe == "Masculin" else "Mme" # ternaire pour tester la condition 
  pseudo = request.form['pseudo']
  
  return render_template("form.html", message= f" Bonjour {title}, {firstname}, {lastname}, votre nom d'utilisateur est {pseudo} ")



#Lancement de la page au moment du demarrage de l'application

if __name__ == "__main__":
  app.run(debug=True)
