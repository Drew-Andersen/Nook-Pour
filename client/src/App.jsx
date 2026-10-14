import { useCallback, useState } from "react";
import { Outlet, ScrollRestoration } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import DrinkModal from "./components/DrinkModal";
import useLocalStorage from "./hooks/useLocalStorage";
import "./App.css";

export default function App() {
  const [selectedDrink, setSelectedDrink] = useState(null);
  const [selectedIngredients, setSelectedIngredients] = useLocalStorage("np:bar", []);
  const [favorites, setFavorites] = useLocalStorage("np:favorites", []);

  const toggleIngredient = useCallback(
    (name) =>
      setSelectedIngredients((prev) =>
        prev.includes(name) ? prev.filter((x) => x !== name) : [...prev, name]
      ),
    [setSelectedIngredients]
  );

  const toggleFavorite = useCallback(
    (slug) =>
      setFavorites((prev) =>
        prev.includes(slug) ? prev.filter((x) => x !== slug) : [...prev, slug]
      ),
    [setFavorites]
  );

  const context = {
    selectedIngredients,
    setSelectedIngredients,
    toggleIngredient,
    favorites,
    toggleFavorite,
    isFavorite: (slug) => favorites.includes(slug),
    handleShowModal: setSelectedDrink,
  };

  return (
    <div className="app-shell">
      <Header barCount={selectedIngredients.length} favoriteCount={favorites.length} />
      <main className="container py-4 py-md-5 flex-grow-1">
        <Outlet context={context} />
      </main>
      <Footer />

      <DrinkModal
        drink={selectedDrink}
        onClose={() => setSelectedDrink(null)}
        isFavorite={selectedDrink ? favorites.includes(selectedDrink.id) : false}
        onToggleFavorite={toggleFavorite}
        have={selectedIngredients}
      />
      <ScrollRestoration />
    </div>
  );
}
