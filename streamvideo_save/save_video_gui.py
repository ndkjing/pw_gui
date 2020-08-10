import os
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QInputDialog,QLineEdit,QLabel
import cv2


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.url = 'rtsp://admin:123456@192.168.8.168:554/h264/ch1/main/av_stream'
        self.cap=None
        self.initUI()

    ## 获取视频
    def get_video_cap(self):
        print('ip 地址', self.ip_edit.text())
        print('用户名', self.username_edit.text())
        print('密码', self.password_edit.text())
        url = 'rtsp://%s:%s@%s:554/h264/ch1/main/av_stream' % (
        self.username_edit.text(), self.password_edit.text(), self.ip_edit.text())
        print('url:', url)
        return1 = os.system('ping -n 2 -w 1 %s'%self.ip_edit.text())
        if return1:
            print('ip地址错误')
            return None
        cap = cv2.VideoCapture(url)

        self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.fps = cap.get(cv2.CAP_PROP_FPS)
        print('宽:{},高:{},fps:{}'.format(self.width, self.height, self.fps))
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        size = (self.width, self.height)
        # size = (1920, 1080)
        self.out = cv2.VideoWriter('output.avi', fourcc, int(self.fps), size
                                   )  # 图像大小参数按（宽，高）一定得与写入帧大小一致
        return cap

    ## 单独保存视频
    def save_video(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        if self.cap is None:
            self.cap = self.get_video_cap()
            if self.cap is None:
                print('输入ip地址或者用户名错误')
            while True:
                # Capture frame-by-frame
                ret, frame = self.cap.read()
                if not ret:
                    print('video is over ')
                    break
                # print(frame.shape)
                frame = cv2.resize(frame, (self.width, self.height))
                self.out.write(frame)


    ## 显示视频
    def show_video(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        self.cap = self.get_video_cap()
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print('video is over ')
                break

            cv2.imshow('CameraDemo', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    ## 同时显示和保存视频
    def show_and_save_video(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        self.cap = self.get_video_cap()
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print('video is over ')
                break
            cv2.imshow('CameraDemo', frame)
            frame = cv2.resize(frame,(self.width, self.height))
            self.out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    ## 关闭视频
    def close_video(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    ## 初始化UI
    def initUI(self):
        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle('录制视频工具')
        # text, ok = QInputDialog.getText(self, 'Input Dialog','Enter your name:')

        self.ip_edit = QLineEdit(self)
        self.ip_edit.move(20, 30)
        self.ip_edit.resize(100, 30)

        self.ip_label = QLabel(self)
        self.ip_label.move(20, 0)
        self.ip_label.setText('ip地址')

        self.username_edit = QLineEdit(self)
        self.username_edit.move(150, 30)
        self.username_edit.resize(100, 30)

        self.username_label = QLabel(self)
        self.username_label.move(150, 0)
        self.username_label.setText('用户名')

        self.password_edit = QLineEdit(self)
        self.password_edit.move(300, 30)
        self.password_edit.resize(100, 30)

        self.password_label = QLabel(self)
        self.password_label.move(300, 0)
        self.password_label.setText('密码')

        ## 案件控件
        self.btn1 = QPushButton("显示视频", self)
        self.btn1.move(20, 70)

        self.btn2 = QPushButton("录制视频", self)
        self.btn2.move(120, 70)

        self.btn4 = QPushButton("显示并录制", self)
        self.btn4.move(220, 70)

        self.btn3 = QPushButton("结束视频", self)
        self.btn3.move(320, 70)

        self.btn1.clicked.connect(self.show_video)
        self.btn2.clicked.connect(self.save_video)
        self.btn3.clicked.connect(self.close_video)
        self.btn4.clicked.connect(self.show_and_save_video)
        self.statusBar()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
