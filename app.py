import streamlit as st
from database import *
from utils import search_by_date
from analytics import plot_monthly_budgets

st.set_page_config(page_title="🎉 Event Manager", layout="centered")
st.title("🎉 Event Management System")
st.markdown("Manage your events: Add, View, Update, Delete & Analyze")

menu = st.sidebar.radio(
    "Menu",
    ["Add Event", "View Events", "Search by Date", "Update Event", "Delete Event", "Event Trends"]
)

# Add Event
if menu == "Add Event":
    st.subheader("➕ Add New Event")
    with st.form("event_form"):
        eid = st.number_input("Event ID", min_value=1, step=1)
        name = st.text_input("Event Name")
        organizer = st.text_input("Organizer")
        etype = st.selectbox("Event Type", ["Conference", "Wedding", "Concert", "Festival"])
        budget = st.number_input("Budget", min_value=0.0, step=0.01)
        date = st.date_input("Event Date")

        submitted = st.form_submit_button("Add Event")

        if submitted:
            try:
                add_event(eid, name, organizer, etype, budget, date)
                st.success("Event added successfully!")
            except:
                st.error("Event ID already exists!")

# View Events
elif menu == "View Events":
    st.subheader("📋 All Events")
    df = get_events()
    if df.empty:
        st.info("No events available.")
    else:
        st.dataframe(df)

# Search by Date
elif menu == "Search by Date":
    event_date = st.date_input("Select Date")
    if st.button("Search"):
        df = search_by_date(str(event_date))
        if not df.empty:
            st.dataframe(df)
        else:
            st.warning("No events found.")

# Update Event
elif menu == "Update Event":
    df = get_events()
    if df.empty:
        st.info("No events to update.")
    else:
        eid = st.selectbox("Select Event ID", df["Event_ID"].tolist())
        field = st.selectbox("Field to update", ["Event_Name", "Organizer", "Event_Type", "Budget", "Event_Date"])
        new_value = st.text_input("Enter New Value")
        if st.button("Update"):
            rows = update_event(eid, field, new_value)
            if rows:
                st.success("Updated successfully!")

# Delete Event
elif menu == "Delete Event":
    df = get_events()
    if df.empty:
        st.info("No events to delete.")
    else:
        eid = st.selectbox("Select Event ID", df["Event_ID"].tolist())
        if st.button("Delete"):
            delete_event(eid)
            st.success("Event deleted!")

# Event Trend
elif menu == "Event Trends":
    st.subheader("📈 Monthly Event Budget Trend")
    fig = plot_monthly_budgets()
    if fig:
        st.pyplot(fig)
    else:
        st.info("Not enough data to show trends.")
