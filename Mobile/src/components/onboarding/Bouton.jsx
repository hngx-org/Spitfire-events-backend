import { Image, StyleSheet, Text, TouchableOpacity } from "react-native";
import twitter from "../../../assets/icons/tweet.png";
import google from "../../../assets/icons/google.png";

export default function CustomBouton({ label, provider, ...props }) {
  return (
    <TouchableOpacity style={styles.bouton} {...props}>
      {provider === "twitter" ? (
        <Image source={twitter} style={styles.img} />
      ) : (
        <Image source={google} style={styles.img} />
      )}
      <Text style={styles.texteBouton}>{label}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  bouton: {
    display: "flex",
    paddingVertical: 10,
    paddingHorizontal: 12,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
    borderColor: "#571FCD",
    borderWidth: 1,
    backgroundColor: "#fff",
    gap: 15,
    borderRadius: 5,
  },
});
