#!/usr/bin/env python3

"""
Factory Color Harmonist - Professional Color Theory and Harmony Controls
Provides color palette management, mood enhancement, and cultural color considerations.

SFW Edition - GitHub Compliant - Professional Grade
"""

import random
import colorsys

class FactoryColorHarmonist:
    """
    Professional color harmonist node that applies color theory principles,
    cultural considerations, and mood-based palettes to enhance prompts.
    """
    
    def __init__(self):
        # Color harmony schemes based on color theory
        self.harmony_schemes = {
            "monochromatic": {
                "description": "Single color with variations in saturation and brightness",
                "tags": ["monochromatic", "single_hue", "tonal_variation", "unified_palette"],
                "mood": ["serene", "minimalist"]
            },
            "analogous": {
                "description": "Colors adjacent on the color wheel",
                "tags": ["analogous_colors", "neighboring_hues", "harmonious", "natural_transition"],
                "mood": ["harmonious", "peaceful", "organic"]
            },
            "complementary": {
                "description": "Colors opposite on the color wheel",
                "tags": ["complementary_colors", "opposite_hues", "high_contrast", "vibrant"],
                "mood": ["dynamic", "energetic", "bold"]
            },
            "split_complementary": {
                "description": "One color plus two colors adjacent to its complement",
                "tags": ["split_complementary", "balanced_contrast", "versatile"],
                "mood": ["balanced", "interesting", "refined"]
            },
            "triadic": {
                "description": "Three colors evenly spaced on the color wheel",
                "tags": ["triadic_colors", "three_way_harmony", "balanced", "vibrant"],
                "mood": ["lively", "balanced", "creative"]
            },
            "tetradic": {
                "description": "Four colors forming a rectangle on the color wheel",
                "tags": ["tetradic_colors", "quad_harmony", "complex", "rich_palette"],
                "mood": ["complex", "rich",]
            }
        }
        
        # Mood-based color palettes
        self.mood_palettes = {
            "warm_energetic": {
                "colors": ["warm_red", "orange", "yellow", "coral", "amber"],
                "tags": ["warm_palette", "energetic_colors", "vibrant", "stimulating"],
                "description": "Energizing warm colors"
            },
            "cool_calming": {
                "colors": ["cool_blue", "teal", "seafoam", "lavender", "mint"],
                "tags": ["cool_palette", "calming_colors", "serene", "peaceful"],
                "description": "Soothing cool colors"
            },
            "earth_natural": {
                "colors": ["earth_brown", "forest_green", "stone_gray", "clay_orange", "sand_beige"],
                "tags": ["earth_tones", "natural_palette", "organic", "grounded"],
                "description": "Natural earth colors"
            },
            "pastel_soft": {
                "colors": ["soft_pink", "pale_blue", "mint_green", "lavender", "cream"],
                "tags": ["pastel_colors", "soft_palette", "delicate", "gentle"],
                "description": "Gentle pastel colors"
            },
            "jewel_rich": {
                "colors": ["emerald_green", "sapphire_blue", "ruby_red", "amethyst_purple", "topaz_yellow"],
                "tags": ["jewel_tones", "rich_colors", "luxurious", "saturated"],
                "description": "Rich jewel tones"
            },
            "monochrome_classic": {
                "colors": ["pure_white", "light_gray", "medium_gray", "dark_gray", "deep_black"],
                "tags": ["monochrome", "grayscale", "classic", "timeless"],
                "description": "Classic black and white"
            },
            "vintage_muted": {
                "colors": ["dusty_rose", "sage_green", "cream", "muted_gold", "faded_blue"],
                "tags": ["vintage_colors", "muted_palette", "aged", "nostalgic"],
                "description": "Vintage muted colors"
            },
            "neon_electric": {
                "colors": ["electric_blue", "neon_pink", "lime_green", "bright_yellow", "magenta"],
                "tags": ["neon_colors", "electric_palette", "fluorescent", "bold"],
                "description": "Bold neon colors"
            },
            "sunset_gradient": {
                "colors": ["deep_orange", "coral_pink", "golden_yellow", "purple_twilight", "navy_blue"],
                "tags": ["sunset_colors", "gradient_palette", "transitional", "romantic"],
                "description": "Sunset gradient colors"
            },
            "forest_deep": {
                "colors": ["deep_green", "moss_green", "bark_brown", "mushroom_gray", "leaf_yellow"],
                "tags": ["forest_colors", "deep_natural", "woodland", "mysterious"],
                "description": "Deep forest colors"
            }
        }
        
        # Comprehensive cultural color associations from around the world
        self.cultural_palettes = {
            # East Asian Cultures
            "japanese_zen": {
                "colors": ["tatami_beige", "zen_white", "bamboo_green", "cherry_pink", "ink_black"],
                "tags": ["japanese_colors", "zen_palette", "minimalist", "traditional"],
                "description": "Japanese aesthetic colors"
            },
            "japanese_vibrant": {
                "colors": ["rising_sun_red", "temple_gold", "kimono_purple", "jade_green", "pearl_white"],
                "tags": ["japanese_bright", "traditional_vibrant", "ceremonial", "festive"],
                "description": "Vibrant Japanese traditional colors"
            },
            "chinese_imperial": {
                "colors": ["imperial_yellow", "dragon_red", "jade_green", "black_ink", "white_porcelain"],
                "tags": ["chinese_imperial", "royal_colors", "feng_shui", "traditional"],
                "description": "Chinese imperial colors"
            },
            "chinese_modern": {
                "colors": ["modern_red", "golden_yellow", "tech_blue", "prosperity_green", "neutral_gray"],
                "tags": ["chinese_contemporary", "modern_china", "business", "prosperity"],
                "description": "Modern Chinese colors"
            },
            "korean_hanbok": {
                "colors": ["hanbok_pink", "traditional_blue", "golden_yellow", "white_cotton", "earth_brown"],
                "tags": ["korean_traditional", "hanbok_colors", "cultural", "heritage"],
                "description": "Korean traditional hanbok colors"
            },
            
            # Nordic and Scandinavian
            "scandinavian_hygge": {
                "colors": ["nordic_white", "soft_gray", "warm_wood", "muted_blue", "cozy_cream"],
                "tags": ["scandinavian_colors", "hygge_palette", "cozy", "minimal"],
                "description": "Scandinavian hygge colors"
            },
            "nordic_winter": {
                "colors": ["arctic_white", "ice_blue", "aurora_green", "twilight_purple", "charcoal_gray"],
                "tags": ["nordic_winter", "arctic_colors", "aurora", "cold_palette"],
                "description": "Nordic winter colors"
            },
            "finnish_sauna": {
                "colors": ["birch_white", "sauna_wood", "lake_blue", "forest_green", "granite_gray"],
                "tags": ["finnish_colors", "sauna_palette", "nature_inspired", "authentic"],
                "description": "Finnish nature and sauna colors"
            },
            
            # Mediterranean Cultures
            "mediterranean_warm": {
                "colors": ["terracotta", "olive_green", "azure_blue", "golden_wheat", "limestone_white"],
                "tags": ["mediterranean_colors", "warm_palette", "coastal", "sunny"],
                "description": "Mediterranean warmth"
            },
            "greek_islands": {
                "colors": ["aegean_blue", "santorini_white", "sunset_orange", "olive_green", "stone_beige"],
                "tags": ["greek_colors", "island_palette", "coastal", "vacation"],
                "description": "Greek island colors"
            },
            "tuscan_countryside": {
                "colors": ["tuscan_red", "vineyard_green", "sunflower_yellow", "stone_gray", "wine_purple"],
                "tags": ["tuscan_colors", "countryside", "vineyard", "rustic"],
                "description": "Tuscan countryside colors"
            },
            "spanish_fiesta": {
                "colors": ["flamenco_red", "saffron_yellow", "olive_green", "terracotta_orange", "deep_purple"],
                "tags": ["spanish_colors", "fiesta_palette", "passionate", "vibrant"],
                "description": "Spanish fiesta colors"
            },
            
            # Middle Eastern and North African
            "moroccan_spice": {
                "colors": ["moroccan_red", "saffron_gold", "mint_green", "royal_blue", "desert_sand"],
                "tags": ["moroccan_colors", "spice_palette", "exotic", "rich"],
                "description": "Moroccan spice market colors"
            },
            "arabian_nights": {
                "colors": ["persian_blue", "golden_amber", "ruby_red", "emerald_green", "midnight_black"],
                "tags": ["arabian_colors", "mystical", "luxury", "exotic"],
                "description": "Arabian nights colors"
            },
            "egyptian_ancient": {
                "colors": ["pharaoh_gold", "nile_blue", "papyrus_beige", "hieroglyph_black", "lotus_pink"],
                "tags": ["egyptian_colors", "ancient", "royal", "historical"],
                "description": "Ancient Egyptian colors"
            },
            "turkish_bazaar": {
                "colors": ["turkish_red", "bazaar_gold", "carpet_blue", "spice_orange", "marble_white"],
                "tags": ["turkish_colors", "bazaar_palette", "merchant", "trade"],
                "description": "Turkish bazaar colors"
            },
            
            # South Asian Cultures
            "indian_vibrant": {
                "colors": ["saffron_orange", "turmeric_yellow", "peacock_blue", "rose_pink", "henna_red"],
                "tags": ["indian_colors", "vibrant_palette", "spice_colors", "festive"],
                "description": "Indian vibrant colors"
            },
            "indian_classical": {
                "colors": ["marigold_orange", "temple_gold", "indigo_blue", "lotus_pink", "sandalwood_cream"],
                "tags": ["indian_classical", "temple_colors", "spiritual", "traditional"],
                "description": "Indian classical colors"
            },
            "bollywood_glamour": {
                "colors": ["bollywood_pink", "golden_glitter", "royal_purple", "emerald_green", "silver_shine"],
                "tags": ["bollywood_colors", "glamour_palette", "entertainment", "flashy"],
                "description": "Bollywood glamour colors"
            },
            "thai_temple": {
                "colors": ["temple_gold", "thai_red", "emerald_green", "lotus_white", "saffron_orange"],
                "tags": ["thai_colors", "temple_palette", "buddhist", "spiritual"],
                "description": "Thai temple colors"
            },
            
            # African Cultures
            "african_earth": {
                "colors": ["terracotta_red", "savanna_gold", "acacia_brown", "sky_blue", "sunset_orange"],
                "tags": ["african_colors", "earth_palette", "warm_tones", "natural"],
                "description": "African earth tones"
            },
            "african_tribal": {
                "colors": ["tribal_red", "ochre_yellow", "mud_brown", "charcoal_black", "bone_white"],
                "tags": ["african_tribal", "primitive", "authentic", "cultural"],
                "description": "African tribal colors"
            },
            "safari_adventure": {
                "colors": ["khaki_tan", "safari_green", "sunset_red", "sand_beige", "elephant_gray"],
                "tags": ["safari_colors", "adventure", "wildlife", "expedition"],
                "description": "Safari adventure colors"
            },
            
            # Latin American Cultures
            "mexican_fiesta": {
                "colors": ["fiesta_red", "lime_green", "bright_yellow", "hot_pink", "deep_purple"],
                "tags": ["mexican_colors", "fiesta_palette", "celebration", "bright"],
                "description": "Mexican fiesta colors"
            },
            "brazilian_carnival": {
                "colors": ["carnival_yellow", "samba_red", "tropical_green", "azure_blue", "magenta_pink"],
                "tags": ["brazilian_colors", "carnival", "tropical", "energetic"],
                "description": "Brazilian carnival colors"
            },
            "peruvian_andes": {
                "colors": ["andes_purple", "alpaca_brown", "sky_blue", "corn_yellow", "stone_gray"],
                "tags": ["peruvian_colors", "mountain", "traditional", "textile"],
                "description": "Peruvian Andes colors"
            },
            
            # Native American
            "native_american": {
                "colors": ["earth_red", "sky_blue", "corn_yellow", "forest_green", "bone_white"],
                "tags": ["native_american", "earth_tones", "spiritual", "natural"],
                "description": "Native American colors"
            },
            "southwestern_desert": {
                "colors": ["desert_orange", "cactus_green", "sunset_red", "sand_tan", "turquoise_blue"],
                "tags": ["southwestern", "desert", "adobe", "southwestern_usa"],
                "description": "Southwestern desert colors"
            },
            
            # European Regional
            "irish_countryside": {
                "colors": ["emerald_green", "shamrock", "stone_gray", "cream_white", "peat_brown"],
                "tags": ["irish_colors", "countryside", "emerald_isle", "natural"],
                "description": "Irish countryside colors"
            },
            "german_oktoberfest": {
                "colors": ["oktoberfest_blue", "bavarian_white", "pretzel_brown", "beer_gold", "lederhosen_green"],
                "tags": ["german_colors", "oktoberfest", "bavarian", "traditional"],
                "description": "German Oktoberfest colors"
            },
            "french_provence": {
                "colors": ["lavender_purple", "sunflower_yellow", "olive_green", "limestone_white", "wine_red"],
                "tags": ["french_colors", "provence", "countryside", "romantic"],
                "description": "French Provence colors"
            },
            "british_heritage": {
                "colors": ["royal_blue", "heritage_red", "english_green", "stone_gray", "cream_white"],
                "tags": ["british_colors", "heritage", "royal", "traditional"],
                "description": "British heritage colors"
            },
        }
        
        # Comprehensive professional color spaces and industry applications
        self.professional_palettes = {
            # Corporate and Business
            "corporate_trust": {
                "colors": ["navy_blue", "silver_gray", "white", "accent_blue", "charcoal"],
                "tags": ["corporate_colors", "professional", "trustworthy", "business"],
                "description": "Corporate trustworthy colors"
            },
            "corporate_modern": {
                "colors": ["modern_blue", "clean_white", "steel_gray", "accent_green", "neutral_beige"],
                "tags": ["corporate_modern", "contemporary", "clean", "progressive"],
                "description": "Modern corporate colors"
            },
            "startup_energy": {
                "colors": ["startup_orange", "innovation_blue", "growth_green", "energy_yellow", "pure_white"],
                "tags": ["startup_colors", "energetic", "innovative", "dynamic"],
                "description": "Startup energy colors"
            },
            "financial_stability": {
                "colors": ["bank_blue", "gold_accent", "trust_gray", "money_green", "professional_white"],
                "tags": ["financial_colors", "banking", "stability", "wealth"],
                "description": "Financial stability colors"
            },
            
            # Luxury and Premium
            "luxury_premium": {
                "colors": ["champagne_gold", "platinum_silver", "deep_black", "ivory_white", "bronze"],
                "tags": ["luxury_colors", "premium_palette", "elegant"],
                "description": "Luxury premium colors"
            },
            "luxury_classic": {
                "colors": ["royal_gold", "classic_black", "pearl_white", "burgundy_red", "platinum"],
                "tags": ["luxury_classic", "timeless", "opulent", "prestigious"],
                "description": "Classic luxury colors"
            },
            "haute_couture": {
                "colors": ["couture_black", "champagne", "rose_gold", "silk_white", "diamond_silver"],
                "tags": ["haute_couture", "fashion", "exclusive", "refined"],
                "description": "Haute couture colors"
            },
            "jewelry_precious": {
                "colors": ["24k_gold", "platinum_white", "diamond_clear", "ruby_red", "sapphire_blue"],
                "tags": ["jewelry_colors", "precious_metals", "gemstone", "valuable"],
                "description": "Precious jewelry colors"
            },
            
            # Technology and Digital
            "tech_modern": {
                "colors": ["electric_blue", "silver_chrome", "pure_white", "neon_accent", "carbon_black"],
                "tags": ["tech_colors", "modern_palette", "digital", "futuristic"],
                "description": "Modern technology colors"
            },
            "tech_innovation": {
                "colors": ["innovation_blue", "cyber_green", "digital_white", "circuit_gray", "ai_purple"],
                "tags": ["tech_innovation", "cutting_edge", "artificial_intelligence", "future"],
                "description": "Technology innovation colors"
            },
            "gaming_neon": {
                "colors": ["gaming_green", "neon_blue", "electric_purple", "laser_red", "cosmic_black"],
                "tags": ["gaming_colors", "neon", "esports", "entertainment"],
                "description": "Gaming neon colors"
            },
            "cyberpunk_future": {
                "colors": ["cyber_pink", "neon_blue", "matrix_green", "digital_purple", "void_black"],
                "tags": ["cyberpunk", "futuristic", "digital_punk", "sci_fi"],
                "description": "Cyberpunk future colors"
            },
            "blockchain_crypto": {
                "colors": ["bitcoin_orange", "ethereum_blue", "crypto_gold", "digital_silver", "network_gray"],
                "tags": ["blockchain", "cryptocurrency", "digital_currency", "fintech"],
                "description": "Blockchain and crypto colors"
            },
            
            # Healthcare and Medical
            "healthcare_clean": {
                "colors": ["medical_blue", "clean_white", "soft_green", "trust_gray", "accent_teal"],
                "tags": ["healthcare_colors", "clean_palette", "medical", "sterile"],
                "description": "Healthcare clean colors"
            },
            "medical_professional": {
                "colors": ["scrubs_blue", "lab_white", "emergency_red", "calm_green", "neutral_gray"],
                "tags": ["medical_professional", "hospital", "clinical", "health"],
                "description": "Medical professional colors"
            },
            "pharmaceutical": {
                "colors": ["pharma_blue", "safety_white", "pill_green", "warning_orange", "prescription_purple"],
                "tags": ["pharmaceutical", "medicine", "drug", "safety"],
                "description": "Pharmaceutical colors"
            },
            "wellness_spa": {
                "colors": ["spa_green", "wellness_white", "calm_blue", "natural_beige", "zen_gray"],
                "tags": ["wellness", "spa", "relaxation", "health"],
                "description": "Wellness spa colors"
            },
            
            # Environmental and Sustainability
            "eco_sustainable": {
                "colors": ["forest_green", "earth_brown", "natural_beige", "sky_blue", "leaf_green"],
                "tags": ["eco_colors", "sustainable_palette", "natural", "environmental"],
                "description": "Eco-friendly colors"
            },
            "renewable_energy": {
                "colors": ["solar_yellow", "wind_blue", "earth_green", "clean_white", "nature_brown"],
                "tags": ["renewable_energy", "solar", "wind", "sustainable"],
                "description": "Renewable energy colors"
            },
            "organic_natural": {
                "colors": ["organic_green", "natural_brown", "pure_white", "earth_tan", "plant_green"],
                "tags": ["organic", "natural", "pure", "wholesome"],
                "description": "Organic natural colors"
            },
            "climate_conscious": {
                "colors": ["earth_blue", "conservation_green", "clean_air_white", "ocean_teal", "forest_brown"],
                "tags": ["climate", "conservation", "environmental", "planet"],
                "description": "Climate conscious colors"
            },
            
            # Education and Academic
            "academic_institution": {
                "colors": ["academic_blue", "knowledge_gold", "wisdom_gray", "book_white", "tradition_red"],
                "tags": ["academic", "education", "university", "scholarly"],
                "description": "Academic institution colors"
            },
            "elementary_school": {
                "colors": ["cheerful_yellow", "learning_blue", "growth_green", "fun_red", "safe_white"],
                "tags": ["elementary", "children", "learning", "colorful"],
                "description": "Elementary school colors"
            },
            "research_scientific": {
                "colors": ["research_blue", "lab_white", "data_gray", "innovation_green", "analysis_purple"],
                "tags": ["scientific", "research", "laboratory", "analysis"],
                "description": "Scientific research colors"
            },
            
            # Food and Beverage Industry
            "restaurant_fine_dining": {
                "colors": ["fine_dining_black", "elegant_gold", "wine_red", "crisp_white", "truffle_brown"],
                "tags": ["fine_dining", "restaurant", "culinary", "gourmet"],
                "description": "Fine dining restaurant colors"
            },
            "fast_food_chain": {
                "colors": ["appetite_red", "golden_yellow", "energy_orange", "fresh_green", "clean_white"],
                "tags": ["fast_food", "quick_service", "appetite", "energetic"],
                "description": "Fast food chain colors"
            },
            "coffee_shop": {
                "colors": ["coffee_brown", "cream_beige", "warm_orange", "cozy_red", "milk_white"],
                "tags": ["coffee", "cafe", "warm", "cozy"],
                "description": "Coffee shop colors"
            },
            "brewery_craft": {
                "colors": ["beer_gold", "hops_green", "malt_brown", "foam_white", "barrel_oak"],
                "tags": ["brewery", "craft_beer", "artisan", "traditional"],
                "description": "Craft brewery colors"
            },
            
            # Real Estate and Architecture
            "real_estate_luxury": {
                "colors": ["property_gold", "estate_blue", "luxury_white", "investment_gray", "prestige_black"],
                "tags": ["real_estate", "property", "luxury_home", "investment"],
                "description": "Luxury real estate colors"
            },
            "architecture_modern": {
                "colors": ["concrete_gray", "steel_silver", "glass_blue", "minimalist_white", "accent_black"],
                "tags": ["architecture", "modern_design", "minimalist", "structural"],
                "description": "Modern architecture colors"
            },
            "interior_design": {
                "colors": ["designer_beige", "accent_teal", "neutral_gray", "warm_white", "statement_black"],
                "tags": ["interior_design", "home_decor", "stylish", "contemporary"],
                "description": "Interior design colors"
            },
            
            # Transportation and Automotive
            "automotive_luxury": {
                "colors": ["luxury_black", "chrome_silver", "leather_brown", "performance_red", "premium_white"],
                "tags": ["automotive", "luxury_car", "performance", "premium"],
                "description": "Luxury automotive colors"
            },
            "aviation_professional": {
                "colors": ["aviation_blue", "sky_white", "professional_gray", "safety_orange", "precision_black"],
                "tags": ["aviation", "aerospace", "flight", "professional"],
                "description": "Aviation professional colors"
            },
            "maritime_nautical": {
                "colors": ["navy_blue", "sail_white", "anchor_black", "ocean_teal", "rope_brown"],
                "tags": ["maritime", "nautical", "sailing", "ocean"],
                "description": "Maritime nautical colors"
            },
            
            # Entertainment and Media
            "entertainment_glamour": {
                "colors": ["glamour_gold", "spotlight_white", "red_carpet", "star_silver", "premiere_black"],
                "tags": ["entertainment", "glamour", "celebrity", "show_business"],
                "description": "Entertainment glamour colors"
            },
            "media_broadcast": {
                "colors": ["broadcast_blue", "news_red", "studio_white", "professional_gray", "live_green"],
                "tags": ["media", "broadcast", "news", "television"],
                "description": "Media broadcast colors"
            },
            "music_industry": {
                "colors": ["music_purple", "sound_gold", "rhythm_red", "harmony_blue", "stage_black"],
                "tags": ["music", "audio", "sound", "entertainment"],
                "description": "Music industry colors"
            },
            
            # Sports and Fitness
            "sports_professional": {
                "colors": ["champion_gold", "victory_blue", "energy_red", "performance_white", "strength_black"],
                "tags": ["sports", "athletic", "competition", "performance"],
                "description": "Professional sports colors"
            },
            "fitness_gym": {
                "colors": ["energy_orange", "power_red", "endurance_blue", "strength_gray", "motivation_yellow"],
                "tags": ["fitness", "gym", "workout", "health"],
                "description": "Fitness gym colors"
            },
            "outdoor_adventure": {
                "colors": ["adventure_green", "mountain_gray", "sunset_orange", "sky_blue", "earth_brown"],
                "tags": ["outdoor", "adventure", "nature", "exploration"],
                "description": "Outdoor adventure colors"
            },
        }
        
        # Comprehensive industry-specific color mappings with detailed application contexts
        self.industry_color_mapping = {
            # Technology and Software
            "technology": {
                "primary": ["electric_blue", "cyber_green", "digital_white", "silicon_gray"],
                "accent": ["neon_blue", "laser_green", "chrome_silver", "ai_purple"],
                "backgrounds": ["tech_black", "circuit_gray", "data_blue", "cloud_white"],
                "contexts": ["software", "hardware", "AI", "robotics", "computing", "innovation"],
                "moods": ["futuristic", "precise", "intelligent", "cutting_edge"]
            },
            "healthcare": {
                "primary": ["medical_blue", "health_green", "clean_white", "care_teal"],
                "accent": ["emergency_red", "pharmacy_orange", "wellness_purple", "recovery_yellow"],
                "backgrounds": ["hospital_white", "scrubs_blue", "clinic_gray", "healing_beige"],
                "contexts": ["medicine", "treatment", "wellness", "emergency", "prevention"],
                "moods": ["caring", "clean", "professional", "trustworthy"]
            },
            "finance": {
                "primary": ["finance_blue", "money_green", "gold_standard", "trust_gray"],
                "accent": ["investment_purple", "growth_cyan", "profit_orange", "security_red"],
                "backgrounds": ["bank_white", "vault_black", "statement_gray", "portfolio_beige"],
                "contexts": ["banking", "investment", "insurance", "trading", "wealth_management"],
                "moods": ["trustworthy", "stable", "prosperous", "secure"]
            },
            "retail": {
                "primary": ["retail_red", "shopping_blue", "sale_orange", "store_white"],
                "accent": ["discount_yellow", "brand_purple", "customer_green", "checkout_cyan"],
                "backgrounds": ["shop_beige", "display_gray", "online_white", "mobile_blue"],
                "contexts": ["shopping", "sales", "customer_service", "inventory", "merchandising"],
                "moods": ["welcoming", "exciting", "accessible", "convenient"]
            },
            "education": {
                "primary": ["education_blue", "knowledge_green", "learning_orange", "book_white"],
                "accent": ["pencil_yellow", "marker_red", "crayon_purple", "chalk_gray"],
                "backgrounds": ["classroom_beige", "library_brown", "campus_green", "study_white"],
                "contexts": ["K-12", "higher_education", "online_learning", "training", "research"],
                "moods": ["inspiring", "encouraging", "focused", "growth-oriented"]
            },
            "entertainment": {
                "primary": ["show_red", "stage_gold", "audience_purple", "spotlight_white"],
                "accent": ["ticket_blue", "popcorn_yellow", "screen_black", "sound_silver"],
                "backgrounds": ["theater_red", "cinema_black", "concert_dark", "festival_bright"],
                "contexts": ["movies", "music", "theater", "gaming", "streaming"],
                "moods": ["exciting", "glamorous", "entertaining", "immersive"]
            },
            "food_beverage": {
                "primary": ["appetite_red", "fresh_green", "natural_brown", "pure_white"],
                "accent": ["spice_orange", "fruit_yellow", "herb_green", "wine_purple"],
                "backgrounds": ["kitchen_beige", "farm_green", "restaurant_black", "home_white"],
                "contexts": ["restaurants", "food_production", "beverages", "catering", "organic"],
                "moods": ["appetizing", "fresh", "natural", "satisfying"]
            },
            "automotive": {
                "primary": ["auto_red", "performance_black", "luxury_silver", "safety_white"],
                "accent": ["speed_orange", "electric_green", "chrome_blue", "racing_yellow"],
                "backgrounds": ["showroom_white", "garage_gray", "road_black", "factory_steel"],
                "contexts": ["manufacturing", "dealership", "service", "racing", "electric_vehicles"],
                "moods": ["powerful", "premium", "innovative", "exciting"]
            },
            "sports": {
                "primary": ["team_red", "victory_gold", "field_green", "uniform_white"],
                "accent": ["energy_orange", "power_blue", "speed_yellow", "strength_black"],
                "backgrounds": ["stadium_grass", "court_wood", "pool_blue", "gym_gray"],
                "contexts": ["professional_sports", "amateur", "youth", "fitness", "recreation"],
                "moods": ["energetic", "competitive", "powerful", "inspiring"]
            },
            "real_estate": {
                "primary": ["property_blue", "home_green", "investment_gold", "mortgage_white"],
                "accent": ["listing_red", "market_orange", "equity_purple", "contract_gray"],
                "backgrounds": ["office_beige", "home_white", "luxury_black", "commercial_steel"],
                "contexts": ["residential", "commercial", "luxury", "investment", "property_management"],
                "moods": ["trustworthy", "aspirational", "stable", "professional"]
            }
        }
        
        # Seasonal color palettes
        self.seasonal_palettes = {
            "spring_fresh": {
                "colors": ["fresh_green", "cherry_blossom", "sky_blue", "daffodil_yellow", "lavender"],
                "tags": ["spring_colors", "fresh_palette", "blooming", "renewal"],
                "description": "Fresh spring colors"
            },
            "summer_bright": {
                "colors": ["sunshine_yellow", "ocean_blue", "coral_pink", "lime_green", "white"],
                "tags": ["summer_colors", "bright_palette", "sunny", "vibrant"],
                "description": "Bright summer colors"
            },
            "autumn_warm": {
                "colors": ["maple_red", "pumpkin_orange", "golden_yellow", "chestnut_brown", "rust"],
                "tags": ["autumn_colors", "warm_palette", "harvest", "cozy"],
                "description": "Warm autumn colors"
            },
            "winter_cool": {
                "colors": ["ice_blue", "snow_white", "pine_green", "silver_gray", "midnight_blue"],
                "tags": ["winter_colors", "cool_palette", "crisp", "serene"],
                "description": "Cool winter colors"
            }
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        instance = cls()
        
        harmony_options = ["auto"] + list(instance.harmony_schemes.keys())
        mood_options = ["auto"] + list(instance.mood_palettes.keys())
        cultural_options = ["none"] + list(instance.cultural_palettes.keys())
        professional_options = ["none"] + list(instance.professional_palettes.keys())
        industry_options = ["none"] + list(instance.industry_color_mapping.keys())
        seasonal_options = ["none"] + list(instance.seasonal_palettes.keys())
        
        return {
            "required": {
                "base_prompt": ("STRING", {"forceInput": True}),
                "color_approach": (["harmony_theory", "mood_based", "cultural", "professional", "industry", "seasonal", "custom"], {"default": "mood_based"}),
                "color_intensity": (["subtle", "moderate", "vibrant", "intense"], {"default": "moderate"}),
            },
            "optional": {
                # Color Theory
                "harmony_scheme": (harmony_options, {"default": "auto"}),
                "color_temperature": (["auto", "warm", "cool", "neutral", "mixed"], {"default": "auto"}),
                "saturation_level": (["auto", "desaturated", "moderate", "saturated", "vivid"], {"default": "auto"}),
                
                # Mood and Style
                "mood_palette": (mood_options, {"default": "auto"}),
                "cultural_palette": (cultural_options, {"default": "none"}),
                "professional_palette": (professional_options, {"default": "none"}),
                "industry_palette": (industry_options, {"default": "none"}),
                "seasonal_palette": (seasonal_options, {"default": "none"}),
                
                # Technical Controls
                "color_balance": (["auto", "warm_highlight", "cool_highlight", "neutral_balance"], {"default": "auto"}),
                "contrast_level": (["low", "moderate", "high", "dramatic"], {"default": "moderate"}),
                "brightness_bias": (["auto", "darker", "balanced", "brighter"], {"default": "auto"}),
                
                # Accessibility
                "accessibility_mode": ("BOOLEAN", {"default": False}),
                "colorblind_friendly": ("BOOLEAN", {"default": False}),
                
                # Creative Controls
                "gradient_flow": ("BOOLEAN", {"default": False}),
                "color_accents": (["none", "single", "dual", "multiple"], {"default": "single"}),
                "metallic_elements": (["none", "gold", "silver", "copper", "mixed"], {"default": "none"}),
                
                # Enhancement
                "color_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "context_awareness": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "color_summary")
    FUNCTION = "harmonize_colors"
    CATEGORY = "Camera Factory Station"
    
    def analyze_prompt_for_colors(self, prompt):
        """Analyze prompt to understand existing color context"""
        prompt_lower = prompt.lower()
        
        detected_colors = []
        color_keywords = {
            "red": ["red", "crimson", "scarlet", "ruby"],
            "blue": ["blue", "azure", "navy", "sapphire"],
            "green": ["green", "emerald", "forest", "jade"],
            "yellow": ["yellow", "golden", "amber", "citrine"],
            "orange": ["orange", "coral", "peach", "sunset"],
            "purple": ["purple", "violet", "lavender", "amethyst"],
            "pink": ["pink", "rose", "magenta", "blush"],
            "brown": ["brown", "tan", "beige", "earth"],
            "black": ["black", "dark", "ebony", "charcoal"],
            "white": ["white", "ivory", "cream", "pearl"],
            "gray": ["gray", "grey", "silver", "platinum"]
        }
        
        for color, keywords in color_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_colors.append(color)
        
        # Analyze mood indicators
        mood_indicators = {
            "warm": ["warm", "cozy", "sunny", "cheerful", "energetic"],
            "cool": ["cool", "calm", "serene", "peaceful", "crisp"],
            "dramatic": ["dramatic", "intense", "bold", "striking"],
            "soft": ["soft", "gentle", "delicate", "subtle", "muted"],
            "vibrant": ["vibrant", "bright", "vivid", "colorful", "lively"]
        }
        
        detected_mood = "neutral"
        for mood, keywords in mood_indicators.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_mood = mood
                break
        
        return {
            "existing_colors": detected_colors,
            "mood_context": detected_mood,
            "has_color_info": len(detected_colors) > 0
        }
    
    def select_palette_based_on_approach(self, approach, context, **kwargs):
        """Select appropriate palette based on chosen approach"""
        if approach == "harmony_theory":
            scheme = kwargs.get("harmony_scheme", "auto")
            if scheme == "auto":
                # Choose based on existing colors and mood
                if context["mood_context"] in ["dramatic", "vibrant"]:
                    scheme = "complementary"
                elif context["mood_context"] in ["soft", "gentle"]:
                    scheme = "analogous"
                else:
                    scheme = random.choice(["analogous", "complementary", "triadic"])
            return self.harmony_schemes[scheme]
        
        elif approach == "mood_based":
            mood = kwargs.get("mood_palette", "auto")
            if mood == "auto":
                mood_map = {
                    "warm": "warm_energetic",
                    "cool": "cool_calming",
                    "dramatic": "jewel_rich",
                    "soft": "pastel_soft",
                    "vibrant": "neon_electric"
                }
                mood = mood_map.get(context["mood_context"], "earth_natural")
            return self.mood_palettes[mood]
        
        elif approach == "cultural":
            cultural = kwargs.get("cultural_palette", "japanese_zen")
            if cultural == "none":
                # Fall back to mood-based approach
                return self.mood_palettes["earth_natural"]
            return self.cultural_palettes[cultural]
        
        elif approach == "professional":
            professional = kwargs.get("professional_palette", "corporate_trust")
            if professional == "none":
                # Fall back to mood-based approach
                return self.mood_palettes["earth_natural"]
            return self.professional_palettes[professional]
        
        elif approach == "industry":
            industry = kwargs.get("industry_palette", "technology")
            if industry == "none":
                # Fall back to mood-based approach
                return self.mood_palettes["earth_natural"]
            industry_mapping = self.industry_color_mapping[industry]
            # Convert industry mapping to standard palette format
            return {
                "colors": industry_mapping["primary"] + industry_mapping["accent"][:2],
                "tags": industry_mapping["contexts"] + industry_mapping["moods"],
                "description": f"{industry.replace('_', ' ').title()} industry colors"
            }
        
        elif approach == "seasonal":
            seasonal = kwargs.get("seasonal_palette", "spring_fresh")
            if seasonal == "none":
                # Fall back to mood-based approach
                return self.mood_palettes["earth_natural"]
            return self.seasonal_palettes[seasonal]
        
        # Default fallback
        return self.mood_palettes["earth_natural"]
    
    def generate_color_tags(self, palette, intensity, **kwargs):
        """Generate color-related tags based on palette and settings"""
        tags = []
        
        # Base palette tags
        tags.extend(palette["tags"])
        
        # Add specific colors if intensity allows
        if intensity in ["moderate", "vibrant", "intense"]:
            # Select 2-3 colors from the palette
            selected_colors = random.sample(palette["colors"], min(3, len(palette["colors"])))
            tags.extend(selected_colors)
        
        # Intensity modifiers
        intensity_tags = {
            "subtle": ["muted", "understated", "refined"],
            "moderate": ["balanced", "harmonious", "pleasing"],
            "vibrant": ["vibrant", "rich", "saturated"],
            "intense": ["intense", "bold", "striking", "vivid"]
        }
        tags.extend(intensity_tags[intensity])
        
        # Temperature tags
        temp = kwargs.get("color_temperature", "auto")
        if temp != "auto":
            temp_tags = {
                "warm": ["warm_tones", "cozy_warmth", "golden_glow"],
                "cool": ["cool_tones", "refreshing", "crisp_coolness"],
                "neutral": ["neutral_balance", "even_temperature"],
                "mixed": ["temperature_contrast", "warm_cool_balance"]
            }
            tags.extend(temp_tags.get(temp, []))
        
        # Saturation tags
        saturation = kwargs.get("saturation_level", "auto")
        if saturation != "auto":
            sat_tags = {
                "desaturated": ["desaturated", "muted_colors", "faded"],
                "moderate": ["balanced_saturation", "natural_colors"],
                "saturated": ["saturated_colors", "rich_hues"],
                "vivid": ["vivid_colors", "pure_hues", "chromatic"]
            }
            tags.extend(sat_tags.get(saturation, []))
        
        # Contrast tags
        contrast = kwargs.get("contrast_level", "moderate")
        contrast_tags = {
            "low": ["low_contrast", "subtle_variation", "gentle"],
            "moderate": ["balanced_contrast", "harmonious"],
            "high": ["high_contrast", "dramatic_difference"],
            "dramatic": ["extreme_contrast", "bold_opposition", "striking"]
        }
        tags.extend(contrast_tags[contrast])
        
        # Special effects
        if kwargs.get("gradient_flow", False):
            tags.extend(["color_gradient", "flowing_colors", "smooth_transition"])
        
        if kwargs.get("metallic_elements", "none") != "none":
            metallic = kwargs.get("metallic_elements")
            if metallic == "mixed":
                tags.extend(["metallic_accents", "mixed_metals", "lustrous"])
            else:
                tags.extend([f"{metallic}_accents", "metallic_finish", "reflective"])
        
        # Accessibility considerations
        if kwargs.get("accessibility_mode", False):
            tags.extend(["high_contrast", "accessible_colors", "readable"])
        
        if kwargs.get("colorblind_friendly", False):
            tags.extend(["colorblind_safe", "universal_colors", "inclusive_palette"])
        
        return tags
    
    def apply_emphasis(self, tag, emphasis_level):
        """Apply emphasis brackets based on level"""
        if emphasis_level == "low":
            return f"({tag})"
        elif emphasis_level == "high":
            return f"(({tag}))"
        elif emphasis_level == "very_high":
            return f"((({tag})))"
        else:  # medium
            return tag
    
    def harmonize_colors(self, base_prompt, color_approach, color_intensity, **kwargs):
        """Main function to harmonize colors in the prompt"""
        
        # Analyze existing prompt for color context
        try:
            context = self.analyze_prompt_for_colors(base_prompt) if kwargs.get("context_awareness", True) else {}
        except Exception as e:
            # Fallback context in case of analysis error
            context = {
                "existing_colors": [],
                "mood_context": "neutral",
                "has_color_info": False
            }
        
        # Ensure context has required keys
        if not isinstance(context, dict):
            context = {}
        context.setdefault("existing_colors", [])
        context.setdefault("mood_context", "neutral")
        context.setdefault("has_color_info", False)
        
        # Select appropriate palette
        try:
            selected_palette = self.select_palette_based_on_approach(color_approach, context, **kwargs)
        except Exception as e:
            # Fallback to a safe default palette
            selected_palette = self.mood_palettes["earth_natural"]
        
        # Generate color tags
        try:
            color_tags = self.generate_color_tags(selected_palette, color_intensity, **kwargs)
        except Exception as e:
            # Fallback tags
            color_tags = ["natural_colors", "balanced_palette", "harmonious"]
        
        # Apply emphasis
        emphasis_level = kwargs.get("color_emphasis", "medium")
        try:
            emphasized_tags = [self.apply_emphasis(tag, emphasis_level) for tag in color_tags]
        except Exception as e:
            emphasized_tags = color_tags
        
        # Create enhanced prompt
        enhanced_prompt = f"{base_prompt}, {', '.join(emphasized_tags)}"
        
        # Create summary
        try:
            summary_parts = [
                f"🎨 Color Harmony Applied:",
                f"• Approach: {color_approach}",
                f"• Palette: {selected_palette.get('description', 'Color palette')}",
                f"• Intensity: {color_intensity}",
            ]
            
            if context.get("existing_colors"):
                summary_parts.append(f"• Detected Colors: {', '.join(context['existing_colors'])}")
            
            if context.get("mood_context") != "neutral":
                summary_parts.append(f"• Mood Context: {context['mood_context']}")
            
            # Add technical settings
            technical_settings = []
            for key in ["color_temperature", "saturation_level", "contrast_level"]:
                value = kwargs.get(key, "auto")
                if value != "auto":
                    technical_settings.append(f"{key.replace('_', ' ').title()}: {value}")
            
            if technical_settings:
                summary_parts.append(f"• Technical: {', '.join(technical_settings)}")
            
            if emphasis_level != "medium":
                summary_parts.append(f"• Emphasis: {emphasis_level}")
            
            summary_parts.append(f"• Color Tags Added: {len(color_tags)}")
            
            color_summary = "\n".join(summary_parts)
        except Exception as e:
            color_summary = f"🎨 Color Harmony Applied: {color_approach} approach with {color_intensity} intensity"
        
        return (enhanced_prompt, color_summary)
