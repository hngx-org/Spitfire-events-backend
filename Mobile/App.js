// In App.js in a new project

import * as React from "react";
import {NavigationContainer} from "@react-navigation/native";
import { TabNavigator } from "./src/navigators/TabNavigator";
import Home from "./src/screens/Home";

const App = () => {
  return (
    <NavigationContainer>
      {/* <TabNavigator /> */}
      <Home />
    </NavigationContainer>
  );
};

export default App;
