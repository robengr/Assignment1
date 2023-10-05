mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }
for mobile in mobile_data['data']:
    price_usd = float(mobile['price'].split()[0])
    price_bdt = round(price_usd * mobile_data['exchnage_rate'])
    print(f"{mobile['name']} is made in {mobile['made']}. The price is {price_usd} USD which is almost equal to {price_bdt} BDT.")