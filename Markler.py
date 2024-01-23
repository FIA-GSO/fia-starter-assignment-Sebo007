open('Test.txt','x')


rooms=int(input("Wie viele Räume gibt es in der Wohnung: "))
print("----- !Achtung!-----\nAlle Werte müssen in Meter angegeben werden")
qm=0
temp_b=0
temp_l=0
it=0
for it in range(rooms):
    print("\n----- Raum",it+1,"-----")
    half=input("Muss der Raum geteilt werden: ")
    if half=="ja" or half=="Ja":
        temp_b=float(input("\nWie Breit ist der 1. Teil des Raumes: "))
        temp_l=float(input("Wie Lang ist der 1. Teil des Raumes: "))
        qm=qm+(temp_b*temp_l)

        temp_b=float(input("\nWie Breit ist der 2. Teil des Raumes: "))
        temp_l=float(input("Wie Lang ist der 2. Teil des Raumes: "))
        qm=qm+(temp_b*temp_l)
    else :
        
        temp_b=float(input("Wie Breit ist der Raum: "))
        temp_l=float(input("Wie Lang ist der Raum: "))
        qm=qm+(temp_b*temp_l)
    
print(f"Die Wohnung umfast ",qm,"Quadratmeter")
