Exercise 1 – Arithmetic Operators

Question:

Create a program that stores:

a = 25
b = 6

Print:

Addition
Subtraction
Multiplication
Division
Floor Division
Modulus
Expected Output
Addition       : 31
Subtraction    : 19
Multiplication : 150
Division       : 4.166666666666667
Floor Division : 4
Modulus        : 1




Exercise 2 – String Slicing

Question:

Store the string:

language = "Artificial"

Print:

First 5 characters
Last 4 characters
Character at index 3
Complete string followed by " Intelligence"
Expected Output
Artif
cial
i
Artificial Intelligence

Exercise 1 – List Operations

Question:

Create a list:

numbers = [12, 45, 67, 89]

Perform:

Append 100
Insert 5 at index 0
Remove 67
Print the final list
Expected Output
[5, 12, 45, 89, 100]

Exercise 2 – List Functions

Question:

Create the list:

marks = [78, 92, 65, 88, 95, 71]

Print:

Smallest value
Largest value
Total number of elements
First three elements
Expected Output
Smallest : 65
Largest  : 95
Length   : 6
First 3 Elements : [78, 92, 65]



Exercise 1 — Data Type Conversion

Question:

Create a program that:

Stores 98.75 in a variable.
Convert it to an integer.
Convert that integer into a complex number by adding an imaginary part of 5.
Print the type after each conversion.
Expected Output
98
<class 'int'>
(98+5j)
<class 'complex'>

Print the following:

int(True)
int(False)
Result of 15 > 10
Type of 15 > 10
Expected Output
1
0
True
<class 'bool'>

Using range() print:

Numbers from 10 to 20
Even numbers from 10 to 20
Odd numbers from 11 to 19
Expected Output
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[10, 12, 14, 16, 18]
[11, 13, 15, 17, 19]


🟢 EASY - 1

Create a student profile using:

Variables
String
List (5 subjects)
Tuple (DOB)
Set (Skills)
Dictionary (Marks of 3 subjects)

Print:

Student Name
First 3 characters of name
Last character of name
Number of subjects
First subject
DOB
Number of unique skills
Marks dictionary keys
Marks dictionary values
Expected Output
Name : Sravan Kumar
Sra
r
5
Python
(17, 2, 2005)
3
dict_keys(['Python', 'Java', 'SQL'])
dict_values([95, 88, 92])



Create a company profile.

Store:

Company Name
Package
Required Skills (Set)
Interview Rounds (List)

Print:

Company Name
Length of Company Name
First Interview Round
Total Interview Rounds
Package Type
Required Skills
Expected Output
Google
6
OA
4
<class 'int'>
{'Python', 'DSA', 'SQL'}




🟡 MODERATE - 1
Create a dictionary of an employee.

Store:
Name
Company
Salary

Create another list containing:

Python
SQL
Git
Linux

Print:

Employee Name
Company
First Skill
Last Skill
Middle Two Skills
Length of Skills
Salary Type
First 4 characters of Company






🟡 MODERATE - 2

Using only range() create:

Numbers from 1–30.

Print:

First 10 numbers
Last 10 numbers
Numbers divisible by 5
Length
Type
Expected Output
[1,2,3,4,5,6,7,8,9,10]
[21,22,23,24,25,26,27,28,29,30]
[5,10,15,20,25,30]
30
<class 'list'>


🔴 HARD - 1

Create a Placement Database.

Store:

Student Name
College
Branch
CGPA
Skills (Set)
Subjects (List)
Marks (Dictionary)
Graduation Year
DOB (Tuple)

Now print:

Student Name
First Name only
Last Name only
First Skill
Total Skills
First Subject
Last Subject
Highest Marks Subject (manually choose from dictionary)
Dictionary Keys
Dictionary Values
Branch Length
Type of CGPA
Graduation Year + 1
Last 3 characters of College

🔴 HARD - 2 (Interview Style)

Create an AI Engineer Profile.

Store:

Name
Role
Company
Experience
Salary
Technologies (List)
Certifications (Tuple)
Projects (Set)
Performance (Dictionary)

Print:

