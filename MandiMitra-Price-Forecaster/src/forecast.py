def forecast(prices):
    return {"signal":"wait" if prices[-1]<2000 else "sell_now"}
