 _____  ______          _____  __  __ ______ 
|  __ \|  ____|   /\   |  __ \|  \/  |  ____|
| |__) | |__     /  \  | |  | | \  / | |__   
|  _  /|  __|   / /\ \ | |  | | |\/| |  __|  
| | \ \| |____ / ____ \| |__| | |  | | |____ 
|_|  \_\______/_/    \_\_____/|_|  |_|______|

       +---------------------------------------------------+
       | Trabalho Prático 2 de Laboratório de Programação  |
       |     "Interpretador de expressões aritméticas"     |
       |      João Lucas Pires , up201606617@fc.up.pt      |
       |      Solange Perdigão , up201603610@fc.up.pt      |
       +---------------------------------------------------+


+---------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                 |
|	Este trabalho é constituido por um programa.                                               				                      |
|	O programa permite calcular expressões aritméticas, tais como soma, subtração, multiplicação, divisão e o resto de uma        |
| divisão.        														                                                          |
|                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------+

Para correr o programa:
-No terminal corremos o comando 'python3 main.py'
(ou 'python3' e dentro do terminal do python: 'from main import *')
('python main.py' retorna um erro e não corre o programa devido a diferenças entre python2 e python3.)
---------------------------------------------------------------------------------------------------------------------------------------------

Para calcular as expressões aritméticas, estas devem estar na forma prefixa.
 EX: (define x 5) ( + (* 2 x) 7)

Regras:
 - Definir uma variável:
	Ex: ( define x 3 )
 - Soma: 
	Ex: (+ 2 1 )
 - Subtração: 
	Ex: (- 10 2 )
 - Multiplicação: 
	Ex: ( * 4 3 )
 - Divisão: 
	Ex: ( / 4 2 )
 - Resto da divisão 
	Ex: (mod 10 3)


O programa retorna: 

 -Resultado: O resultado da expressão;
 -Expressão escrita na forma regular;
 -Tokenize: Divide a expressão numa lista de palavras;
 -Parse: Uma lista de tuplos de cada expressão;
 -Valores das variaveis no dicionário: O valor de cada variavel definida;

---------------------------------------------------------------------------------------------------------------------------------------------

Observações finais:

O programa foi desenvolvido e testado num PC com Ubuntu 17.10 x86/64.
Foi usado o Python 3.6.3 (GCC 7.2.0).
Fez-se um try...catch e alguns if's para apanhar excepções de forma a impedir que hajam erros ou excepções devido a maus inputs do utilizador.