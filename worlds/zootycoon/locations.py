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
    
# ---------------- RESEARCH --------------------

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

# ---------------- AWARDS AND DONATIONS --------------------

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

# ------------------- SCENARIOS -------------------

# Tutorial 1
    "Tutorial 1 - Select Game Options": 177,
    "Tutorial 1 - Select Zoom Buttons": 178,
    "Tutorial 1 - Rotate Game World": 179,
    "Tutorial 1 - Pause and Resume": 180,
    "Tutorial 1 - Place Snack Machine": 181,
    "Tutorial 1 - Delete Lion Exhibit Fence": 182,
    "Tutorial 1 - Scenario Completion": 182,
# Tutorial 2
    "Tutorial 2 - Place Iron Bar Fence": 183,
    "Tutorial 2 - Adopt Bengal Tiger": 184,
    "Tutorial 2 - Hire Zookeeper": 185,
    "Tutorial 2 - Place 8 Concrete Path": 186,
    "Tutorial 2 - Purchase Burger Stand": 187,
    "Tutorial 2 - Purchase Drink Stand": 188,
    "Tutorial 2 - Scenario Completion": 189,
# Tutorial 3
    "Tutorial 3 - Place Savannah Grass Terrain": 190,
    "Tutorial 3 - Correct Jaguar Terrain": 191,
    "Tutorial 3 - Place Grass Trees": 192,
    "Tutorial 3 - Place Umbrella Thorn Trees": 193,
    "Tutorial 3 - Correct Jaguar Trees": 194,
    "Tutorial 3 - Lion Exhibit Suitability": 195,
    "Tutorial 3 - Scenario Completion": 196,
# Dino Tutorial 1
    "Dino Tutorial 1 - Filter Game Content": 197,
    "Dino Tutorial 1 - Construct Dino Exhibit": 198,
    "Dino Tutorial 1 - Place Allosaurus Egg": 199,
    "Dino Tutorial 1 - Hire Scientist": 200,
    "Dino Tutorial 1 - Sort Data by Profit": 201,
    "Dino Tutorial 1 - View Research and Conservation": 202,
    "Dino Tutorial 1 - Scenario Completion": 203,
# Marine Tutorial 1
    "Marine Tutorial 1 - Filter Game Content": 204,
    "Marine Tutorial 1 - Hire Marine Specialist": 205,
    "Marine Tutorial 1 - Build Dolphin Exhibit": 206,
    "Marine Tutorial 1 - Adopt Bottlenose Dolphin": 207,
    "Marine Tutorial 1 - Place Kelp Foliage": 208,
    "Marine Tutorial 1 - Purchase Tank Filter": 209,
    "Marine Tutorial 1 - Scenario Completion": 210,
# Marine Tutorial 2
    "Marine Tutorial 2 - View Show Animals": 211,
    "Marine Tutorial 2 - Adopt Orca": 212,
    "Marine Tutorial 2 - Build Orca Show Exhibit": 212,
    "Marine Tutorial 2 - Purchase Grandstands": 213,
    "Marine Tutorial 2 - Add a Trick to Orca Show": 214,
    "Marine Tutorial 2 - Change Show Frequency": 215,
    "Marine Tutorial 2 - Scenario Completion": 216,
# Marine Tutorial 3
    "Marine Tutorial 3 - Complete Land Exhibit": 217,
    "Marine Tutorial 3 - Lower Walrus Tank": 218,
    "Marine Tutorial 3 - Hire Zookeeper": 219,
    "Marine Tutorial 3 - Lower Show Gate": 220,
    "Marine Tutorial 4 - Scenario Completion": 221,
# Scenario 1 - Small Zoo (Beginner)
    "Scenario 1 (Small Zoo) - Exhibit Suitability Rating": 222,
    "Scenario 1 (Small Zoo) - Animal Happiness": 223,
    "Scenario 1 (Small Zoo) - Scenario Completion": 224,
