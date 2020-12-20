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
    // TODO: Pull var values from backend
    var d1 = 60.0
    var d2 = 60.0
    var d3 = 60.0
    var d4 = 60.0
    var d5 = 60.0
    
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
        
        var backend:[String:Double] = [:]
        
        let s1 = "Takeout"
        let s2 = "Healthy Food"
        let s3 = "Soft Drink"
        let s4 = "Water"
        let s5 = "Home Meals"
        
        backend[s1] = d1
        backend[s2] = d2
        backend[s3] = d3
        backend[s4] = d4
        backend[s5] = d5
        
        for (key, value) in backend {
            entries.append(PieChartDataEntry(value: (value), label: (key)))
        }
        
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
