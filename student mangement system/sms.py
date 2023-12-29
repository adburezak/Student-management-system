from tkinter import *
from tkinter import ttk
from sqlite3 import *

window = Tk()  # creating window
window.geometry('1450x550')  # making window geometry
window.title('STUDENT MANAGEMENT SYSTEM')  # giving title to the window
window.configure(bg='#D3D3D3')  # setting window color to light gray

# label of student management system
label_of_stud = Label(window, text='STUDENT MANAGEMENT SYSTEM', bg='gray', fg='white', font=('Helvetica bold', 20))
label_of_stud.pack(fill=X)

# label frame ou user information
label_of_frame = LabelFrame(window, text='user ', bg='#D3D3D3', borderwidth=5)
label_of_frame.pack(side=LEFT, fill=BOTH)
main_frame = Frame(label_of_frame, bg='#D3D3D3')
main_frame.grid(column=0, row=0)

asses_frame = LabelFrame(main_frame, text='assesement', bg='#D3D3D3', borderwidth=5)
asses_frame.grid(column=0, row=2, padx=12, pady=20)

name_id_frame = LabelFrame(main_frame, text='name', bg='#D3D3D3', borderwidth=5)
name_id_frame.grid(column=0, row=0, padx=5, pady=10)

gender_department_course_frame = LabelFrame(main_frame, text='gender and department ', bg='#D3D3D3', borderwidth=5)
gender_department_course_frame.grid(column=0, row=1, pady=30)

button_frame = LabelFrame(main_frame, text='button', bg='#D3D3D3', borderwidth=5)
button_frame.grid(column=0, row=3, padx=30, pady=10, )

label_of_data = LabelFrame(window, text='data', bg='#D3D3D3', borderwidth=5)
label_of_data.pack(side=LEFT, padx=10, pady=10)
main_frame1 = Frame(label_of_data, bg='#D3D3D3')
main_frame1.grid(column=0, row=0)






# labels for user inputs
name_label = Label(name_id_frame, text='FIRST NAME', bg='#D3D3D3', fg='black', font=('Helvetica bold', 10))
name_label.grid(column=0, row=0, pady=0)

last_name_label = Label(name_id_frame, text='LAST NAME', bg='#D3D3D3', fg='black', font=('Helvetica bold', 10))
last_name_label.grid(column=1, row=0)

ID_number_label = Label(name_id_frame, text='ID NUMBER', bg='#D3D3D3', fg='black', font=('Helvetica bold', 10))
ID_number_label.grid(column=2, row=0)

gender_label = Label(gender_department_course_frame, text='GENDER', bg='#D3D3D3', fg='black',
                     font=('Helvetica bold', 10))
gender_label.grid(column=0, row=0, pady=5)

department_label = Label(gender_department_course_frame, text='DEPARTMENT', bg='#D3D3D3', fg='black',
                         font=('Helvetica bold', 10))
department_label.grid(column=0, row=1, pady=5)

course_label = Label(gender_department_course_frame, text='COURSE', bg='#D3D3D3', fg='black',
                     font=('Helvetica bold', 10))
course_label.grid(column=0, row=2, pady=5)

assignment_label = Label(asses_frame, text='ASSIGNMENT', bg='#D3D3D3', fg='black', font=('Helvetica bold', 10))
assignment_label.grid(column=0, row=0)

mid_exam_label = Label(asses_frame, text='MID EXAM', bg='#D3D3D3', fg='black', font=('Helvetica bold', 10))
mid_exam_label.grid(column=1, row=0)

final_exam_label = Label(asses_frame, text='FINAL EXAM', bg='#D3D3D3', fg='black', font=('Helvetica bold', 10))
final_exam_label.grid(column=2, row=0)








# entry boxes for inputs
name_entry = Entry(name_id_frame)
name_entry.grid(column=0, row=1, padx=20, pady=10)

last_name_entry = Entry(name_id_frame)
last_name_entry.grid(column=1, row=1, padx=20, pady=10)

ID_number_entry = Entry(name_id_frame)
ID_number_entry.grid(column=2, row=1, padx=20, pady=10)

assignment_entry = Entry(asses_frame)
assignment_entry.grid(column=0, row=1, padx=20, pady=10)

mid_exam_entry = Entry(asses_frame)
mid_exam_entry.grid(column=1, row=1, padx=20, pady=10)

final_exam_entry = Entry(asses_frame)
final_exam_entry.grid(column=2, row=1, padx=20, pady=10)






# radio button , combobox , spinbox forms
radio_var = StringVar(value=' ')

male_radio = Radiobutton(gender_department_course_frame, text="MALE", variable=radio_var, value='MALE', bg='#D3D3D3',
                         fg='black')
