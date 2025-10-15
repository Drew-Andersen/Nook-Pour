import { useState } from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";
import DrinkModal from "./components/DrinkModal";
import { SAMPLE_DRINKS } from "./data/drinks";
import './app.css';

export default function App() {
  const [showModal, setShowModal] = useState(false);
  const [selectedDrink, setSelectedDrink] = useState(null);
  const [selectedIngredients, setSelectedIngredients] = useState([]);

  const handleShowModal = (drink) => {
    setSelectedDrink(drink);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setSelectedDrink(null);
    setShowModal(false);
  };

  return (
    <>
      <Header />
      <div className="container mt-4">
        <Outlet
          context={{
            drinks: SAMPLE_DRINKS,
            handleShowModal,
            selectedIngredients,
            setSelectedIngredients,
          }}
        />
      </div>

      <DrinkModal
        show={showModal}
        handleClose={handleCloseModal}
        drink={selectedDrink}
      />
    </>
  );
}