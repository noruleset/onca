import pandas as pd
from flask import Flask
from datetime import date,timedelta

app = Flask(__name__)

@app.route('/')
@app.route('/<skip>')
def main(skip=None):
    today = date.today()
    if skip:
        tom = today + timedelta(days = 1) 
        dt = tom.strftime("%d/%-m/%Y")
    else:
        dt = today.strftime("%d/%-m/%Y")

    db = pd.read_csv('oncadb.csv')
    db = db[db['date'] == dt]
    db = db.head().to_dict()
    resp = {'oncall': db}
    
    return resp

if __name__ == '__main__':
    app.run()