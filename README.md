# Elevador Desafio

Este é um pequeno programa em Python que simula a chamada de um elevador e o transporte de um usuário entre andares.

## Descrição

O script `elevador.py` mantém o estado de dois elevadores e aceita a entrada do usuário para:

- Informar o andar atual do usuário
- Informar o andar de destino
- Escolher o elevador mais próximo do usuário
- Movimentar o elevador até o usuário e depois até o destino

O prédio possui os seguintes andares válidos:

-2, -1, 0, 1, 2, 3, 4

## Requisitos

- Python 3

## Como executar

No terminal, navegue até a pasta do projeto e execute:

```bash
python elevador.py
```

## Exemplo de uso

1. Informe o andar em que você está.
2. Informe o andar para onde deseja ir.
3. O programa mostrará qual elevador foi chamado e o trajeto realizado.

## Estrutura do projeto

- `elevador.py` - código principal do simulador de elevador
- `README.md` - documentação do projeto

## Observações

- O programa trata entradas inválidas e andares fora do intervalo definido.
- Se o usuário informar o mesmo andar de origem e destino, o programa exibirá uma mensagem apropriada.
