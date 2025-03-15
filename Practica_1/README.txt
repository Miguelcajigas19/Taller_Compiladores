1. ¿Cómo se representan los operadores +, -, * y / en los tokens generados?
Respuesta correcta: b) Como operadores aritméticos específicos

Justificación:
En ANTLR, los operadores aritméticos (+, -, *, /) se representan como tokens específicos en la gramática. Estos tokens no son identificadores ni palabras clave reservadas, sino símbolos que representan operaciones aritméticas. Por ejemplo, en la gramática proporcionada, estos operadores se utilizan en la regla expresion para definir operaciones matemáticas:

antlr
Copy
expresion
    : expresion op=('*'|'/') expresion     # MulDiv
    | expresion op=('+'|'-') expresion     # AddSub
    | INT                                  # Int
    | ID                                   # Variable
    | '(' expresion ')'                    # Parens
    ;
Aquí, *, /, + y - son tokens que representan operadores aritméticos.

2. ¿Qué estructura sigue el árbol de análisis sintáctico generado por ANTLR4 para la expresión b = 5 + a * 2;?
Respuesta correcta: d) * se evalúa antes que +, organizando el árbol en función de la precedencia.

Justificación:
ANTLR genera un árbol de análisis sintáctico (parse tree) que respeta la precedencia de operadores definida en la gramática. En la expresión b = 5 + a * 2;, el operador * tiene mayor precedencia que +, por lo que el árbol sintáctico refleja esta jerarquía. El árbol se organiza de la siguiente manera:

El nodo raíz es la asignación b = ....

La expresión 5 + a * 2 se divide en subárboles:

a * 2 se evalúa primero debido a la mayor precedencia de *.

Luego, el resultado de a * 2 se suma a 5.

El árbol sintáctico generado por ANTLR para esta expresión sería similar a:


(asignacion b = (expresion (expresion 5) + (expresion (expresion a) * (expresion 2))))

Esto muestra claramente que * se evalúa antes que +, respetando la precedencia de operadores.

3. ¿Por qué es importante visualizar los tokens y el árbol de análisis en el proceso de compilación?
Respuesta correcta: d) Todas las anteriores.

Justificación:
Visualizar los tokens y el árbol de análisis sintáctico es crucial en el proceso de compilación por las siguientes razones:

a) Para entender cómo el compilador traduce las instrucciones:
Los tokens y el árbol sintáctico permiten ver cómo el compilador descompone y analiza el código fuente, lo que ayuda a comprender el proceso de traducción.

b) Para optimizar el código generado:
Al visualizar el árbol sintáctico, se pueden identificar oportunidades para optimizar el código, como eliminar redundancias o reordenar operaciones.

c) Para verificar que la gramática está bien definida:
La visualización de tokens y el árbol sintáctico ayuda a detectar errores en la gramática, como reglas mal definidas o ambigüedades.

Por lo tanto, todas las opciones son correctas y justifican la importancia de visualizar tokens y el árbol de análisis.

Comandos Utilizados Durante el Desarrollo de la Práctica
Generar el analizador léxico y sintáctico con ANTLR:


antlr4 Practica.g4
Este comando genera los archivos Java necesarios para el analizador léxico (PracticaLexer) y sintáctico (PracticaParser).

Compilar los archivos generados por ANTLR:


javac -cp .:$ANTLR_JAR Practica*.java
Este comando compila los archivos .java generados por ANTLR.

Ejecutar el analizador léxico y sintáctico:


echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Practica programa -tokens
Este comando muestra los tokens generados para la entrada proporcionada.

Visualizar el árbol de análisis sintáctico:


echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Practica programa -tree
Este comando muestra el árbol de análisis sintáctico para la entrada proporcionada.

Resultados Obtenidos en Pantalla
Tokens Generados
Al ejecutar el comando para visualizar los tokens, se obtiene una salida similar a la siguiente:


[@0,0:0='a',<ID>,1:0]
[@1,2:2='=',<'='>,1:2]
[@2,4:5='10',<INT>,1:4]
[@3,6:6=';',<';'>,1:6]
[@4,8:8='b',<ID>,1:8]
[@5,10:10='=',<'='>,1:10]
[@6,12:12='5',<INT>,1:12]
[@7,14:14='+',<'+'>,1:14]
[@8,16:16='a',<ID>,1:16]
[@9,18:18='*',<'*'>,1:18]
[@10,20:20='2',<INT>,1:20]
[@11,21:21=';',<';'>,1:21]
[@12,23:23='c',<ID>,1:23]
[@13,25:25='=',<'='>,1:25]
[@14,27:27='(',<'('>,1:27]
[@15,28:28='b',<ID>,1:28]
[@16,30:30='-',<'-'>,1:30]
[@17,32:32='3',<INT>,1:32]
[@18,33:33=')',<')'>,1:33]
[@19,35:35='/',<'/'>,1:35]
[@20,37:37='2',<INT>,1:37]
[@21,38:38=';',<';'>,1:38]
[@22,40:39='<EOF>',<EOF>,1:40]
Árbol de Análisis Sintáctico
Al ejecutar el comando para visualizar el árbol sintáctico, se obtiene una salida similar a la siguiente:


(programa (sentencia (asignacion a = (expresion 10) ;) (sentencia (asignacion b = (expresion (expresion 5) + (expresion (expresion a) * (expresion 2)) ;) (sentencia (asignacion c = (expresion (expresion (expresion (expresion b) - (expresion 3))) / (expresion 2)) ;) <EOF>)
Conclusión
Los comandos utilizados permiten generar y visualizar los tokens y el árbol sintáctico.

Marlon Ruiz
Miguel Cajigas