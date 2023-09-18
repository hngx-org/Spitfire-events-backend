// In App.js in a new project

import * as React from "react";
import {NavigationContainer} from "@react-navigation/native";
import { TabNavigator } from "./src/navigators/TabNavigator";

function App() {
  return (
    <NavigationContainer>
      <TabNavigator />
    </NavigationContainer>
  );
}

export default App;
