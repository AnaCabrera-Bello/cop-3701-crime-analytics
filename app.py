import streamlit as st
import mysql.connector
import pandas as pd

# App title
st.title("Crime Analytics App")

# Connect to MariaDB database
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1", #local
        user="crime_user", #Enter your user
        password="crimepass123", #Enter your password
        database="crime_analytics" #create the database
    )

# Run a SELECT query and return results as a dataframe
def run_select_query(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]  # column names
    cursor.close()
    conn.close()
    return pd.DataFrame(rows, columns=columns)

# Get all incidents with related info
def get_all_incidents():
    query = """
        SELECT
            i.INCIDENT_ID,
            i.INCIDENT_DATE,
            i.INCIDENT_SEVERITY,
            l.CITY,
            l.STATE,
            c.CRIME_NAME,
            p.PD_NAME
        FROM INCIDENT i
        JOIN LOCATION l
            ON i.LOCATION_ID = l.LOCATION_ID
        JOIN CRIME_TYPE c
            ON i.CRIME_TYPE_ID = c.CRIME_TYPE_ID
        JOIN POLICE_DEPARTMENT p
            ON i.PD_ID = p.PD_ID
        ORDER BY i.INCIDENT_DATE DESC
    """
    return run_select_query(query)

# Get incidents filtered by state
def get_incidents_by_state(state):
    query = """
        SELECT
            i.INCIDENT_ID,
            i.INCIDENT_DATE,
            i.INCIDENT_SEVERITY,
            l.CITY,
            l.STATE,
            c.CRIME_NAME
        FROM INCIDENT i
        JOIN LOCATION l
            ON i.LOCATION_ID = l.LOCATION_ID
        JOIN CRIME_TYPE c
            ON i.CRIME_TYPE_ID = c.CRIME_TYPE_ID
        WHERE UPPER(l.STATE) = UPPER(%s)
        ORDER BY i.INCIDENT_DATE DESC
    """
    return run_select_query(query, (state,))

# Get perpetrators involved in a specific incident
def get_perpetrators_by_incident(incident_id):
    query = """
        SELECT
            i.INCIDENT_ID,
            p.PERP_ID,
            p.PERP_FNAME,
            p.PERP_MNAME,
            p.PERP_LNAME,
            p.PERP_DOB
        FROM INCIDENT i
        JOIN INCIDENT_PERP ip
            ON i.INCIDENT_ID = ip.INCIDENT_ID
        JOIN PERPETRATOR p
            ON ip.PERP_ID = p.PERP_ID
        WHERE i.INCIDENT_ID = %s
    """
    return run_select_query(query, (incident_id,))

# Get incidents and their report dates
def get_incident_reports():
    query = """
        SELECT
            i.INCIDENT_ID,
            i.INCIDENT_DATE,
            i.INCIDENT_SEVERITY,
            r.FILE_DATE
        FROM INCIDENT i
        JOIN INCIDENT_REPORT r
            ON i.INCIDENT_ID = r.INCIDENT_ID
        ORDER BY r.FILE_DATE DESC
    """
    return run_select_query(query)

# Count how many incidents exist for each crime type
def get_crime_type_counts():
    query = """
        SELECT
            c.CRIME_NAME,
            COUNT(*) AS TOTAL_INCIDENTS
        FROM INCIDENT i
        JOIN CRIME_TYPE c
            ON i.CRIME_TYPE_ID = c.CRIME_TYPE_ID
        GROUP BY c.CRIME_NAME
        ORDER BY TOTAL_INCIDENTS DESC
    """
    return run_select_query(query)

# Main dropdown menu
menu = st.selectbox(#menu = the selected box
    "Main Menu",
    [
        "View All Incidents",
        "Search Incidents by State",
        "Show Perpetrators for an Incident",
        "View Incident Reports",
        "Count Incidents by Crime Type"
    ]
)

# Feature 1: show all incidents
if menu == "View All Incidents":
    st.subheader("All Incidents")
    df = get_all_incidents()
    st.dataframe(df, use_container_width=True, hide_index=True)

# Feature 2: search incidents by state
elif menu == "Search Incidents by State":
    st.subheader("Search Incidents by State")
    state = st.text_input("Enter state abbreviation")
    if st.button("Search"):
        df = get_incidents_by_state(state)
        st.dataframe(df, use_container_width=True, hide_index=True)

# Feature 3: show perpetrators for an incident
elif menu == "Show Perpetrators for an Incident":
    st.subheader("Perpetrators for an Incident")
    incident_id = st.number_input("Enter Incident ID", min_value=1, step=1)
    if st.button("Show Perpetrators"):
        df = get_perpetrators_by_incident(int(incident_id))
        st.dataframe(df, use_container_width=True, hide_index=True)

# Feature 4: view incident reports
elif menu == "View Incident Reports":
    st.subheader("Incident Reports")
    df = get_incident_reports()
    st.dataframe(df, use_container_width=True, hide_index=True)

# Feature 5: show crime type counts
elif menu == "Count Incidents by Crime Type":
    st.subheader("Incident Count by Crime Type")
    df = get_crime_type_counts()
    st.dataframe(df, use_container_width=True, hide_index=True)