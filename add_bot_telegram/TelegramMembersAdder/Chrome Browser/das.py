'''
author : Insominia - https://www.youtube.com/channel/UC7VPq7hdgXbp4z98MwcYxeA?sub_confirmation=1
Note : this script works only on windows operating system and runs on chrome browser.

Buy me coffee @paypal: kibedarius@gmail.com
            @neteller: wambudarius1@gmail.com

'''

import webbrowser


url1 = "https://www.youtube.com/channel/UC7VPq7hdgXbp4z98MwcYxeA?sub_confirmation=1"

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

webbrowser.get('chrome').open_new_tab(url1)
