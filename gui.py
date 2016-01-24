__author__ = 'rresol'
__email__  = 'shashank.kumar.apc13@itbhu.ac.in'

import pygtk
pygtk.require('2.0')
import gtk,acnt

class pops:
    def __init__(self,function_name):
        self.title = function_name

    def on_add_click(self,widget,entry1,entry2,data):
        if entry1:    
            entry1.set_activates_default(True)
            name = entry1.get_text()
        
        entry2.set_activates_default(True)
        amount = int(entry2.get_text())
        data = data.lower()
        
        if data == 'credit':
            acnt.credit(name,amount)
        elif data == 'debit':
            acnt.debit(name,amount)
        elif data == 'expense':
            acnt.expense(amount)

    def function_call(self,widget,data=None):
        popup = gtk.Window()
        popup.set_title(data)

        hbox = gtk.HBox(False,0)
        hbox.set_border_width(10)

        #Adding text entry dialog
        vbox1 = gtk.VBox(False,0)
    
        #vbox.set_border_width()
        entry1 = None
        if not data =="Expense":
            label = gtk.Label("Name")
            vbox1.pack_start(label)
            label.show()
            entry1 = gtk.Entry()
            vbox1.pack_start(entry1,False,False,0)
            hbox.pack_start(vbox1,False,False,0)
            entry1.show()
            vbox1.show()
    
        vbox2 = gtk.VBox(False,0)
    
        #vbox.set_border_width()
        label = gtk.Label("Amount")
        vbox2.pack_start(label)
        label.show()
        entry2 = gtk.Entry()
        vbox2.pack_start(entry2)
        hbox.pack_start(vbox2,False,False,0)
    
        vbox2.show()

        #Adding ok button
        button1 = gtk.Button("Add")
        button1.connect("clicked",self.on_add_click,entry1,entry2,data)
        hbox.pack_start(button1,False,False,0)
        button1.show()
    

        popup.add(hbox)
        popup.set_modal(True)
        popup.connect("destroy",gtk.Widget.destroy)
        popup.show_all()


class MyApp:

    def __init__(self):

        #Creating the main window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("SubX")
        self.window.connect("destroy",lambda w:gtk.main_quit())
        self.window.set_size_request(450,340)
        vbox = gtk.VBox(False,0)
        vbox.set_border_width(10)
        
        hbox1= gtk.HBox(False,0)
        hbox1.set_border_width(10)
        
        #Adding a button for credit
        a = pops("Credit")
        button = gtk.Button("Credit")
        button.connect("clicked",a.function_call,"Credit")
        hbox1.pack_start(button,True,True,0)
        button.show()

        #Adding a button for debit
        b = pops("Debit")
        
        button = gtk.Button("Debit")
        button.connect("clicked",a.function_call,"Debit")
        hbox1.pack_start(button,True,True,0)
        button.show()

        #Adding a button for Expenses
        c = pops("Expenses")

        button = gtk.Button("Expenses")
        button.connect("clicked",c.function_call,"Expense")
        hbox1.pack_start(button,False,False,0)
        button.show()

        vbox.pack_start(hbox1,False,False,0)
        #self.window.add(hbox1)
        
        hbox1.show()
        
        #Adding Will Smith's Quote
        hbox3 = gtk.HBox(False,0)
        hbox3.set_border_width(10)
        
        image = gtk.Image()
        image.set_from_file("subx.jpg")
        hbox3.pack_start(image,False,False,0)
        image.show()

        image = gtk.Image()
        image.set_from_file("front.jpeg")
        hbox3.pack_start(image,False,False,0)
        image.show() 

        vbox.pack_start(hbox3,False,False,0)
        #self.window.add(hbox3)

        hbox3.show()

        #Adding a quit button 
       
        hbox2 = gtk.HBox(False,0)
        hbox2.set_border_width(10)
        
        button =  gtk.Button("Close")
        button.connect("clicked",lambda w:gtk.main_quit())
        hbox2.pack_start(button,True,True,0)
        button.show()
        vbox.pack_end(hbox2,False,False,0)
        #self.window.add(hbox2)


        hbox2.show()
        self.window.add(vbox)

        vbox.show()

        self.window.show()

def main():
    gtk.main()
    return 0

if __name__ == '__main__':
    MyApp()
    main()