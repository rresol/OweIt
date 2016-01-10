__author__ = 'irresolute'

import gtk,sys,acnt,shelve

class MyApp(gtk.Window):
        def __init__(self):
            super(MyApp,self).__init__()
            
            self.set_title("Account Manager")
            self.set_size_request(1000,1000)
            self.set_position(gtk.WIN_POS_CENTER)

            btn1 = gtk.Button("Credit")
            btn2 = gtk.Button("Debit")
            btn3 = gtk.Button("Expense")
            
            fixed= gtk.Fixed()
            fixed.put(btn1,150,20)
            fixed.put(btn2,450,20)
            fixed.put(btn3,750,20)

            btn1.set_tooltip_text("Money they Owe.")
            btn2.set_tooltip_text("Money you Owe.")
            btn3.set_tooltip_text("Money spent.")
            
            #self.set_tooltip_text("Manages your daily transactions .")
            
            try:
                self.set_icon_from_file("acnt.jpg")
            except Exception , e:
                print e.message
                sys.exit(1)

            #Creating the ListView 

            vbox =  gtk.VBox(False,8)

            sw = gtk.ScrolledWindow()
            sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
            sw.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)

            vbox.pack_start(sw,True,True,0)

            store = self.create_model()
            
            treeView = gtk.TreeView(store)
            treeView.connect("row-activated",self.on_activated)
            treeView.set_rules_hint(True)
            sw.add(treeView)

            self.create_columns(treeView)
            self.statusbar = gtk.Statusbar()
            
            vbox.pack_start(self.statusbar,False,False,0)
            
            self.add(vbox)
            
            self.connect("destroy",gtk.main_quit)
            self.add(fixed)
            
            self.show_all()
        
        def create_model(self):
            store = gtk.ListStore(str,int)
            f = shelve.open("Credit")
            klist = f.keys()
            for k in klist:
                print k
                store.append(k,f[key])
            return store

        def create_columns(self,treeView):
            
            rendererText = gtk.CellRendererText()
            column = gtk.TreeViewColumn("Name",rendererText,text =0)
            column.set_sort_column_id(0)
            treeView.append_column(column)
    
            rendererText = gtk.CellRendererText()
            column = gtk.TreeViewColumn("Amount",rendererText,text=1)
            column.set_sort_column_id(1)
            treeView.append_column(column)
        
        def on_activated(self,widget,row,col):
            
            model = widget.get_model()
            text = model[row][0]+", " + str(model[row][1])
            self.statusbar.push(0,text) 
        
            self.connect("destroy",gtk.main_quit)
            self.add(fixed)
            
            self.show_all()

MyApp()
gtk.main()
