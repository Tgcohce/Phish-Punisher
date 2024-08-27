import requests
import random
from concurrent.futures import ThreadPoolExecutor

thread_count = 99999

def generate_random_phrase():
    # A list of common English words
    words = [
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
        "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
        "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
        "watermelon", "xigua", "yellow", "zucchini", "adventure", "bravery",
        "curiosity", "determination", "energy", "freedom", "growth", "harmony",
        "insight", "joy", "knowledge", "love", "motivation", "nature", "optimism",
        "peace", "quality", "respect", "strength", "trust", "unity", "vision",
        "wisdom", "youth", "zeal", "mountain", "river", "forest", "ocean",
        "desert", "valley", "island", "volcano", "canyon", "cliff", "stream",
        "waterfall", "glacier", "bay", "peninsula", "reef", "lagoon", "cape",
        "plateau", "plain", "savanna", "tundra", "wetland", "meadow", "hill",
        "ridge", "dune", "prairie", "grove", "jungle", "swamp", "marsh",
        "pond", "lake", "fjord", "delta", "gulf", "harbor", "cove", "beach",
        "shore", "coast", "isthmus", "strait", "archipelago", "atoll", "rain",
        "snow", "wind", "storm", "fog", "mist", "cloud", "sky", "sun", "moon",
        "star", "planet", "galaxy", "universe", "cosmos", "asteroid", "comet",
        "meteor", "nebula", "quasar", "blackhole", "eclipse", "orbit", "gravity",
        "light", "darkness", "shadow", "reflection", "illusion", "dream", "night",
        "day", "dawn", "dusk", "noon", "midnight", "twilight", "horizon", "zenith",
        "equator", "pole", "axis", "season", "year", "century", "decade", "minute",
        "second", "moment", "infinity", "eternity", "timeless", "past", "present",
        "future", "history", "myth", "legend", "fable", "story", "tale", "narrative",
        "chapter", "verse", "poetry", "song", "melody", "rhythm", "harmony", "chord",
        "note", "scale", "tune", "symphony", "concerto", "opera", "ballet", "dance",
        "art", "painting", "sculpture", "mosaic", "carving", "statue", "portrait",
        "landscape", "abstract", "design", "pattern", "color", "shade", "hue",
        "tone", "texture", "form", "structure", "balance", "symmetry", "contrast",
        "proportion", "space", "depth", "perspective", "dimension", "geometry",
        "angle", "line", "curve", "arc", "circle", "triangle", "square", "rectangle",
        "polygon", "ellipse", "parabola", "hyperbola", "spiral", "wave", "fractal",
        "chaos", "order", "logic", "reason", "thought", "mind", "consciousness",
        "subconscious", "memory", "imagination", "creativity", "intuition", "emotion",
        "feeling", "passion", "desire", "love", "hate", "fear", "joy", "sadness",
        "anger", "surprise", "trust", "disgust", "anticipation", "hope", "faith",
        "belief", "conviction", "opinion", "judgment", "decision", "choice", "action",
        "deed", "habit", "routine", "custom", "tradition", "culture", "society",
        "community", "nation", "country", "state", "province", "city", "town", "village",
        "neighborhood", "street", "avenue", "road", "path", "trail", "route", "journey",
        "voyage", "expedition", "adventure", "exploration", "discovery", "invention",
        "innovation", "progress", "evolution", "growth", "development", "change", "transformation",
        "transition", "cycle", "season", "nature", "ecosystem", "environment", "planet",
        "earth", "biosphere", "habitat", "species", "organism", "animal", "plant", "insect",
        "bird", "fish", "reptile", "amphibian", "mammal", "human", "life", "death", "birth",
        "growth", "decay", "regeneration", "reproduction", "mutation", "adaptation", "survival",
        "competition", "cooperation", "symbiosis", "parasitism", "predator", "prey", "herbivore",
        "carnivore", "omnivore", "scavenger", "decomposer", "producer", "consumer", "ecosystem",
        "food", "chain", "web", "energy", "cycle", "climate", "weather", "season", "temperature",
        "precipitation", "humidity", "wind", "air", "water", "soil", "rock", "mineral", "element",
        "compound", "molecule", "atom", "particle", "proton", "neutron", "electron", "quark",
        "photon", "wave", "energy", "force", "gravity", "magnetism", "electricity", "nuclear",
        "fusion", "fission", "reaction", "combustion", "oxidation", "reduction", "catalyst",
        "enzyme", "protein", "carbohydrate", "lipid", "nucleic", "acid", "DNA", "RNA", "chromosome",
        "gene", "mutation", "inheritance", "evolution", "natural", "selection", "adaptation",
        "survival", "species", "biodiversity", "conservation", "ecology", "environment", "pollution",
        "climate", "change", "sustainability", "resource", "management", "renewable", "energy",
        "fossil", "fuels", "solar", "wind", "hydropower", "geothermal", "nuclear", "fusion",
        "fission", "waste", "recycling", "composting", "landfill", "incineration", "emissions",
        "greenhouse", "gases", "carbon", "footprint", "global", "warming", "ozone", "layer",
        "depletion", "acid", "rain", "deforestation", "desertification", "biodiversity", "loss",
        "species", "extinction", "habitat", "destruction", "invasive", "species", "conservation",
        "restoration", "sustainability", "resilience", "adaptation", "mitigation", "innovation",
        "technology", "research", "development", "education", "awareness", "advocacy", "policy",
        "regulation", "legislation", "enforcement", "compliance", "governance", "leadership",
        "collaboration", "partnership", "network", "community", "engagement", "empowerment",
        "participation", "inclusion", "diversity", "equity", "justice", "rights", "freedom",
        "democracy", "citizenship", "responsibility", "accountability", "transparency",
        "ethics", "integrity", "values", "principles", "morality", "duty", "obligation",
        "service", "volunteerism", "philanthropy", "charity", "kindness", "compassion",
        "empathy", "sympathy", "solidarity", "support", "care", "help", "assistance",
        "guidance", "advice", "counseling", "mentoring", "coaching", "teaching", "learning",
        "education", "training", "skill", "development", "knowledge", "understanding",
        "wisdom", "insight", "intuition", "creativity", "imagination", "innovation",
        "invention", "discovery", "exploration", "adventure", "risk", "challenge", "opportunity",
        "success", "achievement", "accomplishment", "goal", "ambition", "aspiration", "dream",
        "vision", "hope", "inspiration", "motivation", "drive", "passion", "enthusiasm", "excitement",
        "energy", "vitality", "strength", "power", "force", "will", "determination", "persistence",
        "resilience", "courage", "bravery", "confidence", "self-esteem", "self-respect", "self-worth",
        "dignity", "pride", "honor", "glory", "fame", "recognition", "reputation", "status",
        "prestige", "influence", "power", "authority", "control", "leadership", "management",
        "administration", "organization", "planning", "strategy", "tactics", "decision-making",
        "problem-solving", "critical", "thinking", "analytical", "reasoning", "logical",
        "deduction", "induction", "inference", "evaluation", "assessment", "judgment",
        "opinion", "perspective", "viewpoint", "attitude", "belief", "conviction", "faith",
        "trust", "confidence", "certainty", "doubt", "skepticism", "questioning", "curiosity",
        "inquiry", "investigation", "research", "exploration", "discovery", "learning",
        "education", "knowledge", "understanding", "wisdom", "insight", "intuition", "creativity",
        "innovation", "imagination", "inspiration", "art", "beauty", "expression", "communication",
        "language", "literature", "poetry", "music", "dance", "drama", "theater", "film", "cinema",
        "photography", "painting", "sculpture", "architecture", "design", "fashion", "style",
        "culture", "civilization", "society", "community", "family", "relationships", "friendship",
        "love", "marriage", "parenting", "childhood", "adulthood", "aging", "death", "mortality",
        "life", "existence", "reality", "universe", "cosmos", "space", "time", "matter", "energy",
        "force", "motion", "gravity", "magnetism", "electricity", "light", "sound", "heat",
        "temperature", "pressure", "density", "volume", "mass", "weight", "dimension", "scale",
        "proportion", "symmetry", "geometry", "mathematics", "physics", "chemistry", "biology",
        "geology", "astronomy", "meteorology", "oceanography", "ecology", "environment",
        "sustainability", "conservation", "renewable", "energy", "climate", "change", "global",
        "warming", "pollution", "deforestation", "biodiversity", "extinction", "conservation",
        "restoration", "sustainability", "ethics", "values", "morality", "justice", "equality",
        "freedom", "rights", "democracy", "citizenship", "responsibility", "service", "volunteerism",
        "philanthropy", "charity", "kindness", "compassion", "empathy", "sympathy", "solidarity",
        "support", "care", "help", "assistance", "guidance", "advice", "counseling", "mentoring",
        "coaching", "teaching", "learning", "education", "training", "knowledge", "understanding",
        "wisdom", "insight", "intuition", "creativity", "innovation", "imagination", "inspiration",
        "motivation", "passion", "enthusiasm", "excitement", "energy", "vitality", "strength",
        "power", "force", "will", "determination", "persistence", "resilience", "courage", "bravery",
        "confidence", "self-esteem", "self-respect", "self-worth", "dignity", "pride", "honor",
        "glory", "fame", "recognition", "reputation", "status", "prestige", "influence", "power",
        "authority", "control", "leadership", "management", "organization", "planning", "strategy",
        "tactics", "decision-making", "problem-solving", "critical", "thinking", "analytical",
        "reasoning", "logical", "deduction", "induction", "inference", "evaluation", "assessment",
        "judgment", "opinion", "perspective", "viewpoint", "attitude", "belief", "conviction",
        "faith", "trust", "confidence", "certainty", "doubt", "skepticism", "questioning", "curiosity",
        "inquiry", "investigation", "research", "exploration", "discovery", "learning", "education",
        "knowledge", "understanding", "wisdom", "insight", "intuition", "creativity", "innovation",
        "imagination"
    ]

    # Generate a random phrase with 12 to 24 words from the list
    word_count = random.randint(12, 24)
    phrase = ' '.join(random.choices(words, k=word_count))
    return phrase

def main():
    url = ''  # The phishing endpoint

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [executor.submit(generate_random_phrase) for _ in range(thread_count)]
        c = 0

        for future in futures:
            print(f"{c + 1}th request")
            random_phrase = future.result()
            data = {
                'load_phrase': '1',
                'data_phrase': random_phrase,
                'wallet_selected': 'Metamask'
            }

            try:
                print(data)
                response = requests.post(url, headers=headers, data=data)
                response.raise_for_status()  # Raise an error for bad status codes
                print(f"Status Code: {response.status_code}")
                print(f"Response Headers: {response.headers}")
                print(thread_count)

            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")

            c += 1

if __name__ == "__main__":
    main()
    thread_count += 1

