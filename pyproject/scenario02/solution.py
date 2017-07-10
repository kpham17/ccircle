# Your solution goes in this file!
import statistics

'''
  --- ACCOUNT ------------------------------------------------------------------

    account.getBalance() -> Real Number

      Get the amount of money in your account

    account.getShares(sym) -> Integer

      Get the number of shares of the given stock that you currently own

  --- MARKET -------------------------------------------------------------------

    market.buy(account, sym, quantity) -> None

      Buy 'quantity' shares of the stock with symbol 'sym' using 'account'
      You must have enough money in your account or the function will fail!

    market.getPrice(sym) -> Real Number

      Return the current price of the given stock

    market.getHistory(sym) -> List

      Return a list of historical prices for the given stock

    market.getStockSymbols() -> List

      Return a list of all the stock symbols

    market.sell(account, sym, quantity) -> None

      Sell 'quantity' shares of the stock with symbol 'sym' using 'account'
      You must have enough shares in your account or the function will fail!
'''

class StockTrader:
    def __init__(self):
        # Set variables if you want
        self.days = 0
        self.stockLast = [[],[] ,[],[],[],[],[],[]]
        self.stockMean=[0,0,0,0,0,0,0,0]
        self.stockVal = [0,0,0,0,0,0,0,0]
        self.max = [0,0,0,0,0,0,0,0]
        self.min = [0,0,0,0,0,0,0,0]
        self.distance = [0,0,0,0,0,0,0,0]]

        pass

    # Controls how difficult the simulation is:
    #    0.0 -> easiest
    #    0.5 -> moderate
    #    1.0 -> hardest
    def getDifficulty(self):
        return 0.2

    # Controls how fast the simulation runs; 0 = fastest
    def getPauseTime(self):
        return 0.1

    # Use different numbers to get different random variations of the simulation
    def getSeed(self):
        return 1337

    # Analyze the market for the current day and make trades as you see fit. Try to make as much money as you can!
    def trade(self, account, market):
        # This is a very basic and bad starter strategy: get a list of stocks, buy any stock that is less than $10
        # (if we can afford it); sell any stock that is more than $20 (if we own it). You must do better than this!
        self.days += 1
        syms = market.getStockSymbols()
        for sym in syms:
            a = syms.index(sym)
            price = market.getPrice(sym)
            self.stockVal.append(price)
            self.stockLast[a]=self.stockVal
            if len(self.stockVal) > 150:
                del self.stockVal[0]
            self.max[a] = max(self.stockVal)
            self.min[a] = min(self.stockVal)
            self.distance[a] = self.max - self.min
            self.average[a] = statistics.mean(self.stockVal)
        print(self.min)
        print(self.max)
        print(self.distance)
        print(self.average)
        if self.days >= 150:
            for sym in syms:
                price = market.getPrice(sym)


