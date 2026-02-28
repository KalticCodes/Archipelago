from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ZooTycoonWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: ZooTycoonWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ZooTycoonWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.

    research_endangered_animals = Region("Endangered Animals", world.player, world.multiworld)
    research_exhibit_foliage = Region("Exhibit Foliage", world.player, world.multiworld)
    research_animal_shelters = Region("Animal Shelters", world.player, world.multiworld)
    research_animal_houses = Region("Animal Houses", world.player, world.multiworld)
    research_staff_education = Region("Staff Education", world.player, world.multiworld)
    research_animal_care = Region("Animal Care", world.player, world.multiworld)
    research_animal_enrichment = Region("Animal Enrichment", world.player, world.multiworld)
    research_panda_care = Region("Panda Care", world.player, world.multiworld)
    research_dino_houses = Region("Dinosaur Houses", world.player, world.multiworld)
    research_dino_care = Region("Dinosaur Care", world.player, world.multiworld)
    research_trex_care = Region("T.Rex Care", world.player, world.multiworld)
    research_genetic_research = Region("Genetic Research", world.player, world.multiworld)
    research_dinosaur_foliage = Region("Dinosaur Foliage", world.player, world.multiworld)
    research_orca_tricks = Region("Orca Tricks", world.player, world.multiworld)
    research_shark_tricks = Region("Great White Shark Tricks", world.player, world.multiworld)
    research_dolphin_tricks = Region("Bottlenose Dolphin Tricks", world.player, world.multiworld)
    research_aquatic_foliage = Region("Aquatic Foliage", world.player, world.multiworld)
    research_aquatic_houses = Region("Aquatic Houses", world.player, world.multiworld)
    research_aquatic_animals = Region("Aquatic Animals", world.player, world.multiworld)
    research_aquatic_animal_care = Region("Aquatic Animal Care", world.player, world.multiworld)
    research_marine_specialist_training = Region("Marine Specialist Training", world.player, world.multiworld)
    research_aquatic_animal_rehab = Region("Aquatic Animal Rehabilitation", world.player, world.multiworld)
    research_sea_otter_tricks = Region("Southern Sea Otter Tricks", world.player, world.multiworld)

    awards_and_donations = Region("Awards and Donations", world.player, world.multiworld)

    tutorial_scenarios = Region("Tutorial Scenarios", world.player, world.multiworld)
    beginner_scenarios = Region("Beginner Scenarios", world.player, world.multiworld)
    intermediate_scenarios = Region("Intermediate Scenarios", world.player, world.multiworld)
    advanced_scenarios = Region("Advanced Scenarios", world.player, world.multiworld)
    very_advanced_scenarios = Region("Very Advanced Scenarios", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [
        tutorial_scenarios,
        beginner_scenarios,
        intermediate_scenarios,
        advanced_scenarios,
        very_advanced_scenarios,

        awards_and_donations,

        research_endangered_animals,
        research_exhibit_foliage,
        research_animal_shelters,
        research_animal_houses,
        research_staff_education,
        research_animal_care,
        research_animal_enrichment,
        research_panda_care,
        research_dino_houses,
        research_dino_care,
        research_trex_care,
        research_genetic_research,
        research_dinosaur_foliage,
        research_orca_tricks,
        research_shark_tricks,
        research_dolphin_tricks,
        research_aquatic_foliage,
        research_aquatic_houses,
        research_aquatic_animals,
        research_aquatic_animal_care,
        research_marine_specialist_training,
        research_aquatic_animal_rehab,
        research_sea_otter_tricks
    ]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
    #     top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #     regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: ZooTycoonWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    tutorial_scenarios = world.get_region("Tutorial Scenarios")
    beginner_scenarios = world.get_region("Beginner Scenarios")
    intermediate_scenarios = world.get_region("Intermediate Scenarios")
    advanced_scenarios = world.get_region("Advanced Scenarios")
    very_advanced_scenarios = world.get_region("Very Advanced Scenarios")

    # scenario_unlocked helper
    tutorial_scenarios.connect(beginner_scenarios)
    beginner_scenarios.connect(intermediate_scenarios, None, scenarioUnlocked("Intermediate"))
    intermediate_scenarios.connect(advanced_scenarios, None, scenarioUnlocked("Advanced"))
    advanced_scenarios.connect(very_advanced_scenarios, None, scenarioUnlocked("Very Advanced"))

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    # overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    # overworld.exits.append(overworld_to_bottom_right_room)

    # You can then connect the Entrance to the target region.
    # overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    # overworld.connect(right_room, "Overworld to Right Room")
    # right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    # overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     overworld.connect(top_middle_room, "Overworld to Top Middle Room")

    def scenarioUnlocked(scenario_type: str):
        return lambda state: state.has(scenario_type+" Scenario Unlock") if world.options.scenario_keys else None
