prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]
stock_array = np.array([prices, earnings])
print(stock_array)
print(stock_array.shape)
print(stock_array.size)
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)
print(stock_array_transposed.shape)
print(stock_array_transposed.size)
prices = stock_array_transposed[:, 0]
print(prices)
earnings = stock_array_transposed[:, 1]
print(earnings)
company_1 = stock_array_transposed[0, :]
print(company_1)
prices_mean = np.mean(prices)
print(prices_mean)
prices_std = np.std(prices)
print(prices_std)
company_ids = np.arange(1, 8, 1)
print(company_ids)
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)