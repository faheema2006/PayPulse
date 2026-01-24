import pandas as pd
import random
from datetime import datetime, timedelta

rows=[]
banks=["SBI","HDFC","ICICI","Axis","PNB"]
modes=["UPI","Debit Card","Credit Card"]
cities=["Delhi","Mumbai","Bangalore","Chennai","Hyderabad"]
reasons=["Timeout","Server Error","Insufficient Funds","Network Issue",None]

start=datetime(2025,1,1)

for i in range(15000):
    t=start+timedelta(minutes=random.randint(0,43200))
    status="FAILED" if random.random()<0.18 else "SUCCESS"
    rows.append([
        i+1,
        random.randint(1,4000),
        random.choice(banks),
        random.choice(modes),
        random.randint(10,5000),
        t,
        status,
        random.choice(reasons) if status=="FAILED" else None,
        random.choice(cities),
        random.choice(["Android","iOS"]),
        random.choice(["4G","5G","WiFi"])
    ])

df=pd.DataFrame(rows,columns=[
"transaction_id","user_id","bank_name","payment_mode","amount",
"transaction_time","status","failure_reason","city","device_type","network_type"
])

print("CSV file generated successfully!")
df.to_csv("data/transactions.csv", index=False)
