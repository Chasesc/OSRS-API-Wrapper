class PriceTrend(object):

    _money_shorthands = {"k": 1000, "m": 1000000, "b": 1000000000}

    def __init__(self, price, trend, change):
        self.price = self._extract_price(price)
        self.trend = trend
        self.change = self._extract_change(change)

    def _extract_price(self, price):
        if price is None:
            return None

        price = str(price).replace(" ", "").replace(",", "")

        last = price[-1]  # Get the last character
        # check if this price is in shorthand notation. EX. '1.6m'
        if last in PriceTrend._money_shorthands.keys():
            # if it is, convert it to be a floating point num.
            # EX. '1.6m' -> 1000000 * 1.6 -> 1600000.0
            return PriceTrend._money_shorthands[last] * float(price[:-1])

        return float(price)

    def _extract_change(self, change):
        if change is None:
            return None

        return float(change[:-1])

    def __str__(self):
        v = vars(self)
        details = ", ".join([f"{n}={v}" for n, v in v.items() if v is not None])
        return f"PriceTrend({details})"

    def __repr__(self):
        return self.__str__()


def main():
    pt = PriceTrend(" 1,320k", "neutral", "+5.0%")
    print(str(pt))


if __name__ == "__main__":
    main()
