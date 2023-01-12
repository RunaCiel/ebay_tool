from pandas_datareader.data import get_quote_yahoo
 
result = get_quote_yahoo('JPY=X')
ary_result = result["price"].values
price = ary_result[0]
 
print(price)