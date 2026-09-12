#######################
#Title: Cupcake Recipe Scaler
#Purpose: Scales the recipe up or down depending on user input
#Author: Asha
#Date: 23/02/26
#######################


#store choclate cupcake recipe (in grams, except for the egg)

#cake ingredients
c_flour = 125
c_sugar = 200
c_cocoapowder = 42
c_bakingsoda = 4
c_bakingpowder = 2
c_salt = 3
c_oil = 80
c_egg = 1
c_buttermilk = 120
c_coffee = 120

#frosting ingredients
c_butter = 115
c_cocoa_powder = 40
c_powderedsugar = 240
c_milk = 45

#store vanilla cupcake recipe (in grams, except for eggs)

#cake ingredients
v_flour = 165
v_bakingpowder = 5
v_salt = 3
v_butter = 115
v_sugar = 200
v_egg = 2
v_vanilla = 10
v_yogurt = 120
v_milk = 120

#frosting ingredients
vbutter = 300
v_powderedsugar = 300
vanilla = 10
vmilk = 45


#introduction to the program
print("Welcome to the Cupcake Calculator! Choose one of our cupcake recipes and get it automatically scaled, up or down, based on the amount you need!")

#input the flavour that the user wants to bake
flavour = input("\nDo you want to make chocolate(press c) or vanilla(press v) cupcakes? ")


#print cupcake recipe based on what flavour the user wants to bake

#if user selected chocolate print the chocolate cupcake recipe
if flavour == "c":
    print("Here are the ingredients, measured in grams, needed to make chocolate cupcakes:")
    print("Cake:\n125g flour \n200g sugar \n42g cocoa powder \n4g baking soda\n2g baking powder \n3g salt \n80g oil\n1 egg\n120g buttermilk \n120g brewed coffee")
    print("\nFrosting:\n115g butter\n40g cocoa powder\n240g powdered sugar\n45g milk")
    print("\nThis recipe yields 12 cupcakes.")
    
#if user selected vanilla print the vanilla cupcake recipe
elif flavour == "v":
    print("Here are the ingredients, measured in grams, needed to make vanilla cupcakes:")
    print("Cake:\n165g flour\n5g baking powder\n3g salt\n115g butter\n200g sugar\n2 eggs\n10g vanilla\n120g yogurt\n120g milk")
    print("\nFrosting:\n300g butter\n300g powdered sugar\n10g vanilla \n45g milk")
    print("\nThis recipe yields 12 cupcakes.")

    
#input whether user needs to scale recipe up or down
servings = int(input("\n\nDo you need to scale this recipe up or down? If so, enter the amount you want. If not, enter '0': "))
if servings == 0:
    print("Enjoy your cupcakes!")
    

#calculate adjusted recipe based on user's desired amount of servings
if servings > 0:
    scale = servings/12
    
#chocolate cupcake recipe calculations

    if flavour == "c":
        #cake ingredient calculations
        c_flour = round(c_flour * scale)
        c_sugar = round(c_sugar*scale)
        c_cocoapowder = round(c_cocoapowder*scale)
        c_bakingsoda = round(c_bakingsoda*scale)
        c_bakingpowder = round(c_bakingpowder*scale)
        c_salt = round(c_salt*scale)
        c_oil = round(c_oil*scale)
        c_egg = round(c_egg*scale,2)
        c_buttermilk = round(c_buttermilk*scale)
        c_coffee = round(c_coffee*scale)
        
        #frosting ingredient calculations
        c_butter = round(c_butter*scale)
        c_cocoa_powder = round(c_cocoa_powder*scale)
        c_powderedsugar = round(c_powderedsugar*scale)
        c_milk = round(c_milk*scale)
    
#vanilla cupcake recipe calculations

    elif flavour == "v":
        #cake ingredient calculations
        v_flour = round(v_flour*scale)
        v_bakingpowder = round(v_bakingpowder*scale)
        v_salt = round(v_salt*scale)
        v_butter = round(v_butter*scale)
        v_sugar = round(v_sugar*scale)
        v_egg = round(v_egg*scale, 2)
        v_vanilla = round(v_vanilla*scale)
        v_yogurt = round(v_yogurt*scale)
        v_milk = round(v_milk*scale)
        
        #frosting ingredient calculations
        vbutter = round(vbutter*scale)
        v_powderedsugar = round(v_powderedsugar*scale)
        vanilla = round(vanilla*scale)
        vmilk = round(vmilk*scale)
    
    
    
    #print adjusted recipes

    #if user selected chocolate, print adjusted chocolate cupcake recipe
    if flavour == "c":
        print("\n\n\nHere is your adjusted chocolate cupcake recipe:")
        print("Cake:\n",c_flour,"g flour\n",c_sugar,"g sugar\n",c_cocoapowder,"g cocoa powder")
        print("",c_bakingsoda,"g baking soda\n", c_bakingpowder,"g baking soda\n",c_salt,"g salt")
        print("",c_oil,"g oil\n",c_egg,"eggs\n",c_buttermilk,"g buttermilk\n", c_coffee,"g brewed coffee") 
        print("\nFrosting:\n",c_butter,"g butter\n",c_cocoa_powder,"g cocoa powder\n",c_powderedsugar,"g powdered sugar\n",c_milk,"g milk")
        print("\nThis recipe has been adjusted to yield", servings,"cupcakes.")

    #if user selected vanilla, print adjusted vanilla cupcake recipe
    elif flavour == "v":
        print("\n\n\nHere is your adjusted vanilla cupcake recipe:")
        print("Cake:\n",v_flour,"g flour\n",v_bakingpowder,"g baking powder\n",v_salt,"g salt")
        print("", v_butter,"g butter\n", v_sugar,"g sugar\n",v_egg,"eggs")
        print("",v_vanilla,"g vanilla extract\n",v_yogurt,"g yogurt\n",v_milk,"g milk") 
        print("\nFrosting:\n",vbutter,"g butter\n",v_powderedsugar,"g powdered sugar\n",vanilla,"g vanilla\n",vmilk,"g milk")
        print("\nThis recipe has been adjusted to yield", servings,"cupcakes.")
