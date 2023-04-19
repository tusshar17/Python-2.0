# String Formatting

# C style formatting

print("%d" % 432)
print("%d %d" % (432, 345))
print("%f" % 432.123)
print("%f" % 432.123456)
print("%f" % 432.12345651)
print("%f" % 432.12345641)
print("%s" % "HelloWorld")
print("%s %s" % ("Hello", "World"))
print("%d %s" % (432, "World"))
# print("%s %d" % (432, "World")) --> TypeError
print("%(nm)s %(ag)d" % {'ag': 432, 'nm': "HelloWorld"})


# using flags
print("%d" % 432)
print("% d" % 432)
print("%+d" % 432)
print("%8d" % 432)
print("%08d" % 432)
print("%f" % 432.123)
print("%.3f" % 432.123)
print("%.2f" % 432.123)
print("%.2f" % 432.128)
print("%9.2f" % 432.128)
print("%09.2f" % 432.128)
