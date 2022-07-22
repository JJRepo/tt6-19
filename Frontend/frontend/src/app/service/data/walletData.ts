import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { API_URL } from 'src/app/app.constant';
import { WalletComponent } from 'src/app/wallet/wallet.component';


@Injectable({
    providedIn: 'root'
})

export class walletData {
    constructor(
        private http:HttpClient
    ) { }

    retrieveWalletData(id: number) {
        return this.http.get<WalletComponent[]>(`${API_URL}/users/${id}/wallets`);
    }


}