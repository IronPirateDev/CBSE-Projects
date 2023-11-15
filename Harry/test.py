import cv2
import mysql.connector as c
con=c.connect(user='root',passwd='dpsbn',host='localhost',database='ticket')
if con.is_connected():
    print("connection successful")
else:
    print("not connected")
cu=con.cursor()
#to count no of rows
def rowcount():
    query="select count(*) from guest"
    cu.execute(query)
    count = cu.fetchone()[0]
    con.commit()
#to add guests
def add_guests():
    query1="select count(*) from guest"
    cu.execute(query1)
    count = cu.fetchone()[0]
    print(count)
    x=int(input("enter no. of guests:"))
    for i in range(x):
        tnoinc=count+1
        name=input("enter guest name:")
        code=input("enter code ('dps___'):")
        query="insert into guest(tno,name,code) values({},'{}','{}')".format(tnoinc,name,code)
        cu.execute(query)
        con.commit()
        print("added sucessfully")
def decode_qr(frame):
    import cv2
    from pyzbar.pyzbar import decode
    import numpy as np
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        return barcodeData, barcodeType
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoded_data= decode_qr(frame)
    if decoded_data:
        #print(decoded_data)
        #print("Type: ", decoded_type)
        break
    cv2.imshow('QR Code Scanner', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


for i in decoded_data:
    code1=i
    break
query = 'select * from guest where code ="{}"'.format(code1)
cu.execute(query)
for i in cu:
    if i[2] ==code1:
        if i[3]=='False':
            co=i[2]
            print(type(co))
            query1='update guest set entry="False" where code="{}"'.format(co)

            cu.execute(query1)
            con.commit()
            print("updated")


        elif i[3]=='True':
            print("already entered")
            query2='select * from guest where code="{}"'.format(code1)
            cu.execute(query2)
            for i in cu:
                print(i)
        else:
            print("no entry")
    else:
        print("no entry")
for i in cu:
    print(i)
"""    if code1i[2]:
        print("no entry")"""
    #print(i)
decode_qr(frame)
'''  else:
      query3='select * from guest'
      cu.execute(query3)
      for k in cu:
          if k[2] != code1:
              print("entry not allowed")'''