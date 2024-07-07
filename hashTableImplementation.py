import numpy as np

class Node:
    def __init__(self, name: str, tip_list: list):
        self.name = name
        self.next = None
        self.items = tip_list

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, name: str, tip_list: list):
        new_node = Node(name, tip_list)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        new_node.next = last_node
        self.head = new_node

class HashTable:
    def __init__(self, max_key_range: int):
        self.list = np.full((4, 4, max_key_range), None)
        self.max_key_range = max_key_range

    def add(self, weather: int, heat_index: int, name: str, tip_list: list):
        reduced_name = name[:2] + name[-1]
        key_index = hash(reduced_name) % self.max_key_range
        if self.list[weather][heat_index][key_index]:
            print(f"Collision Detected: {weather}, {heat_index}, {key_index}:  '{name}'")
        else:
            self.list[weather][heat_index][key_index] = LinkedList()
            
        self.list[weather][heat_index][key_index].add(name, tip_list)
    
    def access(self, weather: int, heat_index: int, name: str):
        reduced_name = name[:2] + name[-1]
        key_index = hash(reduced_name) % self.max_key_range
        pointer = self.list[weather][heat_index][key_index].head
        while pointer:
            if pointer.name == name:
                return pointer.items
            pointer = pointer.next

PET_CARE_TIP = HashTable(50)

PET_CARE_TIP.add(0, 0, "cat", [
    'Set up a comfy perch near a window where your cat can enjoy basking in the warm sunshine and watching birds or outdoor activity.',
    'Engage your cat in interactive play with toys like feather wands or laser pointers to keep them active and entertained indoors.',  
    'Catnip Fun: Sprinkle some catnip on scratching posts or toys to encourage healthy scratching behavior and provide mental stimulation.',
    'Climbing Structures: Provide climbing structures like cat trees or shelves for your cat to explore and climb vertically, mimicking their natural instincts.',
    'Food Puzzles: Challenge your cat with food puzzles that dispense treats as they solve them. This provides mental enrichment and keeps them occupied.'
])

PET_CARE_TIP.add(0, 0, "dog", [
    'Schedule walks during cooler hours (early morning or late evening) to avoid the hottest part of the day. Keep walks shorter and focus on shaded areas.',
    'Take a walk with a portable water bowl and frequently offer your dog cool, fresh water to stay hydrated. Consider a cooling vest for extra protection.',  
    'Set up a sprinkler in your backyard for a refreshing play session. This allows your dog to cool down while having fun in a controlled environment.',
    'Prepare dog-safe frozen treats like frozen Kongs filled with yogurt or broth to provide a cool and hydrating snack.',
    'Practice your dogs to socialize with other pets to lessen their fear and aggression in the outside world.'
])

PET_CARE_TIP.add(0, 1, "cat", [
    'Hydration Station: Place multiple water bowls with fresh, cool water around the house to encourage your cat to drink and stay hydrated.',
    'Cooling Mats: Provide cooling mats made for pets in shaded areas where your cat can lie down and cool off.',
    'Minimize Sun Exposure: Keep curtains or blinds closed in rooms with excessive sunlight to create cooler areas for your cat to rest.',
    'Grooming: Brush your cat regularly to remove excess fur that can trap heat and make them uncomfortable.',
    'Wet Wipes: For short-haired cats, consider using pet-safe wet wipes to gently wipe down their fur and help them cool down.'
])

PET_CARE_TIP.add(0, 1, "dog", [
    'Play fetch or engage in indoor games that provide exercise without excessive heat exposure.',
    'Spread dog-safe treats like mashed fruits or yogurt on a lick mat to keep your dog occupied and cool them down through licking.',
    'Provide a cooling pad for your dog to lie on and help regulate their body temperature.',
    'Consider using paw protection booties if hot pavement is unavoidable during essential walks (e.g., bathroom breaks).',
    'Visit a pet-friendly store or air-conditioned dog park for a short playtime session in a cool environment.'
])

