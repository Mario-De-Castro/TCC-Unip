import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Fires } from './fires';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  API_URL = 'http://localhost:80';

  constructor(private http: HttpClient) { }

  public getFires(): Observable<Fires[]> {
    return this.http.get<Fires[]>(`${this.API_URL}/fires/`);
  }
}
