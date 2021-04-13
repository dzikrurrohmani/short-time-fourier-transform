import tkinter
import numpy as np
from tkinter import ttk
from tkinter import scrolledtext as tkst
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


class Example(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        f1 = GradientFrame(self, width=200, height=600, bd=0, highlightthickness=0)
        f1.pack(side="left", fill="both", expand=True)
        f1.pack_propagate(0)
        round_rectangle(f1, 10, 10, 200, 590, radius=25, fill="#545454")
        round_rectangle(f1, 12, 12, 198, 588, radius=25, fill="#dedede")
        f1_1 = tkinter.Frame(f1, width=200, height=600, bd=0, highlightthickness=0, background="#dedede")
        f1_1.pack(padx=(15, 3), pady=15, side="left", fill="both", expand=True)
        f1_1.pack_propagate(0)
        f2 = GradientFrame(self, width=500, height=600, bd=0, highlightthickness=0)
        f2.pack(side="left", fill="both", expand=True)
        f2.pack_propagate(0)
        round_rectangle(f2, 10, 10, 490, 590, radius=25, fill="#545454")
        round_rectangle(f2, 12, 12, 488, 588, radius=25, fill="#dedede")
        f2_1 = tkinter.Frame(f2, width=450, height=600, bd=0, highlightthickness=0, bg="#dedede")
        f2_1.pack(padx=(15), pady=15)
        f2_1.pack_propagate(0)

        labeldata = tkinter.Label(f1_1, text="INPUT", bg="#dedede")
        labeldata.pack(pady=(5, 10))

        part01_1 = tkinter.Frame(f1_1, bg="#dedede")
        part01_1.pack()
        self.inputan = tkinter.StringVar(part01_1)
        my_combobox = ttk.Combobox(part01_1, width=9, textvariable=self.inputan)
        my_combobox['values'] = ('Test', 'Data')
        my_combobox.configure(justify="center")
        my_combobox.pack(padx=(10, 0), side="left")
        my_button_1 = tkinter.Button(part01_1, text='SET', width=9, command=set_input)
        my_button_1.pack(padx=10, side="left")

        labelwindow = tkinter.Label(f1_1, text="WINDOW TYPE", bg="#dedede")
        labelwindow.pack(pady=(15, 8))

        part01_2 = tkinter.Frame(f1_1, bg="#dedede")
        part01_2.pack()
        part01_2_1 = tkinter.Frame(part01_2, bg="#dedede")
        part01_2_1.pack(side="left")
        part01_2_2 = tkinter.Frame(part01_2, bg="#dedede")
        part01_2_2.pack(side="left")

        self.wintype = tkinter.IntVar(f1)
        r0 = tkinter.Radiobutton(part01_2_1, text='Rectangular', variable=self.wintype, value=0, background='#dedede')
        r0.pack(anchor=tkinter.W)
        r1 = tkinter.Radiobutton(part01_2_1, text='Triangular', variable=self.wintype, value=1, background='#dedede')
        r1.pack(anchor=tkinter.W)
        r0 = tkinter.Radiobutton(part01_2_2, text='Hamming', variable=self.wintype, value=2, background='#dedede')
        r0.pack(anchor=tkinter.W)
        r1 = tkinter.Radiobutton(part01_2_2, text='Hanning', variable=self.wintype, value=3, background='#dedede')
        r1.pack(anchor=tkinter.W)

        labelprop = tkinter.Label(f1_1, text="PROPERTIES", bg="#dedede")
        labelprop.pack(pady=(10, 0))

        part01_3 = tkinter.Frame(f1_1, bg="#dedede")
        part01_3.pack()

        mf1_help1 = tkinter.Frame(part01_3, width=100, height=160, bg='#dedede')
        mf1_help1.pack(padx=(5, 0), side=tkinter.LEFT)
        mf1_help1.pack_propagate(0)
        mf1_help2 = tkinter.Frame(part01_3, width=20, height=160, bg='#dedede')
        mf1_help2.pack(side=tkinter.LEFT)
        mf1_help2.pack_propagate(0)
        mf1_help3 = tkinter.Frame(part01_3, width=75, height=160, bg='#dedede')
        mf1_help3.pack(side=tkinter.LEFT)
        mf1_help3.pack_propagate(0)

        self.mf1_entry1 = tkinter.Spinbox(mf1_help3, from_=0, to=None, width=5, command=win_plot)
        self.mf1_entry1.pack(pady=11)
        self.mf1_entry2 = tkinter.Spinbox(mf1_help3, from_=0, to=None, width=5, command=win_plot)
        self.mf1_entry2.pack()
        self.mf1_entry3 = tkinter.Entry(mf1_help3, width=6)
        self.mf1_entry3.pack(pady=11)
        self.mf1_entry4 = tkinter.Entry(mf1_help3, width=6)
        self.mf1_entry4.pack()
        self.mf1_entry5 = tkinter.Entry(mf1_help3, width=6)
        self.mf1_entry5.pack(pady=11)

        mf1_label1_1 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Wind. Size (Nw)", bg='#dedede')
        mf1_label1_1.pack(pady=9)
        mf1_label1_2 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Shifting (Ns)", bg='#dedede')
        mf1_label1_2.pack()
        mf1_label1_3 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Max Wind. (n)", bg='#dedede')
        mf1_label1_3.pack(pady=9)
        mf1_label1_4 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Freq. Min (Hz)", bg='#dedede')
        mf1_label1_4.pack()
        mf1_label1_5 = tkinter.Label(mf1_help1, anchor="w", width=13, text="Freq. Max (Hz)", bg='#dedede')
        mf1_label1_5.pack(pady=9)

        mf1_label2_1 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#dedede')
        mf1_label2_1.pack(pady=9)
        mf1_label2_2 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#dedede')
        mf1_label2_2.pack()
        mf1_label2_3 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#dedede')
        mf1_label2_3.pack(pady=9)
        mf1_label2_4 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#dedede')
        mf1_label2_4.pack()
        mf1_label2_5 = tkinter.Label(mf1_help2, text=":", anchor="w", bg='#dedede')
        mf1_label2_5.pack(pady=9)

        part01_4 = tkinter.Frame(f1_1, bg="#dedede")
        part01_4.pack(pady=(5, 10), fill="x")
        my_button_2 = tkinter.Button(part01_4, text='STFT', width=9, command=STSF)
        my_button_2.pack(padx=(9, 0), side="left")
        my_button_3 = tkinter.Button(part01_4, text='CLEAR', width=9, command=None)
        my_button_3.pack(padx=(20, 0), side="left")

        labeltkst = tkinter.Label(f1_1, text="INSTRUCTION", bg="#dedede")
        labeltkst.pack(pady=(2, 4))

        part01_5 = tkinter.Frame(f1_1, bg="#dedede")
        part01_5.pack()

        self.part01_5_tkst1 = tkst.ScrolledText(part01_5, wrap=tkinter.WORD, width=24, height=10,
                                                     background='white')
        self.part01_5_tkst1.pack(pady=5, fill=tkinter.BOTH, expand=True)
        self.part01_5_tkst1.configure(font="TkTextFont")
        self.part01_5_tkst1.configure(foreground="black")
        self.part01_5_tkst1.configure(highlightbackground="#e2e6e2")
        self.part01_5_tkst1.configure(highlightcolor="black")
        self.part01_5_tkst1.configure(insertbackground="black")
        self.part01_5_tkst1.configure(insertborderwidth="3")
        self.part01_5_tkst1.configure(selectbackground="#c4c4c4")
        self.part01_5_tkst1.configure(selectforeground="black")

        part02_1 = tkinter.Frame(f2_1, bg="#dedede")
        part02_1.pack()
        self.ax1 = Axis(part02_1, "INPUT DATA", "Detik", "Amplitudo")

        part02_2 = tkinter.Frame(f2_1, bg="#dedede")
        part02_2.pack(pady=(10, 2), fill="both")
        self.ax2 = Ax3D(part02_2, "STFT", "Time", "Frequency", "Magnitude")


class GradientFrame(tkinter.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''

    def __init__(self, parent, color1="#7e7e7e", color2="#212121", **kwargs):
        tkinter.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = height
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(0, i, width, i, tags=("gradient",), fill=color)
        self.lower("gradient")


def round_rectangle(loc, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    loc.create_polygon(points, **kwargs, smooth=True)


class Plot:
    def __init__(self, id, x, y, kondisi, color):
        self.id = id
        self.x = x
        self.y = y
        self.kondisi = kondisi
        self.color = color


class Axis:
    def __init__(self, top, judul, labelx, labely):
        self.master = top
        self.labelx = labelx
        self.labely = labely
        self.title = judul
        self.fig = Figure(figsize=(6, 1.1))
        self.fig.set_facecolor('#dedede')
        self.grafik_windows = FigureCanvasTkAgg(self.fig, self.master)
        self.ax = self.fig.add_subplot(111)
        self.grafik_windows.get_tk_widget().pack(pady=(0, 7))
        self.Attribute()
        box = self.ax.get_position()
        self.ax.set_position([box.x0 - box.width * 0.04, box.y0 + box.height * 0.18,
                              box.width * 1.15, box.height * 0.7])
        self.toolbar = NavigationToolbar2Tk(self.grafik_windows, self.master)
        self.toolbar.config(background='#dedede')
        self.toolbar._message_label.config(background='#dedede')
        self.toolbar.update()
        self.grafik_windows.mpl_connect("key_press_event", self.on_key_press)

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.grafik_windows, self.toolbar)

    def Attribute(self):
        self.ax.set_title(self.title, fontsize=8)
        self.ax.set_xlabel(self.labelx, fontsize=8)
        self.ax.set_ylabel(self.labely, fontsize=8)
        self.ax.tick_params(direction='in', labelsize=6)

    def draw_plot(self):
        self.ax.clear()
        self.Attribute()
        for item in self.plotlist:
            if item.kondisi == 0:
                self.ax.plot(item.x, item.y, color=item.color, linewidth=0.5)
            elif item.kondisi == 1:
                self.ax.bar(item.x, item.y, color=item.color, width=1)
        self.grafik_windows.draw()

    def plot(self, x, y, kondisi=0, color='blue'):
        self.plotlist = []
        self.add_plot(0, x, y, kondisi, color)

    def add_plot(self, id, x, y, kondisi=0, color='blue'):
        for i, item in enumerate(self.plotlist):  # Jika ada plot dengan id yg sama
            if item.id == id:
                self.plotlist[i] = Plot(id, x, y, kondisi, color)
                self.draw_plot()
                return

        self.plotlist += [Plot(id, x, y, kondisi, color)]  # Jika belum ada plot dengan id yang ditentukan
        self.draw_plot()

    def clearfig(self):
        self.ax.clear()
        self.Attribute()
        self.grafik_windows.draw()

class Pl3D:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

class Ax3D:
    def __init__(self, top, judul, labelx, labely, labelz):
        self.master = top
        self.labelx = labelx
        self.labely = labely
        self.labelz = labelz
        self.title = judul
        self.CB_state = False
        self.fig = Figure(figsize=(4.5, 3.65))
        self.fig.set_facecolor('#dedede')
        self.grafik_windows = FigureCanvasTkAgg(self.fig, self.master)
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_facecolor('#dedede')
        self.ax.figure.subplots_adjust(left=0, bottom=0, right=1, top=1)
        self.grafik_windows.get_tk_widget().pack(pady=(0, 7))
        self.Attribute()
        box = self.ax.get_position()
        # self.ax.set_position([box.x0 - box.width * 0.15, box.y0 - box.height * 0.1,
        #                       box.width * 1.2, box.height * 1.2])
        self.ax.set_position([box.x0 - box.width * 0.01, box.y0,
                              box.width * 0.95, box.height])
        self.ax.view_init(22,-58)
        self.toolbar = NavigationToolbar2Tk(self.grafik_windows, self.master)
        self.toolbar.config(background='#dedede')
        self.toolbar._message_label.config(background='#dedede')
        self.toolbar.update()
        self.grafik_windows.mpl_connect("key_press_event", self.on_key_press)


    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.grafik_windows, self.toolbar)

    def Attribute(self):
        self.ax.set_title(self.title, fontsize=8)
        self.ax.set_xlabel(self.labelx, fontsize=8)
        self.ax.set_ylabel(self.labely, fontsize=8)
        self.ax.set_zlabel(self.labelz, fontsize=8)
        self.ax.tick_params(direction='in', labelsize=6)

    def plot(self, x, y, z):
        self.ax.clear()
        self.Attribute()
        if self.CB_state == True: self.CB.remove()
        self.CB_state = True
        # self.ax.plot_trisurf(x, y, z, cmap="magma")
        self.surf = self.ax.plot_surface(x, y, z, cmap="magma",
                               linewidth=5)
        self.CB = self.fig.colorbar(self.surf, shrink=0.5, aspect=5)
        self.grafik_windows.draw()

    def clearfig(self):
        self.ax.clear()
        self.Attribute()
        self.grafik_windows.draw()



def set_input():
    global x_input, y_input, N, fs

    N = 2000
    fs = 800
    amp_1 = 0.1
    freq_1 = 50
    amp_2 = 0.15
    freq_2 = 100
    amp_3 = 0.3
    freq_3 = 150
    amp_4 = 0.25
    freq_4 = 250
    x_input, y_input = np.arange(N) / fs, []

    try:
        if mainFrame.inputan.get() == 'Test':
            for i in range(int(N / 4)): y_input += [amp_1 * np.sin(2 * np.pi * freq_1 * i / fs)]
            for i in range(int(N / 4), int((2 * N) / 4)): y_input += [amp_2 * np.sin(2 * np.pi * freq_2 * i / fs)]
            for i in range(int(N / 2), int((3 * N) / 4)): y_input += [amp_3 * np.sin(2 * np.pi * freq_3 * i / fs)]
            for i in range(int((3 * N) / 4), N): y_input += [amp_4 * np.sin(2 * np.pi * freq_4 * i / fs)]
        elif mainFrame.inputan.get() == 'Data':
            pass
    except:
        mb.showerror("Error", "Please choose training data that you want to learn!")
        return

    mainFrame.ax1.plot(x_input, y_input)
    # mainFrame.ax1.plot([], [])
    mainFrame.mf1_entry1.__setitem__('to', N)
    mainFrame.mf1_entry1.__setitem__('from_', 1)
    mainFrame.mf1_entry2.__setitem__('to', N)
    mainFrame.mf1_entry2.__setitem__('from_', 1)
    mainFrame.mf1_entry1.delete(0, tkinter.END)
    mainFrame.mf1_entry1.insert(0, 100)
    mainFrame.mf1_entry2.delete(0, tkinter.END)
    mainFrame.mf1_entry2.insert(0, 20)
    mainFrame.mf1_entry3.delete(0, tkinter.END)
    mainFrame.mf1_entry3.insert(0, "-")
    mainFrame.mf1_entry4.delete(0, tkinter.END)
    mainFrame.mf1_entry4.insert(0, 1)
    mainFrame.mf1_entry5.delete(0, tkinter.END)
    mainFrame.mf1_entry5.insert(0, 400)

def DFT(yy):
    FFT = np.fft.fft(yy)
    FFT_r = FFT.real
    FFT_i = FFT.imag
    z = []
    for i in range(np.size(FFT_r)):
        z += [(np.sqrt((FFT_r[i] ** 2) + (FFT_i[i] ** 2))) / np.size(FFT_r)]
    return z
    # n = np.size(yy)
    # DFT_r = np.zeros([n])
    # DFT_i = np.zeros([n])
    # y_data = np.zeros([n])
    # for i in range(n):
    #     for j in range(n):
    #         a_1 = yy[j] * np.cos((2 * np.pi * i * j) / n)
    #         a_2 = -(yy[j] * np.sin((2 * np.pi * i * j) / n))
    #         DFT_r[i] += a_1
    #         DFT_i[i] += a_2
    #     y_data[i] = (np.sqrt((DFT_r[i] ** 2) + (DFT_i[i] ** 2))) / n
    # return y_data

def win_plot():
    global ws, shifting, n_win, windows

    ws = int(mainFrame.mf1_entry1.get())  # window size
    shifting = int(mainFrame.mf1_entry2.get())
    w_n = np.zeros([4, ws])
    n_win = int(np.ceil((N-ws)/shifting)+1)
    mainFrame.mf1_entry3.delete(0, tkinter.END)
    mainFrame.mf1_entry3.insert(0, n_win)

    for j in range(ws):
        w_n[0][j] = 1
        w_n[1][j] = 1-(abs(2*j-ws+1)/(ws-1))
        w_n[2][j] = 0.54-(0.46*np.cos((2*np.pi*j)/(ws-1)))
        w_n[3][j] = 0.5-(0.5*np.cos((2*np.pi*j)/(ws-1)))

    windows = np.zeros([n_win, N])
    for i in range(n_win):
        window = np.zeros([N])
        if i==n_win-1:
            j = 0
            while (i*shifting)+j < N:
                window[(i*shifting)+j] = w_n[int(mainFrame.wintype.get())][j]
                j += 1
        else:
            for j in range(ws):
                window[(i*shifting)+j] = w_n[int(mainFrame.wintype.get())][j]
        windows[i] = window

    mainFrame.ax1.plot(x_input, y_input)
    # mainFrame.ax1.plot(np.arange(N)/fs, np.zeros([N]))
    for i in range(n_win):
        mainFrame.ax1.add_plot(i+1, np.arange(N)/fs, windows[i])


def STSF():
    global x_input, y_input, ws, shifting, n_win

    STFT = np.zeros([n_win, int(N/2)])
    for i in range(n_win):
        windowed = np.zeros([N])
        for j in range(N):
            windowed[j] = y_input[j]*windows[i][j]
        y_DFT = DFT(windowed)
        STFT[i] = y_DFT[0:int(N/2)]

    if np.amax(STFT) > 0:
        STFT = STFT / np.amax(STFT)  # agar tidak terjadi gain

    freq_plot = list(map(lambda x: (x * fs)/N, np.arange(int(N/2))))
    X, Y = np.meshgrid((np.arange(n_win)*N)/(n_win*fs), freq_plot)

    # print(n_win, ws)
    #
    # print("--------------------------------------------------------------------")
    # print(np.size(X), np.size(X[1]))
    # print("--------------------------------------------------------------------")
    # print(np.size(Y), np.size(Y[1]))
    # print("--------------------------------------------------------------------")
    # print(np.size(STFT), np.size(STFT[1]))

    # mainFrame.ax2.plot(Y.flatten() ,X.flatten() ,STFT.flatten())
    mainFrame.ax2.plot(X ,Y ,STFT.transpose())

def scrolledtext_init():
    mainFrame.part01_5_tkst1.delete('1.0', tkinter.END)
    mainFrame.part01_5_tkst1.insert(tkinter.INSERT, """Welcome to Time Frequency Analysis Program with STFT Algorithm \
Created by Dzikrur Rohmani Z R M H, BME Dept. ITS\n\nPlease choose data that you want to Analyze!\n\n""")

if __name__ == "__main__":
    # Make a Tkinter Canvas
    window = tkinter.Tk()
    window.title("STFT")
    window.geometry("+250+10")
    window.resizable(False, False)
    # window.attributes('-alpha', 0.98)
    mainFrame = Example(window)
    mainFrame.pack(fill="both", expand=True)

    scrolledtext_init()

    window.mainloop()