PET_CARE_TIP.add(0, 2, "cat", [
    'Supervised Catio Time: If you have a catio, restrict access during the hottest part of the day and only allow playtime in the cooler morning or evening hours. Provide shaded areas and ample water bowls inside the catio.',
    'Minimize Outdoor Exposure: Avoid letting your cat outdoors entirely if possible. If necessary for bathroom breaks (leashed walks for adventurous cats), keep it very brief and prioritize shaded areas.',
    'Monitor Behavior: Closely watch your cat for signs of overheating like excessive panting, lethargy, or glazed eyes.',
    'Cooling Techniques: If your cat seems overheated, utilize cooling techniques like damp towels or misting with cool water (avoid soaking).',
    'Vet Check Readiness: Be prepared to take your cat to the vet immediately if you suspect signs of heatstroke.'
])

PET_CARE_TIP.add(0, 2, "dog", [
    'Keep your dog cool indoors with air conditioning. Provide plenty of water and monitor their breathing for signs of heatstroke.',
    'Utilize cooling techniques like damp towels, fans, and misting to lower your dog\'s body temperature.',
    'Be prepared to take your dog to the vet immediately if you suspect signs of heatstroke (excessive panting, lethargy, vomiting).',
    'Offer cool, fresh water constantly and consider using flavoring like low-sodium broth to encourage drinking.',
    'Keep your dog calm and avoid any unnecessary movement or activity that could elevate their body temperature.'
])

PET_CARE_TIP.add(0, 3, "cat", [
    'Do not allow your cat outdoors under any circumstances during extreme danger conditions.',
    'Ensure your home is cool with air conditioning or utilize fans in well-ventilated areas.',
    'Provide multiple water bowls with fresh, cool water and consider adding flavoring like low-sodium broth to encourage drinking.',
    'Continuously monitor your cat\'s breathing and behavior for signs of heatstroke. Seek immediate veterinary attention if necessary.',
    'These situations may require emergency measures to cool your cat down. Consult your veterinarian for specific advice.'
])

PET_CARE_TIP.add(0, 3, "dog", [
    'These situations may require emergency measures to cool your dog down. Consult your veterinarian for specific advice.',
    'Find immediate access to a cool, air-conditioned space like a veterinary clinic or pet store.',
    'Wet down your dog with cool water (not ice cold) and encourage them to lick ice cubes to lower their body temperature gradually.',
    'Continuously monitor your dog\'s breathing and behavior for signs of heatstroke. Seek immediate veterinary attention if necessary.',
    'Do not take your dog outside under any circumstances during extremely dangerous conditions.'
])

PET_CARE_TIP.add(1, 0, "cat", [
    'Window Watching: Set up a cozy spot by a window for your cat to watch the outside world. Ensure the window is securely closed and offer a comfortable perch.',
    'Hydration Awareness: Although it\'s not hot, always provide fresh water to keep your cat hydrated. Consider using a water fountain to encourage drinking.',
    'Interactive Toys: Engage your cat with interactive toys like feather wands or laser pointers. Rotate toys regularly to keep them interested.',
    'Climbing Structures: Ensure your cat has access to climbing structures or scratching posts for physical activity.',
    'Grooming: Brush your cat to help reduce shedding and keep their coat healthy.'
])

PET_CARE_TIP.add(1, 0, "dog", [
    'Morning/Afternoon Walk: Enjoy a leisurely walk at any time of the day as temperatures are steady. Ensure your dog is leashed and explore new, shaded paths or parks.',
    'Hydration Awareness: Although it\'s not hot, always provide fresh water to keep your dog hydrated.',
    'Playtime Fun: Cloudy days are perfect for a fun game of fetch or tug-of-war in your backyard or a local dog park. Bring toys that stimulate your dog physically and mentally.',
    'Training Sessions: Use the mild weather to conduct short training sessions outside. This helps with mental stimulation and obedience.',
    'Grooming: Take the opportunity to groom your dog outside. The mild weather makes it comfortable for both you and your pet.'
])

PET_CARE_TIP.add(1, 1, "cat", [
    'Warm Naps: Ensure your cat has warm, comfortable places to nap. A soft blanket or a heated bed can be perfect for cooler, cloudy days.',
    'Calm Environment: If the weather turns colder, create a calm, safe environment for your cat. Use calming music or white noise to soothe any anxiety.',
    'Monitor the Weather: Continuously check the weather forecast to be aware of any changes.',
    'Secure Windows: Ensure all windows are securely closed to prevent drafts.',
    'Extra Bedding: Provide extra bedding in your cat\'s favorite spots for added warmth.'
])

