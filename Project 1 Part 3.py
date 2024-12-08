import sqlite3

connection = sqlite3.connect('Pawsome Pets_database.db')  # Connect to your database
cursor = connection.cursor()

queries = [
    """
    CREATE TABLE Clinic (
      clinicNo INT PRIMARY KEY,
      name TEXT NOT NULL,
      address TEXT NOT NULL,
      telephone TEXT NOT NULL,
      StaffNo INT
    );
    """,
    """
    CREATE TABLE Staff (
      staffNo INT PRIMARY KEY,
      name TEXT NOT NULL,
      address TEXT NOT NULL,
      telephone TEXT NOT NULL,
      DOB TEXT NOT NULL,
      position TEXT NOT NULL CHECK( position IN ('Vet', 'Nurse', 'Receptionist') ),
      salary DECIMAL(10, 2) NOT NULL,
      clinicNo INT,
      FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    );
    """,
    """
    CREATE TABLE Owner (
      ownerNo INT PRIMARY KEY,
      name TEXT NOT NULL,
      address TEXT NOT NULL,
      telephone TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE Pet (
      petNo INT PRIMARY KEY,
      name TEXT NOT NULL,
      DOB TEXT NOT NULL,
      species TEXT NOT NULL CHECK( species IN ('Dog', 'Cat', 'Bird') ),
      breed TEXT NOT NULL,
      color TEXT NOT NULL,
      ownerNo INT NOT NULL,
      clinicNo INT NOT NULL,
      FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
      FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    );
    """,
    """
    CREATE TABLE Examination (
      examNo INT PRIMARY KEY,
      complaint TEXT NOT NULL,
      description TEXT NOT NULL,
      date TEXT NOT NULL,
      actions TEXT NOT NULL,
      petNo INT NOT NULL,
      staffNo INT NOT NULL,
      FOREIGN KEY (petNo) REFERENCES Pet(petNo),
      FOREIGN KEY (staffNo) REFERENCES Staff(staffNo)
    );
    """
]

queries = [
    """
    INSERT INTO Clinic VALUES 
    (1, 'Happy Paws', '123 Main St', '123-456-7890', NULL),
    (2, 'Pet Care', '456 Oak St', '987-654-3210', 1),
    (3, 'Vet Clinic', '789 Pine St', '456-789-1234', 2),
    (4, 'Animal House', '321 Elm St', '321-654-9870', 3),
    (5, 'Paws and Claws', '654 Birch St', '789-123-4567', 4);
    """,
    """
    INSERT INTO Staff VALUES
    (1, 'John Doe', '111 First St', '111-111-1111', '1980-01-01', 'Vet', 80000, 2),
    (2, 'Jane Smith', '222 Second St', '222-222-2222', '1985-02-02', 'Nurse', 60000, 3),
    (3, 'Bob Johnson', '333 Third St', '333-333-3333', '1990-03-03', 'Receptionist', 40000, 4),
    (4, 'Alice Williams', '444 Fourth St', '444-444-4444', '1995-04-04', 'Vet', 80000, 5),
    (5, 'Charlie Brown', '555 Fifth St', '555-555-5555', '2000-05-05', 'Nurse', 60000, 1);
    """,
    """
    INSERT INTO Owner VALUES 
    (1, 'Tom Davis', '666 Sixth St', '666-666-6666'),
    (2, 'Mary Miller', '777 Seventh St', '777-777-7777'),
    (3, 'James Wilson', '888 Eighth St', '888-888-8888'),
    (4, 'Patricia Moore', '999 Ninth St', '999-999-9999'),
    (5, 'Robert Taylor', '1010 Tenth St', '101-010-1010');
    """,
    """
    INSERT INTO Pet VALUES 
    (1, 'Rex', '2010-06-06', 'Dog', 'Labrador', 'Yellow', 1, 1),
    (2, 'Mittens', '2011-07-07', 'Cat', 'Siamese', 'White', 2, 2),
    (3, 'Tweety', '2012-08-08', 'Bird', 'Canary', 'Yellow', 3, 3),
    (4, 'Fido', '2013-09-09', 'Dog', 'Bulldog', 'Brown', 4, 4),
    (5, 'Whiskers', '2014-10-10', 'Cat', 'Persian', 'Grey', 5, 5);
    """,
    """
    INSERT INTO Examination VALUES 
    (1, 'Coughing', 'Coughing for a week', '2022-01-01', 'Prescribed cough medicine', 1, 1),
    (2, 'Limping', 'Limping after fall', '2022-01-02', 'X-ray showed no fracture', 2, 2),
    (3, 'Not eating', 'Not eating for two days', '2022-01-03', 'Prescribed appetite stimulant', 3, 3),
    (4, 'Scratching', 'Scratching excessively', '2022-01-04', 'Treated for fleas', 4, 4),
    (5, 'Vomiting', 'Vomiting after meals', '2022-01-05', 'Diet change recommended', 5, 5);
    """
]

