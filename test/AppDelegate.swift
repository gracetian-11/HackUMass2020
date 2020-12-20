//
//  AppDelegate.swift
//  test
//
//  Created by kerry lu on 12/17/20.
//

import UIKit
import GoogleSignIn

@main
class AppDelegate: UIResponder, UIApplicationDelegate, GIDSignInDelegate {
    var window: UIWindow?
    
    func sign(_ signIn: GIDSignIn!, didSignInFor user: GIDGoogleUser!,
              withError error: Error!) {
    if (error == nil) {
        print("Signed in!")
    }
    else if let error = error {
        if (error as NSError).code == GIDSignInErrorCode.hasNoAuthInKeychain.rawValue {
          print("The user has not signed in before or they have since signed out.")
        } else {
          print("\(error.localizedDescription)")
        }
    return
    }
    // Perform any operations on signed in user here.
    let userId = user.userID                  // For client-side use only!
    let idToken = user.authentication.idToken // Safe to send to the server
    let fullName = user.profile.name
    let givenName = user.profile.givenName
    let familyName = user.profile.familyName
    let email = user.profile.email
    // ...
    }
    func sign(_ signIn: GIDSignIn!, didDisconnectWith user: GIDGoogleUser!,
              withError error: Error!) {
      // Perform any operations when the user disconnects from app here.
    NotificationCenter.default.post(
        name: NSNotification.Name(rawValue: "ToggleAuthUINotification"),
        object: nil,
        userInfo: ["statusText": "User has disconnected."])
    }
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        // Initialize sign-in
        GIDSignIn.sharedInstance().clientID = "251887149747-1u3p4djlpl976d48cphlqspd2en1omcs.apps.googleusercontent.com"
        GIDSignIn.sharedInstance().delegate = self
        /* check for user's token */
        if GIDSignIn.sharedInstance().hasPreviousSignIn() {
            /* Code to show your tab bar controller */
            print("user is signed in")
            let sb = UIStoryboard(name: "Main", bundle: nil)
            if let vc = sb.instantiateViewController(withIdentifier: "ViewController") as? ViewController {
                window!.rootViewController = vc
            }
        } else {
            print("user is NOT signed in")
            /* code to show your login VC */
            let sb = UIStoryboard(name: "LoginScreen", bundle: nil)
            if let vc = sb.instantiateViewController(withIdentifier: "LoginViewController") as? LoginViewController {
                window!.rootViewController = vc
            }
        }
    return true
    }
    
    @available(iOS 9.0, *)
    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any]) -> Bool {
      return GIDSignIn.sharedInstance().handle(url)
    }
    func application(_ application: UIApplication,
                     open url: URL, sourceApplication: String?, annotation: Any) -> Bool {
      return GIDSignIn.sharedInstance().handle(url)
    }

    // MARK: UISceneSession Lifecycle

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }
    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
    }
}

