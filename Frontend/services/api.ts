import { Car } from "../types/car";
import { Rental } from "../types/rental";

const API_BASE_URL = "http://192.168.3.51:8000"; // IP do seu backend FastAPI

export const getCars = async (): Promise<Car[]> => {
  const response = await fetch(`${API_BASE_URL}/cars`);
  if (!response.ok) {
    const errorText = await response.text();
    console.error("Erro ao buscar carros:", errorText);
    throw new Error(`Erro ao buscar carros: ${errorText || response.statusText}`);
  }
  const data = await response.json();
  return data.cars ?? data;
};

export const getCarById = async (carId: number): Promise<Car> => {
  console.log("Buscando carro com ID:", carId);

  const response = await fetch(`${API_BASE_URL}/cars/${carId}`);

  if (!response.ok) {
    const errorText = await response.text();
    console.error(`Erro ao buscar carro ${carId}:`, errorText);
    throw new Error(`Erro ao buscar carro: ${errorText || response.statusText}`);
  }

  const data: Car = await response.json();
  console.log("Carro encontrado:", data);

  return data;
};

export const getUserRentals = async (): Promise<Rental[]> => {
  const response = await fetch(`${API_BASE_URL}/rentals/user`);

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Erro ao buscar aluguéis:", errorText);
    throw new Error(`Erro ao buscar aluguéis: ${errorText || response.statusText}`);
  }

  const data = await response.json();
  return data.rentals ?? data;
};

export const deleteRentalById = async (rentalId: number): Promise<void> => {
  const response = await fetch(`${API_BASE_URL}/rentals/${rentalId}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Erro ao deletar aluguel:", errorText);
    throw new Error(`Erro ao deletar aluguel: ${errorText || response.statusText}`);
  }
};
