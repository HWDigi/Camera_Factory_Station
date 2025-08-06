#!/usr/bin/env python3

"""
Camera Factory Station - Professional Photography & Visual Enhancement Suite
A comprehensive ComfyUI node collection for advanced camera, lighting, color, and product photography controls.

SFW Edition - GitHub Compliant - Professional Grade
"""

import sys

# ANSI color codes for terminal output
class Colors:
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

# Startup message
def print_startup_message():
    """Display the Production Imaging Bay startup message in yellow."""
    banner = f"{Colors.YELLOW}{Colors.BOLD}┌─────────────────────────────────────────┐{Colors.END}"
    message = f"{Colors.YELLOW}{Colors.BOLD}│    Production Imaging Bay is Online    │{Colors.END}"
    footer = f"{Colors.YELLOW}{Colors.BOLD}└─────────────────────────────────────────┘{Colors.END}"
    info = f"{Colors.YELLOW}[Camera Factory Station] 1040+ professional options loaded{Colors.END}"
    
    print(banner)
    print(message)
    print(footer)
    print(info)
    sys.stdout.flush()

# Print startup message when module is imported
print_startup_message()

from .factory_camera_operator import FactoryCameraOperator
from .factory_size_optimizer import FactorySizeOptimizer  
from .factory_color_harmonist import FactoryColorHarmonist
from .factory_lighting_studio import FactoryLightingStudio
from .factory_product_photographer import FactoryProductPhotographer

# Node registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "FactoryCameraOperator": FactoryCameraOperator,
    "FactorySizeOptimizer": FactorySizeOptimizer,
    "FactoryColorHarmonist": FactoryColorHarmonist,
    "FactoryLightingStudio": FactoryLightingStudio,
    "FactoryProductPhotographer": FactoryProductPhotographer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FactoryCameraOperator": "📸 Camera Operator",
    "FactorySizeOptimizer": "📏 Size Optimizer", 
    "FactoryColorHarmonist": "🎨 Color Harmonist",
    "FactoryLightingStudio": "💡 Lighting Studio",
    "FactoryProductPhotographer": "🛍️ Product Photographer",
}

__all__ = [
    "FactoryCameraOperator",
    "FactorySizeOptimizer", 
    "FactoryColorHarmonist",
    "FactoryLightingStudio", 
    "FactoryProductPhotographer"
]
