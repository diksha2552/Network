from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/")
def func():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:disk@2552@/Company_struct'
    result = db.engine.execute(text("select name from details_empl"))
    names = []
    for row in result:
        names.append(row[0])
    print(names)
    return ''.join(names)

if __name__ == '__main__':
    app.run(debug=True)
