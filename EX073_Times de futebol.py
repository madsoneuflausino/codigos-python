classificação = ('Palmeiras', 'Grêmio', 'Atletico Mineiro',
                 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
                 'Athletico Paranaense', 'Internacional', 'Fortaleza',
                 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
                 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América Mineiro')
print(f'\033[032mOs 5 primeiros colocados foram:\033[m{classificação[0:5]}')
print(f'\033[032mOs 4 últimos colocados foram:\033[m{classificação[-4:]}')
print(f'\033[032mTimes em ordem alfabética:\033[m {sorted(classificação)}')
print(f'\033[031mO Bahia ficou na\033[m {classificação.index("Bahia") + 1}ª colocação.')