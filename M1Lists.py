prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)
price_max = max(prices)
print(price_max)
names = ['Apple Inc', 'Coca-Cola', 'Walmart']
names.append('Amazon.com')
print(names)
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)
max_price = max(prices)
max_index = prices.index(max_price)
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')
