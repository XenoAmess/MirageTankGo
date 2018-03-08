import MTCore
import PIL


def whiteCar(whiteImg, blackImg, whiteLight=1.0, blackLight=0.18, whiteColor=1, blackColor=1, chess=False):
    whiteImg = PIL.Image.new('RGB', blackImg.size,(255,255,255))
    return MTCore.colorfulCar(whiteImg,blackImg,whiteLight,blackLight,whiteColor,blackColor,chess)
def blackCar(whiteImg, blackImg, whiteLight=1.0, blackLight=0.18, whiteColor=1, blackColor=1, chess=False):
    blackImg = PIL.Image.new('RGB', blackImg.size,(0,0,0))
    return MTCore.grayCar(whiteImg,blackImg,whiteLight,blackLight,whiteColor,blackColor,chess)
