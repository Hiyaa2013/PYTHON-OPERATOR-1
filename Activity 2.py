amount=int(input("Please Enter Ammount For Withdraw..."))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("notes of rs.100 ",note_1)
print("notes of rs.50",note_2)
print("notes of rs.10",note_3)