male_radio.grid(column=1, row=0)
female_radio = Radiobutton(gender_department_course_frame, text="FEMALE", variable=radio_var, value='FEMALE',
                           bg='#D3D3D3', fg='black')
female_radio.grid(column=2, row=0)

combo_var = StringVar()
department_combo = ttk.Combobox(gender_department_course_frame, width=20,textvariable=combo_var )
# Adding combobox drop down list
department_combo['values'] = ('Information Technology ',
                              'software engineering',
                              'computer science',
                              'information system',
                              'information science',
                              )
department_combo.grid(column=1, row=1, padx=5)
department_combo.current()


# spin box grid
data = ['c++', 'java', 'PHP', 'c#', 'python']
spin_var = StringVar()
my_spinbox = Spinbox(gender_department_course_frame, values=data, textvariable=spin_var, width=10, font="Calibri, 10")
my_spinbox.grid(column=1, row=2, pady=5)
spin_var.set('')

# tree view
t = ttk.Treeview(main_frame1, height=17)
t['columns'] = (
    'firstname', 'lastname', 'ID', 'gender', 'department', 'course', 'assignment', 'mid exam', 'final exam',
    'total mark',
    'grade')
# formatting the table
t.column('#0', anchor=W, width=0)
t.column('firstname', anchor=W, width=80)
t.column('lastname', anchor=W, width=80)
t.column('ID', anchor=CENTER, width=80)
t.column('gender', anchor=W, width=80)
t.column('department', anchor=W, width=80)
t.column('course', anchor=W, width=80)
t.column('assignment', anchor=W, width=80)
t.column('mid exam', anchor=W, width=80)
t.column('final exam', anchor=W, width=80)
t.column('total mark', anchor=W, width=80)
t.column('grade', anchor=W, width=80)
# creating heading
t.heading('firstname', text='first name', anchor=W)
t.heading('lastname', text='lastname', anchor=W)
t.heading('ID', text='ID', anchor=CENTER)
t.heading('gender', text='gender', anchor=W)
t.heading('department', text='department', anchor=W)
t.heading('course', text='course', anchor=W)
t.heading('assignment', text='assignment', anchor=W)
t.heading('mid exam', text='mid exam', anchor=W)
t.heading('final exam', text='final exam', anchor=W)
t.heading('total mark', text='total mark', anchor=W)
t.heading('grade', text='grade', anchor=W)
t.grid(column=0, row=0, pady=20, padx=10)


def select(event):
    # get the selected item
    item = t.selection()[0]
    # get the value of the selected item
    selected_value = t.item(item)["values"][0]
    selected_value1 = t.item(item)["values"][1]
    selected_value2 = t.item(item)["values"][2]
    radio_var.set(t.item(item)["values"][3])
    combo_var.set(t.item(item)["values"][4])
    spin_var.set(t.item(item)["values"][5])
    selected_value6 = t.item(item)["values"][6]
    selected_value7 = t.item(item)["values"][7]
    selected_value8 = t.item(item)["values"][8]

    # insert the value into the entry widget
    name_entry.delete(0, END)
    name_entry.insert(0, selected_value)
    last_name_entry.delete(0, END)
    last_name_entry.insert(0, selected_value1)
    ID_number_entry.delete(0, END)
    ID_number_entry.insert(0, selected_value2)
    assignment_entry.delete(0, END)
    assignment_entry.insert(0, selected_value6)
    mid_exam_entry.delete(0, END)
    mid_exam_entry.insert(0, selected_value7)
    final_exam_entry.delete(0, END)
    final_exam_entry.insert(0, selected_value8)


def total():
    tot = int(assignment_entry.get()) + int(mid_exam_entry.get()) + int(final_exam_entry.get())
    return tot


def grade_tot():
    if 90.00 <= total() <= 100.00:
        return 'A+'
    elif 85.00 <= total() <= 89.99:
        return 'A'
    elif 80.00 <= total() <= 84.99:
        return 'A-'
    elif 75.00 <= total() <= 79.99:
        return 'B+'
    elif 70.00 <= total() <= 74.99:
        return 'B'
    elif 65.00 <= total() <= 69.99:
        return 'B-'
    elif 60.00 <= total() <= 64.99:
        return 'C+'
    elif 50.00 <= total() <= 59.99:
        return 'C'
    elif 45.00 <= total() <= 49.99:
        return 'C-'
    elif 40.00 <= total() <= 44.99:
        return 'D'
    else:
        return 'F'


