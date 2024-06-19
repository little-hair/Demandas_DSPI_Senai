import pandas as pd
import matplotlib.pyplot as plt
import requests

request = requests.get('https://github.com/little-hair/Demandas_DSPI_Senai/blob/main/Data.json?raw=true')

data = request.json()

table = pd.DataFrame(data)
table.to_html('demandas_DSPI.html', index=False)
table