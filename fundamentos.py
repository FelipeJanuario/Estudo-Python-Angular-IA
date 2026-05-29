candidatos = [
    {"nome": "Ana", "Nível": "junior", "nota": 8.5},
    {"nome": "Bruno", "Nível": "pleno", "nota": 7.0},
    {"nome": "Carla", "Nível": "junior", "nota": 8.2},
]

aprovados = [c for c in candidatos if c["nota"] >= 8.0]

for c in aprovados:
    print(f'{c["nome"]} foi aprovada com nota {c["nota"]} e o seu nível é {c["Nível"]}')