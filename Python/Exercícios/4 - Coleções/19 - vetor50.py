"""Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5* i)%(i + 1), sendo a posição do elemento no vetor. 
Em seguida imprima o vetor na tela. 
"""
a = []
for i in range(50):
    a.append((i + 5*i)%(i+1))
print(a)