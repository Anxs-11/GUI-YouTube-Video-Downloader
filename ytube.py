from  tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

root=Tk()

root.geometry("500x600")
root.resizable(False,False)
root.title("YouTube Video Downloader")

#----------heading----------------------
heading=Label(root,text="Video Downloader")
heading.config(font=("Courier", 30))
heading.grid(row=0,column=0,columnspan=2,pady=30)

#------------paste link label--------
Label(root,text="Paste link here",padx=10,pady=10).grid(row=1,column=0,columnspan=2)

#-------link-inputfield-----------------
link=Entry(root,width=50,fg="blue")
link.grid(row=2,column=0,columnspan=2,pady=20,padx=10)

filename=""
#----------directory--button------------
def path():
    global pathin,filename
    try:
        filename=filedialog.askdirectory(title="Choose path")
    except:
        messagebox.showerror("Path not Found","Please Choose Correct Path")
    
    pathin=Label(root,text=filename,fg="blue",width=20)
    pathin.grid(row=3,column=1,pady=10)

   
Button(root,text="Browse Path",width=10,command=path,padx=35).grid(row=3,column=0,pady=10)
 


#---------quality label---------
quality=Label(root,text="Quality",padx=10,pady=10,width=25)
quality.grid(row=4,column=0)



#----------------quality-drop down box----------------
clicked=StringVar()
option_list=["high quality","low quality","audio quality"]
clicked.set(option_list[0])
drop=OptionMenu(root,clicked,*option_list)
drop.grid(row=4,column=1,pady=10)




name_v=""
path_v=""
size_v=""
status_v=""
#------------download funtion----------
def download():
        global clicked,link,size_v,name_v,path_v,status_v
        qual=clicked.get()
        url=link.get()
        if len(url)<1:
            messagebox.showerror("URL not Found","Please Input URL")
        elif filename=="" or filename=="/" :
            messagebox.showerror("URL not Found","Please Choose Path")
       
            
        else:  
            try:
                video=YouTube(url)
            except:
                messagebox.showerror("URL not Found","Please Input Correct URL")
            else:
                if qual==option_list[0]:
                    stream=video.streams.filter(progressive=True).first()
                elif qual==option_list[1]:
                    stream=video.streams.filter(progressive=True).last()
                elif qual==option_list[2]:
                    stream=video.streams.filter(only_audio=True).first()
                    
                stream.download(filename)
                t=stream.title
                name_v="Name : "+t[1:41:]+"\n"+t[41:]
                s=stream.filesize/1024000
                size_v="Size : "+str(round(s,1))+" MB"
            
                path_v="Location : "+filename
                status_v="Downloaded"
                
                pathin=Label(root,text="",fg="blue",width=20)
                pathin.grid(row=3,column=1,pady=10)
                
                link.delete(0,END)
                clicked.set(option_list[0])
            
                
                messagebox.showinfo("Vidoe Downloaded","Downloaded"+"\n"+"\n"+name_v+"\n"+size_v+"\n"+path_v)
                
            
            
            
            

#----------download--button------------
dwnd=Button(root,text="Download",width=27,padx=35,command=download)
dwnd.config(font=("Courier bold", 20))
dwnd.grid(row=6,column=0,pady=20,columnspan=2)




# --------------------------------------




root.mainloop()