# Import pandas
import pandas as pd

# Select data
query = """
    SELECT *
    FROM Clinic
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

# Commit any changes to the database
connection.commit()

# Select data from Staff table
query = """
    SELECT *
    FROM Staff
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df_staff = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df_staff)
print(df_staff.columns)

# Commit any changes to the database
connection.commit()

# Select data from Owner table
query = """
    SELECT *
    FROM Owner
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df_staff = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df_staff)
print(df_staff.columns)

# Commit any changes to the database
connection.commit()

# Select data from Pet table
query = """
    SELECT *
    FROM Pet
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df_staff = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df_staff)
print(df_staff.columns)

# Commit any changes to the database
connection.commit()

# Select data from Examination table
query = """
    SELECT *
    FROM Examination
"""
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df_staff = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df_staff)
print(df_staff.columns)

# Commit any changes to the database
connection.commit()

#1. Add a new pet:
new_pet_data = (9, 'New Pet', '2010-01-01', 'Dog', 'Bulldog', 'Black', 1, 1) #change the number if code is ran more than once to avoid error
cursor.execute("INSERT INTO Pet VALUES (?, ?, ?, ?, ?, ?, ?, ?)", new_pet_data)
cursor.execute("SELECT * FROM Pet WHERE petNo = ?", (new_pet_data[0],))
print("New Pet:")
print(cursor.fetchone())

#2. new_staff_info = ('New Address', 'New Telephone', 1)
# Define new staff info
new_staff_info = ('123 New St', '123-456-7890', 1)  # New address, new telephone, staffNo

# Use new_staff_info in your UPDATE query
cursor.execute("UPDATE Staff SET address = ?, telephone = ? WHERE staffNo = ?", new_staff_info)

# Verify the update
cursor.execute("SELECT * FROM Staff WHERE staffNo = ?", (new_staff_info[2],))
print("Updated Staff Info:")
print(cursor.fetchone())

# Commit changes to the database
connection.commit()

#3. Register a new owner:
new_owner_data = (9, 'New Owner', 'New Address', 'New Telephone') #change the number if code is ran more than once to avoid error
cursor.execute("INSERT INTO Owner VALUES (?, ?, ?, ?)", new_owner_data)
cursor.execute("SELECT * FROM Owner WHERE ownerNo = ?", (new_owner_data[0],))
print("New Owner:")
print(cursor.fetchone())

#4. Record a new examination:
new_exam_data = (8, 'New Complaint', 'New Description', '2022-01-01', 'New Actions', 1, 1) #change the number if code is ran more than once to avoid error
cursor.execute("INSERT INTO Examination VALUES (?, ?, ?, ?, ?, ?, ?)", new_exam_data)
cursor.execute("SELECT * FROM Examination WHERE examNo = ?", (new_exam_data[0],))
print("New Examination:")
print(cursor.fetchone())

#5. Change a pet's clinic:
new_clinic_info = (2, 1)
cursor.execute("UPDATE Pet SET clinicNo = ? WHERE petNo = ?", new_clinic_info)
cursor.execute("SELECT * FROM Pet WHERE petNo = ?", (new_clinic_info[1],))
print("Updated Pet Clinic:")
print(cursor.fetchone())

connection.commit()
connection.close()