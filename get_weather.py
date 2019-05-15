import configparser
import requests
import sys


api_key = 'e10580914a2cfa6bbf6e9edb82e9e9c0'
location = '43.0027,-78.7847'	#UB North Campus

'''
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
''' 
def get_weather(api_key, location):
    url = "https://api.darksky.net/forecast/{}/{}".format(api_key, location)
    r = requests.get(url)
    return r.json()
 
def main():
	#if len(sys.argv) != 2:
	#	exit("Usage: {} LOCATION".format(sys.argv[0]))
	#location = sys.argv[1]
 
    #api_key = get_api_key()
    weather = get_weather(api_key, location)
 
    #print(weather['main']['temp'])
    #print(weather)
    #print(weather['latitude'])
    #print(weather['currently']['summary'])
    
    #Create .csv file
    import csv
    with open('weather_data.csv','w') as csv_file:
		#fieldnames = ['Time', 'Summary', 'Precipitation Probability', 'Temperature', 'Wind Speed', 'Wind Gust', 'Cloud Cover', 'Visibility', 'Good to Fly']
		#writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		
    # Insert Header
		#writer.writeheader()
		csv_file.write('Time, Summary, Precipitation Probability, Temperature, Wind Speed, Wind Gust, Cloud Cover, Visibility, Good to Fly? \n')
		
		for i in range(0,len(weather['hourly']['data'])):
			# convert time to actual value and save as variable
			from datetime import datetime
			ts = int('%d' %(weather['hourly']['data'][i]['time']))
			time = (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
			
			WEATHER_IS_GOOD = {}
			#Weather is good?
			if weather['hourly']['data'][i]['precipProbability'] <= 40 and weather['hourly']['data'][i]['temperature'] >= 32 and weather['hourly']['data'][i]['temperature'] <= 95 and weather['hourly']['data'][i]['windSpeed'] < 20 and weather['hourly']['data'][i]['windGust'] < 20 and weather['hourly']['data'][i]['cloudCover'] < 75 and weather['hourly']['data'][i]['visibility'] > 3:
				WEATHER_IS_GOOD = "yes"
				
			else:
				WEATHER_IS_GOOD = "no"
				
			csv_file.write('%s, %s, %d %%, %d F, %.1f mph, %.1f mph, %d %%, %d mi, %s \n'
			%(time, weather['hourly']['data'][i]['summary'], 
			weather['hourly']['data'][i]['precipProbability'], weather['hourly']['data'][i]['temperature'], 
			weather['hourly']['data'][i]['windSpeed'], weather['hourly']['data'][i]['windGust'], 
			weather['hourly']['data'][i]['cloudCover'], weather['hourly']['data'][i]['visibility'], WEATHER_IS_GOOD))
			
			#writerow({'Time': '%s', 'Summary': '%s', 'Precipitation Probability': '%d %%', 'Temperature': '%d F', 'Wind Speed': '%.1f mph', 'Wind Gust': '%.1f mph', 'Cloud Cover': '%d %%', 'Visibility': '%d mi', 'Good to Fly?': '%s'
			#%(time, weather['hourly']['data'][i]['summary'], 
			#weather['hourly']['data'][i]['precipProbability'], weather['hourly']['data'][i]['temperature'], 
			#weather['hourly']['data'][i]['windSpeed'], weather['hourly']['data'][i]['windGust'], 
			#weather['hourly']['data'][i]['cloudCover'], weather['hourly']['data'][i]['visibility'], str(WEATHER_IS_GOOD) })
			
			#print(time, weather['hourly']['data'][i]['summary'], 
			#weather['hourly']['data'][i]['precipProbability'], weather['hourly']['data'][i]['temperature'], 
			#weather['hourly']['data'][i]['windSpeed'], weather['hourly']['data'][i]['windGust'], 
			#weather['hourly']['data'][i]['cloudCover'], weather['hourly']['data'][i]['visibility'])
		#print(len(weather['hourly']['data']))
	 
if __name__ == '__main__':
    main()
