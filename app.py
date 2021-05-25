from flask import Flask,render_template,request,flash,redirect
from forex_python.converter import CurrencyRates,CurrencyCodes
from util import printhello

app = Flask(__name__)
app.config["SECRET_KEY"] = "currency-secret"

@app.route('/',methods=["POST","GET"])
def get_form():
    return render_template('index.html')
    
@app.route('/result',methods=["POST"])
def get_converted_value():
    fromTxt = request.form.get('text-from')
    toTxt = request.form.get('text-to')
    amtTxt = request.form.get('text-amt')

    checkCurrency = CurrencyCodes()
    checkFrom = checkCurrency.get_currency_name(fromTxt)
    checkTo = checkCurrency.get_currency_name(toTxt)
    
    if fromTxt == '' or toTxt == '' :
        flash("Please Enter Currency Name")
    if checkFrom == None and fromTxt != '':
        flash("Enter valid code for FROM")
    if checkTo == None and toTxt != '' :
        flash("Enter valid code for TO")

    if checkFrom != None and checkTo != None :
        c = CurrencyRates()
        codeResult = checkCurrency.get_symbol(toTxt)

        convertedValue = c.convert(fromTxt,toTxt,float(amtTxt))
         
        return render_template('result.html',
        codeResult = codeResult,
        convertedValue = convertedValue)
    
    return redirect('/')
        
    
