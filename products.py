products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	# p = []
	# p.append(name) # 把 name 放入 p
	# p.append(price) # 把 price 也同時放入 p
	# p = [name, price]
	products.append([name, price]) # 把 p 放入 products 清單中
print(products)

for p in products:
	print(p)