PET_CARE_TIP.add(1, 1, "dog", [
    'Layered Clothing: Bring an extra layer for your dog, such as a light sweater, in case it gets cooler.',
    'Shorter Walks: Keep walks a bit shorter to avoid the potential drop in temperature.',
    'Monitor the Weather: Continuously check the weather forecast to plan activities accordingly.',
    'Enrichment Toys: Use interactive toys or treat-dispensing puzzles to keep your dog occupied indoors if it gets too cool.',
    'Warm-up After Walks: Have a warm blanket ready for your dog to use after outdoor activities.'
])

PET_CARE_TIP.add(1, 2, "cat", [
    'Window Perch: Your cat can still enjoy watching the outside from a cozy window perch. Ensure it\'s a warm spot and check for drafts.',
    'Hydration and Comfort: Maintain hydration and offer comforting spaces. Extra blankets or pet-safe heating pads can make a big difference on a cooler day.',
    'Indoor Play: Engage in indoor play sessions with your cat to keep them active.',
    'Litter Box Maintenance: Ensure the litter box is clean and easily accessible, especially if it\'s placed near windows or doors where it might get drafty.',
    'Comfort Items: Provide soft bedding and favorite toys to keep your cat comfortable and entertained.'
])

PET_CARE_TIP.add(1, 2, "dog", [
    'Short Walks: Shorten walks and focus on quick bathroom breaks to avoid the cooler weather.',
    'Indoor Exercise: Continue indoor play and mental stimulation. Agility training in your living room can be a fun way to keep your dog active.',
    'Stay Warm: Use a sweater or coat for your dog to keep them warm during brief outdoor activities.',
    'Comfort Items: Provide your dog with a warm blanket or a cozy bed to help them stay comfortable indoors.',
    'Warm Treats: Offer warm, dog-safe treats to help them stay warm and cozy.'
])

PET_CARE_TIP.add(1, 3, "cat", [
    'Safe Space: Create a warm, quiet space for your cat to retreat to during extreme cold. A covered crate or a designated room can help them feel secure.',
    'Distracting Activities: Engage your cat with distracting activities like puzzle feeders or interactive toys. This can help them focus on something other than the weather.',
    'Emergency Preparedness: Have a plan in place for extreme weather, including knowing where your nearest emergency vet is located. Keep a pet emergency kit with essentials like food, water, medications, and comfort items.',
    'Calm Environment: Use calming pheromones or sprays to help reduce your cat\'s anxiety.',
    'Monitor Behavior: Keep an eye on your cat\'s behavior for signs of stress and provide extra comfort and attention if needed.'
])

PET_CARE_TIP.add(1, 3, "dog", [
    'Safe Space: Create a warm, quiet space for your dog to retreat to during extreme cold. A covered crate or a designated room can help them feel secure.',
    'Calm Assurance: Stay close to your dog and provide reassurance if they seem anxious due to the weather.',
    'Distracting Activities: Engage your dog with distracting activities like puzzle feeders or interactive toys. This can help them focus on something other than the weather.',
    'Emergency Preparedness: Have a plan in place for extreme weather, including knowing where your nearest emergency vet is located. Keep a pet emergency kit with essentials like food, water, medications, and comfort items.',
    'Heating Pads: Use pet-safe heating pads or blankets to provide extra warmth if necessary.'
])

PET_CARE_TIP.add(2, 0, "cat", [
    'Keep your cat indoors to avoid exposure to high heat and rain.',
    'Ensure your cat stays in a cool and shaded area.',
    'Give them plenty of fresh water to drink.',
    'Observe signs of tiredness, panting, and lethargy.',
    'Keep the windows open as long as rainwater is not coming inside, allowing air to circulate and cool the room.'
])

PET_CARE_TIP.add(2, 0, "dog", [
    'Limit outside activities to avoid exhaustion and exposure to wet conditions.',
    'Bring them indoors if they seem uncomfortable outside.',
    'Ensure your dog has access to plenty of cool and clean water.',
    'Prevent your dog from walking on hot, wet pavement, which can be uncomfortable for their paws.',
    'Monitor for excessive panting.'
])

