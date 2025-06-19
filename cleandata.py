from sqlalchemy import create_engine
import pandas as pd
import urllib.parse
import matplotlib.pyplot as plt

# Supabase credentials
db_user = 'postgres'
db_password = 'xxx'
db_host = 'db.xxx.supabase.co'
db_port = 'xxx'
db_name = 'postgres'

# URL-encode password
encoded_password = urllib.parse.quote_plus(db_password)

# SQLAlchemy engine
engine = create_engine(f'postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}')

# Read data from table
df = pd.read_sql('SELECT * FROM sbin_stock', engine)

# Plot the data 
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()




