import pandas as pd

import sqlalchemy as db
import psycopg2
data=pd.read_csv('GOOG.csv',parse_dates=['Date'],index_col='Date')


print(data.loc['2019-04-04':'2019-04-05'])
# d=data.Open.resample('M').mean()
d=data.Open.resample('10d').mean()
print(d.plot())


print(d.plot(kind="bar"))


# install :   pip install psycopg2
engine = db.create_engine('postgresql://admin_banglamm@banglamm:Monday87!@banglamm.postgres.database.azure.com:5432/metamodel_db_test')
ff=pd.read_sql_table("agencies",engine)


db1=pd.read_csv("NewAgency.csv")

# ff.to_csv("NewAgency.csv");


# db1.to_sql(
#     name='agencies',
#     con=engine,
#     index=False,
#     if_exists='append'
#     )






