palavra = input('uma palavra: ')

Type = input("qual é o tipo de palavra?")

mensagem = f''' 
O jOGO COMEÇOU CHUTE PALAVRAS

A DICA É: {Type} e começa com {palavra[0].upper()}



5 TENTATIVAS

'''
print(mensagem)

#palavras pra chutes
i = 5
for _ in range(i):
    t = input("tentativa: ")
    if t == palavra:
        print("certo")
        break
    else:
        print('errado, tente novamente')
        t
