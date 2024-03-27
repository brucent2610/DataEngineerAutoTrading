from strategies.Strategies import Strategies

class LongLeggedDoji(Strategies):

    def __init__(self, threshold=0.1):
        self._threshold = threshold

    # Định nghĩa hàm để kiểm tra nến Doji chân dài
    def _is_long_legged_doji(self, row):
        body_range = abs(row['Close'] - row['Open']) # Doji khong phan biet Open > Close hay Close > Open
        upper_shadow = row['High'] - max(row['Open'], row['Close'])
        lower_shadow = min(row['Open'], row['Close']) - row['Low']
        # Điều chỉnh ngưỡng này theo dữ liệu cụ thể của bạn
        doji_threshold = self._threshold / 100 * row['Close']
        return body_range <= doji_threshold and upper_shadow >= 2 * body_range and lower_shadow >= 2 * body_range
    
    # Định nghĩa hàm để kiểm tra nến tăng
    def _is_bullish_candle(self, current_row, previous_row):
        return (current_row['Close'] > current_row['Open'] and
                current_row['Close'] > previous_row['Close'] and
                previous_row['Close'] <= previous_row['Open'])
    
    # Định nghĩa hàm để kiểm tra nến giảm
    def _is_bearish_candle(self, current_row, previous_row):
        return (current_row['Close'] < current_row['Open'] and
                current_row['Close'] < previous_row['Close'] and
                previous_row['Close'] >= previous_row['Open'])


    def apply(self, data):

        data['Buy_Signal'] = False
        data['Sell_Signal'] = False 
    
        for i in range(0, len(data)): # Chi lay 2 nen
            current_row = data.iloc[i]
            previous_row = data.iloc[i - 1]
            
            # Kiểm tra nến hiện tại có phải là nến tăng và nếu nến trước đó là nến Doji chân dài
            if self._is_bullish_candle(current_row, previous_row) and self._is_long_legged_doji(previous_row):
                # Nếu thỏa mãn cả ba điều kiện, thêm ngày vào danh sách tín hiệu mua
                data.at[current_row.name, 'Buy_Signal'] = True

            if self._is_bearish_candle(current_row, previous_row) and self._is_long_legged_doji(previous_row):
                data.at[current_row.name, 'Sell_Signal'] = True

        return data