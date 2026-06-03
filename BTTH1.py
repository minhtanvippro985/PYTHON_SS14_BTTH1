grade_book = [
    {
     "id": "SV01",
     "name": "Nguyễn Văn A", 
     "info": (8.5, 7.0)},
    {
     "id": "SV02", 
     "name": "Trần Thị B", 
     "info": (6.0, 9.0)
     }
]
def delete_student(book):
    delete_id = input("Nhập mã sinh viên cần xóa : ").strip().upper()
    found_delete = False
    for index, student in enumerate(book , start=1):
        if student['id'] == delete_id:
            found_delete = True
            book.remove(student)
            print(f"Đã xóa học sinh có ID {delete_id}")
            break
    if found_delete == False:
        print(f"Không tìm thấy sinh viên nào có mã {delete_id}")



def update_score(book):
    update_id = input("Nhập mã sinh viên mà bạn muốn sửa : ").strip().upper()
    found = False
    for index , student in enumerate(book , start=1):
        if student['id'] == update_id:
            found = True
            updated_math_score = float(input("Nhập điểm toán cập nhật : "))
            updated_english_score = float(input("Nhập điểm tiếng anh cập nhật : "))
            print(f"Đã cập nhật điểm cho học sinh {update_id}")
            student['info'] = (updated_math_score , updated_english_score)
            break
    if found == False:
        print(f"Không tìm thấy ID {update_id} trong danh sách")        

def add_new_book(book):
    while True:
        flag_duplicate = False
        student_id_input = input("Nhập mã học sinh của bạn : ").strip().upper()
        for student in grade_book:
            if student['id'] == student_id_input:
                flag_duplicate = True
                print(f"{student_id_input} đã tồn tại trong danh sách!")
                break
        if flag_duplicate == False:
            new_studentname = input("Nhập tên học sinh : ").strip().lower().title()
            new_math = float(input("Nhập điểm toán : "))
            new_english = float(input("Nhập điểm tiếng anh: "))
            newstudent = {
                 "id": student_id_input,
                 "name": new_studentname, 
                 "info": (new_math, new_english),
                 }
            book.append(newstudent)
            break
    
            

def display_grades(book):
    if len(book) == 0:
        print("Danh sách hiện đang trống")
    else:
        print("        -------- BẢNG ĐIỂM HỌC SINH ---------       ")
        
        for index,student in enumerate(book , start=1):
            average_score = (student['info'][0] + student["info"][1]) / len(student['info'])
            print(f"ID : {student['id']} | Tên học sinh : {student['name']} | Điểm Toán : {student['info'][0]} | Điểm Anh : {student['info'][1]} | Điểm trunh bình : {average_score:.2f}" )


if __name__ == '__main__':
    while True:
        choice = input("""
=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5): 

""")
        match choice:
            case "1":
                display_grades(grade_book)
            
            case "2":
                add_new_book(grade_book)

            case "3":
                update_score(grade_book)
            
            case "4":
                delete_student(grade_book)
            
            case "5":
                print('Thoát chương trình..')
                break
            case _:
                print('Vui lòng chỉ nhập từ 1 - 5')