import { Component, OnInit } from '@angular/core';
import { BackendApiService } from './backend-api/backend-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [BackendApiService],
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'front-end';

  constructor(private backend:BackendApiService) {
  }

  ngOnInit(): void {
  }

  getHeroes(): void {
    this.backend.exampleGet(["test"])
      .subscribe(response =>{
        console.log(response);
      });
  }
}
