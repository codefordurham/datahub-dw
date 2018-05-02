Data used on by the datahub-be site.
datahub_ingest.bin - comand file that ingest data into the datahub-be database
durham_ltdbacs_7016_tr.csv - Census tract data ingested into the datahub-be database  
durham_ltdbacs_7016_tr.sql - SQL command used to ingest durham_ltdbacs_7016_tr.csv 
into datahub-be database
durham_bgs9800.csv - Census blockgroup data ingested into the datahub-be database
durham_bgs9800.sql - SQL command used to ingest the durham_bgs9800.csv into 
datahub-be database 
durham_bgs1318.csv - Census blockgroup data ingested into the datahub-be database
durham_bgs1318.sql - SQL command used to ingest the durham_bgs1318.csv into
datahub-be database

Jupyter notebooks that generate the blockgroup data ingested into the datahub-be
database. It also generates the models and serializers for the datahub-be, and
generates json tables used in the affordablehousing frontend.
Concat_bgs1318.ipynb
Concat_bgs9800.ipynb

Models used in the datahub-be backend
models_bgs1318.py
models_bgs9800.py
models_ltdbacs7016tr.py

serializers used in the datahub-be backend
serializers_bgs1318.py
serializers_bgs9800.py
serializers_ltdbacs7016tr.py

Json tables used in by the affordablehousing frontend
ltdbacs_trts_vuemapmenu.json
bgs1318_vuemapmenu.json
bgs9800_vuemapmenu.json
bgs_vuemapmenu.csv

Data files used by the Jupyter notebooks
propsalesacs_1517_bgs.csv
propsalescompass_1314_bgs.csv
propsalesdec_9800_bgs.csv

singfamhouse_bgs00_2001.csv
singfamhouse_bgs_011818.csv
singfamhouse_bgs_100517.csv
singfamhouse_bgs_2001.csv

dec_pop_2000.csv
compass_pop_1314.csv
acs_pop_2016.csv

