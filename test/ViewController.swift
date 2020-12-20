//
//  ViewController.swift
//  test
//
//  Created by kerry lu on 12/17/20.
//

import UIKit
import Charts

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    //MARK: Properties
    @IBOutlet weak var photoImageView: UIImageView!
    @IBOutlet weak var header: UILabel!
    @IBOutlet weak var pieView: PieChartView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        header.text = "Welcome Back!"
        setupPieChart()
        
        // Enable UITapGestureRecognizer on image
        photoImageView.isUserInteractionEnabled = true
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(selectImageFromPhotoLibrary(_:)))
        tapGestureRecognizer.numberOfTapsRequired = 1
        photoImageView.addGestureRecognizer(tapGestureRecognizer)
    }
    
    //MARK: UIImagePickerControllerDelegate
    // called when a user taps the image picker’s Cancel button
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        // Dismiss the picker if the user canceled.
        dismiss(animated: true, completion: nil)
    }
    // called when a user selects a photo
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
        // The info dictionary may contain multiple representations of the image. You want to use the original.
        guard let selectedImage = info[UIImagePickerController.InfoKey.originalImage] as? UIImage else {
            fatalError("Expected a dictionary containing an image, but was provided the following: \(info)")
        }
        // Set photoImageView to display the selected image.
        photoImageView.image = selectedImage
        // Dismiss the picker.
        dismiss(animated: true, completion: nil)
    }
    
    //MARK: Actions
    func setupPieChart() {
        pieView.chartDescription?.enabled = false   // Sets title = false
        pieView.drawHoleEnabled = false // true if donut chart, false if pie chart
        pieView.rotationAngle = 0
        pieView.rotationEnabled = false
        pieView.isUserInteractionEnabled = false    // true allows users to see more detailed information upon tapping
        pieView.legend.enabled = false // true enables legend
        
        var entries: [PieChartDataEntry] = Array()
        entries.append(PieChartDataEntry(value: 50.0, label: "Takeout"))   // value = angle
        entries.append(PieChartDataEntry(value: 30.0, label: "Healthy Food"))
        entries.append(PieChartDataEntry(value: 20.0, label: "Soft Drink"))
        entries.append(PieChartDataEntry(value: 10.0, label: "Water"))
        entries.append(PieChartDataEntry(value: 40.0, label: "Home Meals"))
        
        let dataSet = PieChartDataSet(entries: entries, label: "")
                
        let c1 = NSUIColor(hex: 0x3A015C)   // purple
        let c2 = NSUIColor(hex: 0x4F0147)
        let c3 = NSUIColor(hex: 0x35012C)
        let c4 = NSUIColor(hex: 0x290025)
        let c5 = NSUIColor(hex: 0x11001C)
    
        dataSet.colors = [c1, c2, c3, c4, c5] // order passed in = order placed into entries array
        dataSet.drawValuesEnabled = false
        
        pieView.data = PieChartData(dataSet: dataSet)
    }
    // Segue into LoginViewController when Back button is pressed
    @IBAction func backButton(_ sender: Any) {
        performSegue(withIdentifier: "goToLoginScreen", sender: self)
    }
    
    @IBAction func submitButton(_ sender: UIButton) {
        // TODO: Show text saying "submitting"
        // TODO: Submit photo to backend
        print("in submitButton")    // For debugging
    }
    // Select an image from photo library when tapped
    @IBAction func selectImageFromPhotoLibrary(_ sender: UITapGestureRecognizer) {
        
        // UIImagePickerController is a view controller that lets a user pick media from their photo library.
        let imagePickerController = UIImagePickerController()
        // Only allow photos to be picked, not taken.
        imagePickerController.sourceType = .photoLibrary
        
        // Make sure ViewController is notified when the user picks an image.
        imagePickerController.delegate = self
        present(imagePickerController, animated: true, completion: nil)
    }
}