PET_CARE_TIP.add(2, 1, "cat", [
    'Prevent your cat from going outside during peak heat hours and rain showers.',
    'Prepare cooling mats or damp towels for your cat to lie on.',
    'Use fans to maintain a cool indoor temperature.',
    'Monitor for signs of heat stress, such as rapid breathing or drooling, and cool your cat down if needed.',
    'Put water bowls around the house to give your cats easy access to hydration.'
])

PET_CARE_TIP.add(2, 1, "dog", [
    'Use cool, damp towels or a cooling mat to help your dog stay cool.',
    'Walk your dog during early morning or late evening when temperatures are cooler. Also, ensure that it is not raining when doing outdoor activities.',
    'Ensure your dog drinks enough water throughout the day.',
    'Be alert for signs of heat stress, such as excessive panting, drooling, or restlessness.',
    'Move your dog to a cooler area immediately if signs of heat stress occur.'
])

PET_CARE_TIP.add(2, 2, "cat", [
    'Strictly keep your cat indoors and ensure they have a space with a bearable temperature.',
    'Prohibit your cat from engaging in strenuous activities or going outside to avoid exhaustion.',
    'Use cooling mats, fans, or damp towels to help your cat stay cool.',
    'Provide emotional support for your pets by assuring them that they will be fine.',
    'Look for signs of heat exhaustion, such as vomiting, episodic collapse, or uncoordinated movements, and contact your vet immediately when these happen.'
])

PET_CARE_TIP.add(2, 2, "dog", [
    'Place your dog in shoulder-depth cool water until their temperature lowers.',
    'Refrain from exercising your dog during hot, rainy weather to prevent overheating.',
    'Put cool, damp clothes on your dog\'s body, especially the neck, armpits, and groin.',
    'Use isopropyl alcohol on your dog\'s paw pads to aid cooling.',
    'Be vigilant for symptoms of heat exhaustion like vomiting, diarrhea, or seizure, and seek professional help if these occur.'
])

PET_CARE_TIP.add(2, 3, "cat", [
    'If your cat demonstrates signs of heatstroke, perform cooling techniques as first aid and immediately seek veterinary care after.',
    'Give them wet cat food or flavored water. Flavored fluids encourage them to drink more water.',
    'Soak them in cool water, put a damp towel on them, and spray water on their body to reduce their temperature.',
    'Place them directly in front of an electric fan or in a well-ventilated area. The humid air caused by the weather also helps them cool down.',
    'Be ready to call for medical attention if emergency cases occur.'
])

PET_CARE_TIP.add(2, 3, "dog", [
    'Offer small amounts of cool water without forcing them to drink.',
    'Direct fans towards your dog to enhance cooling through evaporation.',
    'If your dog shows signs of heatstroke, immediately move them to a cool area and apply cool water to their body.',
    'Bring them to the nearest vet clinic or contact a veterinarian if they collapse.',
    'Keep an eye on your dog\'s rectal temperature, and halt cooling efforts once they return to their normal temperature, specifically 103°F (39.4°C).'
])

PET_CARE_TIP.add(3, 0, "cat", [
    'Set up a comfy perch near a window with some shade for your cat to enjoy basking in the warm sunshine while watching birds or outdoor activities. Consider rotating toys or placing feeders outside the window for added stimulation.',
    'Create a moving light show using a mirror and sunlight. Reflect the sunlight onto a wall or floor, creating a moving light source for your cat to chase and pounce on.',
    'Fill a cardboard box with shredded paper and sprinkle some catnip inside. This creates a cool, shaded hideaway infused with a scent that encourages playful exploration.',
    'Fill interactive treat-dispensing toys with their favorite kibble or treats. The sunshine might motivate them to be more active as they try to solve the puzzle and earn their rewards.',
    'Utilize vertical spaces like cat trees or shelves placed near sunny windows. This allows your cat to bask in the warmth while also engaging in their natural climbing instincts.'
])

PET_CARE_TIP.add(3, 0, "dog", [
    'Enjoy the cooler temperatures during sunrise or sunset for a refreshing walk. Keep walks shorter and prioritize shaded areas like parks with plenty of trees.',
    'Consider using a hydration backpack for your dog on walks. This allows for easy access to cool water throughout the outing and keeps them hydrated.',
    'Wet a bandana with cool water and tie it loosely around your dog\'s neck for a portable cooling solution during walks. Re-wet the bandana as needed.',
    'Set up a sprinkler in your backyard for a refreshing play session. This allows your dog to cool down while having fun in a controlled environment.',
    'Engage your dog in interactive play with water toys like hoses with misting attachments or squeaky water toys. This provides exercise and keeps them cool.'
])

