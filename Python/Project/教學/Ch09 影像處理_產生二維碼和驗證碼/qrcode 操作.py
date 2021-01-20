import qrcode

# make(): 會傳回一個 qrcode.image.pil.PilImage 物件
qrcode_img = qrcode.make("https://ceq.nkust.edu.tw/Home/StdIndex")
qrcode_img.save("./教學意見調查表.png")
# print("executed.")

# 上面是按照 qrcode 的預設方式產生二維碼，若希望產生不同尺寸的二維碼，則需要使用 QRCode 類別
# QRCode(version=None, error_correction=constants.ERROR_CORRECT_M, box_size=10, border=4, image_factory=None)
# 參數說明
# version: 指二維碼的版本(1~40)，最小為1，對應尺寸為 21x21，每增加一個版本會增加4個尺寸(指的是二維碼的長寬平均分為多少份)
# error_correction: 校正容量，ERROR_CORRECT_L/M/Q/H，分別為 7/15/25/30% 的錯誤修正，預設為 M
# box_size: 圖片的像素
# border: 表示二維碼的邊框寬度，4為最小值
# for example:
holo = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

# holo.add_data("https://hololive.jetri.co/#/")
# holo.make(fit=True)
# holo_qrcode = holo.make_image()
# holo_qrcode.save("./holotools.png")
# QRCode 物件的 make_image() 函數可以透過改變 fill_color, back_color 參數來改變所產生圖片的背景顏色格子顏色

# 產生其他類型的二維碼
pass
