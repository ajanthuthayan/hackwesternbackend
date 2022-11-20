import csv
from flask import Flask, json
from flask_cors import CORS

employees = []

def read_csv(file):
        with open(f'{file}.csv') as file:
            reader = csv.reader(file) 
            data = list(reader) 
            headers = data[0:1:1][0]
            print(headers)
            content = data[1::1]
            for row in content:
              employees.append({headers[0]: row[0], headers[1]:row[1]})
              
read_csv('Amazon')

app = Flask(__name__)
CORS(app)


@app.route('/amazon/software-engineer', methods=['GET'])
def get_amazon_software_engineers():
  return json.dumps(employees)

if __name__ == '__main__':
    app.run() 
