import { SafeAreaView, StyleSheet, Text, View } from "react-native";
import React from "react";
import CustomBouton from "../components/onboarding/Bouton";
import Constants from "expo-constants";

const Onboarding = () => {
  const handleLoginWithGoogle = () => {
    console.log("google");
  };
  const handleLoginWithTwitter = () => {
    console.log("twitter");
  };
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.welcome}>Welcome on board!</Text>

      <View style={styles.content}>
        <Text style={styles.signText}>Sign in or Create an account</Text>

        <CustomBouton
          label={"Continue with Google"}
          provider={"google"}
          onPress={handleLoginWithGoogle}
        />
        <CustomBouton
          label={"Continue with Twitter"}
          provider={"twitter"}
          onPress={handleLoginWithTwitter}
        />
      </View>
    </SafeAreaView>
  );
};

export default Onboarding;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "white",
    paddingHorizontal: 20,
    paddingTop: Constants.statusBarHeight + 30,
  },
  welcome: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#33313E",
  },
  content: {
    flex: 1,
    justifyContent: "center",
    gap: 22,
  },
  signText: {
    fontSize: 20,
    fontWeight: "700",
    color: "#33313E",
  },
});
