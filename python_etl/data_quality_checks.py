import pandas as pd
o=pd.read_csv('data/raw/orders.csv');c=pd.read_csv('data/raw/customers.csv');p=pd.read_csv('data/raw/products.csv')
checks=[['Null payment',o.payment_method.isna().sum()],['Invalid quantity',(o.quantity<=0).sum()],['Negative sales',(o.net_sales<0).sum()],['Orphan customers',(~o.customer_id.isin(c.customer_id)).sum()],['Orphan products',(~o.product_id.isin(p.product_id)).sum()]]
pd.DataFrame(checks,columns=['check','issues']).to_csv('data/processed/data_quality_results.csv',index=False)
