
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { API_URL } from 'src/app/app.constant';
import { Transaction } from 'src/app/transaction/transaction.component';

@Injectable({
  providedIn: 'root'
})
export class TransDataService {

  constructor(
    private http:HttpClient
  ) { }

  retrieveAllTrans(username: string) {
    return this.http.get<Transaction[]>(`${API_URL}/users/${username}/trans`);
    //console.log("Execute Hello World Bean Service")
  }

  deleteTrans(username: string, id: any){
    return this.http.delete(`${API_URL}/users/${username}/trans/${id}`);
  }

  retrieveTrans(username: string, id: number){
    return this.http.get<Transaction>(`${API_URL}/users/${username}/trans/${id}`);
  }

  updateTrans(username: string, id: number, transaction: Transaction){
    return this.http.put(
          `${API_URL}/users/${username}/trans/${id}`
                , transaction);
  }

  createTodo(username: string, transaction: Transaction){
    return this.http.post(
              `${API_URL}/users/${username}/trans`
                , transaction);
  }

}