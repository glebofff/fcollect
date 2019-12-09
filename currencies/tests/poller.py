from django.db import IntegrityError
from django.test import TestCase

from currencies.common.poller import PollerException, FetchException, AlreadyPolledException
from currencies.common.poller.base import BasePoller


class MockPoller(BasePoller):
    abbr = "MOCK"
    url = "http://127.0.0.1:9287"

    def fetch(self, *args):
        return """
        {
          "timestamp": 1575882001,
          "base": "USD",
          "rates": {
            "AED": 3.673,
            "AFN": 78.69964,
            "ALL": 110.846857,
            "AMD": 479.757841,
            "ANG": 1.720396,
            "AOA": 478.391,
            "ARS": 59.895248,
            "AUD": 1.465448,
            "AWG": 1.8,
            "AZN": 1.7025,
            "BAM": 1.768621,
            "BBD": 2,
            "BDT": 85.067227,
            "BGN": 1.7677,
            "BHD": 0.376994,
            "BIF": 1882.162698,
            "BMD": 1,
            "BND": 1.364109,
            "BOB": 6.936836,
            "BRL": 4.1415,
            "BSD": 1,
            "BTC": 0.000133797775,
            "BTN": 71.448483,
            "BWP": 10.856807,
            "BYN": 2.122801,
            "BZD": 2.022064,
            "CAD": 1.32625,
            "CDF": 1672.770017,
            "CHF": 0.990016,
            "CLF": 0.026239,
            "CLP": 783.899361,
            "CNH": 7.038925,
            "CNY": 7.0425,
            "COP": 3468.054432,
            "CRC": 567.789839,
            "CUC": 1,
            "CUP": 25.75,
            "CVE": 100.15,
            "CZK": 23.087699,
            "DJF": 178,
            "DKK": 6.753679,
            "DOP": 53.03703,
            "DZD": 119.9161,
            "EGP": 16.1298,
            "ERN": 14.999786,
            "ETB": 31.576615,
            "EUR": 0.903861,
            "FJD": 2.1735,
            "FKP": 0.759812,
            "GBP": 0.759812,
            "GEL": 2.94,
            "GGP": 0.759812,
            "GHS": 5.682868,
            "GIP": 0.759812,
            "GMD": 51.42,
            "GNF": 9572.450371,
            "GTQ": 7.704209,
            "GYD": 209.874724,
            "HKD": 7.82799,
            "HNL": 24.699551,
            "HRK": 6.7232,
            "HTG": 97.479314,
            "HUF": 299.702286,
            "IDR": 14013.5,
            "ILS": 3.46865,
            "IMP": 0.759812,
            "INR": 71.124495,
            "IQD": 1197.578982,
            "IRR": 42105.230176,
            "ISK": 121.479985,
            "JEP": 0.759812,
            "JMD": 140.55937,
            "JOD": 0.7094,
            "JPY": 108.49683333,
            "KES": 101.3,
            "KGS": 69.66952,
            "KHR": 4082.563273,
            "KMF": 445.950114,
            "KPW": 900,
            "KRW": 1192.13,
            "KWD": 0.303698,
            "KYD": 0.836009,
            "KZT": 387.141066,
            "LAK": 8886.36492,
            "LBP": 1516.750341,
            "LKR": 181.771032,
            "LRD": 189.625034,
            "LSL": 14.695121,
            "LYD": 1.407424,
            "MAD": 9.66216,
            "MDL": 17.350663,
            "MGA": 3698.596595,
            "MKD": 55.695917,
            "MMK": 1506.987137,
            "MNT": 2693.559976,
            "MOP": 8.089072,
            "MRO": 357,
            "MRU": 37.598228,
            "MUR": 36.596168,
            "MVR": 15.45,
            "MWK": 738.640959,
            "MXN": 19.26597,
            "MYR": 4.161001,
            "MZN": 63.986003,
            "NAD": 14.695121,
            "NGN": 363.892086,
            "NIO": 33.840937,
            "NOK": 9.13825,
            "NPR": 114.317489,
            "NZD": 1.526485,
            "OMR": 0.385002,
            "PAB": 1,
            "PEN": 3.389609,
            "PGK": 3.414929,
            "PHP": 50.848,
            "PKR": 155.463392,
            "PLN": 3.86729,
            "PYG": 6461.891766,
            "QAR": 3.652485,
            "RON": 4.3204,
            "RSD": 106.25,
            "RUB": 63.7765,
            "RWF": 937.277556,
            "SAR": 3.749088,
            "SBD": 8.235474,
            "SCR": 13.700289,
            "SDG": 45.253336,
            "SEK": 9.505174,
            "SGD": 1.360416,
            "SHP": 0.759812,
            "SLL": 7479.71008,
            "SOS": 580.36767,
            "SRD": 7.458,
            "SSP": 130.26,
            "STD": 21560.79,
            "STN": 22.28,
            "SVC": 8.777863,
            "SYP": 515.060169,
            "SZL": 14.695121,
            "THB": 30.301,
            "TJS": 9.71234,
            "TMT": 3.5,
            "TND": 2.8545,
            "TOP": 2.304745,
            "TRY": 5.804299,
            "TTD": 6.777954,
            "TWD": 30.4815,
            "TZS": 2308.248698,
            "UAH": 23.7912,
            "UGX": 3696.618194,
            "USD": 1,
            "UYU": 37.828111,
            "UZS": 9540.841025,
            "VEF": 248487.642241,
            "VES": 31174.355,
            "VND": 23240.067962,
            "VUV": 115.5355,
            "WST": 2.657455,
            "XAF": 592.893846,
            "XAG": 0.06021195,
            "XAU": 0.00068375,
            "XCD": 2.70255,
            "XDR": 0.72533,
            "XOF": 592.893846,
            "XPD": 0.00053257,
            "XPF": 107.859289,
            "XPT": 0.00112235,
            "YER": 250.349961,
            "ZAR": 14.6622,
            "ZMW": 15.272958,
            "ZWL": 322.000001
          }
        }
        """
        pass


class TestPoller(BasePoller):
    url = 'https://valid.but.nonexistent.url.de:3333'
    abbr = 'TST'

    def get_params(self):
        return {
            'a': 'b'
        }
    pass


class PollerTestCase(TestCase):
    def test_url_and_abbr_validation(self):
        self.assertRaises(PollerException, TestPoller, url='invalid_url')

        try:
            poller = TestPoller(abbr='')
            self.fail("Creating pollers with empty abbr is prohibited.")
        except IntegrityError:
            pass

    def test_currency_validation(self):
        self.assertRaises(PollerException, TestPoller, base='XXXXXX')

    def test_source_creation(self):
        poller = TestPoller()
        self.assertIsNotNone(poller.src)
        self.assertEqual(poller.src.abbr, poller.abbr)

    def test_fetch_error(self):
        poller = TestPoller()
        self.assertRaises(FetchException, poller.fetch, force=True)

    def test_already_polled(self):
        poller = MockPoller()
        poller.poll()

        self.assertRaises(AlreadyPolledException, poller.poll)

    def test_unique_data(self):
        poller = MockPoller()
        poller.poll()
        try:
            poller.poll(force=True)
            self.fail('Should be unique constraint error here')

        except IntegrityError:
            pass


