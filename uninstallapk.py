#!/usr/bin/env python
#coding:utf8

#installapk.py
#date:2015.1.6
#author:zhang hai

import os
import shutil
import sys
import subprocess
import zipfile
import re
import mobileinfo

reload(sys)
sys.setdefaultencoding("gbk")

#如果系统为64位，AdbWinApi.dll放入 C:Windows\SysWOW64下
#如果系统为32位，AdbWinApi.dll放入 C:Windows\System32下
#adb.exe放入 C:Windows\System32下

#批量卸载apk
def uninstall_apk(device):
    apklist = []
    apkdir = "uninstallapk"
    if len(sys.argv) == 1:    
        for f in os.listdir(apkdir):
            extname = os.path.splitext(f)[1]
            if extname == ".apk" :
                apklist.append(f)
        for apk in apklist:
            print "uninstall "+apk+" on "+device
            pkgname = get_packaganame("uninstallapk" +"/"+apk)
            res = os.system("adb -s " + device + " uninstall " + pkgname)
            res = res>>8
            if res != 0:
                print "Failed to uninstall " + apk +"\n"
                return False
            else:
                print "Success to uninstall " + apk +"\n"
    elif len(sys.argv) > 1:
        argvlen = len(sys.argv)
        for l in xrange(argvlen):
            if l != 0 :
                apk = sys.argv[l]
                print "uninstall "+apk+" on "+device
                pkgname = get_packaganame("uninstallapk" +"/"+apk)
                res = os.system("adb -s " + device + " uninstall " + pkgname)
                res = res>>8
                if res != 0:
                    print "Failed to uninstall " + apk +"\n"
                    return False
                else:
                    print "Success to uninstall " + apk +"\n"


#获取应用主包名
def get_packaganame(apk):
    zf = zipfile.ZipFile(apk, "r")
    zf.extract("AndroidManifest.xml", "temp")
    zf.close()
    child = subprocess.Popen("java -jar AXMLPrinter2.jar temp/AndroidManifest.xml", stdout=subprocess.PIPE, shell=True)
    message = child.stdout.read()     
    reg = re.compile(r"(?<=package=)\"(.*)\"")
    m = re.search(reg, message)
    package_name =  m.group(1)
    print package_name
    return package_name

def main():
    mounted_devices = mobileinfo.find_devices()
    if mounted_devices is not None:
        for device in mounted_devices:
            uninstall_apk(device)

if __name__ == '__main__':
    main()
    
