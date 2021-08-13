import serial# import pyserial module 
import tkinter# import tkinter module
arduinoData = serial.Serial('com11', 9600)# assign Arduino COM port and Boud rate
def led_on():  # function for led1-on
    arduinoData.write(b'a')  # send charactor 'a' when button1 pressed
def led_off():  # function for led1-off
    arduinoData.write(b'b')  # send charactor 'b' when button2 pressed
def led1_on():  # function for led2-on
    arduinoData.write(b'c')  # send charactor 'c' when button3 pressed
def led1_off():  # function for led2-off
    arduinoData.write(b'd')  # send charactor 'd' when button4 pressed
led_control_window = tkinter.Tk()
led_control_window.geometry("350x200")# Application window size
led_control_window.title("ANOKHAUTOMATION")# Application title
led_control_window.configure(background="yellow")# Application window background color
Button = tkinter.Button # create a button object.
# button 1
btn1 = Button(led_control_window, text="LOAD1-ON", bg="red", fg="blue", font="Times 16 bold", padx=20, pady=10,
              command=led_on)
btn1.grid(row=0, column=1)
# button 2
btn2 = Button(led_control_window, text="LOAD1-OFF", bg="green", fg="blue", font="Times 16 bold", padx=20, pady=10,
              command=led_off)
btn2.grid(row=0, column=2)
# button 3
btn3 = Button(led_control_window, text="LOAD2-ON", bg="red", fg="blue", font="Times 16 bold", padx=20, pady=10,
              command=led1_on)
btn3.grid(row=1, column=1)
# button 3
btn4 = Button(led_control_window, text="LOAD2-OFF", bg="green", fg="blue", font="Times 16 bold", padx=20, pady=10,
              command=led1_off)
btn4.grid(row=1, column=2)

led_control_window.mainloop()
input("press enter to exit")
