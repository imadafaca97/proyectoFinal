import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import Card from '../interfaces/card';
import { MatDialog } from '@angular/material/dialog';
import { ModalComponent } from './modal/modal.component'; 
import { NgIf } from '@angular/common';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MatButtonModule, MatDividerModule, MatIconModule, MatCardModule, ModalComponent, NgIf],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  public cardToEdit!: Card;
  public card!: Card[]; 
  title = 'ProyectoFinal';

  constructor(public dialog: MatDialog) {
    this.card = [
      {
        title: "Primer título",
        subtitle: "Primer subtítulo",
        status: "inProgress",
        description: "Descripción del primer elemento"
      },
      {
        title: "Segundo título",
        subtitle: "Segundo subtítulo",
        status: "toDo",
        description: "Descripción del segundo elemento"
      },
      {
        title: "Tercer título",
        subtitle: "Tercer subtítulo",
        status: "done",
        description: "Descripción del tercer elemento"
      }
    ]
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(ModalComponent, {
      data: {} as Card,
    });

    dialogRef.afterClosed().subscribe((result: Card) => {
      if(result){
        result.status = 'toDo'
        this.card.push(result)
      }
    });
  }
  openEditDialog(index: number): void {
    const dialogRef = this.dialog.open(ModalComponent, {
      width: '500px',
      data: this.card[index] // Pasar los datos del elemento que se va a editar
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) { // Verificar si se recibió algún resultado
        // Actualizar el elemento editado en la matriz 'card'
        this.card[index] = result;
      }
    });
  }

  deleteTask(index: number): void {
    this.card.splice(index, 1); // Elimina el elemento en la posición 'index'
  }

  changeStatus(index: number, status: string): void {
    this.card[index].status = status
  }
}
