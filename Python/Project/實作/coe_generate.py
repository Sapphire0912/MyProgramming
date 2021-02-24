from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy import sqrt
from cv2 import resize, cvtColor, error, imread
from cv2 import COLOR_BGR2RGB, COLOR_BGR2GRAY


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

        x, y = size_height_val.get(), size_width_val.get()  # get height, width
        img_type = img_type_val.get()  # get output types
        img = resize(imread(path), (y, x))  # get image array
        img = cvtColor(img, img_type)  # using img_type open image

        # display image
        img_canvas = Canvas(win, width=y, height=x)
        img_canvas.place(x=150, y=230)

        img_trans = ImageTk.PhotoImage(Image.fromarray(img))  # array into image
        img_canvas.create_image(0, 0, anchor=NW, image=img_trans)
        img_canvas.img = img_trans

    except error:
        pass


def transform():
    global coe_content

    def gray(coe_width, coe_depth, thres, img_height, img_width, base):
        if thres < -1:
            messagebox.showerror("錯誤3", "threshold 數值有錯: 範圍0~255")
        elif thres == -1:
            thres = 128

        if coe_width * coe_depth != img_height * img_width:
            messagebox.showerror("錯誤2", "資料大小和圖片的大小不符合")
        else:
            img = resize(imread(path), (img_width, img_height))
            img = cvtColor(img, COLOR_BGR2GRAY)
            # img.shape  # (wid, length)

            # image digitization (base 2 need)
            digitize = list()
            for i in range(0, img_width):
                for j in range(0, img_height):
                    s = ""
                    if img[i][j] >= thres:
                        s += "1"
                    else:
                        s += "0"
                    digitize.append(s)

            index = 0
            # coe format
            if base == 2:
                coe_format = list()
                for data_depth in range(0, coe_depth):
                    s = ""
                    while len(s) < coe_width:
                        s += digitize[index]
                        index += 1
                    coe_format.append(s)
                return coe_format
            else:
                messagebox.showinfo("資訊1", "功能尚未推出敬請期待")
                return None

    def rgb(coe_width, coe_depth, thres, img_height, img_width, base):
        if thres < -1:
            messagebox.showerror("錯誤3", "threshold 數值有錯: 範圍0~255")
        elif thres == -1:
            thres = 200

        if coe_width * coe_depth != img_height * img_width * 3:
            messagebox.showerror("錯誤2", "資料大小和圖片的大小不符合")
        else:
            img = resize(imread(path), (img_width, img_height))
            img = cvtColor(img, COLOR_BGR2RGB)
            # print(img.shape)  # (wid, length, 3)

            # image digitization (base 2 need)
            digitize = list()
            for i in range(0, img_width):
                for j in range(0, img_height):
                    s = ""
                    for color in img[i][j]:
                        if color >= thres:
                            s += "1"
                        else:
                            s += "0"
                    digitize.append(s)

            index = 0
            # coe format
            if base == 2:
                coe_format = list()
                for data_depth in range(0, coe_depth):
                    s = ""
                    while len(s) < coe_width:
                        s += digitize[index]
                        index += 1
                    coe_format.append(s)
                return coe_format
            else:
                messagebox.showinfo("資訊1", "功能尚未推出敬請期待")
                return None

    img_type = img_type_val.get()  # get output type
    width = width_val.get()  # coe width
    depth = depth_val.get()  # coe depth
    threshold = thres_val.get()  # threshold
    img_h = size_height_val.get()  # image height
    img_w = size_width_val.get()  # image width
    base_type = digits_val.get()  # get base type

    if img_type == COLOR_BGR2GRAY:
        coe_content = gray(width, depth, threshold, img_h, img_w, base_type)

    elif img_type == COLOR_BGR2RGB:
        coe_content = rgb(width, depth, threshold, img_h, img_w, base_type)

    try:
        frame_text = Frame(win)
        pos = sqrt(pow(img_w, 2) + pow(img_h, 2))

        # display text
        coe_text = Text(frame_text, height=25, width=40, state='disable')
        scroll = Scrollbar(frame_text)

        coe_text.config(state='normal')
        for text in coe_content:
            coe_text.insert("insert", text)
            coe_text.insert("insert", '\n')
        coe_text.config(state='disable')

        coe_text.config(yscrollcommand=scroll.set)  # coe_text -> scrollbar
        scroll.config(command=coe_text.yview)  # scrollbar -> coe_text

        scroll.pack(side=RIGHT, fill=Y)
        coe_text.pack()
        frame_text.place(x=(150+pos), y=230)

        coe_content = None
    except TypeError:
        pass


