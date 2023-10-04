mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'UK'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchange_rate': 107.25
            }

for phone in mobile_data['data']:
    price_usd = float(phone['price'].replace(' USD', ''))
    price_bdt = round(price_usd * mobile_data['exchange_rate'])
    print(f"{phone['name']} is made in {phone['made']}. The price is {price_usd} USD which is almost equal to {price_bdt} BDT.")
