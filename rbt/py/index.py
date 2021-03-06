class Index():
    @classmethod
    def add_sma(self,stock,window,keep = True):
    # Add Sma column
        sma                     = (lambda stock,sma:stock.Close.rolling(window).mean())
        name                    = f"Sma_{window}"
        stock[name]             = sma(stock,window) 
        if keep:
            value_0             = stock[name].loc[~stock[name].isnull()].iloc[0] # first value not null
            stock[name].fillna(value_0,inplace=True) # #https://stackoverflow.com/questions/25147707/pandas-fillna-not-working
            print(value_0)
        print(f"Added {name}, {window} campioni")
        return stock
    @classmethod
    def add_rsi(self,stock,length,keep = True):
    # Add Rsi column
    # https://www.roelpeters.be/many-ways-to-calculate-the-rsi-in-python-pandas/
        import pandas_ta as pta
        name                    = f'Rsi_{length}'
        stock[name]             = pta.rsi(stock['Close'], length = length) # Add Rsi column
        if keep:
            value_0             = stock[name].loc[~stock[name].isnull()].iloc[0] # first value not null
            stock[name].fillna(value_0,inplace=True)
            print(value_0)
        print(f"Added {name}, {length} campioni")
        return stock
    @classmethod
    def add_stocastich(self,stock,window_k,window_d,keep = True):
    # Add Rsi column
        stock[f'low_k']         = stock['Close'].rolling(window_k).min()
        stock[f'high_k']        = stock['Close'].rolling(window_k).max()
        name1                   = f"%K_{window_k}"
        stock[name1]            = (stock['Close']-stock['low_k'])*100/(stock['high_k']-stock['low_k'])
        name2                   = f"%D_{window_d}"
        stock[name2]            = stock[name1].rolling(window_d).mean()
        name                    = f'Stocastic_{window_k,window_d}'
        if keep:
            value1_0            = stock[name1].loc[~stock[name1].isnull()].iloc[0] # first value not null
            stock[name1].fillna(value1_0,inplace=True)
            value2_0            = stock[name2].loc[~stock[name2].isnull()].iloc[0] # first value not null
            stock[name2].fillna(value2_0,inplace=True)
            print(value1_0,value2_0)
        print(f"Added {name}, {window_k,window_d} campioni")
        return stock
    @classmethod
    def add_momentum(self,stock,window_m,keep = True):
    # Add momentum index
        name = f'Momentum_{window_m}'
        stock[name]             = stock['Close'].pct_change(window_m)
        if keep:
            value_0             = stock[name].loc[~stock[name].isnull()].iloc[0] # first value not null
            stock[name].fillna(value_0,inplace=True)
            print(value_0)
        print(f"Added momentum_{window_m}, {window_m} campioni")
        return stock
# Test
def test1():
    import pandas as pd                                                     #                                     
    stock = pd.DataFrame([])                                                #             
    stock['Close'] = pd.Series(range(10,20))                                #                             
    stock = Index().add_sma(stock,7,keep=True)                                        #                     
    print(stock)
def test2():
    import pandas as pd
    import random
    stock           = pd.DataFrame([])
    stock['Close']  = pd.Series(random.sample(range(1000), 10))
    stock           = Index().add_stocastich(stock,6,3)
    print(stock)
def atest1():
    'https://stackoverflow.com/questions/55203292/calculating-momentum-signal-in-python-using-1-month-and-12-month-lag'
    'auxilary for test'
    import pandas as pd
    import random
    size = 10
    Investment_start = 1
    wallet = ['BTC-EUR']
    stock                   = pd.DataFrame([],columns=['Close'])
    stock['Close']          = pd.Series(random.sample(range(1000), size))   # Create random array
    stock['Diff']           = pd.Series(stock['Close'].diff())              # Diff with previous value
    stock['Cumsum']         = pd.Series(stock['Close'].diff().cumsum())     # Sum of diff
    stock['Momentum']       = pd.Series(stock['Close'].pct_change(1))       # Percentage in window
    stock['Strategy']       = pd.Series(['enable']*size)                    # Strategy status
    stock['Investment']     = pd.Series([Investment_start][0])              # 
    print(stock)

if __name__ == '__main__':
    # test1()
    test1()