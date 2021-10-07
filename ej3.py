_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021",
"Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    is_valid = False
    index = 0
    while (is_valid == False) and (index < len(_AVAILABLE_DISCOUNT_CODES)):
        total = 0

        for char in "".join(dict.fromkeys(discount_code)):
            if not char in _AVAILABLE_DISCOUNT_CODES[index]:
                total += 1
                if total>3: break

        if total < 3:
            for char in "".join(dict.fromkeys(_AVAILABLE_DISCOUNT_CODES[index])):
                if not char in discount_code:
                    total += 1
                    if total >3: break

        if total < 3:
            is_valid = True
        else:
            index += 1

    return (is_valid)                         

code = 'primavera2021'
print(validate_discount_code(code))