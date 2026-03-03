

import pandas as pd




df = pd.read_csv(r"data/housing.csv")




df





from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:55432/housing')





#makes sure we only create the table, we don't add any data yet.
print(pd.io.sql.get_schema(df, name='housing', con=engine))





df.head(n=0).to_sql(name='housing', con=engine, if_exists='replace')




df_iter = pd.read_csv(
    r"data/housing.csv",

    iterator=True,
    chunksize=1000)





for df_chunk in df_iter:
    print(len(df_chunk))





for i, df_chunk in enumerate(df_iter):
    if i == 0:
        df_chunk.head(0).to_sql(name="housing", con=engine, if_exists="replace")

    df_chunk.to_sql(name="housing", con=engine, if_exists="append")
    print("Inserted:", len(df_chunk))







