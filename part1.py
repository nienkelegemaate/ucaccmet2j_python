import json
# ---part 1---
seattle_station = 'GHCND:US1WAKG0038'
# use station code to select all measurements belonging to it from the JSON file
with open ('precipitation.json','r') as file:
     precipitation = json.load(file) #list of dictionaries
     seattle_data = [] #create a variable with an empty list
     for item in precipitation:
         if item['station'] == seattle_station:
             seattle_data.append(item) #a list with all the data for seattle

total_monthly_precipitation = [] #create an empty list where the data will go into
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] # create a list representing each month to loop over
for month in months:
    x = 0
    for measurement_data in seattle_data:
        if f'2010-{month}' in measurement_data['date']:
            x += measurement_data['value'] # sum all the measurement for Seattle for each month 
    total_monthly_precipitation.append(x)
        
print(total_monthly_precipitation)

# save the results to a json file
with open ('total_monthly_precipitation.json', 'w') as outfile:
    json.dump(total_monthly_precipitation, outfile)