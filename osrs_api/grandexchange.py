import urllib.request
import json
import warnings

from . import const
from .item import Item
from .pricetrend import PriceTrend
from .priceinfo import PriceInfo


class GrandExchange(object):
    # OSBuddy is an unofficial API, but it is more accurate than the offical API.
    # They give more significant figures than the offical API and the values
    # are closer to the actively traded prices.
    @staticmethod
    def _osbuddy_price(id):
        # TODO: remove this. OSBuddy no longer has a public API?
        warnings.warn(
            "OSBuddy no longer provides a public API. This functionality will be removed.",
            DeprecationWarning,
            stacklevel=2,
        )

        osb_uri = const.OSBUDDY_PRICE_URI + str(id)
        osb_price = None
        try:
            osb_response = urllib.request.urlopen(osb_uri)

            osb_data = osb_response.read()
            encoding = osb_response.info().get_content_charset("utf-8")
            osb_response.close()

            osb_json_data = json.loads(osb_data.decode(encoding))
            osb_price = osb_json_data["overall"]
        except Exception:
            pass  # oh well, price will just be less accurate

        return osb_price

    @staticmethod
    def item(id, try_osbuddy=False):
        uri = const.GE_BY_ID + str(id)

        try:
            response = urllib.request.urlopen(uri)
        except urllib.error.HTTPError:
            raise Exception("Unable to find item with id %d." % id)

        data = response.read()
        encoding = response.info().get_content_charset("utf-8")
        response.close()

        osb_price = None
        if try_osbuddy:
            osb_price = GrandExchange._osbuddy_price(id)

        json_data = json.loads(data.decode(encoding))["item"]

        name = json_data["name"]
        description = json_data["description"]
        is_mem = bool(json_data["members"])
        type = json_data["type"]
        type_icon = json_data["typeIcon"]

        # price info/trends
        current = json_data["current"]
        today = json_data["today"]
        day30 = json_data["day30"]
        day90 = json_data["day90"]
        day180 = json_data["day180"]

        curr_trend = PriceTrend(current["price"], current["trend"], None)
        trend_today = PriceTrend(today["price"], today["trend"], None)
        trend_30 = PriceTrend(None, day30["trend"], day30["change"])
        trend_90 = PriceTrend(None, day90["trend"], day90["change"])
        trend_180 = PriceTrend(None, day180["trend"], day180["change"])

        price_info = PriceInfo(
            curr_trend, trend_today, trend_30, trend_90, trend_180, osb_price
        )

        return Item(id, name, description, is_mem, type, type_icon, price_info)


def main():
    abyssal_whip_id = 4151
    whip = GrandExchange.item(abyssal_whip_id)
    print(whip.name, whip.description, whip.price(), sep="\n")

    rune_axe_id = Item.get_ids("rune axe")
    rune_axe = GrandExchange.item(rune_axe_id)
    print(rune_axe.name, rune_axe.description, rune_axe.price(), sep="\n")


if __name__ == "__main__":
    main()
