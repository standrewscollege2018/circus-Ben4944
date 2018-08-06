# Ticketing System
# 3/08/2018
# Ben Smith

# Import Tkinter
from tkinter import *

# Define ticket class
class Ticket:
    def __init__(self, time, capacity, cost):
        self._time = time
        self._capacity = int(capacity)
        self._sold = 0
        self._cost = float(cost)
        tickets.append(self)
        ticket_list.append(self._time)
        
        
    def _values(self):
        available = self._capacity - self._sold
        sales = self._sold * self._cost
        return {'time': self._time, 'capacity': self._capacity, 'sold': self._sold, 'cost': self._cost, 'available': available, 'sales': sales}

tickets = []
ticket_list = []

Ticket("10AM SHOW", 150, 5)
Ticket("3PM SHOW", 150, 5)
Ticket("8PM SHOW", 250, 12)



# Tkinter Window
root = Tk()
root.title("Ticketing System")
root.geometry("500x400")


# Title
lbl_current_showings = Label(root, text="CURRENT SHOWINGS").grid(row=0, column=0)


# Display Tickets --------------------
var_display_tickets = StringVar()
lbl_display_tickets = Label(root, textvariable=var_display_tickets)
lbl_display_tickets.grid(row=1, column=0)
def display_tickets():
    join_tickets = ""
    for t in tickets:
        t_data = t._values()
        t_display = "{} | Available: {}, Sold: {}, Sales: ${}\n".format(t_data['time'], t_data['available'], t_data['sold'], t_data['sales'])
        join_tickets += t_display
    var_display_tickets.set(join_tickets)
display_tickets()


# Sell Tickets --------------------
# Select show to sell tickets from with dropdown
selected_show = StringVar()
selected_show.set(ticket_list[0])
def change_show(self):
    selected_show.set(self)
ticket_menu = OptionMenu(root, selected_show, *ticket_list, command=change_show)
ticket_menu.grid(row=0, column=1)

# Sell tickets function
def sell_tickets():
    var_display_tickets.set("Failed to sell tickets")
    if entry_sell.get():
        for t in tickets:
            if t._time == selected_show.get():
                if (t._capacity - t._sold - int(entry_sell.get())) >= 0:
                    t._sold += int(entry_sell.get())
                    var_sell_status.set("{} tickets sold".format(entry_sell.get()))
                    display_tickets()
                else:
                    var_sell_status.set("Not enough capacity")
    else:
        var_sell_status.set("Please enter a quantity")
        

# Sell ticket quantity entry box
entry_sell = Entry(root)
entry_sell.grid(row=1, column=1)

# Sell tickets button
btn_sell = Button(root, text="Sell Tickets", command=sell_tickets)
btn_sell.grid(row=2, column=1)

# Sell ticket status label
var_sell_status = StringVar()
lbl_sell_status = Label(root, textvariable=var_sell_status)
lbl_sell_status.grid(row=3, column=1)


root.mainloop()