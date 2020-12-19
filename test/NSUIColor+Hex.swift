//
//  NSUIColor+Hex.swift
//  test
//
//  Created by kerry lu on 12/19/20.
//

import Foundation
import Charts

// Allows usage of hex colors for NSUIColor parameters
extension NSUIColor {
    
    // Initialize color by passing in hex values for red, green, and blue individually
    convenience init(red: Int, green: Int, blue: Int) {
        assert(red >= 0 && red <= 255, "Invalid red component")
        assert(green >= 0 && green <= 255, "Invalid green component")
        assert(blue >= 0 && blue <= 255, "Invalid red component")
        
        self.init(red: CGFloat(red) / 255.0, green: CGFloat(green) / 255.0, blue: CGFloat(blue) / 255.0, alpha: 1.0)
    }
    
    // Initialize NSUIColor from hex value
    convenience init(hex: Int) {
        self.init(
            red: (hex >> 16) & 0xFF,
            green: (hex >> 8) & 0xFF,
            blue: hex & 0xFF
        )
    }
    
}
