# import os
# print(os.getcwd())
# os.chdir('..')                  
# os.chdir('..')
# print(os.getcwd())
# os.chdir('C:\\')
# print(os.getcwd())
# directorio = os.path.join('C:', 'Users', 'snm_1', 'Documents', 'UNSAM', 'Python', 'ejercicios_python')
# os.chdir(directorio)
# print(os.getcwd())
# print(os.listdir('Data'))
# os.mkdir('test')          # creo el directorio test
# os.mkdir(os.path.join('test', 'carpeta'))  # creo el subdirectorio carpeta dentro de test
# os.listdir('test')
# os.chdir('test')                     # entro en el directorio test
# os.listdir()
# os.rename('carpeta','carpeta_nueva') # cambio el nombre de carpeta
# os.listdir()
# os.chdir('..')
# os.listdir('test')
# os.rename(os.path.join('test', 'carpeta_nueva'), os.path.join('test','carpeta_vieja'))
# os.listdir('test')
# os.rename(os.path.join('test','carpeta_vieja'), 'carpeta_vieja') 
# print(os.listdir('test'))

import os
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))



