
def Rate_Cal(self,s_station, e_station):

    # case 1 !!!
    if s_station in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}:
        if e_station in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}:
            print("price : 15")
        elif e_station == 18:
            print("price : 32")
        elif e_station == 19:
            print("price : 40")
        elif e_station == 20:
            print("price : 43")
        elif e_station == 21:
            print("price : 47")
        elif e_station == 22:
            print("price : 50")
        elif e_station == 23:
            print("price : 55")
        elif e_station == 24:
            print("price : 58")
        else:
            print("price : 62")
    # case 2 !!!
    elif s_station == 17 :
        if e_station in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}:
            print("price : 15")
        elif e_station in {17, 18}:
            print("price : 17")
        elif e_station == 19:
            print("price : 25")
        elif e_station == 20:
            print("price : 28")
        elif e_station == 21:
            print("price : 32")
        elif e_station == 22:
            print("price : 35")
        elif e_station == 23:
            print("price : 40")
        elif e_station == 24:
            print("price : 43")
        elif e_station in {25,26,27,28,29,30,31,32,33,34}:
            print("price : 47")
        else: print("price : 62")
