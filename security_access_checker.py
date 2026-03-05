allowed_permissions={"read","write","list"}
admin_permissions={"read","write","list","delete","modify"}
read_only_permissions={"read"}
user1_permissions={"read","list"}
user2_permissions={"read","write","delete"}
user3_permissions={"read","write","list","delete","modify"}
user4_permissions=set()

print("==SECURITY ACCESS REPORT==")
print()
print("User1 Permissions:", user1_permissions)
if user1_permissions.issubset(allowed_permissions):
 print("User1 is safe , no unauthorized permissions")
else:
 print("ALERT! User1 has unauthorized access")
 print("Unauthorized permissions:", user1_permissions -allowed_permissions)
print()
print("User2 Permissions :", user2_permissions)
if user2_permissions.issubset(allowed_permissions):
 print("User2 is safe , no unauthorized permissions ")
else:
 print("ALERT! User2 has unauthorized access")
 print("Unauthorized permissions:", user2_permissions - allowed_permissions)
print()
print("User3 Permissions :", user3_permissions)
if user3_permissions==admin_permissions:
 print("User 3 has authorized access as the Admin")
else:
 print("User3 has unauthorized Admin permissions")
 print("Unauthorized Admin permissions:", user3_permissions-admin_permissions)
print()
print("User1  permissions:",user1_permissions)
if user1_permissions == read_only_permissions:
 print("User1 is viable for read only permissions")
else:
 print("User1 does not have read only permissions")
print()
print("User2  permissions:",user2_permissions)
if user2_permissions == read_only_permissions:
 print("User2 is viable for read only permissions")
else:
 print("User2 does not have read only permissions")
print()
print("User3 permissions:",user3_permissions)
if user3_permissions == read_only_permissions:
 print("User3 is viable for read only permissions")
else:
 print("User3 does not have read only permissions")
print()
shared_permissions=user1_permissions&user2_permissions&user3_permissions
print("Shared permissions by all users :",shared_permissions)