#!/usr/bin/python

import subprocess

eww_status = subprocess.run("eww active-windows | grep playlist_selector",
                            shell=True,
                            capture_output=True).stdout.decode("utf-8")
print(len(eww_status))
#Checks if window is opened
if eww_status:
    subprocess.run("eww close playlist_selector",shell=True)

else:
    subprocess.run("eww open playlist_selector",shell=True)

