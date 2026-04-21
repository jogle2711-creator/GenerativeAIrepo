import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Simulate hourly electricity usage for 7 days 
hours = pd.date_range("2026-04-01", periods=24*7, freq="h")
usage = np.random.randint(200, 800, size=len(hours)) # watts

df = pd.DataFrame({"time": hours, "usage_watts": usage})
print(df.head())

# Plot usage
plt.figure(figsize=(10,5))
plt.plot(df["time"], df["usage_watts"])
plt.title("Household Electricity Usage")
plt.xlabel("Time")
plt.ylabel("Watts")
plt.show()

# Find peak usage hours
peak_hours = df.groupby(df["time"].dt.hour)["usage_watts"].mean()
print("Average usage by hour:\n", peak_hours)

def suggest_optimizations(df):
    avg_usage = df.groupby(df["time"].dt.hour)["usage_watts"].mean()
    peak_hour = avg_usage.idmax()
    low_hour = avg_usage.idxmin

    return f"Peak usage is at {peak_hour}: 00. Consider running heavy appliances at {low_hour}: 00 to save energy and reduce costs."

print(suggest_optimizations(df))

from fastapi import FastAPI

app = FastAPI()

@app.get("/usage")
def get_usage():
    return df.to_dict(orient="records")

@app.get("/suggestions")
def get_suggestions():
    return {"suggestion": suggest_optimizations(df)}