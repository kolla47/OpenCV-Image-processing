from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
import numpy as np
import PIL.Image
import PIL.ImageTk

class Editor(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.title('Image Editor')
		self.resizable(0,0)

		self.imageLabel = Label(self)
		self.imageLabel.grid(row=0,column=0)


		self.butFrame = Frame(self)
		self.butFrame.grid(row=0,column=1)

		self.buttonOpen			= Button(self.butFrame, 		text='Open image', 		command=self.openImage					).pack(fill=BOTH)
		self.flipLabel 			= Label(self.butFrame)
		self.flipLabel.pack()
		self.flipText			= Label(self.flipLabel, 		text='Flip:'													).pack(fill=BOTH, side='left')
		self.buttonFlipHor 		= Button(self.flipLabel,		text='Horiz',			command=lambda: self.flip('HORIZONTAL')	).pack(fill=BOTH, side='left')
		self.buttonFlipVer 		= Button(self.flipLabel,		text='Vert',			command=lambda: self.flip('VERTICAL')	).pack(fill=BOTH, side='right')
		self.brightLabel		= Label(self.butFrame)
		self.brightLabel.pack()
		self.brightText			= Label(self.brightLabel,		text='Brightness:'												).pack(fill=BOTH, side='left')
		self.buttonBrightUp		= Button(self.brightLabel,		text='Up',				command=lambda: self.brightness('UP')	).pack(fill=BOTH, side='left')
		self.buttonBrightDown	= Button(self.brightLabel,		text='Down',			command=lambda: self.brightness('DOWN')	).pack(fill=BOTH, side='right')
		self.contrastLabel		= Label(self.butFrame)
		self.contrastLabel.pack()
		self.contrastText		= Label(self.contrastLabel, 	text='Contrast:'												).pack(fill=BOTH, side='left')
		self.buttonContrastUp	= Button(self.contrastLabel,	text='Up',				command=lambda: self.contrast('UP')		).pack(fill=BOTH, side='left')
		self.buttonContrastDown	= Button(self.contrastLabel,	text='Down',			command=lambda: self.contrast('DOWN')	).pack(fill=BOTH, side='right')
		self.buttonGray 		= Button(self.butFrame, 		text='Grayscale', 		command=self.grayscale 					).pack(fill=BOTH)
		self.buttonNeg			= Button(self.butFrame, 		text='Negative',		command=self.negative 					).pack(fill=BOTH)
		self.buttonCanny		= Button(self.butFrame, 		text='Detect Edge',		command=self.canny						).pack(fill=BOTH)
		self.buttonBlur			= Button(self.butFrame, 		text='Blur',			command=self.blur 						).pack(fill=BOTH)
		self.buttonSharp 		= Button(self.butFrame, 		text='Sharpen', 	    command=self.sharpen    				).pack(fill=BOTH)
		self.buttonBin			= Button(self.butFrame, 		text='Binary',			command=self.binary						).pack(fill=BOTH)
		self.BGRText			= Label(self.butFrame, 			text='BGR:'													    ).pack(fill=BOTH)
		self.BGRLabel 			= Label(self.butFrame)
		self.BGRLabel.pack()
		self.buttonB			= Button(self.BGRLabel,			text='B',				command=lambda: self.BGR('B')			).pack(fill=BOTH, side='left')
		self.buttonG			= Button(self.BGRLabel,			text='G',				command=lambda: self.BGR('G')			).pack(fill=BOTH, side='left')
		self.buttonR			= Button(self.BGRLabel,			text='R',				command=lambda: self.BGR('R')			).pack(fill=BOTH, side='left')
		self.HSVText			= Label(self.butFrame, 			text='HSV:'													    ).pack(fill=BOTH)
		self.HSVLabel 			= Label(self.butFrame)
		self.HSVLabel.pack()
		self.buttonB			= Button(self.HSVLabel,			text='H',				command=lambda: self.HSV('H')			).pack(fill=BOTH, side='left')
		self.buttonG			= Button(self.HSVLabel,			text='S',				command=lambda: self.HSV('S')			).pack(fill=BOTH, side='left')
		self.buttonR			= Button(self.HSVLabel,			text='V',				command=lambda: self.HSV('V')			).pack(fill=BOTH, side='left')
		self.rotateLabel		= Label(self.butFrame)
		self.rotateLabel.pack()
		self.rotateText			= Label(self.rotateLabel, 		text='Rotate:'													).pack(fill=BOTH, side='left')
		self.buttonRotLeft		= Button(self.rotateLabel,		text='Left',			command=lambda: self.rotate('LEFT')		).pack(fill=BOTH, side='left')
		self.buttonRotRight		= Button(self.rotateLabel, 		text='Right',			command=lambda: self.rotate('RIGHT')	).pack(fill=BOTH, side='right')
		self.buttonSave			= Button(self.butFrame, 		text='Save image', 		command=self.saveImage					).pack(fill=BOTH)
		

	def updateLabel(self, img):
		tempImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
		tempImg = PIL.Image.fromarray(tempImg)
		tempImg = PIL.ImageTk.PhotoImage(image=tempImg)
		self.imageLabel.configure(image=tempImg)
		self.imageLabel.image = tempImg

	def openImage(self, filename=None):
		if filename is None:
			try:
				filename = filedialog.askopenfilename(initialdir='~/Pictures',title='Open image')
			except(OSError, FileNotFoundError):
				messagebox.showerror('Error','Unable to find or open file <filename>')
			except Exception as error:
				messagebox.showerror('Error','An error occurred: <error>')

		if filename:
			self.image = cv2.imread(filename)	
			self.updateLabel(self.image)

	def saveImage(self):
		try:
			filename = filedialog.asksaveasfilename(initialdir='~/Pictures',title='Save image')
		except Exception as error:
			messagebox.showerror('Error','An error occurred: <error>')

		if filename:
			cv2.imwrite(filename, self.image)

	def flip(self, option):
		h, w, _ = self.image.shape
		temp = np.zeros((h,w,3), np.uint8)
		if option == 'HORIZONTAL':
			for i in range(0,w):
				temp[:,i,:] = self.image[:,w-i-1,:]
		elif option == 'VERTICAL':
			for j in range(0,h):
				temp[j,:,:] = self.image[h-j-1,:,:]
		self.image = temp
		self.updateLabel(self.image)

	def grayscale(self):
		b = self.image[:,:,0]
		g = self.image[:,:,1]
		r = self.image[:,:,2]
		gray = 0.114*b + 0.587*g + 0.299*r
		self.image[:,:,0] = self.image[:,:,1] = self.image[:,:,2] = gray
		self.updateLabel(self.image)

	def sharpen(self):
		kernel = np.array([[-1,-1,-1], 
                 		   [-1, 9,-1],
                   		   [-1,-1,-1]])
		self.image = cv2.filter2D(self.image, -1, kernel)
		self.updateLabel(self.image)

	def brightness(self, option):
		if option == 'UP':
			bias = 20
		elif option == 'DOWN':
			bias = -20
		self.image = cv2.addWeighted(self.image, 1, np.zeros(self.image.shape, self.image.dtype), 0, bias)
		self.updateLabel(self.image)

	def contrast(self, option):
		if option == 'UP':
			gain = 1.25
		elif option == 'DOWN':
			gain = 0.8
		self.image = cv2.addWeighted(self.image, gain, np.zeros(self.image.shape, self.image.dtype), 0, 0)
		self.updateLabel(self.image)

	def BGR(self, option):
		height=self.image.shape[0]
		width=self.image.shape[1]
		B,G,R=cv2.split(self.image)
		zeros=np.zeros((height,width),dtype="uint8")
		if option == 'B':
			self.image=cv2.merge([B,zeros,zeros])
		elif option == 'G':
			self.image=cv2.merge([zeros,G,zeros])
		elif option == 'R':
			self.image=cv2.merge([zeros,zeros,R])
		self.updateLabel(self.image)

	def HSV(self, option):
		img_HSV=cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
		if option == 'H':
			self.image=img_HSV[:,:,0]
		elif option == 'S':
			self.image=img_HSV[:,:,1]
		elif option == 'V':
			self.image=img_HSV[:,:,2]
		self.updateLabel(self.image)

	def negative(self):
		self.image[:,:,:] = 255 - self.image[:,:,:]
		self.updateLabel(self.image)

	def blur(self):
		self.image = cv2.GaussianBlur(self.image,(3,3),0)
		self.updateLabel(self.image)

	def canny(self):
		self.image = cv2.Canny(self.image,20,170)
		self.updateLabel(self.image)

	def binary(self):
		img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
		_,self.image = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
		self.updateLabel(self.image)

	def rotate(self, option):
		h, w, _ = self.image.shape
		temp = np.zeros((w,h,3), np.uint8)
		if option == 'LEFT':
			for i in range(0,w):
				temp[w-i-1,:,:] = self.image[:,i,:]
		elif option == 'RIGHT':
			for j in range(0,h):
				temp[:,h-j-1,:] = self.image[j,:,:]
		self.image = temp
		self.updateLabel(self.image)
if __name__ == '__main__':
	app = Editor()
	app.mainloop()