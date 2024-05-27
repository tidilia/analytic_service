import ProductsListGroup from "./components/ProductsListGroup";
import NavigationBar from "./components/NavigationBar";
import { Container } from "react-bootstrap";
import "./App.css"
import { useState } from "react";
import SEOComponent from "./components/Seo";

function App() {
  const [selectedProduct, setSelectedProduct] = useState<{productID: number, amount: number}>()

  const handleSelectItem = (item: any) => {
    setSelectedProduct((item.nmID, item.quantity))
  }

  return (
    <>
      <NavigationBar />
      <SEOComponent />
    </>
  )
}

{/* <NavigationBar />
<ProductsListGroup heading="" onSelectItem={handleSelectItem} listType="full"></ProductsListGroup> */}

export default App;
