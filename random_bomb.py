import random #function random

def random_bom(rows: int, cols: int, bom_number: int) -> list: #function random_bomb ต้องใช้ rows , cols เเละ bom_number เป็นข้อมูลเเบบ Integer ทั้งหมดเพื่อดำเนินการด้วย function พร้อมสร้าง List ว่างไว้
    mine = [] #สร้าง arrat
    for row in range(rows):  #สร้าง row ตามจำนวนเเถวที่ได้กำหนดไว้
        row_data = [] #สร้าง array ขึ้นมา
        for col in range(cols):  #สร้าง row ตามจำนวนเเถวที่ได้กำหนดไว้
            position = random.randint(0, rows) #เอาตัวเลขใส่เข้าไปในเเถว
            if position == 1 and bom_number > 0: #สุ่มตัวเลขตามจำนวน rows โดยเริ่มจากเเถวที่ 0
                row_data.append(-1) #นำค่า -1 ใส่เข้าไปใน row_data
                bom_number -= 1 #วางระเบิดโดยระเบิดจะลดจำนวนลงครั้งละ 1 ลูก
            else:
                row_data.append(0) #เปลี่ยนตัวเลขอื่นที่สุ่มได้เป็น 0 
        mine.append(row_data)  #นำค่าที่อยู่ใน row_data มาใส่ใน mine 
    return mine # เเสดงค่าใน Array 

if __name__ == "__main__":
    mine = random_bom(5, 5, 5) #กำหนดขนาด 5x5 ซึ่งมีจำนวนระเบิด เท่ากับ 5 ลูก
    for row in mine:
        print(row) #เเสดงทุก row ใน mine