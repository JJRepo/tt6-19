import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TransDataService } from '../service/data/transDataservice';


export class Transaction{
  constructor(
    public id:number,
    public description:string,
    public currency:string,
    public value:number,
    public targetDate:Date
  ){

  }
}

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})
export class TransactionComponent implements OnInit {

 // transactions: Transaction[] = [];

  transactions = [
    new Transaction(1,'Transaction 1 ','SGD',100,new Date()),
    new Transaction(2,'Transaction 2 ','CAD',20,new Date()),
  ]
  message!: string;
 
  constructor(
    private transService:TransDataService,
    private router:Router
  ) { }

  ngOnInit(): void {
  }

  refreshTransaction(){
    this.transService.retrieveAllTrans('sky').subscribe(
      response => {
        this.transactions = response;
      }
    )
  }

  deleteTransaction(id: any){
    this.transService.deleteTrans('sky',id).subscribe(
      response=>{
        this.message = `Delete of ${id} is successfull!`;
        this.refreshTransaction();

      }
    )
  }
  updateTransaction(id: any){
    this.router.navigate(['transactions',id])

  }
  addTransaction(){
    this.router.navigate(['transactions',-1])
  }

}
