#gerar palavra aleatória
import random;
import background;

nomes = ['Alice', 'Bob', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Isaac', 'Julia', 'Gyovana', 'Laura', 'Miguel', 'Natalia', 'Otavio', 'Paula', 'Rafael', 'Sofia', 'Thiago', 'Valentina', 'Luiz']

random_name = (nomes[random.randint(1, len(nomes) - 1)]).lower()
print (random_name)

#gerar nome na tela
keyword = ("_" * len(random_name))
keyword_list = list(keyword)

vida = 0

while True:
    print(keyword)

    background.back(vida)

    letra = input("Escolha uma letra: ")

    if(letra in random_name):
        contador = 0
        for i in random_name:
            if(i) == letra:
                keyword_list[contador] = letra
                keyword = ''.join(keyword_list)
            contador += 1

    else:
        if(vida == 5):
            background.back(vida + 1)
            break
        else:
            vida += 1
            
    if(keyword == random_name):
        print("Você ganhou!!")
        break