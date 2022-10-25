import { LocalData } from './../interfaces/local-data';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_URL = 'http://localhost';

  constructor(private http: HttpClient) { }

  public getFires(lat:number, lng:number, raio:number, year:number, url:string): Observable<LocalData> {
    if(url) {
      return this.http.get<LocalData>(url);
    }
     else {
      return this.http.get<LocalData>(`${this.API_URL}/datafire/?lat=${lat}&lng=${lng}&ray=${raio}&year=${year}`);
    }
  }
}
