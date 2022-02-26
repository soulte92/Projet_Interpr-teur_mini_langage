import calcBase as cb

# s = input('calc > ')

""" Simple with print and affect intructions """
# s = 'a=1+3;print(a);'
# s = 'print(1+2);a=2;print(a);'
# s='print(1+2);x=4;x=x+1;print(x);'

#s = 'x=1;print(x);'
#s = 'x=1;x=x+1;x=x+1;print(x);'

""" for instruction """
# s = 'for(x=0;x<11;x=x+1;){print(x);};'
# s = 'for(i=0; i<10; i=i+1){print(i);};'

""" while instruction """
#s = 'x=2;while(x<5){x=x+1;print(x);};'
#s = 'while(5){print(1);};'
# s = 'x=5;while(x<8){print(2+9);};'

""" if and if else instruction """
#s = 'if(2<4){print(2*3);print(3);};'
# s = 'if(2<0){print("x");} else{ print("a");};'

""" Functions without return """
# s = 'functionVoid carre(){print(2+1);return;};for(i=0;i<10;i=i+1){carre();};'

# s = 'functionVoid carre(a,b){a=1;b=2;print(a+b);};carre(2,1);'

# s = 'functionVoid carre(a,b){print(a*b);};for(i=0;i<5;i=i+1){print(i);carre(i,i);};print(1+2,"toto", 3+4);if(2<0){print("x");} else{ print("y");};'

""" Functions with return """
# s = 'functionValue cinq(){a=1;a=a+1;b=3;c=a+b;return c;};print(cinq());'

# s = 'functionValue carre(a,b){return a+b;};print(carre(2,1));'

s = 'functionValue carre(toto,titi){return toto*titi;};a=carre(2,4);print(a);'

# s = 'functionValue cinq(){a=2;b=3;return a+b;};a = cinq();print(a);'

# s = 'functionValue carre(a){return a*a;print(1);};print(carre(2));'

# s = 'functionValueImp c(a){c=a*a;print(3);};print(c(2));'

# s = 'functionValueImp carre(toto,titi){carre=3*(toto*titi);};a=carre(2,4);print(a);'


# s = 'a=2;print(2);'

# s = 'functionVoid f(a){print(a+1);return;};functionValue c(a){ f(a*2);return a+1;};print(c(2));'
# s = 'functionValue g(a){a=6+1;print(a);};g(2);'
# s = 'Main(){x=2 ;print(g(x)) ;}'

# s= 'functionValue c(a){a=a+1;return a+1;};result=c(2);print(result);'

# s= 'functionValue fiboRec(n){if(n==0 | n==1){return n;}else{return fiboRec(n-1)+fiboRec(n-2);}};result=fiboRec(9);print(result);'

# s = 'functionValue carre(a){a=a+1; return a;};print(carre(1));'
# s = 'functionValue cinq(a){b=3;return b;};'
# s = 'fonctionValue toto(a, b){if(a==0) return b ; c=toto(a-1, b-#1) ;return c ; print(666) ;} x=toto(3, 5) ; print(x) ;’ 


cb.yacc.parse(s)