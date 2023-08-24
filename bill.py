from tkinter import *
import random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.img=PhotoImage(file="img\\imag.png")
        self.root.iconphoto(False,self.root.img)
        self.root.geometry("1320x760")
        self.root.state("zoomed")
        self.root.title("Billing software-maddy_creation")
        self.root.config(bg="#262928")

        #cosmetics
        self.cream = IntVar()
        self.wash = IntVar()
        self.spray = IntVar()
        self.soap = IntVar()
        self.gel = IntVar()
        self.loation = IntVar()

        #groceries
        self.rice = IntVar()
        self.oil = IntVar()
        self.dhal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #cooldrinks
        self.dew = IntVar()
        self.cola = IntVar()
        self.slice = IntVar()
        self.frooti = IntVar()
        self.bovonto = IntVar()
        self.up = IntVar()

        #cust details
        self.c_name=StringVar()
        self.mob_num = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #total stock
        self.gro = StringVar()
        self.cos = StringVar()
        self.c_drink= StringVar()

        #tax
        self.gro_tax = StringVar()
        self.cos_tax = StringVar()
        self.c_tax = StringVar()

        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg="#262928", fg="white",font=("Arial Rounded MT", 30, "bold")).pack(fill=X)

#frame1
        f1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("Arial Rounded MT", 15, "bold"), fg="#aeb8b5",bg="#262928")
        f1.place(x=0, y=80, relwidth=1)

        cust_name = Label(f1, text="Customer Name:", bg="#262928", fg="white", font=("Arial Rounded MT", 18, "bold")).grid(row=0, column=0,padx=20, pady=5)
        cust_ent = Entry(f1, width=15, textvariable=self.c_name,font="arial 15", bg="#a0a3a8",bd=7, relief=RIDGE).grid(row=0, column=1, pady=5, padx=10)

        mob_num = Label(f1, text="Mobile Number:", bg="#262928", fg="white", font=("Arial Rounded MT", 18, "bold")).grid(row=0, column=2,padx=20, pady=5)
        mob_ent= Entry(f1, width=15, textvariable=self.mob_num,font="arial 15", bg="#a0a3a8",bd=7, relief=RIDGE).grid(row=0, column=3, pady=5, padx=10)

        bill_no= Label(f1, text="Bill No:", bg="#262928", fg="white", font=("Arial Rounded MT", 18, "bold")).grid(row=0, column=4,padx=20, pady=5)
        bill_ent= Entry(f1, width=15, textvariable=self.search_bill,font="arial 15",bg="#a0a3a8", bd=7, relief=RIDGE).grid(row=0, column=5, pady=5, padx=10)

        search_but=Button(f1,text="Search",command=self.find_bill,bg="#262928",fg="white",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=20,pady=5)


#frame2
        f2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("Arial Rounded MT", 15, "bold"), fg="#aeb8b5",bg="#262928")
        f2.place(x=5, y=180, width=325, height=380)

        face_cr = Label(f2, text="Face Cream", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=0, column=0,padx=10, pady=10,sticky="w")
        face_crent= Entry(f2, width=10, textvariable=self.cream,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=0, column=1, padx=10,pady=10)

        face_wa = Label(f2, text="Face Wash", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=1, column=0,padx=10, pady=10,sticky="w")
        face_waent= Entry(f2, width=10, textvariable=self.wash,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=1, column=1, padx=10,pady=10)

        hair_sp = Label(f2, text="Hair Spray", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=2, column=0,padx=10, pady=10,sticky="w")
        hair_spent= Entry(f2, width=10, textvariable=self.spray,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=2, column=1, padx=10,pady=10)

        bath_sp= Label(f2, text="Bath Soap", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=3, column=0,padx=10, pady=10,sticky="w")
        bath_spent= Entry(f2, width=10, textvariable=self.soap,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=3, column=1, padx=10,pady=10)

        hair_gel = Label(f2, text="Hair Gel", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=4, column=0,padx=10, pady=10,sticky="w")
        hair_gelent = Entry(f2, width=10, textvariable=self.gel,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=4, column=1, padx=10,pady=10)

        body_lo= Label(f2, text="Body Loation", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=5, column=0,padx=10, pady=10,sticky="w")
        body_loent= Entry(f2, width=10, textvariable=self.loation,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=5, column=1, padx=10,pady=10)

