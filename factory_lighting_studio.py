#!/usr/bin/env python3

"""
Factory Lighting Studio - Professional Lighting Design and Control
Provides lighting setups, natural conditions, and studio equipment simulation.

SFW Edition - GitHub Compliant - Professional Grade
"""

import random
import math

class FactoryLightingStudio:
    """
    Professional lighting studio node that simulates various lighting conditions,
    studio setups, and natural lighting scenarios with technical precision.
    """
    
    def __init__(self):
        # Comprehensive studio lighting setups covering all professional scenarios
        self.studio_setups = {
            # Classic Portrait Setups
            "three_point_classic": {
                "description": "Classic three-point lighting with key, fill, and rim",
                "components": ["key_light", "fill_light", "rim_light"],
                "tags": ["three_point_lighting", "classic_setup", "professional", "balanced"],
                "mood": "professional"
            },
            "rembrandt_portrait": {
                "description": "Rembrandt lighting with characteristic triangle",
                "components": ["angled_key_light", "minimal_fill", "shadow_play"],
                "tags": ["rembrandt_lighting", "portrait_style", "dramatic_shadows", "artistic"],
                "mood": "dramatic"
            },
            "butterfly_glamour": {
                "description": "Butterfly lighting for glamour and beauty",
                "components": ["overhead_key", "under_eye_fill", "hair_light"],
                "tags": ["butterfly_lighting", "glamour_style", "beauty_lighting", "symmetrical"],
                "mood": "glamorous"
            },
            "split_dramatic": {
                "description": "Split lighting for dramatic effect",
                "components": ["side_key_light", "no_fill", "deep_shadows"],
                "tags": ["split_lighting", "dramatic_effect", "half_shadow", "moody"],
                "mood": "intense"
            },
            "broad_commercial": {
                "description": "Broad lighting for commercial applications",
                "components": ["broad_key_light", "even_fill", "background_light"],
                "tags": ["broad_lighting", "commercial_style", "even_illumination", "clean"],
                "mood": "clean"
            },
            "short_slimming": {
                "description": "Short lighting for slimming effect",
                "components": ["shadow_side_key", "subtle_fill", "contouring_shadows"],
                "tags": ["short_lighting", "slimming_effect", "flattering", "dimensional"],
                "mood": "flattering"
            },
            "loop_natural": {
                "description": "Loop lighting for natural portrait look",
                "components": ["slightly_off_center_key", "nose_shadow_loop", "natural_fill"],
                "tags": ["loop_lighting", "natural_portrait", "versatile", "everyday"],
                "mood": "natural"
            },
            
            # Beauty and Fashion Setups
            "beauty_dish_glamour": {
                "description": "Beauty dish for flawless skin rendering",
                "components": ["beauty_dish_key", "reflector_fill", "hair_separation"],
                "tags": ["beauty_dish", "flawless_skin", "fashion_beauty", "soft_shadows"],
                "mood": "beautiful"
            },
            "ring_light_even": {
                "description": "Ring light for even shadowless illumination",
                "components": ["ring_light_source", "catch_light_eyes", "even_coverage"],
                "tags": ["ring_light", "shadowless", "beauty_lighting", "modern"],
                "mood": "contemporary"
            },
            "softbox_fashion": {
                "description": "Large softbox for fashion photography",
                "components": ["large_softbox", "gradual_falloff", "soft_wrap_around"],
                "tags": ["softbox_lighting", "fashion_style", "soft_light", "professional"],
                "mood": "editorial"
            },
            "octabox_portrait": {
                "description": "Octagonal softbox for natural light simulation",
                "components": ["octagonal_softbox", "natural_catchlight", "round_falloff"],
                "tags": ["octabox", "natural_simulation", "round_catchlight", "flattering"],
                "mood": "natural"
            },
            "strip_light_edge": {
                "description": "Strip light for edge lighting effects",
                "components": ["strip_softbox", "edge_illumination", "body_contouring"],
                "tags": ["strip_light", "edge_lighting", "body_sculpting", "dramatic"],
                "mood": "sculptural"
            },
            
            # Commercial and Product Setups
            "high_key_commercial": {
                "description": "High key lighting for bright commercial look",
                "components": ["multiple_softboxes", "white_background", "minimal_shadows"],
                "tags": ["high_key_lighting", "bright_commercial", "clean_background", "optimistic"],
                "mood": "bright"
            },
            "low_key_dramatic": {
                "description": "Low key lighting for dramatic mood",
                "components": ["single_key_light", "black_background", "deep_shadows"],
                "tags": ["low_key_lighting", "dramatic_mood", "mystery", "selective_illumination"],
                "mood": "mysterious"
            },
            "product_table_top": {
                "description": "Table top product lighting setup",
                "components": ["overhead_softbox", "side_fill_cards", "reflection_control"],
                "tags": ["product_lighting", "table_top", "commercial_photography", "detail_clarity"],
                "mood": "clinical"
            },
            "jewelry_macro": {
                "description": "Specialized jewelry and macro lighting",
                "components": ["ring_flash", "fiber_optic_spots", "reflection_elimination"],
                "tags": ["jewelry_lighting", "macro_illumination", "sparkle_enhancement", "precision"],
                "mood": "pristine"
            },
            "automotive_studio": {
                "description": "Automotive studio lighting setup",
                "components": ["large_area_lights", "gradient_background", "reflection_management"],
                "tags": ["automotive_lighting", "large_scale", "reflective_surfaces", "industrial"],
                "mood": "powerful"
            },
            
            # Environmental and Natural Simulation
            "window_light_sim": {
                "description": "Natural window light simulation",
                "components": ["large_softbox_window", "direction_control", "time_variation"],
                "tags": ["window_light", "natural_simulation", "soft_directional", "home_like"],
                "mood": "domestic"
            },
            "outdoor_shade_sim": {
                "description": "Open shade outdoor lighting simulation",
                "components": ["large_diffused_source", "blue_sky_fill", "even_coverage"],
                "tags": ["outdoor_shade", "even_lighting", "cool_temperature", "natural"],
                "mood": "serene"
            },
            "golden_hour_sim": {
                "description": "Golden hour warm light simulation",
                "components": ["warm_key_light", "orange_gels", "low_angle_direction"],
                "tags": ["golden_hour", "warm_lighting", "romantic_glow", "sunset_simulation"],
                "mood": "romantic"
            },
            "overcast_sim": {
                "description": "Overcast sky lighting simulation",
                "components": ["large_overhead_diffusion", "even_soft_light", "neutral_temperature"],
                "tags": ["overcast_lighting", "soft_even", "diffused_sky", "portrait_friendly"],
                "mood": "gentle"
            },
            "dappled_shade_sim": {
                "description": "Dappled forest shade simulation",
                "components": ["gobo_patterns", "varied_light_spots", "green_color_cast"],
                "tags": ["dappled_light", "forest_shade", "pattern_light", "organic"],
                "mood": "natural"
            },
            
            # Cinematic and Artistic Setups
            "film_noir_classic": {
                "description": "Classic film noir lighting style",
                "components": ["hard_key_light", "venetian_blind_gobo", "dramatic_shadows"],
                "tags": ["film_noir", "hard_shadows", "dramatic_contrast", "classic_cinema"],
                "mood": "noir"
            },
            "sci_fi_futuristic": {
                "description": "Science fiction futuristic lighting",
                "components": ["colored_led_panels", "haze_atmosphere", "neon_accents"],
                "tags": ["sci_fi_lighting", "futuristic_mood", "colored_light", "atmospheric"],
                "mood": "futuristic"
            },
            "horror_dramatic": {
                "description": "Horror genre dramatic lighting",
                "components": ["bottom_light", "colored_gels", "shadow_play"],
                "tags": ["horror_lighting", "dramatic_shadows", "unnatural_direction", "ominous"],
                "mood": "ominous"
            },
            "music_video_dynamic": {
                "description": "Dynamic music video lighting",
                "components": ["moving_lights", "color_changing", "rhythmic_patterns"],
                "tags": ["music_video", "dynamic_lighting", "color_effects", "energetic"],
                "mood": "energetic"
            },
            "stage_theatrical": {
                "description": "Theatrical stage lighting setup",
                "components": ["multiple_spots", "colored_washes", "dramatic_angles"],
                "tags": ["stage_lighting", "theatrical", "multiple_sources", "performance"],
                "mood": "theatrical"
            },
            
            # Specialized Professional Setups
            "corporate_headshot": {
                "description": "Corporate headshot lighting setup",
                "components": ["softbox_key", "reflector_fill", "gradient_background"],
                "tags": ["corporate_lighting", "professional_headshot", "business_appropriate", "trustworthy"],
                "mood": "professional"
            },
            "editorial_magazine": {
                "description": "Editorial magazine lighting style",
                "components": ["dramatic_key", "creative_shadows", "artistic_vision"],
                "tags": ["editorial_lighting", "magazine_style", "creative_shadows", "storytelling"],
                "mood": "editorial"
            },
            "e_commerce_clean": {
                "description": "E-commerce product lighting",
                "components": ["even_illumination", "white_background", "shadow_elimination"],
                "tags": ["e_commerce", "product_photography", "clean_lighting", "sales_ready"],
                "mood": "commercial"
            },
            "lifestyle_natural": {
                "description": "Lifestyle photography natural lighting",
                "components": ["mixed_natural_artificial", "realistic_shadows", "home_environment"],
                "tags": ["lifestyle_lighting", "natural_mixed", "authentic_feel", "relatable"],
                "mood": "authentic"
            },
            "food_styling": {
                "description": "Food photography styling lighting",
                "components": ["directional_key", "bounce_fill", "texture_enhancement"],
                "tags": ["food_lighting", "texture_emphasis", "appetizing_glow", "culinary"],
                "mood": "appetizing"
            },
            
            # Event and Documentary Setups
            "wedding_romantic": {
                "description": "Wedding photography romantic lighting",
                "components": ["soft_key_light", "warm_temperature", "flattering_fill"],
                "tags": ["wedding_lighting", "romantic_mood", "soft_flattering", "celebration"],
                "mood": "romantic"
            },
            "event_coverage": {
                "description": "Event coverage lighting setup",
                "components": ["mobile_lighting", "bounce_flash", "ambient_balance"],
                "tags": ["event_lighting", "mobile_setup", "natural_balance", "documentary"],
                "mood": "celebratory"
            },
            "conference_speaker": {
                "description": "Conference speaker lighting",
                "components": ["front_key_light", "background_separation", "professional_clarity"],
                "tags": ["conference_lighting", "speaker_illumination", "clear_visibility", "business"],
                "mood": "authoritative"
            },
            "concert_performance": {
                "description": "Concert performance lighting",
                "components": ["stage_spots", "colored_washes", "dramatic_backlighting"],
                "tags": ["concert_lighting", "performance_illumination", "dynamic_colors", "entertainment"],
                "mood": "energetic"
            },
            
            # Technical and Scientific Setups
            "medical_clinical": {
                "description": "Medical clinical lighting setup",
                "components": ["even_white_light", "shadow_elimination", "accurate_color"],
                "tags": ["medical_lighting", "clinical_accuracy", "sterile_environment", "documentation"],
                "mood": "clinical"
            },
            "scientific_documentation": {
                "description": "Scientific documentation lighting",
                "components": ["precise_illumination", "color_accuracy", "detail_emphasis"],
                "tags": ["scientific_lighting", "documentation", "accurate_reproduction", "technical"],
                "mood": "technical"
            },
            "forensic_evidence": {
                "description": "Forensic evidence lighting",
                "components": ["raking_light", "texture_revelation", "shadow_detail"],
                "tags": ["forensic_lighting", "evidence_documentation", "detail_revelation", "investigative"],
                "mood": "investigative"
            },
            "art_reproduction": {
                "description": "Art reproduction lighting setup",
                "components": ["even_cross_lighting", "color_accuracy", "glare_elimination"],
                "tags": ["art_lighting", "reproduction_quality", "museum_standard", "archival"],
                "mood": "preservation"
            }
        }
        
        # Natural lighting conditions
        self.natural_lighting = {
            "golden_hour": {
                "description": "Warm golden hour lighting",
                "characteristics": ["warm_temperature", "low_angle", "soft_shadows", "golden_glow"],
                "tags": ["golden_hour", "warm_light", "magic_hour", "romantic_lighting"],
                "time": "sunset/sunrise"
            },
            "blue_hour": {
                "description": "Cool blue hour atmosphere",
                "characteristics": ["cool_temperature", "even_lighting", "twilight_blue", "atmospheric"],
                "tags": ["blue_hour", "twilight", "cool_lighting", "atmospheric_blue"],
                "time": "twilight"
            },
            "noon_harsh": {
                "description": "Direct midday sunlight",
                "characteristics": ["hard_shadows", "high_contrast", "bright_highlights", "intense"],
                "tags": ["noon_sun", "harsh_lighting", "strong_shadows", "bright_daylight"],
                "time": "midday"
            },
            "overcast_soft": {
                "description": "Soft overcast lighting",
                "characteristics": ["diffused_light", "soft_shadows", "even_coverage", "muted"],
                "tags": ["overcast", "soft_lighting", "diffused", "cloudy_sky"],
                "time": "cloudy"
            },
            "window_natural": {
                "description": "Natural window lighting",
                "characteristics": ["directional_soft", "gradual_falloff", "natural_color", "authentic"],
                "tags": ["window_light", "natural_indoor", "soft_directional", "authentic_lighting"],
                "time": "daytime"
            },
            "shade_open": {
                "description": "Open shade lighting",
                "characteristics": ["cool_shadows", "reflected_light", "soft_contrast", "peaceful"],
                "tags": ["open_shade", "reflected_lighting", "cool_shadows", "gentle"],
                "time": "shaded"
            },
            "backlit_rim": {
                "description": "Backlighting with rim effect",
                "characteristics": ["rim_lighting", "silhouette_potential", "dramatic_contrast", "ethereal"],
                "tags": ["backlit", "rim_lighting", "silhouette", "dramatic_backlight"],
                "time": "variable"
            },
            "filtered_dappled": {
                "description": "Dappled light through foliage",
                "characteristics": ["filtered_light", "pattern_shadows", "organic_patterns", "natural"],
                "tags": ["dappled_light", "filtered_sunlight", "leaf_shadows", "organic_lighting"],
                "time": "under_trees"
            }
        }
        
        # Professional equipment simulation
        self.equipment_types = {
            "softbox_large": {
                "description": "Large softbox for soft, even lighting",
                "characteristics": ["soft_light", "large_source", "even_coverage", "professional"],
                "tags": ["softbox", "soft_lighting", "professional_equipment", "even_illumination"],
                "size": "large"
            },
            "umbrella_reflective": {
                "description": "Reflective umbrella for broad coverage",
                "characteristics": ["broad_coverage", "soft_shadows", "reflective_quality", "versatile"],
                "tags": ["umbrella_lighting", "reflective", "broad_coverage", "studio_standard"],
                "size": "medium"
            },
            "beauty_dish": {
                "description": "Beauty dish for glamour lighting",
                "characteristics": ["controlled_spill", "catchlight_quality", "beauty_specific", "focused"],
                "tags": ["beauty_dish", "glamour_lighting", "controlled_light", "portrait_specialist"],
                "size": "medium"
            },
            "ring_light": {
                "description": "Ring light for even facial lighting",
                "characteristics": ["shadowless", "even_facial", "circular_catchlight", "modern"],
                "tags": ["ring_light", "shadowless_lighting", "circular_catchlight", "modern_style"],
                "size": "small"
            },
            "strip_box": {
                "description": "Strip softbox for edge lighting",
                "characteristics": ["narrow_beam", "edge_lighting", "controlled_width", "accent"],
                "tags": ["strip_light", "edge_lighting", "narrow_beam", "accent_light"],
                "size": "narrow"
            },
            "grid_spot": {
                "description": "Grid spot for controlled lighting",
                "characteristics": ["focused_beam", "controlled_spill", "precise_placement", "dramatic"],
                "tags": ["grid_spot", "controlled_beam", "precise_lighting", "dramatic_focus"],
                "size": "focused"
            },
            "parabolic_reflector": {
                "description": "Parabolic reflector for powerful directional light",
                "characteristics": ["powerful_output", "sharp_shadows", "directional", "high_contrast"],
                "tags": ["parabolic", "powerful_light", "sharp_shadows", "directional_lighting"],
                "size": "large"
            },
            "octobox_giant": {
                "description": "Giant octagonal softbox",
                "characteristics": ["huge_source", "wrap_around", "soft_shadows", "luxurious"],
                "tags": ["octabox", "giant_softbox", "wrap_around_light", "luxury_lighting"],
                "size": "giant"
            }
        }
        
        # Lighting moods and atmospheres
        self.lighting_moods = {
            "cinematic_dramatic": {
                "description": "Cinematic dramatic lighting",
                "characteristics": ["high_contrast", "selective_lighting", "mood_driven", "storytelling"],
                "tags": ["cinematic_lighting", "dramatic_mood", "high_contrast", "film_style"],
                "emotion": "dramatic"
            },
            "commercial_clean": {
                "description": "Clean commercial lighting",
                "characteristics": ["even_lighting", "minimal_shadows", "product_focused", "neutral"],
                "tags": ["commercial_lighting", "clean_style", "product_lighting", "neutral_mood"],
                "emotion": "professional"
            },
            "romantic_soft": {
                "description": "Romantic soft lighting",
                "characteristics": ["warm_temperature", "soft_shadows", "gentle_gradients", "intimate"],
                "tags": ["romantic_lighting", "soft_mood", "warm_glow", "intimate_atmosphere"],
                "emotion": "romantic"
            },
            "mysterious_moody": {
                "description": "Mysterious moody lighting",
                "characteristics": ["low_key", "deep_shadows", "selective_highlights", "enigmatic"],
                "tags": ["mysterious_lighting", "moody_atmosphere", "low_key", "shadow_play"],
                "emotion": "mysterious"
            },
            "energetic_bright": {
                "description": "Energetic bright lighting",
                "characteristics": ["high_key", "bright_overall", "minimal_shadows", "vibrant"],
                "tags": ["bright_lighting", "energetic_mood", "high_key", "vibrant_atmosphere"],
                "emotion": "energetic"
            },
            "vintage_nostalgic": {
                "description": "Vintage nostalgic lighting",
                "characteristics": ["warm_tint", "soft_contrast", "aged_quality", "nostalgic"],
                "tags": ["vintage_lighting", "nostalgic_mood", "warm_tint", "aged_atmosphere"],
                "emotion": "nostalgic"
            },
            "futuristic_cool": {
                "description": "Futuristic cool lighting",
                "characteristics": ["cool_temperature", "clean_lines", "technological", "modern"],
                "tags": ["futuristic_lighting", "cool_mood", "technological", "modern_atmosphere"],
                "emotion": "futuristic"
            },
            "natural_organic": {
                "description": "Natural organic lighting",
                "characteristics": ["realistic_shadows", "natural_color", "organic_patterns", "authentic"],
                "tags": ["natural_lighting", "organic_mood", "realistic", "authentic_atmosphere"],
                "emotion": "natural"
            }
        }
        
        # Technical lighting parameters
        self.lighting_ratios = {
            "1_to_1": {"description": "Even lighting ratio", "contrast": "low"},
            "2_to_1": {"description": "Gentle lighting ratio", "contrast": "moderate"},
            "3_to_1": {"description": "Standard lighting ratio", "contrast": "normal"},
            "4_to_1": {"description": "Dramatic lighting ratio", "contrast": "high"},
            "8_to_1": {"description": "High contrast ratio", "contrast": "very_high"}
        }
        
        # Color temperature ranges
        self.color_temperatures = {
            "tungsten_warm": {"kelvin": "3200K", "description": "Warm tungsten", "tags": ["warm_tungsten", "3200K", "indoor_warm"]},
            "halogen_standard": {"kelvin": "3400K", "description": "Halogen standard", "tags": ["halogen", "3400K", "warm_white"]},
            "daylight_balanced": {"kelvin": "5600K", "description": "Daylight balanced", "tags": ["daylight_balanced", "5600K", "neutral_white"]},
            "overcast_cool": {"kelvin": "6500K", "description": "Overcast daylight", "tags": ["overcast_daylight", "6500K", "cool_white"]},
            "shade_blue": {"kelvin": "7500K", "description": "Open shade blue", "tags": ["shade_blue", "7500K", "cool_blue"]},
            "mixed_temperature": {"kelvin": "mixed", "description": "Mixed color temperatures", "tags": ["mixed_temperatures", "color_contrast", "temperature_variation"]}
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        instance = cls()
        
        studio_options = ["auto"] + list(instance.studio_setups.keys())
        natural_options = ["auto"] + list(instance.natural_lighting.keys())
        equipment_options = ["auto"] + list(instance.equipment_types.keys())
        mood_options = ["auto"] + list(instance.lighting_moods.keys())
        ratio_options = ["auto"] + list(instance.lighting_ratios.keys())
        temperature_options = ["auto"] + list(instance.color_temperatures.keys())
        
        return {
            "required": {
                "base_prompt": ("STRING", {"forceInput": True}),
                "lighting_approach": (["studio_professional", "natural_conditions", "equipment_simulation", "mood_atmospheric", "technical_control", "creative_artistic"], {"default": "mood_atmospheric"}),
                "lighting_quality": (["soft", "moderate", "dramatic", "cinematic"], {"default": "moderate"}),
            },
            "optional": {
                # Studio Controls
                "studio_setup": (studio_options, {"default": "auto"}),
                "lighting_ratio": (ratio_options, {"default": "auto"}),
                "key_light_angle": (["auto", "45_degrees", "60_degrees", "90_degrees", "side_light", "back_light"], {"default": "auto"}),
                
                # Natural Lighting
                "natural_condition": (natural_options, {"default": "auto"}),
                "time_of_day": (["auto", "sunrise", "morning", "noon", "afternoon", "sunset", "twilight", "night"], {"default": "auto"}),
                "weather_condition": (["auto", "clear", "partly_cloudy", "overcast", "stormy", "foggy"], {"default": "auto"}),
                
                # Equipment Simulation
                "primary_equipment": (equipment_options, {"default": "auto"}),
                "modifier_count": (["single", "dual", "multiple", "complex"], {"default": "dual"}),
                "equipment_size": (["auto", "compact", "standard", "large", "professional"], {"default": "auto"}),
                
                # Atmospheric Controls
                "lighting_mood": (mood_options, {"default": "auto"}),
                "atmosphere_density": (["clear", "light_haze", "atmospheric", "moody", "heavy"], {"default": "atmospheric"}),
                "environmental_interaction": ("BOOLEAN", {"default": True}),
                
                # Technical Parameters
                "color_temperature": (temperature_options, {"default": "auto"}),
                "light_falloff": (["auto", "rapid", "gradual", "minimal", "dramatic"], {"default": "auto"}),
                "shadow_detail": (["auto", "deep_shadows", "moderate_shadows", "lifted_shadows", "minimal_shadows"], {"default": "auto"}),
                
                # Creative Effects
                "practical_lights": ("BOOLEAN", {"default": False}),
                "lens_flare": (["none", "subtle", "moderate", "dramatic"], {"default": "none"}),
                "light_rays": ("BOOLEAN", {"default": False}),
                "volumetric_lighting": ("BOOLEAN", {"default": False}),
                
                # Advanced Controls
                "lighting_contrast": (["low", "moderate", "high", "extreme"], {"default": "moderate"}),
                "highlight_control": (["auto", "protected", "normal", "blown", "artistic"], {"default": "auto"}),
                "shadow_control": (["auto", "blocked", "detailed", "lifted", "artistic"], {"default": "auto"}),
                
                # Enhancement
                "lighting_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "context_awareness": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "lighting_summary")
    FUNCTION = "design_lighting"
    CATEGORY = "Camera Factory Station"
    
    def analyze_prompt_for_lighting(self, prompt):
        """Analyze prompt to understand existing lighting context"""
        prompt_lower = prompt.lower()
        
        # Detect existing lighting keywords
        lighting_keywords = {
            "studio": ["studio", "professional", "controlled"],
            "natural": ["sunlight", "daylight", "outdoor", "natural"],
            "dramatic": ["dramatic", "moody", "cinematic", "intense"],
            "soft": ["soft", "gentle", "diffused", "even"],
            "warm": ["warm", "golden", "sunset", "cozy"],
            "cool": ["cool", "blue", "morning", "crisp"],
            "artificial": ["neon", "led", "fluorescent", "artificial"]
        }
        
        detected_types = []
        for light_type, keywords in lighting_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_types.append(light_type)
        
        # Detect time and environment
        time_keywords = {
            "sunrise": ["sunrise", "dawn", "early morning"],
            "sunset": ["sunset", "dusk", "golden hour"],
            "night": ["night", "evening", "dark"],
            "day": ["day", "daylight", "noon", "afternoon"]
        }
        
        detected_time = "unknown"
        for time_period, keywords in time_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_time = time_period
                break
        
        # Detect environment
        environment_keywords = {
            "indoor": ["indoor", "inside", "studio", "room"],
            "outdoor": ["outdoor", "outside", "landscape", "nature"],
            "urban": ["city", "street", "urban", "building"],
            "natural": ["forest", "beach", "mountain", "field"]
        }
        
        detected_environment = "unknown"
        for env_type, keywords in environment_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_environment = env_type
                break
        
        return {
            "lighting_types": detected_types,
            "time_context": detected_time,
            "environment": detected_environment,
            "has_lighting_info": len(detected_types) > 0
        }
    
    def select_lighting_based_on_approach(self, approach, context, **kwargs):
        """Select appropriate lighting based on chosen approach"""
        if approach == "studio_professional":
            setup = kwargs.get("studio_setup", "auto")
            if setup == "auto":
                # Choose based on context
                if "dramatic" in context.get("lighting_types", []):
                    setup = "rembrandt_portrait"
                elif "soft" in context.get("lighting_types", []):
                    setup = "clamshell_beauty"
                else:
                    setup = "three_point_classic"
            
            # Validate key exists in dictionary
            if setup not in self.studio_setups:
                print(f"Warning: Studio setup '{setup}' not found, using 'three_point_classic'")
                setup = "three_point_classic"
            return self.studio_setups[setup]
        
        elif approach == "natural_conditions":
            condition = kwargs.get("natural_condition", "auto")
            if condition == "auto":
                time_map = {
                    "sunrise": "golden_hour",
                    "sunset": "golden_hour",
                    "night": "blue_hour",
                    "day": "overcast_soft"
                }
                condition = time_map.get(context.get("time_context", "unknown"), "window_natural")
            
            # Validate key exists in dictionary
            if condition not in self.natural_lighting:
                print(f"Warning: Natural condition '{condition}' not found, using 'window_natural'")
                condition = "window_natural"
            return self.natural_lighting[condition]
        
        elif approach == "equipment_simulation":
            equipment = kwargs.get("primary_equipment", "auto")
            if equipment == "auto":
                if "soft" in context.get("lighting_types", []):
                    equipment = "softbox_large"
                elif "dramatic" in context.get("lighting_types", []):
                    equipment = "grid_spot"
                else:
                    equipment = "umbrella_reflective"
            
            # Validate key exists in dictionary
            if equipment not in self.equipment_types:
                print(f"Warning: Equipment type '{equipment}' not found, using 'umbrella_reflective'")
                equipment = "umbrella_reflective"
            return self.equipment_types[equipment]
        
        elif approach == "mood_atmospheric":
            mood = kwargs.get("lighting_mood", "auto")
            if mood == "auto":
                if "dramatic" in context.get("lighting_types", []):
                    mood = "cinematic_dramatic"
                elif "soft" in context.get("lighting_types", []):
                    mood = "romantic_soft"
                else:
                    mood = "natural_organic"
            
            # Validate key exists in dictionary
            if mood not in self.lighting_moods:
                print(f"Warning: Lighting mood '{mood}' not found, using 'natural_organic'")
                mood = "natural_organic"
            return self.lighting_moods[mood]
        
        # Default fallback
        return self.lighting_moods.get("natural_organic", {
            "description": "Default natural lighting",
            "characteristics": ["natural", "organic", "realistic"],
            "tags": ["natural_lighting", "organic_mood", "realistic"],
            "emotion": "natural"
        })
    
    def generate_lighting_tags(self, lighting_config, quality, **kwargs):
        """Generate lighting-related tags based on configuration and settings"""
        tags = []
        
        # Base configuration tags
        if hasattr(lighting_config, 'get'):
            tags.extend(lighting_config.get("tags", []))
            
            # Add characteristics if available
            if "characteristics" in lighting_config:
                tags.extend(lighting_config["characteristics"])
        
        # Quality modifiers
        quality_tags = {
            "soft": ["soft_lighting", "gentle_illumination", "diffused"],
            "moderate": ["balanced_lighting", "natural_quality", "professional"],
            "dramatic": ["dramatic_lighting", "high_contrast", "cinematic"],
            "cinematic": ["cinematic_lighting", "film_quality", "artistic"]
        }
        tags.extend(quality_tags[quality])
        
        # Technical parameters
        ratio = kwargs.get("lighting_ratio", "auto")
        if ratio != "auto" and ratio in self.lighting_ratios:
            ratio_info = self.lighting_ratios[ratio]
            tags.extend([f"lighting_ratio_{ratio.replace('_to_', '_')}", ratio_info["contrast"] + "_contrast"])
        
        # Color temperature
        temperature = kwargs.get("color_temperature", "auto")
        if temperature != "auto" and temperature in self.color_temperatures:
            temp_info = self.color_temperatures[temperature]
            tags.extend(temp_info["tags"])
        
        # Environmental factors
        if kwargs.get("atmosphere_density", "atmospheric") != "clear":
            density = kwargs.get("atmosphere_density")
            density_tags = {
                "light_haze": ["light_haze", "subtle_atmosphere"],
                "atmospheric": ["atmospheric", "mood_lighting"],
                "moody": ["moody_atmosphere", "heavy_mood"],
                "heavy": ["heavy_atmosphere", "dense_mood"]
            }
            tags.extend(density_tags.get(density, []))
        
        # Creative effects
        if kwargs.get("practical_lights", False):
            tags.extend(["practical_lights", "ambient_sources", "environmental_lighting"])
        
        lens_flare = kwargs.get("lens_flare", "none")
        if lens_flare != "none":
            tags.extend([f"{lens_flare}_lens_flare", "optical_effects"])
        
        if kwargs.get("light_rays", False):
            tags.extend(["light_rays", "volumetric_rays", "atmospheric_rays"])
        
        if kwargs.get("volumetric_lighting", False):
            tags.extend(["volumetric_lighting", "light_beams", "atmospheric_lighting"])
        
        # Shadow and highlight control
        shadow_control = kwargs.get("shadow_control", "auto")
        if shadow_control != "auto":
            shadow_tags = {
                "blocked": ["blocked_shadows", "deep_blacks"],
                "detailed": ["detailed_shadows", "shadow_information"],
                "lifted": ["lifted_shadows", "open_shadows"],
                "artistic": ["artistic_shadows", "creative_shadows"]
            }
            tags.extend(shadow_tags.get(shadow_control, []))
        
        highlight_control = kwargs.get("highlight_control", "auto")
        if highlight_control != "auto":
            highlight_tags = {
                "protected": ["protected_highlights", "detail_retention"],
                "normal": ["natural_highlights", "balanced_exposure"],
                "blown": ["blown_highlights", "high_key"],
                "artistic": ["artistic_highlights", "creative_exposure"]
            }
            tags.extend(highlight_tags.get(highlight_control, []))
        
        # Contrast control
        contrast = kwargs.get("lighting_contrast", "moderate")
        contrast_tags = {
            "low": ["low_contrast", "flat_lighting", "even_tones"],
            "moderate": ["moderate_contrast", "balanced_tones"],
            "high": ["high_contrast", "dramatic_tones"],
            "extreme": ["extreme_contrast", "artistic_contrast"]
        }
        tags.extend(contrast_tags[contrast])
        
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
    
    def design_lighting(self, base_prompt, lighting_approach, lighting_quality, **kwargs):
        """Main function to design lighting for the prompt"""
        
        # Analyze existing prompt for lighting context
        context = self.analyze_prompt_for_lighting(base_prompt) if kwargs.get("context_awareness", True) else {}
        
        # Select appropriate lighting configuration
        lighting_config = self.select_lighting_based_on_approach(lighting_approach, context, **kwargs)
        
        # Generate lighting tags
        lighting_tags = self.generate_lighting_tags(lighting_config, lighting_quality, **kwargs)
        
        # Apply emphasis
        emphasis_level = kwargs.get("lighting_emphasis", "medium")
        emphasized_tags = [self.apply_emphasis(tag, emphasis_level) for tag in lighting_tags]
        
        # Create enhanced prompt
        enhanced_prompt = f"{base_prompt}, {', '.join(emphasized_tags)}"
        
        # Create summary
        summary_parts = [
            f"💡 Lighting Design Applied:",
            f"• Approach: {lighting_approach}",
            f"• Configuration: {lighting_config.get('description', 'Custom setup')}",
            f"• Quality: {lighting_quality}",
        ]
        
        if context.get("lighting_types"):
            summary_parts.append(f"• Detected Lighting: {', '.join(context['lighting_types'])}")
        
        if context.get("time_context") != "unknown":
            summary_parts.append(f"• Time Context: {context['time_context']}")
        
        if context.get("environment") != "unknown":
            summary_parts.append(f"• Environment: {context['environment']}")
        
        # Add technical settings
        technical_settings = []
        for key in ["lighting_ratio", "color_temperature", "lighting_contrast"]:
            value = kwargs.get(key, "auto")
            if value != "auto":
                technical_settings.append(f"{key.replace('_', ' ').title()}: {value}")
        
        if technical_settings:
            summary_parts.append(f"• Technical: {', '.join(technical_settings)}")
        
        # Add creative effects
        effects = []
        if kwargs.get("practical_lights", False):
            effects.append("Practical Lights")
        if kwargs.get("lens_flare", "none") != "none":
            effects.append(f"Lens Flare ({kwargs.get('lens_flare')})")
        if kwargs.get("light_rays", False):
            effects.append("Light Rays")
        if kwargs.get("volumetric_lighting", False):
            effects.append("Volumetric")
        
        if effects:
            summary_parts.append(f"• Effects: {', '.join(effects)}")
        
        if emphasis_level != "medium":
            summary_parts.append(f"• Emphasis: {emphasis_level}")
        
        summary_parts.append(f"• Lighting Tags Added: {len(lighting_tags)}")
        
        lighting_summary = "\n".join(summary_parts)
        
        return (enhanced_prompt, lighting_summary)
