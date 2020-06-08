locations = (
    "Kippel",
    "Yukon Hotel",
    "Capple Quarters",
    "Thorton Residence",
    "Ennis House",
    "The Bradbury",
    "Animoid Row",
    "Chinatown",
    "Hysteria Hall",
    "Nightclub Row",
    "Gardner Strait",
    "Tyrell Corporation",
    "Polizeipräsidium",
)

NPC = (
    "Eldon Tyrell",
    "Miranda Tyrell",
    "Rep Vorarbeiter",
    "Chefinspektor Bryant",
    "Inspektor Resch",
    "Inspektor Steele",
    "Inspektor Mc Coy",
    "Gerichtsmedizinerin",
    "Wachoffizier",
    "Howie Lee",
    "Mama Isabella",
    "Early Q",
    "Taffy Lewis",
    "Mia",
    "Crazy Legs Larry",
    "Izo",
    "Bob Gorsky",
    "Emil Runciter",
    "Rick Deckard",
    "Slater",
    "Arthur Kaufmann",
    "Rajesh Singh",
    "Dektora",
    "Chiara",
    "Chalisa",
    "Gaff",
    "George Gleason",
    "Cash Grigorian",
    "Willbur Mercer"
)

Spieler = [

]

eldon_tyrell = {"name": "Eldon Tyrell", "race": "Mensch", "location": "Tyrell Corp"}
miranda_tyrell = {"name": "Miranda Tyrell", "race": "Replikant", "location": "Tyrell Corp"}
NPC_Dicts = (
    eldon_tyrell,
    miranda_tyrell,

)

for char in NPC_Dicts:
    name = char.get("name").lower()
    name = name.replace(" ","_")

