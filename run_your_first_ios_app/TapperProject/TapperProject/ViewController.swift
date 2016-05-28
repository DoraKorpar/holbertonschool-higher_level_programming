//
//  ViewController.swift
//  TapperProject
//
//  Created by Dora Korpar on 5/26/16.
//  Copyright © 2016 Dora Korpar. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    
    var taps_done = 0
    var taps_requested:Int? = 0
    
    @IBAction func clickPlayButton(sender: AnyObject) {
        if self.textfield_number.text != "" {
            self.taps_requested = Int(self.textfield_number.text!)
            print("Let's do \(taps_requested) taps")
            
            if self.taps_requested != nil && self.taps_requested > 0 {
                initGame()
            }
        }
    }
    
    @IBAction func clickCoinButton(sender: AnyObject) {
        self.taps_done += 1
        if self.taps_done < self.taps_requested {
            self.label_taps.text = "\(taps_done) TAPS!"
        }
        if self.taps_done == self.taps_requested {
            self.label_taps.text = "YOU WIN"
        }
        if self.taps_done > self.taps_requested {
            resetGame()
        }
    }
    
    func initGame() -> Void {
        self.button_coin.hidden = false
        self.label_taps.hidden = false
        self.image_tapper.hidden = true
        self.button_play.hidden = true
        self.textfield_number.hidden = true
        self.label_taps.text = "0 TAPS!"
    }
    
    func resetGame() -> Void {
        self.label_taps.hidden = true
        self.button_coin.hidden = true
        self.image_tapper.hidden = false
        self.button_play.hidden = false
        self.textfield_number.hidden = false
        self.taps_requested = 0
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    

}

