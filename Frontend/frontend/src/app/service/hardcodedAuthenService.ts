import { Injectable } from '@angular/core';
import { ApiService } from '../api/api.service';

@Injectable({
  providedIn: 'root'
})
export class HardcodedAuthenService {

  constructor(private apiservice:ApiService) { }
  authenticate(username: string,password: string){
    //console.log('before'+this.isUserLoggedIn);
      this.apiservice.postAPI("http://127.0.0.1:5000/login",[username,password]).subscribe((data: any) => {
        if(data["message"] == "success"){
          sessionStorage.setItem('authenticaterUser',data["username"]);
          sessionStorage.setItem('authenticaterUserID',data["id"]);
          sessionStorage.setItem('authenticaterUserName',data["name"]);
        }
    });
      return true;
  }
  isUserLoggedIn(){
    let user = sessionStorage.getItem('authenticaterUser')

    return !(user===null)
  }
  logout(){
    sessionStorage.removeItem('authenticaterUser')
  }
}
