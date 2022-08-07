COINS_SYMBOL = "BTCUSDT"

COIN_MAXIMUM_PRICE = 100000

START_DEPOSIT = 1000

LEVERAGE = 1
OPEN_POSITION_FEE_PERCENT = 0.01 * LEVERAGE
CLOSE_POSITION_FEE_PERCENT = 0.01 * LEVERAGE

USE_LONG_POSITIONS = True
USE_SHORT_POSITIONS = True

TAKE_PROFIT_PERCENTS_LIST = [1]
STOP_LOSS_PERCENTS_LIST = [-1] * len(TAKE_PROFIT_PERCENTS_LIST)

MOVING_AVERAGE_SIZE = 50

START_YEAR = 2022
START_MONTH = 1
START_DAY = 1
START_HOUR = 0
START_MINUTE = 0
START_SECOND = 0

END_YEAR = 2022
END_MONTH = 6
END_DAY = 1
END_HOUR = 0
END_MINUTE = 0
END_SECOND = 0

TIMEFRAME = "m1"
INDICATORS_TIMEFRAME = "m15"
IMPORTANT_RECENT_CANDLES_TIMEFRAME = "m15"
IMPORTANT_RECENT_CANDLES_COUNT = 256
OPEN_POSITION_TIMEFRAME = "m15"
ALL_TIMEFRAMES_LIST = ["m1", "m5", "m15", "m30", "h1", "h2", "h4", "d1", "w1"]

REPORT_PERCENTILES_COUNT = 20

TRAIN_CSV_FILE_PATH = "train_set.csv"
TEST_CSV_FILE_PATH = "test_set.csv"
CSV_FILE_DELIMITER = ","

PLOT_FILE_PATH = "plot.png"
POSITIONS_CSV_REPORT_FILE_PATH = "positions.csv"
DEPOSIT_CHANGES_CSV_REPORT_FILE_PATH = "deposit_changes.csv"

TEST_SET_SIZE_RATIO = 0.1

MINIMUM_NUMBER_OF_CANDLES_TO_START_TRADING = 256
