import pandas as pd
from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def main():
    dt = date.today().strftime("%d/%-m/%Y")
    db = pd.read_csv('oncadb.csv')
    db = db[db['date'] == dt]
    db = db.head().to_dict()
    resp = {'oncall': db}

    return resp

if __name__ == '__main__':
    app.run()