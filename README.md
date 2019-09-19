# ConversorCSV
Este é um simples conversor escrito em Python, para um arquivo .txt que é gerado a partir do Datalogger de um medidor de vazão ULTRAFLOW da empresa Tricomex

O objetivo deste conversor é tratar o arquivo de log que é gravado de forma estruturada, transformando o mesmo em um arquivo CSV (comma-separated values), um formato mais versátil, que pode ser utilizado posteriormente por bibliotecas de manipulação e visualização de dados como Pandas, NumPy, Plotly, etc. ou para a edição do mesmo em um programa de planilhas, como o Excel

<h2>Funcionamento</h2>
  O arquivo gerado pelo logger possui uma estrutura definida, com cada valor de leitura possuindo uma série de valores, que muitas vezes não são interessantes para uma correta visualização dos dados<br>
  Estrutura padrão de leitura:
<pre>
    <code>
    19-08-17 10:30:00\n
    SYS:*R\n
    Flow  11809   l/h *R
    NET  +779656x1 L
    UP:77.5,DN:77.7,Q=87
    FLOW: 11809.7  l/h
    VEL: 1.46043 m/s
    </code>
</pre>

Este bloco de informações é então filtrado, mantendo apenas os campos de interesse, separando data e hora em dois valores diferentes e formatando a data para o padrão brasileiro DD/MM/AAAA, opção esta que o datalogger não permite modificar

Estrutura desejada para cada valor de leitura, mantendo os campos Data,Hora,Vazao,Totalizador:
<pre>
  <code>  
09/08/19,10:30:00,11748,842281
   </code>
</pre>

<h2>Uso</h2>
  <p>O conversor pode ser executado na linha de comandos a partir do comando <code>python conversor.py</code><br> 
  O nome do arquivo de entrada (que deve estar no mesmo diretório) então é solicitado para o usuário e o script se encarrega do restante, gerando um arquivo chamado resultado.csv
    
  Este repositório possui um arquivo chamado PRINT.txt que foi gerado a partir de um dos medidores de vazão e que pode ser utilizado para testes
  </p>
  
