manage-apk
====================
# manage-apk是一款批量安装和卸载apk的工具，依赖于adb的python脚本，安装和卸载十分方便，适合测试手机人员使用。 
本脚本支持apk批量安装和卸载

安装操作步骤如下：

* 1.将要安装的apk包拷贝到apk目录下

* 2.调用installapk.py
  python installapk.py [<apkname1>,<apkname2>...] 
  可选参数不给出时，默认安装apk下的所有包文件
  也可以指定apk文件安装

卸载操作步骤如下：  

* 1.将要卸载的apk包拷贝到uninstallapk目录下 

* 2.调用uninstallapk.py

  python uninstallapk.py [<apkname1>,<apkname2>...] 
  可选参数不给出时，默认卸载uninstallapk下的所有包文件对应的手机上的app 
  也可以指定apk包卸载

 另:
 install.bat和uninstall.bat支持在windows下安装和卸载所有包文件。
 install.sh和uninstall.sh支持在linux下安装和卸载所有包文件。 
 
 注：
 使用前请将手机调至开发者调试模式，使adb获得安装和卸载权限。
