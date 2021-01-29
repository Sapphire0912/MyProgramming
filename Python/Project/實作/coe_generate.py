from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2



# print(pic[60][60])  # BGR

# l = list()
# l2 = list()
# for i in range(128):
#     for j in range(128):
#         s = ""
#         for k in pic[i][j]:
#             if k > 200:
#                 s += '1'
#             else:
#                 s += '0'
#         l.append(s)
# print(len(l))
# print(len(l2))



def img_file():
    global path

    file_type = [
        'jpg', 'jpeg', 'png', 'bmp'
    ]
    path = filedialog.askopenfilename()  # get file path
    target_name = path.split("/")  # get filename and type. ex. filename.jpg

    try:
        if target_name[-1].split('.')[-1] not in file_type:
            messagebox.showerror("錯誤1", "檔案類型不是jpg, jpeg, png, bmp")

        img_type = img_type_val.get()  # get output type
        img = cv2.imread(path)  # get image array
        img = cv2.cvtColor(img, img_type)  # using img_type open image
        x, y = img.shape[0], img.shape[1]  # get height, width
        # display image
        img_canvas = Canvas(win, width=y, height=x)
        img_canvas.place(x=180, y=0)

        img_trans = ImageTk.PhotoImage(Image.fromarray(img))  # array into image
        img_canvas.create_image(0, 0, anchor=NW, image=img_trans)
        img_canvas.img = img_trans

    except cv2.error:
        pass


def transform():
    pass


# global variable
ft = ('標楷體', 14)
path = ""

# interface
win = Tk()
win.geometry('960x600')
win.title('coe 文件生成')

# choose digits type
frame_digits = Frame(win)
digits_label = LabelFrame(frame_digits, text='選擇進制', font=('標楷體', '14', 'bold'))
digits_val = IntVar()
digits_val.set(2)
digits_2 = Radiobutton(digits_label, text='2進位', variable=digits_val, value=2, font=ft)
digits_8 = Radiobutton(digits_label, text='8進位', variable=digits_val, value=8, font=ft)
digits_10 = Radiobutton(digits_label, text='10進位', variable=digits_val, value=10, font=ft)
digits_16 = Radiobutton(digits_label, text='16進位', variable=digits_val, value=16, font=ft)

digits_2.grid(column=0, row=1, sticky='w')
digits_8.grid(column=0, row=2, sticky='w')
digits_10.grid(column=0, row=3, sticky='w')
digits_16.grid(column=0, row=4, sticky='w')
digits_label.grid(column=0, row=0, sticky='w')
frame_digits.place(x=0, y=0)

# choose image type
frame_img_type = Frame(win)
img_label = LabelFrame(frame_img_type, text='輸出格式', font=('標楷體', '14', 'bold'))
img_type_val = IntVar()
img_type_val.set(cv2.COLOR_BGR2GRAY)
img_gray = Radiobutton(img_label, text='灰階', variable=img_type_val, value=cv2.COLOR_BGR2GRAY, font=ft)
image_full_color = Radiobutton(img_label, text='RGB', variable=img_type_val, value=cv2.COLOR_BGR2RGB, font=ft)

img_gray.grid(column=0, row=6, sticky='w')
image_full_color.grid(column=0, row=7, sticky='w')
img_label.grid(column=0, row=5, sticky='w')
frame_img_type.place(x=0, y=150)

# setting value(width, depth)
desc = "" \
       "    width: 單筆資料長度\n" \
       "depth: 幾筆資料\n" \
       "threshold: 區分顏色門檻"

frame_val = Frame(win)
val_label = LabelFrame(frame_val, text='輸出目標資料', font=('標楷體', '14', 'bold'))
description = Label(val_label, text=desc, font=ft)
width_label = Label(val_label, text='width: ', font=ft)
width_val = IntVar()
width_input = Entry(val_label, textvariable=width_val, width=10)
depth_label = Label(val_label, text='depth: ', font=ft)
depth_val = IntVar()
depth_input = Entry(val_label, textvariable=depth_val, width=10)
thres_label = Label(val_label, text='threshold: ', font=ft)
thres_val = IntVar()
thres_input = Entry(val_label, textvariable=thres_val, width=10)

description.grid(column=0, row=9, sticky='n')
width_label.grid(column=0, row=10, sticky='w')
width_input.grid(column=1, row=10, sticky='w')
depth_label.grid(column=0, row=11, sticky='w')
depth_input.grid(column=1, row=11, sticky='w')
thres_label.grid(column=0, row=12, sticky='w')
thres_input.grid(column=1, row=12, sticky='w')
val_label.grid(column=0, row=8, sticky='w')
frame_val.place(x=0, y=240)

# select file, transform button
frame_target = Frame(win)
img_button = Button(frame_target, text='選擇圖片', font=ft, command=img_file)
trans_button = Button(frame_target, text='轉換', font=ft, command=transform)
img_button.grid(column=0, row=13, sticky='w')
trans_button.grid(column=0, row=14, sticky='w')
frame_target.place(x=0, y=400)


# text
# frame_text = Frame(win)
# coe_text = Text(frame_text, height=30, width=50, state='disable', font=('標楷體', 12))
# coe_text.pack()
# frame_text.pack()

win.mainloop()

