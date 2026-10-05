
name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

score = (len(name1) + len(name2)) * 7 % 101

print()
print("💕 Love Compatibility Calculator 💕")
print(name1, "❤️", name2)
print("Compatibility:", score, "%")
if percentage >= 80:
    print("💕 Perfect match!")
elif percentage >= 60:
    print("❤️ Very good compatibility!")
elif percentage >= 40:
    print("😊 There is some connection!")
else:
    print("😅 Maybe just friends!")
