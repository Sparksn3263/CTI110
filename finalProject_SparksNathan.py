# Nathan Sparks
# 12 May 26
# finalProject
# Space exploration game



# Space Explorer: The Lost Star Crystal
# Objective:
# Find 3 Star Crystal Fragments and assemble the legendary Star Crystal.
# The game continues until the objective is completed or the player dies.
# Designed to take several minutes to finish and encourages:
# - Exploring planets
# - Trading for supplies
# - Eating food
# - Resting
# - Managing health, fuel, and energy

import random
import time

# print text slowing 
def slow_print(message, delay=1):
    
    print(message)
    time.sleep(delay)

# Create astronaut dictionary
def create_player():
    
    player = {
        "name": input("Enter your astronaut's name: "),
        "health": 100,
        "energy": 100,          # Must sleep to restore
        "fuel": 60,
        "credits": 100,
        "missions_completed": 0,
        "inventory": {
            "Med Kits": 2,
            "Food Packs": 4,
            "Ship Parts": 2,
            "Artifacts": 0,
            "Crystal Fragments": 0
        }
    }
    return player

# Display character stats 
def show_stats(player):
    
    print("\n🚀 ASTRONAUT STATUS")
    print("-" * 35)
    print(f"👨‍🚀 Name: {player['name']}")
    print(f"❤️ Health: {player['health']}")
    print(f"⚡ Energy: {player['energy']}")
    print(f"⛽ Fuel: {player['fuel']}")
    print(f"💳 Credits: {player['credits']}")
    print(f"🛰️ Missions Completed: {player['missions_completed']}")
    print("\n🎯 Objective: Collect 3 Crystal Fragments")
    print(f"💎 Fragments Found: {player['inventory']['Crystal Fragments']}/3")
    print("\n🎒 Inventory:")
    for item, quantity in player["inventory"].items():
        print(f"   {item}: {quantity}")
    print()

# use medkit to restore characters health
def use_medkit(player):
    if player["inventory"]["Med Kits"] > 0:
        player["inventory"]["Med Kits"] -= 1
        heal = random.randint(20, 35)
        player["health"] = min(100, player["health"] + heal)
        slow_print(f"🩹 You restored {heal} health.")
    else:
        slow_print("❌ No Med Kits available.")

# eat food to restore health and energy
def eat_food(player):
    if player["inventory"]["Food Packs"] > 0:
        player["inventory"]["Food Packs"] -= 1
        health_gain = random.randint(5, 10)
        energy_gain = random.randint(15, 30)
        player["health"] = min(100, player["health"] + health_gain)
        player["energy"] = min(100, player["energy"] + energy_gain)
        slow_print(
            f"🍎 You ate a Food Pack. +{health_gain} health, +{energy_gain} energy."
        )
    else:
        slow_print("❌ No Food Packs left.")

# Rest character to restore energy and health
def rest(player):
    
    energy_gain = random.randint(30, 50)
    health_gain = random.randint(5, 10)

    player["energy"] = min(100, player["energy"] + energy_gain)
    player["health"] = min(100, player["health"] + health_gain)

    slow_print(
        f"😴 You slept in your ship. +{energy_gain} energy, +{health_gain} health."
    )

# Repair ship
def repair_ship(player):
    if player["inventory"]["Ship Parts"] > 0:
        player["inventory"]["Ship Parts"] -= 1
        fuel_gain = random.randint(20, 40)
        player["fuel"] += fuel_gain
        slow_print(f"🔧 Ship repaired. +{fuel_gain} fuel.")
    else:
        slow_print("❌ No Ship Parts available.")


