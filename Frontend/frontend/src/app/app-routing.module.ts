import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ErrorComponent } from './error/error.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { RegisterComponent } from './register/register.component';
import { WelcomeComponent } from './welcome/welcome.component';

const routes: Routes = [  
  {path:'',component: LoginComponent},
  {path:'login',component: LoginComponent},
  {path:'welcome/:name',component: WelcomeComponent},
  {path:'logout',component: LogoutComponent},
  {path:'register',component: RegisterComponent},
  {path:'**',component: ErrorComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
