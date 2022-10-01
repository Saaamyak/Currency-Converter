import json
from flask import Flask, app, render_template, request
import requests
  
class Currency_convertor:
    rates = {} 
    def __init__(self, url):
        data = requests.get(url).json() #used to fetch data from url
        self.rates = data["rates"] 
    
    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'EUR' :
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        return amount
  
app = Flask(__name__) #creating instance of flask where 'name' is python module


@app.route('/',methods=['GET','POST'])
def hello():
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '28fab490330c9b581266f96de7a3a92f') #creating string object from given object
    data = list((requests.get(url).json())['rates'].keys())
    if request.method == 'POST':
        try:
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            amount = float(request.form['amount']) #convert a string or number to float
            c = Currency_convertor(url) #instance of class 
            
            ans = c.convert(from_currency, to_currency, amount)
            return render_template('index.html',response='succeess', ans=str(ans),data=json.dumps(data))
        except Exception as e:
            return render_template('index.html',response='fail',ans=str(e),data=json.dumps(data))
    else:
        return render_template('index.html', response='', ans = '',data=json.dumps(data))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)