# Buy and Sell suppies at trading station
def trade_at_station(player):
    
    while True:
        print("\n🏪 SPACE STATION MARKET")
        print(f"💳 Credits Available: {player['credits']}")
        print("\nBUY ITEMS")
        print("1. Food Pack (+1) ........ 25 credits")
        print("2. Med Kit (+1) ......... 60 credits")
        print("3. Ship Parts (+1) ...... 50 credits")
        print("4. Fuel (+25) ........... 45 credits")

        print("\nSELL ITEMS")
        print("5. Sell Artifact ........ 75 credits")
        print("6. Sell Ship Parts ...... 25 credits")
        print("7. Sell Food Pack ....... 10 credits")

        print("\n8. Leave Market")

        choice = input("Choose an option: ")

        # ---------- BUY OPTIONS ----------
        if choice == "1":
            if player["credits"] >= 25:
                player["credits"] -= 25
                player["inventory"]["Food Packs"] += 1
                slow_print("🍎 Purchased Food Pack.")
            else:
                slow_print("❌ Not enough credits.")

        elif choice == "2":
            if player["credits"] >= 60:
                player["credits"] -= 60
                player["inventory"]["Med Kits"] += 1
                slow_print("🩹 Purchased Med Kit.")
            else:
                slow_print("❌ Not enough credits.")

        elif choice == "3":
            if player["credits"] >= 50:
                player["credits"] -= 50
                player["inventory"]["Ship Parts"] += 1
                slow_print("🔧 Purchased Ship Parts.")
            else:
                slow_print("❌ Not enough credits.")

        elif choice == "4":
            if player["credits"] >= 45:
                player["credits"] -= 45
                player["fuel"] += 25
                slow_print("⛽ Purchased fuel.")
            else:
                slow_print("❌ Not enough credits.")

        # ---------- SELL OPTIONS ----------
        elif choice == "5":
            if player["inventory"]["Artifacts"] > 0:
                player["inventory"]["Artifacts"] -= 1
                player["credits"] += 75
                slow_print("🔮 You sold an Artifact for 75 credits.")
            else:
                slow_print("❌ You have no Artifacts to sell.")

        elif choice == "6":
            if player["inventory"]["Ship Parts"] > 0:
                player["inventory"]["Ship Parts"] -= 1
                player["credits"] += 25
                slow_print("🔧 You sold Ship Parts for 25 credits.")
            else:
                slow_print("❌ You have no Ship Parts to sell.")

        elif choice == "7":
            if player["inventory"]["Food Packs"] > 0:
                player["inventory"]["Food Packs"] -= 1
                player["credits"] += 10
                slow_print("🍎 You sold a Food Pack for 10 credits.")
            else:
                slow_print("❌ You have no Food Packs to sell.")

        # ---------- EXIT ----------
        elif choice == "8":
            slow_print("👋 Leaving the market.")
            break

        # ---------- INVALID ----------
        else:
            slow_print("❌ Invalid choice.")

# Main game options rules that limit exploring based on fuel and energy and set chances for each exploration
def explore_planet(player):
    
    if player["fuel"] < 15:
        slow_print("⛽ You need more fuel before exploring.")
        return

    if player["energy"] < 20:
        slow_print("😴 You are too tired. You should rest first.")
        return

    slow_print("\n🪐 Exploring a distant planet...")

    # Exploration costs
    player["fuel"] -= 15
    player["energy"] -= 20

    event = random.randint(1, 100)

    # Rare chance to find a crystal fragment
    if event <= 15:
        player["inventory"]["Crystal Fragments"] += 1
        slow_print("💎 AMAZING! You discovered a Star Crystal Fragment!")
    elif event <= 35:
        reward = random.randint(40, 100)
        player["credits"] += reward
        player["inventory"]["Artifacts"] += 1
        slow_print(f"🔮 You found ancient artifacts worth {reward} credits.")
    elif event <= 55:
        damage = random.randint(10, 25)
        player["health"] -= damage
        slow_print(f"👾 Hostile aliens attacked! You lost {damage} health.")
    elif event <= 75:
        player["inventory"]["Food Packs"] += 1
        slow_print("🍎 You found a Food Pack.")
    elif event <= 90:
        player["inventory"]["Ship Parts"] += 1
        slow_print("🔧 You salvaged useful Ship Parts.")
    else:
        slow_print("🌌 Nothing unusual was discovered.")

    player["missions_completed"] += 1

# print intro to game, name character, and start game
def main():
    slow_print("🌠 WELCOME TO SPACE EXPLORER: THE LOST STAR CRYSTAL 🌠")
    slow_print("Legend says a powerful Star Crystal was shattered into 3 fragments.")
    slow_print("Your mission is to recover all 3 fragments and restore the crystal.")
    slow_print("Manage your health, energy, fuel, and supplies carefully.\n")

    player = create_player()

    # Main game loop continues until objective is complete
    while (
        player["health"] > 0
        and player["inventory"]["Crystal Fragments"] < 3
    ):
        show_stats(player)

        print("Choose an action:")
        print("1. 🪐 Explore a planet")
        print("2. 🍎 Eat Food")
        print("3. 😴 Sleep")
        print("4. 🩹 Use Med Kit")
        print("5. 🔧 Repair Ship")
        print("6. 🏪 Trade at Space Station")
        print("7. 🚪 Quit Game")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            explore_planet(player)
        elif choice == "2":
            eat_food(player)
        elif choice == "3":
            rest(player)
        elif choice == "4":
            use_medkit(player)
        elif choice == "5":
            repair_ship(player)
        elif choice == "6":
            trade_at_station(player)
        elif choice == "7":
            slow_print("👋 Mission aborted.")
            return
        else:
            slow_print("❌ Invalid choice.")

        # Ongoing fatigue and hunger create need for sleep and food
        player["energy"] -= 5
        if player["energy"] < 0:
            player["energy"] = 0

        if player["energy"] == 0:
            slow_print("😵 You collapsed from exhaustion.")
            player["health"] -= 15

        # Prevent stats from going negative
        if player["health"] < 0:
            player["health"] = 0

    # Endings
    if player["health"] <= 0:
        slow_print("\n💀 Your mission has failed.")
    else:
        slow_print("\n✨ You assembled the legendary Star Crystal! ✨")
        slow_print("🏆 The galaxy celebrates your incredible discovery!")
        slow_print(f"🎉 Congratulations, Captain {player['name']}!")


if __name__ == "__main__":
    main()