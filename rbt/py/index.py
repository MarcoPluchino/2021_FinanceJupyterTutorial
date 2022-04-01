class Index():

    @classmethod
    def add_sma(self,stock,window):
    # Add Sma column
        sma = (lambda stock,sma:stock.Close.rolling(window).mean())
        name = f"Sma_{window}"
        stock[name] = sma(stock,window) 
        print(f"Added {name}, {window} campioni")
        return stock
    @classmethod
    def add_rsi(self,stock,length):
    # Add Rsi column
    # https://www.roelpeters.be/many-ways-to-calculate-the-rsi-in-python-pandas/
        import pandas_ta as pta
        name = f'Rsi_{length}'
        stock[name] = pta.rsi(stock['Close'], length = length) # Add Rsi column
        print(f"Added {name}, {length} campioni")
        return stock
    @classmethod
    def add_stocastich(self,stock,window_k,window_d):
    # Add Rsi column
        stock['low_k']    = stock['Close'].rolling(window_k).min()
        stock['high_k']   = stock['Close'].rolling(window_k).max()
        stock['%K']     = (stock['Close']-stock['low_k'])*100/(stock['high_k']-stock['low_k'])
        stock['%D']     = stock['%K'].rolling(window_d).mean()
        return stock
# Test
def test1():
    import pandas as pd
    import random as rd
    stock = pd.DataFrame([])
    stock['Close'] = pd.Series(range(10,20))
    stock = Index().add_sma(stock,7)
    print(stock)
def test2():
    import pandas as pd
    import random
    stock = pd.DataFrame([])
    stock['Close'] = pd.Series(random.sample(range(1, 50), 49))
    stock = Index().add_stocastich(stock,6,3)
    print(stock)
if __name__ == '__main__':
    test2()