PET_CARE_TIP.add(3, 1, "cat", [
    'Indoor Time: Encourage your cat to stay indoors during the hottest part of the day, typically from late morning to mid-afternoon.',
    'Fresh Water: Keep multiple bowls of fresh water indoors and consider placing them in cool, shaded spots to encourage hydration.',
    'Cooling Mats: Provide cooling mats or pads in shaded areas of your home where your cat likes to rest.',
    'Airflow: Ensure good airflow indoors with fans or air conditioning to keep the environment cool and comfortable for your cat.',
    'Grooming: Brush your cat regularly to remove excess fur, which can help them stay cooler during hot weather.'
])

PET_CARE_TIP.add(3, 1, "dog", [
    'Limit Outdoor Time: During peak sunlight hours, limit your dog\'s outdoor activities to early mornings or late evenings to avoid the hottest part of the day.',
    'Stay Hydrated: Always carry fresh water and offer it frequently to prevent dehydration. Consider adding ice cubes to their water bowl to keep it cool longer.',
    'Shade Access: Ensure there are shaded areas available if your dog needs to be outside. Use portable shade covers or trees for protection from direct sunlight.',
    'Cooling Vests: Consider using a cooling vest or bandana to help regulate your dog\'s body temperature during walks or outdoor activities.',
    'Paw Protection: Use paw wax or booties to protect your dog\'s paws from hot pavement, which can cause burns and discomfort.'
])

PET_CARE_TIP.add(3, 2, "cat", [
    'Submerge your cat in cool water having a temperature of 72.0 °F (22.2 °C), making sure that it only goes up to their shoulders. Do not use ice-cold water as the sudden change of temperature may cause a shock to their system.',
    'Apply isopropyl alcohol on their paw pads.',
    'Instead of air conditioners, use an evaporation cooler as it is more eco-friendly and produces fresh clean air.',
    'If evaporation coolers are not available, improvise by spraying water all over your cat\'s body while allowing air circulation.',
    'Do not force your cat to drink more water because cats usually drink less than they should. But make sure to always fill up their bowl with water and feed them wet food.'
])

PET_CARE_TIP.add(3, 2, "dog", [
    'Immerse your dog in shoulder-depth water with a temperature of at least 72.0 °F (22.2 °C) for 30 seconds or longer.',
    'Apply isopropyl alcohol on their paw pads.',
    'Put your dog in a room with an evaporation cooler.',
    'Spray water on your dog\'s body while giving them some air.',
    'Keep your dog hydrated with water or flavored oral electrolyte solutions (OES).'
])

PET_CARE_TIP.add(3, 3, "cat", [
    'Indoor Stay: Keep your cat indoors throughout the day during extreme heat to prevent heatstroke and discomfort.',
    'Cool Indoor Spaces: Provide multiple cool, shaded spots indoors for your cat to rest. Use fans or air conditioning to maintain a comfortable temperature.',
    'Hydration: Ensure your cat has access to fresh water at all times. Consider using a pet fountain to encourage drinking.',
    'Emergency Kit: Prepare a pet emergency kit that includes items like cool packs, electrolyte solutions, and contact information for your veterinarian.',
    'Cooling Techniques: Use cooling mats or chilled ceramic tiles for your cat to lie on. Monitor their behavior for signs of heat stress and act promptly if needed.'
])

PET_CARE_TIP.add(3, 3, "dog", [
    'Avoid Outdoor Activity: Keep your dog indoors as much as possible during extreme heat to prevent heatstroke and dehydration.',
    'Cool Indoor Environment: Maintain a cool indoor environment with air conditioning or fans. Provide a comfortable area for your dog to rest away from direct sunlight.',
    'Hydration Focus: Ensure your dog has constant access to cool, fresh water. Consider adding electrolytes to their water or offering ice cubes as a refreshing treat.',
    'Emergency Preparedness: Have a plan in place for emergencies related to heatstroke. Know the signs and symptoms, and have contact information for a veterinarian ready.',
    'Wet Towels: Use damp towels or cooling blankets to help lower your dog\'s body temperature if they show signs of overheating.'
])