class MAATG:
    def __init__(self, short_window, long_window, period=14, threshold=50):
        # Set time for MA and ATR
        self._short_window = short_window
        self._long_window = long_window

        # Set threshold for market volatility
        self._period = period
        self._threshold = threshold

    def apply(self, data):
    
        data.set_index('Datetime', inplace=True)

        data['MA_Fast'] = data['Close'].rolling(window=self._short_window).mean()
        data['MA_Slow'] = data['Close'].rolling(window=self._long_window).mean()

        # Calculate True Range (TR)
        data['prev_close'] = data['Close'].shift(1)  # Lấy giá đóng cửa của ngày trước đó
        data['high_low'] = data['High'] - data['Low']
        data['high_close'] = abs(data['High'] - data['prev_close'])
        data['low_close'] = abs(data['Low'] - data['prev_close'])
        data['TR'] = data[['high_low', 'high_close', 'low_close']].max(axis=1)

        # Calculate ATR
        data['ATR'] = data['TR'].rolling(window=self._period).mean()

        # Buy Signals
        data['Buy_Signal'] = (data['MA_Fast'] >= data['MA_Slow']) & (data['ATR'] <= self._threshold)

        # Sell Signals
        data['Sell_Signal'] = (data['MA_Fast'] < data['MA_Slow']) & (data['ATR'] <= self._threshold)

        return data
    
    def to_csv(self, data, name="default.csv", path='data/'):
        data.to_csv(path + name)