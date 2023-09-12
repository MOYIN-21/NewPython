
age = int(input("Enter your age:"))
max_heart_rate = 220 - age

target_heart_rate_min = 0.5 * max_heart_rate
target_heart_rate_max = 0.85 * max_heart_rate

print("Maximum Heart Rate:", max_heart_rate, "beats per minute")
print("Target Heart Rate Range:", target_heart_rate_min, "to", target_heart_rate_max, "beats per minute")
