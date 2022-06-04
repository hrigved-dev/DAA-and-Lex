/* Write a LEX program to find out whether given input is a adverb, adjective or
preposition. */

%{

%}

%%
[ |t ]+

slowly |
rapidly |
clumsily |
badly |
diligently |
sweetly |
warmly |
sadly {printf("%s: is an adverb\n", yytext);}

charming |
cruel |
fantastic |
gentle |
huge |
perfect |
rough |
sharp {printf("%s: is an adjective\n", yytext);}

in |
on |
inside |
over |
around |
at |
by |
within |
of |
among {printf("%s: is a preposition\n", yytext);}

[a-zA-Z]+ {printf("%s: is not among adverb, adjective or preposition\n", yytext);}
.|\n {ECHO ;}
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return(1);
}