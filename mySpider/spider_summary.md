### 利用Scrapy实现豆瓣网top250电影的信息爬取和储存

### 实现过程

* 安装Scrapy环境
* 新建Scrapy项目
* 了解项目中各个文件的作用
* 对项目进行配置,编辑Python代码
* 运行项目.保存数据

#### 安装Scrapy环境

1. 进入虚拟环境
```shell script
workon Spider
```
2. 利用pip3安装Scrapy
```shell script
# 此处已使用alias将pip3重命名为pip
pip install scrapy
```
3. 安装Scrapy后,可通过PyCharm查看自己建立的虚拟环境配置

#### 新建Scrapy项目

1. 通过命令建立Scrapy文件名.csvProject
```shell script
scrapy startproject douban_spider
```
2. cd 项目名称进入项目/通过Pychaspodersrm查看项目
cd douban_project

#### 了解项目中各个文件的作用

1. scrapy.cfg : 项目的配置文件
2. 项目名称/spiders/    : Python代码的目录(定义spider的名称,解析方法xpath,调用模块)
3. 项目名称/items.py    : 项目中的item文件,用于配置数据结构等信息
4. 项目名称/piplines.py : 项目中的pipline文件
5. 项目名称/setting.py  : 项目的设置文件

#### 运行项目文件,保存数据库

1. 命令行输入: scrapy crawl 项目名称
2. 命令行输入: scrapy crawl 项目名称 -o 文件名.json
3. 命令行输入: scrapy crawl 项目名称 -o 文件名.csv