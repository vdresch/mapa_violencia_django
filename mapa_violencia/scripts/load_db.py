from mapa.models import Crime, Bairro
from scripts.process_data import process
import pandas as pd
import re
import numpy as np
import locale
import datetime

locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')

#Process csv files, before uploading to db
process()

def run():
    processed_data = pd.read_pickle('scripts/data/processed_data.pkl')
    bairros_metadata = pd.read_pickle('scripts/data/bairros_metadata.pkl')

    Crime.objects.all().delete()
    Bairro.objects.all().delete()

    bairros_metadata['Área'] = bairros_metadata['Área'].apply(lambda x: re.findall('\d+\.?\d*', x)[0] if pd.notna(x) else np.nan)
    bairros_metadata['Densidade'] = bairros_metadata['Densidade'].apply(lambda x: re.findall('\d+\.?\d*', x)[0] if pd.notna(x) else np.nan)
    bairros_metadata['Renda média por \ndomicílio'] = bairros_metadata['Renda média por \ndomicílio'].apply(lambda x: re.findall('\d+\.?\d*', x)[0] if pd.notna(x) else np.nan)
    bairros_metadata['Data de \nCriação'] = bairros_metadata['Data de \nCriação'].apply(lambda x: datetime.datetime.strptime(x, '%d %b %Y'))

    bairros_metadata = bairros_metadata.drop_duplicates(subset=['Bairro'], keep='first')

    bairros_metadata = bairros_metadata.fillna(0)

    i = 1

    for row in bairros_metadata.iterrows():
        print(i, " de ", len(bairros_metadata))
        i += 1
        Bairro.objects.get_or_create(
            bairro=row[1]['Bairro'], 
            date_creation=row[1]['Data de \nCriação'],
            area=row[1]['Área'],
            population=row[1]['População\n2010'],
            density=row[1]['Densidade'],
            income=row[1]['Renda média por \ndomicílio']
            )


    processed_data['Data Fato'] = processed_data['Data Fato'].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
    processed_data['Hora Fato'] = processed_data['Hora Fato'].apply(lambda x: datetime.datetime.strptime(x, '%H:%M:%S'))

    i = 1

    for row in processed_data.iterrows():
        print(i, " de ", len(processed_data))
        i += 1
        Crime.objects.get_or_create(
            bairro=row[1]['Bairro'], 
            local_fato=row[1]['Local Fato'],
            enquadramento=row[1]['Tipo Enquadramento'],
            date=row[1]['Data Fato'],
            time=row[1]['Hora Fato']
            )