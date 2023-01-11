#!/usr/bin/python3

# 20221027 Rui Rigel

import os
import requests
import socket
import http.client
import psutil
import subprocess

def get_username():
    username = os.environ.get('USER') or os.environ.get('USERNAME')
    return username

def run_script(script_path:str):
    subprocess.Popen(["python3", script_path])

def kill_process_by_name(process_name:str):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def get_default_gateway_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def server_up(address:str,port:int):
    conn = http.client.HTTPConnection(address, port, timeout=10)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

address = get_default_gateway_ip()
port = 8000
username = get_username()
status = server_up(address, port)

if not status:
    print(f'{address}:{port} is down!')
    process_name = 'dht22server.py'
    kill_process_by_name(process_name)
    script_path = f'/home/{username}/dht22_server/dht22server.py'
    run_script(script_path)
