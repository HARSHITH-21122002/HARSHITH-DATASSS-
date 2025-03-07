from flask import FLASK
from flask_sqlalchemy  import SQLAlchemy
from flask_cors import CORS

app=FLASK(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///friends.db"
app.config["SQLALCHEMY_TRACKING_MODIFICATIONS"]=False

db = SQLAlchemy(app)

if __name__ =="__main__":
    db.run(debug=False)