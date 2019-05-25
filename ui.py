import backend
import langs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class MainUi(object):
    def __init__(self, main_window):

        self.main_dir = ""
        self.lang = langs.EN

        main_window.setObjectName("main_window")

        main_window.resize(1265, 767)

        main_window.setMaximumWidth(1265)
        main_window.setMinimumWidth(1265)

        main_window.setMaximumHeight(767)
        main_window.setMinimumHeight(767)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.pic_frame = QtWidgets.QFrame(self.central_widget)
        self.pic_frame.setGeometry(QtCore.QRect(260, 10, 761, 571))
        self.pic_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pic_frame.setObjectName("pic_frame")

        self.pic = QtWidgets.QLabel(self.pic_frame)
        self.pic.setGeometry(QtCore.QRect(1, 0, 761, 570))
        self.pic.setText("")
        self.pic.setTextFormat(QtCore.Qt.AutoText)
        self.pic.setPixmap(QtGui.QPixmap())
        self.pic.setScaledContents(False)
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.pic.setWordWrap(True)
        self.pic.setObjectName("pic")

        self.files_list = QtWidgets.QListWidget(self.central_widget)
        self.files_list.setGeometry(QtCore.QRect(0, 170, 251, 591))
        self.files_list.setObjectName("files_list")

        self.dirs_list = QtWidgets.QListWidget(self.central_widget)
        self.dirs_list.setGeometry(QtCore.QRect(1030, 350, 231, 411))
        self.dirs_list.setObjectName("dirs_list")

        self.dirs_menu = QtWidgets.QFrame(self.central_widget)
        self.dirs_menu.setGeometry(QtCore.QRect(1030, 10, 231, 331))
        self.dirs_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dirs_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dirs_menu.setObjectName("dirs_menu")

        self.btn_add_dir = QtWidgets.QPushButton(self.dirs_menu)
        self.btn_add_dir.setGeometry(QtCore.QRect(10, 50, 211, 41))
        self.btn_add_dir.setObjectName("btn_add_dir")

        self.btn_rmv_dir = QtWidgets.QPushButton(self.dirs_menu)
        self.btn_rmv_dir.setGeometry(QtCore.QRect(10, 100, 211, 41))
        self.btn_rmv_dir.setObjectName("btn_rmv_dir")

        self.inp_dir_to_add = QtWidgets.QLineEdit(self.dirs_menu)
        self.inp_dir_to_add.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.inp_dir_to_add.setObjectName("inp_dir_to_add")

        self.edit_menu = QtWidgets.QFrame(self.central_widget)
        self.edit_menu.setGeometry(QtCore.QRect(260, 590, 761, 171))
        self.edit_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_menu.setObjectName("edit_menu")

        self.btn_move = QtWidgets.QPushButton(self.edit_menu)
        self.btn_move.setGeometry(QtCore.QRect(600, 110, 151, 41))
        self.btn_move.setObjectName("btn_move")

        self.inp_name = QtWidgets.QLineEdit(self.edit_menu)
        self.inp_name.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.inp_name.setObjectName("inp_name")

        self.btn_set_name = QtWidgets.QPushButton(self.edit_menu)
        self.btn_set_name.setGeometry(QtCore.QRect(190, 20, 91, 31))
        self.btn_set_name.setObjectName("btn_set_name")

        self.files_menu = QtWidgets.QFrame(self.central_widget)
        self.files_menu.setGeometry(QtCore.QRect(0, 10, 251, 151))
        self.files_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_menu.setObjectName("files_menu")

        self.btn_get_files = QtWidgets.QPushButton(self.files_menu)
        self.btn_get_files.setGeometry(QtCore.QRect(10, 50, 231, 41))
        self.btn_get_files.setObjectName("btn_get_files")

        self.inp_main_dir = QtWidgets.QLineEdit(self.files_menu)
        self.inp_main_dir.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.inp_main_dir.setObjectName("inp_main_dir")
        self.inp_main_dir.setText("/home/fox/Wallpaper")
        main_window.setCentralWidget(self.central_widget)

        self.set_tittles(main_window)

        self.set_listeners()

    def set_tittles(self, main_window):
        main_window.setWindowTitle(self.lang["dict"]["main_tittle"])
        self.btn_add_dir.setText(self.lang["dict"]["add_dit_btn"])
        self.btn_rmv_dir.setText(self.lang["dict"]["rm_dit_btn"])
        self.btn_move.setText(self.lang["dict"]["move_btn"])
        self.btn_set_name.setText(self.lang["dict"]["set_name_btn"])
        self.btn_get_files.setText(self.lang["dict"]["get_files_btn"])

    def set_listeners(self):
        self.btn_get_files.clicked.connect(self.get_files)
        self.btn_add_dir.clicked.connect(self.add_dir)
        self.files_list.itemSelectionChanged.connect(self.select_file)
        self.btn_set_name.clicked.connect(self.rename_file)
        self.btn_rmv_dir.clicked.connect(self.rm_dir)
        self.btn_move.clicked.connect(self.move_file)

    def get_files(self):
        self.files_list.clear()
        self.pic.setPixmap(QtGui.QPixmap())

        self.main_dir = self.inp_main_dir.text()
        files = backend.get_files(self.main_dir)

        for file in files:
            self.files_list.addItem(file)

    def add_dir(self):
        path = backend.add_dir(self.inp_dir_to_add.text())
        item = self.dirs_list.findItems(path, Qt.MatchExactly)

        if not item:
            self.dirs_list.addItem(backend.add_dir(path))

    def rm_dir(self):
        item = self.dirs_list.selectedItems()

        if item:
            self.dirs_list.takeItem(self.dirs_list.row(item[0]))

    def select_file(self, item=None):
        if not item:
            item = self.files_list.currentItem()

        pix = QtGui.QPixmap(self.main_dir + "/" + item.text())

        if pix.width() > pix.height():
            pix = pix.scaledToWidth(760)

            if pix.height() > self.pic_frame.height():
                pix = pix.scaledToHeight(569)
        else:
            pix = pix.scaledToHeight(569)

            if pix.width() > self.pic_frame.width():
                pix = pix.scaledToWidth(760)

        self.pic.setPixmap(pix)

    def rename_file(self):
        old_name: str = self.files_list.currentItem().text()

        new_name = self.inp_name.text()

        new_name = backend.rename_file(self.main_dir, old_name, new_name)

        self.files_list.currentItem().setText(new_name)

    def move_file(self):
        new_path = self.dirs_list.currentItem().text()
        file = self.files_list.currentItem().text()

        backend.move_file(self.main_dir, new_path, file)

        item = self.files_list.selectedItems()

        if item:
            self.files_list.takeItem(self.files_list.row(item[0]))
