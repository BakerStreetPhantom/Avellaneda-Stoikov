import numpy 
import math
# VARIABLES
s = # INITIAL PRICE
q = # INVENTORY
gamma = # INVENTORY RISK AVERSION PARAMETER
sigma = # MARKET VOLATILITY
K = # ORDERBOOK LIQUIDITY PARAMETER
T = 1 # TERMINAL TIME
t = 0 # CURRENT TIME

#RESERVATION PRICE
res_price = s - (q*gamma*sigma*sigma*(T-t))

#SPREAD
spread = gamma*sigma*sigma*(T-t) + (2/gamma)*np.log(1 + (gamma/K))

#OPTIMAL QUOTES
bid_price = math.ceil(res_price - spread/2)
ask_price = math.floor(res_price + spread/2)

