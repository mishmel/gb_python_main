import sys
sale_amount = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(sale_amount + '\n')