#frame3
        f3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Groceries", font=("Arial Rounded MT", 15, "bold"), fg="#aeb8b5",bg="#262928")
        f3.place(x=340, y=180, width=325, height=380)

        rice= Label(f3, text="Rice", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=0, column=0, padx=10,pady=10, sticky="w")
        rice_ent= Entry(f3, width=10, textvariable=self.rice,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=0, column=1, padx=10,pady=10)

        oil= Label(f3, text="Food Oil", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=1, column=0,padx=10, pady=10,sticky="w")
        oil_ent= Entry(f3, width=10, textvariable=self.oil,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=1, column=1, padx=10,pady=10)

        dhal= Label(f3, text="Dhal", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=2, column=0, padx=10,pady=10, sticky="w")
        dhal_ent= Entry(f3, width=10, textvariable=self.dhal,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=2, column=1, padx=10,pady=10)

        wheat= Label(f3, text="Wheat", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=3, column=0, padx=10,pady=10, sticky="w")
        wheat_ent= Entry(f3, width=10, textvariable=self.wheat,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=3, column=1, padx=10,pady=10)

        sugar= Label(f3, text="Sugar", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=4, column=0, padx=10,pady=10, sticky="w")
        sugar_ent= Entry(f3, width=10, textvariable=self.sugar,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=4, column=1, padx=10,pady=10)

        tea = Label(f3, text="Tea", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=5, column=0, padx=10,pady=10, sticky="w")
        tea_ent = Entry(f3, width=10, textvariable=self.tea,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=5, column=1, padx=10,pady=10)

#frame 4
        f4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cool Drinks", font=("Arial Rounded MT", 15, "bold"), fg="#aeb8b5",bg="#262928")
        f4.place(x=670, y=180, width=325, height=380)

        dew= Label(f4, text="Mountain Dew", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=0, column=0,padx=10, pady=10,sticky="w")
        dew_ent = Entry(f4, width=10, textvariable=self.dew,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=0, column=1, padx=10,pady=10)

        cola= Label(f4, text="Coco Cola", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=1, column=0,padx=10, pady=10,sticky="w")
        cola_ent= Entry(f4, width=10, textvariable=self.cola,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=1, column=1, padx=10,pady=10)

        slic= Label(f4, text="Slice", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=2, column=0, padx=10,pady=10, sticky="w")
        slic_ent= Entry(f4, width=10, textvariable=self.slice,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=2, column=1, padx=10,pady=10)

        froo= Label(f4, text="Frooti", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=3, column=0,padx=10, pady=10,sticky="w")
        froo_ent = Entry(f4, width=10, textvariable=self.frooti,font=("Arial Rounded MT", 16, "bold"),bg="#a0a3a8", bd=5, relief=RIDGE).grid(row=3, column=1, padx=10,pady=10)

        bov = Label(f4, text="Bovonto", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=4, column=0,padx=10, pady=10,sticky="w")
        bov_ent = Entry(f4, width=10, textvariable=self.bovonto,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=4, column=1, padx=10,pady=10)

        up= Label(f4, text="7 Up", font=("Arial Rounded MT", 16, "bold"), bg="#262928", fg="white").grid(row=5, column=0, padx=10,pady=10, sticky="w")
        up_ent = Entry(f4, width=10, textvariable=self.up,font=("Arial Rounded MT", 16, "bold"), bg="#a0a3a8",bd=5, relief=RIDGE).grid(row=5, column=1, padx=10,pady=10)

