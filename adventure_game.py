from random import randint

print('''Isto é um jogo de escolhas, cada escolha terá consequências. 
Te desejo sorte, e boas escolhas!\n
São 6h da manhã e seu despertador está tocando.
[1] Acordar na hora
[2] Soneca de 10 minutos
Sua opção: ''', end='')

while True:
    opção = input()
    if opção != '1' and opção != '2':
        print("Digite '1' ou '2' pra tomar sua decisão.")
        continue
    
    else:
        opção = int(opção)
        if opção == 1:
            print('''Você acordou logo, agora você tem que tomar café da manhã, 
tomar banho e se arrumar pra escola.
[1] Fazer logo as tarefas matinais
[2] Mexer no celular
Sua opção: ''', end='')

            while True:
                opção = input()
                if opção != '1' and opção != '2':
                    print("Digite '1' ou '2' pra tomar sua decisão.")
                    continue

                else:
                    opção = int(opção)
                    if opção == 1:
                        print('''Você fez suas tarefas, e assim conseguiu se adiantar 15 minutos.
[1] Mexer no celular até dar o horário
[2] Sair adiantado mesmo 
Sua opção: ''', end='')

                        while True:
                            opção = input()
                            if opção != '1' and opção != '2':
                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                continue

                            else:
                                opção = int(opção)
                                if opção == 1:
                                        print('''Você ficou mexendo no celular até dar o horário e então saiu.
Chegou na escola e ficou conversando com seus amigos até a professora chegar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')

                                if opção == 2:
                                    print('''Você saiu adiantado e sem muito tumulto na rua, chegou cedo na escola.
[1] Ficar do lado de fora, esperando seus amigos
[2] Entrar na escola e ir para a sala
Sua opção: ''', end='')

                                    while True:
                                        opção = input()
                                        if opção != '1' and opção != '2':
                                            print("Digite '1' ou '2' pra tomar sua decisão.")
                                            continue

                                        else:
                                            opção = int(opção)
                                            if opção == 1:
                                                print('''Você esperou seus amigos, e eles chegaram. 
Vocês foram juntos para a sala de aula e esperaram a professora chegar.
Ela chegou e vocês começaram a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')
                                            
                                            if opção == 2:
                                                print('''Você entrou na sala de aula e ninguém chegou ainda.
[1] Pegar seus cadernos e ler a matéria
[2] Tirar uma sonequinha
Sua opção: ''', end='')

                                                while True:
                                                    opção = input()
                                                    if opção != '1' and opção != '2':
                                                        print("Digite '1' ou '2' pra tomar sua decisão.")
                                                        continue

                                                    else:
                                                        opção = int(opção)
                                                        if opção == 1:
                                                            print('''Quando seus colegas chegam na sala, te veem estudando.
Apontam para você e te zombam de 'nerd' pelo resto da aula.
FINAL TRISTE! Reinicie o script e tente descobrir outro final. ''')

                                                        if opção == 2:
                                                            wake_up = randint(0, 4)
                                                            if wake_up < 3:
                                                                print('''Quando seus colegas chegam na sala, você acorda.
Vocês conversam um pouco antes da professora chegar.
Ela chegou e vocês começaram a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')
                                                                
                                                            if wake_up > 2:
                                                                print('''Enquanto você está dormindo, seus colegas chegam na sala.
Você está num sono pesado e eles percebem isso.
Aproveitam isso para desenhar bigodinhos e te zoar por toda a aula como 'dorminhoco'
FINAL TRISTE! Reinicie o script e tente descobrir outro final.''')

                    if opção == 2:
                        print('''Você decidiu mexer no celular antes de fazer suas tarefas.
Como consequência, você se atrasou para sair de casa.
Agora tem que sair correndo para não se atrasar na escola.
[1] Ir pelo caminho convencional
[2] Pegar um atalho
Sua opção: ''', end='')
                   
                        while True:
                            opção = input()
                            if opção != '1' and opção != '2':
                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                continue

                            else:
                                opção = int(opção)
                                if opção == 1:
                                    print('''Você foi pelo caminho seguro, mas chegou atrasado na escola.
Por causa disso, você só entrou na segunda aula.
Ao chegar na sala, alguns zombam de você. 
'De novo atrasado, esse cara não tem jeito'
'Hahaha, não sei como ele quer ter um futuro assim'
'Que moleque inútil, nem chegar no horário consegue'
FINAL TRISTE! Reinicie o script e tente descobrir outro final. ''')

                                if opção == 2:
                                    print('''Você saiu adiantado e sem muito tumulto na rua, chegou cedo na escola.
[1] Ficar do lado de fora, esperando seus amigos
[2] Entrar na escola e ir para a sala
Sua opção: ''', end='')

                                    while True:
                                        opção = input()
                                        if opção != '1' and opção != '2':
                                            print("Digite '1' ou '2' pra tomar sua decisão.")
                                            continue

                                        else:
                                            opção = int(opção)
                                            if opção == 1:
                                                print('''Você esperou seus amigos, e eles chegaram. 
Vocês foram juntos para a sala de aula e esperaram a professora chegar.
Ela chegou e vocês começaram a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')
                                            
                                            if opção == 2:
                                                print('''Você entrou na sala de aula e ninguém chegou ainda.
[1] Pegar seus cadernos e ler a matéria
[2] Tirar uma sonequinha
Sua opção: ''', end='')

                                                while True:
                                                    opção = input()
                                                    if opção != '1' and opção != '2':
                                                        print("Digite '1' ou '2' pra tomar sua decisão.")
                                                        continue

                                                    else:
                                                        opção = int(opção)
                                                        if opção == 1:
                                                            print('''Quando seus colegas chegam na sala, te veem estudando.
Apontam para você e te zombam de 'nerd' pelo resto da aula.
FINAL TRISTE! Reinicie o script e tente descobrir outro final. ''')

                                                        if opção == 2:
                                                            wake_up = randint(0, 1)
                                                            if wake_up == 0:
                                                                print('''Quando seus colegas chegam na sala, você acorda.
Vocês conversam um pouco antes da professora chegar.
Ela chegou e vocês começaram a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')
                                                                
                                                            if wake_up == 1:
                                                                print('''Enquanto você está dormindo, seus colegas chegam na sala.
Você está num sono pesado e eles percebem isso.
Aproveitam isso para desenhar bigodinhos e te zoar por toda a aula como 'dorminhoco'
FINAL TRISTE! Reinicie o script e tente descobrir outro final.''')

                    if opção == 2:  
                        print('''Você acabou se distraindo com as redes sociais e agora está atrasado.
Tomou banho correndo, colocou a roupa, pegou um pedaço de pão e foi pra escola.
[1] Ir pelo caminho convencional
[2] Pegar um atalho
Sua opção: ''', end='') 

                        while True:
                            opção = input()
                            if opção != '1' and opção != '2':
                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                continue

                            else:
                                opção = int(opção)
                                if opção == 1:
                                    print('''Você acabou chegando atrasado, mesmo se esforçando para andar rápido.
Por causa disso, você só entrou na segunda aula.
Ao chegar na sala, alguns zombam de você. 
'De novo atrasado, esse cara não tem jeito'
'Hahaha, não sei como ele quer ter um futuro assim'
'Que moleque inútil, nem chegar no horário consegue'
FINAL TRISTE! Reinicie o script e tente descobrir outro final. ''')
                                    
                                if opção == 2:
                                    stole = randint(0, 1)
                                    if stole == 0:
                                        print('''Pegando o atalho, você conseguiu chegar a tempo na escola. 
Você senta na sua carteira e conversa com seus amigos até a professora chegar.
Depois você começa a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')
                                
                                    if stole == 1:
                                        print('''Um cara está andando atrás de você, perto de um beco.
De repente, ele te aborda e anuncia um assalto, te ameaçando com uma faca.
[1] Resistir e tentar desarmar ele
[2] Deixar ele levar o celular
Sua opção: ''', end='')

                                        while True:
                                            opção = input()
                                            if opção != '1' and opção != '2':
                                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                                continue

                                            else:
                                                opção = int(opção)
                                                if opção == 1:
                                                    disarm = randint(0, 1)
                                                    if disarm == 0:
                                                        print('''Você infelizmente não conseguiu desarmar o assaltante...
E pela sua reação agressiva, ele te atingiu com a faca no peito.
Você morreu.
FINAL TRISTE! Reinicie o script e tente descobrir outro final.''')

                                                    if disarm == 1:
                                                        print('''Você conseguiu desarmar o assaltante e assim, ele fugiu.
Você foi correndo pra escola, ainda meio assustado.
Assim, chegou a tempo na escola e entrou na sala.
Conversou com seus amigos até a professora chegar e começar o estudo.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')

                                                if opção == 2:
                                                    print('''Você deixou o assaltante levar o seu celular e saiu ileso.
Continuou seu caminho até a escola, andando rápido, ainda meio assustado.
Assim, chegou a tempo na escola e entrou na sala.
Conversou com seus amigos até a professora chegar e começar o estudo.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')

        if opção == 2:
            print('''Você tirou sua sonequinha e ficou um pouco melhor, 
agora você tem que tomar café da manhã, tomar banho e se arrumar pra escola.
[1] Fazer logo as tarefas matinais
[2] Mexer no celular
Sua opção: ''', end='')

            while True:
                opção = input()
                if opção != '1' and opção != '2':
                    print("Digite '1' ou '2' pra tomar sua decisão.")
                    continue

                else:
                    opção = int(opção)
                    if opção == 1:
                        print('''Você fez suas tarefas, e assim conseguiu se adiantar 10 minutos.
[1] Mexer no celular até dar o horário
[2] Sair adiantado mesmo 
Sua opção: ''', end='')

                        while True:
                            opção = input()
                            if opção != '1' and opção != '2':
                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                continue

                            else:
                                opção = int(opção)
                                if opção == 1:
                                    distraction = randint(0, 1)
                                    if distraction == 0:
                                        print('''Você ficou mexendo no celular até dar o horário e então saiu.
Chegou na escola e ficou conversando com seus amigos até a professora chegar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')
                                    
                                    if distraction == 1:
                                        print('''Você acabou se distraindo com as redes sociais e agora está atrasado.
[1] Ir pelo caminho convencional
[2] Pegar um atalho
Sua opção: ''', end='')
                                
                                if opção == 2:
                                    print('''Você saiu adiantado e sem muito tumulto na rua, chegou cedo na escola.
[1] Ficar do lado de fora, esperando seus amigos
[2] Entrar na escola e ir para a sala
Sua opção: ''', end='')

                                    while True:
                                        opção = input()
                                        if opção != '1' and opção != '2':
                                            print("Digite '1' ou '2' pra tomar sua decisão.")
                                            continue

                                        else:
                                            opção = int(opção)
                                            if opção == 1:
                                                print('''Você esperou seus amigos, e eles chegaram. 
Vocês foram juntos para a sala de aula e esperaram a professora chegar.
Ela chegou e vocês começaram a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')
                                            
                                            if opção == 2:
                                                print('''Você entrou na sala de aula e ninguém chegou ainda.
[1] Pegar seus cadernos e ler a matéria
[2] Tirar uma sonequinha
Sua opção: ''', end='')

                                                while True:
                                                    opção = input()
                                                    if opção != '1' and opção != '2':
                                                        print("Digite '1' ou '2' pra tomar sua decisão.")
                                                        continue

                                                    else:
                                                        opção = int(opção)
                                                        if opção == 1:
                                                            print('''Quando seus colegas chegam na sala, te veem estudando.
Apontam para você e te zombam de 'nerd' pelo resto da aula.
FINAL TRISTE! Reinicie o script e tente descobrir outro final. ''')

                                                        if opção == 2:
                                                            wake_up = randint(0, 1)
                                                            if wake_up == 0:
                                                                print('''Quando seus colegas chegam na sala, você acorda.
Vocês conversam um pouco antes da professora chegar.
Ela chegou e vocês começaram a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')
                                                                
                                                            if wake_up == 1:
                                                                print('''Enquanto você está dormindo, seus colegas chegam na sala.
Você está num sono pesado e eles percebem isso.
Aproveitam isso para desenhar bigodinhos e te zoar por toda a aula como 'dorminhoco'
FINAL TRISTE! Reinicie o script e tente descobrir outro final.''')

                    if opção == 2:  
                        print('''Você acabou se distraindo com as redes sociais e agora está atrasado.
Tomou banho correndo, colocou a roupa, pegou um pedaço de pão e foi pra escola.
[1] Ir pelo caminho convencional
[2] Pegar um atalho
Sua opção: ''', end='') 

                        while True:
                            opção = input()
                            if opção != '1' and opção != '2':
                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                continue

                            else:
                                opção = int(opção)
                                if opção == 1:
                                    print('''Você acabou chegando atrasado, mesmo se esforçando para andar rápido.
Por causa disso, você só entrou na segunda aula.
Ao chegar na sala, alguns zombam de você. 
'De novo atrasado, esse cara não tem jeito'
'Hahaha, não sei como ele quer ter um futuro assim'
'Que moleque inútil, nem chegar no horário consegue'
FINAL TRISTE! Reinicie o script e tente descobrir outro final. ''')
                                    
                                if opção == 2:
                                    stole = randint(0, 1)
                                    if stole == 0:
                                        print('''Pegando o atalho, você conseguiu chegar a tempo na escola. 
Você senta na sua carteira e conversa com seus amigos até a professora chegar.
Depois você começa a estudar.
FINAL FELIZ! Reinicie o script e tente descobrir outro final. ''')

                                    if stole == 1:
                                        print('''Um cara está andando atrás de você, perto de um beco.
De repente, ele te aborda e anuncia um assalto, te ameaçando com uma faca.
[1] Resistir e tentar desarmar ele
[2] Deixar ele levar o celular
Sua opção: ''', end='')

                                        while True:
                                            opção = input()
                                            if opção != '1' and opção != '2':
                                                print("Digite '1' ou '2' pra tomar sua decisão.")
                                                continue

                                            else:
                                                opção = int(opção)
                                                if opção == 1:
                                                    disarm = randint(0, 1)
                                                    if disarm == 0:
                                                        print('''Você infelizmente não conseguiu desarmar o assaltante...
E pela sua reação agressiva, ele te atingiu com a faca no peito.
Você morreu.
FINAL TRISTE! Reinicie o script e tente descobrir outro final.''')

                                                    if disarm == 1:
                                                        print('''Você conseguiu desarmar o assaltante e assim, ele fugiu.
Você foi correndo pra escola, ainda meio assustado.
Assim, chegou a tempo na escola e entrou na sala.
Conversou com seus amigos até a professora chegar e começar o estudo.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')

                                                if opção == 2:
                                                    print('''Você deixou o assaltante levar o seu celular e saiu ileso.
Continuou seu caminho até a escola, andando rápido, ainda meio assustado.
Assim, chegou a tempo na escola e entrou na sala.
Conversou com seus amigos até a professora chegar e começar o estudo.
FINAL FELIZ! Reinicie o script e tente descobrir outro final.''')
