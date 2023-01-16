from array import array
import nmap3
import os
import json
import time
import requests

path = os.path.join(os.getcwd(), 'out')
report_name = f'report_{time.time()}.json'
if not os.path.exists(path=path):
    os.makedirs(path)
path = os.path.join(path, report_name)
if not os.path.exists(path=path):
    with open(path, 'w') as f:
        f.write(json.dumps([], indent=4))

def print_json(obj: dict):
    print(json.dumps(obj, indent=4))

def log_report(save: object):
    f = open(path, 'r')
    reports: list = json.load(f)
    print(save)
    reports.append(save)
    with open(path, 'w') as f:
        f.write(json.dumps(reports, indent=4))

def scan_ip(hostname: str):
    print('Scanning...')
    nmap = nmap3.Nmap()
    result = nmap.nmap_os_detection(hostname)
    log_report(result)
    print('Saved')

def ping(hostname: str):
    response = os.system(f'ping -n 1 -c 1 {hostname} > nul"')
    if response == 0:
        print(f'Hostname: {hostname} up!')
        scan_ip(hostname)

if __name__ == '__main__':

    country_code = 'FR'
    response = requests.get(f'https://cdn-lite.ip2location.com/datasets/{country_code}.json', headers={'Accept': 'application/json'})

    for slice_array in response.json()['data']:
        slice = {
            'start': slice_array[0],
            'end': slice_array[1]
        }

        print(f'Slice: [{slice["start"]} - {slice["end"]}]')

        startSplitted = slice['start'].split('.')
        sb1 = int(startSplitted[3])
        sb2 = int(startSplitted[2])
        sb3 = int(startSplitted[1])
        sb4 = int(startSplitted[0])

        endSplitted = slice['end'].split('.')
        eb1 = int(endSplitted[3])
        eb2 = int(endSplitted[2])
        eb3 = int(endSplitted[1])
        eb4 = int(endSplitted[0])

        for byte4 in range(sb4, 255):
            for byte3 in range(sb3, 255):
                for byte2 in range(sb2, 255):
                    for byte1 in range(sb1, 255):
                        #addr = f'39.238.{byte2}.{byte1}.rev.sfr.net'
                        addr = f'{byte4}.{byte3}.{byte2}.{byte1}'
                        if addr == slice['end']:
                            raise Exception(f'End of slice [{slice["start"]} - {slice["end"]}]')
                        print(f'Hostname: ' + addr, end='\r')
                        ping(addr)
    