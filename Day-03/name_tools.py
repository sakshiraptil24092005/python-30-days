name =input("enter your full name :").strip()
print("uppercase:",name.upper())
print("lowercase:",name.lower())
print("titlecase:",name.title())
print("reversed:",name[::-1])
divide = name.split()
initials=""
for part in divide:
    initials=initials + part[0].upper() + "."
print("initials:",initials)
