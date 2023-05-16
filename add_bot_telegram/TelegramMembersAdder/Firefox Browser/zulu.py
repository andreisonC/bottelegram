'''
author : Insominia - https://www.youtube.com/channel/UC7VPq7hdgXbp4z98MwcYxeA?sub_confirmation=1
Note : this script works only on windows operating system and runs on Mozilla firefox browser.

Buy me coffee @paypal: kibedarius@gmail.com
            @neteller: wambudarius1@gmail.com

'''

import webbrowser


url1 = "https://www.youtube.com/channel/UC7VPq7hdgXbp4z98MwcYxeA?sub_confirmation=1"

firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

webbrowser.get('firefox').open_new_tab(url1)

