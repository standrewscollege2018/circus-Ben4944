# Ticketing System
# 7/08/2018
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

# Create tickets
def init_tickets():
    global tickets
    global ticket_list
    tickets = []
    ticket_list = []
    Ticket("10AM SHOW", 150, 5)
    Ticket("3PM SHOW", 150, 5)
    Ticket("8PM SHOW", 250, 12)
init_tickets()



# Tkinter Window
root = Tk()
root.title("Ticketing System")
root.geometry("500x400")


# Display Tickets --------------------
var_display_tickets = StringVar()
lbl_display_tickets = Label(root, textvariable=var_display_tickets)
lbl_display_tickets.grid(row=0, column=0)
def display_tickets():
    join_tickets = "CURRENT SHOWINGS\n"
    for t in tickets:
        t_data = t._values()
        t_display = "{} | Available: {}, Price: ${}, Sold: {}, Sales: ${}\n".format(t_data['time'], t_data['available'], t_data['cost'], t_data['sold'], t_data['sales'])
        join_tickets += t_display
    var_display_tickets.set(join_tickets)
display_tickets()


# Tickets Summary --------------------
var_tickets_summary = StringVar()
lbl_tickets_summary = Label(root, textvariable=var_tickets_summary)
lbl_tickets_summary.grid(row=2, column=0)
def display_summary():
    total_sold = 0
    total_sales = 0
    for t in tickets:
        t_data = t._values()
        total_sold += t_data['sold']
        total_sales += t_data['sales']
    var_tickets_summary.set("SUMMARY\n{} tickets sold today\n${} earned today".format(total_sold, total_sales))
display_summary()
    


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
    status_lbl("Failed to sell tickets", "red")
    if entry_sell.get():
        for t in tickets:
            if t._time == selected_show.get():
                # Check entered value is int
                try:
                    # If selling quantity is less than or equal to zero, don't allow sale
                    if int(entry_sell.get()) <= 0:
                        status_lbl("Value must be greater than 0", "red")
                    # Check there are enough tickets available ((capacity - sold qty - requested qty) >= 0)
                    elif (t._capacity - t._sold - int(entry_sell.get())) >= 0:
                        t._sold += int(entry_sell.get())
                        status_lbl("{} tickets sold".format(entry_sell.get()), "green")
                        display_tickets()
                        display_summary()
                    # Otherwise there is not enough capacity
                    else:
                        status_lbl("Not enough capacity", "red")
                # Except if value is not int - display error
                except:
                    status_lbl("Value must be int", "red")
    # No value entered in box - display error
    else:
        status_lbl("Please enter a quantity", "red")
        

# Sell ticket quantity entry box
entry_sell = Entry(root)
entry_sell.grid(row=1, column=1)

# Sell tickets button
btn_sell = Button(root, text="Sell Tickets", bg="green yellow", command=sell_tickets)
btn_sell.grid(row=2, column=1)

# Sell ticket status label
var_sell_status = StringVar()
lbl_sell_status = Label(root, textvariable=var_sell_status)
lbl_sell_status.grid(row=3, column=1)

# Function for changing status label colour
def status_lbl(message, colour):
    var_sell_status.set(message)
    lbl_sell_status.config(fg=colour)


# Reset ticket sales --------------------
def reset_sales():
    init_tickets()
    display_tickets()
    display_summary()
btn_reset = Button(root, text="Reset Sales", bg="tomato", command=reset_sales)
btn_reset.grid(row=4, column=1)


# Window Mainloop --------------------
root.mainloop()