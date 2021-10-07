import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": [
        "Chocolate",
        "Granizado", 
        "Limon", 
        "Dulce de Leche"
    ], 
    "quantity": [3,10,0,5]
})

def is_product_available(product_name, quantity):
    resp = False

    temp = _PRODUCT_DF[_PRODUCT_DF["product_name"]==product_name].reset_index(drop=True)

    if len(temp) > 0: #Producto encontrado
        if temp["quantity"][0] >= quantity:
            resp = True

    return (resp)

p_name = "Chocolate"
p_quantity = 3
print(is_product_available(p_name,p_quantity))

