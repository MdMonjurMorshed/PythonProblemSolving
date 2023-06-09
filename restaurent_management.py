class Restaurent:
    def __init__(self):

        self.add_item_menu={}
        self.book_table=[]
        self.order_item=[]

    def add_item_to_menu(self,item,price):
        self.add_item_menu[item]=price
    def reserve_table(self,table_number):
        self.book_table.append(table_number)
    def make_order(self,table_number):
     
        do_order=list(map(str,input("enter space seperated order for {}:".format(table_number)).split()))
        orders_done=[]
        for i in do_order:
            if i in self.add_item_menu:


               orders_done.append(i)
        orders={"table_number":table_number,'orders':orders_done}       

        self.order_item.append(orders)

    def total_bill(self,table_number): 
        total_price=0
        for obj in self.order_item:
            if obj['table_number'] == table_number:
                for i in obj['orders']:
                    total_price+=self.add_item_menu[i]
        print("table No:{} ,total bill:{}".format(table_number,total_price))            
                 
    def print_menu_item(self):
        for item,price in self.add_item_menu.items():
            print("{}:{}".format(item,price))
    def print_reservation(self):
        for table in self.book_table:

           print("booked table number is :{} ".format(table))
    def print_orders(self):
        for order in self.order_item:
            print("{}".format(order))


rest=Restaurent()
rest.add_item_to_menu('Burger',130)
rest.add_item_to_menu('pidzza',170)
rest.add_item_to_menu('chiclken wings',200)
rest.add_item_to_menu('sandwitch',130)

rest.reserve_table(1)
rest.reserve_table(2)
rest.reserve_table(3)

rest.make_order(1)
rest.make_order(2)

rest.print_menu_item()
rest.print_reservation()
rest.print_orders()
rest.total_bill(1)
rest.total_bill(2)
