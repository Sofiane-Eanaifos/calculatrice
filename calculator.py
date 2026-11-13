print(" Bienvenue  !!")
x=input("Quelle opération voulez-vous faire : somme , soustraction ,division, multiplication ?: ")
print(" Vous avez choisi ", x ," comme opération  maintenant entrer deux nombres dans l'ordre que vous souhaitez.")
y=int(input("Entrer un premier nombre :"))
z=int(input("Entrer un deuxieme nombre :"))
if x=="somme":
    s=y+z
    print("la",x,"des deux nombres",y,"et",z,"est égale a ",s)
elif x=="soustraction":
    s=y-z
    print("la", x, "des deux nombres", y, "et", z, "est égale a ", s)
elif x=="division":
    d=y/z
    print("la", x, "des deux nombres", y, "par", z, "est égale a ", d)
elif x=="multiplication":
    m=y*z
    print("la", x, "entre les  deux nombres", y, "et", z, "est égale a ", m)




