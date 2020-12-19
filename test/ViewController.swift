//
//  ViewController.swift
//  test
//
//  Created by kerry lu on 12/17/20.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    //MARK: Properties
    let pieChartView = PieChartView()
    @IBOutlet weak var photoImageView: UIImageView!
    @IBOutlet weak var header: UILabel!
    var userName: String?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        header.text = userName
        
        let padding: CGFloat = 20
        let height = (view.frame.height - padding * 3) / 2

            pieChartView.frame = CGRect(
                x: 0, y: padding*22.5, width: view.frame.size.width, height: height
            )
            pieChartView.segments = [
              LabelledSegment(color: #colorLiteral(red: 1.0, green: 0.121568627, blue: 0.28627451, alpha: 1.0), name: "Red",        value: 57.56),
              LabelledSegment(color: #colorLiteral(red: 1.0, green: 0.541176471, blue: 0.0, alpha: 1.0), name: "Orange",     value: 30),
              LabelledSegment(color: #colorLiteral(red: 0.478431373, green: 0.423529412, blue: 1.0, alpha: 1.0), name: "Purple",     value: 27),
              LabelledSegment(color: #colorLiteral(red: 0.0, green: 0.870588235, blue: 1.0, alpha: 1.0), name: "Light Blue", value: 40),
              LabelledSegment(color: #colorLiteral(red: 0.392156863, green: 0.945098039, blue: 0.717647059, alpha: 1.0), name: "Green",      value: 25),
              LabelledSegment(color: #colorLiteral(red: 0.0, green: 0.392156863, blue: 1.0, alpha: 1.0), name: "Blue",       value: 38)
            ]
            pieChartView.segmentLabelFont = .systemFont(ofSize: 10)
            view.addSubview(pieChartView)
        
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

