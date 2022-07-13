'''Agregar a Ventas si se desea normalizar 'mql_id' de alfanumerico a numerico'''
df35= pd.DataFrame(ventas['mql_id'].unique())
df35.columns =['mql_id']
df35.columns.name='Imql_id'
df35['mql_idN']=np.arange(1,len(df35)+1)
clienteMercadeoNorma=df35
Ventas= clienteMercadeoNorma.mql_id.value_counts().index
Ventas_page_unique = ventas.mql_id.unique()
normalized = []
def get_matches(query,choices):
    for i in query:
        tuple = process.extractOne(i,choices)
        normalized.append(tuple[0])
    return normalized
Ventas_page_correg = get_matches(Ventas_page_unique, Ventas)
mydict = {Ventas_page_unique[i]: clienteMercadeoNorma[clienteMercadeoNorma['mql_id']==Ventas_page_correg[i]]['mql_idN'] for i in range(0,842)}
ventas =ventas.convert_dtypes()
ventas["IdmqlN"] = ventas["mql_id"].map(mydict)
df36 =ventas["IdmqlN"]
df37=list(df36.astype(str))
df36=np.arange(len(df36))
lindice=[]
for i in df36 :
    cadena=df37[i].split("\n")
    indice=cadena[0].split(" ")
    lindice.append(indice[4])
ventas["IdmqlN"]=lindice
ventas.drop(['mql_id'], axis=1, inplace=True)
ventas.rename(columns={'IdmqlN': 'mql_id'}, inplace=True)
'''Agregarlo antes de cambiar los tipos de dato'''