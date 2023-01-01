import sys
import os
import re
import requests as r
import wget


FILEDIR = os.path.join('')
ERASE_LINE = '\x1b[2K'

try:
    LINK = input("Enter a Facebook Video Post URL: ")
    html = r.get(LINK)
    sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
except r.ConnectionError as e:
    print("OOPS!! Connection Error.")
except r.Timeout as e:
    print("OOPS!! Timeout Error")
except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")
except (KeyboardInterrupt, SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
except TypeError:
    print("Video May Private or Invalid URL")
else:
    sd_url = sdvideo_url.replace('sd_src:"', '')
    print("\n")
    print("Normal Quality: " + sd_url)
    print("[+] Video Started Downloading")
    wget.download(sd_url, FILEDIR)
    sys.stdout.write(ERASE_LINE)
    print("\n")
    print("Video downloaded")