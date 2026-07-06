#### candidate details ###

Candidate_Name = "Sravan Kumar"
College = "AVNIET"
Branch = "AI&DS"
Cgpa = 7.8
Graduation_Year = 2027

### Technologies #####

Technologies = ['git','docker','cloud','html','mongodb']

### SKills ###

Skills = {"python","java","communication","problem solving","Teamwork"}

### Subjects ####

Subjects = ['java','python','c++','DBMS','cn']

#### interview Scores ####

keys = ['aptitude','reasoning','technical','hr']
values = [65,58,90,89]
Interview_scores = dict(zip(keys,values))

### internship package details #### 

Internship_package = 50000


# Printing values

print("Name            :",Candidate_Name)
print("College         :",College)
print("Branch          :",Branch)
print("CGPA            :",Cgpa)
print("Graduation Year :",Graduation_Year)

print("Technologies  :" ,Technologies)
print("Total Technologies : ",(len(Technologies)))

print("Total Skills :",Skills)
print("Skills :" , len(Skills))

print("Subjects :",Subjects)
print("First Subject :",Subjects[0])
print("Last Subject :",Subjects[4])

print("Interview Scores :",Interview_scores)
print("Highest Interview Score :" ,(max(values)))
print("Lowest Interview Score :" ,(min(values)))

print("Internship Package :",Internship_package)
print("Package Type :",type(Internship_package))
print("Package (Binary) :",(bin(Internship_package)))
print("Package (Hexadecimal) :",(hex(Internship_package)))
      
