# cop-3701-crime-analytics
Database project about crime data for COP3701.



### Project Scope (tentative)
A crime analytics database tracking:
- incidents
- locations
- severity

Hotspot ranking and temporal crime pattern analysis will be included.

 

### Users
- Police officers
- Crime analysts

 

### Data Source(s)
https://www.kaggle.com/datasets/murderaccountability/homicide-reports


## Database Application Proposal

This project is a crime analytics database that tracks incidents, locations, and severity. The system is designed to support hotspot ranking and temporal crime pattern analysis.

The ER design includes strong entities such as INCIDENT, LOCATION, and CRIME_TYPE, along with an associative entity to model a many-to-many relationship and a weak entity to track incident updates. The structure supports both operational record keeping and analytical queries over time and by location.

A key challenge is keeping the schema normalized while still supporting analytics (hotspot ranking and temporal patterns), and correctly modeling many-to-many relationships using an associative entity.


