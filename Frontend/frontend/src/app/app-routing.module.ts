import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component'
import { ErrorComponent } from './error/error.component';
import { LoginComponent } from './login/login.component';
import { LogoutComponent } from './logout/logout.component';
import { RegisterComponent } from './register/register.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { TransactionComponent } from './transaction/transaction.component';

const routes: Routes = [  
  {path:'',component: LoginComponent},
  {path:'login',component: LoginComponent},
  {path:'welcome/:name',component: WelcomeComponent},
  {path:'logout',component: LogoutComponent},
  {path:'register',component: RegisterComponent},
  {path:'home', component: HomeComponent},
  {path:'trans', component: TransactionComponent},
  {path:'**',component: ErrorComponent}];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
