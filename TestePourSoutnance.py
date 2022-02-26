import calcBase as cb

"""1. affectation, print fichier1.txt"""

# s = 'x=4;x=x+3;print(x);' 

"""2. affectation élargie, affectation  fichier2.txt"""

# s = 'x=9; x+=4; x++; print(x);'

"""3. while, for  fichier3.txt"""

# s = 'x=4;while(x<30){x=x+3;print(x);}; '
s = 'for(i=0 ;i<4 ;i=i+1){print(i*i);} ;'

"""4. fonctions void avec paramètres  fichier4.txt"""

# s = 'functionVoid toto(a,b){print(a+b);}; toto(3,5);'

"""5. fonctions value avec paramètres  fichier5.txt"""

# s = 'functionValue toto(a, b){c=a+b ;return c ;}; print(toto(3, 5)) ;'

"""6. fonctions value avec paramètres et return coupe circuit  fichier6.txt"""

# s ='functionValue toto(a, b){c=a+b ;return c ; print(666) ;}; x=toto(3, #5) ; print(x) ;'

"""8. 'functionValue value avec paramètres, return coupe circuit et scope des variables fichier7.txt'"""

# s = 'functionValue toto(a, b){if(a==0){ return b ;} c=toto(a-1, b-1) ;return c ; print(666) ;}; x=toto(3, 5) ; print(x) ;' 

cb.yacc.parse(s)