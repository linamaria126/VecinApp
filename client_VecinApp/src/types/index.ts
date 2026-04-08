export interface User {
  id: string;
  email: string;
  name: string;
  role: 'admin' | 'residente';
  unidadId?: string;
}

export interface Reserva {
  id: string;
  zonaId: string;
  fecha: Date;
  horaInicio: string;
  horaFin: string;
  usuarioId: string;
}

export interface Publicacion {
  id: string;
  titulo: string;
  contenido: string;
  autorId: string;
  createdAt: Date;
  likes: number;
}

export interface Unidad {
  id: string;
  numero: string;
  torre: string;
}

export interface ZonaSocial {
  id: string;
  nombre: string;
  descripcion: string;
  capacidad: number;
}