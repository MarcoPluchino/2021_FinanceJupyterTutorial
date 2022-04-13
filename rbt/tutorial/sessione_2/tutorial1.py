import datetime
import requests
from urllib.parse import urljoin

class BinanceException(Exception):
    def __init__(self, status_code, data=None):

        self.status_code = status_code
        if data:
            self.code = data['code']
            self.msg = data['msg']
            message = f"{status_code} [{self.code}] {self.msg}"
        else:
            self.code = None
            self.msg = None
            message = f"status_code={status_code}"

        # Python 2.x
        # super(BinanceException, self).__init__(message)
        super().__init__(message)


def download_historical_data(symbol, date):

    def download_12h(start_date, end_date):
        start_time = int(start_date.timestamp() * 1000)
        end_time = int(end_date.timestamp() * 1000)

        BINANCE_API_KEY = '...'
        # BINANCE_SECRET_KEY = '...'

        PATH = '/api/v1/klines'

        params = {
            'symbol': symbol,
            'interval': '1m',   # 1m, 3m, 5m, 15m, 30m
            'limit': 1000,       # 1000 is max, but we using 720 = 60 (minutes) * 12 (hours)
            'startTime': start_time,
            'endTime': end_time
        }

        headers = {
            'X-MBX-APIKEY': BINANCE_API_KEY
        }

        url = urljoin(self.BASE_URL, PATH)
        r = requests.get(url, headers=headers, params=params)

        if r.status_code == 200:
            return r.json()
        else:
            if r.headers['Content-Type'] == 'application/json':
                raise BinanceException(status_code=r.status_code, data=r.json())
            else:
                raise BinanceException(status_code=r.status_code)

    # start_date = datetime.datetime(2019, 7, 15)
    # 0-12h
    start_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    end_date = start_date + datetime.timedelta(hours=12) - datetime.timedelta(seconds=1)
    data = download_12h(start_date, end_date)

    # 12-24h
    start_date = start_date + datetime.timedelta(hours=12)
    end_date = start_date + datetime.timedelta(hours=12) - datetime.timedelta(seconds=1)
    data.extend(download_12h(start_date, end_date))

    filename = f"{symbol}_{start_date.strftime('%Y-%m-%d')}"

    with open(f"{filename}.json", 'w') as f:
        json.dump(data, f, indent=2)

    with open(f"{filename}.csv", 'w') as f:
        for row in data:
            f.write(f"{row[1]}\n") # open price
            # f.write(f"{row[0]}, {row[1]}\n") # open time, open price
            # f.write("f{row[6]}, {row[4]}\n") # close time, close price
if __name__ == '__main__':
    download_historical_data('BTCUSDT', '2019-07-15')