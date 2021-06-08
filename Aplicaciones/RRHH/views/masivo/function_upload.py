import pandas as pd
# openpyxl


def archivo():
	archivo = 'C:/Users/Santiago/Desktop/DATA.xlsx'
	d = pd.read_excel(archivo, sheet_name='Hoja1')
	df = pd.DataFrame(data=d)
	documents = []

	# for i in df['NOMBRE DOCUMENTO']:
	# 	# documents.append(i)
	# 	yield i

	return df

# r = archivo()
