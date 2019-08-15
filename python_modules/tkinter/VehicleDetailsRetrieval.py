from tkinter import *


def retrieve_input():
    global vehicle_registration
    global vehicle_time
    global vehicle_distance
    vehicle_registration = veh_reg_text_box.get()
    vehicle_time = time_text_box.get()
    vehicle_distance = distance_text_box.get()
    print(vehicle_registration, vehicle_time, vehicle_distance)
    # number_checker()
root = Tk()
root.title("Average Speed Checker")
root.geometry("450x165")

veh_reg_label = Label(root, text="Vehicle Registration:")
veh_reg_label.pack()

veh_reg_text_box = Entry(root, bd=1)
veh_reg_text_box.pack()

distance_label = Label(root, text="Distance")
distance_label.pack()

distance_text_box = Entry(root, bd=1)
distance_text_box.pack()

time_label = Label(root, text="Time")
time_label.pack()

time_text_box = Entry(root, bd=1)
time_text_box.pack()

enter_button = Button(root, text="Enter", command=retrieve_input)
enter_button.pack()

root.mainloop()