import os
import shutil
import warnings
import requests
import time
import argparse
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('''
                     _                _____                 
    /\              | |              / ____|                
   /  \   _ __   ___| |__   ___  _ _| (___   ___ __ _ _ __  
  / /\ \ | '_ \ / __| '_ \ / _ \| '__\___ \ / __/ _` | '_ \ 
 / ____ \| | | | (__| | | | (_) | |  ____) | (_| (_| | | | |
/_/    \_\_| |_|\___|_| |_|\___/|_| |_____/ \___\__,_|_| |_|

                                        Author: BetterDefender
                                        Version: 1.0
''')

parser = argparse.ArgumentParser()
parser.add_argument('-u', type=str, help='Target Site,URL to scan')
parser.add_argument('-t',type=int,help='Timeout in seconds,Default is 3 seconds')
args = parser.parse_args()
if not args.u:
    print('Error: Please enter the URL!\n')
    print('Example: http://www.example.com/abc/#/')
    exit(1)
url = args.u

if os.path.getsize('uri.txt') == 0:
    print("Error: uri.txt file is empty, please fill in the anchor link.")
    exit(1)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome(chrome_options=options)
driver.set_window_size(1920, 1080)

def getTime():
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    return timestamp


fname = 'reports/res_' + getTime() + '.html'

try:
    print('The program is running, please wait...\n')
    with open(fname, 'w') as t:
        t.write('<html>\n')
        t.write('<head>\n')
        t.write('<title>Anchor Scan Report</title>\n')
        t.write('<style>\n')
        t.write('table td {text-align: center;}\n')
        t.write('tr, td {border: 1px solid black;}\n')
        t.write('</style>\n')
        t.write('</head>\n')
        t.write('<body>\n')
        t.write('<h3>Verification method：</h3>\n')
        t.write('<h4>1.URL access requires a incognito browser window, otherwise the target anchor point may not be accessed properly.</h4>\n')
        t.write('<h4>2.You can also open the specified anchor page by typing \'windows.location.hash\' into the console in the incognito window.</h4>\n')
        t.write('<table>\n')
        t.write('<tr>\n')
        t.write('<td>URL</td>\n')
        t.write('<td>Screenshot</td>\n')
        t.write('<td>Manually modify web anchors</td>\n')
        t.write('</tr>\n')
        with open('uri.txt', 'r') as f:
            for line in f:
                parsed_url = urlparse(url)
                parsed_url = parsed_url._replace(fragment=line.rstrip())
                modified_url = urlunparse(parsed_url)
                driver.get(modified_url)
                if not args.t:
                    time.sleep(2)
                else:
                    time.sleep(args.t)
                screenshot = driver.get_screenshot_as_png()
                filename = 'screenshot' + getTime() + '.png'
                filepath = os.path.join('images', filename)
                with open(filepath, 'wb') as f:
                    f.write(screenshot)
                t.write('<tr>\n')
                t.write('<td><a href="#" onclick="window.open(\'{}\', \'_blank\', \'noopener noreferrer\'); return false;">{}</a></td>\n'.format(modified_url,modified_url))
                t.write('<td><img src="../{}" alt="Screenshot" width="850" height="500"></td>\n'.format(filepath))
                t.write('<td style="word-break: break-all;">window.location.hash=\'{}\';</td>\n'.format(line.strip()))
                t.write('<tr>\n')
        t.write('</table>\n')
        t.write('</body>\n')
        t.write('</html>\n')
except KeyboardInterrupt:
    print('\nYou have pressed Ctrl+C to exit the program.')
    exit(1)

print('The program is finished, please check the {} file.'.format(fname))
driver.close()