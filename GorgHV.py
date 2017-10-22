#!/usr/bin/env python3

from gi.repository import Gtk
import os

class GorgHV(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GorgHV")

        self.set_border_width(30)
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        self.add(self.vbox)

        applyLabel = Gtk.Label()
        applyLabel.set_markup("Apply / Remove changes to <b>xorg.conf</b>")

        global applySwitch
        applySwitch = Gtk.Switch()
        applySwitch.connect("notify::active", self.applySwitch_activated)
        
        if os.path.isfile("/etc/X11/xorg.conf") == True:
        	applySwitch.set_active(True)
        elif os.path.isfile("/etc/X11/xorg.conf") == False:
        	applySwitch.set_active(False)

        self.vbox.pack_start(applyLabel, True, True, 0)
        self.vbox.pack_start(applySwitch,  True, True, 0)

    def applySwitch_activated(self, applySwitch, gparam):
        switch = applySwitch.get_active()
        # applySwitch is ON
        if switch == True:
            # create temporary variable for writing to xorg.conf
            with open("/etc/X11/xorg.conf", 'w') as writeXorg:
                print("Creating / Overwriting /etc/X11/xorg.conf")
                xorgConfig = ["Section \"Monitor\"\n"
                              "\tIdentifier \"Monitor0\"\n"
                              "\tModelName  \"Monitor name (you can set this as anything)\"\n"
                              "\tHorizSync    20.0 - 300.0\n"
                              "\tVertRefresh  30.0 - 300.0\n"
                              "EndSection\n\n"
                              					"Section \"Screen\"\n"
        						"\tIdentifier      \"Default Screen\"\n"
        						"\tDevice        \"Intel Corporation 945G Integrated Graphics Controller\"\n"
        						"\tMonitor       \"foo\"\n"
        						"\tDefaultDepth  24\n"
        						"\tSubSection \"Display\"\n"
                			"\t\tDepth          24\n"
               				"\t\tModes         \"1280x1024\"  \"1024x768\"  \"640x480\" \"1280x960\" \"1366 x 768\" \"1440 x 900\"  \"1440 x 960\" \"1440 x 1080\" \"1600 x 1200\" \"1920 x 1080\" \"1920 x 1200\" \n"
        						"\tEndSubSection\n"
											"EndSection\n"]
                print("Writing changes to xorg.conf")
                writeXorg.writelines(xorgConfig)
                print("\nOperation successful\n")

     	# applySwitch is OFF
        elif switch  == False:
            # remove the created xorg.conf file
            os.remove("/etc/X11/xorg.conf")
            print("\nRemoved /etc/X11/xorg.conf")

window = GorgHV()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
