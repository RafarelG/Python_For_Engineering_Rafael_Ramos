import numpy as np

recipes = np.genfromtxt('recipes.csv', delimiter=',')

print(recipes)

print(recipes.shape)
print(recipes.dtype)

cupcakes = recipes[0]
print(cupcakes)
cookies = recipes[2]
print(cookies)

grocery_list = 2 *cupcakes + cookies
print(grocery_list) # 2 batches of cupcakes and 1 batch of cookies