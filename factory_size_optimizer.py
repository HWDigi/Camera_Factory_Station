#!/usr/bin/env python3

"""
Factory Size Optimizer - Professional Sizing and Resolution Controls
Provides intelligent sizing options for different platforms, print formats, and use cases.

SFW Edition - GitHub Compliant - Professional Grade
"""

import math

class FactorySizeOptimizer:
    """
    Professional sizing node that optimizes dimensions for specific platforms,
    print formats, and use cases with aspect ratio intelligence.
    """
    
    def __init__(self):
        # Comprehensive platform-specific optimal sizes
        self.platform_sizes = {
            # Social Media Platforms - Instagram
            "instagram_square": {"width": 1080, "height": 1080, "ratio": "1:1", "description": "Instagram Square Post"},
            "instagram_portrait": {"width": 1080, "height": 1350, "ratio": "4:5", "description": "Instagram Portrait Post"},
            "instagram_landscape": {"width": 1080, "height": 566, "ratio": "1.91:1", "description": "Instagram Landscape Post"},
            "instagram_story": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "Instagram Story/Reels"},
            "instagram_carousel": {"width": 1080, "height": 1080, "ratio": "1:1", "description": "Instagram Carousel Slide"},
            "instagram_profile": {"width": 320, "height": 320, "ratio": "1:1", "description": "Instagram Profile Picture"},
            "instagram_highlight": {"width": 1080, "height": 1080, "ratio": "1:1", "description": "Instagram Story Highlight"},
            
            # Social Media Platforms - Facebook/Meta
            "facebook_post": {"width": 1200, "height": 630, "ratio": "1.91:1", "description": "Facebook Post"},
            "facebook_cover": {"width": 1200, "height": 315, "ratio": "3.8:1", "description": "Facebook Cover Photo"},
            "facebook_story": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "Facebook Story"},
            "facebook_event": {"width": 1920, "height": 1080, "ratio": "16:9", "description": "Facebook Event Cover"},
            "facebook_ad": {"width": 1200, "height": 628, "ratio": "1.91:1", "description": "Facebook Ad Image"},
            "facebook_profile": {"width": 180, "height": 180, "ratio": "1:1", "description": "Facebook Profile Picture"},
            
            # Social Media Platforms - Twitter/X
            "twitter_post": {"width": 1200, "height": 675, "ratio": "16:9", "description": "Twitter/X Post"},
            "twitter_header": {"width": 1500, "height": 500, "ratio": "3:1", "description": "Twitter/X Header"},
            "twitter_card": {"width": 1200, "height": 628, "ratio": "1.91:1", "description": "Twitter Card Image"},
            "twitter_profile": {"width": 400, "height": 400, "ratio": "1:1", "description": "Twitter Profile Picture"},
            
            # Social Media Platforms - LinkedIn
            "linkedin_post": {"width": 1200, "height": 627, "ratio": "1.91:1", "description": "LinkedIn Post"},
            "linkedin_banner": {"width": 1584, "height": 396, "ratio": "4:1", "description": "LinkedIn Banner"},
            "linkedin_company": {"width": 1192, "height": 220, "ratio": "5.4:1", "description": "LinkedIn Company Cover"},
            "linkedin_profile": {"width": 400, "height": 400, "ratio": "1:1", "description": "LinkedIn Profile Picture"},
            "linkedin_article": {"width": 1200, "height": 627, "ratio": "1.91:1", "description": "LinkedIn Article Header"},
            
            # Video Platforms - YouTube
            "youtube_thumbnail": {"width": 1280, "height": 720, "ratio": "16:9", "description": "YouTube Thumbnail"},
            "youtube_banner": {"width": 2560, "height": 1440, "ratio": "16:9", "description": "YouTube Channel Art"},
            "youtube_watermark": {"width": 150, "height": 150, "ratio": "1:1", "description": "YouTube Watermark"},
            "youtube_end_screen": {"width": 1280, "height": 720, "ratio": "16:9", "description": "YouTube End Screen"},
            "youtube_short": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "YouTube Shorts"},
            
            # Video Platforms - TikTok
            "tiktok_video": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "TikTok Video"},
            "tiktok_profile": {"width": 200, "height": 200, "ratio": "1:1", "description": "TikTok Profile Picture"},
            
            # Pinterest
            "pinterest_pin": {"width": 1000, "height": 1500, "ratio": "2:3", "description": "Pinterest Pin"},
            "pinterest_story": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "Pinterest Story Pin"},
            "pinterest_square": {"width": 1000, "height": 1000, "ratio": "1:1", "description": "Pinterest Square Pin"},
            "pinterest_wide": {"width": 1000, "height": 667, "ratio": "3:2", "description": "Pinterest Wide Pin"},
            
            # Other Social Platforms
            "snapchat_story": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "Snapchat Story"},
            "discord_banner": {"width": 960, "height": 540, "ratio": "16:9", "description": "Discord Server Banner"},
            "twitch_banner": {"width": 1920, "height": 480, "ratio": "4:1", "description": "Twitch Channel Banner"},
            "reddit_banner": {"width": 1920, "height": 384, "ratio": "5:1", "description": "Reddit Community Banner"},
            
            # Professional/Business Platforms
            "website_hero": {"width": 1920, "height": 1080, "ratio": "16:9", "description": "Website Hero Banner"},
            "website_thumbnail": {"width": 400, "height": 300, "ratio": "4:3", "description": "Website Thumbnail"},
            "website_full_width": {"width": 1920, "height": 600, "ratio": "3.2:1", "description": "Website Full Width Banner"},
            "website_blog_header": {"width": 1200, "height": 630, "ratio": "1.91:1", "description": "Blog Header Image"},
            
            # Email Marketing
            "email_header": {"width": 600, "height": 200, "ratio": "3:1", "description": "Email Header"},
            "email_banner": {"width": 600, "height": 300, "ratio": "2:1", "description": "Email Newsletter Banner"},
            "email_signature": {"width": 300, "height": 100, "ratio": "3:1", "description": "Email Signature Banner"},
            "email_mobile": {"width": 320, "height": 180, "ratio": "16:9", "description": "Mobile Email Banner"},
            
            # E-commerce Platforms
            "amazon_main": {"width": 2000, "height": 2000, "ratio": "1:1", "description": "Amazon Main Image"},
            "amazon_additional": {"width": 1500, "height": 1500, "ratio": "1:1", "description": "Amazon Additional Images"},
            "shopify_product": {"width": 2048, "height": 2048, "ratio": "1:1", "description": "Shopify Product Image"},
            "shopify_collection": {"width": 1024, "height": 1024, "ratio": "1:1", "description": "Shopify Collection Image"},
            "etsy_listing": {"width": 2000, "height": 2000, "ratio": "1:1", "description": "Etsy Listing Photo"},
            "etsy_shop_banner": {"width": 1200, "height": 300, "ratio": "4:1", "description": "Etsy Shop Banner"},
            "ebay_listing": {"width": 1600, "height": 1600, "ratio": "1:1", "description": "eBay Listing Photo"},
            "woocommerce_product": {"width": 1024, "height": 1024, "ratio": "1:1", "description": "WooCommerce Product"},
            
            # Advertising Formats
            "google_ad_square": {"width": 1200, "height": 1200, "ratio": "1:1", "description": "Google Ads Square"},
            "google_ad_landscape": {"width": 1200, "height": 628, "ratio": "1.91:1", "description": "Google Ads Landscape"},
            "facebook_ad_carousel": {"width": 1080, "height": 1080, "ratio": "1:1", "description": "Facebook Carousel Ad"},
            "instagram_ad_story": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "Instagram Story Ad"},
            "display_banner_728x90": {"width": 728, "height": 90, "ratio": "8.09:1", "description": "Leaderboard Banner"},
            "display_banner_300x250": {"width": 300, "height": 250, "ratio": "1.2:1", "description": "Medium Rectangle"},
            "display_banner_160x600": {"width": 160, "height": 600, "ratio": "0.27:1", "description": "Wide Skyscraper"},
            
            # Print Formats - Standard (300 DPI)
            "print_wallet": {"width": 900, "height": 600, "ratio": "3:2", "description": "Wallet Size (300 DPI)"},
            "print_3x5": {"width": 1500, "height": 900, "ratio": "5:3", "description": "3x5 Print (300 DPI)"},
            "print_4x6": {"width": 1800, "height": 1200, "ratio": "3:2", "description": "4x6 Print (300 DPI)"},
            "print_5x7": {"width": 2100, "height": 1500, "ratio": "7:5", "description": "5x7 Print (300 DPI)"},
            "print_8x10": {"width": 3000, "height": 2400, "ratio": "5:4", "description": "8x10 Print (300 DPI)"},
            "print_8x12": {"width": 3600, "height": 2400, "ratio": "3:2", "description": "8x12 Print (300 DPI)"},
            "print_11x14": {"width": 4200, "height": 3300, "ratio": "14:11", "description": "11x14 Print (300 DPI)"},
            "print_11x17": {"width": 5100, "height": 3300, "ratio": "17:11", "description": "11x17 Print (300 DPI)"},
            "print_12x18": {"width": 5400, "height": 3600, "ratio": "3:2", "description": "12x18 Print (300 DPI)"},
            "print_16x20": {"width": 6000, "height": 4800, "ratio": "5:4", "description": "16x20 Print (300 DPI)"},
            "print_16x24": {"width": 7200, "height": 4800, "ratio": "3:2", "description": "16x24 Print (300 DPI)"},
            "print_20x24": {"width": 7200, "height": 6000, "ratio": "6:5", "description": "20x24 Print (300 DPI)"},
            "print_20x30": {"width": 9000, "height": 6000, "ratio": "3:2", "description": "20x30 Print (300 DPI)"},
            "print_24x36": {"width": 10800, "height": 7200, "ratio": "3:2", "description": "24x36 Print (300 DPI)"},
            
            # Print Formats - Large Format (150 DPI)
            "poster_18x24": {"width": 2700, "height": 3600, "ratio": "3:4", "description": "18x24 Poster (150 DPI)"},
            "poster_24x36": {"width": 3600, "height": 5400, "ratio": "2:3", "description": "24x36 Poster (150 DPI)"},
            "poster_27x40": {"width": 4050, "height": 6000, "ratio": "27:40", "description": "Movie Poster (150 DPI)"},
            "billboard_small": {"width": 1800, "height": 600, "ratio": "3:1", "description": "Small Billboard (72 DPI)"},
            "billboard_large": {"width": 2880, "height": 864, "ratio": "10:3", "description": "Large Billboard (72 DPI)"},
            
            # Business Cards and Stationery
            "business_card_us": {"width": 1050, "height": 600, "ratio": "1.75:1", "description": "US Business Card (300 DPI)"},
            "business_card_eu": {"width": 1063, "height": 638, "ratio": "1.67:1", "description": "EU Business Card (300 DPI)"},
            "letterhead": {"width": 2550, "height": 3300, "ratio": "17:22", "description": "Letterhead (300 DPI)"},
            "envelope_standard": {"width": 2975, "height": 1238, "ratio": "2.4:1", "description": "Standard Envelope (300 DPI)"},
            
            # Standard Video/TV Resolutions
            "ntsc_480i": {"width": 720, "height": 480, "ratio": "3:2", "description": "NTSC 480i"},
            "pal_576i": {"width": 720, "height": 576, "ratio": "5:4", "description": "PAL 576i"},
            "sd_480p": {"width": 640, "height": 480, "ratio": "4:3", "description": "SD 480p"},
            "ed_480p": {"width": 854, "height": 480, "ratio": "16:9", "description": "Enhanced Definition 480p"},
            "hd_720p": {"width": 1280, "height": 720, "ratio": "16:9", "description": "HD 720p"},
            "hd_900p": {"width": 1600, "height": 900, "ratio": "16:9", "description": "HD+ 900p"},
            "fhd_1080p": {"width": 1920, "height": 1080, "ratio": "16:9", "description": "Full HD 1080p"},
            "qhd_1440p": {"width": 2560, "height": 1440, "ratio": "16:9", "description": "QHD 1440p"},
            "uhd_4k": {"width": 3840, "height": 2160, "ratio": "16:9", "description": "4K UHD"},
            "cinema_4k": {"width": 4096, "height": 2160, "ratio": "1.9:1", "description": "Cinema 4K DCI"},
            "uhd_8k": {"width": 7680, "height": 4320, "ratio": "16:9", "description": "8K UHD"},
            "cinema_8k": {"width": 8192, "height": 4320, "ratio": "1.9:1", "description": "Cinema 8K DCI"},
            
            # Gaming and VR Resolutions
            "vga": {"width": 640, "height": 480, "ratio": "4:3", "description": "VGA Resolution"},
            "svga": {"width": 800, "height": 600, "ratio": "4:3", "description": "SVGA Resolution"},
            "xga": {"width": 1024, "height": 768, "ratio": "4:3", "description": "XGA Resolution"},
            "sxga": {"width": 1280, "height": 1024, "ratio": "5:4", "description": "SXGA Resolution"},
            "uxga": {"width": 1600, "height": 1200, "ratio": "4:3", "description": "UXGA Resolution"},
            "wuxga": {"width": 1920, "height": 1200, "ratio": "8:5", "description": "WUXGA Resolution"},
            "vr_oculus": {"width": 2880, "height": 1700, "ratio": "1.69:1", "description": "Oculus VR Resolution"},
            "vr_vive": {"width": 2160, "height": 1200, "ratio": "1.8:1", "description": "HTC Vive Resolution"},
            
            # Mobile and Tablet Formats
            "iphone_se": {"width": 750, "height": 1334, "ratio": "9:16", "description": "iPhone SE Screen"},
            "iphone_standard": {"width": 828, "height": 1792, "ratio": "9:19.5", "description": "iPhone 11 Screen"},
            "iphone_pro": {"width": 1125, "height": 2436, "ratio": "9:19.5", "description": "iPhone Pro Screen"},
            "iphone_pro_max": {"width": 1284, "height": 2778, "ratio": "9:19.5", "description": "iPhone Pro Max Screen"},
            "ipad": {"width": 1620, "height": 2160, "ratio": "3:4", "description": "iPad Screen"},
            "ipad_pro": {"width": 2048, "height": 2732, "ratio": "3:4", "description": "iPad Pro Screen"},
            "android_phone": {"width": 1080, "height": 2340, "ratio": "9:19.5", "description": "Android Phone Screen"},
            "android_tablet": {"width": 1200, "height": 1920, "ratio": "5:8", "description": "Android Tablet Screen"},
            
            # Portrait Orientations
            "portrait_2_3": {"width": 1080, "height": 1620, "ratio": "2:3", "description": "Portrait 2:3"},
            "portrait_3_4": {"width": 1080, "height": 1440, "ratio": "3:4", "description": "Portrait 3:4"},
            "portrait_4_5": {"width": 1080, "height": 1350, "ratio": "4:5", "description": "Portrait 4:5"},
            "portrait_9_16": {"width": 1080, "height": 1920, "ratio": "9:16", "description": "Portrait 9:16"},
            "portrait_tall": {"width": 1080, "height": 2400, "ratio": "9:20", "description": "Tall Portrait"},
            
            # Square Formats
            "square_256": {"width": 256, "height": 256, "ratio": "1:1", "description": "Square 256x256"},
            "square_512": {"width": 512, "height": 512, "ratio": "1:1", "description": "Square 512x512"},
            "square_768": {"width": 768, "height": 768, "ratio": "1:1", "description": "Square 768x768"},
            "square_1024": {"width": 1024, "height": 1024, "ratio": "1:1", "description": "Square 1024x1024"},
            "square_1536": {"width": 1536, "height": 1536, "ratio": "1:1", "description": "Square 1536x1536"},
            "square_2048": {"width": 2048, "height": 2048, "ratio": "1:1", "description": "Square 2048x2048"},
            "square_4096": {"width": 4096, "height": 4096, "ratio": "1:1", "description": "Square 4096x4096"},
            
            # Panoramic and Wide Formats
            "panoramic_2_1": {"width": 2048, "height": 1024, "ratio": "2:1", "description": "Panoramic 2:1"},
            "panoramic_3_1": {"width": 3072, "height": 1024, "ratio": "3:1", "description": "Panoramic 3:1"},
            "panoramic_4_1": {"width": 4096, "height": 1024, "ratio": "4:1", "description": "Panoramic 4:1"},
            "panoramic_6_1": {"width": 6144, "height": 1024, "ratio": "6:1", "description": "Ultra Panoramic 6:1"},
            "ultrawide_21_9": {"width": 2560, "height": 1080, "ratio": "21:9", "description": "Ultrawide 21:9"},
            "ultrawide_32_9": {"width": 3840, "height": 1080, "ratio": "32:9", "description": "Super Ultrawide 32:9"},
            
            # AI Training Common Sizes
            "ai_training_512": {"width": 512, "height": 512, "ratio": "1:1", "description": "AI Training 512x512"},
            "ai_training_768": {"width": 768, "height": 768, "ratio": "1:1", "description": "AI Training 768x768"},
            "ai_training_1024": {"width": 1024, "height": 1024, "ratio": "1:1", "description": "AI Training 1024x1024"},
            "ai_sdxl": {"width": 1024, "height": 1024, "ratio": "1:1", "description": "SDXL Base Resolution"},
            "ai_flux": {"width": 1024, "height": 1024, "ratio": "1:1", "description": "Flux Base Resolution"},
        }
        
        # Comprehensive aspect ratios for all use cases
        self.aspect_ratios = {
            # Standard Photo Ratios
            "1:1": {"ratio": 1.0, "description": "Square (Instagram, Profile Pictures)"},
            "4:3": {"ratio": 1.333, "description": "Traditional Photo (Micro Four Thirds)"},
            "3:2": {"ratio": 1.5, "description": "Classic Film (35mm Film, Most DSLRs)"},
            "5:4": {"ratio": 1.25, "description": "Large Format (8x10 Print)"},
            "8:10": {"ratio": 0.8, "description": "Portrait Standard (8x10)"},
            "11:14": {"ratio": 0.786, "description": "Portrait Extended (11x14)"},
            
            # Widescreen and Cinema Ratios
            "16:9": {"ratio": 1.778, "description": "HD Widescreen (TV, Monitor)"},
            "16:10": {"ratio": 1.6, "description": "Computer Monitor (MacBook)"},
            "21:9": {"ratio": 2.333, "description": "Ultrawide Monitor"},
            "32:9": {"ratio": 3.556, "description": "Super Ultrawide Monitor"},
            "2:1": {"ratio": 2.0, "description": "Univisium (Cinema)"},
            "2.35:1": {"ratio": 2.35, "description": "Cinemascope (Anamorphic)"},
            "2.39:1": {"ratio": 2.39, "description": "Modern Cinema Standard"},
            "1.85:1": {"ratio": 1.85, "description": "US Cinema Standard"},
            "1.43:1": {"ratio": 1.43, "description": "IMAX Format"},
            
            # Social Media Ratios
            "4:5": {"ratio": 0.8, "description": "Instagram Portrait Post"},
            "1.91:1": {"ratio": 1.91, "description": "Facebook/Twitter Landscape"},
            "9:16": {"ratio": 0.563, "description": "Mobile Portrait (Stories, TikTok)"},
            "1:2": {"ratio": 0.5, "description": "Tall Portrait (Pinterest)"},
            "2:3": {"ratio": 0.667, "description": "Portrait Classic (Pinterest Pin)"},
            "3:4": {"ratio": 0.75, "description": "Portrait Standard (Instagram)"},
            
            # Print and Design Ratios
            "8.5:11": {"ratio": 0.773, "description": "US Letter Paper"},
            "210:297": {"ratio": 0.707, "description": "A4 Paper (ISO Standard)"},
            "11:17": {"ratio": 0.647, "description": "Tabloid/Ledger"},
            "1.618:1": {"ratio": 1.618, "description": "Golden Ratio"},
            "√2:1": {"ratio": 1.414, "description": "Silver Ratio (A-Series Paper)"},
            "√3:1": {"ratio": 1.732, "description": "Bronze Ratio"},
            "φ:1": {"ratio": 1.618, "description": "Phi Ratio (Golden)"},
            
            # Video Game and VR Ratios
            "4:3": {"ratio": 1.333, "description": "Retro Gaming (CRT)"},
            "5:3": {"ratio": 1.667, "description": "Gaming Laptop"},
            "8:5": {"ratio": 1.6, "description": "Gaming Monitor (16:10)"},
            "12:5": {"ratio": 2.4, "description": "Triple Monitor Setup"},
            "1.9:1": {"ratio": 1.9, "description": "DCI Cinema 4K"},
            
            # Mobile Device Ratios
            "18:9": {"ratio": 2.0, "description": "Modern Smartphone"},
            "19:9": {"ratio": 2.111, "description": "Tall Smartphone"},
            "19.5:9": {"ratio": 2.167, "description": "iPhone X+ Series"},
            "20:9": {"ratio": 2.222, "description": "Extra Tall Smartphone"},
            "18.5:9": {"ratio": 2.056, "description": "Samsung Galaxy"},
            
            # Tablet Ratios
            "4:3": {"ratio": 1.333, "description": "iPad Standard"},
            "16:10": {"ratio": 1.6, "description": "Android Tablet"},
            "3:4": {"ratio": 0.75, "description": "iPad Portrait"},
            
            # Panoramic Ratios
            "3:1": {"ratio": 3.0, "description": "Panoramic Standard"},
            "4:1": {"ratio": 4.0, "description": "Wide Panoramic"},
            "5:1": {"ratio": 5.0, "description": "Ultra Wide Panoramic"},
            "6:1": {"ratio": 6.0, "description": "Extreme Panoramic"},
            "12:1": {"ratio": 12.0, "description": "360° Partial Panoramic"},
            
            # Vertical Panoramic
            "1:3": {"ratio": 0.333, "description": "Vertical Panoramic"},
            "1:4": {"ratio": 0.25, "description": "Tall Vertical Panoramic"},
            "1:5": {"ratio": 0.2, "description": "Skyscraper Panoramic"},
            
            # Artistic and Creative Ratios
            "1.272:1": {"ratio": 1.272, "description": "Plastic Number Ratio"},
            "1.325:1": {"ratio": 1.325, "description": "Academy Ratio (Silent Film)"},
            "1.375:1": {"ratio": 1.375, "description": "Academy Standard"},
            "1.66:1": {"ratio": 1.66, "description": "European Widescreen"},
            "1.75:1": {"ratio": 1.75, "description": "Early Widescreen"},
            "2.2:1": {"ratio": 2.2, "description": "70mm Films"},
            "2.55:1": {"ratio": 2.55, "description": "Original CinemaScope"},
            "2.76:1": {"ratio": 2.76, "description": "Ultra Panavision"},
            
            # Business Card and Stationery
            "1.75:1": {"ratio": 1.75, "description": "US Business Card"},
            "1.67:1": {"ratio": 1.67, "description": "EU Business Card"},
            "1.41:1": {"ratio": 1.41, "description": "Credit Card Standard"},
            
            # Square Variants
            "1:1": {"ratio": 1.0, "description": "Perfect Square"},
            "1.05:1": {"ratio": 1.05, "description": "Near Square Landscape"},
            "1:1.05": {"ratio": 0.952, "description": "Near Square Portrait"},
        }
        
        # Comprehensive DPI/Quality presets for all use cases
        self.quality_presets = {
            # Web and Digital Display
            "web_minimal": {"dpi": 72, "quality": "minimal", "description": "Basic Web Display (72 DPI)"},
            "web_optimized": {"dpi": 96, "quality": "optimized", "description": "Standard Web Display (96 DPI)"},
            "web_enhanced": {"dpi": 120, "quality": "enhanced", "description": "Enhanced Web Display (120 DPI)"},
            "web_high": {"dpi": 144, "quality": "high", "description": "High-DPI Screens (144 DPI)"},
            "web_retina": {"dpi": 192, "quality": "retina", "description": "Retina/HiDPI Displays (192 DPI)"},
            "web_ultra": {"dpi": 240, "quality": "ultra", "description": "Ultra High-DPI (240 DPI)"},
            
            # Social Media Optimized
            "social_standard": {"dpi": 72, "quality": "social", "description": "Social Media Standard (72 DPI)"},
            "social_enhanced": {"dpi": 96, "quality": "social_plus", "description": "Enhanced Social Media (96 DPI)"},
            "social_premium": {"dpi": 144, "quality": "social_premium", "description": "Premium Social Media (144 DPI)"},
            
            # Email and Digital Marketing
            "email_basic": {"dpi": 72, "quality": "email", "description": "Email Marketing (72 DPI)"},
            "email_enhanced": {"dpi": 96, "quality": "email_plus", "description": "Enhanced Email (96 DPI)"},
            "newsletter_quality": {"dpi": 120, "quality": "newsletter", "description": "Newsletter Quality (120 DPI)"},
            
            # Print Qualities
            "print_draft": {"dpi": 150, "quality": "draft", "description": "Draft Print Quality (150 DPI)"},
            "print_standard": {"dpi": 300, "quality": "print", "description": "Standard Print Quality (300 DPI)"},
            "print_enhanced": {"dpi": 400, "quality": "enhanced_print", "description": "Enhanced Print (400 DPI)"},
            "print_high": {"dpi": 600, "quality": "premium", "description": "High-End Print (600 DPI)"},
            "print_professional": {"dpi": 720, "quality": "professional", "description": "Professional Print (720 DPI)"},
            "print_ultra": {"dpi": 900, "quality": "ultra_print", "description": "Ultra Print Quality (900 DPI)"},
            
            # Large Format and Poster
            "poster_standard": {"dpi": 150, "quality": "poster", "description": "Standard Poster (150 DPI)"},
            "poster_enhanced": {"dpi": 200, "quality": "poster_plus", "description": "Enhanced Poster (200 DPI)"},
            "poster_premium": {"dpi": 250, "quality": "poster_premium", "description": "Premium Poster (250 DPI)"},
            "billboard_standard": {"dpi": 30, "quality": "billboard", "description": "Billboard Standard (30 DPI)"},
            "billboard_enhanced": {"dpi": 50, "quality": "billboard_plus", "description": "Enhanced Billboard (50 DPI)"},
            "signage_large": {"dpi": 72, "quality": "signage", "description": "Large Format Signage (72 DPI)"},
            
            # Photography and Fine Art
            "photo_standard": {"dpi": 300, "quality": "photo", "description": "Standard Photo (300 DPI)"},
            "photo_enhanced": {"dpi": 400, "quality": "photo_plus", "description": "Enhanced Photo (400 DPI)"},
            "photo_professional": {"dpi": 600, "quality": "photo_pro", "description": "Professional Photo (600 DPI)"},
            "fine_art": {"dpi": 720, "quality": "fine_art", "description": "Fine Art Print (720 DPI)"},
            "gallery_quality": {"dpi": 900, "quality": "gallery", "description": "Gallery Quality (900 DPI)"},
            "museum_quality": {"dpi": 1200, "quality": "museum", "description": "Museum Quality (1200 DPI)"},
            "archival": {"dpi": 1440, "quality": "archival", "description": "Archival Quality (1440 DPI)"},
            "master_archive": {"dpi": 2400, "quality": "master", "description": "Master Archive (2400 DPI)"},
            
            # Professional Publishing
            "magazine_standard": {"dpi": 300, "quality": "magazine", "description": "Magazine Standard (300 DPI)"},
            "magazine_premium": {"dpi": 400, "quality": "magazine_premium", "description": "Premium Magazine (400 DPI)"},
            "book_interior": {"dpi": 300, "quality": "book", "description": "Book Interior (300 DPI)"},
            "book_cover": {"dpi": 300, "quality": "book_cover", "description": "Book Cover (300 DPI)"},
            "textbook_quality": {"dpi": 400, "quality": "textbook", "description": "Textbook Quality (400 DPI)"},
            "catalog_standard": {"dpi": 300, "quality": "catalog", "description": "Product Catalog (300 DPI)"},
            "catalog_premium": {"dpi": 400, "quality": "catalog_premium", "description": "Premium Catalog (400 DPI)"},
            
            # Business and Marketing
            "business_card": {"dpi": 300, "quality": "business", "description": "Business Card (300 DPI)"},
            "brochure_standard": {"dpi": 300, "quality": "brochure", "description": "Standard Brochure (300 DPI)"},
            "brochure_premium": {"dpi": 400, "quality": "brochure_premium", "description": "Premium Brochure (400 DPI)"},
            "flyer_standard": {"dpi": 300, "quality": "flyer", "description": "Standard Flyer (300 DPI)"},
            "presentation_screen": {"dpi": 150, "quality": "presentation", "description": "Screen Presentation (150 DPI)"},
            "presentation_print": {"dpi": 300, "quality": "presentation_print", "description": "Print Presentation (300 DPI)"},
            
            # Packaging and Labels
            "packaging_standard": {"dpi": 300, "quality": "packaging", "description": "Product Packaging (300 DPI)"},
            "packaging_premium": {"dpi": 400, "quality": "packaging_premium", "description": "Premium Packaging (400 DPI)"},
            "label_standard": {"dpi": 300, "quality": "label", "description": "Product Label (300 DPI)"},
            "label_high_detail": {"dpi": 600, "quality": "label_detail", "description": "Detailed Label (600 DPI)"},
            
            # Gaming and Interactive
            "game_texture_low": {"dpi": 72, "quality": "game_low", "description": "Game Texture Low (72 DPI)"},
            "game_texture_med": {"dpi": 150, "quality": "game_med", "description": "Game Texture Medium (150 DPI)"},
            "game_texture_high": {"dpi": 300, "quality": "game_high", "description": "Game Texture High (300 DPI)"},
            "game_texture_ultra": {"dpi": 600, "quality": "game_ultra", "description": "Game Texture Ultra (600 DPI)"},
            "ui_standard": {"dpi": 96, "quality": "ui", "description": "User Interface (96 DPI)"},
            "ui_retina": {"dpi": 192, "quality": "ui_retina", "description": "Retina UI (192 DPI)"},
            
            # Video Production
            "video_thumbnail": {"dpi": 72, "quality": "video_thumb", "description": "Video Thumbnail (72 DPI)"},
            "video_title_card": {"dpi": 150, "quality": "video_title", "description": "Video Title Card (150 DPI)"},
            "video_graphics": {"dpi": 300, "quality": "video_gfx", "description": "Video Graphics (300 DPI)"},
            "broadcast_standard": {"dpi": 72, "quality": "broadcast", "description": "Broadcast Standard (72 DPI)"},
            
            # AI and Machine Learning
            "ai_training_low": {"dpi": 72, "quality": "ai_low", "description": "AI Training Low Res (72 DPI)"},
            "ai_training_med": {"dpi": 150, "quality": "ai_med", "description": "AI Training Medium (150 DPI)"},
            "ai_training_high": {"dpi": 300, "quality": "ai_high", "description": "AI Training High Res (300 DPI)"},
            "ai_inference": {"dpi": 96, "quality": "ai_inference", "description": "AI Inference (96 DPI)"},
            "dataset_standard": {"dpi": 150, "quality": "dataset", "description": "Dataset Standard (150 DPI)"},
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        instance = cls()
        platform_options = ["custom"] + list(instance.platform_sizes.keys())
        ratio_options = ["auto"] + list(instance.aspect_ratios.keys())
        quality_options = list(instance.quality_presets.keys())
        
        return {
            "required": {
                "base_prompt": ("STRING", {"forceInput": True}),
                "size_preset": (platform_options, {"default": "fhd_1080p"}),
                "optimization_target": (["quality", "file_size", "balanced", "performance", "bandwidth", "storage"], {"default": "balanced"}),
            },
            "optional": {
                # Custom sizing
                "custom_width": ("INT", {"default": 1024, "min": 64, "max": 16384, "step": 8}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 16384, "step": 8}),
                "aspect_ratio": (ratio_options, {"default": "auto"}),
                "maintain_aspect": ("BOOLEAN", {"default": True}),
                "force_multiple_of_8": ("BOOLEAN", {"default": True}),
                
                # Quality and Performance
                "quality_preset": (quality_options, {"default": "web_high"}),
                "dpi_override": ("INT", {"default": 0, "min": 0, "max": 3000, "step": 1}),
                "upscale_method": (["none", "nearest", "linear", "cubic", "lanczos", "area", "bicubic", "ai_upscale", "super_resolution"], {"default": "none"}),
                "downscale_method": (["none", "nearest", "linear", "cubic", "lanczos", "area", "bicubic", "mitchell"], {"default": "area"}),
                "interpolation_quality": (["fastest", "fast", "balanced", "high_quality", "best"], {"default": "balanced"}),
                
                # Platform Optimization
                "platform_optimization": ("BOOLEAN", {"default": True}),
                "mobile_optimization": ("BOOLEAN", {"default": False}),
                "retina_optimization": ("BOOLEAN", {"default": False}),
                "compression_target": (["none", "jpg_low", "jpg_medium", "jpg_high", "jpg_maximum", "png_8bit", "png_24bit", "png_optimized", "webp_lossy", "webp_lossless", "avif", "heic"], {"default": "none"}),
                "progressive_encoding": ("BOOLEAN", {"default": False}),
                
                # Professional Settings
                "color_space": (["sRGB", "Adobe_RGB", "ProPhoto_RGB", "Rec2020", "DCI_P3", "Rec709", "CMYK"], {"default": "sRGB"}),
                "color_profile": (["auto", "embedded", "sRGB_IEC61966", "Adobe_RGB_1998", "ProPhoto_RGB", "Rec2020", "DCI_P3"], {"default": "auto"}),
                "bit_depth": (["8_bit", "10_bit", "12_bit", "16_bit", "32_bit_float"], {"default": "8_bit"}),
                "output_format": (["auto", "jpg", "png", "webp", "tiff", "bmp", "tga", "exr", "hdr", "avif", "heic"], {"default": "auto"}),
                "metadata_handling": (["preserve", "strip", "minimal", "custom"], {"default": "minimal"}),
                
                # Advanced Sizing
                "pixel_density_class": (["auto", "ldpi", "mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"], {"default": "auto"}),
                "viewport_scaling": (["none", "responsive", "adaptive", "fluid"], {"default": "none"}),
                "content_aware_crop": ("BOOLEAN", {"default": False}),
                "smart_resize": ("BOOLEAN", {"default": False}),
                
                # Print Specific
                "print_bleed": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.125}),
                "print_margin": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 2.0, "step": 0.125}),
                "print_safe_area": ("BOOLEAN", {"default": False}),
                "cmyk_conversion": ("BOOLEAN", {"default": False}),
                "icc_profile": ("BOOLEAN", {"default": False}),
                
                # Gaming and Interactive
                "texture_filtering": (["none", "bilinear", "trilinear", "anisotropic"], {"default": "none"}),
                "mipmap_generation": ("BOOLEAN", {"default": False}),
                "power_of_two": ("BOOLEAN", {"default": False}),
                "atlas_optimization": ("BOOLEAN", {"default": False}),
                
                # Video and Animation
                "frame_rate_consideration": (["none", "24fps", "30fps", "60fps", "120fps", "variable"], {"default": "none"}),
                "motion_blur_factor": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.1}),
                "temporal_optimization": ("BOOLEAN", {"default": False}),
                
                # AI and Machine Learning
                "model_architecture": (["none", "cnn", "transformer", "gan", "diffusion", "vae"], {"default": "none"}),
                "training_optimization": ("BOOLEAN", {"default": False}),
                "inference_optimization": ("BOOLEAN", {"default": False}),
                "batch_processing": ("BOOLEAN", {"default": False}),
                
                # Size Emphasis and Tags
                "size_emphasis": (["none", "low", "medium", "high", "very_high"], {"default": "medium"}),
                "add_size_tags": ("BOOLEAN", {"default": True}),
                "add_quality_tags": ("BOOLEAN", {"default": True}),
                "add_platform_tags": ("BOOLEAN", {"default": True}),
                "add_technical_tags": ("BOOLEAN", {"default": False}),
                "verbose_tagging": ("BOOLEAN", {"default": False}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "INT", "INT")
    RETURN_NAMES = ("enhanced_prompt", "size_summary", "optimal_width", "optimal_height")
    FUNCTION = "optimize_sizing"
    CATEGORY = "Camera Factory Station"
    
    def calculate_optimal_size(self, preset, custom_width, custom_height, aspect_ratio, maintain_aspect):
        """Calculate optimal width and height based on settings"""
        
        if preset == "custom":
            base_width = custom_width
            base_height = custom_height
            
            # Apply aspect ratio if specified
            if aspect_ratio != "auto" and maintain_aspect:
                if aspect_ratio in self.aspect_ratios:
                    target_ratio = self.aspect_ratios[aspect_ratio]["ratio"]
                    current_ratio = base_width / base_height
                    
                    if abs(current_ratio - target_ratio) > 0.01:  # If ratios don't match
                        # Adjust height to match ratio (keeping width)
                        base_height = int(base_width / target_ratio)
                else:
                    print(f"Warning: Aspect ratio '{aspect_ratio}' not found, maintaining original proportions")
        else:
            # Use preset dimensions
            if preset in self.platform_sizes:
                size_data = self.platform_sizes[preset]
                base_width = size_data["width"]
                base_height = size_data["height"]
            else:
                print(f"Warning: Platform size preset '{preset}' not found, using default 1024x1024")
                base_width = 1024
                base_height = 1024
        
        # Ensure dimensions are multiples of 8 (common requirement for AI models)
        optimal_width = (base_width // 8) * 8
        optimal_height = (base_height // 8) * 8
        
        return optimal_width, optimal_height
    
    def generate_size_tags(self, width, height, preset, quality_preset, platform_optimization):
        """Generate appropriate sizing and quality tags"""
        tags = []
        
        # Resolution category tags
        pixel_count = width * height
        if pixel_count >= 7680 * 4320:  # 8K+
            tags.extend(["8K_resolution", "ultra_high_definition", "maximum_detail"])
        elif pixel_count >= 3840 * 2160:  # 4K
            tags.extend(["4K_resolution", "ultra_high_definition", "crisp_detail"])
        elif pixel_count >= 2560 * 1440:  # QHD
            tags.extend(["QHD_resolution", "high_definition", "sharp_detail"])
        elif pixel_count >= 1920 * 1080:  # Full HD
            tags.extend(["full_HD", "1080p", "high_definition"])
        elif pixel_count >= 1280 * 720:   # HD
            tags.extend(["HD_resolution", "720p", "standard_definition"])
        else:
            tags.extend(["standard_resolution", "optimized_size"])
        
        # Aspect ratio tags
        ratio = width / height
        if abs(ratio - 1.0) < 0.1:
            tags.append("square_format")
        elif ratio > 2.0:
            tags.extend(["ultrawide", "panoramic", "cinematic_width"])
        elif ratio > 1.5:
            tags.extend(["widescreen", "landscape_format"])
        elif ratio > 1.0:
            tags.append("landscape_orientation")
        elif ratio < 0.7:
            tags.extend(["portrait_orientation", "vertical_format", "mobile_friendly"])
        else:
            tags.append("portrait_format")
        
        # Quality tags based on preset
        if quality_preset in self.quality_presets:
            quality_data = self.quality_presets[quality_preset]
            if quality_data["dpi"] >= 600:
                tags.extend(["premium_quality", "print_ready", "archival_grade"])
            elif quality_data["dpi"] >= 300:
                tags.extend(["print_quality", "professional_grade", "high_resolution"])
            elif quality_data["dpi"] >= 144:
                tags.extend(["retina_display", "high_DPI", "screen_optimized"])
            else:
                tags.extend(["web_optimized", "fast_loading"])
        else:
            print(f"Warning: Quality preset '{quality_preset}' not found, using standard quality tags")
            tags.extend(["standard_quality", "balanced_optimization"])
        
        # Platform-specific optimization
        if platform_optimization and preset != "custom":
            if "instagram" in preset:
                tags.extend(["instagram_optimized", "social_media_ready"])
            elif "print" in preset:
                tags.extend(["print_optimized", "CMYK_ready"])
            elif "product" in preset:
                tags.extend(["ecommerce_ready", "product_showcase"])
            elif any(x in preset for x in ["youtube", "website", "blog"]):
                tags.extend(["web_optimized", "digital_display"])
        
        return tags
    
    def apply_emphasis(self, tag, emphasis_level):
        """Apply emphasis brackets based on level"""
        if emphasis_level == "low":
            return f"({tag})"
        elif emphasis_level == "high":
            return f"(({tag}))"
        else:  # medium
            return tag
    
    def optimize_sizing(self, base_prompt, size_preset, optimization_target, **kwargs):
        """Main function to optimize sizing and add appropriate tags"""
        
        # Calculate optimal dimensions
        custom_width = kwargs.get("custom_width", 1024)
        custom_height = kwargs.get("custom_height", 1024)
        aspect_ratio = kwargs.get("aspect_ratio", "auto")
        maintain_aspect = kwargs.get("maintain_aspect", True)
        
        optimal_width, optimal_height = self.calculate_optimal_size(
            size_preset, custom_width, custom_height, aspect_ratio, maintain_aspect
        )
        
        # Generate size and quality tags
        quality_preset = kwargs.get("quality_preset", "web_high")
        platform_optimization = kwargs.get("platform_optimization", True)
        add_size_tags = kwargs.get("add_size_tags", True)
        
        size_tags = []
        if add_size_tags:
            size_tags = self.generate_size_tags(
                optimal_width, optimal_height, size_preset, quality_preset, platform_optimization
            )
        
        # Add optimization-specific tags
        optimization_tags = []
        if optimization_target == "quality":
            optimization_tags.extend(["maximum_quality", "detail_enhanced", "crisp"])
        elif optimization_target == "file_size":
            optimization_tags.extend(["size_optimized", "efficient", "compressed"])
        elif optimization_target == "performance":
            optimization_tags.extend(["performance_optimized", "fast_processing", "efficient_rendering"])
        else:  # balanced
            optimization_tags.extend(["balanced_quality", "optimized", "professional"])
        
        # Apply emphasis
        emphasis_level = kwargs.get("size_emphasis", "medium")
        emphasized_size_tags = [self.apply_emphasis(tag, emphasis_level) for tag in size_tags]
        emphasized_opt_tags = [self.apply_emphasis(tag, emphasis_level) for tag in optimization_tags]
        
        # Combine all tags
        all_tags = emphasized_size_tags + emphasized_opt_tags
        
        # Create enhanced prompt
        if all_tags:
            enhanced_prompt = f"{base_prompt}, {', '.join(all_tags)}"
        else:
            enhanced_prompt = base_prompt
        
        # Create detailed summary
        summary_parts = [
            f"📏 Size Optimization Applied:",
            f"• Dimensions: {optimal_width} x {optimal_height}",
            f"• Aspect Ratio: {optimal_width/optimal_height:.3f}:1",
        ]
        
        if size_preset != "custom":
            if size_preset in self.platform_sizes:
                preset_info = self.platform_sizes[size_preset]
                summary_parts.append(f"• Platform: {preset_info['description']}")
                summary_parts.append(f"• Standard Ratio: {preset_info['ratio']}")
            else:
                summary_parts.append(f"• Platform: {size_preset} (preset not found)")
        
        if quality_preset in self.quality_presets:
            quality_info = self.quality_presets[quality_preset]
            summary_parts.extend([
                f"• Quality: {quality_info['description']} ({quality_info['dpi']} DPI)",
                f"• Optimization: {optimization_target}",
            ])
        else:
            summary_parts.extend([
                f"• Quality: {quality_preset} (preset not found)",
                f"• Optimization: {optimization_target}",
            ])
        
        if emphasis_level != "medium":
            summary_parts.append(f"• Emphasis: {emphasis_level}")
        
        if all_tags:
            summary_parts.append(f"• Tags Added: {len(all_tags)}")
        
        size_summary = "\n".join(summary_parts)
        
        return (enhanced_prompt, size_summary, optimal_width, optimal_height)
