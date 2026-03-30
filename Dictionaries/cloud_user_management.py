users={
"user1":{"name":"adi","role":"admin","active":True},
"user2":{"name":"cedo","role":"developer","active":True},
"user3":{"name":"kim","role":"viewer","active":False}
}
print("***CLOUD USER MANAGEMENT SYSTEM*** ")
print()
 
print("~~All Cloud Users~~")
for users_id,details in users.items():
 print(users_id)
 for key, value in details.items():
  print("->",key+":", value)
print()

print("--Active Status Check--")
for users_id,details in users.items():
 if details["active"]==True:
  print(details["name"] ,"is ACTIVE")
 else:
  print(details["name"],"is INACTIVE")
  
users.update({"user4":{"name":"chiri","role":"viewer","active":True}})
print()
print("~~New User Added~~")
print(users["user4"])
print()
 
users["user3"]["active"]=True
print("#Activating Kim#")
print("Is Kim active :",users["user3"]["active"])
print()

users["user2"]["active"]=False
print("#Deactivating Cedo#")
print("Is Cedo active :",users["user2"]["active"])
print()

removed_user=users.pop("user1")
print("~~Removing a user~~")
print("The removed user is :", removed_user["name"])
print()
print("Remaining users:")
for users_id, details in users.items():
 print("*",details["name"],"->",details["role"])
 
print("==THE END==")
