from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ZooTycoonWorld


"""
IDs:
    Research: 1-139 (non-continuous, theres a couple missing research ids)
    Awards and Donations: 140-174
    Easter Egg Unlocks: 175+176
    Scenario Objectives: 177-???
"""

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
# RESEARCH: Endagered Animals
    "Research: Lowland Gorilla": 1,
    "Research: Black Leopard": 2,
    "Research: White Bengal Tiger": 3,
    "Research: Snow Leopard": 4,
    "Research: Giant Panda": 5,
    "Research: Okapi": 6,
# RESEARCH: Exhibit Foliage
    "Thorn Acacia Tree": 7,
    "Llala Palm Tree": 8,
    "Bamboo Stand": 9,
    "Acacia Caffra Tree": 10,
    "Globe Willow Tree": 11,
# RESEARCH: Animal Shelters
    "Rock Cave 1": 15,
    "Snowy Rock Cave": 16,
    "Panda Cave": 54,
    "Elephant House? (Elehous2)": 55,
    "Giraffe House? (Girhous2)": 56,
    "Leanto3": 58,
    "Conhous3": 59,
    "Wodhous3": 61,
    "Stable3": 62,
    "Burrow3": 63,
# RESEARCH: Animal Houses
    "Reptile House": 18,
    "Aviary": 19,
    "Primate House": 20,
    "Insect House": 44,
    "Primate House 1: Primates of Southeast Asia": 38,
    "Aviary 1: Birds of Africa": 39,
    "Reptile House 2: Deadly Snakes of the World": 40,
    "Aviary 2: Raptors of the World": 41,
    "Primate House 2: Lemurs of Madagascar": 42,
    "Insect House 2: Venomous Spiders": 43,
    "Primate House 3: Endangered Primates of the World": 45,
    "Aviary 3: Birds of the Tropical Rainforest": 46,
    "Reptile House 1: Reptiles of the Rainforest": 47,
    "Insect House 1: Scorpions of Africa": 48,
# RESEARCH: Staff Education
    "Zookeeper Training 1": 21,
    "Maintenance Worker Training 1": 22,
    "Zookeeper Training 2": 23,
    "Tour Guide Training": 24,
    "Maintenance Worker Training 2": 26,
# RESEARCH: Animal Care
    "Nutritional Food": 27,
    "Increased Reproduction Chance": 28,
    "Reduced Food Costs": 29,
    "Animal Antibiotics": 30,
# RESEARCH: Animal Enrichment
    "Lion Climbing Rock": 32,
    "Swinging Log Toy": 33,
    "Gorilla Climbing Bars": 34,
    "Cat Climbing Tree": 35,
    "Large Chimpanzee Bars": 36,
# RESEARCH: Panda Care
    "Panda Enrichment": 49,
    "Panda Fertility": 50,
    "Panda Innoculations": 51,
# RESEARCH: Dino Houses
    "Pteranodon House": 65,
    "Lepospondyl House": 66,
    "Pteranodon House 1: Pterodactylus of the late Jurassic": 67,
    "Pteranodon House 2: Ramphorhyncus of the late Jurassic": 68,
    "Pteranodon House 3: Dimorphodon of the early Jurassic": 69,
    "Lepospondyl House 1: Triadobatrachus of the Triassic": 70,
    "Lepospondyl House 2: Karaurus of the Jurassic": 71,
    "Lepospondyl House 3: Diplocaulus of the Permian": 72,
# RESEARCH: Dino Care
    "Nutritional Food: Dino": 73,
    "Reduced Food Costs: Dino": 74,
    "Dinosaur Antibiotics": 75,
    "Dinosaur Longevity": 76,
# RESEARCH: T-Rex Care
    "T-Rex Enrichment": 77,
    "T-Rex Innoculations": 78,
    "T-Rex Temperament Adjustment": 79,
# RESEARCH: Genetic Research
    "Research: T-Rex": 80,
    "Research: Spinosaurus": 81,
    "Research: Kentrosaurus": 83,
    "Research: Wooly Mammoth": 84,
    "Research: Plesiosaur": 85,
    "Research: Velociraptor": 86,
    "Research: Ankylosaurus": 87,
    "Research: Coelophysis": 88,
    "Research: Apatosaurus": 89,
# RESEARCH: Dinosaur Foliage
    "Monkey Puzzle Tree": 90,
    "Cycad": 91,
    "Glossopteris": 92,
    "Club Moss Shrub": 93,
    "Horsetail": 94,
    "Bald Cypress": 95,
    "Dawn Redwood": 96,
    "Norfolk Island Pine": 97,
    "Arctic Birch": 98,
# RESEARCH: Staff Education (Dino)
    "Scientist Training 1": 99,
    "Scientist Training 2": 100,
    "Scientist Training 3": 101,
# RESEARCH: Staff Education (Marine)
    "Maintenance Worker 3": 126,
    "Kayak Rental Shack": 133,
    "Swan Boat Rental Shack": 134,
    "Paddle Boat Rental Shack": 135,