# Scenario 2 - Seasideville Zoo (Beginner)
    "Scenario 2 (Seasideville Zoo) - Exhibit Suitability Rating": 225,
    "Scenario 2 (Seasideville Zoo) - Animal Happiness": 226,
    "Scenario 2 (Seasideville Zoo) - Guest Happiness": 227,
    "Scenario 2 (Seasideville Zoo) - Scenario Completion": 228,
# Scenario 3 - Forest Zoo (Beginner)
    "Scenario 3 (Forest Zoo) - Exhibit Suitability Rating": 229,
    "Scenario 3 (Forest Zoo) - Animal Happiness": 230,
    "Scenario 3 (Forest Zoo) - Zoo Rating": 231,
    "Scenario 3 (Forest Zoo) - Scenario Completion": 232,
# Scenario 4 - Holiday Tree Farm (Beginner)
    "Scenario 4 (Holiday Tree Farm) - Zoo Rating": 233,
    "Scenario 4 (Holiday Tree Farm) - Animal Happiness": 234,
    "Scenario 4 (Holiday Tree Farm) - Moose Exhibit Suitability Rating": 235,
    "Scenario 4 (Holiday Tree Farm) - Arctic Wolf Exhibit Suitability Rating": 236,
    "Scenario 4 (Holiday Tree Farm) - Grizzly Bear Exhibit Suitability Rating": 237,
    "Scenario 4 (Holiday Tree Farm) - Scenario Completion": 238,
# Scenario 5 - Ice Age Animal Zoo (Beginner)
    "Scenario 5 (Ice Age Animal Zoo) - Adopt Giant Tortoise": 239,
    "Scenario 5 (Ice Age Animal Zoo) - Adopt Saber-Toothed Cat": 240,
    "Scenario 5 (Ice Age Animal Zoo) - Adopt Wooly Rhino": 241,
    "Scenario 5 (Ice Age Animal Zoo) - Adopt Wooly Mammoth": 242,
    "Scenario 5 (Ice Age Animal Zoo) - Exhibit Suitability Rating": 243,
    "Scenario 5 (Ice Age Animal Zoo) - Animal Happiness": 244,
    "Scenario 5 (Ice Age Animal Zoo) - Scenario Completion": 245,
# Scenario 6 - Orca Show (Beginner)
    "Scenario 6 (Orca Show) - Exhibit Suitability": 246,
    "Scenario 6 (Orca Show) - Profit": 247,
    "Scenario 6 (Orca Show) - Guest Count": 248,
    "Scenario 6 (Orca Show) - Scenario Completion": 249,
# Scenario 7 - Seasideville Dolphin Park (Beginner)
    "Scenario 7 (Seasideville Dolphin Park) - Exhibit Suitability Rating": 250,
    "Scenario 7 (Seasideville Dolphin Park) - Marine Animal Count": 251,
    "Scenario 7 (Seasideville Dolphin Park) - Animal Happiness": 252,
    "Scenario 7 (Seasideville Dolphin Park) - Guest Happiness": 253,
    "Scenario 7 (Seasideville Dolphin Park) - Total Profit": 254,
    "Scenario 7 (Seasideville Dolphin Park) - Scenario Completion": 255,
# Scenario 8 - Shark World (Beginner)
    "Scenario 8 (Shark World) - Hammerhead Shark Exhibit": 256,
    "Scenario 8 (Shark World) - Hammerhead Shark Exhibit Suitability": 257,
    "Scenario 8 (Shark World) - Mako Shark Exhibit": 258,
    "Scenario 8 (Shark World) - Shortfin Mako Shark Exhibit Suitability": 259,
    "Scenario 8 (Shark World) - Tiger Shark Exhibit": 260,
    "Scenario 8 (Shark World) - Tiger Shark Exhibit Suitability": 261,
    "Scenario 8 (Shark World) - Great White Shark Exhibit": 262,
    "Scenario 8 (Shark World) - Great White Shark Exhibit Suitability": 263,
    "Scenario 8 (Shark World) - Guest Count": 264,
    "Scenario 8 (Shark World) - Scenario Completion": 265,