def insert_data():
    # get the values from the widgets
    first_name = name_entry.get()
    last_name = last_name_entry.get()
    id = ID_number_entry.get()
    gender = radio_var.get()
    department = combo_var.get()
    course = my_spinbox.get()
    assignment = assignment_entry.get()
    mid_exam = mid_exam_entry.get()
    final_exam = final_exam_entry.get()
    total_mark = total()
    grade = grade_tot()

    conn = connect('super7.db')
    conn.execute('''INSERT INTO STUDENT2 (first_name, last_name, ID, gender, department, course, assignment, 
    mid_exam, final_exam, total_mark, grade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        first_name, last_name, id, gender, department, course, assignment, mid_exam, final_exam, total_mark, grade))

    t.insert("", END, values=(
        first_name, last_name, id, gender, department, course, assignment, mid_exam, final_exam, total_mark, grade))

    conn.commit()
    conn.close()
    # clearing the entry spaces
    name_entry.delete(0, END)
    radio_var.set(value=' ')
    combo_var.set(value=' ')
    spin_var.set(value=' ')
    last_name_entry.delete(0, END)
    ID_number_entry.delete(0, END)
    assignment_entry.delete(0, END)
    mid_exam_entry.delete(0, END)
    final_exam_entry.delete(0, END)


def review():
    conn = connect('super7.db')
    cur = conn.cursor()
    cur.execute('''select *from student2''')
    f = cur.fetchall()
    if not t.get_children():
        for i in f:
            t.insert('', END, values=i)
    conn.commit()
    conn.close()
    name_entry.delete(0, END)
    radio_var.set(value=' ')
    combo_var.set(value=' ')
    spin_var.set(value=' ')
    last_name_entry.delete(0, END)
    ID_number_entry.delete(0, END)
    assignment_entry.delete(0, END)
    mid_exam_entry.delete(0, END)
    final_exam_entry.delete(0, END)


def delete_record():
    conn = connect("super7.db")
    cur = conn.cursor()
    for selected_item in t.selection():
        print(selected_item)  # it prints the selected row id
        cur.execute("DELETE FROM student2 WHERE id=?", (t.set(selected_item, '#3'),))
        conn.commit()
        t.delete(selected_item)

    name_entry.delete(0, END)
    radio_var.set(value=' ')
    combo_var.set(value=' ')
    spin_var.set(value=' ')
    last_name_entry.delete(0, END)
    ID_number_entry.delete(0, END)
    assignment_entry.delete(0, END)
    mid_exam_entry.delete(0, END)
    final_exam_entry.delete(0, END)


def update():
    # get the selected item from the treeview
    item = t.selection()[0]
    # get the ID of the selected item
    selected_id = t.item(item, 'values')[2]

    # get the values from the input fields
    first_name = name_entry.get()
    last_name = last_name_entry.get()
    gender = radio_var.get()
    department = combo_var.get()
    new_id = ID_number_entry.get()
    course = my_spinbox.get()
    assignment = assignment_entry.get()
    mid_exam = mid_exam_entry.get()
    final_exam = final_exam_entry.get()
    total_mark = total()
    grade = grade_tot()

    # update the database with the new values
    conn = connect("super7.db")
    cur = conn.cursor()
    cur.execute("UPDATE student2 SET first_name = ?, last_name = ? , ID = ? ,  gender = ? , department = ? , "
                "course = ? ,"
                "assignment = ? , mid_exam = ? ,final_exam = ?,total_mark = ?,grade = ? WHERE ID =?", (
                    first_name, last_name, new_id, gender, department, course, assignment, mid_exam, final_exam,
                    total_mark, grade, selected_id))
    conn.commit()
    conn.close()

    # update the selected item in the treeview with the new values
    t.item(item, text=new_id, values=(
        first_name, last_name, new_id, gender, department, course, assignment, mid_exam, final_exam, total_mark, grade))

    name_entry.delete(0, END)
    radio_var.set(value=' ')
    combo_var.set(value=' ')
    spin_var.set(value=' ')
    last_name_entry.delete(0, END)
    ID_number_entry.delete(0, END)
    assignment_entry.delete(0, END)
    mid_exam_entry.delete(0, END)
    final_exam_entry.delete(0, END)


t.bind("<<TreeviewSelect>>", select)

add_record_button = Button(button_frame, text='add record', command=insert_data, bg='#088F8F', fg='white')
add_record_button.grid(column=0, row=0, padx=10)

delete_record_button = Button(button_frame, text='delete record', command=delete_record, bg='#8F282B', fg='white')
delete_record_button.grid(column=1, row=0, padx=5)

update_record_button = Button(button_frame, text='update record', command=update, bg='#088F8F', fg='white')
update_record_button.grid(column=2, row=0, padx=5)

review_records_button = Button(button_frame, text='review record', command=review, bg='#088F8F', fg='white')
review_records_button.grid(column=3, row=0, padx=5)

window.resizable(False, False)
window.mainloop()
