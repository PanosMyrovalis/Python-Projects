# ΑΣΚΗΣΗ 7.5


#δημιουργία μιας κενής λίστας 
students_grades = list()


#πλήθος των βαθμολογιών που θα εισάγει ο χρήστης
number_of_grades = 10


for i in range (number_of_grades):
    
    try:
        
        #Διάβασμα της βαθμολογίας (grade) του χρήστη 
        grade = int(input(f"Δώσε τη βαθμολογία του {i+1}ου μαθητή: "))
        
        assert 0 <= grade <= 10  #προφανώς οι επιθυμητές τιμές των βαθμολογιών κυμαίνονται μεταξύ 0 και 10
        
    
    #Έλεγχος για συντακτικά λάθη 
    except ValueError:
        print(f" Δεν έδωσες κάποιον αριθμό. Παρακαλώ ξαναπροσπάθησε!")
 


    #Έλεγχος για λογικά λάθη   
    except AssertionError :
        print(f" Μη επιτρεπτή είσοδος. Η βαθμολογία κυμαίνεται μεταξύ 0 και 10. Παρακαλώ ξαναπροσπάθησε!")
        
        
    
    else :
       
       #Εισαγωγή του βαθμού στη λίστα
       students_grades.append(grade)
       
       

#Yπολογισμός του μέσου όρου των βαθμών
average_grade = sum(students_grades) / len(students_grades)   


#Εύρεση του μέγιστου βαθμού
max_grade = max(students_grades) 


#Εύρεση του ελάχιστου βαθμού
min_grade = min(students_grades) 

count = 0

#Yπολογισμός του ποσοστόυ επιτυχίας των μαθητών
for i in students_grades:
    
    if(i >= 5):
        
        count = count + 1

percentage_of_success = (count / number_of_grades) * 100



print(f" O μέσος όρος των βαθμών είναι ίσος με {average_grade}")


print(f" O μέγιστος βαθμός είναι ίσος με {max_grade}")


print(f" O ελάχιστος βαθμός είναι ίσος με {min_grade}")


print(f" To ποσοστό επιτυχίας των μαθητών είναι ίσο με {percentage_of_success} %")

students_grades.sort(reverse=True)

print(f" Όλοι οι βαθμοί που καταχωρήσατε είναι οι εξής : {students_grades}")


    
       
       
       
       
       


        
        
        
        
         
         
         
         
        
        
    
    