import calcBase as cb

# s = input('calc > ')

# s = 'a=1+3;print(a);'
# s = 'print(1+2);a=2;print(a);'
# s='print(1+2);x=4;x=x+1;print(x);'

#s = 'x=1;print(x);'
#s = 'x=1;x=x+1;x=x+1;print(x);'

# s = 'for(x=0;x<11;x=x+1;){print(x);};'
# s = 'for(i=0; i<10; i=i+1){print(i);};'

#s = 'x=2;while(x<5){x=x+1;print(x);};'
#s = 'while(5){print(1);};'
# s = 'x=5;while(x<8){print(2+9);};'

#s = 'if(2<4){print(2*3);print(3);};'
# s = 'if(2<0){print("x");} else{ print("a");};'

# s = 'functionVoid carre(){print(2+1);};for(i=0;i<10;i=i+1){carre();};'

# s = 'functionVoid carre(a,b){a=1;b=2;print(a+b);};carre(2,1);'

# s = 'functionVoid carre(a,b){print(a*b);};for(i=0;i<5;i=i+1){print(i);carre(i,i);};print(1+2,"toto", 3+4);if(2<0){print("x");} else{ print("y");};'


# s = 'functionValue cinq(){a=2;b=3;return a+b;};print(cinq());'

# s = 'functionValue carre(a,b){return a+b;};print(carre(2,1));'

s = 'functionValue carre(toto,titi){return 2*(toto*titi);};print(carre(2,2));'

# s = 'functionValue carre(a){return a*a;};print(carre(2));'

# s = 'a=1;b=2;c=a+5;print(c);'

cb.yacc.parse(s)