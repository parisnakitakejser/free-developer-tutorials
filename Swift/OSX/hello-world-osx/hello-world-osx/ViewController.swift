//
//  ViewController.swift
//  hello-world-osx
//
//  Created by Paris Nakita Kejser on 24/07/15.
//  Copyright © 2015 Paris Nakita Kejser. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    @IBOutlet weak var lblHelloWorld: NSTextField!
    @IBOutlet weak var textFieldHelloWorld: NSTextField!
    
    @IBAction func actionPush(sender: AnyObject) {
        lblHelloWorld.stringValue = "Hello! " + textFieldHelloWorld.stringValue
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: AnyObject? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

