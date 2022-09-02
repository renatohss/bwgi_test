# bwgi_test
Scripts for solving the problems proposed by BGWI interviewers

# last_lines 
Escreva uma função, last_lines, que devolva as linhas de um dado 
arquivo de texto em ordem inversa. Caso esteja familiarizado com a 
linha de comando Unix, sua função deve fazer o mesmo que o 
comando `tac`. 

Note que last_lines deve incluir o caractere terminador de linha 
(suponha \n) para cada linha. Sua função deverá devolver um iterator. 

Sua função deve ler o arquivo fornecido em pedaços não maiores que o 
tamanho dado por um argumento da função, cujo valor padrão deve ser 
`io.DEFAULT_BUFFER_SIZE`. Dito de outro modo, last_lines não deve 
ler mais do que um certo número de bytes (número esse dado por um 
argumento facultativo) de cada vez. 
Suponha ainda que o arquivo fornecido possa estar codificado em 
UTF-8, de modo a conter qualquer caractere Unicode válido. 
Isso significa que, ao ler e decodificar texto do arquivo, deve se 
certificar de não decodificar um trecho que contenha um caractere 
pela metade. 

