import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { HttpErrorHandler, HandleError } from './http-error-handler.service';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable()
export class BackendApiService implements OnInit {

  private handleError: HandleError;

  constructor(private http: HttpClient, httpErrorHandler: HttpErrorHandler) {
    this.handleError = httpErrorHandler.createHandleError('HeroesService');
  }

  ngOnInit(): void {
  }

  /* POST heroes whose name contains search term */
  examplePost(object: any): Observable<any> {
    return this.http.post<any>('/examples/postExample', JSON.stringify(object), httpOptions)
      .pipe(
        catchError(this.handleError('examplePost', object))
      );
  }

  /* GET heroes whose name contains search term */
  exampleGet(object: any): Observable<any> {
    return this.http.get<any>('/examples/getExample')
      .pipe(
        catchError(this.handleError('exampleGet', []))
      );
  }

}
