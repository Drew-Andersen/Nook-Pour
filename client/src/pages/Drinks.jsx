import { Link, useOutletContext } from "react-router-dom";
import { Card, Button } from "react-bootstrap";

export default function Drinks() {
  const { drinks, handleShowModal, selectedIngredients } = useOutletContext();

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
            variant="warning"
            className="text-white"
          >
            <Link style={{textDecoration: "none", color: "white"}} to="/alldrinks">View All Drinks</Link>
          </Button>
          </div>
      ) : (
        <div className="row g-3">
          {availableDrinks.map((drink) => (
            <div className="col-md-6 col-lg-4" key={drink.id}>
              <Card className="shadow-sm h-100">
                <Card.Body>
                  <Card.Title className="fs-5">
                    {drink.icon} {drink.name}
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
