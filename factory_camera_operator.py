#!/usr/bin/env python3

"""
Factory Camera Operator - Professional Camera Controls for AI Image Generation
Provides camera settings, lens choices, and photography techniques.

SFW Edition - GitHub Compliant - Professional Grade
"""

import random
import re

class FactoryCameraOperator:
    """
    Professional camera operator node that adds photography controls
    to any prompt. Includes lens simulation, shot types, camera angles, and technical settings.
    """
    
    def __init__(self):
        # Comprehensive professional camera settings database covering all photography scenarios
        self.camera_settings = {
            # Comprehensive shot types covering all photography genres
            "shot_types": {
                "auto": ["medium_shot", "close_up", "wide_shot"],
                
                # Close-up Categories
                "extreme_close_up": ["extreme_close_up", "macro_shot", "detail_shot", "texture_focus", "eye_level_detail"],
                "close_up": ["close_up", "head_shot", "face_focus", "portrait_tight", "intimate_framing"],
                "medium_close_up": ["medium_close_up", "chest_up", "upper_body", "conversational_distance"],
                
                # Medium Shot Categories  
                "medium_shot": ["medium_shot", "half_body", "waist_up", "three_quarter_shot"],
                "medium_wide": ["medium_wide_shot", "knee_up", "social_distance", "environmental_context"],
                
                # Wide Shot Categories
                "wide_shot": ["wide_shot", "full_body", "establishing_shot", "scene_setting"],
                "extreme_wide": ["extreme_wide_shot", "landscape_view", "aerial_perspective", "environmental_overview"],
                "master_shot": ["master_shot", "scene_master", "wide_establishing", "context_setting"],
                
                # Specialized Shots
                "bird_eye_view": ["bird_eye_view", "top_down", "overhead_shot", "aerial_perspective"],
                "worm_eye_view": ["worm_eye_view", "ground_level", "low_angle_extreme", "upward_perspective"],
                "profile_shot": ["profile_shot", "side_view", "silhouette_potential", "edge_lighting"],
                "three_quarter_view": ["three_quarter_view", "angled_portrait", "dimensional_face", "classic_pose"],
                "back_view": ["back_view", "rear_perspective", "environmental_focus", "anonymity"],
                "over_shoulder": ["over_shoulder_shot", "POV_suggestion", "depth_layering", "conversation_angle"],
                
                # Dynamic Shots
                "action_shot": ["action_shot", "motion_capture", "dynamic_pose", "energy_freeze"],
                "candid_shot": ["candid_shot", "natural_moment", "unposed", "authentic_expression"],
                "reaction_shot": ["reaction_shot", "emotional_response", "facial_expression", "moment_capture"],
                
                # Creative Compositions
                "dutch_angle": ["dutch_angle", "tilted_frame", "dynamic_tension", "unbalanced_composition"],
                "symmetrical": ["symmetrical_composition", "balanced_frame", "centered_subject", "formal_balance"],
                "rule_of_thirds": ["rule_of_thirds", "off_center_subject", "natural_composition", "visual_balance"],
                "leading_lines": ["leading_lines", "compositional_guide", "eye_flow", "directional_emphasis"],
                "frame_within_frame": ["frame_within_frame", "natural_border", "depth_illusion", "focus_direction"],
                
                # Genre-Specific Shots
                "fashion_shot": ["fashion_shot", "style_focus", "clothing_emphasis", "editorial_style"],
                "beauty_shot": ["beauty_shot", "flawless_skin", "makeup_focus", "glamour_lighting"],
                "lifestyle_shot": ["lifestyle_shot", "natural_living", "authentic_moment", "relatable_scene"],
                "editorial_shot": ["editorial_shot", "storytelling", "concept_driven", "artistic_vision"],
                "commercial_shot": ["commercial_shot", "product_integration", "brand_focused", "marketing_ready"],
                "documentary_shot": ["documentary_shot", "real_life", "unscripted", "authentic_capture"],
                "street_photography": ["street_photography", "urban_life", "candid_public", "city_energy"],
                "environmental_portrait": ["environmental_portrait", "context_setting", "location_story", "personal_space"],
                "headshot": ["professional_headshot", "business_portrait", "clean_background", "confident_expression"],
                
                # Technical Shots
                "focus_stacking": ["focus_stacking", "everything_sharp", "extended_dof", "technical_precision"],
                "long_exposure": ["long_exposure", "motion_blur", "time_passage", "smooth_water"],
                "high_speed": ["high_speed_capture", "frozen_motion", "split_second", "action_freeze"],
                "multiple_exposure": ["multiple_exposure", "layered_image", "creative_blend", "artistic_overlap"],
                "panoramic": ["panoramic_shot", "wide_vista", "sweeping_view", "horizontal_expansion"],
                "tilt_shift": ["tilt_shift", "selective_focus", "miniature_effect", "plane_focus"],
                
                # Lighting-Based Shots
                "golden_hour": ["golden_hour_shot", "warm_light", "magic_hour", "sunset_glow"],
                "blue_hour": ["blue_hour_shot", "twilight_mood", "evening_balance", "city_lights"],
                "rim_lighting": ["rim_lighting", "edge_highlight", "subject_separation", "dramatic_outline"],
                "backlighting": ["backlighting", "silhouette_potential", "halo_effect", "atmospheric_mood"],
                "side_lighting": ["side_lighting", "dramatic_shadows", "texture_emphasis", "dimensional_form"],
                "front_lighting": ["front_lighting", "even_illumination", "detail_clarity", "shadow_minimal"],
                
                # Mood-Based Shots  
                "dramatic_shot": ["dramatic_shot", "high_contrast", "emotional_intensity", "powerful_presence"],
                "romantic_shot": ["romantic_shot", "soft_mood", "intimate_feeling", "tender_moment"],
                "mysterious_shot": ["mysterious_shot", "shadow_play", "hidden_elements", "intrigue_building"],
                "energetic_shot": ["energetic_shot", "dynamic_composition", "movement_suggestion", "vibrant_life"],
                "peaceful_shot": ["peaceful_shot", "calm_composition", "serene_mood", "tranquil_scene"],
                "powerful_shot": ["powerful_shot", "strong_presence", "commanding_view", "authoritative_stance"],
                "playful_shot": ["playful_shot", "fun_composition", "lighthearted_mood", "joyful_energy"],
                "professional_shot": ["professional_shot", "business_ready", "polished_look", "corporate_style"]
            },
            
            # Comprehensive lens database covering all focal lengths and specialty lenses
            "lens_types": {
                "auto": ["50mm", "35mm", "85mm"],
                
                # Ultra-Wide Angle Lenses (8-24mm)
                "ultra_wide": ["8mm_fisheye", "14mm_ultra_wide", "16mm_ultra_wide", "20mm_ultra_wide"],
                "fisheye": ["8mm_fisheye", "circular_fisheye", "180_degree_view", "extreme_distortion"],
                "architectural": ["14mm_architectural", "16mm_tilt_shift", "perspective_control", "building_photography"],
                
                # Wide Angle Lenses (24-35mm)
                "wide_angle": ["24mm_wide", "28mm_wide", "35mm_wide"],
                "landscape": ["24mm_landscape", "28mm_environmental", "wide_vista", "expansive_view"],
                "environmental": ["35mm_environmental", "context_inclusion", "scene_setting", "storytelling_wide"],
                
                # Standard Lenses (40-60mm)
                "standard": ["50mm_standard", "55mm_normal", "human_vision", "natural_perspective"],
                "documentary": ["50mm_documentary", "natural_view", "street_photography", "honest_perspective"],
                "photojournalism": ["35mm_photojournalism", "50mm_reportage", "real_world_view"],
                
                # Short Telephoto/Portrait Lenses (70-135mm)
                "portrait": ["85mm_portrait", "105mm_portrait", "135mm_portrait"],
                "beauty": ["85mm_beauty", "flattering_compression", "smooth_bokeh", "subject_isolation"],
                "fashion": ["105mm_fashion", "135mm_editorial", "compressed_perspective", "background_separation"],
                
                # Medium Telephoto (135-300mm)
                "telephoto": ["200mm_telephoto", "300mm_long", "subject_compression", "background_blur"],
                "sports": ["300mm_sports", "action_capture", "distant_subjects", "fast_autofocus"],
                "wildlife": ["400mm_wildlife", "600mm_super_tele", "nature_photography", "animal_capture"],
                
                # Super Telephoto (300mm+)
                "super_telephoto": ["400mm_super", "600mm_extreme", "800mm_professional"],
                "astronomy": ["800mm_astronomy", "moon_photography", "celestial_capture", "extreme_zoom"],
                
                # Macro Lenses
                "macro": ["60mm_macro", "100mm_macro", "180mm_macro"],
                "close_focus": ["1:1_magnification", "life_size_reproduction", "extreme_detail"],
                "focus_stacking": ["macro_stacking", "extended_dof", "detail_perfection"],
                
                # Specialty Lenses
                "tilt_shift": ["24mm_tilt_shift", "85mm_tilt_shift", "perspective_control", "selective_focus"],
                "anamorphic": ["anamorphic_lens", "cinematic_bokeh", "oval_highlights", "2.35:1_aspect"],
                "lensbaby": ["creative_focus", "selective_blur", "artistic_distortion", "dreamy_effect"],
                "infrared": ["infrared_lens", "IR_photography", "false_color", "artistic_spectrum"],
                
                # Vintage/Character Lenses
                "vintage": ["vintage_character", "classic_rendering", "film_aesthetic", "nostalgic_feel"],
                "helios": ["helios_swirl", "swirly_bokeh", "vintage_soviet", "character_lens"],
                "petzval": ["petzval_lens", "swirly_bokeh", "vintage_portrait", "artistic_blur"],
                
                # Zoom Lenses
                "standard_zoom": ["24-70mm", "versatile_range", "all_purpose", "event_photography"],
                "telephoto_zoom": ["70-200mm", "portrait_zoom", "sports_range", "flexible_framing"],
                "super_zoom": ["18-300mm", "travel_lens", "convenience_zoom", "one_lens_solution"],
                
                # Cinema Lenses
                "cinema": ["cinema_lens", "film_quality", "cinematic_look", "video_optimized"],
                "anamorphic_cinema": ["anamorphic_cinema", "2.39:1_aspect", "lens_flares", "cinematic_bokeh"]
            },
            
            # Comprehensive aperture settings for all scenarios
            "aperture_settings": {
                "auto": ["f2.8", "f4", "f5.6"],
                
                # Ultra-Wide Apertures (f/1.0 - f/1.8)
                "ultra_wide_aperture": ["f1.0", "f1.2", "f1.4", "f1.8"],
                "extreme_bokeh": ["f1.0_dream", "f1.2_butter", "f1.4_creamy", "ultra_shallow_dof"],
                "low_light_extreme": ["f1.0_night", "f1.2_available_light", "extreme_light_gathering"],
                
                # Wide Apertures (f/2.0 - f/2.8)  
                "wide_aperture": ["f2.0", "f2.8"],
                "portrait_bokeh": ["f2.0_portrait", "f2.8_subject_isolation", "smooth_background"],
                "low_light": ["f2.0_evening", "f2.8_indoor", "available_light"],
                
                # Moderate Apertures (f/4.0 - f/5.6)
                "moderate_aperture": ["f4.0", "f5.6"],
                "balanced_depth": ["f4_balanced", "f5.6_general", "moderate_dof"],
                "group_portraits": ["f4_group", "f5.6_multiple_subjects", "sufficient_depth"],
                
                # Narrow Apertures (f/8.0 - f/11)
                "narrow_aperture": ["f8.0", "f11"],
                "landscape_sharp": ["f8_landscape", "f11_everything_sharp", "maximum_sharpness"],
                "street_photography": ["f8_street", "zone_focusing", "extended_dof"],
                
                # Very Narrow Apertures (f/16 - f/32)
                "very_narrow": ["f16", "f22", "f32"],
                "architecture": ["f16_architecture", "f22_technical", "edge_to_edge_sharp"],
                "product_photography": ["f11_product", "f16_commercial", "everything_in_focus"],
                
                # Specialized Settings
                "hyperfocal": ["hyperfocal_focus", "infinity_focus", "landscape_optimal"],
                "focus_stacking": ["focus_stack_setup", "f8_stacking", "maximum_detail"],
                "sun_star": ["f16_sun_star", "f22_starburst", "diffraction_spikes"],
                
                # Creative Aperture Effects
                "bokeh_balls": ["f1.4_bokeh_balls", "f2_circular_highlights", "smooth_highlights"],
                "swirly_bokeh": ["swirly_background", "artistic_blur", "vintage_character"],
                "soap_bubble": ["soap_bubble_bokeh", "f1.4_dreamy", "ethereal_background"],
                
                # Technical Precision
                "diffraction_limited": ["f8_diffraction_limit", "optical_sweet_spot", "maximum_resolution"],
                "depth_of_field_preview": ["dof_preview", "aperture_stopped_down", "final_result_preview"]
            },
            
            # Comprehensive camera angles covering all perspectives and photography scenarios
            "camera_angles": {
                "auto": ["eye_level", "slightly_low", "slightly_high"],
                
                # Standard Eye Level Angles
                "eye_level": ["eye_level", "natural_perspective", "straight_on", "neutral_viewpoint"],
                "human_perspective": ["human_eye_height", "natural_viewing", "comfortable_angle", "relatable_view"],
                "conversational": ["conversational_level", "social_distance", "interpersonal_angle"],
                
                # Low Angle Variations (Camera Below Subject)
                "low_angle": ["low_angle", "upward_perspective", "heroic_angle", "powerful_view"],
                "worm_eye_view": ["worm_eye_view", "ground_level", "extreme_low", "dramatic_upward"],
                "heroic_low": ["heroic_low_angle", "empowering_view", "dominant_subject", "larger_than_life"],
                "slight_low": ["slightly_low", "subtle_upward", "gentle_heroic", "confidence_boost"],
                "dramatic_low": ["dramatic_low_angle", "extreme_upward", "intimidating_view", "tower_perspective"],
                "architectural_low": ["architectural_low", "building_perspective", "structural_dominance"],
                
                # High Angle Variations (Camera Above Subject)  
                "high_angle": ["high_angle", "downward_perspective", "diminishing_view", "overhead_look"],
                "bird_eye_view": ["bird_eye_view", "aerial_perspective", "top_down", "god_view"],
                "overhead": ["overhead_shot", "directly_above", "flat_lay_angle", "table_top_view"],
                "slight_high": ["slightly_high", "subtle_downward", "gentle_dominance", "protective_view"],
                "dramatic_high": ["dramatic_high_angle", "extreme_downward", "vulnerability_emphasis"],
                "security_camera": ["security_camera_angle", "surveillance_view", "corner_mounted"],
                "drone_perspective": ["drone_angle", "aerial_photography", "elevated_view", "landscape_overview"],
                
                # Tilted/Dutch Angles
                "dutch_angle": ["dutch_angle", "tilted_horizon", "dynamic_tension", "unbalanced_frame"],
                "slight_tilt": ["slight_dutch", "subtle_tilt", "mild_tension", "gentle_dynamic"],
                "extreme_tilt": ["extreme_dutch", "severe_tilt", "disorienting_angle", "chaos_suggestion"],
                "clockwise_tilt": ["clockwise_dutch", "right_lean", "falling_right"],
                "counterclockwise_tilt": ["counterclockwise_dutch", "left_lean", "falling_left"],
                
                # Profile and Side Angles
                "profile": ["profile_view", "side_angle", "90_degree_turn", "silhouette_potential"],
                "three_quarter": ["three_quarter_view", "45_degree_angle", "dimensional_face", "classic_portrait"],
                "seven_eighths": ["seven_eighths_view", "near_profile", "slight_turn", "elegant_angle"],
                "back_three_quarter": ["back_three_quarter", "rear_diagonal", "shoulder_emphasis"],
                
                # Specific Directional Angles
                "front_facing": ["front_facing", "direct_confrontation", "head_on", "full_frontal"],
                "back_view": ["back_view", "rear_perspective", "away_facing", "departure_angle"],
                "left_profile": ["left_profile", "left_side_view", "sinister_profile"],
                "right_profile": ["right_profile", "right_side_view", "dexter_profile"],
                
                # Camera Movement Suggestions
                "tracking_angle": ["tracking_shot", "following_movement", "parallel_motion"],
                "dolly_in": ["dolly_in_angle", "approaching_subject", "zoom_in_perspective"],
                "dolly_out": ["dolly_out_angle", "revealing_context", "pull_back_view"],
                "crane_up": ["crane_up_angle", "rising_perspective", "elevating_view"],
                "crane_down": ["crane_down_angle", "descending_view", "lowering_perspective"],
                
                # Specialized Photography Angles
                "macro_angle": ["macro_perspective", "extreme_close_angle", "detail_focus"],
                "wide_angle_distortion": ["wide_angle_perspective", "barrel_distortion", "expanded_view"],
                "telephoto_compression": ["telephoto_angle", "compressed_perspective", "flattened_depth"],
                "fisheye_curve": ["fisheye_perspective", "curved_horizon", "spherical_distortion"],
                
                # Portrait-Specific Angles
                "beauty_angle": ["beauty_angle", "flattering_high", "feminine_perspective", "glamour_angle"],
                "masculine_angle": ["masculine_angle", "strong_low", "powerful_perspective", "authoritative_view"],
                "child_angle": ["child_level", "low_adult_perspective", "kid_friendly_angle"],
                "group_angle": ["group_perspective", "multiple_subject_angle", "inclusive_view"],
                
                # Fashion and Editorial Angles
                "fashion_high": ["fashion_high_angle", "editorial_perspective", "model_dominance"],
                "runway_angle": ["runway_perspective", "catwalk_view", "fashion_show_angle"],
                "editorial_dramatic": ["editorial_angle", "magazine_perspective", "story_telling_view"],
                "avant_garde": ["avant_garde_angle", "experimental_perspective", "artistic_view"],
                
                # Architectural Photography Angles
                "architectural_straight": ["architectural_angle", "vertical_correction", "building_perspective"],
                "keystone_correction": ["corrected_perspective", "parallel_lines", "architectural_precision"],
                "leading_lines": ["leading_lines_angle", "perspective_convergence", "depth_guidance"],
                "symmetrical_view": ["symmetrical_angle", "centered_perspective", "balanced_composition"],
                
                # Action and Sports Angles
                "action_low": ["action_low_angle", "dynamic_sports", "energy_perspective"],
                "sports_sideline": ["sideline_angle", "sports_perspective", "field_level_view"],
                "freeze_motion": ["freeze_action_angle", "stopped_time", "peak_action"],
                "motion_blur": ["motion_blur_angle", "speed_suggestion", "movement_emphasis"],
                
                # Cinematic Angles
                "cinematic_wide": ["cinematic_angle", "film_perspective", "movie_view"],
                "establishing_shot": ["establishing_angle", "scene_setting", "context_providing"],
                "close_up_dramatic": ["dramatic_close_angle", "intense_perspective", "emotional_focus"],
                "medium_conversational": ["conversational_angle", "dialogue_perspective", "social_distance"],
                
                # Environmental Angles
                "landscape_level": ["landscape_angle", "horizon_level", "natural_perspective"],
                "forest_looking_up": ["forest_canopy_angle", "tree_perspective", "upward_nature"],
                "mountain_perspective": ["mountain_angle", "peak_view", "alpine_perspective"],
                "urban_canyon": ["urban_angle", "city_perspective", "building_canyon"],
                
                # Artistic and Creative Angles
                "abstract_angle": ["abstract_perspective", "unconventional_view", "artistic_interpretation"],
                "geometric_angle": ["geometric_perspective", "pattern_emphasis", "structural_view"],
                "reflection_angle": ["reflection_perspective", "mirror_view", "doubled_image"],
                "shadow_play": ["shadow_angle", "light_play_perspective", "chiaroscuro_view"],
                
                # Technical Photography Angles
                "focus_stacking": ["focus_stack_angle", "extended_dof_perspective", "technical_precision"],
                "product_angle": ["product_perspective", "commercial_view", "marketing_angle"],
                "scientific_angle": ["scientific_perspective", "documentation_view", "technical_angle"],
                "forensic_angle": ["forensic_perspective", "evidence_view", "detailed_documentation"],
                
                # Psychological Angles
                "intimidating_low": ["intimidating_angle", "threatening_perspective", "fear_inducing"],
                "vulnerable_high": ["vulnerable_angle", "weakness_perspective", "helpless_view"],
                "empowering_level": ["empowering_angle", "confidence_perspective", "strength_view"],
                "intimate_close": ["intimate_angle", "personal_perspective", "emotional_closeness"],
                
                # Cultural and Traditional Angles
                "japanese_low": ["japanese_angle", "respectful_low", "cultural_perspective"],
                "western_eye_level": ["western_angle", "direct_confrontation", "equality_perspective"],
                "formal_portrait": ["formal_angle", "traditional_portrait", "classical_perspective"],
                "casual_candid": ["candid_angle", "natural_perspective", "unposed_view"]
            },
            
            # Comprehensive lighting styles covering all photography scenarios and moods
            "lighting_styles": {
                "auto": ["natural_light", "soft_light", "diffused"],
                
                # Natural Lighting
                "natural": ["natural_light", "available_light", "window_light", "outdoor_ambient"],
                "sunlight": ["direct_sunlight", "bright_daylight", "harsh_sun", "solar_illumination"],
                "overcast": ["overcast_sky", "cloudy_diffusion", "even_natural_light", "soft_daylight"],
                "shade": ["open_shade", "indirect_sunlight", "cool_shadows", "even_shade"],
                "indoor_natural": ["window_lighting", "interior_daylight", "ambient_indoor"],
                
                # Golden Hour and Magic Hour
                "golden_hour": ["golden_hour", "warm_sunset", "magic_hour", "honeyed_light"],
                "sunrise": ["sunrise_light", "dawn_glow", "morning_warmth", "early_light"],
                "sunset": ["sunset_light", "evening_glow", "dusk_warmth", "twilight_gold"],
                "magic_hour_warm": ["warm_magic_hour", "golden_glow", "amber_light"],
                
                # Blue Hour and Twilight
                "blue_hour": ["blue_hour", "twilight_blue", "evening_balance", "dusk_cool"],
                "civil_twilight": ["civil_twilight", "balanced_lighting", "mixed_light"],
                "nautical_twilight": ["nautical_twilight", "deep_blue", "city_lights_emerging"],
                "astronomical_twilight": ["astronomical_twilight", "star_emergence", "deep_dusk"],
                
                # Studio Lighting Setups
                "studio": ["studio_lighting", "controlled_environment", "professional_setup", "artificial_light"],
                "key_light": ["main_light", "primary_illumination", "subject_lighting", "key_illumination"],
                "fill_light": ["fill_lighting", "shadow_reduction", "secondary_light", "balance_illumination"],
                "background_light": ["background_separation", "backdrop_lighting", "depth_creation"],
                "rim_light": ["rim_lighting", "edge_light", "hair_light", "separation_light"],
                "hair_light": ["hair_lighting", "top_light", "halo_effect", "crown_illumination"],
                
                # Portrait Lighting Patterns
                "rembrandt": ["rembrandt_lighting", "triangle_shadow", "dramatic_portrait", "classical_light"],
                "butterfly": ["butterfly_lighting", "paramount_light", "glamour_lighting", "beauty_light"],
                "loop": ["loop_lighting", "nose_shadow", "natural_portrait", "versatile_light"],
                "split": ["split_lighting", "half_face_shadow", "dramatic_contrast", "moody_portrait"],
                "broad": ["broad_lighting", "face_illumination", "wider_face_effect"],
                "short": ["short_lighting", "shadow_side_emphasis", "slimming_effect", "dramatic_depth"],
                
                # Dramatic Lighting
                "dramatic": ["dramatic_lighting", "high_contrast", "chiaroscuro", "moody_shadows"],
                "low_key": ["low_key_lighting", "dark_background", "minimal_fill", "mystery_mood"],
                "high_key": ["high_key_lighting", "bright_overall", "minimal_shadows", "cheerful_mood"],
                "noir": ["film_noir_lighting", "stark_contrast", "venetian_blind_shadows"],
                "gothic": ["gothic_lighting", "cathedral_light", "dramatic_arches", "stone_shadows"],
                
                # Soft Lighting
                "soft": ["soft_lighting", "diffused_light", "gentle_illumination", "flattering_light"],
                "beauty_light": ["beauty_lighting", "flawless_skin", "soft_shadows", "glamour_glow"],
                "baby_light": ["baby_lighting", "gentle_soft", "tender_illumination", "delicate_glow"],
                "bridal": ["bridal_lighting", "romantic_soft", "dreamy_glow", "wedding_light"],
                "maternity": ["maternity_lighting", "glowing_skin", "soft_curves", "maternal_glow"],
                
                # Hard Lighting  
                "hard": ["hard_lighting", "sharp_shadows", "direct_light", "crisp_definition"],
                "direct_flash": ["direct_flash", "frontal_hard", "snapshot_light", "camera_flash"],
                "bare_bulb": ["bare_bulb", "point_source", "harsh_shadows", "industrial_light"],
                "spotlight": ["spotlight", "theatrical_light", "focused_beam", "stage_illumination"],
                "laser": ["laser_light", "coherent_beam", "sci_fi_illumination", "precision_light"],
                
                # Colored Lighting
                "neon": ["neon_lighting", "electric_colors", "urban_glow", "night_city"],
                "rgb": ["rgb_lighting", "color_changing", "digital_illumination", "tech_colors"],
                "led_panel": ["led_panel_lighting", "even_color", "adjustable_temperature"],
                "gel_filters": ["colored_gels", "theatrical_colors", "mood_lighting"],
                "disco": ["disco_lighting", "multi_color", "party_illumination", "dance_floor"],
                
                # Environmental Lighting
                "fire": ["firelight", "flame_illumination", "warm_flicker", "campfire_glow"],
                "candle": ["candlelight", "intimate_glow", "romantic_flicker", "soft_warmth"],
                "moonlight": ["moonlight", "cool_night", "ethereal_glow", "lunar_illumination"],
                "starlight": ["starlight", "minimal_illumination", "cosmic_glow", "night_sky"],
                "aurora": ["aurora_light", "northern_lights", "cosmic_colors", "sky_dance"],
                
                # Artificial Lighting Sources
                "fluorescent": ["fluorescent_light", "office_lighting", "cool_white", "commercial_illumination"],
                "tungsten": ["tungsten_light", "warm_incandescent", "household_bulb", "3200k_light"],
                "halogen": ["halogen_light", "bright_white", "hot_light", "intense_illumination"],
                "hmi": ["hmi_light", "daylight_balanced", "film_lighting", "professional_source"],
                "led": ["led_lighting", "energy_efficient", "adjustable_temperature", "modern_source"],
                
                # Specialty Lighting Effects
                "backlighting": ["backlighting", "silhouette_potential", "rim_glow", "separation_effect"],
                "side_lighting": ["side_lighting", "texture_emphasis", "dimensional_form", "sculptural_light"],
                "top_lighting": ["top_lighting", "overhead_illumination", "downward_shadows"],
                "bottom_lighting": ["bottom_lighting", "upward_illumination", "horror_effect", "dramatic_uplighting"],
                "cross_lighting": ["cross_lighting", "multiple_angles", "complex_shadows", "dimensional_depth"],
                
                # Weather-Based Lighting
                "storm": ["storm_lighting", "dramatic_clouds", "lightning_illumination", "tempest_mood"],
                "fog": ["fog_lighting", "diffused_atmosphere", "mysterious_glow", "ethereal_mood"],
                "rain": ["rain_lighting", "wet_reflections", "storm_atmosphere", "dramatic_weather"],
                "snow": ["snow_lighting", "winter_brightness", "reflected_light", "crystalline_glow"],
                "mist": ["misty_lighting", "soft_diffusion", "dreamy_atmosphere", "gentle_haze"],
                
                # Time-Based Lighting
                "dawn": ["dawn_light", "early_morning", "soft_awakening", "gentle_beginning"],
                "morning": ["morning_light", "fresh_illumination", "clear_bright", "energetic_start"],
                "noon": ["noon_light", "overhead_sun", "harsh_shadows", "intense_brightness"],
                "afternoon": ["afternoon_light", "warm_slant", "golden_approach", "mellow_warmth"],
                "evening": ["evening_light", "descending_sun", "warm_glow", "day_ending"],
                "night": ["night_lighting", "artificial_sources", "city_glow", "darkness_punctuated"],
                "midnight": ["midnight_lighting", "deep_night", "minimal_sources", "mystery_hour"],
                
                # Architectural Lighting
                "cathedral": ["cathedral_lighting", "stained_glass", "divine_illumination", "sacred_glow"],
                "museum": ["museum_lighting", "artwork_illumination", "display_lighting", "cultural_glow"],
                "gallery": ["gallery_lighting", "white_walls", "neutral_illumination", "art_focused"],
                "theater": ["theater_lighting", "stage_illumination", "dramatic_spots", "performance_light"],
                "concert": ["concert_lighting", "stage_effects", "colored_beams", "musical_atmosphere"],
                
                # Commercial Lighting
                "retail": ["retail_lighting", "product_illumination", "shopping_brightness", "commercial_appeal"],
                "restaurant": ["restaurant_lighting", "dining_ambiance", "warm_atmosphere", "social_glow"],
                "office": ["office_lighting", "work_illumination", "productivity_light", "business_bright"],
                "hospital": ["hospital_lighting", "clinical_bright", "sterile_illumination", "medical_clarity"],
                "school": ["classroom_lighting", "learning_environment", "educational_bright"],
                
                # Creative and Artistic Lighting
                "experimental": ["experimental_lighting", "artistic_exploration", "creative_illumination"],
                "abstract": ["abstract_lighting", "non_representational", "pattern_light", "geometric_illumination"],
                "surreal": ["surreal_lighting", "dreamlike_illumination", "impossible_light", "fantasy_glow"],
                "minimalist": ["minimalist_lighting", "simple_illumination", "clean_light", "essential_glow"],
                "maximum": ["maximum_lighting", "intense_illumination", "overwhelming_bright", "extreme_light"]
            },
            
            "composition_rules": {
                "auto": ["rule_of_thirds", "centered", "dynamic"],
                "rule_of_thirds": ["rule_of_thirds", "off_center", "balanced_thirds"],
                "centered": ["centered_composition", "symmetrical", "bull_eye"],
                "dynamic": ["dynamic_composition", "diagonal_lines", "movement"],
                "leading_lines": ["leading_lines", "perspective_lines", "depth_guide"],
                "frame_within_frame": ["natural_frame", "architectural_frame", "creative_border"],
                "symmetrical": ["perfect_symmetry", "mirror_composition", "balanced"],
                "asymmetrical": ["asymmetrical_balance", "visual_weight", "tension"],
                "golden_ratio": ["golden_ratio", "phi_composition", "divine_proportion"],
                "diagonal_lines": ["diagonal_composition", "dynamic_angles", "perspective_depth"],
                "patterns": ["pattern_composition", "repetition", "rhythmic_elements"],
                "negative_space": ["negative_space", "minimalist", "breathing_room"],
                "depth_layers": ["layered_depth", "foreground_middle_background", "dimensional"],
                "foreground_focus": ["foreground_emphasis", "depth_separation", "layered_focus"],
                "background_blur": ["background_bokeh", "subject_isolation", "depth_blur"],
                "environmental_context": ["environmental_setting", "contextual_placement", "scene_integration"]
            },
            
            "focus_techniques": {
                "auto": ["sharp_focus", "selective_focus"],
                "sharp_focus": ["crystal_clear", "pin_sharp", "detailed", "crisp"],
                "selective_focus": ["selective_focus", "subject_isolation", "background_blur"],
                "focus_stacking": ["focus_stacking", "extended_dof", "macro_sharp"],
                "rack_focus": ["rack_focus", "focus_pull", "depth_transition"],
                "soft_focus": ["soft_focus", "dreamy", "ethereal", "romantic_blur"],
                "bokeh_emphasis": ["bokeh_background", "creamy_bokeh", "artistic_blur"],
                "zone_focusing": ["zone_focus", "street_photography", "depth_coverage"],
                "hyperfocal_focus": ["hyperfocal_distance", "maximum_depth", "landscape_focus"],
                "macro_focus": ["macro_detail", "close_up_sharp", "magnified_detail"],
                "infinity_focus": ["infinity_sharp", "distant_focus", "landscape_depth"]
            },
            
            "camera_movements": {
                "auto": ["static_shot", "slight_movement"],
                "static": ["static_shot", "tripod_stable", "locked_down"],
                "pan": ["panning_shot", "horizontal_movement", "following_action"],
                "tilt": ["tilting_shot", "vertical_movement", "reveal_shot"],
                "dolly": ["dolly_shot", "smooth_movement", "cinematic_push"],
                "handheld": ["handheld", "organic_movement", "documentary_style"],
                "crane": ["crane_shot", "sweeping_movement", "elevated_perspective"]
            }
        }
        
        # Professional quality enhancers
        self.quality_enhancers = {
            "professional": ["professional_photography", "high_end", "commercial_quality"],
            "cinematic": ["cinematic", "film_quality", "movie_grade"],
            "artistic": ["artistic_photography", "fine_art", "gallery_worthy"],
            "documentary": ["documentary_style", "photojournalism", "authentic"],
            "fashion": ["fashion_photography", "editorial", "magazine_quality"],
            "portrait": ["portrait_photography", "character_study", "intimate"],
            "landscape": ["landscape_photography", "nature", "environmental"]
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_prompt": ("STRING", {"forceInput": True}),
                "photography_style": (["auto", "professional", "cinematic", "artistic", "documentary", "fashion", "portrait", "landscape", "street", "wildlife", "macro", "architectural", "sports", "event", "commercial", "editorial"], {"default": "professional"}),
                "shot_type": (["auto", "extreme_close_up", "close_up", "medium_close_up", "medium_shot", "medium_wide", "wide_shot", "extreme_wide", "master_shot", "action_shot", "candid_shot", "fashion_shot", "beauty_shot", "lifestyle_shot", "editorial_shot", "commercial_shot", "documentary_shot", "environmental_portrait", "headshot"], {"default": "auto"}),
                "camera_quality": (["standard", "professional", "high_end", "cinematic", "broadcast", "IMAX", "large_format"], {"default": "professional"}),
            },
            "optional": {
                # Lens and Technical - Comprehensive Coverage
                "lens_type": (["auto", "ultra_wide", "fisheye", "architectural", "wide_angle", "landscape", "environmental", "standard", "documentary", "photojournalism", "portrait", "beauty", "fashion", "telephoto", "sports", "wildlife", "super_telephoto", "astronomy", "macro", "tilt_shift", "anamorphic", "lensbaby", "vintage", "helios", "petzval", "standard_zoom", "telephoto_zoom", "super_zoom", "cinema", "anamorphic_cinema"], {"default": "auto"}),
                "aperture": (["auto", "ultra_wide_aperture", "extreme_bokeh", "low_light_extreme", "wide_aperture", "portrait_bokeh", "low_light", "moderate_aperture", "balanced_depth", "group_portraits", "narrow_aperture", "landscape_sharp", "street_photography", "very_narrow", "architecture", "product_photography", "hyperfocal", "focus_stacking", "sun_star", "bokeh_balls", "swirly_bokeh", "soap_bubble", "diffraction_limited"], {"default": "auto"}),
                "focus_technique": (["auto", "sharp_focus", "selective_focus", "focus_stacking", "rack_focus", "soft_focus", "bokeh_emphasis", "zone_focusing", "hyperfocal_focus", "macro_focus", "infinity_focus"], {"default": "auto"}),
                
                # Composition and Angles - Massive Expansion
                "camera_angle": (["auto", "eye_level", "human_perspective", "conversational", "low_angle", "worm_eye_view", "heroic_low", "slight_low", "dramatic_low", "architectural_low", "high_angle", "bird_eye_view", "overhead", "slight_high", "dramatic_high", "security_camera", "drone_perspective", "dutch_angle", "slight_tilt", "extreme_tilt", "clockwise_tilt", "counterclockwise_tilt", "profile", "three_quarter", "seven_eighths", "back_three_quarter", "front_facing", "back_view", "left_profile", "right_profile", "beauty_angle", "masculine_angle", "child_angle", "group_angle", "fashion_high", "runway_angle", "editorial_dramatic", "avant_garde", "architectural_straight", "keystone_correction", "leading_lines", "symmetrical_view", "action_low", "sports_sideline", "freeze_motion", "motion_blur", "cinematic_wide", "establishing_shot", "close_up_dramatic", "medium_conversational", "landscape_level", "forest_looking_up", "mountain_perspective", "urban_canyon", "abstract_angle", "geometric_angle", "reflection_angle", "shadow_play", "intimidating_low", "vulnerable_high", "empowering_level", "intimate_close"], {"default": "auto"}),
                "composition": (["auto", "rule_of_thirds", "centered", "dynamic", "leading_lines", "frame_within_frame", "symmetrical", "asymmetrical", "golden_ratio", "diagonal_lines", "patterns", "negative_space", "depth_layers", "foreground_focus", "background_blur", "environmental_context"], {"default": "auto"}),
                "camera_movement": (["auto", "static", "pan", "tilt", "dolly", "handheld", "crane", "tracking_angle", "dolly_in", "dolly_out", "crane_up", "crane_down"], {"default": "auto"}),
                
                # Lighting - Comprehensive Coverage
                "lighting_style": (["auto", "natural", "sunlight", "overcast", "shade", "indoor_natural", "golden_hour", "sunrise", "sunset", "magic_hour_warm", "blue_hour", "civil_twilight", "nautical_twilight", "astronomical_twilight", "studio", "key_light", "fill_light", "background_light", "rim_light", "hair_light", "rembrandt", "butterfly", "loop", "split", "broad", "short", "dramatic", "low_key", "high_key", "noir", "gothic", "soft", "beauty_light", "baby_light", "bridal", "maternity", "hard", "direct_flash", "bare_bulb", "spotlight", "laser", "neon", "rgb", "led_panel", "gel_filters", "disco", "fire", "candle", "moonlight", "starlight", "aurora", "fluorescent", "tungsten", "halogen", "hmi", "led", "backlighting", "side_lighting", "top_lighting", "bottom_lighting", "cross_lighting", "storm", "fog", "rain", "snow", "mist", "dawn", "morning", "noon", "afternoon", "evening", "night", "midnight", "cathedral", "museum", "gallery", "theater", "concert", "retail", "restaurant", "office", "hospital", "school"], {"default": "auto"}),
                
                # Technical Settings - Professional Grade
                "iso_setting": (["auto", "low_iso_50", "low_iso_100", "low_iso_200", "medium_iso_400", "medium_iso_800", "high_iso_1600", "high_iso_3200", "ultra_high_iso_6400", "extreme_iso_12800", "push_iso_25600"], {"default": "auto"}),
                "shutter_speed": (["auto", "ultra_fast_freeze", "fast_freeze", "medium_sharp", "slow_motion_blur", "long_exposure", "bulb_mode", "light_trails", "star_trails", "time_lapse"], {"default": "auto"}),
                "white_balance": (["auto", "daylight_5600k", "cloudy_6500k", "shade_7500k", "tungsten_3200k", "fluorescent_4000k", "flash_5500k", "underwater", "custom_kelvin"], {"default": "auto"}),
                
                # Advanced Professional Controls
                "metering_mode": (["auto", "matrix", "center_weighted", "spot", "highlight_weighted"], {"default": "auto"}),
                "color_profile": (["auto", "srgb", "adobe_rgb", "prophoto_rgb", "rec2020", "dci_p3"], {"default": "auto"}),
                "dynamic_range": (["auto", "standard", "hdr_moderate", "hdr_high", "hdr_extreme"], {"default": "auto"}),
                "image_stabilization": (["auto", "optical_is", "in_body_is", "electronic_is", "tripod_mode"], {"default": "auto"}),
                
                # Creative and Artistic Controls
                "artistic_effect": (["none", "vintage_film", "cross_process", "bleach_bypass", "tilt_shift_blur", "orton_effect", "black_white", "sepia_tone", "split_tone", "color_grading"], {"default": "none"}),
                "film_emulation": (["none", "kodak_portra", "fuji_velvia", "ilford_hp5", "tri_x", "ektar", "superia", "provia"], {"default": "none"}),
                "lens_character": (["clean", "vintage_coating", "lens_flare", "chromatic_aberration", "vignetting", "barrel_distortion", "pincushion"], {"default": "clean"}),
                
                # Environment and Context
                "weather_condition": (["auto", "clear_sky", "partly_cloudy", "overcast", "stormy", "foggy", "misty", "rainy", "snowy", "windy"], {"default": "auto"}),
                "time_of_day": (["auto", "pre_dawn", "dawn", "morning", "late_morning", "noon", "afternoon", "late_afternoon", "sunset", "dusk", "night", "late_night"], {"default": "auto"}),
                "season": (["auto", "spring", "summer", "autumn", "winter"], {"default": "auto"}),
                
                # Post-Processing Hints
                "post_processing": (["none", "minimal", "standard", "enhanced", "artistic", "commercial", "editorial"], {"default": "standard"}),
                "color_treatment": (["natural", "warm_tone", "cool_tone", "high_contrast", "low_contrast", "desaturated", "oversaturated", "monochrome"], {"default": "natural"}),
                
                # Enhancement Controls
                "camera_emphasis": (["low", "medium", "high", "very_high", "maximum"], {"default": "medium"}),
                "technical_detail": (["minimal", "standard", "detailed", "technical", "professional", "expert"], {"default": "standard"}),
                "context_awareness": ("BOOLEAN", {"default": True}),
                "genre_optimization": ("BOOLEAN", {"default": True}),
                "professional_metadata": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "camera_summary")
    FUNCTION = "enhance_with_camera"
    CATEGORY = "Camera Factory Station"
    
    def analyze_prompt_context(self, prompt):
        """Analyze the base prompt to understand the scene context"""
        prompt_lower = prompt.lower()
        
        context = {
            "subject_type": "person",  # default
            "scene_type": "portrait",  # default
            "environment": "indoor",   # default
            "mood": "neutral",         # default
            "activity": "static"       # default
        }
        
        # Detect subject type
        if any(word in prompt_lower for word in ["1girl", "1boy", "person", "character", "portrait"]):
            context["subject_type"] = "person"
        elif any(word in prompt_lower for word in ["landscape", "scenery", "nature", "building"]):
            context["subject_type"] = "environment"
        elif any(word in prompt_lower for word in ["product", "object", "item", "still_life"]):
            context["subject_type"] = "object"
        
        # Detect scene type
        if any(word in prompt_lower for word in ["close", "face", "head", "portrait"]):
            context["scene_type"] = "portrait"
        elif any(word in prompt_lower for word in ["full_body", "standing", "sitting", "pose"]):
            context["scene_type"] = "full_figure"
        elif any(word in prompt_lower for word in ["landscape", "wide", "environment", "scenery"]):
            context["scene_type"] = "landscape"
        elif any(word in prompt_lower for word in ["product", "commercial", "advertising"]):
            context["scene_type"] = "product"
        
        # Detect environment
        if any(word in prompt_lower for word in ["outdoor", "outside", "nature", "park", "street"]):
            context["environment"] = "outdoor"
        elif any(word in prompt_lower for word in ["indoor", "inside", "room", "office", "studio"]):
            context["environment"] = "indoor"
        
        # Detect mood
        if any(word in prompt_lower for word in ["dramatic", "dark", "moody", "intense"]):
            context["mood"] = "dramatic"
        elif any(word in prompt_lower for word in ["bright", "happy", "cheerful", "light"]):
            context["mood"] = "bright"
        elif any(word in prompt_lower for word in ["romantic", "soft", "gentle", "intimate"]):
            context["mood"] = "romantic"
        
        # Detect activity
        if any(word in prompt_lower for word in ["running", "jumping", "dancing", "moving", "action"]):
            context["activity"] = "dynamic"
        elif any(word in prompt_lower for word in ["sitting", "standing", "posing", "static"]):
            context["activity"] = "static"
        
        return context
    
    def smart_selection(self, category, user_choice, context):
        """Make intelligent selections based on context when user chooses 'auto'"""
        if user_choice != "auto":
            # Check if the key exists in the category
            if user_choice in self.camera_settings[category]:
                return random.choice(self.camera_settings[category][user_choice])
            else:
                # Fallback to 'auto' if key doesn't exist
                return random.choice(self.camera_settings[category]["auto"])
        
        # Smart defaults based on context
        if category == "shot_types":
            if context["scene_type"] == "portrait":
                return random.choice(self.camera_settings[category]["close_up"])
            elif context["scene_type"] == "landscape":
                return random.choice(self.camera_settings[category]["wide_shot"])
            elif context["scene_type"] == "product":
                return random.choice(self.camera_settings[category]["medium_shot"])
            else:
                return random.choice(self.camera_settings[category]["auto"])
        
        elif category == "lens_types":
            if context["scene_type"] == "portrait":
                return random.choice(self.camera_settings[category]["portrait"])
            elif context["scene_type"] == "landscape":
                return random.choice(self.camera_settings[category]["wide_angle"])
            else:
                return random.choice(self.camera_settings[category]["auto"])
        
        elif category == "aperture_settings":
            if context["scene_type"] == "portrait":
                return random.choice(self.camera_settings[category]["wide_aperture"])
            elif context["scene_type"] == "landscape":
                return random.choice(self.camera_settings[category]["narrow_aperture"])
            else:
                return random.choice(self.camera_settings[category]["auto"])
        
        elif category == "lighting_styles":
            if context["mood"] == "dramatic":
                return random.choice(self.camera_settings[category]["dramatic"])
            elif context["mood"] == "romantic":
                return random.choice(self.camera_settings[category]["soft"])
            elif context["environment"] == "outdoor":
                return random.choice(self.camera_settings[category]["natural"])
            else:
                return random.choice(self.camera_settings[category]["auto"])
        
        # Default fallback
        return random.choice(self.camera_settings[category].get("auto", list(self.camera_settings[category].values())[0]))
    
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
    
    def enhance_with_camera(self, base_prompt, photography_style, shot_type, camera_quality, **kwargs):
        """Main function to enhance prompt with professional camera settings"""
        
        # Analyze the base prompt for context-aware enhancements
        context = self.analyze_prompt_context(base_prompt) if kwargs.get("context_awareness", True) else {}
        
        camera_tags = []
        technical_tags = []
        summary_parts = []
        
        # Core photography style
        if photography_style != "auto":
            style_tags = self.quality_enhancers.get(photography_style, [photography_style])
            camera_tags.extend(style_tags)
            summary_parts.append(f"Style: {photography_style}")
        
        # Shot type selection
        shot_tag = self.smart_selection("shot_types", shot_type, context)
        camera_tags.append(shot_tag)
        summary_parts.append(f"Shot: {shot_tag}")
        
        # Lens selection
        lens_choice = kwargs.get("lens_type", "auto")
        lens_tag = self.smart_selection("lens_types", lens_choice, context)
        technical_tags.append(lens_tag)
        summary_parts.append(f"Lens: {lens_tag}")
        
        # Aperture settings
        aperture_choice = kwargs.get("aperture", "auto")
        aperture_tag = self.smart_selection("aperture_settings", aperture_choice, context)
        technical_tags.append(aperture_tag)
        summary_parts.append(f"Aperture: {aperture_tag}")
        
        # Camera angle
        angle_choice = kwargs.get("camera_angle", "auto")
        angle_tag = self.smart_selection("camera_angles", angle_choice, context)
        camera_tags.append(angle_tag)
        summary_parts.append(f"Angle: {angle_tag}")
        
        # Composition
        comp_choice = kwargs.get("composition", "auto")
        comp_tag = self.smart_selection("composition_rules", comp_choice, context)
        camera_tags.append(comp_tag)
        summary_parts.append(f"Composition: {comp_tag}")
        
        # Lighting
        light_choice = kwargs.get("lighting_style", "auto")
        light_tag = self.smart_selection("lighting_styles", light_choice, context)
        camera_tags.append(light_tag)
        summary_parts.append(f"Lighting: {light_tag}")
        
        # Focus technique
        focus_choice = kwargs.get("focus_technique", "auto")
        focus_tag = self.smart_selection("focus_techniques", focus_choice, context)
        technical_tags.append(focus_tag)
        summary_parts.append(f"Focus: {focus_tag}")
        
        # Camera movement
        movement_choice = kwargs.get("camera_movement", "auto")
        movement_tag = self.smart_selection("camera_movements", movement_choice, context)
        camera_tags.append(movement_tag)
        summary_parts.append(f"Movement: {movement_tag}")
        
        # Technical settings (if detailed mode)
        detail_level = kwargs.get("technical_detail", "standard")
        if detail_level in ["detailed", "technical"]:
            # ISO settings
            iso_choice = kwargs.get("iso_setting", "auto")
            if iso_choice != "auto":
                iso_tags = {
                    "low_iso_100": ["ISO_100", "clean_image", "no_noise"],
                    "medium_iso_400": ["ISO_400", "balanced", "versatile"],
                    "high_iso_1600": ["ISO_1600", "low_light", "slight_grain"],
                    "ultra_high_iso": ["high_ISO", "extreme_low_light", "film_grain"]
                }
                technical_tags.extend(iso_tags.get(iso_choice, [iso_choice]))
                summary_parts.append(f"ISO: {iso_choice}")
            
            # Shutter speed
            shutter_choice = kwargs.get("shutter_speed", "auto")
            if shutter_choice != "auto":
                shutter_tags = {
                    "fast_freeze": ["fast_shutter", "frozen_motion", "sharp_action"],
                    "medium_sharp": ["medium_shutter", "handheld_sharp"],
                    "slow_motion_blur": ["slow_shutter", "motion_blur", "dynamic_blur"],
                    "long_exposure": ["long_exposure", "light_trails", "smooth_water"]
                }
                technical_tags.extend(shutter_tags.get(shutter_choice, [shutter_choice]))
                summary_parts.append(f"Shutter: {shutter_choice}")
            
            # White balance
            wb_choice = kwargs.get("white_balance", "auto")
            if wb_choice != "auto":
                wb_tags = {
                    "daylight": ["daylight_balanced", "natural_colors"],
                    "tungsten": ["tungsten_balanced", "warm_corrected"],
                    "fluorescent": ["fluorescent_balanced", "cool_corrected"],
                    "cloudy": ["cloudy_balanced", "slightly_warm"],
                    "shade": ["shade_balanced", "blue_corrected"]
                }
                technical_tags.extend(wb_tags.get(wb_choice, [wb_choice]))
                summary_parts.append(f"WB: {wb_choice}")
        
        # Quality enhancers based on camera_quality
        quality_tags = {
            "standard": ["good_quality", "clear"],
            "professional": ["professional_quality", "commercial_grade", "high_end"],
            "high_end": ["premium_quality", "luxury_grade", "top_tier"],
            "cinematic": ["cinematic_quality", "film_grade", "movie_quality"]
        }
        camera_tags.extend(quality_tags.get(camera_quality, ["professional_quality"]))
        
        # Apply emphasis
        emphasis_level = kwargs.get("camera_emphasis", "medium")
        emphasized_camera_tags = [self.apply_emphasis(tag, emphasis_level) for tag in camera_tags]
        emphasized_technical_tags = [self.apply_emphasis(tag, emphasis_level) for tag in technical_tags]
        
        # Combine all tags
        all_camera_tags = emphasized_camera_tags + emphasized_technical_tags
        
        # Create enhanced prompt
        enhanced_prompt = f"{base_prompt}, {', '.join(all_camera_tags)}"
        
        # Create summary
        camera_summary = f"📸 Camera Settings Applied:\n" + "\n".join([f"• {part}" for part in summary_parts])
        if emphasis_level != "medium":
            camera_summary += f"\n• Emphasis: {emphasis_level}"
        
        return (enhanced_prompt, camera_summary)
