import pandas as pd
import matplotlib.pyplot as plt
from database import get_events


def plot_monthly_budgets():
    df = get_events()
    if df.empty:
        return None

    df["Event_Date"] = pd.to_datetime(df["Event_Date"])
    df["Month"] = df["Event_Date"].dt.to_period("M")

    monthly = df.groupby("Month")["Budget"].sum()

    fig, ax = plt.subplots()
    monthly.plot(ax=ax, marker="o")
    ax.set_title("Monthly Event Budget Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Budget Spent")
    return fig
