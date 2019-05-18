one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7
thousand = 8
andd = 3

#stevilo crk je:

rezultat_do_100 = (one + two + three + four + five + six + seven + eight + nine) * 9 +\
    ten + eleven + twelve + thirteen + fourteen + fifteen + sixteen + seventeen + eighteen + nineteen +\
        (twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety) * 10

rezultat_do_1000 = (one + two + three + four + five + six + seven + eight + nine) * 100 + andd * 99 * 9 +\
    one + thousand + rezultat_do_100 * 10 + hundred * (999 - 99)


print(rezultat_do_1000)