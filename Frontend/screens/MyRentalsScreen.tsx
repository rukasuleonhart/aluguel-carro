import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  ScrollView,
  Pressable,
  Image,
  ActivityIndicator,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { SafeAreaView } from "react-native-safe-area-context";
import { getUserRentals, deleteRentalById } from "../services/api";
import { Rental } from "../types/rental";

const MyRentalsScreen = () => {
  const [rentals, setRentals] = useState<Rental[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRentals = async () => {
      try {
        const data = await getUserRentals(); // <- função da API
        setRentals(data);
      } catch (error) {
        console.error("Erro ao buscar aluguéis:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchRentals();
  }, []);

  const handleRemove = async (rentalId: number) => {
    try {
      await deleteRentalById(rentalId); // <- função da API
      setRentals((prev) => prev.filter((r) => r.id !== rentalId));
    } catch (error) {
      console.error("Erro ao remover aluguel:", error);
    }
  };

  if (loading) {
    return (
      <SafeAreaView className="flex-1 justify-center items-center bg-white">
        <ActivityIndicator size="large" color="#DC1637" />
      </SafeAreaView>
    );
  }

  if (rentals.length === 0) {
    return (
      <SafeAreaView className="flex-1 bg-white px-6">
        <View className="flex-1 justify-center items-center space-y-3">
          <Text className="text-2xl font-bold">Aluguéis</Text>
          <Text className="text-gray-500 text-sm">
            Nenhum aluguel foi feito ainda.
          </Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView className="flex-1 bg-white px-6">
      <ScrollView
        contentContainerStyle={{ paddingVertical: 24, paddingBottom: 40 }}
        showsVerticalScrollIndicator={false}
      >
        <Text className="text-2xl font-bold text-center mb-6">Aluguéis</Text>

        {rentals.map((rental) => {
          const start = new Date(rental.start_date);
          const end = new Date(rental.end_date);
          const dayMs = 1000 * 60 * 60 * 24;
          const rentalDays = Math.ceil((end.getTime() - start.getTime()) / dayMs);
          const totalPrice = rental.car.price * rentalDays;

          return (
            <View
              key={rental.id}
              className="bg-gray-100 p-4 rounded-xl shadow-sm space-y-1 relative mb-4"
            >
              <Pressable
                onPress={() => handleRemove(rental.id)}
                className="absolute top-2 right-2 z-10 p-1"
              >
                <Ionicons name="close-circle" size={20} color="#DC1637" />
              </Pressable>

              <View className="flex-row items-center space-x-4">
                <Image
                  source={{ uri: rental.car.images[0] }}
                  style={{ width: 80, height: 60, borderRadius: 8 }}
                  resizeMode="cover"
                />
                <View>
                  <Text className="text-base font-semibold">
                    {rental.car.brand} {rental.car.model}
                  </Text>
                  <Text className="text-sm text-gray-600">
                    {start.toDateString()} → {end.toDateString()}
                  </Text>
                  <Text className="text-sm text-gray-600">{rentalDays} Dia</Text>
                  <Text className="text-red-500 font-semibold">
                    R$ {totalPrice}
                  </Text>
                </View>
              </View>
            </View>
          );
        })}
      </ScrollView>
    </SafeAreaView>
  );
};

export default MyRentalsScreen;
