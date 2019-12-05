from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from currencies.common import CurrencyCode
from currencies.utils import to_decimal


class ConversionException(Exception):
    pass


class ConvertCurrencyView(TemplateView):
    """
    Currency converter JSON View:

    URL:
        /currencies/convert?src=czk&dst=pln&amount=155

    Required params:
        src: source currency code
        dst: destination currency code

    Optional params:
        amount: amount in source currency

    Result:
        {
            "ok": true,
            "rate": "0.16751",
            "result": "25.96405",
            "src": "CZK",
            "dst": "PLN",
            "amount": "155.00000"
        }
    """

    def get(self, request, *args, **kwargs):
        from django.db import connection
        from django.http import JsonResponse

        payload = {
            'src': request.GET.get('src', '').upper(),
            'dst': request.GET.get('dst', '').upper(),
            'amount': to_decimal(request.GET.get('amount') or 1)
        }

        result = {
            'ok': True,
            'rate': None,
            'result': None
        }
        result.update(payload)

        try:
            for code in ['src', 'dst']:
                if not CurrencyCode.is_valid(payload[code]):
                    raise ConversionException(f'Invalid {code} code "{payload[code]}"')

            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    select 
                      distinct dst.rate / src.rate as rate 
                    from 
                      currencies_ratelog src
                    join 
                      currencies_ratelog dst on dst.ts=src.ts and dst.source_id=src.source_id and dst.code != src.code
                    where 
                      src.code = %s 
                      and dst.code = %s
                      and src.ts = (
                        select ts from currencies_ratelog where source_id = src.source_id order by ts desc limit 1
                      )
                    """,
                    [
                        payload['src'],
                        payload['dst']
                    ]
                )
                r = cursor.fetchone()
                rate = r and to_decimal(r[0])

            if not rate:
                raise ConversionException('Exchange rate not found')

            result['rate'] = rate
            result['result'] = to_decimal(rate * payload['amount'])

        except Exception as e:
            result['ok'] = False
            result['error'] = f'{e}'

        return JsonResponse(result)




