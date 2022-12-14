from os.path import dirname, join
from pymt5pure.response import Response

this_dir = dirname(__file__)
stuff_dir = join(this_dir, "stuff")


def test_response():
    data = (
        "AUTH_START|RETCODE=0 Done|VERSION_ACCESS=3320|"
        "SRV_RAND=7a69e44f6d214cacd7a1d144d0b2f039|\r\n"
    ).encode("utf-16le")
    r = Response(data)
    assert r.cmd == "AUTH_START"
    assert r.params["RETCODE"] == "0 Done"
    assert r.params["VERSION_ACCESS"] == "3320"
    assert r.params["SRV_RAND"] == "7a69e44f6d214cacd7a1d144d0b2f039"


def test_response2():
    with open(join(stuff_dir, "symbol_next_output.txt"), "rb") as f:
        data = f.read()
    r = Response(data)
    assert r.cmd == "SYMBOL_NEXT"
    assert r.params["RETCODE"] == "0 Done"
    assert r.json == {
        "Symbol": "AUDCAD.stp",
        "Path": "FX Crosses\\AUDCAD.stp",
        "ISIN": "",
        "CFI": "",
        "Category": "",
        "Exchange": "",
        "Description": "Australian Dollar vs Canadian Dollar",
        "International": "",
        "Sector": "12",
        "Industry": "0",
        "Country": "",
        "Basis": "",
        "Source": "AUDCAD_STP",
        "Page": "",
        "CurrencyBase": "AUD",
        "CurrencyBaseDigits": "2",
        "CurrencyProfit": "CAD",
        "CurrencyProfitDigits": "2",
        "CurrencyMargin": "AUD",
        "CurrencyMarginDigits": "2",
        "Color": "4278190080",
        "ColorBackground": "4278190080",
        "Digits": "5",
        "Point": "0.00001000",
        "Multiply": "100000.00000000",
        "TickFlags": "1",
        "TickBookDepth": "0",
        "TickChartMode": "0",
        "SubscriptionsDelay": "15",
        "FilterSoft": "0",
        "FilterSoftTicks": "0",
        "FilterHard": "0",
        "FilterHardTicks": "0",
        "FilterDiscard": "0",
        "FilterSpreadMax": "0",
        "FilterSpreadMin": "0",
        "FilterGap": "0",
        "FilterGapTicks": "0",
        "TradeMode": "4",
        "TradeFlags": "2",
        "CalcMode": "0",
        "ExecMode": "2",
        "GTCMode": "0",
        "FillFlags": "2",
        "ExpirFlags": "15",
        "OrderFlags": "127",
        "Spread": "0",
        "SpreadBalance": "0",
        "SpreadDiff": "0",
        "SpreadDiffBalance": "0",
        "TickValue": "0.00000000",
        "TickSize": "0.00000",
        "ContractSize": "100000.00000000",
        "StopsLevel": "1",
        "FreezeLevel": "0",
        "QuotesTimeout": "0",
        "VolumeMin": "100",
        "VolumeMinExt": "1000000",
        "VolumeMax": "300000",
        "VolumeMaxExt": "3000000000",
        "VolumeStep": "100",
        "VolumeStepExt": "1000000",
        "VolumeLimit": "0",
        "VolumeLimitExt": "0",
        "MarginFlags": "0",
        "MarginInitial": "0.00000000",
        "MarginMaintenance": "0.00000000",
        "MarginInitialBuy": "1.00000000",
        "MarginInitialSell": "1.00000000",
        "MarginInitialBuyLimit": "0.00000000",
        "MarginInitialSellLimit": "0.00000000",
        "MarginInitialBuyStop": "0.00000000",
        "MarginInitialSellStop": "0.00000000",
        "MarginInitialBuyStopLimit": "0.00000000",
        "MarginInitialSellStopLimit": "0.00000000",
        "MarginMaintenanceBuy": "1.00000000",
        "MarginMaintenanceSell": "1.00000000",
        "MarginMaintenanceBuyLimit": "0.00000000",
        "MarginMaintenanceSellLimit": "0.00000000",
        "MarginMaintenanceBuyStop": "0.00000000",
        "MarginMaintenanceSellStop": "0.00000000",
        "MarginMaintenanceBuyStopLimit": "0.00000000",
        "MarginMaintenanceSellStopLimit": "0.00000000",
        "MarginLiquidity": "0.00000000",
        "MarginHedged": "0.00000000",
        "MarginCurrency": "0.00000000",
        "SwapMode": "1",
        "SwapLong": "-1.12000000",
        "SwapShort": "-8.58000000",
        "SwapFlags": "0",
        "Swap3Day": "3",
        "SwapYearDay": "360",
        "SwapRateSunday": "0.00000000",
        "SwapRateMonday": "1.00000000",
        "SwapRateTuesday": "1.00000000",
        "SwapRateWednesday": "3.00000000",
        "SwapRateThursday": "1.00000000",
        "SwapRateFriday": "1.00000000",
        "SwapRateSaturday": "0.00000000",
        "TimeStart": "0",
        "TimeExpiration": "0",
        "SessionsQuotes": [
            [{"Open": "1260", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1320"}],
            [],
        ],
        "SessionsTrades": [
            [{"Open": "1260", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1440"}],
            [{"Open": "0", "Close": "1320"}],
            [],
        ],
        "REFlags": "0",
        "RETimeout": "7",
        "IECheckMode": "0",
        "IETimeout": "7",
        "IESlipProfit": "2",
        "IESlipLosing": "2",
        "IEVolumeMax": "0",
        "IEVolumeMaxExt": "0",
        "PriceSettle": "0.00000",
        "PriceLimitMax": "0.00000",
        "PriceLimitMin": "0.00000",
        "PriceStrike": "0.00000",
        "OptionMode": "0",
        "FaceValue": "0.00",
        "AccruedInterest": "0.00",
        "SpliceType": "0",
        "SpliceTimeType": "0",
        "SpliceTimeDays": "0",
    }
