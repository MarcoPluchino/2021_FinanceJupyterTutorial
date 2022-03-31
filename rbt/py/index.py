class Index():

    @classmethod
    def add_sma(self,stock,window):
    # Add Sma column
        sma = (lambda stock,sma:stock.Close.rolling(window).mean())
        name = f"Sma{window}"
        stock[name] = sma(stock,window) 
        return stock
    @classmethod
    def add_rsi(self,stock,length):
    # Add Rsi column
    # https://www.roelpeters.be/many-ways-to-calculate-the-rsi-in-python-pandas/
        import pandas_ta as pta
        stock['Rsi'] = pta.rsi(stock['Close'], length = length) # Add Rsi column
        return stock
# Test
def test1():
    import pandas as pd
    import random as rd
    stock = pd.DataFrame([])
    stock['Close'] = pd.Series(range(10,20))
    stock = Index().add_sma(stock,7)
    print(stock)
if __name__ == '__main__':
    test1()
