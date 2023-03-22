# Manipulador de arquivo de envio (para B3) do sistema Swap

## Pré-requisitos
* Python instalado:

Abrir o CMD e executar:
```
c:>python --version
```
Se o python estiver instalado, aparecerá um texto como o abaixo:

```
Python 3.11.0
```

## Configurar o "Manipulador":

Para inserir novos valores, existe um arquivo de configuração chamado "CamposSwapAlterar.txt".
Este arquivo traz as seguintes informações, com base no layout da B3 de março de 2023:
* O número da ordem do campo
   * Ex.: 004
* A descrição do campo
   * Ex.: Participante que gerou o arquivo
* O tipo de campo: 
   * X - alphanumeric | 9 - numeric
* O tamanho do campo
   * Ex.: ( 20)
* Obrigatoriedade do preenchimento do campo no arquivo de envio:
   * (S ou N)
* A posição deste campo na linha do arquivo (primeira e última posição)
   * Ex.: 11      30
* Valor que deve ser inserido/substituído no arquivo de envio
   * Ex.: MATERABM

Cada informação está em uma posição especifica neste txt, por isso, caso seja necessário incluir algum valor ou alterar, as posições devem ser preservadas.

Exemplo de parte do arquivo:
```
Header
004 Participante que gerou o arquivo X ( 20) S 11      30      MATERABM  
005 Data                             9 (  8) S 31      38      Atual     
Linha 1
005 Parte                            9 (  8) S 21      28      00743006  
006 CPF CNPJ Cliente Parte           X ( 14) N 29      42                
008 Contraparte                      9 (  8) N 53      60      02039000  
009 CPF CNPJ Cliente Contraparte     X ( 14) N 61      74                
011 Data inicio                      9 (  8) S 85      92      Atual     
012 Data vencimento                  9 (  8) N 93      100     200   
```

* Legenda:
   * Header - Delimitação dos campos referentes ao Header do arquivo de envio.
   * Linha 1 - Delimitação dos campos referentes a linha de dados (segunda linha) do arquivo de envio.
   * MATERABM - Nome do Participante que deve ser inserido no Header, em substituição a informação que está no arquivo.
   * Atual - Informa ao Manipulador que deve ser inserida a data atual em substituição a data que está no arquivo.
   * 200 (ou outro valor de até 3 caracteres, como 20) - Informa ao Manipulador que deve ser inserida a data atual acrescida de 200 dias a frente, em substituição a data que está no arquivo. 
   * 00743006 - Conta da parte que deve ser inserida em substituição a conta que está no arquivo.
   * 02039000 - Conta da contraparte que deve ser inserida em substituição a conta que está no arquivo.
   * CPF - Informa ao Manipulador que deve ser inserido um CPF válido em substituição ao valor que está no arquivo. Este CPF é criado automaticamente e randomicamente pelo manipulador
   * 20230320 (ou qualque outra data) - Informa ao Manipulador que deve ser inserida esta data específica em substituição a data que está no arquivo.


## Como rodar o "Manipulador"?

* Baixar o projeto em arquivo ZIP, ou fazer um clone.
* Se baixou o ZIP, descompactar
* Cole na pasta do projeto (descompactado ou clonado) o arquivo gerado no sistema, para envio no B3.
* Renomeie o arquivo para TESTE.txt
* No CMD, na pasta do projeto, execute:

```
python .\Manipular.py
```
* Abra o novo arquivo gerado (NovoTeste1.txt), na pasta do projeto, para conferir
* Envie este novo arquivo no sistema B3.
