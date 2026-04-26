# cop-3701-crime-analytics
Database project about crime data for COP3701.



### Project Scope
A crime analytics database tracking:
- incidents
- locations
- severity
- perpetrators

Allows for viewing all crimes, searching for incidents by state, searching by perpetrators, viewing incident reports, and seeing how many incidents there's been for each type of crime. 
 

### Users
- Police officers
- Crime analysts

 

### Data Source(s)
https://www.kaggle.com/datasets/murderaccountability/homicide-reports



### ER Diagram
[Crime ER Model.pdf](https://github.com/user-attachments/files/26426601/Crime.ER.Model.pdf)



## Database Application Proposal

This project is a crime analytics database that tracks incidents, locations, and severity.

The ER design includes strong entities such as INCIDENT, LOCATION, and CRIME_TYPE, along with an associative entity to model a many-to-many relationship and a weak entity to track incident updates. The structure supports both operational record keeping and analytical queries over time and by location.

A key challenge is keeping the schema normalized while still supporting analytics (hotspot ranking and temporal patterns), and correctly modeling many-to-many relationships using an associative entity.



### How To Use
1. Open the GitHub Repository
2. Click the green **Code** button
3. Click the **Codespaces** tab. You need to be signed into GitHub to see this.
4. Click **Create codespace on main**
5. Run the setup file by pasting this into the terminal: **bash setup.sh**
6. Start the app by pasting this into the terminal: **streamlit run app.py**
7. Click **Open in Browser** on the popup
