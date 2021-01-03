sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}   


total_profit = round((float(sales["sell_value"]) - float(sales["cost_value"])) * float(sales["inventory"]))
print('the profit will be :', str(total_profit))

###########



