# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("1 Hello ", name,"!")	# with a comma
print("2 Hello " + name +"!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("3 Hello", name )	# with a comma
print( "4 Hello" + name )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "5 I love to eat {food1} and {food2}".format(food1 = fave_food1, food2 = fave_food2) ) # with .format()
print( f"6 I love to eat {fave_food1} and {fave_food2}." ) # with an f string