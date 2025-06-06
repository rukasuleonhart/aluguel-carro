import React, { useEffect, useState } from "react";
import { View, Text, ScrollView, Image, ActivityIndicator } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import CarCard from "../components/CarCard";
import { getCars } from "../services/api";
import { Car } from "../types/car";

const HomeScreen = () => {
  const [cars, setCars] = useState<Car[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  const fetchCars = async () => {
    try {
      const data = await getCars(); // já é Car[]
      setCars(data); // usa direto o array
    } catch (error) {
      console.error("Erro ao buscar carros:", error);
    } finally {
      setLoading(false);
    }
  };

  fetchCars();
}, []);

  return (
    <SafeAreaView className="flex-1 bg-white">
      <ScrollView
        contentContainerStyle={{ paddingHorizontal: 16, paddingBottom: 80 }}
        showsVerticalScrollIndicator={false}
      >
        {/* Logo */}
        <View className="flex-1 justify-center items-center mt-4 mb-4">
          <Image
            source={require("../assets/images/logo.png")}
            style={{
              width: 200,
              height: 100,
              resizeMode: "contain",
            }}
          />
        </View>

        <Text className="text-2xl font-bold mt-4 mb-4">Veículos Próximos</Text>

        {loading ? (
          <ActivityIndicator size="large" color="#DC1637" />
        ) : cars.length === 0 ? (
          <Text className="text-center text-gray-500">Nenhum veículo disponível.</Text>
        ) : (
          cars.map((car) => <CarCard key={car.id} car={car} />)
        )}
      </ScrollView>
    </SafeAreaView>
  );
};

export default HomeScreen;
