import os
from tkinter import *
from tkinter import Tk
import tkinter
from turtle import width
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import *

 
##-----------------configurer la fenetre----------------------
 
root=Tk()
root.geometry('615x415')
root.title('IMAGE WATERMARKING USING AIR CANVAS WITH PYTHON')
root.config(bg='beige')



            
##-----------------------fonctions-----------------------
                  #----fct° upload image-----
def upload_image():
    global image_originale
    filename = filedialog.askopenfilename(filetypes=[('Image Files', '.jpg'), ('Image Files', '.png')])
    img=Image.open(filename)
    img.save("image_originale.jpg")
    img_resized=img.resize((300,250)) 
    image_originale =ImageTk.PhotoImage(img_resized)
    ci = Canvas(root, width=275, height=250, bg='beige')
    ci.create_image(0,0,anchor=NW,image=image_originale)
    ci.place(x=5,y=200)
    
                  #----fct° open canva-----

def open_aircanvas():
    os.system("python3 canvas.py")
    
    
                  #----fct° apply watermark-----
def apply_watermark():
    os.system("python3 Watermark_Algorithm-main\watermark.py --input=image_originale.jpg --output=output_image.jpg --wimage watermark_image.jpg --wposx=0 --wposy=300 --verbose")
                          
                  
                  
                  #----fct° show watermarked image-----
def show_result():
    global resultat_final
    load= Image.open("output_image.jpg")
    resultat = load.resize((300,250))
    resultat_final = ImageTk.PhotoImage(resultat)
    cr = Canvas(root, width=275, height=250, bg='beige')
    cr.create_image(0,0,anchor=NW,image=resultat_final)
    cr.place(x=320,y=200)    
   


##-----------------------Image_Originale------------------------
 
l1=Frame(root,width=275,height=150)
l1.place(x=5,y=5,height=200,width=300)

        #canvas
c1=Canvas(l1,width=210,height=50,bg='beige')
txt=c1.create_text(100,30,text='Original Image',font='Arial 15',fill='black')
c1.pack(side=TOP,padx=5,pady=5)

        #boutons
    
bouton1=Button(l1,text="Select image",command=upload_image)
bouton1.pack(side=LEFT,padx=100,pady=0)


##-----------------------Watermark------------------------

l2=Frame(root,width=275,height=20,borderwidth=2)
l2.place(x=310,y=5,height=200,width=300)

        #  canvas
c2=Canvas(l2,width=210,height=50,bg='beige')

txt=c2.create_text(100,30,text='Create signature watermark',font='Arial 12',fill='black')
c2.pack(side=TOP,padx=5,pady=5)

     # boutons
   
bouton2=Button(l2,text="Open Canvas",command=open_aircanvas)
bouton2.pack(side=LEFT,padx=5,pady=0)

bouton3=Button(l2,text="Apply Watermark",command=apply_watermark)
bouton3.pack(side=LEFT,padx=10,pady=0)

bouton4=Button(l2,text="See Result",command=show_result)
bouton4.pack(side=LEFT,padx=8,pady=0)



root.mainloop()