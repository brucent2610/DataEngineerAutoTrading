import os

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

SSI_API_KEY = os.getenv("SSI_API_KEY")
SSI_API_SECRET = os.getenv("SSI_API_SECRET")

if __name__ == "__main__": 
    print("Module Progress: app.py")
    print(BINANCE_API_KEY)
    print(BINANCE_API_SECRET)
    print(SSI_API_KEY)
    print(SSI_API_SECRET)

