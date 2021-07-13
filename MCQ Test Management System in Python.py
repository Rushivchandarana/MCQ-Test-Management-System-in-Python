print("Welcome to the MCQ Test Management System\n")
password="shivmcq"
profile=int(input("Press 1 to login as teacher and Press 0 to login as student: \n"))

if profile==1:
    p_check=input("Enter the password: \n")
    if p_check == password:
        print("\nWelcome to the MCQ Paper Creating Section")
        subject=input("Enter the Subject: ")
        mcq_count=int(input("Enter the number of MCQ's you want to input: "))
        
        f=open("mcqcount.txt","a")
        f.write(str(mcq_count))
        f.close()
        
        n=1
        while (n<=mcq_count):
            f=open(str(n)+" "+"MCQ.txt","a")
            Question=input("\nEnter the question: ")
            a=input("Enter Option A: ")
            b=input("Enter Option B: ")
            c=input("Enter Option C: ")
            d=input("Enter Option D: ")
            
            f.write(str(n)+". "+Question)    
            f.write("\n(a)"+" "+a)    
            f.write("\n(b)"+" "+b)    
            f.write("\n(c)"+" "+c)    
            f.write("\n(d)"+" "+d)
           
            Data=open("Answers.txt","a")
            ans=input("Enter the Correct Answer(a,b,c,d): ")
            Data.write("\nMcq"+str(n)+"="+ans)
            
            n=n+1
            f.close()
            Data.close()
    else:
        print("Wrong Password Entered.!!")

elif profile==0:
    print("Welcome to the MCQ Examination\n")
    student_name=input("Enter Your Name: ")
    
    with open ("mcqcount.txt") as f:
        sample=int(f.read())
        n=1
        marks=0
        
        while (n<=sample):
            with open (str(n)+" "+"MCQ.txt") as f:
                    qreader=f.read()
                    print(qreader)
                    tool=input("\nEnter your answer: ")
                    
                    with open ("Answers.txt") as f:
                        content=f.readlines()[n]
                        if tool in content:
                            marks=marks+1
                        n=n+1
                        f.close()
                        f.close()
                        
    a=f"you have scored {marks} out of {sample}"
    print(a)
                
                
        
