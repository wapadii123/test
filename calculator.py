# calculator.py

def add(x, y):
    """ฟังก์ชันสำหรับบวกเลข"""
    return x + y

def subtract(x, y):
    """ฟังก์ชันสำหรับลบเลข"""
    return x - y

def multiply(x, y):
    """ฟังก์ชันสำหรับคูณเลข"""
    return x * y

def divide(x, y):
    """ฟังก์ชันสำหรับหารเลข"""
    if y == 0:
        return "ข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้"
    return x / y

def main():
    print("=== โปรแกรมเครื่องคิดเลขอย่างง่าย ===")
    print("เลือกการทำงาน:")
    print("1. บวก (+)")
    print("2. ลบ (-)")
    print("3. คูณ (*)")
    print("4. หาร (/)")

    while True:
        choice = input("\nโปรดเลือกหมายเลข (1/2/3/4) หรือพิมพ์ 'q' เพื่อออก: ")

        if choice.lower() == 'q':
            print("ออกจากโปรแกรม...")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("ใส่ตัวเลขแรก: "))
                num2 = float(input("ใส่ตัวเลขที่สอง: "))
            except ValueError:
                print("กรุณาใส่ตัวเลขที่ถูกต้อง!")
                continue

            if choice == '1':
                print(f"ผลลัพธ์: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"ผลลัพธ์: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"ผลลัพธ์: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"ผลลัพธ์: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main()