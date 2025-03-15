grammar Practica3;

// 📌 REGLA PRINCIPAL
query       : SELECT column_list FROM table (WHERE condition)? SEMI ;

// 📌 Definición de columnas y tabla
column_list : STAR | column (COMMA column)* ;
column      : IDENTIFIER ;
table       : IDENTIFIER ;

// 📌 Condición en WHERE
condition   : column operator value ;
operator    : GT | LT | EQ | GE | LE | NE ;
value       : NUMBER | STRING ;

// 📌 Estructura de control `for`
forStmt
    : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' (sentencia ';'?)* '}' # ForLoop
    ;

// Inicialización del `for` (Ej: i = 0)
inicializacion
    : ID '=' expresion 
    ;

// Condiciones dentro del `for` (Ej: i < 10)
condicion
    : ID op=('>' | '<' | '==' | '!=') INT  
    ;

// Actualización del `for` (Ej: i = i + 1)
actualizacion
    : ID '=' expresion 
    ;

// Asignaciones con `;`
asignacion
    : ID '=' expresion ';' 
    ;

// Expresiones matemáticas
expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;

// 📌 PALABRAS RESERVADAS
SELECT      : 'SELECT' ;
FROM        : 'FROM' ;
WHERE       : 'WHERE' ;
STAR        : '*' ;
COMMA       : ',' ;
SEMI        : ';' ;
GT          : '>' ;
LT          : '<' ;
EQ          : '=' ;
GE          : '>=' ;
LE          : '<=' ;
NE          : '!=' ;

// 📌 IDENTIFICADORES Y VALORES
ID          : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT         : [0-9]+ ;                   // Números enteros
NUMBER      : [0-9]+ ('.' [0-9]+)? ;     // Números con decimales
STRING      : '\'' (~('\'' | '\r' | '\n'))* '\'' ; // Cadenas de texto

// 📌 IGNORAR ESPACIOS Y SALTOS DE LÍNEA
WS          : [ \t\r\n]+ -> skip ;