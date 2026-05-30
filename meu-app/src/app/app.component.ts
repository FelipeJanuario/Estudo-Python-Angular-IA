import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Meu App Angular';
  contador = 0;

  incrementar() {
    this.contador++;
  }

  resetar() {
    this.contador = 0;
  }
}
