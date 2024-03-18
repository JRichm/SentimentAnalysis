import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template
)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)