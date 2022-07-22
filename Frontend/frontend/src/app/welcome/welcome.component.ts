import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {

  message = 'Some Welcome Message'
  welcomeMessageFromService!: string;
  name = ''
  
  constructor() { }

  ngOnInit(): void {
  }

  getWelcomeMessage() {
    
    console.log('last line of getWelcomeMessage')

    //console.log("get welcome message");
  }

}
