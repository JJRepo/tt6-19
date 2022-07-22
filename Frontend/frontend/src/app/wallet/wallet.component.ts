import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { walletData } from '../service/data/walletData';

interface Wallet {
  id: number,
  userid: number,
  name: string
}

@Component({
  selector: 'app-wallet',
  templateUrl: './wallet.component.html',
  styleUrls: ['./wallet.component.css']
})
export class WalletComponent implements OnInit {

  wallet: Wallet[] = [];
  message!: string;

  dummyData = [{
    "id": 1,
    "user_id": 1,
    "name": "Multi-Currency Account"
  },
  {
    "id": 2,
    "user_id": 1,
    "name": "Travel Account"
  },
  {
    "id": 3,
    "user_id": 2,
    "name": "Trading Account"
  },
  {
    "id": 4,
    "user_id": 3,
    "name": "Multi-Currency Account"
  },
  {
    "id": 5,
    "user_id": 4,
    "name": "Trip to Japan"
  }]

  constructor(
    // private walletService = walletData,
    // private router:Router
  ) { }

  ngOnInit(): void {
  }

  // deleteWallet(id: any){
  //   this.walletService.retrieveWalletData('sky',id).subscribe(res => {
        
  //     }
  //   )
  // }
}
