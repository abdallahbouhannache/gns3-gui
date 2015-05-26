# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Configuration page for server preferences.
"""

import os
import sys
import re
import uuid
from gns3.qt import QtNetwork, QtWidgets, QtCore
from ..ui.server_preferences_page_ui import Ui_ServerPreferencesPageWidget
from ..servers import Servers
from ..topology import Topology
from ..utils.message_box import MessageBox
from ..utils.progress_dialog import ProgressDialog
from ..utils.wait_for_connection_worker import WaitForConnectionWorker
from ..settings import LOCAL_SERVER_SETTINGS


class ServerPreferencesPage(QtWidgets.QWidget, Ui_ServerPreferencesPageWidget):

    """
    QWidget configuration page for server preferences.
    """

    def __init__(self, parent=None):

        super().__init__()
        self.setupUi(self)
        self._remote_servers = {}

        # connect the slots
        self.uiLocalServerToolButton.clicked.connect(self._localServerBrowserSlot)
        self.uiAddRemoteServerPushButton.clicked.connect(self._remoteServerAddSlot)
        self.uiDeleteRemoteServerPushButton.clicked.connect(self._remoteServerDeleteSlot)
        self.uiRemoteServersTreeWidget.itemClicked.connect(self._remoteServerClickedSlot)
        self.uiRemoteServersTreeWidget.itemSelectionChanged.connect(self._remoteServerChangedSlot)
        self.uiRestoreDefaultsPushButton.clicked.connect(self._restoreDefaultsSlot)
        self.uiLocalServerAutoStartCheckBox.stateChanged.connect(self._useLocalServerAutoStartSlot)
        self.uiRemoteServerProtocolComboBox.currentIndexChanged.connect(self._remoteServerProtocolCurrentIndexSlot)
        self.uiRemoteServerSSHKeyPushButton.clicked.connect(self._remoteServerSSHKeyPushButtonSlot)

        # load all available addresses
        for address in QtNetwork.QNetworkInterface.allAddresses():
            address_string = address.toString()
            if address.protocol() == QtNetwork.QAbstractSocket.IPv6Protocol:
                continue  # FIXME: finish IPv6 support (problem with ws4py)
                # we do not want the scope id when using an IPv6 address...
                address.setScopeId("")
            self.uiLocalServerHostComboBox.addItem(address_string, address.toString())

        # default is 127.0.0.1
        index = self.uiLocalServerHostComboBox.findText("127.0.0.1")
        if index != -1:
            self.uiLocalServerHostComboBox.setCurrentIndex(index)

        self._remoteServerProtocolCurrentIndexSlot(0)

    def _remoteServerSSHKeyPushButtonSlot(self):
        """
        Slot to open a file browser and select an ssh key.
        """

        filter = ""
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the SSH key", ".", filter)
        if not path:
            return

        self.uiRemoteServerSSHKeyLineEdit.setText(path)

    def _remoteServerProtocolCurrentIndexSlot(self, index):
        if self.uiRemoteServerProtocolComboBox.currentText() == "SSH":
            self.uiRemoteServerUserLineEdit.setText("")
            self.uiRemoteServerUserLabel.show()
            self.uiRemoteServerUserLineEdit.show()
            self.uiRemoteServerSSHPortLabel.show()
            self.uiRemoteServerSSHPortSpinBox.show()
            self.uiRemoteServerSSHKeyLabel.show()
            self.uiRemoteServerSSHKeyLineEdit.show()
            self.uiRemoteServerSSHKeyPushButton.show()
        else:
            self.uiRemoteServerUserLabel.hide()
            self.uiRemoteServerUserLineEdit.hide()
            self.uiRemoteServerSSHPortLabel.hide()
            self.uiRemoteServerSSHPortSpinBox.hide()
            self.uiRemoteServerSSHKeyLabel.hide()
            self.uiRemoteServerSSHKeyLineEdit.hide()
            self.uiRemoteServerSSHKeyPushButton.hide()

    def _useLocalServerAutoStartSlot(self, state):
        """
        Slot to enable or not local server settings.
        """

        if state:
            self.uiGeneralSettingsGroupBox.setEnabled(True)
            self.uiConsolePortRangeGroupBox.setEnabled(True)
            self.uiUDPPortRangeGroupBox.setEnabled(True)
        else:
            self.uiGeneralSettingsGroupBox.setEnabled(False)
            self.uiConsolePortRangeGroupBox.setEnabled(False)
            self.uiUDPPortRangeGroupBox.setEnabled(False)

    def _restoreDefaultsSlot(self):
        """
        Slot to restore default settings
        """

        self._populateWidgets(LOCAL_SERVER_SETTINGS)

    def _localServerBrowserSlot(self):
        """
        Slot to open a file browser and select a local server.
        """

        filter = ""
        if sys.platform.startswith("win"):
            filter = "Executable (*.exe);;All files (*.*)"
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select the local server", ".", filter)
        if not path:
            return

        self.uiLocalServerPathLineEdit.setText(path)

    def _remoteServerClickedSlot(self, item, column):
        """
        Loads a selected remote server from the tree widget.

        :param item: selected QTreeWidgetItem instance
        :param column: ignored
        """

        settings = item.settings
        protocol = settings["protocol"].upper()
        try:
            port = int(settings["port"])
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Remote server", "Invalid port")
            return
        self.uiRemoteServerProtocolComboBox.setCurrentIndex(self.uiRemoteServerProtocolComboBox.findText(protocol))
        self.uiRemoteServerPortLineEdit.setText(settings["host"])
        self.uiRemoteServerPortSpinBox.setValue(port)
        self.uiRemoteServerUserLineEdit.setText(settings["user"])
        self.uiRemoteServerSSHKeyLineEdit.setText(settings.get("ssh_key", None))
        self.uiRemoteServerSSHPortSpinBox.setValue(settings.get("ssh_port", 22))

    def _remoteServerChangedSlot(self):
        """
        Enables the use of the delete button.
        """

        item = self.uiRemoteServersTreeWidget.currentItem()
        if item:
            self.uiDeleteRemoteServerPushButton.setEnabled(True)
        else:
            self.uiDeleteRemoteServerPushButton.setEnabled(False)

    def _remoteServerAddSlot(self):
        """
        Adds a new remote server.
        """

        protocol = self.uiRemoteServerProtocolComboBox.currentText().lower()
        host = self.uiRemoteServerPortLineEdit.text().strip()
        port = self.uiRemoteServerPortSpinBox.value()
        user = self.uiRemoteServerUserLineEdit.text().strip()
        ssh_port = self.uiRemoteServerSSHPortSpinBox.value()
        ssh_key = self.uiRemoteServerSSHKeyLineEdit.text().strip()

        if not re.match(r"^[a-zA-Z0-9\.{}-]+$".format("\u0370-\u1CDF\u2C00-\u30FF\u4E00-\u9FBF"), host):
            QtWidgets.QMessageBox.critical(self, "Remote server", "Invalid remote server hostname {}".format(host))
            return
        if port is None or port < 1:
            QtWidgets.QMessageBox.critical(self, "Remote server", "Invalid remote server port {}".format(port))
            return

        if protocol == "ssh" and len(user) == 0:
            QtWidgets.QMessageBox.critical(self, "Remote server", "Missing user login")
            return

        if protocol == "ssh" and len(ssh_key) == 0:
            QtWidgets.QMessageBox.critical(self, "Remote server", "Missing SSH key")
            return

        # check if the remote server is already defined
        for server in self._remote_servers.values():
            if server["protocol"] == protocol and server["host"] == host and server["port"] == port and server["user"] == user:
                QtWidgets.QMessageBox.critical(self, "Remote server", "Remote server is already defined.")
                return

        settings = {"protocol": protocol,
                    "host": host,
                    "port": port,
                    "user": user,
                    "ssh_port": ssh_port,
                    "ssh_key": ssh_key}

        # add a new entry in the tree widget
        item = QtWidgets.QTreeWidgetItem(self.uiRemoteServersTreeWidget)
        item.setText(0, protocol)
        item.setText(1, host)
        item.setText(2, str(port))
        item.setText(3, user)
        item.settings = settings
        item.server_id = uuid.uuid4()  #  Create a temporay unique server id

        # keep track of this remote server
        self._remote_servers[item.server_id] = settings

        self.uiRemoteServerPortSpinBox.setValue(self.uiRemoteServerPortSpinBox.value() + 1)
        self.uiRemoteServersTreeWidget.resizeColumnToContents(0)

    def _remoteServerDeleteSlot(self):
        """
        Deletes a remote server.
        """

        item = self.uiRemoteServersTreeWidget.currentItem()
        if item:
            protocol = item.text(0)
            host = item.text(1)
            port = int(item.text(2))
            user = item.text(3).strip()
            assert item.server_id in self._remote_servers, "Missing {} in {}".format(item.server_id, self._remote_servers)
            del self._remote_servers[item.server_id]
            self.uiRemoteServersTreeWidget.takeTopLevelItem(self.uiRemoteServersTreeWidget.indexOfTopLevelItem(item))

    def _populateWidgets(self, settings):
        """
        Populates the widgets with the settings.

        :param settings: Local server settings
        """

        self.uiLocalServerPathLineEdit.setText(settings["path"])
        index = self.uiLocalServerHostComboBox.findData(settings["host"])
        if index != -1:
            self.uiLocalServerHostComboBox.setCurrentIndex(index)
        self.uiLocalServerPortSpinBox.setValue(settings["port"])
        self.uiLocalServerAutoStartCheckBox.setChecked(settings["auto_start"])
        self.uiConsoleConnectionsToAnyIPCheckBox.setChecked(settings["allow_console_from_anywhere"])
        self.uiConsoleStartPortSpinBox.setValue(settings["console_start_port_range"])
        self.uiConsoleEndPortSpinBox.setValue(settings["console_end_port_range"])
        self.uiUDPStartPortSpinBox.setValue(settings["udp_start_port_range"])
        self.uiUDPEndPortSpinBox.setValue(settings["udp_end_port_range"])

    def loadPreferences(self):
        """
        Loads the server preferences.
        """

        servers = Servers.instance()

        # load the local server preferences
        local_server_settings = servers.localServerSettings()
        self._populateWidgets(local_server_settings)

        # load remote server preferences
        self._remote_servers.clear()
        self.uiRemoteServersTreeWidget.clear()
        for server_id, server in servers.remoteServers().items():
            protocol = server.protocol()
            host = server.host()
            port = server.port()
            user = server.user()
            self._remote_servers[server_id] = server.settings()
            item = QtWidgets.QTreeWidgetItem(self.uiRemoteServersTreeWidget)
            item.setText(0, protocol)
            item.setText(1, host)
            item.setText(2, str(port))
            item.setText(3, user)
            item.settings = server.settings()
            item.server_id = server_id

        self.uiRemoteServersTreeWidget.resizeColumnToContents(0)

    def savePreferences(self):
        """
        Saves the server preferences.
        """

        servers = Servers.instance()
        current_settings = servers.localServerSettings()
        restart_local_server = False

        # save the local server preferences
        new_settings = {}
        new_settings["path"] = self.uiLocalServerPathLineEdit.text()
        new_settings["host"] = self.uiLocalServerHostComboBox.itemData(self.uiLocalServerHostComboBox.currentIndex())
        new_settings["port"] = self.uiLocalServerPortSpinBox.value()
        new_settings["auto_start"] = self.uiLocalServerAutoStartCheckBox.isChecked()
        new_settings["allow_console_from_anywhere"] = self.uiConsoleConnectionsToAnyIPCheckBox.isChecked()
        new_settings["console_start_port_range"] = self.uiConsoleStartPortSpinBox.value()
        new_settings["console_end_port_range"] = self.uiConsoleEndPortSpinBox.value()
        new_settings["udp_start_port_range"] = self.uiUDPStartPortSpinBox.value()
        new_settings["udp_end_port_range"] = self.uiUDPEndPortSpinBox.value()
        new_settings["images_path"] = current_settings["images_path"]
        new_settings["projects_path"] = current_settings["projects_path"]
        new_settings["report_errors"] = current_settings["report_errors"]

        if new_settings["console_end_port_range"] <= new_settings["console_start_port_range"]:
            QtWidgets.QMessageBox.critical(self, "Local", "Invalid console port range from {} to {}".format(new_settings["console_start_port_range"],
                                                                                                            new_settings["console_end_port_range"]))
            return

        if new_settings["udp_end_port_range"] <= new_settings["udp_start_port_range"]:
            QtWidgets.QMessageBox.critical(self, "Local", "Invalid UDP port range from {} to {}".format(new_settings["udp_start_port_range"],
                                                                                                        new_settings["udp_end_port_range"]))
            return

        if new_settings["auto_start"]:
            if not os.path.isfile(new_settings["path"]):
                QtWidgets.QMessageBox.critical(self, "Local server", "Could not find local server {}".format(new_settings["path"]))
                return
            if not os.access(new_settings["path"], os.X_OK):
                QtWidgets.QMessageBox.critical(self, "Local server", "{} is not an executable".format(new_settings["path"]))

            if new_settings != current_settings:
                # first check if we have nodes on the local server
                local_nodes = []
                topology = Topology.instance()
                for node in topology.nodes():
                    if node.server().isLocal():
                        local_nodes.append(node.name())
                if local_nodes:
                    nodes = "\n".join(local_nodes)
                    MessageBox(self, "Local server", "Please close your project or delete all the nodes running on the \
                    local server before changing the local server settings", nodes)
                    return
                restart_local_server = True
        else:
            servers.stopLocalServer(wait=True)

        # save the local server preferences
        servers.setLocalServerSettings(new_settings)
        # save the remote server preferences
        servers.updateRemoteServers(self._remote_servers)
        servers.save()

        # restart the local server if required
        if restart_local_server:
            servers.stopLocalServer(wait=True)
            if servers.startLocalServer():
                worker = WaitForConnectionWorker(new_settings["host"], new_settings["port"])
                dialog = ProgressDialog(worker, "Local server", "Connecting...", "Cancel", busy=True, parent=self)
                dialog.show()
                dialog.exec_()
            else:
                QtWidgets.QMessageBox.critical(self, "Local server", "Could not start the local server process: {}".format(new_settings["path"]))
