import pickle
print("Welcome to the MCQ Test Management System\n")
password="shivmcq"
profile=int(input("Press 1 to login as teacher and Press 0 to login as student: \n"))

class teacher:
    
    def __init__(self,Question,a,b,c,d,answer):
        self.Question=Question
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.answer=answer
        
    def printdetails(self):
        print(self.Question)
        print("a) "+self.a)
        print("b) "+self.b)
        print("c) "+self.c)
        print("d) "+self.d)

    def anscomp(self):
        return self.answer
        
        
if profile==1:
    p_check=input("Enter the password: \n")
    if p_check == password:
        print("\nWelcome to the MCQ Paper Creating Section")
        mcq_count=int(input("Enter the number of MCQ's you want to input: \n"))
        
        f=open("mcqcount.txt","a")
        f.write(str(mcq_count))
        f.close()
        
        n=1
        while (n<=mcq_count):
            f=open(str(n)+" "+"MCQ.txt","wb")
            Question=input("\nEnter the question: ")
            a=input("Enter Option A: ")
            b=input("Enter Option B: ")
            c=input("Enter Option C: ")
            d=input("Enter Option D: ")
            answer=input("Enter the Correct Answer(a,b,c,d): ")
            
            t=teacher(Question,a,b,c,d,answer)         
            pickle.dump(t,f)
            
            n=n+1
            f.close()
    else:
        print("Wrong Password Entered.!!")

elif profile==0:
    print("Welcome to the MCQ Examination\n")
    student_name=input("Enter Your Name: ")
    with open ("mcqcount.txt") as f:
        sample=int(f.read())
        empty=" "
        n=1
        marks=0
        while (n<=sample):
            with open (str(n)+" "+"MCQ.txt","rb") as f:
                    p=pickle.load(f)
                    print("\nQuestion no :",n)
                    p.printdetails()
                    tool=input("Enter your Answer (a,b,c,d): ")
                    content = p.anscomp()
                    if tool in content:
                            marks=marks+1
                    n=n+1
                    f.close()
                    f.close()
    a=f"you have scored {marks} out of {sample}"
    print(a)
                
                
        
