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

def is_product_available(product_name="", quantity=""):
    """ 
    Se debe dar la posibilidad de seguir el flujo sin necesidad de agregar un producto. 
    Una solucion es crear una instancia donde la función devuelva True.
    Se pueden aislar los casos posibles para luego realizar x acción.
    """  
    temp = _PRODUCT_DF[_PRODUCT_DF["product_name"]==product_name].reset_index(drop=True)
    resp = False
    if product_name == "" or quantity == "":
        # Corta el ciclo 
        resp = True
    else:
        if len(temp) == 0: 
            # Producto no válido
            pass
        else:
            if temp["quantity"][0] >= quantity:
                # El producto y el stock son válidos
                resp = True
            else:
                # El producto es válido pero no hay stock
                pass

    return (resp)

p_name = "Chocolate"
p_quantity = 3

# Se puede invocar la funcion sin parametros para simular una entrada exitosa
print(is_product_available()) 