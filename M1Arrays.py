prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]
prices_array = np.array(prices)
earnings_array = np.array(earnings)
print(prices_array)
print(earnings_array)
pe_array = np.array(prices_array/earnings_array)
print(pe_array)
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)
stock_array = np.array([prices, earnings])
print(stock_array)
print(stock_array.shape)
print(stock_array.size)
price_mean = np.mean(prices)
boolean_array = (prices > price_mean)
print(boolean_array)
above_avg = prices[boolean_array]
print(above_avg)
boolean_array = (sectors == 'Health Care')
print(boolean_array)
health_care = names[boolean_array]
print(health_care)
boolean_array = (sectors == 'Consumer Staples')
cs_names = names[boolean_array]
cs_pe = pe[boolean_array]
print(cs_names)
print(cs_pe)
it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)
print(it_pe_mean)
print(it_pe_std)
cs_pe_mean = np.mean(cs_pe)
cs_pe_std = np.std(cs_pe)
print(cs_pe_mean)
print(cs_pe_std)