"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import subprocess
from subprocess import CalledProcessError
from . import const

DEVICE = const.DEVICE


class unmount:
    def __init__(self, blkid):
        self.blkid = blkid
        self.__unmount()

    def __unmount(self):
        """
        Unmount disks
        """
        global DDOUTPUT1
        global DDOUTPUT2
        print('unmount %s and %s' % (self.blkid.master[DEVICE],
                                     self.blkid.slave[DEVICE]))
        x = 'sudo unmount %s'
        try:
            xx = x % (self.blkid.master[DEVICE])
            cmd = subprocess.Popen(x % (self.blkid.master[DEVICE]))
            DDOUTPUT1 = cmd.communicate()[0]
            print(xx)
            print(DDOUTPUT1)
            xx = x % (self.blkid.slave[DEVICE])
            cmd = subprocess.Popen(x % (self.blkid.slave[DEVICE]))
            DDOUTPUT2 = cmd.communicate()[0]
            print(xx)
            print(DDOUTPUT2)
        except CalledProcessError:
            print('Error in sudo e2label')
            print('Command: %s' % (xx))
