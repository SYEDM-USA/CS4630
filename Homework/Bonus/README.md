#### Problem 1: 
Use Google Maps API to create a spatial visualization of the  coronavirus epidemiological dataset and show the count (of deaths) for all counties in US, through date X, X is user input. The Center for Systems Science and Engineering (CSSE) at Johns Hopkins University harvests Covid-19 data and makes it available to the public (perhaps you may already be familiar with CSSE’s online dashboard). The Covid-19 map output should include these items:
###### •	US map layer with state boundaries, with Zoom in/out. A legend or some that shows date X and your name
###### •	Markers @ the (centroids* of) counties with a label that shows count (of causalities) 

#### Problem 2: 
Extend Problem 1 - use ESRI shape files [see shapeData folder; Hint: install pyshp to help read this geometry file] to extract (county) centroids’ latitude/longitude
 
#### Problem 2: 
Extend Problem 1 (or 2) to a timeseries map, with a slider - as one drags the slider, date range expands with corresponding map update
