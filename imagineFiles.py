from QScore import *

penguinFile = """Penguins are flightless birds uniquely adapted to life in the water. Their tuxedo-like plumage helps camouflage them from predators, and they use their wings as flippers to swim at high speeds. Most species live in the Southern Hemisphere, enduring harsh, freezing conditions."""
batmanFile = """Batman is Gotham City's brooding vigilante, operating from the shadows to fight crime. Unlike many superheroes, Bruce Wayne possesses no superhuman abilities, relying instead on his intellect, martial arts mastery, and vast wealth to fund his high-tech gadgets. His ultimate goal is to rid his city of corruption."""
doritosFile = """Doritos are a popular brand of seasoned tortilla chips known for their intense flavors and crunchy texture. The classic Nacho Cheese and Cool Ranch varieties are staple snacks at parties and gaming sessions. They are recognizable by their distinctive triangular shape and the heavy coating of flavor dust."""
spaceFile = """The airlock hissed shut, leaving nothing but the sound of my own breathing inside the helmet. Earth was a tiny blue marble hanging in the endless black void, beautiful but terrifyingly distant. I pushed off the hull, tethered only by a single braided wire."""
pizzaFile = """Pizza is a globally beloved dish originating from Italy, typically consisting of a round, flat dough base baked with tomato sauce and cheese. Additional toppings can range from pepperoni and mushrooms to more controversial choices like pineapple. It is a highly customizable and convenient comfort food."""
pikachuFile = """Pikachu is the iconic electric-type Pokémon and the official mascot of the Pokémon franchise. Recognizable by its yellow fur, pointy ears, and lightning-bolt tail, it stores electrical energy in its red cheeks. Its adorable "pika-pika" cry has made it a global pop culture phenomenon."""
legoFile = """Lego bricks are interlocking plastic building toys that have sparked creativity in children and adults for decades. The patented tube-and-stud design allows the pieces to snap together securely, enabling the construction of everything from simple houses to complex, motorized mechanical models."""
mysteryFile = """The detective adjusted his fedora and knelt beside the shattered antique vase. A single red rose lay untouched amidst the ceramic shards, leaving a deliberate message. Whoever broke in wasn't looking for money; they were looking for revenge."""
blackHoleFile = """Black holes are regions of spacetime where gravity is so intense that nothing, not even light, can escape their pull. They are typically formed from the collapsed remnants of massive stars. At their center lies a singularity, a point where current laws of physics break down."""
titanicFile = """The RMS Titanic was a British passenger liner celebrated as an unsinkable marvel of modern engineering. Tragically, it sank during its maiden voyage in 1912 after striking an iceberg in the North Atlantic. The disaster resulted in massive loss of life and forever changed maritime safety regulations."""
iphoneFile = """The iPhone is a line of smartphones designed and marketed by Apple, credited with revolutionizing the mobile device industry. Featuring a sleek touchscreen interface, a robust app ecosystem, and advanced camera technology, it serves as a pocket-sized computer for millions of users worldwide."""
dragonFile = """The beast awoke with a rumble that shook the cavern walls, sending cascades of gold coins spilling down the hoard. Smoke curled lazily from its nostrils as one massive, reptilian eye snapped open. It knew instantly that a thief had breached its sanctuary."""
coffeeFile = """Coffee is a brewed beverage prepared from roasted coffee beans, the seeds of berries from certain Coffea species. Consumed globally for its stimulating caffeine content, it can be served hot or iced in countless variations, from a simple black drip to elaborate espresso-based drinks like lattes and cappuccinos."""
sherlockFile = """Sherlock Holmes is a legendary fictional detective created by British author Sir Arthur Conan Doyle. Operating out of 221B Baker Street, Holmes is renowned for his astute logical reasoning, ability to adopt almost any disguise, and his use of forensic science to solve difficult cases."""
volcanoFile = """Volcanoes are ruptures in the crust of a planetary-mass object that allow hot lava, volcanic ash, and gases to escape from a magma chamber below the surface. While their eruptions can be wildly destructive, they also create new landmasses and contribute to nutrient-rich soils."""
nikeFile = """Nike is a multinational corporation recognized worldwide for its athletic footwear, apparel, and equipment. Famous for the "Swoosh" logo and the "Just Do It" slogan, the brand sponsors many high-profile athletes and sports teams, heavily influencing modern streetwear and sneaker culture."""
cyberpunkFile = """Neon lights reflected off the rain-slicked pavement of Neo-Tokyo, casting long, distorted shadows. A hover-cab zoomed past, splashing synthetic water onto my cybernetic boots. I checked the datapad hidden in my trench coat; the target was supposed to be at the noodle stand by midnight."""
sunflowerFile = """Sunflowers are tall, vibrant plants known for their large yellow blooms that resemble the sun. A fascinating trait of young sunflowers is heliotropism, where their flower heads actively track the sun's movement across the sky from east to west throughout the day."""
marioFile = """Mario is a mustached Italian plumber who serves as the titular protagonist of Nintendo's massive video game franchise. Usually clad in a red cap and blue overalls, he frequently embarks on quests through the Mushroom Kingdom to rescue Princess Peach from the villainous Bowser."""
guitarFile = """The acoustic guitar is a fretted musical instrument that produces sound by plucking or strumming its strings, which resonate through a hollow wooden body. It is a versatile instrument foundational to many genres, including folk, country, blues, and pop music."""
cowFile = """Cows are gentle farm animals raised for milk, meat, and leather. They chew cud, have four-part stomachs that help digest grass, and often live in herds. Their calm nature and familiar moo make them beloved animals around the world."""
darthVaderFile = """Darth Vader is the feared Sith Lord and enforcer of the Galactic Empire in Star Wars. Once the Jedi Anakin Skywalker, he fell to the dark side and became a powerful opponent of the Rebel Alliance. His story takes a surprising turn when he ultimately rejects the Emperor to save his son, Luke."""
monsterFile = """Monster Energy drinks are caffeinated beverages sold in a variety of flavors and styles, including sugar-free options. Many versions contain caffeine, B vitamins, and other ingredients such as taurine; the caffeine and sugar amounts vary by product, so check the can’s label"""
scaryFile = """The old house creaked in the wind, though no one had lived there for years. Then, from upstairs, came the sound of slow footsteps—and a whisper calling my name."""


listOfFiles = [
    ["monster.txt", model.encode(monsterFile), 0],
    ["cow.txt", model.encode(cowFile), 0],
    ["darth.txt", model.encode(darthVaderFile), 0],
    ["scary.txt", model.encode(scaryFile), 0],
    ["penguin.txt", model.encode(penguinFile), 0],
    ["batman.txt", model.encode(batmanFile), 0],
    ["doritos.txt", model.encode(doritosFile), 0],
    ["space.txt", model.encode(spaceFile), 0],
    ["pizza.txt", model.encode(pizzaFile), 0],
    ["guitar.txt", model.encode(guitarFile), 0]
] 




# Sorts the list of files by score
def sortList(request, shots=256, qubits=12):
    kingOfHillScore = 0
    kingOfHillFilename = ""
    for i in range(len(listOfFiles)):
        listOfFiles[i][2] = calcScore(request=request, docVector=listOfFiles[i][1], shots=shots, qubits=qubits)
        if listOfFiles[i][2] >= kingOfHillScore:
            kingOfHillFilename = listOfFiles[i][0]
            kingOfHillScore = listOfFiles[i][2]
    return sorted(listOfFiles, key=lambda x: x[2], reverse=True)
