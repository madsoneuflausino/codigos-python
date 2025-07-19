larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem {larg}m de largura e {alt}m de altura\nA área da parede é {area}m²\nVocê precisa de {tinta:.1f}l de tinta para pintar sua parede.')