# PKUAutoBookingVenues
PKU智慧场馆自动预约工具

部分代码和这个README的一部分引用自大佬的自动报备项目 https://github.com/Bruuuuuuce/PKUAutoSubmit


## 说明

- 本工具采用 Python3 搭配 `selenium` 完成自动化操作，实现全自动预约场馆
- 采用定时任务可实现定期（如每周）免打扰预约，请设置在三天前的11:55-12:00之间
- 第三方依赖包几乎只有 `selenium` 一个
- 由于我只测试过羽毛球场的预约，其他场馆只是理论上可行，如果出现任何问题，可以提issue



## 安装与需求

### Python 3

本项目需要 Python 3，可以从[Python 官网](https://www.python.org/)下载安装

### Packages

#### selenium

采用如下命令安装 `selenium`，支持 2.48.0 及以上版本：

```python
pip3 install selenium==2.48.0
```

## 基本用法



1. 用文本编辑器（建议代码编辑器）打开 `config.ini` 文件

2. 配置学号、密码、手机号、预约时间等参数。

3. 双击new.py，保持页面常驻。




## 责任须知

- 本项目仅供参考学习，造成的一切后果由使用者自行承担

