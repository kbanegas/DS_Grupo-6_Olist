''' ingestamos en un dataframe los clientes calificados de marketing a partir 
de las columnas landing_page_id y origen obtenemos dos tablas con valores unicos para la normalizacion de estos campos'''

df10= pd.read_csv(r'"~/ip_files/olist_marketing_qualified_leads_dataset.csv', sep=',')
'''Creamos una tabla para normalizar los id de pagina alfanumericos'''
df20= pd.DataFrame(df10['landing_page_id'].unique())
df20.columns =['landing_page_id']
df20.columns.name='IdPage'
df20['IdPages']=np.arange(1,len(df20)+1)
df20.to_csv("~/ip_files/olist_landing_page_id_Normalizada.csv")
'''Creo una columna Idlanding para sustituir el campo landing_page_id alfanumerico por un valor numerico'''
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
landing = df20.landing_page_id.value_counts().index
landing_page_unique = df10.landing_page_id.unique()
normalized = []
def get_matches(query,choices):
    for i in query:
        tuple = process.extractOne(i,choices)
        normalized.append(tuple[0])
    return normalized
landing_page_correg = get_matches(landing_page_unique, landing)
mydict = {landing_page_unique[i]: df20[df20['landing_page_id']==landing_page_correg[i]]['IdPages'] for i in range(0,495)}
df10 = df10.convert_dtypes()
df10["Idlanding"] = df10["landing_page_id"].map(mydict)
df31 =df10['Idlanding']
df32=list(df31.astype(str))
df31=np.arange(len(df31))
lindice=[]
for i in df31 :
    cadena=df32[i].split("\n")
    indice=cadena[0].split(" ")
    lindice.append(indice[4])
df10['IdLandingN']=lindice
df10.drop(['landing_page_id','Idlanding'], axis=1, inplace=True)
df10.rename(columns={'IdLandingN': 'landing_page_id'}, inplace=True)
'''Creo una columna IdOrigin para sustituir el campo Origin alfanumerico por un valor numerico'''
df10['origin'].fillna('unknown',inplace=True)
df21=pd.DataFrame(df10['origin'].unique())
df21.columns =['Origin']
df21.columns.name='IdOrigin'
df21['IdPages']=np.arange(1,len(df21)+1)
df21.to_csv("~/ip_files/olist_IdOrigin_Normalizada.csv")
#comparo y sustituyo
Origin = df21.Origin.value_counts().index
Origin_unique = df10.origin.unique()
normalized = []
def get_matches(query,choices):
    for i in query:
        tuple = process.extractOne(i,choices)
        normalized.append(tuple[0])
    return normalized
Origin_correg = get_matches(Origin_unique, Origin)
mydict = {Origin_unique[i]: df21[df21['Origin']==Origin_correg[i]]['IdPages'] for i in range(0,10)}
df10 = df10.convert_dtypes()
df10["IdOrigin"] = df10["origin"].map(mydict)
df33 =df10['IdOrigin']
df34=list(df33.astype(str))
df33=np.arange(len(df33))
lindice=[]
for i in df33 :
    cadena=df34[i].split("\n")
    indice=cadena[0].split(" ")
    lindice.append(indice[4])
df10['IdOriginN']=lindice
df10.drop(['origin','IdOrigin'], axis=1, inplace=True)
df10.rename(columns={'IdOriginN': 'IdOrigin'}, inplace=True)
'''creacion de tabla con valores unicos para normalización'''
df35= pd.DataFrame(df10['mql_id'].unique())
df35.columns =['mql_id']
df35.columns.name='Imql_id'
df35['mql_idN']=np.arange(1,len(df35)+1)
df35.to_csv("~/ip_files/olist_mql_idN_Normalizada.csv")
'''Creo una columna mql_idN para sustituir el campo mql_id alfanumerico por un valor numerico'''
df10['mql_idN']=np.arange(1,len(df10)+1)
df10.drop(['mql_id'], axis=1, inplace=True)
df10.rename(columns={'mql_idN': 'mql_id'}, inplace=True)
'''Cambiar el tipo de datos a las columnas'''
df10['first_contact_date'] = pd.to_datetime(df10['first_contact_date'])
df10['landing_page_id'] = pd.to_numeric(df10['landing_page_id'])
df10['IdOrigin'] = pd.to_numeric(df10['IdOrigin'])
df10['mql_id'] = pd.to_numeric(df10['mql_id'])
'''levar a csv ya normaliza'''
df10.to_csv("~/ip_files/olist_marketing_qualified_leads_dataset_Normalizada.csv")