# Scenario 9 - Surf and Turf Zoo (Beginner)
    "Scenario 9 (Surf and Turf Zoo) - Zoo Rating": 266,
    "Scenario 9 (Surf and Turf Zoo) - Exhibit Suitability Rating": 267,
    "Scenario 9 (Surf and Turf Zoo) - Zoo Animal Count": 268,
    "Scenario 9 (Surf and Turf Zoo) - Marine Animal Count": 269,
    "Scenario 9 (Surf and Turf Zoo) - Scenario Completion": 270,
# Scenario 10 - Revitalize Burkitsville Zoo (Intermediate)
    "Scenario 10 (Revitalize Burkitsville Zoo) - Zoo Rating": 271,
    "Scenario 10 (Revitalize Burkitsville Zoo) - Animal Happiness": 272,
    "Scenario 10 (Revitalize Burkitsville Zoo) - Animal Species Count": 273,
    "Scenario 10 (Revitalize Burkitsville Zoo)- Scenario Completion": 274,
# Scenario 11 - Inner City Zoo (Intermediate)
    "Scenario 11 (Inner City Zoo) - Zoo Rating": 275,
    "Scenario 11 (Inner City Zoo) - Guest Happiness": 276,
    "Scenario 11 (Inner City Zoo) - Animal Happiness": 277,
    "Scenario 11 (Inner City Zoo) - Animal Species Count": 278,
    "Scenario 11 (Inner City Zoo) - Scenario Completion": 279,
# Scenario 12 - Saving the Great Cats (Intermediate)
    "Scenario 12 (Saving the Great Cats) - Adopt Lions": 280,
    "Scenario 12 (Saving the Great Cats) - Adopt Bengal Tigers": 281,
    "Scenario 12 (Saving the Great Cats) - Adopt White Bengal Tigers": 282,
    "Scenario 12 (Saving the Great Cats) - Adopt Siberian Tigers": 283,
    "Scenario 12 (Saving the Great Cats) - Adopt Leopards": 284,
    "Scenario 12 (Saving the Great Cats) - Adopt Black Leopards": 285,
    "Scenario 12 (Saving the Great Cats) - Adopt Snow Leopards": 286,
    "Scenario 12 (Saving the Great Cats) - Adopt Clouded Leopards": 287,
    "Scenario 12 (Saving the Great Cats) - Adopt Cheetahs": 288,
    "Scenario 12 (Saving the Great Cats) - Adopt Jaguars": 289,
    "Scenario 12 (Saving the Great Cats) - Exhibit Suitability": 290,
    "Scenario 12 (Saving the Great Cats) - Animal Happiness": 291,
    "Scenario 12 (Saving the Great Cats) - Scenario Completion": 292,
# Scenario 13 - Endangered Species Zoo (Intermediate)
    "Scenario 13 (Endangered Species Zoo) - Exhibit Suitability": 293,
    "Scenario 13 (Endangered Species Zoo) - Zoo Rating": 294,
    "Scenario 13 (Endangered Species Zoo) - Guest Happiness": 295,
    "Scenario 13 (Endangered Species Zoo) - Animal Happiness": 296,
    "Scenario 13 (Endangered Species Zoo) - Baby Black Leopard": 297,
    "Scenario 13 (Endangered Species Zoo) - Baby Okapi": 298,
    "Scenario 13 (Endangered Species Zoo) - Baby White Bengal Tiger": 299,
    "Scenario 13 (Endangered Species Zoo) - Scenario Completion": 300,
# Scenario 14 - Arctic Zoo (Intermediate)
    "Scenario 14 (Arctic Zoo) - Exhibit Suitability": 301,
    "Scenario 14 (Arctic Zoo) - Animal Happiness": 302,
    "Scenario 14 (Arctic Zoo) - Scenario Completion": 303,
