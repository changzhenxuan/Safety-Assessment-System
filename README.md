# Safety-Assessment-System
A student's playing work.

----

日期：2022/11/19

一、已实现功能：

- 扫描本地端口：多线程扫描，测试结果：

  ![portScanResult](image\portScanResult.png)

  

- 或取本地浏览器的数据、书签(收藏夹)

  - 历史记录的url：

    ![browserHistory](image\browserHistory.png)

  - 书签(收藏夹)中的url：

    ![browserBookmark](image\browserBookmark.png)

- 扫描指定路径的病毒：pyclamd连接本地clamd，测试结果：

  ![clamdScanResult1](image\clamdScanResult1.png)

二、即将实现功能：

- 检查恶意url：virustotal_python

- 获取并解析widows日志：python_Evtx
- 获取浏览器存储在本地数据库中的用户名和密码

三、计划实现功能：

- 获取windows防火墙规则
- 文件权限检查
- 漏洞扫描、挖掘
- ...
- 最后集成为一个软件

----
