import json
# ---part 1---
#find the station code for each city
with open ('stations.csv') as file:
    stationdata = file.readlines()
    for row in stationdata:
        if 'Seattle' in row:
            row.split(',')
            seattle_stationcode = row.strip().split(',')[2]
        if 'Cincinnati' in row:
            row.split(',')
            cincinnati_stationcode = row.strip().split(',')[2]
        if 'Maui' in row:
            row.split(',')
            maui_stationcode = row.strip().split(',')[2]
        if 'San Diego' in row:
            row.split(',')
            sandiego_stationcode = row.strip().split(',')[2]
        

# use station code to select all measurements belonging to it from the JSON file
with open ('precipitation.json','r') as file:
     precipitation = json.load(file) #list of dictionaries
     seattle_data = [] #create a variable with an empty list
     cincinnati_data = []
     maui_data = []
     sandiego_data = []
     for data in precipitation:
         if data["station"] == seattle_stationcode:
             seattle_data.append(data) # adding the data to each city list
         elif data["station"] == cincinnati_stationcode:
            cincinnati_data.append(data)
         elif data["station"] == maui_stationcode:
            maui_data.append(data)
         elif data["station"] == sandiego_stationcode:
            sandiego_data.append(data)


#create empty lists per city where the data will go into
seattle_total_monthly_precipitation = []
cincinnati_total_monthly_precipitation = []
maui_total_monthly_precipitation = []
sandiego_total_monthly_precipitation = []
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] # create a list representing each month to loop over
for month in months:
    x = 0
    for measurement_data in seattle_data:
        if f'2010-{month}' in measurement_data['date']:
            x += measurement_data['value'] # sum all the measurement for Seattle for each month 
    seattle_total_monthly_precipitation.append(x)
    for measurement_data in cincinnati_data:
        if f'2010-{month}' in measurement_data['date']:
            x += measurement_data['value'] 
    cincinnati_total_monthly_precipitation.append(x)
    for measurement_data in maui_data:
        if f'2010-{month}' in measurement_data['date']:
            x += measurement_data['value'] 
    maui_total_monthly_precipitation.append(x)
    for measurement_data in sandiego_data:
        if f'2010-{month}' in measurement_data['date']:
            x += measurement_data['value'] 
    sandiego_total_monthly_precipitation.append(x)


# save the results from seattle to a json file
with open ('seattle_total_monthly_precipitation.json', 'w') as outfile:
    json.dump(seattle_total_monthly_precipitation, outfile)

# ---part 2---
# Calculate the relative precipitation per month (percentage compared to the precipitation over the whole year)
seattle_yearly_precipitation = sum(seattle_total_monthly_precipitation)
seattle_relative_precipitation_month = [round((x/seattle_yearly_precipitation), ndigits = 2) for x in seattle_total_monthly_precipitation] 

cincinnati_yearly_precipitation = sum(cincinnati_total_monthly_precipitation)
cincinnati_relative_precipitation_month = [round((x/cincinnati_yearly_precipitation), ndigits = 2) for x in cincinnati_total_monthly_precipitation]

maui_yearly_precipitation = sum(maui_total_monthly_precipitation)
maui_relative_precipitation_month = [round((x/maui_yearly_precipitation), ndigits = 2) for x in maui_total_monthly_precipitation]

sandiego_yearly_precipitation = sum(sandiego_total_monthly_precipitation)
sandiego_relative_precipitation_month = [round((x/sandiego_yearly_precipitation), ndigits = 2) for x in sandiego_total_monthly_precipitation]

totalprecipitation = (seattle_yearly_precipitation + cincinnati_yearly_precipitation + maui_yearly_precipitation + sandiego_yearly_precipitation)
seattle_relative_yearly_precipitation = [round((x/totalprecipitation), ndigits = 2) for x in seattle_yearly_precipitation]
cincinnati_relative_yearly_precipitation = [round((x/totalprecipitation), ndigits = 2) for x in cincinnati_yearly_precipitation]
maui_relative_yearly_precipitation = [round((x/totalprecipitation), ndigits = 2) for x in maui_yearly_precipitation]
sandiego_relative_yearly_precipitation = [round((x/totalprecipitation), ndigits = 2) for x in sandiego_yearly_precipitation]

cities = ['Seattle', 'Cincinnati', 'Maui', 'San Diego']
station = [seattle_stationcode, cincinnati_stationcode, maui_stationcode, sandiego_stationcode]
states = ['WA', 'OH', 'HI', 'CA']
totalMonthlyPrecipitation = [seattle_total_monthly_precipitation, cincinnati_total_monthly_precipitation, maui_total_monthly_precipitation, sandiego_total_monthly_precipitation]
relativeMonthlyPrecipitation = [seattle_relative_precipitation_month, cincinnati_relative_precipitation_month, maui_relative_precipitation_month, sandiego_relative_precipitation_month]
totalYearlyPrecipitation = [seattle_yearly_precipitation, cincinnati_yearly_precipitation, maui_yearly_precipitation, sandiego_yearly_precipitation]
relativeYearlyPrecipitation = [seattle_relative_yearly_precipitation, cincinnati_relative_yearly_precipitation, maui_relative_yearly_precipitation, sandiego_relative_yearly_precipitation]

# ---part 3---
# Calculate the relative precipitation over the whole year compared to the other stations (i.e. what percentage of all the measured rain fell in Seattle?)
for i in range(4):
    
with open ('result.json', 'w') as outfile:
    json.dump(results, outfile)