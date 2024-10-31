from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
import warnings

warnings.filterwarnings('ignore')

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.vw = QVideoWidget()
        self.vw.setFixedSize(1920, 1080)  # 设置视频播放器控件的大小为1920x1080
        self.layout.addWidget(self.vw)
        self.setLayout(self.layout)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.vw)

    def playVideo(self, videoPath):
        url = QUrl.fromLocalFile(videoPath)
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    def moveWindowToCenter(self):
        availableGeometry = QDesktopWidget().availableGeometry(self)
        size = self.size()
        self.move((availableGeometry.width() - size.width()) // 2,
                  (availableGeometry.height() - size.height()) // 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setWindowTitle("演示软件")
    player.setWindowIcon(QIcon("static/logo.png"))
    player.resize(1920, 1080)
    player.moveWindowToCenter()
    player.show()

    # 指定视频文件的路径
    videoPath = 'Video.mp4'  # 替换为你的视频文件路径
    player.playVideo(videoPath)

    sys.exit(app.exec_())