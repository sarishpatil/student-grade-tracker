import json
import os

DATA_FILE = "student.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return{}

def save_data():
    with open(DATA_FILE,"w") as file:
        json.dump(students, file, indent=4)
        
students = load_data()

def add_student():
    name = input("Enter student name: ").strip().title()
    if name in students:
        print(f"Error: {name} is already registered")
        return
        
    try:
        grade=float(input("Enter grade: "))
        attendance=float(input("Enter attendance %: "))
        
        students[name]={
            "grade":grade,
            "attendance":attendance
        }
        print("Name added successfully")
        
    except ValueError:
        print("Invalid input")
    
def view_students():
    if not students:
        print("\nNo student record was found")
        return
    print("\n" + "=" * 45)
    print(f"{'Name':<20} | {'Grade (%)':<10} | {'Attendance (%)':<12}")
    print("=" * 45)
    for name, info in students.items():
        print(f"{name:<20} | {info['grade']:<10.1f} | {info['attendance']:<12.1f}")
    print("=" * 45) 

def main():
    while True:
        print("\n===STDENT GRADE CALCULATOR===")
        print("1. View all students ")
        print("2. Add new student ")
        print("3. Exit")
        
        choice=input("Enter your choice: ").strip()
        
        if choice=="1":
            view_students()
        elif choice=="2":
            add_student()
        elif choice=="3":
            print("Exiting program")
            break
        else:
            print("Invalid selection")
            
if __name__=="__main__":
    main()
    

    

    