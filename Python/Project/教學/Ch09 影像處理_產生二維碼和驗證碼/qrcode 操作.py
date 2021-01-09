import qrcode

# make(): 會傳回一個 qrcode.image.pil.PilImage 物件
QRCode = qrcode.make("https://ceq.nkust.edu.tw/Home/StdIndex")
QRCode.save("./教學意見調查表.png")
# print("executed.")


