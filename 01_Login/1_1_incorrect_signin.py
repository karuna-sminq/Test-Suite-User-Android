#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import os


import unittest

from com.dtmilano.android.viewclient import ViewClient, CulebraTestCase

TAG = 'CULEBRA'


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.5, 'find-views-with-content-description': False, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'drop-shadow': False, 'unit-test-method': None, 'interactive': False}
        cls.sleep = 0.85

    def setUp(self):
        super(CulebraTests, self).setUp()

    def tearDown(self):
        super(CulebraTests, self).tearDown()

    def preconditions(self):
        if not super(CulebraTests, self).preconditions():
            return False
        return True

    def testSomething(self):
        if not self.preconditions():
            self.fail('Preconditions failed')

        _s = CulebraTests.sleep
        _v = CulebraTests.verbose

        self.vc.dump(window=-1)

        print "Test Case: Login: Incorrect Credentials"

        # Launch App
        self.vc.findViewWithText(u'Sminq Business').touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        # Enter Mobile Number
        self.vc.findViewWithText(u'Registered mobile number').setText('1212121212')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        # Login
        self.vc.findViewById("com.sminq.businessbug:id/button_login").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        # Check for Incorrect Login
        if self.vc.findViewById("android:id/message"):
            print "Passed! Non registered mobile number entered!"
            self.vc.sleep(_s)
            self.vc.dump(window=-1)
            self.vc.findViewById("android:id/button1").touch()
            self.vc.sleep(_s)
            self.vc.dump(window=-1)
        else:
            print "Mobile number entered is Registered!"

if __name__ == '__main__':
    CulebraTests.main()