# Scenario 15 - Beach Resort Zoo (Intermediate)
    "Scenario 15 (Beach Resort Zoo) - Zoo Rating": 304,
    "Scenario 15 (Beach Resort Zoo) - Animal Happiness": 305,
    "Scenario 15 (Beach Resort Zoo) - Exhibit Suitability": 306,
    "Scenario 15 (Beach Resort Zoo) - Arctic Animals": 307,
    "Scenario 15 (Beach Resort Zoo) - Australian Animals": 308,
    "Scenario 15 (Beach Resort Zoo) - South American Animals": 309,
    "Scenario 15 (Beach Resort Zoo) - North American Animals": 310,
    "Scenario 15 (Beach Resort Zoo) - Southeast Asian Animals": 311,
    "Scenario 15 (Beach Resort Zoo) - North African Desert Animals": 312,
    "Scenario 15 (Beach Resort Zoo) - African Savannah Animals": 313,
    "Scenario 15 (Beach Resort Zoo) - Scenario Completion": 314,
# Scenario 16 - Valley of the Dinosaurs (Intermediate)
    "Scenario 16 (Valley of the Dinosaurs) - Zoo Rating": 315,
    "Scenario 16 (Valley of the Dinosaurs) - Animal Happiness": 316,
    "Scenario 16 (Valley of the Dinosaurs) - Prehistoric Animals": 317,
    "Scenario 16 (Valley of the Dinosaurs) - Exhibit Suitability": 318,
    "Scenario 16 (Valley of the Dinosaurs) - Scenario Completion": 319,
# Scenario 17 - Jurassic Zoo (Intermediate)
    "Scenario 17 (Jurassic Zoo) - Zoo Rating": 320,
    "Scenario 17 (Jurassic Zoo) - Animal Happiness": 321,
    "Scenario 17 (Jurassic Zoo) - Exhibit Suitability": 322,
    "Scenario 17 (Jurassic Zoo) - Adopt Allosaurus": 323,
    "Scenario 17 (Jurassic Zoo) - Adopt Camptosaurus": 324,
    "Scenario 17 (Jurassic Zoo) - Adopt Caudipteryx": 325,
    "Scenario 17 (Jurassic Zoo) - Adopt Kentrosaurus": 326,
    "Scenario 17 (Jurassic Zoo) - Adopt Plesiosaurus": 327,
    "Scenario 17 (Jurassic Zoo) - Adopt Stegosaurus": 328,
    "Scenario 17 (Jurassic Zoo) - Adopt Apatosaurus": 329,
    "Scenario 17 (Jurassic Zoo) - Scenario Completion": 330,
# Scenario 18 - Oceans of the World (Intermediate)
    "Scenario 18 (Oceans of the World) - Zoo Rating": 331,
    "Scenario 18 (Oceans of the World) - Animal Happiness": 332,
    "Scenario 18 (Oceans of the World) - Exhibit Suitability": 333,
    "Scenario 18 (Oceans of the World) - Animal Species Count": 334,
    "Scenario 18 (Oceans of the World) - Arctic Ocean Animals": 335,
    "Scenario 18 (Oceans of the World) - Tropical Ocean Animals": 336,
    "Scenario 18 (Oceans of the World) - Pacific Ocean Animals": 337,
    "Scenario 18 (Oceans of the World) - Atlantic Ocean Animals": 338,
    "Scenario 18 (Oceans of the World) - Scenario Completion": 339,
# Scenario 19 - Save the Marine Animals (Intermediate)
    "Scenario 19 (Save the Marine Animals) - West Indian Manatee Exhibit Suitability": 340,
    "Scenario 19 (Save the Marine Animals) - Research Sea Mammal Rescue": 341,
    "Scenario 19 (Save the Marine Animals) - Beluga Exhibit Suitability": 342,
    "Scenario 19 (Save the Marine Animals) - Research Beluga Care": 343,
    "Scenario 19 (Save the Marine Animals) - Manta Ray Exhibit Suitability": 344,
    "Scenario 19 (Save the Marine Animals) - Research Oil Exposure": 345,
    "Scenario 19 (Save the Marine Animals) - Humpback Whale Exhibit Suitability": 346,
    "Scenario 19 (Save the Marine Animals) - Research Baby Humpback Whale Care": 347,
    "Scenario 19 (Save the Marine Animals) - Exhibit Suitability": 348,
    "Scenario 19 (Save the Marine Animals) - Scenario Completion": 349,
