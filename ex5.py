my_name = "Marco Machado"
my_age = 29 #number
my_height = 70 #kg
my_weight = 185 #cm
my_eyes = 'brown'
my_teeth = 'white'
my_hair = "brown"

print "Let's talk about %s." %my_name
print "He's %d inches tall" %my_height
print "He's %d pounds heavy" %my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" %my_teeth

#this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age+my_height+my_weight)