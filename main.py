import csv
import requests

'''
Initial config to API consume.
Return a response request as a json.
'''
def responseRequest():
    header = {
        'Content-Type':'application/json'
    }

    token = 'token'
    url = f'http://DNS/?auth={token}'
    
    response = requests.request('GET', url=url, headers=header)
    return response.json()

'''
Decode API response in json to list
'''
def data_all():
    dataJson = responseRequest()
    data = []
    
    # In 'l' we need put columns that we receive from API.
    for i in dataJson:
        l = [i['Id'], i['Type'], i['Name'], i['Cluster'], i['Tags'], i['HasSensitiveData']]
        data.append(l)

    return data

'''
Fetch data from API to CSV file
'''
def responseToCsv(data):
    # In 'csvHeader' we need put columns that we receive from API to make a header CSV.
    csvHeader = ['Id', 'Type', 'Name', 'Cluster', 'Tags', 'HasSensitiveData']
    pathFile = '/home/ribeirin/Documents/Testing/file.csv'

    csvFile = open(pathFile, 'w')
    w = csv.writer(csvFile)

    w.writerow(csvHeader)
    w.writerows(data)

    csvFile.close()

if __name__ == '__main__':
    data = data_all()
    responseToCsv(data)
    