# Scenario 20 - Free Admission (Intermediate)
    "Scenario 20 (Free Admission) - Net Income": 350,
    "Scenario 20 (Free Admission) - Zoo Animal Count": 351,
    "Scenario 20 (Free Admission) - Marine Animal Count": 352,
    "Scenario 20 (Free Admission) - Animal Species Count": 353,
    "Scenario 20 (Free Admission) - Exhibit Suitability": 354,
    "Scenario 20 (Free Admission) - Scenario Completion": 355,
# Scenario 21 - Aquatic Show Park (Intermediate)
    "Scenario 21 (Aquatic Show Park) - Orca Show Profit": 356,
    "Scenario 21 (Aquatic Show Park) - Bottlenose Dolphin Profit": 357,
    "Scenario 21 (Aquatic Show Park) - California Sea Lion Profit": 358,
    "Scenario 21 (Aquatic Show Park) - Southern Sea Otter Profit": 359,
    "Scenario 21 (Aquatic Show Park) - Animal Species Count": 360,
    "Scenario 21 (Aquatic Show Park) - Exhibit Suitability": 361,
    "Scenario 21 (Aquatic Show Park) - Animal Happiness": 362,
    "Scenario 21 (Aquatic Show Park) - Guest Happiness": 363,
    "Scenario 21 (Aquatic Show Park) - Scenario Completion": 364,
# Scenario 22 - Carnivore Zoo (Intermediate)
    "Scenario 22 (Carnivore Zoo) - First Shipment Exhibit Suitability": 365,
    "Scenario 22 (Carnivore Zoo) - Second Shipment Exhibit Suitability": 366,
    "Scenario 22 (Carnivore Zoo) - T-Rex Exhibit Suitability": 367,
    "Scenario 22 (Carnivore Zoo) - Scenario Completion": 368,
# Scenario 23 - Southeast Asia Zoo (Intermediate)
    "Scenario 23 (Southeast Asia Zoo) - Adopt Orangutans": 369,
    "Scenario 23 (Southeast Asia Zoo) - Adopt Jana Rhinoceroses": 370,
    "Scenario 23 (Southeast Asia Zoo) - Adopt Malaysian Tapir": 371,
    "Scenario 23 (Southeast Asia Zoo) - Non-Empty Exhibit Count": 372,
    "Scenario 23 (Southeast Asia Zoo) - Exhibit Suitability": 373,
    "Scenario 23 (Southeast Asia Zoo) - Southeast Asian Animal Count": 374,
    "Scenario 23 (Southeast Asia Zoo) - Zoo Rating": 375,
    "Scenario 23 (Southeast Asia Zoo) - Scenario Completion": 376,
# Scenario 24 - Island Zoo (Advanced)
    "Scenario 24 (Island Zoo) - Guest Happiness": 377,
    "Scenario 24 (Island Zoo) - Zoo Rating": 378,
    "Scenario 24 (Island Zoo) - Animal Happiness": 379,
    "Scenario 24 (Island Zoo) - Exhibit Suitability": 380,
    "Scenario 24 (Island Zoo) - Scenario Completion": 381,
# Scenario 25 - African Savannah Zoo (Advanced)
    "Scenario 25 (African Savannah Zoo) - African Savannah Animal Count": 382,
    "Scenario 25 (African Savannah Zoo) - Exhibit Suitability": 383,
    "Scenario 25 (African Savannah Zoo) - Animal Happiness": 384,
    "Scenario 25 (African Savannah Zoo) - Guest Happiness": 385,
    "Scenario 25 (African Savannah Zoo) - Zoo Rating": 386,
    "Scenario 25 (African Savannah Zoo) - Scenario Completion": 387,
# Scenario 26 - Mountain Zoo (Advanced)
    "Scenario 26 (Mountain Zoo) - Animal Species Count": 388,
    "Scenario 26 (Mountain Zoo) - Exhibit Suitability": 389,
    "Scenario 26 (Mountain Zoo) - Animal Happiness": 390,
    "Scenario 26 (Mountain Zoo) - Zoo Rating": 391,
    "Scenario 26 (Mountain Zoo) - Scenario Completion": 392,
