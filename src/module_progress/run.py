import os
import sys

from datetime import datetime, timedelta

# Get the directory that contains your current file (run.py)
current_directory = os.path.dirname(os.path.abspath(__file__))
# Create a path to the additional directories
models_directory = os.path.join(current_directory, 'models')
utils_directory = os.path.join(current_directory, 'utils')
strategies_directory = os.path.join(current_directory + "models/strategies", 'strategies')

# Add the additional directories to the system path
sys.path.append(models_directory)
sys.path.append(strategies_directory)
sys.path.append(utils_directory)

from models.Binance import Spot
from strategies.MAATG import MAATG
from strategies.BollingerBands import BollingerBands

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
BINANCE_SYMBOL = os.getenv("BINANCE_SYMBOL")
BINANCE_TIMEFRAME = os.getenv("BINANCE_TIMEFRAME")

SSI_API_KEY = os.getenv("SSI_API_KEY")
SSI_API_SECRET = os.getenv("SSI_API_SECRET")

if __name__ == "__main__":
    print("Module Trading: app.py")
    print(BINANCE_API_KEY)
    print(BINANCE_API_SECRET)
    print(BINANCE_SYMBOL)

    print(SSI_API_KEY)
    print(SSI_API_SECRET)

    from_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')  # Lấy ngày hôm qua
    to_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    binanceSpot = Spot()
    account_balance = binanceSpot.ohlcv(
        symbol=BINANCE_SYMBOL, 
        from_date=from_date, 
        to_date=to_date, 
        timeframe=BINANCE_TIMEFRAME
    )
    binanceSpot.to_csv(data=account_balance, name="ohlcv.csv")

    strategy_MAATG = MAATG(
        short_window=50, 
        long_window=200, 
        period=14, 
        threshold=50
    )
    strategy_MAATG_result = strategy_MAATG.apply(account_balance)
    strategy_MAATG.to_csv(data=strategy_MAATG_result, name="maatg.csv")

    strategy_bollinger_bands = BollingerBands(
        window=20, 
        window_rsi=14
    )
    strategy_bollinger_bands_result = strategy_bollinger_bands.apply(account_balance)
    strategy_bollinger_bands.to_csv(data=strategy_bollinger_bands_result, name="bollinger_bands.csv")

