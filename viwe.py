import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class RehabUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("康复系统")
        self.setGeometry(100, 100, 600, 500)

        arch_button = QPushButton("拱桥", self)
        arch_button.setFixedSize(300, 250)  # 设置按钮大小为300x250

        superman_button = QPushButton("超人式", self)
        superman_button.setFixedSize(300, 250)  # 设置按钮大小为300x250

        layout = QHBoxLayout()
        layout.addStretch(1)  # 添加伸展以将按钮推向窗口左边
        layout.addWidget(arch_button)
        layout.addWidget(superman_button)
        layout.addStretch(1)  # 再次添加伸展以将按钮推向窗口右边

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RehabUI()
    window.show()
    sys.exit(app.exec_())
