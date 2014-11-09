#!/usr/bin/env python
#
# mms-card-updater.py
# A desktop based card updater client to allow quick adding or changing of member's RFID badges.

### IMPORTS ###
import time
import serial
import wx

### GLOBALS ###
serialPort = ""

### CLASSES ###

### FUNCTIONS ###

### MAIN ###
def main():
    # Stuff.
    app = wx.App( False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame = wx.Frame( None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
    frame.Show( True)  # Show the frame.
    app.MainLoop()


if __name__ == '__main__':
	main()
