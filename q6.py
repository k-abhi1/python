cost_price=int(input("enter the cost price:"));
selling_price=int(input("enter the selling price:"));
profit=selling_price-cost_price;
print("profit is",profit);
if profit>0:
    print("profit is made");
else:
    print("loss is made");