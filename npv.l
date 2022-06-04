/* Write a LEX program to find out whether given input is a noun, pronoun,verb. */

%{

%}

%%
[ |t ]+

man |
woman |
teacher |
table |
car |
money |
music |
dog |
monkey {printf("%s: is a noun\n", yytext);}

I |
he |
him |
you |
we |
her |
yours | 
theirs | 
someone |
me {printf("%s: is a pronoun\n", yytext);}

is |
am |
are |
were |
was |
be |
being |
been |
do |
does |
did |
will |
would |
should |
can |
could |
has |
have |
had |
go    {printf("%s: is a verb\n", yytext);}

[a-zA-Z]+ {printf("%s: is not  a verb\n", yytext);}
.|\n  {ECHO ;}
%%

int main()
{ yylex();
return 0;
}

int yywrap(){return(1);}