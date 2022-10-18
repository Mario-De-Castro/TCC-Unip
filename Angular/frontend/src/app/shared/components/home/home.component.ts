import { ApiService } from './../../services/api.service';

import { Fires } from './../../interfaces/fires';
import { LocalData } from './../../interfaces/local-data';

import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  @ViewChild('mapContainer', { static: false }) gmap: ElementRef;

  fires$: Observable<LocalData>;

  public map: google.maps.Map;
  public heatmap: google.maps.visualization.HeatmapLayer;
  public circle: google.maps.Circle;

  public mapOptions: google.maps.MapOptions;

  public allFires: Fires[];
  public latitude: number;
  public longitude: number;
  public heatMapData: google.maps.LatLng[];
  public heatMapOptions: {radius:number}
  public step:number;
  public raio:number;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.latitude = -23.533773;
    this.longitude = -46.625290;
    this.heatMapOptions = {radius: 5};
    this.heatMapData = [];
    this.step = 1;
    this.raio = 25;

    this.heatmap = new google.maps.visualization.HeatmapLayer({
      map: this.map,
      data: []
    });

    this.circle = new google.maps.Circle({
      strokeColor: "#FF0000",
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: "#FF0000",
      fillOpacity: 0.35
    })

    this.initMap();
  }

  initMap(): void {
    this.map = new google.maps.Map(document.getElementById("map") as HTMLElement, {
      zoom: 10,
      center: { lat: this.latitude, lng: this.longitude }
    });
  }

  updateHeatmap(): void {
    this.heatmap.setMap(this.map);
  }

  centralize() {
    if (!this.latitude || !this.longitude) {
      alert('Insira a latitude e longitude que deseja utilizar.');
      return;
    }
    this.map.setCenter(new google.maps.LatLng(this.latitude, this.longitude))
  }

  nextStep() {
    this.step += 1;
    if(this.step == 2) {
      this.updateCircle();
    } else if(this.step != 2) {
      this.removeCircle()
    }
  }

  updateCircle() {
    this.circle.setCenter(new google.maps.LatLng(this.latitude, this.longitude));
    this.circle.setRadius(this.raio * 1000);
    this.circle.setMap(this.map)
  }

  removeCircle() {
    this.circle.setMap(null)
  }

  getFires() {
    this.apiService
      .getFires(this.latitude, this.longitude, this.raio)
      .subscribe((json) => {
        this.allFires = json.results;
        json.results.forEach(elem => {
          this.heatMapData.push(new google.maps.LatLng(elem.latitude, elem.longitude))
        });
        this.heatmap.setData(this.heatMapData);
        this.updateHeatmap();
      });
  }
}
