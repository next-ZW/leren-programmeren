# nawfal kouzmane Pizza calculator

small_pizza_prijs = 9
medium_pizza_prijs = 11
large_pizza_prijs = 13

print(f'small pizza kost {small_pizza_prijs} euro')
print(f'medium pizza kost {medium_pizza_prijs}euro')
print(f'large pizza kost {large_pizza_prijs} euro')
 

hoeveel_pizzas_small = int(input('hoeveel small pizzas wil je?'))
hoeveel_pizza_medium = int(input('hoeveel medium pizzas wil je?'))
hoeveel_pizza_large =int (input('hoeveel large pizzas wil je?'))

prijs_small_pizza = hoeveel_pizzas_small * small_pizza_prijs 
prijs_medium_pizza = hoeveel_pizza_medium * medium_pizza_prijs 
prijs_large_pizza = hoeveel_pizza_large * large_pizza_prijs 
totaal_prijs = prijs_small_pizza + prijs_medium_pizza + prijs_large_pizza


print("--------------------------------------------------")
print(f' {hoeveel_pizzas_small} small pizza: {prijs_small_pizza} euro')
print(f' {hoeveel_pizza_medium} medium pizza: {prijs_medium_pizza} euro')
print(f' {hoeveel_pizza_large} large pizza: {prijs_large_pizza} euro')
print(f'{ totaal_prijs } euro, dit is je totale prijs ' ) 
print("--------------------------------------------------")