import os

#encryption
def encryption():
 path = input(r"Enter path of Image : ")
 key = int(input("Enter Key for encryption of Image : "))
 
 print('The path of file : ', path)
 print('Key for encryption : ', key)

 fin = open(path, "rb")
 image = fin.read()
 fin.close()

 image = bytearray(image)

 for index,values in enumerate(image):
		 image[index] = values ^ key
 
 fin = open(path, "wb")
 fin.write(image)
 fin.close()
 print("Encryption Done...")

#decryption
def decryption():
 path = input(r"Enter path of Image : ")
 key = int(input("Enter Key for decryption of Image : "))
 
 print('The path of file : ', path)
 print('Key for encryption : ', key)

 fin = open(path, "rb")
 image = fin.read()
 fin.close()

 image = bytearray(image)

 for index,values in enumerate(image):
		 image[index] = values ^ key
 
 fin = open(path, "wb")
 fin.write(image)
 fin.close()
 print("decryption Done...")


def main():
 print("Current directory  "+os.getcwd())
 while True:
    print("\n1.Encrypt")
    print("\n2.Decrypt")
    print("\n3.Exit")
    ch=int(input("enter your choice: "))
        
    if ch==1:
     encryption()
    elif ch==2:
        decryption()
    elif ch==3:
        break
    else:
        print("\nwrong choice")

if __name__=="__main__":
 main()