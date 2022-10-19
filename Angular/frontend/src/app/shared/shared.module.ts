import { AppComponent } from '../app.component';

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { GoogleMapsModule } from '@angular/google-maps';

import { FormsModule } from '@angular/forms';
import { HomeComponent } from './components/home/home.component';

@NgModule({
  declarations: [HomeComponent],
  imports: [BrowserModule, HttpClientModule, FormsModule, GoogleMapsModule],
  exports: [HomeComponent],
  providers: [],
  bootstrap: [AppComponent],
})
export class SharedModule {}
