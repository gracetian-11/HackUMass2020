//
//  LoginViewController.swift
//  test
//
//  Created by kerry lu on 12/18/20.
//

import UIKit

class LoginViewController: UIViewController, UIViewControllerTransitioningDelegate {
    // MARK: Properties
    @IBOutlet weak var emailAddress: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
        
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    // Segue into ViewController when continue button is pressed
    @IBAction func continueButton(_ sender: UIButton) {
        performSegue(withIdentifier: "goToMainStoryboard", sender: self)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "goToMainStoryboard" {
            guard let destinationVC = segue.destination as? ViewController else { return }
            destinationVC.userName = "Welcome Back, " + emailAddress.text!
        }
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
