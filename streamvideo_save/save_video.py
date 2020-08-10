# -*- coding: utf-8 -*-
'''
demo
#rtsp://[username]:[password]@[ip]:[port]/
1) username  用户名，常用 admin
2) password  密码，123456
3) ip        摄像头IP，如 192.168.6.66
4) port      端口号，默认为 554  都是默认值
'''
import cv2

# url = 'rtsp://admin:create741025@192.168.8.168:554/h264/ch1/main/av_stream'  # 根据摄像头设置IP及rtsp端口
url = 'rtsp://admin:123456@192.168.8.168:554/h264/ch1/main/av_stream'  # 根据摄像头设置IP及rtsp端口



def get_video_cap(url=0):
    if url==0:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(url)
    return cap


def save_video(cap):
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(height, width, fps)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))  # 图像大小参数按（宽，高）一定得与写入帧大小一致
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print('video is over ')
            break
        # print(frame.shape)
        # Display the resulting frame
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)


    # When everything done, release the capture
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def show_video(cap):
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            print('video is over ')
            break

        cv2.imshow('CameraDemo', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    cap = get_video_cap(url=url)
    # save_video(cap)
    show_video(cap)
