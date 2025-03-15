# Práctica 2: Implementación de una Estructura de Control `while`

## Objetivo
Extender la gramática para incluir estructuras de control `while`, permitiendo la ejecución repetitiva de sentencias basadas en una condición y analizando su estructura mediante tokens y árboles de análisis sintáctico.

## Comandos Utilizados
1. Generar el analizador léxico y sintáctico:
   ```bash
   antlr4 Practica2.g4
   javac -cp .:$ANTLR_JAR Practica2*.java

Generar tokens para la estructura while:
echo "x = 0; while (x < 5) { x = x + 1; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tokens

Generar el árbol de análisis sintáctico:
echo "x = 0; while (x < 5) { x = x + 1; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig MiGramatica programa -tree

Tokens Generados
[@0,0:0='x',<ID>,1:0]
[@1,2:2='=',<'='>,1:2]
[@2,4:4='0',<INT>,1:4]
[@3,5:5=';',<';'>,1:5]
[@4,7:11='while',<'while'>,1:7]
[@5,13:13='(',<'('>,1:13]
[@6,14:14='x',<ID>,1:14]
[@7,16:16='<',<'<'>,1:16]
[@8,18:18='5',<INT>,1:18]
[@9,19:19=')',<')'>,1:19]
[@10,21:21='{',<'{'>,1:21]
[@11,23:23='x',<ID>,1:23]
[@12,25:25='=',<'='>,1:25]
[@13,27:27='x',<ID>,1:27]
[@14,29:29='+',<'+'>,1:29]
[@15,31:31='1',<INT>,1:31]
[@16,32:32=';',<';'>,1:32]
[@17,34:34='}',<'}'>,1:34]
[@18,36:35='<EOF>',<EOF>,1:36]

Árbol de Análisis Sintáctico

(programa (sentencia (asignacion x = (expresion 0) ;) (sentencia (whileStmt while ( (condicion x < 5) ) { (sentencia (asignacion x = (expresion (expresion x) + (expresion 1)) ;) })) <EOF>)
Cuestionario
¿Qué tokens se generan para la estructura while (x < 5) { x = x + 1; }?
Respuesta: a) WHILE, (, ID, <, INT, ), {, ID, =, ID, +, INT, }

¿Cómo se organiza la estructura while en el árbol de análisis sintáctico?
Respuesta: c) while es el nodo raíz y su condición y cuerpo son nodos secundarios.

¿Qué ocurre si en la gramática se omiten las llaves {} en la estructura while?
Respuesta: b) Se genera un error de sintaxis.

Marlon Ruiz 
Miguel Cajigas



