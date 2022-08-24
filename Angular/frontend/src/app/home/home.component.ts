import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { ApiService } from '../api.service';
import { Fires } from '../fires';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  fires$: Observable<Fires[]>;
  
  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getFires();
  }

  public getFires() {
    this.fires$ = this.apiService.getFires();
  }

}