# RESEARCH: Orca Tricks
    "Orca Back Swim": 102,
    "Orca Back Breach": 103,
# RESEARCH: Great White Shark Tricks
    "Great White Shark Air Jump": 105,
# RESEARCH: Bottlenose Dolphin Tricks
    "Bottlenose Dolphin Water Ring": 106,
    "Bottlenose Dolphin Belly Flop": 107,
    "Bottlenose Dolphin Surface Spin": 138,
    "Bottlenose Dolphin Wave to Crowd": 139,
# RESEARCH: Aquatic Foliage
    "Sea Lettuce": 120,
    "Divercate Tree Coral": 121,
    "Sea Anemone": 122,
    "Sea Star": 123,
# RESEARCH: Aquatic Houses
    "Crustacean House": 108,
    "Tropical Fish Aquarium": 109,
    "Tropical Fish Aquarium 1: Clownfish Program": 110,
    "Tropical Fish Aquarium 2: Angelfish Program": 111,
    "Tropical Fish Aquarium 3: Sunfish Program": 112,
    "Crustacean House 1: Crayfish Program": 113,
    "Crustacean House 2: Rock Crab Program": 114,
    "Crustacean House 3: Maine Lobster Program": 115,
# RESEARCH: Aquatic Animals
    "Research: Narwhal": 116,
    "Research: Mako Shark": 117,
    "Research: Great White Shark": 118,
    "Research: Humpback Whale": 119,
# RESEARCH: Aquatic Animal Care
    "Aquatic Animal Antibiotics": 127,
    "Aquatic Animal Longevity": 128,
# RESEARCH: Marine Specialist Training
    "Marine Specialist Training 1": 124,
    "Marine Specialist Training 2": 125,
# RESEARCH: Aquatic Animal Rehabilitation
    "Manatee Cure": 129,
    "Beluga Cure": 130,
    "Walrus Cure": 131,
    "Humpback Cure": 132,
# RESEARCH: Southern Sea Otter Tricks
    "Southern Sea Otter Jump": 136,
    "Southern Sea Otter Surface Spin": 137,
# AWARDS
    "Best Zoo, Silver Trophy": 140,
    "Best Zoo, Gold Trophy": 141,
    "Diverse Species, Silver Plaque": 142,
    "Diverse Species, Gold Plaque": 143,
    "Excellence in Exhibit Design, Silver Plaque": 144,
    "Excellence in Exhibit Design, Gold Plaque": 145,
    "Highest Customer Satisfaction, Blue Ribbon": 146,
    "Highest Quality Exhibits, Silver Certificate": 147,
    "Highest Quality Exhibits, Gold Certificate": 148,
    "Most Popular Zoo, Silver Certificate": 149,
    "Most Popular Zoo, Gold Certificate": 150,
    "Quality Animal Care": 151,
    "Complete Ice Age Zoo": 152,
    "Complete Jurassic Zoo": 153,
    "Excellence in Dinosaur Exhibit Design": 154,
    "Outstanding Animal Health Plaque": 155,
    "Quality Dinosaur Care": 156,
    "Tyrannosaurus Rex Egg": 157,
    "Arctic Aquatic Care": 158,
    "Best Dolphin Show in the Country": 159,
    "Best Orca Show in the Country": 160,
    "Best Sea Lion Show in the Country": 161,
    "Best Sea Otter Show in the Country": 162,
    "Best Zoo in the World": 163,
    "Excellence in Arctic Conservation": 164,
    "Excellence in Savannah Exhibit Construction": 165,
    "Excellence in Shark Conservation": 166,
    "Excellence in Arctic Construction": 167,
    "Penguin Colony, Silver Plaque": 168,
    "Superior Whale Care, Gold Plaque": 169,
    "Zoo of the Year": 170,
# DONATIONS
    "Emergency Donation": 171,
    "Endangered Species Donation": 172,
    "Panda Donation": 173,
    "Great White Shark Donation": 174,
# EASTER EGGS
    "Xanadu": 175,
    "The Exhibit of Oz": 176,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ZooTycoonLocation(Location):
    game = "Zoo Tycoon"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ZooTycoonWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ZooTycoonWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    overworld = world.get_region("Overworld")
    top_left_room = world.get_region("Top Left Room")
    bottom_right_room = world.get_region("Bottom Right Room")
    right_room = world.get_region("Right Room")

    # One way to create locations is by just creating them directly via their constructor.
    bottom_left_chest = ZooTycoonLocation(
        world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    )

    # You can then add them to the region.
    overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    bottom_right_room_locations = get_location_names_with_ids(
        ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    )
    bottom_right_room.add_locations(bottom_right_room_locations, ZooTycoonLocation)

    top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    top_left_room.add_locations(top_left_room_locations, ZooTycoonLocation)

    right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    right_room.add_locations(right_room_locations, ZooTycoonLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, ZooTycoonLocation)
    else:
        overworld.add_locations(top_middle_room_locations, ZooTycoonLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, ZooTycoonLocation)


def create_events(world: ZooTycoonWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = ZooTycoonLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=ZooTycoonLocation, item_type=items.ZooTycoonItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
