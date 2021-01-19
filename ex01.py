#agência de carros
chevrolet = {'modelo' : 'camaro 2020',
'preço': 'R$ 381 mil', 
'velocidade_max' : '250km/h'
}
mercedes = {'modelo' : 'Mercedes class G',
'preço' : 'R$ 1,41milhões', 
'velocidade_max': '220 km/h'
}
audi = {'modelo': 'audio A6',
'preço': 'R$ 479 mil', 
'velocidade_max': '250km/h' 
}
ferrari = {'modelo':'Ferrari 481',
'preço': 'R$ 2,8 milhões',
'velocidade_max' : '330km/h',
}
hyundai = {'modelo': 'Tucson',
'preço' : 'R$ 152 mil',
'velocidade_max': '200km/h'
}
print('--'*60)
desejo = 'sim'
while desejo == 'sim':
    info = input("Deseja comprar um carro de que marca? ")
    if info == 'ferrari':
        pergunta = (input("Quais informações você busca? Temos: modelo, velocidade máxima ou preço. :"))
        if pergunta == 'modelo':
            print("Modelo disponível: {}".format(ferrari['modelo']))
        elif pergunta == 'preço':
            print("Preço da Ferrari que temos disponível: {}".format(ferrari['preço']))
        elif pergunta == 'velocidade maxima':
            print("A velocidade máxima da Ferrari é {}".format(ferrari['velocidade_max']))
    if info == 'chevrolet':
        pergunta = (input("Quais informações você busca? Temos: modelo, velocidade máxima ou preço. :"))    
        if pergunta == 'modelo':
            print("O modelo da Chevrolet que tem disponível é o {}".format(chevrolet['modelo']))
        elif pergunta == 'preço':
            print(print("Preço do Camaro que temos disponível: {}".format(chevrolet['preço'])))
        elif pergunta == 'velocidade maxima':
            print("A velocidade máxima do Camaro é {}".format(chevrolet['velocidade_max'])) 
    if info == 'hyundai':
        pergunta = (input("Quais informações você busca? Temos: modelo, velocidade máxima ou preço. :"))
        if pergunta == 'modelo':
             print("O modelo da Hyndai que tem disponível é o {}".format(hyundai['modelo']))
        elif pergunta == 'preço':
            print(print("Preço da Tucson que temos disponível: {}".format(hyundai['preço'])))  
        elif pergunta == 'velocidade maxima':
            print("A velocidade máxima da Tucson é {}".format(hyundai['preço']))
    if info == 'mercedes':
        pergunta = (input("Quais informações você busca? Temos: modelo, velocidade máxima ou preço. :"))
        if pergunta == 'modelo':
            print("O modelo da Mercedes que tem disponível é o {}".format(mercedes['modelo']))
        elif pergunta == 'preço':
            print(print("Preço da Mercedes que temos disponível: {}".format(mercedes['preço'])))
        elif pergunta == 'velocidade maxima':
            print("A velocidade máxima da Mercedes é {}".format(mercedes['velocidade_max']))
    if info == 'audi':
        pergunta = (input("Quais informações você busca? Temos: modelo, velocidade máxima ou preço. :"))
        if pergunta == 'modelo':
            print("O modelo do Audi que tem disponível é o {}".format(audi['modelo']))
        elif pergunta == 'preço':
            print(print("Preço do Audi que temos disponível: {}".format(audi['preço'])))
        elif pergunta == 'velocidade maxima':
            print("A velocidade máxima do Audi é {}".format(audi['velocidade_max']))
    desejo = input("Deseja mais informações? ")