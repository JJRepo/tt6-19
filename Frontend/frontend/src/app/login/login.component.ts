import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HardcodedAuthenService } from '../service/hardcodedAuthenService';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username = 'sky'
  password = ''
  errorMessage = 'Invalid Credentials'
  invalidLogin = false

  constructor(
    private router: Router,
    private hardcodedAuthenService:HardcodedAuthenService,
    ) { }

  ngOnInit(): void {
  }
  handleLogin(){
    if(this.hardcodedAuthenService.authenticate(this.username,this.password)){
      console.log(sessionStorage.getItem('authenticaterUser'))
      this.router.navigate(['welcome',this.username])
      this.invalidLogin = false;
    }else{
      this.invalidLogin = true;
    }
  }
}
