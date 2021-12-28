
# creation de la page  Helo Word

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("home.html", message = "Hello World style is corrcet !")

@app.route("/second")
def secondPage():
  return render_template("second_page.html")

if __name__ == "__main__":
  app.run()
