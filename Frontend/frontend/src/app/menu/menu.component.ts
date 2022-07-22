import { Component, OnInit } from '@angular/core';
import { HardcodedAuthenService } from '../service/hardcodedAuthenService';


@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  isUserLogIn: boolean = false;
  constructor(public  hardcodedAuthenService:HardcodedAuthenService) { }

  ngOnInit(): void {
    this.isUserLogIn = this.hardcodedAuthenService.isUserLoggedIn();
  }

}
