# 🚀 Quick Start Guide - Camera Factory Station

## 📦 Installation

### Step 1: Download and Install
1. Copy the entire `Camera_Factory_Station` folder to your ComfyUI `custom_nodes` directory
2. Restart ComfyUI
3. Look for "Camera Factory Station" in your node menu

### Step 2: Verify Installation
- Check that all 5 nodes appear under "Camera Factory Station" category:
  - FactoryCameraOperator
  - FactoryColorHarmonist  
  - FactoryLightingStudio
  - FactoryProductPhotographer
  - FactorySizeOptimizer

## 🎬 Example Workflows

Load these example workflows to see the Camera Factory Station in action:

### 📄 Available Workflow Files:

1. **`example_workflow.json`** - Complete chain demonstrating all 5 nodes
2. **`portrait_workflow.json`** - Professional portrait/headshot workflow  
3. **`product_workflow.json`** - E-commerce product photography workflow
4. **`multi_platform_workflow.json`** - Social media multi-format workflow

### 🔄 How to Load Workflows:

1. Open ComfyUI
2. Click "Load" button
3. Navigate to the Camera Factory Station folder
4. Select any `.json` workflow file
5. Click "Load Default" to load the workflow

## ⚡ Quick Usage

### Basic Chain (Recommended):
```
Input Text → FactoryCameraOperator → FactoryColorHarmonist → FactorySizeOptimizer → CLIPTextEncode
```

### Professional Portrait:
```
Input Text → FactoryCameraOperator → FactoryLightingStudio → FactorySizeOptimizer → Generation
```

### Product Photography:
```
Input Text → FactoryCameraOperator → FactoryProductPhotographer → FactorySizeOptimizer → Generation
```

## 🎯 Common Settings

### For Portraits:
- **Camera Operator**: `photography_style="portrait"`, `shot_type="close_up"`
- **Lighting Studio**: `studio_setup="rembrandt_lighting"`
- **Size Optimizer**: `platform_preset="linkedin_profile"`

### For Products:
- **Camera Operator**: `photography_style="commercial"`, `shot_type="product_hero"`
- **Product Photographer**: `photography_style="amazon_optimized"`
- **Size Optimizer**: `platform_preset="amazon_main"`

### For Social Media:
- **Color Harmonist**: `color_theory="vibrant_energetic"`
- **Size Optimizer**: `platform_preset="instagram_square"`

## 🎨 Node Details

### 🎥 FactoryCameraOperator (267 options)
**Purpose**: Professional camera controls and shot composition
**Key Settings**: photography_style, shot_type, lens_type, camera_angle
**Best For**: Technical photography enhancement

### 🎨 FactoryColorHarmonist (150 options)  
**Purpose**: Color theory and cultural color palettes
**Key Settings**: color_theory, cultural_palette, professional_palette
**Best For**: Brand consistency and emotional impact

### 💡 FactoryLightingStudio (147 options)
**Purpose**: Professional lighting setup simulation
**Key Settings**: studio_setup, natural_lighting, equipment_type
**Best For**: Portrait and commercial lighting

### 📸 FactoryProductPhotographer (133 options)
**Purpose**: E-commerce and product photography optimization
**Key Settings**: photography_style, platform_optimization, product_category
**Best For**: Online sales and product marketing

### 📐 FactorySizeOptimizer (352 options)
**Purpose**: Platform-specific size and format optimization
**Key Settings**: platform_preset, quality_preset, aspect_ratio
**Best For**: Multi-platform content creation

## 🔧 Troubleshooting

### Node Not Appearing?
- Ensure folder is in `ComfyUI/custom_nodes/Camera_Factory_Station/`
- Restart ComfyUI completely
- Check console for any error messages

### Prompt Too Long?
- Lower emphasis levels (use "low" or "medium")
- Use fewer nodes in chain
- Enable "auto" settings for intelligent selection

### Quality Issues?
- Increase emphasis levels (use "high" or "very_high")
- Use "professional_print" quality preset
- Chain more nodes for comprehensive enhancement

## 📊 Performance Tips

### For Speed:
- Use individual nodes instead of full chain
- Select "auto" for most settings
- Use "draft_preview" quality preset

### For Quality:
- Use full 5-node chain
- Set emphasis to "high" or "very_high"
- Use "professional_print" quality preset

### For Balance:
- Use 2-3 node chains
- Set emphasis to "medium"
- Use "high_quality" preset

## 🌟 Pro Tips

1. **Start Simple**: Begin with "auto" settings and adjust from there
2. **Context Matters**: The nodes analyze your prompt for intelligent suggestions
3. **Chain Wisely**: Order matters - Camera → Color → Lighting → Product → Size
4. **Platform First**: Always end with Size Optimizer for proper formatting
5. **Test Settings**: Use lower emphasis for testing, higher for final output

## 🎊 You're Ready!

The Camera Factory Station provides **1040+ professional options** for universal photography coverage. Start with the example workflows and customize from there!

**Happy creating!** 📸✨
