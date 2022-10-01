from enum import IntFlag
from pydoc import describe
from subprocess import call
from tkinter.messagebox import NO
import cv2 as cv
import pyttsx3
from pyzbar.pyzbar import decode
from PIL import Image

__author__  = "CT"

def call_type(tp) -> str:
    data_type = [
    # 输出中文 - 0
    'utf-8',

    #输出英文 - 1
    'ascill'
    ]

    if "中文" in tp:
        return data_type[0]
    elif "英文" in tp:
        return data_type[1]
    else:
        print("错误")
     

class BaseQrcodeTool(object):

    def __init__(self, describe) -> None:
        self.describe = describe


    def __repr__(self) -> str:
        return f"生成二维码工具：{self.describe}"

    def build_qrcode(self, message, img_output):
        try:
            import qrcode
        except ImportError:
            assert "缺少{qrcode}库"

        if message and img_output:
            image = qrcode.make(message)
            image.save(img_output)

        return None


class QrcodeOperator(BaseQrcodeTool):
    
    def __init__(self, describe=None) -> None:
        self.broadcast_engine = pyttsx3.init()
        if describe:
            super(QrcodeOperator, self).__init__(describe)
        
    @property
    def broadcat(self, message: str, downfile = None):
        self._broadcast(message, downfile)

    def _build_qrcode(self, message, img_output):
        super(QrcodeOperator, self).build_qrcode(message, img_output)

    def verification(self, image_dir, data_type) -> str:
        if image_dir and data_type:
            decodeQR = decode(Image.open(image_dir))
            
            # show data detail.
            print(decodeQR[0].data.decode(data_type))

            # operator qrcode data.
            self._broadcast(decodeQR[0].data.decode(data_type))

    def _broadcast(self, message: str, downfile = None):
        if message:
            self.broadcast_engine.say(message)
            self.broadcast_engine.runAndWait()

        
    def _down_broadcast_file(direct: str, message: str):
        try:
            from pydub import AudioSegment
        except ImportError:
            assert "缺少{pydub}库"

        if message and direct:
            AudioSegment.from_file(direct).export("xx.mp3", format="mp3")

        return None



op = QrcodeOperator()
op.verification('C:/Users/luzihang/Desktop/DexScreener/test.png', call_type("中文"))

op.build_qrcode("fsdf", "abc.jpg")
#op._down_broadcast_file("C:/Users/luzihang/Desktop/DexScreener", "小飞棍来啦")
