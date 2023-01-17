import nmap3
import os
from reporter import Reporter

report = Reporter()

def scan(hostname: str):
    print('Scanning...')
    nmap = nmap3.Nmap()
    result = nmap.nmap_os_detection(hostname)
    report.log_report(result)
    print('Saved')

def ping(hostname: str):
    response = os.system(f'ping -n 1 {hostname} > nul"')
    if response == 0:
        print(f'Hostname: {hostname} up!')
        scan(hostname)