#!/usr/bin/env python3
"""
BIDS conversion tool main window class

AUTHOR
----
Mike Tyszka, Ph.D.

DATES
----
2018-11-06 JMT Adapt from dcm2bids and stellate UI

LICENSE
----

This file is part of bidskit.

bidskit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

bidskit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with stellate.  If not, see <https://www.gnu.org/licenses/>.
"""

from PySide2.QtWidgets import QMainWindow, QFileDialog
from bidskit.bidskit_ui import Ui_MainWindow


class BIDSKitMainWindow(QMainWindow):
    """
    Single inheritance class for BIDSKit UI
    See http://pyqt.sourceforge.net/Docs/PyQt5/designer.html
    """

    def __init__(self):

        # Init the base class
        super().__init__()

        # Set up the Qt Designer-generated UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu callbacks
        self.ui.actionDICOMDirMenu.triggered.connect(self.select_dicom_dir)

        # Button callbacks
        self.ui.actionDICOMDirButton.triggered.connect(self.select_dicom_dir)

    def select_dicom_dir(self):
        """
        Open file chooser to select DICOM source directory

        :return:
        """

        # Open a directory chooser dialog
        dname = QFileDialog.getExistingDirectory(self,
            directory="/Users/jmt/sandbox",
            options=QFileDialog.ShowDirsOnly)

        if dname:
            self.ui.dicomdirText.setText(dname)
