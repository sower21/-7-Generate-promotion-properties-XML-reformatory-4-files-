import search_promotions
import tkinter as tk
from tkinter import *
from  tkinter import ttk
from tkinter.messagebox import showinfo


def preview():
    for i in set.get_children():
        set.delete(i)
    package = iuput_text_package.get()
    search = menu.get()
    id = iuput_text_number.get()
    # "PROMOTION_ID", "PRODUCT_ID","COUPON_ID"
    # (search != "PROMOTION_ID" or search != "PRODUCT_ID" or search != "COUPON_ID" )

    if  ((package != '') & (all(i.isdigit() for i in package))) & (search != 'Select Type') &((id != '') & (all(i.isdigit() for i in id))):
        df = search_promotions.search_promotion_all(search, id, package)
        if len(df)!= 0:
            for i in range(len(df)) :
                set.insert(parent='', index='end', iid=i, text='', values=(df[i]))
        else:
            output_is_none()

    else :
        output_failed()
        


def output_failed():
    global output_screen
    output_screen = Toplevel()
    output_screen.title("Failed")
    output_screen.geometry("300x100")
    Label(output_screen, text = "Invalid input or missing some input values.").pack()
    Button(output_screen, text="OK", command=delete_output_failed).pack()
    output_screen.mainloop()


def output_is_none():
    global output_none_screen
    output_none_screen = Toplevel()
    output_none_screen.title("Failed")
    output_none_screen.geometry("300x100")
    Label(output_none_screen, text = "No data found.").pack()
    Button(output_none_screen, text="OK", command=delete_output_none).pack()
    output_none_screen.mainloop()
    
def delete_output_none():
    iuput_text_package.delete(0, END)
    iuput_text_number.delete(0, END)
    for i in set.get_children():
        set.delete(i)
    output_none_screen.destroy()

def delete_output_failed():
    iuput_text_package.delete(0, END)
    iuput_text_number.delete(0, END)
    for i in set.get_children():
        set.delete(i)
    output_screen.destroy()


def clear_screen():
    iuput_text_package.delete(0, END)
    iuput_text_number.delete(0, END)
    for i in set.get_children():
        set.delete(i)
    reset()

def reset():
    menu.set("Select Type")


def main_screen():
    global app
    app = tk.Tk()
    app.title("Gosoft Young Coders Challenges Group 7")
    app.geometry("1520x540+0+0")
    # app['background'] ='#de152c'
    bg = PhotoImage(file = "BG.png")
    label1 = Label( app, image = bg)
    label1.place(x = 0, y = 0)
   
    global iuput_text_package
    username=Label(app,text="GENERATE PROMOTION PROPERTIES XML",font=('Arial Bold',25),bg="#de152c",fg="#fcffff")
    username.place(x=450,y=10)
    label_package = tk.Label(master=app,text="Package : ",font=('Arial Bold',15) ,bg="#de152c",fg="#fcffff")
    label_package.place(x=250, y=60)
    iuput_text_package = tk.Entry(app,width=35)
    iuput_text_package.place(x=360, y=65)

    label_Search = tk.Label(master=app,text="Search From : ",font=('Arial Bold',15),bg="#de152c",fg="#fcffff")
    label_Search.place(x=700, y=60)



    #Set the Menu initially
    global menu,iuput_text_number, set
    menu= tk.StringVar()
    menu.set("Select Type")
    #Create a dropdown Menu
    dropdown= tk.OptionMenu(app, menu,"PROMOTION_ID", "PRODUCT_ID","COUPON_ID" )
    dropdown.place(x=590, y=60)

    iuput_text_number = tk.Entry(app,width=35)
    iuput_text_number.place(x=850, y=65)
    button = Button(text="Preview" ,command=preview ,font=('PT Sans',10))
    # button = tk.Button(text='Preview', command= lambda :print_something('print this'))
    button.place(x=1090, y=60)

    set = ttk.Treeview(app)
    set.place(x=15, y=100,height=400)
    scrollbar = ttk.Scrollbar(app, orient='vertical',command=set.yview)
    scrollbar.pack(side= RIGHT, fill= 'y')
    set.configure(yscrollcommand=scrollbar.set)
    set['columns']= ('MMBR_PROM_ID', 'COUPON_ID','STRT_DATE','END_DATE','EntityId','PROM_DESC',)
    set.column("#0", width=0,  stretch='NO')
    set.column("MMBR_PROM_ID",anchor=CENTER, width=150)
    set.column("COUPON_ID",anchor=CENTER, width=150)
    set.column("EntityId",anchor=CENTER, width=265)
    set.column("PROM_DESC",anchor=CENTER, width=500)
    set.column("STRT_DATE",anchor=CENTER, width=200)
    set.column("END_DATE",anchor=CENTER, width=200)

    set.heading("#0",text="",anchor=CENTER)
    set.heading("MMBR_PROM_ID",text="Promotion ID",anchor=CENTER)
    set.heading("COUPON_ID",text="Coupon ID",anchor=CENTER)
    set.heading("EntityId",text="Product ID",anchor=CENTER)
    set.heading("PROM_DESC",text="Promotion Description",anchor=CENTER)
    set.heading("STRT_DATE",text="Start date",anchor=CENTER)
    set.heading("END_DATE",text="End date",anchor=CENTER)

    button1 = Button(text="Clear Data" ,command=clear_screen ,font=('PT Sans',10))
    button1.place(x=1160, y=60)
    dropdown= tk.OptionMenu(app, menu,"PROMOTION_ID", "PRODUCT_ID","COUPON_ID")
    app.mainloop()

    # app.resizable(0,0)


    # test = main_search_promotion(input,number)
    # print(test)

if __name__ == '__main__':
    main_screen()