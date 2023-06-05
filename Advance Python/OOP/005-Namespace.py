# Namespace


class Mobile:
    fp = "Yes"


realme = Mobile()
samsung = Mobile()
apple = Mobile()

#
print("Initially Without Any Modifications:")
print("For Class:", Mobile.fp)
print("For realme:", realme.fp)
print("For samsung:", samsung.fp)
print("For apple:", apple.fp)

print()

#
print("Modifying clas variable using class:")
Mobile.fp = "No"
print("For Class:", Mobile.fp)
print("For realme:", realme.fp)
print("For samsung:", samsung.fp)
print("For apple:", apple.fp)

print()

#
print("Modifying clas variable using an instance:")
samsung.fp = "Issue"
print("For Class:", Mobile.fp)
print("For realme:", realme.fp)
print("For samsung:", samsung.fp)
print("For apple:", apple.fp)
