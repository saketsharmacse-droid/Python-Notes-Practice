meeting = int(input("Enter the number of hours of meeting: "))
battery = list(map(int, input("Enter the battery percentages: ").split()))

count = 0
for i in battery:
    if i >= meeting:
        count += 1
print(f"Total of {count} laptops would be able to participate in meeting")