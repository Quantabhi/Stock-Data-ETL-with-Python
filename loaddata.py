from sqlalchemy import create_engine
import yfinance as yf
import pandas as pd
import urllib.parse

# Credentials
db_user = 'postgres'
db_password = 'xxxx'
db_host = 'db.xxx.supabase.co'
db_port = 'xxx'
db_name = 'postgres'

# URL encode the password
encoded_password = urllib.parse.quote_plus(db_password)

# Create SQLAlchemy engine
engine = create_engine(f'postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}')

# Download stock data
ticker = "SBIN.NS"
df = yf.download(ticker, start="2024-01-01", end="2024-12-31")

# Keep only Date and Close columns
df = df[['Close']]
df.reset_index(inplace=True)  # this adds the Date column from index to the DataFrame

# Upload to Supabase
df.to_sql('sbin_stock', engine, if_exists='replace', index=False)
print("✅ Stock data (Date & Close) uploaded successfully to Supabase PostgreSQL!")
