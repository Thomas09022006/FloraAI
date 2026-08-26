"""
FloraAI - Flower Information Module
Botanical knowledge base and detailed species characteristics for Iris Setosa, Versicolor, and Virginica.
"""

FLOWER_SPECIES_INFO = {
    "Iris-setosa": {
        "title": "🌸 Iris Setosa (Bristle-pointed Iris)",
        "icon": "🌸",
        "petal_length_range": "1.0 – 1.9 cm",
        "petal_width_range": "0.1 – 0.6 cm",
        "sepal_length_range": "4.3 – 5.8 cm",
        "sepal_width_range": "2.3 – 4.4 cm",
        "color": "Deep blue, purple-violet, or white with yellow signals",
        "characteristics": "Distinct small petals, large prominent sepals, highly linear and separable from other species.",
        "distribution": "Native to subarctic regions, Alaska, Northeastern North America, and Eastern Siberia.",
        "interesting_fact": "Setosa flowers are adapted to cold arctic climates and possess bristles at the petal base, giving them their common name."
    },
    "Iris-versicolor": {
        "title": "🌺 Iris Versicolor (Harlequin / Blue Flag Iris)",
        "icon": "🌺",
        "petal_length_range": "3.0 – 5.1 cm",
        "petal_width_range": "1.0 – 1.8 cm",
        "sepal_length_range": "4.9 – 7.0 cm",
        "sepal_width_range": "2.0 – 3.4 cm",
        "color": "Violet-blue, lavender, with white and yellow patch at sepal base",
        "characteristics": "Medium-sized balanced petals and sepals, moderate variation in petal growth.",
        "distribution": "Widespread across marshes, wetlands, and stream banks in Eastern North America.",
        "interesting_fact": "It is the official provincial floral emblem of Quebec, Canada, and was historically used in traditional herbal botany."
    },
    "Iris-virginica": {
        "title": "🌼 Iris Virginica (Virginia Iris)",
        "icon": "🌼",
        "petal_length_range": "4.5 – 6.9 cm",
        "petal_width_range": "1.4 – 2.5 cm",
        "sepal_length_range": "4.9 – 7.9 cm",
        "sepal_width_range": "2.2 – 3.8 cm",
        "color": "Bright violet to blue-purple with bold gold crests on sepals",
        "characteristics": "Largest petals and sepals among the three species, exhibits substantial variance.",
        "distribution": "Found in coastal plains, swamps, and freshwater marshes of Eastern and Southern United States.",
        "interesting_fact": "Virginica features lush, elongated bright green leaves that often arch gracefully over water bodies."
    }
}

def get_species_information(species_name: str) -> dict:
    """Retrieves full botanical profile for a given Iris species."""
    clean_name = species_name.strip()
    if not clean_name.startswith("Iris-") and clean_name in ["setosa", "versicolor", "virginica"]:
        clean_name = f"Iris-{clean_name}"
    return FLOWER_SPECIES_INFO.get(clean_name, FLOWER_SPECIES_INFO["Iris-setosa"])
