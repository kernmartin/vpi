from flask import Flask, render_template
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True,
)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/cuemode")
def cuemode():
  return render_template("cuemode.html")

@app.route("/cueeditmode")
def cueeditmode():
  return render_template("cueeditmode.html")

if __name__ == "__main__":
  app.run(debug=True)
