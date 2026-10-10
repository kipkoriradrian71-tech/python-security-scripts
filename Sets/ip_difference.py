known_good_ips = {"10.0.0.1", "10.0.0.2", "10.0.0.3"}
todays_logins = {"10.0.0.1", "10.0.0.9", "192.168.1.5"}

quiet_ips = known_good_ips.difference(todays_logins)
print(quiet_ips)