#frame5
        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1000, y=180, width=355, height=380)

        bill_ar= Label(f5, text="BILL", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll= Scrollbar(f5, orient=VERTICAL)
        self.area = Text(f5, yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.area.yview)
        self.area.pack(fill=BOTH, expand=1)

#frame6
        f6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("Arial Rounded MT", 15, "bold"), fg="#aeb8b5",bg="#262928")
        f6.place(x=0, y=560, relwidth=1, height=140)

        a1 = Label(f6, text="Total Cosmetics Price:", bg="#262928", fg="white", font=("Arial Rounded MT", 14, "bold")).grid(row=0, column=0, pady=1, padx=20, sticky="w")
        a2 = Label(f6, text="Total Groceries Price:", bg="#262928", fg="white", font=("Arial Rounded MT", 14, "bold")).grid(row=1, column=0, pady=1, padx=20, sticky="w")
        a3 = Label(f6, text="Total Cool Drinks Price:", bg="#262928", fg="white",font=("Arial Rounded MT", 14, "bold")).grid(row=2, column=0, pady=1, padx=20, sticky="w")

        ent = Entry(f6, width=18, textvariable=self.cos,font="arial 10 bold",bg="#a0a3a8", bd=7, relief=RIDGE).grid(row=0, column=1, padx=10, pady=1)
        ent1 = Entry(f6, width=18, textvariable=self.gro ,font="arial 10 bold", bg="#a0a3a8",bd=7, relief=RIDGE).grid(row=1, column=1, padx=10, pady=1)
        ent2 = Entry(f6, width=18, textvariable=self.c_drink,bg="#a0a3a8",font="arial 10 bold", bd=7, relief=RIDGE).grid(row=2, column=1, padx=10, pady=1)

        a4 = Label(f6, text="Cosmetics Tax:", bg="#262928", fg="white", font=("Arial Rounded MT", 14, "bold")).grid(row=0,column=2,pady=1,padx=20, sticky="w")
        a5 = Label(f6, text="Groceries Tax:", bg="#262928", fg="white", font=("Arial Rounded MT", 14, "bold")).grid(row=1,column=2,pady=1,padx=20,sticky="w")
        a6 = Label(f6, text="Cool Drinks Tax:", bg="#262928", fg="white", font=("Arial Rounded MT", 14, "bold")).grid(row=2,column=2,pady=1,padx=20,sticky="w")

        ent3 = Entry(f6, width=18, textvariable=self.cos_tax,font="arial 10 bold", bg="#a0a3a8",bd=7, relief=RIDGE).grid(row=0, column=3, padx=10, pady=1)
        ent4 = Entry(f6, width=18,  textvariable=self.gro_tax,font="arial 10 bold",bg="#a0a3a8", bd=7, relief=RIDGE).grid(row=1, column=3, padx=10, pady=1)
        ent5 = Entry(f6, width=18,  textvariable=self.c_tax,font="arial 10 bold",bg="#a0a3a8", bd=7, relief=RIDGE).grid(row=2, column=3, padx=10, pady=1)

        bt = Frame(f6, bd=7,bg="#262829", relief=FLAT)
        bt.place(x=770, width=570, height=100)

        tot_b= Button(bt, command=self.total,text="Total", bg="#262928", fg="white", bd=5, pady=15, width=11, font="ariel 12 bold").grid(row=0,column=0,padx=5,pady=5)
        gene_b= Button(bt, text="Generate Bill",command=self.bill_area, bg="#262928", bd=5, fg="white", pady=15, width=11, font="ariel 12 bold").grid(row=0, column=1, padx=5, pady=5)
        cle_b= Button(bt, text="Clear",command=self.clear_data,bg="#262928", fg="white", bd=5, pady=15, width=11, font="ariel 12 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_b= Button(bt, text="Exit",command=self.exit_app,bg="#262928", fg="white", bd=5, pady=15, width=11, font="ariel 12 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_f_c=self.cream.get()*40
        self.c_f_w=self.wash.get() * 120
        self.c_h_s=self.spray.get() * 60
        self.c_s_p=self.soap.get() * 50
        self.c_b_l=self.loation.get() * 140
        self.c_h_g=self.gel.get() * 180
        self.total_cosmetic_price=float(
            self.c_f_c+
            self.c_f_w+
            self.c_h_s+
            self.c_s_p+
            self.c_b_l+
            self.c_h_g
        )
        self.cos.set("Rs."+str(self.total_cosmetic_price))
        self.cs_tax=round((self.total_cosmetic_price*0.05),2)
        self.cos_tax.set("Rs."+str(self.cs_tax))

        self.g_r=self.rice.get() * 40
        self.g_f_o=self.oil.get() * 120
        self.g_d=self.dhal.get() * 70
        self.g_w=self.wheat.get() * 30
        self.g_s=self.sugar.get() * 100
        self.g_t=self.tea.get() * 50

        self.total_grocery_price =float (
            self.g_r+
            self.g_f_o+
            self.g_d+
            self.g_w+
            self.g_s+
            self.g_t
        )
        self.gro.set("Rs."+str(self.total_grocery_price))
        self.gr_tax=round((self.total_grocery_price * 0.05),2)
        self.gro_tax.set("Rs."+str(self.gr_tax))

        self.cd_d=self.dew.get() * 40
        self.cd_cc=self.cola.get() * 60
        self.cd_s=self.slice.get() * 40
        self.cd_f=self.frooti.get() * 60
        self.cd_b=self.bovonto.get() * 80
        self.cd_u=self.up.get() * 80

        self.total_cooldrink_price =float (
            self.cd_d+
            self.cd_cc+
            self.cd_s+
            self.cd_f+
            self.cd_b+
            self.cd_u
        )
        self.c_drink.set("Rs."+str(self.total_cooldrink_price))
        self.cd_tax=round((self.total_cooldrink_price * 0.05),2)
        self.c_tax.set("Rs."+str(self.cd_tax))

        self.total_bill=float(
            self.total_grocery_price+
            self.total_cosmetic_price+
            self.total_cooldrink_price+
            self.cd_tax+
            self.gr_tax+
            self.cs_tax
        )

    def welcome_bill(self):
        self.area.delete("1.0", END)
        self.area.insert(END, "\t\t Welcome")
        self.area.insert(END, f"\n Bill_num: {self.bill_no.get()}")
        self.area.insert(END, f"\n Customer_Name: {self.c_name.get()}")
        self.area.insert(END, f"\n Mobile_No: {self.mob_num.get()}")
        self.area.insert(END, f"\n======================================")
        self.area.insert(END, "\n Products\t\tQty\t\tPrice")
        self.area.insert(END, "\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.mob_num.get()=="":
            messagebox.showerror("Error","Customer Detail Must")
        elif self.cos.get()=="Rs.0.0" and self.gro.get()=="Rs.0.0" and self.c_drink.get()=="Rs.0.0" :
            messagebox.showerror("Error","No Product Purchase")
        else:
            self.welcome_bill()

            # cosmetics
            if self.cream.get() != 0:
                self.area.insert(END, f"\n Face Cream:\t\t{self.cream.get()}\t\t{self.c_f_c}")
            if self.wash.get() != 0:
                self.area.insert(END, f"\n Face Wash:\t\t{self.wash.get()}\t\t{self.c_f_w}")
            if self.spray.get() != 0:
               self.area.insert(END, f"\n Hair Spray:\t\t{self.spray.get()}\t\t{self.c_h_s}")
            if self.soap.get() != 0:
                self.area.insert(END, f"\n Bath Soap:\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.gel.get() != 0:
                self.area.insert(END, f"\n Hair Gel:\t\t{self.gel.get()}\t\t{self.c_h_g}")
            if self.loation.get() != 0:
                self.area.insert(END, f"\n Body Loation:\t\t{self.loation.get()}\t\t{self.c_b_l}")

            # groceries
            if self.rice.get() != 0:
                self.area.insert(END, f"\n Rice:\t\t{self.rice.get()}\t\t{self.g_r}")
            if self.oil.get() != 0:
                self.area.insert(END, f"\n Food Oil:\t\t{self.oil.get()}\t\t{self.g_f_o}")
            if self.dhal.get() != 0:
                self.area.insert(END, f"\n Dhal:\t\t{self.dhal.get()}\t\t{self.g_d}")
            if self.wheat.get() != 0:
                self.area.insert(END, f"\n Wheat:\t\t{self.wheat.get()}\t\t{self.g_w}")
            if self.sugar.get() != 0:
                self.area.insert(END, f"\n Sugar:\t\t{self.sugar.get()}\t\t{self.g_s}")
            if self.tea.get() != 0:
                self.area.insert(END, f"\n Tea:\t\t{self.tea.get()}\t\t{self.g_t}")

            # cooldrinks
            if self.dew.get() != 0:
                self.area.insert(END, f"\n Dew:\t\t{self.dew.get()}\t\t{self.cd_d}")
            if self.cola.get() != 0:
                self.area.insert(END, f"\n Coke:\t\t{self.cola.get()}\t\t{self.cd_cc}")
            if self.slice.get() != 0:
                self.area.insert(END, f"\n Slice:\t\t{self.slice.get()}\t\t{self.cd_s}")
            if self.frooti.get() != 0:
                self.area.insert(END, f"\n Frooti:\t\t{self.frooti.get()}\t\t{self.cd_f}")
            if self.bovonto.get() != 0:
                self.area.insert(END, f"\n Bovonto:\t\t{self.bovonto.get()}\t\t{self.cd_b}")
            if self.up.get() != 0:
                self.area.insert(END, f"\n 7UP:\t\t{self.up.get()}\t\t{self.cd_u}")

            self.area.insert(END, f"\n---------------------------------------")
            if self.cos_tax.get() != 0:
                self.area.insert(END, f"\n Cosmetic Tax:\t\t\t{self.cos_tax.get()}")
            if self.gro_tax.get() != 0:
                self.area.insert(END, f"\n Grocery Tax:\t\t\t{self.gro_tax.get()}")
            if self.c_tax.get() != 0:
                self.area.insert(END, f"\n Cool Drink Tax:\t\t\t{self.c_tax.get()}")
            self.area.insert(END, f"\n---------------------------------------")
            if self.total_bill != 0:
                self.area.insert(END, f"\n Total:\t\t\tRs.{self.total_bill}")
            self.area.insert(END, f"\n---------------------------------------")
            self.area.insert(END,f"\t\t     Thank You\n")
            self.area.insert(END, f"\t     Come Again")
            self.save_bill()
            pass


    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do You Want To Save The Bill?")
        if op==1:
            self.bill_data = self.area.get("1.0",END)
            f1= open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no.: {self.bill_no.get()} Saved Sucessfully")
        else:
            return


    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.area.delete('1.0',END)
                for d in f1:
                    self.area.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
#clear button
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear the data?")
        if op ==1:
            # cosmetics
            self.cream.set(0)
            self.wash.set(0)
            self.spray.set(0)
            self.soap.set(0)
            self.gel.set(0)
            self.loation.set(0)
            # groceries
            self.rice.set(0)
            self.oil.set(0)
            self.dhal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # cooldrinks
            self.dew.set(0)
            self.cola.set(0)
            self.slice.set(0)
            self.frooti.set(0)
            self.bovonto.set(0)
            self.up.set(0)
            # cust details
            self.c_name.set("")
            self.mob_num.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            # total stock
            self.gro.set("")
            self.cos.set("")
            self.c_drink.set("")
            # tax
            self.gro_tax.set("")
            self.cos_tax.set("")
            self.c_tax.set("")
            self.welcome_bill()
#exit_button
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op==1:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
