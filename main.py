import qrcode
import os


user_inpt = input("What string do you want to encode: ")
file_name = input("Input filename: ")
data = user_inpt

img = qrcode.make(data) 
my_dest = (file_name + ".png") if file_name != "" else "QR" + ".png"



path = 'C:/Users/user/OneDrive/Desktop/'  
for filename in os.listdir(path):
    if filename==my_dest:
        print("File already exists/n")
        prompt = input("press O to overwrite or give a new name: ")
        if prompt != "O or o":
            my_dest = prompt +".png"
        
        else:
            print("File overwritten ")
            
    else:
        continue
        
        
        
img.save('C:/Users/user/OneDrive/Desktop/'+my_dest)




        
        
        
        
#sd