print('Jij bent een DSI-agent. jouw missie is je gaat een huis binnen stormen en de twee vijanden verslaan en de gijzelaar te redden')

point_if_entry = input('Ga jij de voor of achter deur doorbreken?')
if point_if_entry == 'achterdeur' or point_if_entry == 'voordeur':
    print('Je breekt de deur open door en expolsie verlies je je wapen.')
wel_of_niet = input('A: Pak je wapen op of B: Pak je hem niet op.')
if wel_of_niet == 'a' or wel_of_niet == 'A':
    print('Je pakt je wapen op en gaat naar binnen. je loopt naar de gang')
elif wel_of_niet == 'b' or wel_of_niet == 'B':
    print('Je ging zonder wapen naar binnen. Je bent dood')
    quit()
woonkamer = input('Je loopt naar de woonkamer. je ziet een van de gijzelaars en de gijzelaar. Hij schiet op jou, ga je A: Hem arresteren of B: schiet op hem ')
if woonkamer == 'a' or woonkamer == 'A':
    print('Hij schiet nog een keer op je want schreeuwen helpt niet (GAME OVER)')
    quit()
elif woonkamer == 'b' or woonkamer == 'B':
    print('Je raakt hem in zijn schouder hij ligt op de grond en je red de gijzelaar. Je loopt naar boven en gaat 1 kamer steeds doorzoeken')
sniper = input('Je ziet wat glinsteren in de kast je loopt er naar toe, het is een sniper. Pak je op of niet')
if sniper == 'pak de sniper op' or sniper == 'ja':
    print('je hebt de sniper op gepakt en gaat terug naar de gang')
elif sniper == 'niet' or sniper == 'nee': 
    print('je pakt hem niet op, je loopt terug naar de gang')
tweede_kamer = input('Je hoort geluid van de tweede kamer, je trapt de deur je ziet de gijzelaar hij sprint uit het raam. Spring je of niet?')
if tweede_kamer == 'niet':
    print('omdat je niet sprong is hij er vandoor gegaan jij loser')
    quit()
elif tweede_kamer == 'spring':
    if sniper == 'ja' or sniper == 'pak de sniper op':
        print('Je springt uit de raam en doet een 360 no scope across the map GG EZ (WIN)')
    elif sniper == 'nee' or sniper == 'niet':
        print('Je springt uit het raam maar je kan geen 360 no scope doen want je hebt geen sniper (fail)')