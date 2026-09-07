import pandas as pd,sqlite3
o=pd.read_csv('data/raw/orders.csv'); c=pd.read_csv('data/raw/customers.csv'); p=pd.read_csv('data/raw/products.csv')
o['payment_method']=o['payment_method'].fillna('Unknown'); o['quantity']=o['quantity'].clip(lower=1); o['net_sales']=o['net_sales'].clip(lower=0)
db=sqlite3.connect('warehouse/retail_dw.db'); o.to_sql('fact_sales',db,if_exists='replace',index=False); c.to_sql('dim_customer',db,if_exists='replace',index=False); p.to_sql('dim_product',db,if_exists='replace',index=False); db.close()
print('ETL completed')
