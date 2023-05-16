'''
author : Insominia - https://www.youtube.com/channel/UC7VPq7hdgXbp4z98MwcYxeA?sub_confirmation=1
Note : this script works only on windows operating system and runs on Opera Browser.

Buy me coffee @paypal: kibedarius@gmail.com
            @neteller: wambudarius1@gmail.com

'''

import webbrowser


url1 = "https://www.youtube.com/channel/UC7VPq7hdgXbp4z98MwcYxeA?sub_confirmation=1"

opera_path = r'C:\Users\dariu\AppData\Local\Programs\Opera\opera.exe'
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))

webbrowser.get('opera').open_new_tab(url1)

