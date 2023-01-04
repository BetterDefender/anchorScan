# anchorScan

This tool is designed to help penetration testers to access a large number of anchor paths in the JS and other files of a website in bulk, and to take screenshots of all anchor pages, and finally output reports through html files.

[中文版本(Chinese version)](README.zh-cn.md)

## Installation

`pip install -r requirements.txt`

`git clone https://github.com/BetterDefender/anchorScan.git`



### **Chrome Headless**

Since this tool uses Selenium to set up a headless browser, you will need to install a browser driver called Chrome Headless before you can use it.

**For Windows：**

1. Install the latest version of Chrome browser on your computer
2. Download Chrome Headless driver at http://chromedriver.chromium.org/downloads
3. Decompress the downloaded zip file
4. Add the extracted folder to the environment variables for easy invocation in the command line



**For Mac：**

1. Open a terminal.
2. Use the following command to install Homebrew.（Skip this step if already installed）

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

3. Install Chrome using the following command. (Skip this step if already installed)

```bash
brew cask install google-chrome
```

4. Install the Chrome Headless driver using the following command.

```
brew install chromedriver
```



**For Linux：**

Download Chrome Headless driver at http://chromedriver.chromium.org/downloads.

To install the Chrome Headless driver on your Linux system, the following conditions need to be met.

1. You already have Google Chrome installed on your Linux system.
2. You have downloaded the latest version of Chrome Headless driver.

Then, you can follow the steps below to install the Chrome Headless driver.
1. Extract the downloaded driver file to your preferred directory.
2. Go to the extracted directory and add the driver to the system path using the following command.
```bash
sudo mv chromedriver /usr/local/bin/chromedriver
```
3. Use the following command to grant execute privileges.
```bash
sudo chmod +x /usr/local/bin/chromedriver
```






## Usage

`python3 anchorScan.py -u http://www.example.com/abc/#/`

`-u`  Target Site,URL to scan

`-t`  Timeout in seconds,Default is 3 seconds

<img src="https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821686035/rf40Fd.png" alt="image-20230104145937912" width="660" height="393" />



The **uri.txt** file needs to be filled in with the anchor points that need to be accessed. 

For example：

```
/test/edit
/test/view
/test/add
```



When the script is executed, the page will automatically survive the report in html format in the **reports** directory，screenshots will be saved in the **images** folder.

**HTML report：**

![image-20230104152449732](https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821686741/MEr6wr.png)



### Verification method：

1. URL access requires a incognito browser window, otherwise the target anchor point may not be accessed properly.

<img src="https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821687136/laG82y.png" alt="image-20230104152034529" width="363" height="433" />

2. You can also open the specified anchor page by typing 'windows.location.hash' into the console in the incognito window.

![image-20230104152324193](https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821687562/5NIRsr.png)

