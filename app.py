from flask import Flask, session, request, render_template, redirect, make_response, flash, jsonify

from currency import ConversionRates, currencyDict

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"


@app.route("/")
def homepage():
    """Show Homepage"""
    currency_list = currencyDict
    return render_template("home.html", currency_list=currency_list)


@app.route("/convert", methods=["GET", "POST"])
def convert():
    if request.method == "POST":
        req = request.form
        fromCurrency = req.get("fromCurrency")
        toCurrency = req.get("toCurrency")
        if req.get("amount"):
            amount = int(request.form["amount"])
        else:
            amount = 1

        if currencyDict.get(fromCurrency) is None:
            flash(f"{fromCurrency} is an invalid currency code")
            return redirect("/")
        if currencyDict.get(toCurrency) is None:
            flash(f"{toCurrency} is an invalid currency code")
            return redirect("/")

    newConversion = ConversionRates(fromCurrency, toCurrency, amount)
    symbol = newConversion.get_code()
    response = newConversion.get_rate()

    result = str(f"result: {symbol[1]} {round(response,2)}")
    return render_template("results.html", result=result)
