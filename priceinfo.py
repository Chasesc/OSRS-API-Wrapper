class PriceInfo(object):
    def __init__(
        self, curr_trend, trend_today, trend_30, trend_90, trend_180, osbuddy_price
    ):
        self.curr_trend = curr_trend
        self.trend_today = trend_today
        self.trend_30 = trend_30
        self.trend_90 = trend_90
        self.trend_180 = trend_180
        self.osbuddy_price = osbuddy_price

    def price(self):
        if not self.osbuddy_price:
            return self.curr_trend.price
        return self.osbuddy_price
