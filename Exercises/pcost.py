def portfolio_cost(filename):
    with open(filename, 'r') as f:
        total_price = 0.0
        for line in f:
            line = line.split()
            try:
                shares = int(line[1])
                purchase_price = float(line[2])
                total_price = total_price + (shares *  purchase_price)
            except ValueError as e:
                print("Couldn't parse", line)
                print("Reason:", e)
    return total_price

if __name__ == '__main__':
    print(portfolio_cost("../Data/portfolio.dat"))