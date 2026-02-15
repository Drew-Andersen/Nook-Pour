import { useOutletContext, Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Card, Button } from "react-bootstrap";

export default function Drinks() {
  const { handleShowModal, selectedIngredients } = useOutletContext();
  const [drinks, setDrinks] = useState([])

  useEffect(() => {
    fetch('/api/drinks')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch Drinks')
        return res.json()
      })
      .then(data => setDrinks(data))
      .then(err => console.error(err))
  }, [])

  const availableDrinks = drinks.filter((drink) =>
    drink.ingredients.every((ing) =>
      selectedIngredients.some(
        (s) =>
          s.toLowerCase().includes(ing.toLowerCase()) ||
          ing.toLowerCase().includes(s.toLowerCase())
      )
    )
  );

  return (
    <div>
      <h2 className="mb-3">Available Drinks</h2>

      {availableDrinks.length === 0 ? (
        <div>
          <p className="text-muted">
            No drinks match your selected ingredients. Try adding more!
          </p>
          <Button
            as={Link}
            to='/alldrinks'
            variant="warning"
            className="text-white"
          >
            View All Drinks
          </Button>
          </div>
      ) : (
        <div className="row g-3">
          {availableDrinks.map((drink) => (
            <div className="col-md-6 col-lg-4" key={drink.id}>
              <Card className="shadow-sm h-100">
                <Card.Body>
                  <Card.Img src={drink.image} alt={drink.name} style={{ width: "140px" }} />
                  <Card.Title className="fs-5">
                    {drink.name}
                  </Card.Title>
                  <Card.Text className="text-muted">
                    {drink.ingredients.join(" • ")}
                  </Card.Text>
                  <Button
                    variant="warning"
                    className="text-white"
                    onClick={() => handleShowModal(drink)}
                  >
                    View Recipe
                  </Button>
                </Card.Body>
              </Card>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
