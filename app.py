import pandas as pd 
import json
from tqdm import tqdm
from redisearch import Client, TextField, NumericField, Query
from time import sleep
from rediscluster import StrictRedisCluster

sleep(15)

nodes = [{'host': "173.17.0.2", 'port': "7000"}]
rc = StrictRedisCluster(startup_nodes=nodes, decode_responses=True)


client=Client('week1', conn=rc)
client.create_index([TextField('name'), TextField('surname'), TextField('job')])
dat = pd.read_csv("test.csv")


for idx, row in tqdm(dat.iterrows()):
	client.add_document(f"{row['index']}", replace=True, partial=True, name = f"{row['name']}", surname = f"{row['surname']}", job = f"{row['job']}")