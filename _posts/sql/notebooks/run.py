import uuid
import random
import json
from faker import Faker
fake = Faker()

# WRITE INSERTS TO FILE
def write_file(filename, lines):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + ";\n")
    print(f"Generated: {filename}")

# --------------------------------------------------------
# 1️⃣ ECOMMERCE DB
# --------------------------------------------------------

# Customers (100)
customers = []
for i in range(100):
    customers.append(
        f"INSERT INTO Customers (full_name, email, phone, city, address, is_active, preferences) VALUES ("
        f"'{fake.name()}', '{fake.email()}', '{fake.msisdn()[:10]}', '{fake.city()}', "
        f"'{fake.address().replace(chr(10), ' ')}', {random.choice([0,1])}, "
        f"'{json.dumps({'theme': random.choice(['dark','light']), 'lang':'en'})}'"
        f")"
    )
write_file("customers.sql", customers)


# Products (100)
categories = ["Electronics", "Clothing", "Furniture", "Other"]
tags = ["New","Sale","Featured","Limited"]

products = []
for i in range(100):
    products.append(
        f"INSERT INTO Products (name, category, price, rating, stock, tags, specs) VALUES ("
        f"'{fake.word().title()}', '{random.choice(categories)}', {round(random.uniform(5,500), 2)}, "
        f"{round(random.uniform(1,5),2)}, {random.randint(0,200)}, "
        f"'{','.join(random.sample(tags, random.randint(1,4)))}', "
        f"'{json.dumps({'color': fake.color_name(), 'weight': random.randint(1,10)})}'"
        f")"
    )
write_file("products.sql", products)


# Orders (100)
orders = []
for i in range(100):
    orders.append(
        f"INSERT INTO Orders (customer_id, order_date, order_time, payment_status, total_amount) VALUES ("
        f"{random.randint(1,100)}, '{fake.date_this_year()}', '{fake.time()}', "
        f"'{random.choice(['Pending','Paid','Failed'])}', {round(random.uniform(20,1000),2)}"
        f")"
    )
write_file("orders.sql", orders)


# OrderItems (100)
order_items = []
for i in range(100):
    qty = random.randint(1,5)
    price = round(random.uniform(5,200),2)
    order_items.append(
        f"INSERT INTO OrderItems (order_id, product_id, quantity, price) VALUES ("
        f"{random.randint(1,100)}, {random.randint(1,100)}, {qty}, {price}"
        f")"
    )
write_file("order_items.sql", order_items)




# --------------------------------------------------------
# 2️⃣ UNIVERSITY DB
# --------------------------------------------------------

# Students (100)
students = []
for i in range(100):
    students.append(
        f"INSERT INTO Students (student_id, full_name, major, email, gpa, admission_year, birthdate, metadata) "
        f"VALUES ('{uuid.uuid4()}', '{fake.name()}', '{fake.job()[:30]}', '{fake.email()}', "
        f"{round(random.uniform(2.0,4.0),2)}, {random.randint(2018,2025)}, "
        f"'{fake.date_of_birth(minimum_age=17, maximum_age=30)}', "
        f"'{json.dumps({'hobby': fake.word()})}'"
        f")"
    )
write_file("students.sql", students)


# Courses (100)
courses = []
for i in range(100):
    cid = f"C{random.randint(10000,99999)}"
    courses.append(
        f"INSERT INTO Courses (course_id, course_name, credits, syllabus, course_outline) VALUES ("
        f"'{cid}', '{fake.sentence()[:-1]}', {random.randint(1,5)}, "
        f"'{fake.text(100)}', '<outline><unit>{fake.word()}</unit></outline>'"
        f")"
    )
write_file("courses.sql", courses)


# Enrollments (100)
enrollments = []
for i in range(100):
    enrollments.append(
        f"INSERT INTO Enrollments (student_id, course_id, grade, semester, attendance) VALUES ("
        f"'{uuid.uuid4()}', 'C{random.randint(10000,99999)}', "
        f"'{random.choice(['A','B','C','D','F'])}', '{random.choice(['Fall','Spring','Summer'])}', "
        f"{round(random.uniform(50,100),2)}"
        f")"
    )
write_file("enrollments.sql", enrollments)


# Professors (100)
professors = []
for i in range(100):
    professors.append(
        f"INSERT INTO Professors (full_name, department, salary, join_date, profile) VALUES ("
        f"'{fake.name()}', '{fake.job()[:20]}', {round(random.uniform(30000,150000),2)}, "
        f"'{fake.date_between(start_date='-10y', end_date='today')}', "
        f"'{json.dumps({'experience': random.randint(1,30)})}'"
        f")"
    )
write_file("professors.sql", professors)


# CourseAssignments (100)
assignments = []
for i in range(100):
    assignments.append(
        f"INSERT INTO CourseAssignments (prof_id, course_id, semester, is_active) VALUES ("
        f"{random.randint(1,100)}, 'C{random.randint(10000,99999)}', "
        f"'{random.choice(['Fall','Spring','Summer'])}', {random.choice([0,1])}"
        f")"
    )
write_file("course_assignments.sql", assignments)
