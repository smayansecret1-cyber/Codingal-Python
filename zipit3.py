print("\n")

print("\n")

stocks = ['reliance', 'infosys', 'tcs']

prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,

prices in zip(stocks, prices)}

print('\n{}'.format(new_dict))

print("\n")

print("\n")