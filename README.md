# WLAN Rate  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <a href="https://twitter.com/intent/follow?screen_name=kfrawee">
        <img src="https://img.shields.io/twitter/follow/shields_io?style=social&logo=twitter"
            alt="follow on Twitter"></a>

## About
This simple script uses [selenium](https://pypi.org/project/selenium/) to automate a basic task of changing wlan rate (speed) for controlling internet usage and quota. **only for Huawei - HG630 V2**. *You may try on other modems*<br>
- It will list your current rate.
- List all availble rates.

![](WLAN-Rate.gif)

---
## Usage
- Clone the repo to your local machine.
- Use the `requirements.txt` to install required libraries.
```
pip install -r requirements.txt
```
- Install a comatable webdriver. *[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)* 
- Modify [`login.py`](https://github.com/kfrawee/WLANRate/blob/master/login.py) with your login credentials.
- Check `default_gateway` in [`wlan_rate.py`](https://github.com/kfrawee/WLANRate/blob/master/wlan_rate.py). *By dafault `default_gateway = r'https://192.168.1.1/'`*
- In script directory, type `python wlan_rate.py` in your terminal 
--- 
