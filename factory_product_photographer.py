#!/usr/bin/env python3

"""
Factory Product Photographer - E-commerce and Product Photography Specialist
Provides optimization for product photography, brand consistency, and platform-specific formatting.

SFW Edition - GitHub Compliant - Professional Grade
"""

import random

class FactoryProductPhotographer:
    """
    Specialized product photography node that optimizes for e-commerce,
    brand consistency, and platform-specific requirements.
    """
    
    def __init__(self):
        # Comprehensive product photography styles covering all commercial scenarios
        self.photography_styles = {
            # E-commerce Essentials
            "clean_minimal": {
                "description": "Clean minimal product photography",
                "characteristics": ["white_background", "minimal_shadows", "even_lighting", "product_focus"],
                "tags": ["clean_product", "minimal_style", "white_background", "professional_clean"],
                "use_case": "e-commerce"
            },
            "amazon_optimized": {
                "description": "Amazon marketplace optimized photography",
                "characteristics": ["white_background_pure", "85_percent_frame_fill", "multiple_angles", "detail_shots"],
                "tags": ["amazon_ready", "marketplace_optimized", "guidelines_compliant", "sales_focused"],
                "use_case": "amazon_listing"
            },
            "shopify_standard": {
                "description": "Shopify store standard product shots",
                "characteristics": ["consistent_background", "brand_aligned", "mobile_optimized", "conversion_focused"],
                "tags": ["shopify_ready", "store_consistent", "mobile_friendly", "conversion_optimized"],
                "use_case": "shopify_store"
            },
            "etsy_handmade": {
                "description": "Etsy handmade product photography",
                "characteristics": ["artisan_feel", "handcrafted_story", "texture_emphasis", "authentic_presentation"],
                "tags": ["etsy_style", "handmade_appeal", "artisan_craft", "authentic_product"],
                "use_case": "etsy_listing"
            },
            "ebay_auction": {
                "description": "eBay auction product photography",
                "characteristics": ["detailed_condition", "multiple_views", "honest_representation", "competitive_appeal"],
                "tags": ["ebay_ready", "auction_style", "condition_clear", "competitive_listing"],
                "use_case": "ebay_auction"
            },
            
            # Lifestyle and Context
            "lifestyle_contextual": {
                "description": "Lifestyle contextual product shots",
                "characteristics": ["natural_setting", "context_provided", "storytelling", "relatable"],
                "tags": ["lifestyle_product", "contextual", "in_use", "natural_setting"],
                "use_case": "marketing"
            },
            "in_use_demonstration": {
                "description": "Product in active use demonstration",
                "characteristics": ["hands_on_interaction", "practical_application", "real_world_context", "usage_clarity"],
                "tags": ["in_use_shot", "demonstration", "practical_context", "user_interaction"],
                "use_case": "instructional"
            },
            "home_environment": {
                "description": "Product in home environment setting",
                "characteristics": ["domestic_setting", "interior_context", "cozy_atmosphere", "relatable_space"],
                "tags": ["home_setting", "domestic_product", "interior_styling", "lifestyle_integration"],
                "use_case": "home_goods"
            },
            "office_workspace": {
                "description": "Product in office workspace context",
                "characteristics": ["professional_environment", "work_context", "productivity_focus", "business_setting"],
                "tags": ["office_setting", "workspace_product", "professional_context", "business_use"],
                "use_case": "office_products"
            },
            "outdoor_adventure": {
                "description": "Product in outdoor adventure setting",
                "characteristics": ["natural_environment", "adventure_context", "durability_emphasis", "active_lifestyle"],
                "tags": ["outdoor_product", "adventure_gear", "nature_setting", "active_use"],
                "use_case": "outdoor_gear"
            },
            
            # Premium and Luxury
            "hero_dramatic": {
                "description": "Hero dramatic product photography",
                "characteristics": ["dramatic_lighting", "bold_composition", "premium_feel", "attention_grabbing"],
                "tags": ["hero_shot", "dramatic_product", "premium_style", "bold_composition"],
                "use_case": "advertising"
            },
            "luxury_premium": {
                "description": "Luxury premium product presentation",
                "characteristics": ["premium_materials", "elegant_composition", "exclusivity", "refined_aesthetic"],
                "tags": ["luxury_product", "premium_style", "elegant", "exclusive_appeal"],
                "use_case": "luxury"
            },
            "jewelry_precious": {
                "description": "Precious jewelry product photography",
                "characteristics": ["sparkle_enhancement", "reflection_control", "luxury_backdrop", "detail_precision"],
                "tags": ["jewelry_product", "precious_metals", "sparkle_capture", "luxury_jewelry"],
                "use_case": "jewelry"
            },
            "watch_timepiece": {
                "description": "Watch and timepiece photography",
                "characteristics": ["face_clarity", "mechanism_detail", "luxury_presentation", "precision_focus"],
                "tags": ["watch_product", "timepiece", "mechanism_detail", "precision_craft"],
                "use_case": "watches"
            },
            "automotive_luxury": {
                "description": "Luxury automotive product photography",
                "characteristics": ["reflective_surfaces", "power_emphasis", "premium_details", "performance_suggestion"],
                "tags": ["automotive_product", "luxury_vehicle", "performance_focus", "premium_auto"],
                "use_case": "automotive"
            },
            
            # Technical and Detailed
            "technical_detailed": {
                "description": "Technical detailed product documentation",
                "characteristics": ["detailed_view", "technical_accuracy", "informative", "precise"],
                "tags": ["technical_product", "detailed_view", "documentation", "precision"],
                "use_case": "technical"
            },
            "exploded_view": {
                "description": "Exploded view technical photography",
                "characteristics": ["component_separation", "assembly_clarity", "technical_diagram", "educational_focus"],
                "tags": ["exploded_view", "technical_diagram", "component_detail", "assembly_guide"],
                "use_case": "technical_manual"
            },
            "cutaway_section": {
                "description": "Cutaway section product photography",
                "characteristics": ["internal_structure", "cross_section", "educational_value", "technical_insight"],
                "tags": ["cutaway_view", "internal_structure", "cross_section", "technical_education"],
                "use_case": "educational"
            },
            "before_after": {
                "description": "Before and after product demonstration",
                "characteristics": ["transformation_shown", "effectiveness_proof", "comparison_clear", "result_emphasis"],
                "tags": ["before_after", "transformation", "effectiveness", "comparison_shot"],
                "use_case": "demonstration"
            },
            "size_comparison": {
                "description": "Size comparison product photography",
                "characteristics": ["scale_reference", "size_clarity", "proportion_understanding", "measurement_visual"],
                "tags": ["size_comparison", "scale_reference", "proportion", "measurement_guide"],
                "use_case": "sizing_guide"
            },
            
            # Food and Beverage
            "food_appetizing": {
                "description": "Appetizing food product photography",
                "characteristics": ["fresh_appearance", "texture_emphasis", "color_vibrant", "mouth_watering"],
                "tags": ["food_product", "appetizing", "fresh_food", "culinary_appeal"],
                "use_case": "food_marketing"
            },
            "beverage_refreshing": {
                "description": "Refreshing beverage product photography",
                "characteristics": ["condensation_drops", "ice_crystal", "liquid_clarity", "thirst_quenching"],
                "tags": ["beverage_product", "refreshing", "liquid_appeal", "drink_marketing"],
                "use_case": "beverage_marketing"
            },
            "ingredient_natural": {
                "description": "Natural ingredient product photography",
                "characteristics": ["organic_appearance", "natural_texture", "fresh_quality", "pure_ingredients"],
                "tags": ["ingredient_product", "natural_food", "organic", "pure_quality"],
                "use_case": "ingredient_marketing"
            },
            "packaging_design": {
                "description": "Product packaging design photography",
                "characteristics": ["label_clarity", "brand_visibility", "shelf_appeal", "package_integrity"],
                "tags": ["packaging_product", "label_design", "brand_showcase", "shelf_ready"],
                "use_case": "packaging_design"
            },
            
            # Fashion and Apparel
            "fashion_flat_lay": {
                "description": "Fashion flat lay product photography",
                "characteristics": ["garment_flat", "styling_accessories", "color_coordination", "layout_artistic"],
                "tags": ["fashion_product", "flat_lay", "garment_styling", "fashion_layout"],
                "use_case": "fashion_retail"
            },
            "apparel_detail": {
                "description": "Apparel detail product photography",
                "characteristics": ["fabric_texture", "construction_quality", "detail_focus", "craftsmanship"],
                "tags": ["apparel_product", "fabric_detail", "construction", "quality_showcase"],
                "use_case": "apparel_detail"
            },
            "shoes_footwear": {
                "description": "Shoes and footwear product photography",
                "characteristics": ["profile_angles", "sole_detail", "material_texture", "style_emphasis"],
                "tags": ["footwear_product", "shoe_detail", "style_showcase", "material_focus"],
                "use_case": "footwear"
            },
            "accessories_fashion": {
                "description": "Fashion accessories product photography",
                "characteristics": ["texture_detail", "color_accuracy", "style_focus", "versatility_shown"],
                "tags": ["accessory_product", "fashion_detail", "style_accent", "accessory_appeal"],
                "use_case": "accessories"
            },
            
            # Electronics and Technology
            "electronics_clean": {
                "description": "Clean electronics product photography",
                "characteristics": ["screen_clarity", "button_detail", "modern_aesthetic", "tech_appeal"],
                "tags": ["electronics_product", "tech_device", "modern_design", "digital_appeal"],
                "use_case": "electronics"
            },
            "gadget_innovative": {
                "description": "Innovative gadget product photography",
                "characteristics": ["feature_highlight", "innovation_emphasis", "modern_tech", "functionality_clear"],
                "tags": ["gadget_product", "innovation", "tech_feature", "modern_gadget"],
                "use_case": "tech_gadgets"
            },
            "software_ui": {
                "description": "Software UI product photography",
                "characteristics": ["screen_capture", "interface_clarity", "user_experience", "functionality_demo"],
                "tags": ["software_product", "ui_design", "interface", "digital_product"],
                "use_case": "software"
            },
            "mobile_app": {
                "description": "Mobile app product photography",
                "characteristics": ["phone_mockup", "app_interface", "user_interaction", "mobile_optimized"],
                "tags": ["app_product", "mobile_interface", "user_experience", "app_showcase"],
                "use_case": "mobile_apps"
            },
            
            # Health and Beauty
            "cosmetics_beauty": {
                "description": "Cosmetics beauty product photography",
                "characteristics": ["color_accuracy", "texture_appeal", "luxury_feel", "beauty_enhancement"],
                "tags": ["cosmetics_product", "beauty_appeal", "makeup", "skincare"],
                "use_case": "beauty_products"
            },
            "skincare_clean": {
                "description": "Skincare clean product photography",
                "characteristics": ["purity_emphasis", "clean_aesthetic", "health_focus", "ingredient_transparency"],
                "tags": ["skincare_product", "clean_beauty", "health_focus", "pure_ingredients"],
                "use_case": "skincare"
            },
            "supplement_health": {
                "description": "Health supplement product photography",
                "characteristics": ["clinical_clean", "health_emphasis", "trust_building", "quality_assurance"],
                "tags": ["supplement_product", "health_focus", "wellness", "quality_supplement"],
                "use_case": "health_supplements"
            },
            "fitness_equipment": {
                "description": "Fitness equipment product photography",
                "characteristics": ["strength_emphasis", "durability_shown", "action_ready", "performance_focus"],
                "tags": ["fitness_product", "exercise_equipment", "strength_training", "workout_gear"],
                "use_case": "fitness_equipment"
            },
            
            # Home and Garden
            "furniture_home": {
                "description": "Home furniture product photography",
                "characteristics": ["room_context", "comfort_emphasis", "style_showcase", "quality_materials"],
                "tags": ["furniture_product", "home_decor", "interior_design", "comfort_living"],
                "use_case": "furniture"
            },
            "kitchenware_functional": {
                "description": "Functional kitchenware product photography",
                "characteristics": ["utility_clear", "cooking_context", "durability_emphasis", "kitchen_ready"],
                "tags": ["kitchenware_product", "cooking_tools", "kitchen_utility", "culinary_equipment"],
                "use_case": "kitchenware"
            },
            "garden_outdoor": {
                "description": "Garden outdoor product photography",
                "characteristics": ["natural_setting", "outdoor_context", "weather_resistant", "garden_integration"],
                "tags": ["garden_product", "outdoor_living", "landscaping", "garden_tools"],
                "use_case": "gardening"
            },
            "home_improvement": {
                "description": "Home improvement product photography",
                "characteristics": ["tool_precision", "project_context", "durability_emphasis", "professional_grade"],
                "tags": ["home_improvement", "tool_product", "construction", "diy_project"],
                "use_case": "tools_hardware"
            },
            
            # Specialized Categories
            "toy_playful": {
                "description": "Playful toy product photography",
                "characteristics": ["fun_emphasis", "bright_colors", "play_context", "child_appeal"],
                "tags": ["toy_product", "playful", "child_friendly", "fun_design"],
                "use_case": "toys"
            },
            "pet_supplies": {
                "description": "Pet supplies product photography",
                "characteristics": ["pet_context", "comfort_emphasis", "safety_focus", "animal_friendly"],
                "tags": ["pet_product", "animal_care", "pet_comfort", "pet_safety"],
                "use_case": "pet_care"
            },
            "book_media": {
                "description": "Book and media product photography",
                "characteristics": ["cover_clarity", "content_preview", "educational_value", "knowledge_focus"],
                "tags": ["book_product", "media", "educational", "content_showcase"],
                "use_case": "books_media"
            },
            "art_supplies": {
                "description": "Art supplies product photography",
                "characteristics": ["creative_context", "color_accuracy", "artistic_potential", "quality_materials"],
                "tags": ["art_product", "creative_supplies", "artistic_tools", "creativity_enabler"],
                "use_case": "art_supplies"
            },
            "musical_instruments": {
                "description": "Musical instruments product photography",
                "characteristics": ["craftsmanship_detail", "sound_suggestion", "artistic_beauty", "quality_construction"],
                "tags": ["music_product", "instrument", "craftsmanship", "musical_quality"],
                "use_case": "musical_instruments"
            }
        }
        
        # Platform-specific optimizations
        self.platform_specs = {
            "amazon_ecommerce": {
                "requirements": ["white_background", "85%_frame_fill", "high_resolution", "no_watermarks"],
                "tags": ["amazon_compliant", "ecommerce_ready", "marketplace_optimized"],
                "aspect_ratio": "1:1",
                "background": "pure_white"
            },
            "shopify_store": {
                "requirements": ["consistent_styling", "brand_aligned", "mobile_optimized", "fast_loading"],
                "tags": ["shopify_optimized", "store_ready", "brand_consistent"],
                "aspect_ratio": "4:5",
                "background": "flexible"
            },
            "instagram_social": {
                "requirements": ["square_format", "visually_striking", "story_compatible", "mobile_first"],
                "tags": ["instagram_ready", "social_optimized", "mobile_friendly"],
                "aspect_ratio": "1:1",
                "background": "lifestyle"
            },
            "pinterest_discovery": {
                "requirements": ["vertical_format", "text_overlay_space", "visually_appealing", "clickable"],
                "tags": ["pinterest_optimized", "discovery_ready", "vertical_format"],
                "aspect_ratio": "2:3",
                "background": "contextual"
            },
            "facebook_catalog": {
                "requirements": ["catalog_compliant", "clear_product_view", "brand_consistent", "ad_ready"],
                "tags": ["facebook_catalog", "ad_optimized", "clear_view"],
                "aspect_ratio": "1:1",
                "background": "neutral"
            },
            "website_hero": {
                "requirements": ["high_impact", "brand_showcase", "responsive_design", "conversion_focused"],
                "tags": ["website_hero", "high_impact", "conversion_focused"],
                "aspect_ratio": "16:9",
                "background": "branded"
            },
            "print_catalog": {
                "requirements": ["high_resolution", "print_quality", "color_accurate", "detailed"],
                "tags": ["print_ready", "catalog_quality", "high_resolution"],
                "aspect_ratio": "4:5",
                "background": "neutral"
            },
            "email_marketing": {
                "requirements": ["attention_grabbing", "email_optimized", "quick_loading", "mobile_responsive"],
                "tags": ["email_optimized", "attention_grabbing", "mobile_ready"],
                "aspect_ratio": "2:1",
                "background": "simple"
            }
        }
        
        # Product categories and their specific needs
        self.product_categories = {
            "electronics_tech": {
                "focus_points": ["technical_details", "screen_visibility", "port_access", "sleek_design"],
                "tags": ["tech_product", "electronic_device", "modern_tech", "sleek_design"],
                "lighting_needs": ["even_lighting", "no_reflections", "detail_emphasis"]
            },
            "fashion_apparel": {
                "focus_points": ["fabric_texture", "fit_demonstration", "color_accuracy", "style_showcase"],
                "tags": ["fashion_product", "apparel", "textile", "style_focused"],
                "lighting_needs": ["soft_lighting", "texture_enhancement", "color_accurate"]
            },
            "beauty_cosmetics": {
                "focus_points": ["color_precision", "texture_detail", "packaging_elegance", "application_view"],
                "tags": ["beauty_product", "cosmetics", "color_accurate", "elegant"],
                "lighting_needs": ["color_accurate", "soft_shadows", "luxury_feel"]
            },
            "home_decor": {
                "focus_points": ["material_texture", "size_reference", "style_context", "room_integration"],
                "tags": ["home_decor", "interior_product", "lifestyle_context", "material_focus"],
                "lighting_needs": ["natural_lighting", "context_appropriate", "warm_atmosphere"]
            },
            "food_beverage": {
                "focus_points": ["appetizing_appearance", "freshness_indication", "ingredient_visibility", "serving_suggestion"],
                "tags": ["food_product", "appetizing", "fresh_appearance", "culinary"],
                "lighting_needs": ["warm_lighting", "appetizing_glow", "fresh_appearance"]
            },
            "jewelry_accessories": {
                "focus_points": ["detail_precision", "material_reflection", "craftsmanship", "luxury_presentation"],
                "tags": ["jewelry", "luxury_accessory", "precious", "detailed"],
                "lighting_needs": ["controlled_reflection", "detail_enhancement", "luxury_lighting"]
            },
            "sports_fitness": {
                "focus_points": ["functionality_demonstration", "durability_suggestion", "action_context", "performance_focus"],
                "tags": ["sports_product", "fitness_gear", "performance", "active"],
                "lighting_needs": ["dynamic_lighting", "action_ready", "performance_focused"]
            },
            "books_media": {
                "focus_points": ["cover_clarity", "spine_visibility", "content_preview", "collection_view"],
                "tags": ["book_product", "media", "educational", "content_focused"],
                "lighting_needs": ["even_lighting", "no_glare", "readable"]
            },
            "automotive_parts": {
                "focus_points": ["precision_engineering", "fit_compatibility", "material_quality", "technical_specs"],
                "tags": ["automotive", "precision_part", "engineering", "technical"],
                "lighting_needs": ["technical_lighting", "detail_focused", "professional"]
            },
            "toys_games": {
                "focus_points": ["fun_factor", "safety_features", "age_appropriateness", "play_demonstration"],
                "tags": ["toy_product", "family_friendly", "fun", "playful"],
                "lighting_needs": ["bright_lighting", "colorful", "inviting"]
            }
        }
        
        # Brand positioning styles
        self.brand_positioning = {
            "premium_luxury": {
                "characteristics": ["exclusive", "high_quality", "elegant"],
                "tags": ["premium_brand", "luxury_positioning",  "exclusive"],
                "visual_style": "refined"
            },
            "affordable_accessible": {
                "characteristics": ["value_focused", "practical", "relatable", "friendly"],
                "tags": ["affordable_brand", "accessible", "value_focused", "practical"],
                "visual_style": "approachable"
            },
            "innovative_tech": {
                "characteristics": ["cutting_edge", "modern", "advanced", "forward_thinking"],
                "tags": ["innovative_brand", "tech_forward", "modern", "advanced"],
                "visual_style": "futuristic"
            },
            "sustainable_eco": {
                "characteristics": ["environmentally_conscious", "natural", "responsible", "authentic"],
                "tags": ["sustainable_brand", "eco_friendly", "natural", "responsible"],
                "visual_style": "organic"
            },
            "artisan_handmade": {
                "characteristics": ["crafted", "authentic", "unique", "personal"],
                "tags": ["artisan_brand", "handmade", "crafted", "authentic"],
                "visual_style": "rustic"
            },
            "professional_business": {
                "characteristics": ["reliable", "efficient", "trustworthy", "corporate"],
                "tags": ["professional_brand", "business_grade", "reliable", "corporate"],
                "visual_style": "corporate"
            }
        }
        
        # Composition techniques for products
        self.composition_techniques = {
            "rule_of_thirds": {
                "description": "Product positioned using rule of thirds",
                "tags": ["rule_of_thirds", "balanced_composition", "dynamic_placement"]
            },
            "centered_symmetrical": {
                "description": "Centered symmetrical product placement",
                "tags": ["centered_composition", "symmetrical", "balanced", "formal"]
            },
            "diagonal_dynamic": {
                "description": "Dynamic diagonal product arrangement",
                "tags": ["diagonal_composition", "dynamic_angle", "energetic"]
            },
            "negative_space": {
                "description": "Emphasis on negative space around product",
                "tags": ["negative_space", "minimal_composition", "clean_layout"]
            },
            "layered_depth": {
                "description": "Layered composition with depth",
                "tags": ["layered_composition", "depth_of_field", "dimensional"]
            },
            "pattern_repetition": {
                "description": "Pattern and repetition in product layout",
                "tags": ["pattern_composition", "repetition", "rhythmic"]
            }
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        instance = cls()
        
        style_options = ["auto"] + list(instance.photography_styles.keys())
        platform_options = ["none"] + list(instance.platform_specs.keys())
        category_options = ["auto"] + list(instance.product_categories.keys())
        brand_options = ["auto"] + list(instance.brand_positioning.keys())
        composition_options = ["auto"] + list(instance.composition_techniques.keys())
        
        return {
            "required": {
                "base_prompt": ("STRING", {"forceInput": True}),
                "photography_style": (style_options, {"default": "clean_minimal"}),
                "product_focus": (["primary_product", "product_group", "lifestyle_context", "detail_macro", "comparison_view"], {"default": "primary_product"}),
            },
            "optional": {
                # Platform Optimization
                "target_platform": (platform_options, {"default": "none"}),
                "platform_compliance": ("BOOLEAN", {"default": True}),
                "mobile_optimization": ("BOOLEAN", {"default": True}),
                
                # Product Category
                "product_category": (category_options, {"default": "auto"}),
                "category_specific": ("BOOLEAN", {"default": True}),
                
                # Brand Positioning
                "brand_positioning": (brand_options, {"default": "auto"}),
                "brand_consistency": ("BOOLEAN", {"default": True}),
                "brand_colors": ("BOOLEAN", {"default": False}),
                
                # Technical Settings
                "background_style": (["auto", "pure_white", "neutral_gray", "transparent", "lifestyle", "gradient", "textured"], {"default": "auto"}),
                "lighting_setup": (["auto", "studio_even", "natural_soft", "dramatic_accent", "technical_precise"], {"default": "auto"}),
                "angle_perspective": (["auto", "straight_on", "three_quarter", "overhead", "low_angle", "detail_macro"], {"default": "auto"}),
                
                # Composition
                "composition_technique": (composition_options, {"default": "auto"}),
                "frame_filling": (["loose", "balanced", "tight", "full_frame"], {"default": "balanced"}),
                "depth_of_field": (["auto", "shallow", "moderate", "deep", "all_focus"], {"default": "auto"}),
                
                # Commercial Features
                "price_point_indicator": (["auto", "budget", "mid_range", "premium", "luxury"], {"default": "auto"}),
                "conversion_optimization": ("BOOLEAN", {"default": True}),
                "a_b_test_ready": ("BOOLEAN", {"default": False}),
                
                # Quality Standards
                "image_quality": (["standard", "high", "professional", "commercial"], {"default": "professional"}),
                "color_accuracy": (["standard", "enhanced", "true_to_life", "brand_matched"], {"default": "enhanced"}),
                "detail_level": (["overview", "detailed", "macro", "technical"], {"default": "detailed"}),
                
                # Marketing Integration
                "call_to_action_space": ("BOOLEAN", {"default": False}),
                "text_overlay_ready": ("BOOLEAN", {"default": False}),
                "social_sharing_optimized": ("BOOLEAN", {"default": False}),
                
                # Enhancement
                "product_emphasis": (["low", "medium", "high", "very_high"], {"default": "medium"}),
                "context_awareness": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("enhanced_prompt", "product_summary")
    FUNCTION = "optimize_product_photography"
    CATEGORY = "Camera Factory Station"
    
    def analyze_product_context(self, prompt):
        """Analyze prompt to understand product photography context"""
        prompt_lower = prompt.lower()
        
        # Detect product indicators
        product_keywords = {
            "electronics": ["phone", "laptop", "camera", "headphones", "gadget", "device"],
            "fashion": ["clothing", "shirt", "dress", "shoes", "accessories", "fabric"],
            "beauty": ["makeup", "skincare", "cosmetics", "perfume", "beauty"],
            "home": ["furniture", "decor", "kitchen", "home", "interior"],
            "food": ["food", "beverage", "drink", "meal", "snack", "culinary"],
            "jewelry": ["jewelry", "ring", "necklace", "watch", "precious", "gold"],
            "sports": ["sports", "fitness", "athletic", "exercise", "gym", "outdoor"],
            "automotive": ["car", "auto", "vehicle", "motor", "mechanical", "parts"]
        }
        
        detected_category = "general"
        for category, keywords in product_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_category = category
                break
        
        # Detect commercial intent
        commercial_keywords = ["product", "commercial", "marketing", "advertising", "sale", "buy", "purchase"]
        has_commercial_intent = any(keyword in prompt_lower for keyword in commercial_keywords)
        
        # Detect style preferences
        style_keywords = {
            "clean": ["clean", "minimal", "simple", "white"],
            "lifestyle": ["lifestyle", "natural", "contextual", "in_use"],
            "dramatic": ["dramatic", "bold", "striking", "hero"],
            "luxury": ["luxury", "premium", "elegant"]
        }
        
        detected_style = "clean"
        for style, keywords in style_keywords.items():
            if any(keyword in prompt_lower for keyword in keywords):
                detected_style = style
                break
        
        return {
            "product_category": detected_category,
            "commercial_intent": has_commercial_intent,
            "style_preference": detected_style,
            "has_product_context": detected_category != "general"
        }
    
    def select_configuration_by_style(self, style, context, **kwargs):
        """Select configuration based on photography style and context"""
        if style == "auto":
            # Auto-select based on context
            if context.get("commercial_intent", False):
                style = "clean_minimal"
            elif context.get("style_preference") == "luxury":
                style = "luxury_premium"
            elif context.get("style_preference") == "dramatic":
                style = "hero_dramatic"
            else:
                style = "clean_minimal"
        
        return self.photography_styles.get(style, self.photography_styles["clean_minimal"])
    
    def generate_product_tags(self, config, context, **kwargs):
        """Generate product photography tags"""
        tags = []
        
        # Base configuration tags
        tags.extend(config.get("tags", []))
        tags.extend(config.get("characteristics", []))
        
        # Platform-specific tags
        platform = kwargs.get("target_platform", "none")
        if platform != "none" and platform in self.platform_specs:
            platform_config = self.platform_specs[platform]
            tags.extend(platform_config["tags"])
            tags.extend(platform_config["requirements"])
            
            # Add background requirement
            bg_requirement = platform_config.get("background", "flexible")
            if bg_requirement != "flexible":
                tags.append(f"{bg_requirement}_background")
        elif platform != "none":
            print(f"Warning: Platform '{platform}' not found in platform_specs")
        
        # Category-specific tags
        category = kwargs.get("product_category", "auto")
        if category == "auto":
            category = context.get("product_category", "general")
        
        if category != "general" and category in self.product_categories:
            cat_config = self.product_categories[category]
            tags.extend(cat_config["tags"])
            tags.extend(cat_config["focus_points"])
            tags.extend(cat_config["lighting_needs"])
        elif category != "general":
            print(f"Warning: Product category '{category}' not found in product_categories")
        
        # Brand positioning
        brand = kwargs.get("brand_positioning", "auto")
        if brand != "auto" and brand in self.brand_positioning:
            brand_config = self.brand_positioning[brand]
            tags.extend(brand_config["tags"])
            tags.extend(brand_config["characteristics"])
            tags.append(f"{brand_config['visual_style']}_style")
        elif brand != "auto":
            print(f"Warning: Brand positioning '{brand}' not found in brand_positioning")
        
        # Technical settings
        background = kwargs.get("background_style", "auto")
        if background != "auto":
            tags.append(f"{background}_background")
        
        lighting = kwargs.get("lighting_setup", "auto")
        if lighting != "auto":
            tags.append(f"{lighting}_lighting")
        
        angle = kwargs.get("angle_perspective", "auto")
        if angle != "auto":
            tags.append(f"{angle}_angle")
        
        # Composition
        composition = kwargs.get("composition_technique", "auto")
        if composition != "auto" and composition in self.composition_techniques:
            comp_config = self.composition_techniques[composition]
            tags.extend(comp_config["tags"])
        elif composition != "auto":
            print(f"Warning: Composition technique '{composition}' not found in composition_techniques")
        
        # Frame filling
        frame_fill = kwargs.get("frame_filling", "balanced")
        tags.append(f"{frame_fill}_framing")
        
        # Quality settings
        quality = kwargs.get("image_quality", "professional")
        quality_tags = {
            "standard": ["standard_quality", "basic_commercial"],
            "high": ["high_quality", "enhanced_detail"],
            "professional": ["professional_quality", "commercial_grade"],
            "commercial": ["commercial_quality", "premium_standard"]
        }
        tags.extend(quality_tags[quality])
        
        # Color accuracy
        color_acc = kwargs.get("color_accuracy", "enhanced")
        color_tags = {
            "standard": ["standard_color", "basic_accuracy"],
            "enhanced": ["enhanced_color", "vibrant_accurate"],
            "true_to_life": ["true_to_life_color", "natural_accurate"],
            "brand_matched": ["brand_matched_color", "consistent_palette"]
        }
        tags.extend(color_tags[color_acc])
        
        # Detail level
        detail = kwargs.get("detail_level", "detailed")
        detail_tags = {
            "overview": ["overview_shot", "general_view"],
            "detailed": ["detailed_view", "feature_focus"],
            "macro": ["macro_detail", "close_up_precision"],
            "technical": ["technical_detail", "specification_view"]
        }
        tags.extend(detail_tags[detail])
        
        # Commercial optimization
        if kwargs.get("conversion_optimization", True):
            tags.extend(["conversion_optimized", "sales_focused", "purchase_intent"])
        
        if kwargs.get("mobile_optimization", True):
            tags.extend(["mobile_optimized", "responsive", "touch_friendly"])
        
        # Marketing features
        if kwargs.get("call_to_action_space", False):
            tags.extend(["cta_space", "text_ready", "marketing_layout"])
        
        if kwargs.get("social_sharing_optimized", False):
            tags.extend(["social_ready", "sharing_optimized", "viral_potential"])
        
        # Price point indication
        price_point = kwargs.get("price_point_indicator", "auto")
        if price_point != "auto":
            price_tags = {
                "budget": ["budget_friendly", "value_focused", "accessible"],
                "mid_range": ["mid_range", "balanced_value", "mainstream"],
                "premium": ["premium_product", "high_value", "quality_focused"],
                "luxury": ["luxury_product", "exclusive", "premium_tier"]
            }
            tags.extend(price_tags.get(price_point, []))
        
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
    
    def optimize_product_photography(self, base_prompt, photography_style, product_focus, **kwargs):
        """Main function to optimize product photography"""
        
        # Analyze product context
        context = self.analyze_product_context(base_prompt) if kwargs.get("context_awareness", True) else {}
        
        # Select photography configuration
        photo_config = self.select_configuration_by_style(photography_style, context, **kwargs)
        
        # Generate product photography tags
        product_tags = self.generate_product_tags(photo_config, context, **kwargs)
        
        # Add product focus tags
        focus_tags = {
            "primary_product": ["single_product_focus", "main_subject", "hero_product"],
            "product_group": ["product_group", "collection_shot", "family_view"],
            "lifestyle_context": ["lifestyle_context", "in_use", "natural_setting"],
            "detail_macro": ["macro_detail", "close_up", "feature_focus"],
            "comparison_view": ["comparison_shot", "side_by_side", "variant_display"]
        }
        product_tags.extend(focus_tags.get(product_focus, []))
        
        # Apply emphasis
        emphasis_level = kwargs.get("product_emphasis", "medium")
        emphasized_tags = [self.apply_emphasis(tag, emphasis_level) for tag in product_tags]
        
        # Create enhanced prompt
        enhanced_prompt = f"{base_prompt}, {', '.join(emphasized_tags)}"
        
        # Create summary
        summary_parts = [
            f"📸 Product Photography Optimized:",
            f"• Style: {photography_style}",
            f"• Configuration: {photo_config['description']}",
            f"• Focus: {product_focus}",
        ]
        
        if context.get("product_category", "general") != "general":
            summary_parts.append(f"• Category: {context['product_category']}")
        
        if context.get("commercial_intent"):
            summary_parts.append(f"• Commercial Intent: Detected")
        
        # Platform optimization
        platform = kwargs.get("target_platform", "none")
        if platform != "none":
            summary_parts.append(f"• Platform: {platform}")
            
            if platform in self.platform_specs:
                platform_config = self.platform_specs[platform]
                summary_parts.append(f"• Aspect Ratio: {platform_config['aspect_ratio']}")
            else:
                print(f"Warning: Platform '{platform}' not found in platform_specs for summary")
        
        # Brand and quality settings
        brand = kwargs.get("brand_positioning", "auto")
        if brand != "auto":
            summary_parts.append(f"• Brand Positioning: {brand}")
        
        quality = kwargs.get("image_quality", "professional")
        summary_parts.append(f"• Quality Standard: {quality}")
        
        # Technical settings
        technical_settings = []
        for key in ["background_style", "lighting_setup", "angle_perspective"]:
            value = kwargs.get(key, "auto")
            if value != "auto":
                technical_settings.append(f"{key.replace('_', ' ').title()}: {value}")
        
        if technical_settings:
            summary_parts.append(f"• Technical: {', '.join(technical_settings)}")
        
        # Commercial features
        commercial_features = []
        if kwargs.get("conversion_optimization", True):
            commercial_features.append("Conversion Optimized")
        if kwargs.get("mobile_optimization", True):
            commercial_features.append("Mobile Ready")
        if kwargs.get("social_sharing_optimized", False):
            commercial_features.append("Social Ready")
        
        if commercial_features:
            summary_parts.append(f"• Commercial: {', '.join(commercial_features)}")
        
        if emphasis_level != "medium":
            summary_parts.append(f"• Emphasis: {emphasis_level}")
        
        summary_parts.append(f"• Product Tags Added: {len(product_tags)}")
        
        product_summary = "\n".join(summary_parts)
        
        return (enhanced_prompt, product_summary)
