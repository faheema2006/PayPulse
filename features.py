import pandas as pd

df=pd.read_csv("transactions.csv")

df["failure_flag"]=(df["status"]=="FAILED").astype(int)

bank_kpi=df.groupby("bank_name").agg(
    total_txn=("transaction_id","count"),
    failures=("failure_flag","sum")
)
bank_kpi["failure_rate_%"]=(bank_kpi.failures/bank_kpi.total_txn)*100
bank_kpi.sort_values("failure_rate_%",ascending=False).to_csv("bank_kpi.csv")

mode_kpi=df.groupby("payment_mode").agg(
    total_txn=("transaction_id","count"),
    failures=("failure_flag","sum")
)
mode_kpi["failure_rate_%"]=(mode_kpi.failures/mode_kpi.total_txn)*100
mode_kpi.sort_values("failure_rate_%",ascending=False).to_csv("mode_kpi.csv")

city_kpi=df.groupby("city").agg(
    total_txn=("transaction_id","count"),
    failures=("failure_flag","sum")
)
city_kpi["failure_rate_%"]=(city_kpi.failures/city_kpi.total_txn)*100
city_kpi.sort_values("failure_rate_%",ascending=False).to_csv("city_kpi.csv")

print("KPI files saved successfully")
