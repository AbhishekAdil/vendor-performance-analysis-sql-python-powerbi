# Use this script to save csv files into database with their filename as tablename

import pandas as pd
from sqlalchemy import create_engine
import os
import time
import logging

# create logging

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

# create engine

engine = create_engine('sqlite:///inventory.db')

# create a function for ingestion
# this function will ingest the dataframe into database table

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace' , index = False)

'''This function will load the CSVs as dataframe and ingest into db'''

def load_raw_data():
    strat = time.time()
    for file in os. listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingestion {file} in db')
            ingest_db(df, file[-4], engine)
    end = time.time()
    total_time = (end - strat)/60
    logging.info('----Ingestion Complete----')
    logging.info(f'\nTotal Time Taken : {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()