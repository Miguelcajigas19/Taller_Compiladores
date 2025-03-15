# Práctica 3: Implementación de una Estructura de Control `for`

## Objetivo
Extender la gramática para incluir estructuras de control `for`, permitiendo la ejecución repetitiva de sentencias basadas en un rango de valores y analizando su estructura mediante tokens y árboles de análisis sintáctico.

## Comandos Utilizados
1. Generar el analizador léxico y sintáctico:
   ```bash
   antlr4 Practica3.g4
   javac -cp .:$ANTLR_JAR Practica3*.java

Generar tokens para la estructura for:
echo "for (i = 0; i < 10; i = i + 1) { x = x + i; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Practica3 query -tokens

[@0,0:2='for',<'for'>,1:0]
[@1,4:4='(',<'('>,1:4]
[@2,5:5='i',<ID>,1:5]
[@3,7:7='=',<'='>,1:7]
[@4,9:9='0',<INT>,1:9]
[@5,10:10=';',<';'>,1:10]
[@6,12:12='i',<ID>,1:12]
[@7,14:14='<',<'<'>,1:14]
[@8,16:17='10',<INT>,1:16]
[@9,18:18=';',<';'>,1:18]
[@10,20:20='i',<ID>,1:20]
[@11,22:22='=',<'='>,1:22]
[@12,24:24='i',<ID>,1:24]
[@13,26:26='+',<'+'>,1:26]
[@14,28:28='1',<INT>,1:28]
[@15,29:29=')',<')'>,1:29]
[@16,31:31='{',<'{'>,1:31]
[@17,33:33='x',<ID>,1:33]
[@18,35:35='=',<'='>,1:35]
[@19,37:37='x',<ID>,1:37]
[@20,39:39='+',<'+'>,1:39]
[@21,41:41='i',<ID>,1:41]
[@22,42:42=';',<';'>,1:42]
[@23,44:44='}',<'}'>,1:44]
[@24,46:45='<EOF>',<EOF>,1:46]

Árbol de Análisis Sintáctico

echo "for (i = 0; i < 10; i = i + 1) { x = x + i; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Practica3 query -tree

(query (forStmt for ( (inicializacion i = (expresion 0)) ; (condicion i < 10) ; (actualizacion i = (expresion (expresion i) + (expresion 1)) ) { (sentencia (asignacion x = (expresion (expresion x) + (expresion i)) ;) }) <EOF>)



1. ¿Qué tokens se generan para la estructura for (i = 0; i < 10; i = i + 1) { x = x + i; }?
Respuesta correcta: a) FOR, (, ID, =, INT, ;, ID, <, INT, ;, ID, =, ID, +, INT, ), {, ID, =, ID, +, ID, }

Justificación:
Los tokens generados para la estructura for son:

FOR: Palabra clave reservada.

( y ): Paréntesis que delimitan el encabezado del for.

ID: Identificadores (i, x).

=, <, +: Operadores.

INT: Números enteros (0, 10, 1).

;: Delimitador de expresiones dentro del for.

{ y }: Llaves que delimitan el cuerpo del for.

2. ¿Cómo se organiza la estructura for en el árbol de análisis sintáctico?
Respuesta correcta: a) for es el nodo raíz y sus componentes (inicialización, condición, actualización y cuerpo) son nodos secundarios.

Justificación:
En el árbol sintáctico, la estructura for se organiza de la siguiente manera:

El nodo raíz es forStmt.

Los nodos secundarios son:

inicializacion: Inicialización del bucle (i = 0).

condicion: Condición del bucle (i < 10).

actualizacion: Actualización del bucle (i = i + 1).

Cuerpo del for: Asignación x = x + i;.

3. ¿Qué ocurre si en la gramática se omiten los ; en la estructura for?
Respuesta correcta: a) Se genera un error de sintaxis.

Justificación:
Los ; son obligatorios en la gramática para separar las tres partes del encabezado del for (inicialización, condición y actualización). Si se omiten, el analizador sintáctico no podrá reconocer la estructura correctamente y generará un error de sintaxis.

Marlon Ruiz
Miguel Cajigas