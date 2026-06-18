andares_validos = [-2, -1, 0, 1, 2, 3, 4]

elevadores = [
    {"nome": "Elevador A", "andar": 0},
    {"nome": "Elevador B", "andar": 4},
]


def ler_numero(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        return None


def andar_valido(andar):
    return andar in andares_validos


def escolher_elevador(andar_usuario):
    elevador_escolhido = elevadores[0]
    menor_distancia = abs(elevador_escolhido["andar"] - andar_usuario)

    for elevador in elevadores[1:]:
        distancia = abs(elevador["andar"] - andar_usuario)
        if distancia < menor_distancia:
            elevador_escolhido = elevador
            menor_distancia = distancia

    return elevador_escolhido


def mover_ate(elevador, andar_destino):
    while elevador["andar"] < andar_destino:
        elevador["andar"] += 1
        print(f"{elevador['nome']} passando pelo andar {elevador['andar']}.")

    while elevador["andar"] > andar_destino:
        elevador["andar"] -= 1
        print(f"{elevador['nome']} passando pelo andar {elevador['andar']}.")


andar_usuario = ler_numero("Em qual andar você está? ")
if andar_usuario is None:
    print("Entrada inválida.")
elif not andar_valido(andar_usuario):
    print("Esse andar não existe.")
else:
    andar_destino = ler_numero("Para qual andar você quer ir? ")
    if andar_destino is None:
        print("Entrada inválida.")
    elif not andar_valido(andar_destino):
        print("Esse andar não existe.")
    elif andar_usuario == andar_destino:
        print("Você já está nesse andar.")
    else:
        elevador = escolher_elevador(andar_usuario)
        print(f"\n{elevador['nome']} está no andar {elevador['andar']}.")
        print(f"{elevador['nome']} foi chamado para o andar {andar_usuario}.")
        print(f"Distância até o usuário: {abs(elevador['andar'] - andar_usuario)}")

        print(f"\n{elevador['nome']} indo até o andar do usuário...")
        mover_ate(elevador, andar_usuario)

        print(f"Usuário entrou no {elevador['nome']}.")
        print(f"{elevador['nome']} indo para o andar {andar_destino}...")
        mover_ate(elevador, andar_destino)

        print(f"\nChegou ao andar {elevador['andar']}.")
        print(f"Nova posição de {elevador['nome']}: andar {elevador['andar']}")