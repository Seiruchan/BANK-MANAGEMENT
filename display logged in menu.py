def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("CopyAssignment Bank | Welcome - "+name)
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="blue3",font=("Times",16),fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="balance1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction.gif")
	myimg5=img5.subsample(2,2)
	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	b5.image=myimg5
	
	img6=tk.PhotoImage(file="logout.gif")
	myimg6=img6.subsample(2,2)
	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
	b6.image=myimg6
	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b6.place(x=500,y=400)