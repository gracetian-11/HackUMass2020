//
//  LoginViewController.swift
//  test
//
//  Created by kerry lu on 12/18/20.
//

import UIKit
import GoogleSignIn

class LoginViewController: UIViewController, UIViewControllerTransitioningDelegate {
    // MARK: Properties
    
    override func viewDidLoad() {
        super.viewDidLoad()
        GIDSignIn.sharedInstance()?.presentingViewController = self
        GIDSignIn.sharedInstance()?.restorePreviousSignIn()
    }
    @IBAction func didTapSignOut(sender: AnyObject) {
            GIDSignIn.sharedInstance().signOut()
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    func signInWillDispatch(signIn: GIDSignIn!, error: NSError!) {
            print("Nothing!")
    }
    // Present a view that prompts the user to sign in with Google
    func signIn(signIn: GIDSignIn!,
        presentViewController viewController: UIViewController!) {
        self.present(viewController, animated: true, completion: nil)
    }

    // Dismiss the "Sign in with Google" view
    func signIn(signIn: GIDSignIn!,
        dismissViewController viewController: UIViewController!) {
        self.dismiss(animated: true, completion: nil)
    }
    // Segue into ViewController when continue button is pressed
    @IBAction func continueButton(_ sender: Any) {
        performSegue(withIdentifier: "goToMainStoryboard", sender: self)
    }
}
