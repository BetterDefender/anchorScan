# anchorScan

该工具旨在帮助渗透测试人员批量访问网站JS和其他文件中的大量锚点路径，并对所有锚点页面进行截图，最后通过html文件输出报告。



## Installation

`pip install -r requirements.txt`

`git clone https://github.com/BetterDefender/anchorScan.git`



### **Chrome Headless**

由于该工具使用Selenium来设置无头浏览器，因此在使用之前，你需要安装一个名为Chrome Headless的浏览器驱动程序。

**For Windows：**

1. 在你的电脑上安装最新版本的Chrome浏览器
2. 下载Chrome Headless驱动，请点击 http://chromedriver.chromium.org/downloads
3. 解压下载的压缩文件
4. 将提取的文件夹添加到环境变量中，以方便在命令行中调用



**For Mac：**

1. 打开终端
2. 使用下面的命令来安装Homebrew（如果已经安装，请跳过）

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

3. 使用以下命令安装Chrome（如果已经安装，请跳过）

```bash
brew cask install google-chrome
```

4. 使用以下命令安装Chrome Headless驱动程序

```
brew install chromedriver
```



**For Linux：**

下载Chrome Headless驱动，请点击 http://chromedriver.chromium.org/downloads.

要在Linux系统中安装Chrome Headless驱动，需要满足以下条件：

1. 你的Linux系统上已经安装了Google Chrome浏览器。
2. 你已经下载了最新版本的Chrome Headless驱动。

然后，你可以按照以下步骤来安装Chrome Headless驱动：
1. 将下载的驱动文件解压到你喜欢的目录。
2. 进入解压出来的目录，使用以下命令将驱动添加到系统路径：
```bash
sudo mv chromedriver /usr/local/bin/chromedriver
```
3. 使用以下命令给予执行权限：
```bash
sudo chmod +x /usr/local/bin/chromedriver
```






## Usage

`python3 anchorScan.py -u http://www.example.com/abc/#/`

`-u`  目标网站，要扫描的URL

`-t`  网页加载时间，默认为3秒（如果网站截图为空白可能是因为未加载完，可以通过该指令增加网页加载时长）

<img src="https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821686035/rf40Fd.png" alt="image-20230104145937912" width="660" height="393" />



在**uri.txt**文件中，需要填写需要访问的锚点。

例：

```
/test/edit
/test/view
/test/add
```



当脚本被执行时，该脚本将自动在**reports**目录下生存html格式的报告，截图将被保存在**images**文件夹下。

**HTML 报告：**

![image-20230104152449732](https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821686741/MEr6wr.png)



### 验证方法：

1. 访问URL需要使用浏览器的无痕窗口，否则可能无法正常访问目标锚点页面。

<img src="https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821687136/laG82y.png" alt="image-20230104152034529" width="363" height="433" />

2. 你也可以通过在无痕窗口的控制台中输入 "windows.location.hash "来打开指定的锚点页面。

![image-20230104152324193](https://ekkoipic.oss-cn-beijing.aliyuncs.com/1672821687562/5NIRsr.png)

