import requests
import ip
from network import *

if __name__ == '__main__':

    country_code = 'CH'
    response = requests.get(f'https://cdn-lite.ip2location.com/datasets/{country_code}.json', headers={'Accept': 'application/json'})
    try:
        for slice_array in response.json()['data']:

                start = ip.Ip(slice_array[0])
                end = ip.Ip(slice_array[1])

                print(f'Slice: [{start} - {end}]')
                try: 
                    for start.b4 in range(start.b4, 255):
                        for start.b3 in range(start.b3, 255):
                            for start.b2 in range(start.b2, 255):
                                for start.b1 in range(start.b1, 255):
                                    addr = start.__str__()
                                    if addr == end.__str__():
                                        raise Exception(f'End of slice [{slice["start"]} - {slice["end"]}]')
                                    print(f'Hostname: ' + addr, end='\r')
                                    ping(addr)
                except KeyboardInterrupt as e:
                    rep = input('S=Stop | N=Next slice : ')
                    if rep in ['s', 'S', 'stop']:
                        raise Exception('Stop manually')
                    else:
                        continue
    except Exception as e:
        print(e)
