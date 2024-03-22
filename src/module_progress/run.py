import os
import sys

# Get the directory that contains your current file (run.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create a path to the additional directories
models_directory = os.path.join(current_directory, 'models')
utils_directory = os.path.join(current_directory, 'utils')

# Add the additional directories to the system path
sys.path.append(models_directory)
sys.path.append(utils_directory)

from models.Binance import Binance
from models.SSI import SSI

from utils.utils import test

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

SSI_API_KEY = os.getenv("SSI_API_KEY")
SSI_API_SECRET = os.getenv("SSI_API_SECRET")

if __name__ == "__main__":
    print("Module Trading: app.py")
    print(BINANCE_API_KEY)
    print(BINANCE_API_SECRET)
    print(SSI_API_KEY)
    print(SSI_API_SECRET)

    binance = Binance()
    binance.load_data()

    ssi = SSI()
    ssi.load_data()

    test()

