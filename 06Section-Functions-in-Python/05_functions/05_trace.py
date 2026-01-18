def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")
# Original: 100, Final with VAT: 110.0
# Original: 150, Final with VAT: 165.0
# Original: 200, Final with VAT: 220.0