# Scenario 27 - Tropical Rainforest Zoo (Advanced)
    "Scenario 27 (Tropical Rainforest Zoo) - Animal Species Count": 393,
    "Scenario 27 (Tropical Rainforest Zoo) - Animal Happiness": 394,
    "Scenario 27 (Tropical Rainforest Zoo) - Exhibit Suitability": 395,
    "Scenario 27 (Tropical Rainforest Zoo) - Zoo Rating": 396,
    "Scenario 27 (Tropical Rainforest Zoo) - Guest Happiness": 397,
    "Scenario 27 (Tropical Rainforest Zoo) - Scenario Completion": 398,
# Scenario 28 - Dinosaur Island Research Lab (Advanced)
    "Scenario 28 (Dinosaur Island Research Lab) - Zoo Rating": 399,
    "Scenario 28 (Dinosaur Island Research Lab) - Zoo Value": 400,
    "Scenario 28 (Dinosaur Island Research Lab) - Exhibit Suitability": 401,
    "Scenario 28 (Dinosaur Island Research Lab) - Scenario Completion": 402,
# Scenario 29 - Marine Conservation (Advanced)
    "Scenario 29 (Marine Conservation) - Animal Happiness": 403,
    "Scenario 29 (Marine Conservation) - Exhibit Suitability": 404,
    "Scenario 29 (Marine Conservation) - Guest Happiness": 405,
    "Scenario 29 (Marine Conservation) - Zoo Value": 406,
    "Scenario 29 (Marine Conservation) - Zoo Rating": 407,
    "Scenario 29 (Marine Conservation) - Scenario Completion": 408,
# Scenario 30 - Save the Zoo (Advanced)
    "Scenario 30 (Save the Zoo) - Initial Animal Exhibit Suitability": 409,
    "Scenario 30 (Save the Zoo) - Initial Animal Happiness": 410,
    "Scenario 30 (Save the Zoo) - Exhibit Suitability": 411,
    "Scenario 30 (Save the Zoo) - Guest Happiness": 412,
    "Scenario 30 (Save the Zoo) - Orca Show Profit": 413,
    "Scenario 30 (Save the Zoo) - Scenario Completion": 414,
# Scenario 31 - Conservation Zoo (Advanced)
    "Scenario 31 (Conservation Zoo) - Animal Happiness": 415,
    "Scenario 31 (Conservation Zoo) - Non-Empty Exhibit Count": 416,
    "Scenario 31 (Conservation Zoo) - Exhibit Suitability": 417,
    "Scenario 31 (Conservation Zoo) - Scenario Completion": 418,
# Scenario 32 - Paradise Island (Very Advanced)
    "Scenario 32 (Paradise Island) - Zoo Rating": 419,
    "Scenario 32 (Paradise Island) - Guest Happiness": 420,
    "Scenario 32 (Paradise Island) - Animal Happiness": 421,
    "Scenario 32 (Paradise Island) - Exhibit Suitability": 422,
    "Scenario 32 (Paradise Island) - Scenario Completion": 423,
# Scenario 33 - Breeding Giant Pandas (Very Advanced)
    "Scenario 33 (Breeding Giant Pandas) - Baby Giant Panda": 424,
    "Scenario 33 (Breeding Giant Pandas) - Exhibit Suitability": 425,
    "Scenario 33 (Breeding Giant Pandas) - Scenario Completion": 426,
# Scenario 32 - Return to Dinosaur Island Research Lab (Very Advanced)
    "Scenario 34 (Return to Dinosaur Island Research Lab) - Zoo Rating": 419,
    "Scenario 34 (Return to Dinosaur Island Research Lab) - Guest Happiness": 420,
    "Scenario 34 (Return to Dinosaur Island Research Lab) - All Dinosaurs": 421,
    "Scenario 34 (Return to Dinosaur Island Research Lab) - Exhibit Suitability": 422,
    "Scenario 34 (Return to Dinosaur Island Research Lab) - Scenario Completion": 423,
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
