"""script simples remoção do background de imagens, imagens são adicionadas na pasta to remove, ao rodar o código, 
uma janela de pergunta para o usuário selecionar a pasta onde está o arquivo que deseja remover o background, o usuário
selecionar a pasta e o arquivo, o script foi escrito de tal forma que, o programa vai rodar na mesma quantidade de 
de arquivos que houver na pasta to remove, ao selecionar uma a uma as imagens, o programa removerá o background e 
adicionará automaticamente para pasta removed"""

import os
import easygui as eg
from rembg import remove
from PIL import Image

images = os.listdir('./to remove')
i = 1

for image in images:
 
    image = eg.fileopenbox(title='Selecione o arquivo')
    input = Image.open(image)
    output = remove(input)
    output_path = f'./removed/removed{i}.png'
    output.save(output_path)
    i += 1

