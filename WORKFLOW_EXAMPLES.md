# 🎬 Camera Factory Station - Example Workflows

This document provides comprehensive examples of how to use the Camera Factory Station nodes in ComfyUI workflows for various photography scenarios.

## 📋 Table of Contents

1. [Basic Chain Workflow](#basic-chain-workflow)
2. [Portrait Photography Workflow](#portrait-photography-workflow)
3. [Product Photography Workflow](#product-photography-workflow)
4. [Social Media Content Workflow](#social-media-content-workflow)
5. [Commercial Photography Workflow](#commercial-photography-workflow)
6. [Multi-Platform Campaign Workflow](#multi-platform-campaign-workflow)

---

## 🎯 Basic Chain Workflow

**File**: `example_workflow.json`

### Description
The complete Camera Factory Station chain demonstrating all 5 nodes working together to transform a basic prompt into a professional photography setup.

### Flow:
```
Base Prompt → Camera Operator → Color Harmonist → Lighting Studio → Product Photographer → Size Optimizer → Image Generation
```

### Settings Used:
- **Camera Operator**: Professional portrait, medium close-up, high-end quality
- **Color Harmonist**: Complementary colors, Scandinavian hygge palette
- **Lighting Studio**: Rembrandt lighting with golden hour ambiance
- **Product Photographer**: Lifestyle natural style for fashion
- **Size Optimizer**: Instagram square format optimization

### Expected Result:
A professionally enhanced prompt optimized for Instagram with sophisticated lighting, color harmony, and commercial-grade camera settings.

---

## 👤 Portrait Photography Workflow

### Use Case: Professional Headshots and Portraits

```json
{
  "camera_operator": {
    "photography_style": "portrait",
    "shot_type": "close_up",
    "lens_type": "portrait",
    "aperture": "portrait_bokeh",
    "camera_angle": "beauty_angle",
    "lighting_style": "beauty_light"
  },
  "color_harmonist": {
    "color_theory": "monochromatic",
    "cultural_palette": "timeless_classic",
    "professional_palette": "corporate_professional"
  },
  "lighting_studio": {
    "studio_setup": "butterfly_lighting",
    "equipment_type": "beauty_dish",
    "atmospheric_effect": "soft_glamour"
  },
  "size_optimizer": {
    "platform_preset": "linkedin_profile",
    "quality_preset": "professional_print"
  }
}
```

**Best For**: LinkedIn profiles, corporate headshots, professional portfolios

---

## 📦 Product Photography Workflow

### Use Case: E-commerce Product Listings

```json
{
  "camera_operator": {
    "photography_style": "commercial",
    "shot_type": "product_shot",
    "lens_type": "macro",
    "aperture": "product_photography",
    "camera_angle": "three_quarter",
    "lighting_style": "studio"
  },
  "color_harmonist": {
    "color_theory": "neutral_palette",
    "professional_palette": "clean_minimal"
  },
  "lighting_studio": {
    "studio_setup": "product_table",
    "equipment_type": "softbox_large",
    "atmospheric_effect": "clean_commercial"
  },
  "product_photographer": {
    "photography_style": "amazon_optimized",
    "platform_optimization": "marketplace_standard",
    "product_category": "electronics_tech",
    "brand_positioning": "innovative_tech"
  },
  "size_optimizer": {
    "platform_preset": "amazon_main",
    "quality_preset": "e_commerce_standard"
  }
}
```

**Best For**: Amazon listings, Shopify stores, product catalogs

---

## 📱 Social Media Content Workflow

### Use Case: Instagram, TikTok, Social Platforms

```json
{
  "camera_operator": {
    "photography_style": "lifestyle",
    "shot_type": "medium_wide",
    "lens_type": "wide_angle",
    "camera_angle": "slight_high",
    "lighting_style": "natural"
  },
  "color_harmonist": {
    "color_theory": "vibrant_energetic",
    "cultural_palette": "mediterranean_warm",
    "professional_palette": "social_media_bright"
  },
  "lighting_studio": {
    "studio_setup": "natural_window",
    "natural_lighting": "golden_hour",
    "atmospheric_effect": "bright_cheerful"
  },
  "product_photographer": {
    "photography_style": "lifestyle_natural",
    "platform_optimization": "social_media_optimized"
  },
  "size_optimizer": {
    "platform_preset": "instagram_story",
    "quality_preset": "social_media_optimized"
  }
}
```

**Best For**: Instagram posts, TikTok content, Facebook ads, social campaigns

---

## 🏢 Commercial Photography Workflow

### Use Case: High-End Commercial and Advertising

```json
{
  "camera_operator": {
    "photography_style": "cinematic",
    "shot_type": "dramatic_wide",
    "lens_type": "anamorphic_cinema",
    "aperture": "cinematic_depth",
    "camera_angle": "dramatic_low",
    "lighting_style": "dramatic"
  },
  "color_harmonist": {
    "color_theory": "split_complementary",
    "professional_palette": "luxury_premium",
    "industry_palette": "entertainment_media"
  },
  "lighting_studio": {
    "studio_setup": "commercial_hero",
    "equipment_type": "hmi_fresnel",
    "atmospheric_effect": "cinematic_dramatic"
  },
  "product_photographer": {
    "photography_style": "luxury_editorial",
    "brand_positioning": "luxury_premium"
  },
  "size_optimizer": {
    "platform_preset": "print_billboard",
    "quality_preset": "professional_print"
  }
}
```

**Best For**: Magazine ads, billboards, luxury brand campaigns, commercial photography

---

## 🌐 Multi-Platform Campaign Workflow

### Use Case: Creating Multiple Versions for Different Platforms

This workflow demonstrates how to create multiple outputs from one base setup by varying the Size Optimizer settings:

### Base Setup (Shared):
```json
{
  "camera_operator": {
    "photography_style": "professional",
    "shot_type": "medium_shot",
    "lens_type": "standard",
    "camera_angle": "eye_level"
  },
  "color_harmonist": {
    "color_theory": "complementary",
    "professional_palette": "brand_consistent"
  },
  "lighting_studio": {
    "studio_setup": "three_point_classic",
    "atmospheric_effect": "professional_clean"
  },
  "product_photographer": {
    "photography_style": "versatile_commercial"
  }
}
```

### Platform Variations (Size Optimizer):

**Instagram Feed**: `instagram_square` (1080x1080)
**Instagram Story**: `instagram_story` (1080x1920)
**Facebook Ad**: `facebook_ad` (1200x628)
**LinkedIn Post**: `linkedin_post` (1200x627)
**Pinterest Pin**: `pinterest_standard` (1000x1500)
**YouTube Thumbnail**: `youtube_thumbnail` (1280x720)
**Print Flyer**: `print_flyer_a4` (2480x3508)

---

## 🛠️ Workflow Customization Tips

### 1. **Context-Aware Selection**
Use "auto" settings to let the nodes intelligently select based on your base prompt context.

### 2. **Progressive Enhancement**
Start with basic settings and gradually increase complexity by chaining more nodes.

### 3. **Platform-Specific Optimization**
Always end with Size Optimizer to ensure proper formatting for your target platform.

### 4. **Emphasis Control**
Adjust emphasis levels (low/medium/high/very_high) to control how strongly effects are applied.

### 5. **Quality Presets**
Match quality presets to your intended use:
- `draft_preview` for quick tests
- `social_media_optimized` for online content
- `professional_print` for commercial use
- `high_end_commercial` for premium applications

---

## 📈 Performance Optimization

### Single Node Usage
For simple enhancements, use individual nodes:
- Camera Operator only for technical photography improvements
- Color Harmonist only for color correction
- Size Optimizer only for format conversion

### Selective Chaining
Choose 2-3 nodes based on your primary need:
- **Portrait Focus**: Camera Operator → Lighting Studio → Size Optimizer
- **Product Focus**: Camera Operator → Product Photographer → Size Optimizer  
- **Social Media Focus**: Color Harmonist → Size Optimizer

### Full Chain
Use all 5 nodes for maximum professional enhancement when quality is paramount.

---

## 🎯 Common Use Cases

| Use Case | Recommended Chain | Key Settings |
|----------|------------------|--------------|
| **LinkedIn Headshot** | Camera → Color → Lighting → Size | Portrait style, professional colors, corporate lighting |
| **Instagram Product** | Camera → Product → Size | Commercial style, product optimization, social format |
| **Print Advertisement** | All 5 Nodes | Cinematic style, premium colors, commercial lighting |
| **Social Media Story** | Color → Size | Vibrant colors, story format optimization |
| **E-commerce Listing** | Camera → Product → Size | Commercial style, marketplace optimization |

---

Ready to create professional-quality images with the Camera Factory Station! 📸✨
