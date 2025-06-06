import React from "react";
import { View, Text, Pressable } from "react-native";
import { useRentalStore } from "../store/rentalStore";
import { useRoute, useNavigation, RouteProp } from "@react-navigation/native";
import { Ionicons } from "@expo/vector-icons";
import { RootStackParamList } from "../navigation/AppNavigator";
import { Car } from "../types/car";
import { SafeAreaView } from "react-native-safe-area-context";
import { NativeStackNavigationProp } from "@react-navigation/native-stack";

type SchedulingDetailsRouteProp = RouteProp<RootStackParamList, "SchedulingDetails">;
type SchedulingDetailsNavigationProp = NativeStackNavigationProp<RootStackParamList, "SchedulingDetails">;

const SchedulingDetailsScreen = () => {
  const route = useRoute<SchedulingDetailsRouteProp>();
  const navigation = useNavigation<SchedulingDetailsNavigationProp>();

  const car: Car | undefined = route.params?.car;
  const { startDate, endDate, addRental } = useRentalStore();

  if (!car) {
    return (
      <View className="flex-1 justify-center items-center bg-white">
        <Text className="text-red-500 text-lg">Carro não encontrado.</Text>
      </View>
    );
  }

  if (!startDate || !endDate) {
    return (
      <View className="flex-1 justify-center items-center bg-white">
        <Text className="text-red-500 text-lg">Período de aluguel não definido.</Text>
      </View>
    );
  }

  // Garante que sejam objetos Date
  const startDateObj = new Date(startDate);
  const endDateObj = new Date(endDate);

  const dayMs = 1000 * 60 * 60 * 24;
  const rentalDays = Math.ceil(
    (endDateObj.getTime() - startDateObj.getTime()) / dayMs
  );
  const totalPrice = rentalDays * car.price;

  return (
    <SafeAreaView className="flex-1 bg-white px-6">
      <View className="flex-row items-center space-x-2 mb-6 mt-4">
        <Pressable
          onPress={() => {
            if (navigation.canGoBack()) {
              navigation.goBack();
            } else {
              navigation.navigate("Main", { screen: "Rentals" });
            }
          }}
        >
          <Ionicons name="chevron-back" size={26} color="#dc1637" />
        </Pressable>
        <Text className="text-xl font-bold">Resumo do aluguel</Text>
      </View>

      {/* aqui você coloca o resto do conteúdo do resumo do aluguel */}

      <View className="bg-gray-100 rounded-xl p-4">
        <Text className="text-gray-500">Total</Text>
        <Text className="text-lg font-semibold text-red-500">
          R$ {totalPrice.toFixed(2)}
        </Text>
      </View>

      <Pressable
        className="bg-primary py-4 rounded-lg mt-4"
        onPress={() => {
          addRental({ car, startDate: startDateObj, endDate: endDateObj });
          navigation.navigate("Main", { screen: "Rentals" });
        }}
      >
        <Text className="text-white text-center font-semibold text-base">
          Alugar
        </Text>
      </Pressable>
    </SafeAreaView>
  );
};

export default SchedulingDetailsScreen;
