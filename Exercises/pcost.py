with open("../Data/portfolio.dat", 'r') as f:
    total_price = 0.0
    for line in f:
        line = line.split()
        share_x_purchase_price = int(line[1]) * float(line[2])
        total_price = total_price + share_x_purchase_price
print(total_price)