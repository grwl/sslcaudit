''' ----------------------------------------------------------------------
SSLCAUDIT - a tool for automating security audit of SSL clients
Released under terms of GPLv3, see COPYING.TXT
Copyright (C) 2012 Alexandre Bezroutchko abb@gremwell.com
---------------------------------------------------------------------- '''

import sys, logging

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import SSLCauditGUIGenerated

logger = logging.getLogger('SSLCAuditGUI')

class SSLCAuditGUI(object):
    def __init__(self, options):
        '''
        Initialize UI. Dictionary 'options' comes from SSLCAuditUI.parse_options().
        '''
        self.options = options

        self.app = QApplication(sys.argv)
        self.window = SSLCauditGUIWindow(self.options)

    def run(self):
        self.window.show()
        return self.app.exec_()


class SSLCauditGUIWindow(QMainWindow):
    def __init__(self, options, parent=None):
        '''
        Initialize UI. Dictionary 'options' comes from SSLCAuditUI.parse_options().
        '''
        QMainWindow.__init__(self, parent)
        
        self.options = options

        self.ui = SSLCauditGUIGenerated.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.startButton.setIcon(QIcon.fromTheme('media-playback-start'))
        
        for control in [
          self.ui.certificateBrowse1,
          self.ui.certificateBrowse2,
          self.ui.keyBrowse1,
          self.ui.keyBrowse2
        ]:
          control.setIcon(QIcon.fromTheme('document-open'))
          