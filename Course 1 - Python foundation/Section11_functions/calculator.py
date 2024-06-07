def tax_calculator(subtotal):
    taxpct = 0.06
    tax = round(subtotal * taxpct, 2)
    total = round(subtotal + tax, 2)
    lst = []
    lst.extend((subtotal, tax, total))
    return lst
