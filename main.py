import random

from classes import *


def winning_game():  # Defining how to win
    print("You got enough gold for a ticket out the city!")
    print("You win the game!")


player = Player()
battle = False
locked = False

# Opening story

xyz = input("What is your name?\n")
print("After days of wondering the backcountry of Saskatchewan.")
print("You rest for a short while. Your eyes darken...")
print("You wake up to a somewhat deserted town")
print("You could visit the town")
print("or you will stay in the plains to see what else you missed...")
while player.hp > 0:

    if player.hp > player.maxhp: # staying alive
        player.hp = player.maxhp

    print("\nWould you explore the prairie? (Y/N)")
    ans = input().lower() # Main menu 1

    if ans == "y": # Randomized barrel encounter
        encounter = random.randint(1, 100)
        if encounter < 10:
            locked = True
            if player.gold >= 200:
                winning_game()
            while locked == True: # Locked/unlocked barrel
                print("You found a barrel while in a canola field! ")
                print(
                    "It appears to be locked...Do you want to try and unlock it? (Y/N)"
                )
                chest = input().lower()

                if chest != "y" and chest != "n":
                    print("Please enter a valid action")

                elif chest == "y":
                    unlock = random.randint(1, 100)

                    if player.lockpicks == True:
                        if unlock <= 80:
                            gold = random.randint(2, 10)
                            player.gold = player.gold + gold
                            print(f"You opened the barrel!")
                            print(f"You found {gold} gold inside of it!\n")
                            print("You now have {player.gold} gold.")
                            locked = False
                        elif unlock > 80:
                            print("Unfortunately, the barrel didn't open")
                            locked = False
                            continue

                    elif unlock > 80:
                        gold = random.randint(2, 10)
                        player.gold = player.gold + gold
                        print(f"You opened the chest!")
                        print(" You found {gold} gold inside of it!\n")
                        print("You now have {player.gold} gold.")
                        locked = False

                    elif unlock <= 80:
                        print("Unfortunately, the barrel didn't open")
                        locked = False
                        continue

                elif chest == "n":
                    continue

        elif encounter >= 10: # Enenmy encounters
            battle = True

            while battle == True:
                if player.upg == 0:
                    enemy_class = random.choice([Deer, Crow])
                else:
                    enemy_class = random.choice([Deer, Crow, Wolf])

                enemy = enemy_class()
                enemy_name = enemy_class.__name__

                print(f"You find a wild {enemy_name}! (A to attack)")

                enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

                while enemy.hp > 0 or player.hp > 0:
                    print("Press A to attack")
                    user = input().lower()

                    if user != "a" and user != "y":
                        print("Please enter a valid action")
                        continue

                    if user == "a":
                        enemy.hp = enemy.hp - player.dmg
                        print(
                            f"You dealt {player.dmg} damage to the {enemy_name}!"
                        )

                    if enemy.hp <= 0:
                        print("The wild animal is killed!")
                        battle = False

                        loot = random.randint(1, 100)

                        if loot >= 70: # Randomized loot from corpses
                            print(f" You found a bandage on the corpse!")
                            print("Some of your wounds have been healed!")
                            player.hp = player.hp + 5
                            print(f"You now have {player.hp} health.")
                        else:
                            gold = random.randint(1, 4)
                            player.gold = player.gold + gold

                            print(f"You found {gold} gold on the corpse!")
                            print(f"You now have {player.gold} gold!")
                        break

                    if user == "a":
                        enemy.dmg = enemy.dmg + random.choice([0, 1
                                                               ]) - player.ac
                        player.hp = player.hp - enemy.dmg

                        if enemy.dmg > 0:
                            print(f"The {enemy_name} attacks you!")
                            print(f"it deals {enemy.dmg} damage to you!")
                        elif enemy.dmg <= 0:
                            print(
                                f"The {enemy_name}'s attack was dodged your {player.armor}!"
                            )
                    if player.hp <= 0: # death/unconcious message

                        print(f"The {enemy_name} knocked you out!")
                        print("You wake with a headache")
                        print("and your gold is missing!")
                        player.gold = 0
                        print(f"You now have {player.gold} gold")
                        player.hp = 6
                        battle = False
                        break

    elif ans == "n": # Main menu 2 (town map)
        print(f"You have {player.hp} health.")
        print(f"{player.maxhp} is your maximum health.")
        print("You find a local town..")
        print("In town, there is an cozy looking inn")
        print("As well as a Co-Op store")
        print("and a beautiful church on the edge of the railroad")
        print("\nWhere will you go? (Inn/Co-Op/Church)")
        village = input().lower()

        if village == "inn": # Inn location of town
            print(f" It's a slow night for the Inn.")
            print(f"Beer is one gold piece and a bed is 3 gold pieces.")
            print(f"You have {player.gold} gold. (Drink/Sleep)")
            inn = input().lower()

            if inn == "sleep": # Sleeping at the Inn
                if player.gold < 3:
                    print("\nYou do not have enough gold!")
                    continue

                elif player.gold >= 3:
                    cost = 3
                    player.gold = player.gold - cost
                    print(
                        f"You stay the night at the Tavern and heal from the hard day."
                    )
                    print(f"You now have {player.gold}")
                    print(f"your health is {player.maxhp} health.")
                    player.hp = player.maxhp

            if inn == "drink":  # Drinking at the Inn
                if player.gold < 1:
                    print("You do not have enough gold!")
                    continue

                elif player.gold >= 1:
                    cost = 1
                    player.gold = player.gold - cost
                    print(f"You stop at the bar and grab yourself a beer")
                    print(
                        f"You now have {player.gold} gold left in your pockets."
                    )
                    drunken_event = random.randint(1, 100) # Randomized instance after drinking

                    if drunken_event > 10 and drunken_event <= 30:
                        print(
                            f"{player.hp} is your current health. {player.gold} is your gold."
                        )

                    elif drunken_event > 30 and drunken_event <= 80:

                        if player.gold >= 5:
                            bad_bet = random.randint(1, 5)
                        elif player.gold >= 2 and player.gold < 5:
                            bad_bet = random.randint(1, 2)
                        elif player.gold < 2:
                            continue
                        player.gold = player.gold - bad_bet
                        print(f"In your drunken stupidness,")
                        print(
                            "someone snatched {bad_bet} gold from your pockets"
                        )
                        print("You now have only {player.gold} gold left.")

                    elif drunken_event > 80:
                        good_bet = random.randint(1, 5)
                        player.gold = player.gold + good_bet
                        print(f" You won multiple bets from the bartender!")
                        print(
                            " You won {good_bet} gold.\nYou now have {player.gold} gold!"
                        )
                    break

        elif village == "coop" or village == "co-op":  # Co-Op location of town
            print("The marketplace is also very quiet with littleactivity.")
            print("You see a clothing area to your left")
            print("You see a weapons area to your right")
            print("You see a locksmith directly in front of you")
            print(
                "Would you like to go left, right or straight? (clothing/Smith/Locksmith)"
            )
            market = input().lower()
            if market == "clothing" or market == "left":  # Clothing area of Co-Op
                print(
                    "The clothing store is stocked with all sorts of clothes.")
                print(
                    "\nThe cashier asks if you would like the items in stock. (Y/N)" 
                )
                ans = input().lower()
                clothing = ["Leather jacket", "Steel jacket"] 
                leather_price = 8
                steel_price = 25
                if ans == "y":
                    print(
                        f"The cashier says he currently has {clothing} in stock."
                    )
                    print("Would you like to buy one?(Y/N)")
                    ans2 = input().lower()

                    if ans2 == "y":
                        print(f"The {clothing[0]} costs {leather_price}")
                        print(
                            f"{clothing[1]} costs {steel_price}.\nleather or steel?"
                        )
                        ans3 = input().lower()

                        if ans3 == "leather":
                            if player.gold < leather_price:
                                print("You do not have enough gold!")
                            elif player.gold >= leather_price:
                                player.gold = player.gold - leather_price
                                print(
                                    f"The cashier hands you the Leather jacket. Your armor has increased!"
                                )
                                print(f"You now have {player.gold} gold.")
                                player.ac = 1
                                player.armor = "Leather jacket"

                        if ans3 == "steel":
                            if player.gold < steel_price:
                                print("You do not have enough gold!")
                                continue
                            elif player.gold >= steel_price:
                                player.gold = player.gold - steel_price
                                print(
                                    f"The cashier hands you the Steel jacket. Your armor has increased!"
                                )
                                print(f"You now have {player.gold} gold.")
                                player.ac = 2
                                player.upg = player.upg + 1
                                player.armor = "Steel Plated armor"

                    elif ans == "n":
                        print(
                            "The cashier turns his back and asks you to come back next time."
                        )
                        continue
                elif ans == "n":
                    print(
                        "The cashier turns his back and asks you to come back next time."
                    )
                    continue

            if market == "weapons" or market == "right": # Weapons area of Co-Op

                if player.upg == 0:
                    cost = 10

                    print(
                        f"The cashier agrees to upgrade your sword for {cost} gold."
                    )
                    print(
                        f" You have {player.gold} gold. Do you want him to upgrade your blade? (Y/N)"
                    )
                    upgrade = input().lower()
                    if upgrade == "y":
                        if player.gold < cost:
                            print("You do not have enough gold!")
                            continue
                        elif player.gold >= cost:
                            player.gold = player.gold - cost
                            print(
                                "The cashier upgraded your sword. You now do more damage!"
                            )
                            player.dmg = player.dmg + 2
                            player.upg = player.upg + 1
                        elif upgrade == "n":
                            continue

                elif player.upg == 1:
                    cost = 25

                    print(
                        f"The cashier agrees to upgrade your sword for {cost} gold."
                    )
                    print(
                        f" You have {player.gold} gold. Do you want him to upgrade your blade? (Y/N)"
                    )
                    upgrade = input().lower()
                    if upgrade == "y":
                        if player.gold < cost:
                            print("You do not have enough gold!")
                            continue
                        elif player.gold >= cost:
                            player.gold = player.gold - cost
                            print(
                                "The cashier upgraded your sword. You now do more damage!"
                            )
                            player.dmg = player.dmg + 2
                            player.upg = player.upg + 1
                    elif upgrade == "n":
                        continue

                elif player.upg == 2:
                    cost = 50

                    print(
                        f"The cashier agrees to upgrade your sword for {cost} gold."
                    )
                    print(
                        f" You have {player.gold} gold. Do you want him to upgrade your blade? (Y/N)"
                    )
                    upgrade = input().lower()
                    if upgrade == "y":
                        if player.gold < cost:
                            print("You do not have enough gold!")
                            continue
                        elif player.gold >= cost:
                            player.gold = player.gold - cost
                            print(
                                "The cashier upgraded your sword. You now do more damage!"
                            )
                            player.dmg = player.dmg + 2
                            player.upg = player.upg + 1

                    elif upgrade == "n":
                        continue

                elif player.upg >= 3:
                    print(f"The cashier cannot upgrade any further")
                    continue

            elif market == "straight" or market == "Locksmith": # locksmith area of Co-Op
                print(
                    "The locksmith asks if you'd care to browse his sets. (Y/N)"
                )
                locksmither = input().lower()

                if locksmither == "y":
                    price = 20
                    lockings = [
                        "lockpick set",
                    ]
                    print(
                        f"The locksmither tells you he currently has a {lockings} in stock."
                    )
                    print(
                        " They cost {price} gold. Would you like to buy one? (Y/N)"
                    )
                    ans = input().lower()
                    if ans == "y":
                        if player.gold < price:
                            print("You do not have enough gold!")
                            continue

                        elif player.gold >= price:
                            player.gold = player.gold - price
                            player.lockpicks = True
                            print(f"You bought the {lockings}!")
                            print("You now have {player.gold} gold left")
                    elif ans == "n":
                        print("You wasted the locksmiths time")
                        print("he locksmither agrily cusses you out.")
                        continue

                elif locksmither == "n":
                    print("You wasted the locksmiths time")
                    print("he locksmither agrily cusses you out.")
                    continue
            else:
                print("Please enter a valid action")
                continue

        elif village == "church": # Church of the town

            print(
                'You enter the lowkey town church,\n"Health?" He asks. (Y/N)')
            ans = input().lower()
            if player.hpupg == 0:
                price = 15
            elif player.hpupg == 1:
                price = 50

            if ans == "y":
                print(f"This comes with a price. It costs {price} gold ")
                print("Do you agree to this?(Y/N)")
                ans2 = input().lower()

                if ans2 == "y":
                    if player.gold < price:
                        print("not enough gold!")
                        continue
                    elif player.gold >= price:
                        player.gold = player.gold - price
                        player.maxhp = player.maxhp + 10
                        print("Your health has increased! ")
                        player.hpupg = player.hpupg + 1
                        continue

                elif ans2 == "n":
                    print("The preist walks away from you")
                    continue

            if ans == "n":
                print("The preist walks away from you")
                continue

        else:
            print("Please enter a valid action")
            continue

    else:
        print("Please enter a valid action")
        continue
