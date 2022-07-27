import pandas as pd

# ruta file csv
rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"


def listaPeliculas(rutaFileCsv: str) -> str:
    if "csv" in rutaFileCsv:
        try:
            data = pd.read_csv(rutaFileCsv)
            subData = data[["Country", "Language", "Gross Earnings"]]
            tablaDinamica = subData.pivot_table(index=["Country", "Language"])
            return tablaDinamica.head(10)
        except:
            return f"Error al leer el archivo de datos."
    else:
        return f"Extensión inválida."


print(listaPeliculas(rutaFileCsv))
