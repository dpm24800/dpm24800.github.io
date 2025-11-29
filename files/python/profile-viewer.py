import webbrowser
import time

url = "https://github.com/dpm24800"   # change this to your target URL

for i in range(100):
    webbrowser.open_new_tab(url)
    print(f"Opened {i+1} times")
    time.sleep(0.5)  # small delay so it doesn't freeze your system
