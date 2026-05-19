def main():
    mock_data = {
        "APX-901": "ประกอบอุปกรณ์ SMT",
        "APX-902": "ตรวจสอบคุณภาพ QA",
        "APX-903": "จัดส่งเรียบร้อยแล้ว"
    }

    print("==================================================")
    print("  ยินดีต้อนรับสู่ระบบ Apex Circuit PCB Production Tracking  ")
    print("==================================================")

    while True:
        user_input = input("กรุณากรอกรหัสใบสั่งผลิต (พิมพ์ 'exit' เพื่อออกจากโปรแกรม): ").strip()
        
        if user_input.lower() == 'exit':
            print("ออกจากระบบ ขอบคุณที่ใช้บริการ Apex Circuit")
            break
        
        if user_input in mock_data:
            print(f"รหัสใบสั่งผลิต: {user_input} | สถานะ: {mock_data[user_input]}")
        else:
            print("คำเตือน: ไม่พบรหัสใบสั่งผลิตที่คุณระบุ กรุณาตรวจสอบและลองใหม่อีกครั้ง")
        
        print("-" * 50)

if __name__ == "__main__":
    main()
