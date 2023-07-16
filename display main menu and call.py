def Main_Menu():
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Bank Management System - 	CopyAssignment")
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(text="BANK MANAGEMENT SYSTEM ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Verdana","40","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new.gif")
	imglo=tk.PhotoImage(file="login.gif")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)

	b1=tk.Button(image=imgc,command=Create)
	b1.image=imgc
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b2.image=imglog
	img6=tk.PhotoImage(file="quit.gif")
	myimg6=img6.subsample(2,2)

	b6=tk.Button(image=myimg6,command=rootwn.destroy)
	b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=920,y=400)

	rootwn.mainloop()

Main_Menu()