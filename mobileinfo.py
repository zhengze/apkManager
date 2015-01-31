#!/usr/bin/env python
#coding:utf8

import os
import sys
import subprocess

MANUFACTURER_CMD = 'adb -s %s shell getprop ro.product.manufacturer'
MODEL_CMD = 'adb -s %s shell getprop ro.product.model'
VERSION_CMD = 'adb -s %s shell getprop ro.build.version.release'

def get_info(command, serialno):
    command = command %serialno
    child = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = child.stdout
    message = output.read()
    if message is not None:
        return message
    else:
        return None

def get_infos(serialno):
    command_list = [MANUFACTURER_CMD, MODEL_CMD, VERSION_CMD]
    info_list = []
    for cmd in command_list:
        command = cmd%serialno
        child = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output = child.stdout
        message = output.read().rstrip("\r\n")
        info_list.append(message)
    if len(info_list) > 0:
        return info_list
    else:
        return None

def mobile_table(seriallist):
    print "|==== 设备号 ====|==== 厂商 ====|==== 型号 ====|==== 版本 =====|"
    for sl in seriallist:
        manufacturer, model, version = get_infos(sl)
        print ("|%-15s|%-15s|%-15s|%-15s|") %(sl, manufacturer, model, version)
    print "="*55
    return seriallist

#寻找连接上的设备
def find_devices():
    child = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True)    
    message = child.stdout.read()
    devicelist = message.split("\n")[1:]
    serial_list = list()
    for dl in devicelist :
        if "\tdevice" in dl:
            serialno = dl.split("\t")[0]
            serial_list.append(serialno)

    mobile_table(serial_list)    
    return serial_list

if __name__ == "__main__":
    find_devices()
