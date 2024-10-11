from Train_Function_App import tk
from Train_Function_App import TrainTicketApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x700+80+50')
    app = TrainTicketApp(root)
    root.mainloop()
