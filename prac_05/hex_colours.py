COLOURS = {"bittersweet shimmer":"#bf4f51",
           "bole":"#79443b",
           "boysenberry":"#873260",
           "brandeis blue":"#0070ff",
           "british racing green":"#004225",
           "brunswick green":"#1b4d3e",
           "bubble gum":"#ffc1cc",
           "burlywood":"#deb887",
           "cadetblue":"#5f9ea0",
           "candy pink":"#e4717a",
           "carrot orange":"#ed9121"}

colour_choice = input("What colour do you want? ").lower()
while colour_choice != "":
    try:
        print(f"the {colour_choice} has key: {COLOURS[colour_choice]}")
    except KeyError:
        print("Sorry, I didn't find that colour.")
    colour_choice = input("What colour do you want? ")