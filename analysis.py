import pandas as pd


df = pd.read_csv("data/transactions.csv")


print(df.shape)
print(df.head())

print("\nOverall Status Count")
print(df["status"].value_counts())

print("\nFailure Rate (%)")
print(df["status"].value_counts(normalize=True)*100)

print("\nFailures by Bank")
print(df[df.status=="FAILED"]["bank_name"].value_counts())

print("\nFailures by Payment Mode")
print(df[df.status=="FAILED"]["payment_mode"].value_counts())

print("\nTop Failure Reasons")
print(df["failure_reason"].value_counts())

df["hour"]=pd.to_datetime(df["transaction_time"]).dt.hour

print("\nFailures by Hour")
print(df[df.status=="FAILED"]["hour"].value_counts().sort_index())

bank_kpi = (
    df.groupby("bank_name")
      .agg(
          total_txn=("transaction_id", "count"),
          failures=("status", lambda x: (x == "FAILED").sum())
      )
      .reset_index()
)

bank_kpi["failure_rate_%"] = (bank_kpi["failures"] / bank_kpi["total_txn"]) * 100
mode_kpi = (
    df.groupby("payment_mode")
      .agg(
          total_txn=("transaction_id", "count"),
          failures=("status", lambda x: (x == "FAILED").sum())
      )
      .reset_index()
)

mode_kpi["failure_rate_%"] = (mode_kpi["failures"] / mode_kpi["total_txn"]) * 100
city_kpi = (
    df.groupby("city")
      .agg(
          total_txn=("transaction_id", "count"),
          failures=("status", lambda x: (x == "FAILED").sum())
      )
      .reset_index()
)

city_kpi["failure_rate_%"] = (city_kpi["failures"] / city_kpi["total_txn"]) * 100
bank_kpi.to_csv("data/bank_kpi.csv", index=False)
mode_kpi.to_csv("data/mode_kpi.csv", index=False)
city_kpi.to_csv("data/city_kpi.csv", index=False)
