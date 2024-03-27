class BollingerBands:

    def __init__(self, window=20, window_rsi=14):
        self._window = window
        self._window_rsi = window_rsi

    def _compute_rsi(self, data):
        delta = data.diff()
        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        gain = up.rolling(window=self._window_rsi).mean()
        loss = down.abs().rolling(window=self._window_rsi).mean()
        RS = gain / loss
        return 100 - (100 / (1 + RS))

    def apply(self, data):
    
        # Tính toán SMA và độ lệch chuẩn cho giá đóng cửa
        data['SMA'] = data['Close'].rolling(window=self._window).mean()
        data['STD'] = data['Close'].rolling(window=self._window).std()

        # Tính toán Bollinger Bands
        data['Upper_Band'] = data['SMA'] + (data['STD'] * 2)
        data['Lower_Band'] = data['SMA'] - (data['STD'] * 2)

        data['RSI'] = self._compute_rsi(data['Close'])

        # Xác định tín hiệu mua
        data['Buy_Signal'] = ((data['Close'] <= data['Lower_Band']) & (data['RSI'] < 30)) # & ((np.maximum(data['Open'], data['Close'])) >= data['Lower_Band']))

        # Xác định tín hiệu bán
        data['Sell_Signal'] = ((data['Close'] >= data['Upper_Band']) & (data['RSI'] > 70))

        return data
    
    def to_csv(self, data, name="default.csv", path='data/'):
        data.to_csv(path + name)