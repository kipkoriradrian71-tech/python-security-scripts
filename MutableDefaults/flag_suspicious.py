def flag_suspicious(ip, failed_attempts, flagged=None):
 if flagged is None:
  flagged =[]
 if failed_attempts >=3:
  flagged.append(ip)
 return flagged
result_1 = flag_suspicious("192.168.1.5", 5)
result_2 = flag_suspicious("10.0.0.9", 1)

print(result_1)
print(result_2)
