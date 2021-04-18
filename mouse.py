#!/usr/bin/python3
import openrazer.client
a = openrazer.client.DeviceManager()
b = a.devices[0]     # Assumes deathadder is in first place
b.dpi = (600,600)
