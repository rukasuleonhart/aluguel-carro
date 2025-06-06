import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import TabNavigator from "./TabNavigator";
import CarDetailScreen from "../screens/CarDetailScreen";
import SchedulingScreen from "../screens/SchedulingScreen";
import SchedulingDetailsScreen from "../screens/SchedulingDetailsScreen";
import LoadingScreen from "../screens/LoadingScreen";
import { Car } from "../types/car"; // importe o tipo Car

// Defina aqui o RootStackParamList
export type RootStackParamList = {
  Loading: undefined;
  Main: undefined;
  CarDetail: { carId: number };
  Scheduling: { car: Car };           // aqui passa o objeto Car inteiro
  SchedulingDetails: { car: Car };    // e aqui também
};

const Stack = createNativeStackNavigator<RootStackParamList>();

const AppNavigator = () => (
  <NavigationContainer>
    <Stack.Navigator screenOptions={{ headerShown: false }}>
      <Stack.Screen name="Loading" component={LoadingScreen} />
      <Stack.Screen name="Main" component={TabNavigator} />
      <Stack.Screen name="CarDetail" component={CarDetailScreen} />
      <Stack.Screen name="Scheduling" component={SchedulingScreen} />
      <Stack.Screen name="SchedulingDetails" component={SchedulingDetailsScreen} />
    </Stack.Navigator>
  </NavigationContainer>
);

export default AppNavigator;
