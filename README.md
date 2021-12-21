# GeraTxtRioCard
Script em python, utilizando PySimpleGUI, para a geração de arquivo txt a ser importado no sistema de Bilhetagem Eletrônica da RioCard, no Estado do Rio de Janeiro.

As regras para a geração do arquivo txt se encontram no capítulo 2 do documento "PEF-V14-Ver1.6.0_-_Layouts_dos_arquivos_de_importacao_de_usuarios_e_pedidos", encontrado em https://www.cartaoriocard.com.br/rcc/paraEmpresa/downloads na seção Layouts dos Arquivos de importação.

O módulo PySimpleGUI permite a interface gráfica, que recebe os seguintes dados (digitados ou usando CTRL + C/ CTRL + V):

&emsp; Matrículas: à esquerda <br>
&emsp; Totais    : à direita <br>
&emsp; Nome do Arquivo TXT a ser gerado e importado no site da RioCard <br>
&emsp; Caminho do Arquivo TXT, onde será gravado
<br>
<br>

![image](https://user-images.githubusercontent.com/76176469/142970752-c7c29800-7bf3-4d0f-88ea-3378c9b7e9e6.png)