Full Name
Initials
Company Length
Last Technology
First 2 Technologies
Number of Projects
Number of Certifications
Performance Keys
Performance Values
Type of Salary
Boolean Result of Salary > 15
Integer value of the Boolean
Numbers from 2–20 using range()
Even numbers
Odd numbers
Expected Output
Sravan Kumar
SK
6
Docker
['Python','SQL']
4
3
dict_keys(...)
dict_values(...)
<class 'int'>
True
1
[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
[2,4,6,8,10,12,14,16,18,20]
[3,5,7,9,11,13,15,17,19]


Question 1

A server stores the value 128. Display its:

Binary representation
Octal representation
Hexadecimal representation

Expected Output

0b10000000
0o200
0x80


Question 2

A system stores the value 144. Display:

Square root
Floor of 9.95
Ceiling of 9.01

Expected Output

12.0
9
10

Question 3

Two conditions are:

Age is greater than 18.
Salary is greater than ₹5 LPA.

Display:

Result using AND
Result using OR
Opposite of the first condition

Expected Output

True
True
False


🟡 Level 2 (Moderate)
Question 1

Two system flags are 45 and 29.

Display:

Bitwise AND
Bitwise OR
Bitwise XOR

Expected Output

13
61
48




Question 2

A cloud server has 64 GB RAM.

Display:

Left Shift by 3
Right Shift by 2

Expected Output

512
16


A company stores:

CPU = 16
RAM = 32
Storage = 512

Display:

Binary value of Storage
Hexadecimal value of RAM
Whether CPU is greater than 8 AND RAM is greater than 16

Expected Output

0b1000000000
0x20
True



🔴 Level 3 (Hard)
Question 1

A security system stores the values 170 and 85.

Display:

Bitwise AND
Bitwise OR
Bitwise XOR
Left Shift of the first value by 2
Right Shift of the second value by 3

Expected Output

0
255
255
680
10

Question 2

A data center stores:

Servers = 1024
Active Servers = 768

Display:

Binary value of Active Servers
Octal value of Servers
Hexadecimal value of Active Servers
Square root of Servers
Floor of 31.99
Ceiling of 31.01

Expected Output

0b1100000000
0o2000
0x300
32.0
31
32

Question 3 (Interview Level)

A candidate has:

Coding Score = 88
Aptitude Score = 76

Display:

Bitwise AND
Bitwise OR
Bitwise XOR
Binary value of Coding Score
Hexadecimal value of Aptitude Score
Whether Coding Score is greater than 80 AND Aptitude Score is greater than 70
Opposite of the condition "Coding Score is less than 90"

Expected Output

72
92
20
0b1011000
0x4c
True
False




🟡 Mock Interview Round 2
Company: Amazon SDE Intern (Fundamentals Round)
Scenario

Amazon's recruitment team wants a small console application to generate an internship candidate report before scheduling interviews.

The HR manager has given you the following requirements.

The report must display:

Candidate ID
Candidate Name
College
Branch
Current CGPA
Graduation Year

The report must also include:

All programming languages known by the candidate
Total programming languages
All technologies the candidate has worked with
Total technologies
All completed projects
Total projects
Technical interview scores
Highest interview score
Lowest interview score

Finally, display:

Internship stipend
Stipend data type
Binary representation of stipend
Hexadecimal representation of stipend

The HR team also wants to know:

Whether the candidate is eligible for the internship.
Expected joining year (one year after graduation).

End the report professionally.

Expected Output Format
==================================================
           AMAZON INTERNSHIP REPORT
==================================================

----------- Candidate Details -----------

Candidate ID          :
Candidate Name        :
College               :
Branch                :
CGPA                  :
Graduation Year       :

----------- Technical Profile -----------

Programming Languages :
Total Languages       :

Technologies          :
Total Technologies    :

Projects              :
Total Projects        :

----------- Assessment -----------

Interview Scores      :
Highest Score         :
Lowest Score          :

----------- Internship -----------

Stipend               :
Type                  :
Binary                :
Hexadecimal           :

Eligible              :
Joining Year          :

==================================================
              END OF REPORT
==================================================