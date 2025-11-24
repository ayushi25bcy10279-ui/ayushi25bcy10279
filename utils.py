import pandas as pd
from database import con

def search_by_date(date):
    df = pd.read_sql_query(
        "SELECT * FROM events WHERE Event_Date = ?", con, params=(date,)
    )
    return df