# global variable
ft = ('標楷體', 14)
path = ""
coe_content = None

# interface
win = Tk()
win.geometry('700x600')
win.title('coe 文件生成')

# choose base type
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
img_type_val.set(COLOR_BGR2GRAY)
img_gray = Radiobutton(img_label, text='灰階', variable=img_type_val, value=COLOR_BGR2GRAY, font=ft)
image_full_color = Radiobutton(img_label, text='RGB', variable=img_type_val, value=COLOR_BGR2RGB, font=ft)

img_gray.grid(column=0, row=6, sticky='w')
image_full_color.grid(column=0, row=7, sticky='w')
img_label.grid(column=0, row=5, sticky='w')
frame_img_type.place(x=0, y=150)

# setting value(width, depth)
desc = "" \
       "    width: 單筆資料長度\n" \
       "depth: 幾筆資料\n" \
       "threshold: 區分顏色門檻\n" \
       "(默認 灰階 128, RGB 200; 使用默認值可以不用填)\n" \
       "       size: 輸出格式的大小(默認 128*128 )"

frame_val = Frame(win)
val_label = LabelFrame(frame_val, text='輸出目標資料', font=('標楷體', '14', 'bold'))

description = Label(frame_val, text=desc, font=('標楷體', 12))
width_label = Label(val_label, text='width:', font=ft)
width_val = IntVar()
width_input = Entry(val_label, textvariable=width_val, width=10)
depth_label = Label(val_label, text='depth:', font=ft)
depth_val = IntVar()
depth_input = Entry(val_label, textvariable=depth_val, width=10)

thres_label = Label(val_label, text='threshold:', font=ft)
thres_val = IntVar()
thres_val.set(-1)
thres_input = Entry(val_label, textvariable=thres_val, width=10)

size_height_label = Label(val_label, text='size: height', font=ft)
size_height_val = IntVar()
size_height_val.set(128)
size_height_input = Entry(val_label, textvariable=size_height_val, width=10)
size_width_label = Label(val_label, text='width', font=ft)
size_width_val = IntVar()
size_width_val.set(128)
size_width_input = Entry(val_label, textvariable=size_width_val, width=10)

description.grid(column=0, row=9, sticky='w')
width_label.grid(column=0, row=10, sticky='w')
width_input.grid(column=1, row=10, sticky='w')
depth_label.grid(column=0, row=11, sticky='w')
depth_input.grid(column=1, row=11, sticky='w')

thres_label.grid(column=0, row=12, sticky='w')
thres_input.grid(column=1, row=12, sticky='w')

size_height_label.grid(column=0, row=13, sticky='w')
size_height_input.grid(column=1, row=13, sticky='w')
size_width_label.grid(column=2, row=13, sticky='w')
size_width_input.grid(column=3, row=13, sticky='w')

val_label.grid(column=0, row=8, sticky='w')
frame_val.place(x=100, y=0)

# select file, transform button
frame_target = Frame(win)
img_button = Button(frame_target, text='選擇圖片', font=ft, command=img_file)
trans_button = Button(frame_target, text='轉換', font=ft, command=transform)
using = Label(frame_target, text='目前只有2進制\nRGB(僅1bit)的功能', font=('標楷體', 10))
img_button.grid(column=0, row=14, sticky='w')
trans_button.grid(column=0, row=15, sticky='w')
using.grid(column=0, row=16, sticky='w')
frame_target.place(x=0, y=240)

win.mainloop()
