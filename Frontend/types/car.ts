export interface Car {
  id: number;
  brand: string;
  model: string;
  price: number;
  images: string[];
  speed: string;
  acceleration: string;
  fuel: "Gasolina" | "Eletrico" | "Hibrido";
  transmission: "Auto" | "Manual";
  horsepower: string;
  seats: number;
}
