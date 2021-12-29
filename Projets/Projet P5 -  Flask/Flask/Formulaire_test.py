
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

# Définition de la route pour la page du formulaire

@app.route('/register', methods=['POST', 'GET'])
def register():
  form = request.form['firstname', 'lastname', 'sexe', 'pseudo']
  processed_form = form.capitalize()

  return render_template("test_formulaire.html", form=processed_form)


#Lancement de la page au moment du demarrage de l'application

if __name__ == "__main__":
  app.run(debug=True)
