from forex_python.converter import CurrencyRates, CurrencyCodes


# Formatting the Currency information into a dictionary
with open("CurrencyCodes.txt") as f:
    for line in f:
        curList = line.split("|")
        curList.pop(0)
    curList = [s.replace('-', '') for s in curList]
    curList = [item.strip() for item in curList]
    curList = [item.split(" ", 1) for item in curList]

currencyDict = {currency[0]: currency[1] for currency in curList}


class ConversionRates:
    def __init__(self, fromCurrency, toCurrency, amount=1):
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        self.amount = amount

    def get_rate(self):
        c = CurrencyRates()

        if self.toCurrency not in currencyDict:
            raise Exception(f"{self.toCurrency} is not a valid currency")
        elif self.fromCurrency not in currencyDict:
            result = f"{self.fromCurrency} is not valid currency"
        elif self.fromCurrency and self.toCurrency in currencyDict:
            result = c.convert(self.fromCurrency,
                               self.toCurrency, self.amount)

        return result

    def get_code(self):
        sym = CurrencyCodes()
        symA = sym.get_symbol(self.fromCurrency)
        symB = sym.get_symbol(self.toCurrency)
        return symA, symB


# newConv = ConversionRates('USD', 'INR')
# returnedConv = newConv.get_rate()

# symbolss = newConv.get_code()
# print(symbolss[1], returnedConv)
