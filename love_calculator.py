name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

combined_names = (name1 + name2).lower()

score = sum(ord(char) for char in combined_names)

percentage = score % 101

print("Love compatibility:", percentage, "%")

if percentage >= 80:
    print("❤️ Perfect match! ❤️")
    elif percentage >= 60:
        print("💕 Very good compatibility!")
        elif percentage >= 40:
            print("😊 Good compatibility!")
            else:
                print("💔 You may need more")