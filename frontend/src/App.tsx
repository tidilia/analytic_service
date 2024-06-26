import ProductsListGroup from "./components/ProductsListGroup";
import NavigationBar from "./components/NavigationBar";
import Report from "./components/reportsTables/Report";
import { Container } from "react-bootstrap";
import "./App.css"
import { useState } from "react";
import SEOComponent from "./components/Seo";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { useParams } from "react-router-dom";
import ProductPage from "./components/productPage/ProductPage";
import HomePage from "./components/homePage/HomePage";


function App() {
  const [selectedProduct, setSelectedProduct] = useState<{ productID: number, amount: number }>()


  const handleSelectItem = (item: any) => {

  }


  return (
    <>
      <NavigationBar />
      <div id="myBodyID">
        <Router>
          <div>
            <Routes>
              <Route path="/" Component={HomePage} />
              <Route path="/products"
                Component={() => <ProductsListGroup
                  heading=""
                  onSelectItem={handleSelectItem}
                  listType="full" 
                  loading={false}/>} />
              <Route path="/seo" Component={SEOComponent} />
              <Route path="/reports" Component={Report} />
              <Route path="/products/:id" Component={ProductPage} />
            </Routes>
          </div>
        </Router>
      </div>
    </>
  )
}

{/* <NavigationBar />
<ProductsListGroup heading="" onSelectItem={handleSelectItem} listType="full"></ProductsListGroup> */}

export default App;
