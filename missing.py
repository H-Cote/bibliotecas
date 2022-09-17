import pandas as pd


def mv(df):
    
    """Obtenemos la cantidad de datos faltantes totales por columna y su porcentaje respecto al total de filas"""
    
    missing_values_count = pd.DataFrame(df.isnull().sum(), columns=['Missing'])
    
    missing_values_count["Porcent"]=missing_values_count.apply(lambda x: (x/df.shape[0])*100, axis=1)
    
    return missing_values_count 

