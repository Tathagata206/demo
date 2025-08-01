#Unique price
prices = [1200,899,899,1500,2100,2100,700]
unique_prices = list(set(prices))
print("Unique product prices:", unique_prices)
#Duplicate price
prices = [1200,899,899,1500,2100,2100,700]
duplicate_set = set()
for p in prices:
    if prices.count(p)>1:
        duplicate_set.add(p)
print(duplicate_set)
# Average price
avg_price = sum(prices)/len(prices)
print(avg_price)
#print prices above 1000
new_price_list = []
for p in prices:
    if p>1000:
        new_price_list.append(p)
print(new_price_list)