import { useOutletContext } from "react-router-dom";
import { Card, Button } from "react-bootstrap";

export default function AllDrinks() {
  const { drinks, handleShowModal } = useOutletContext();

  return (
    <div>
      <h2 className="mb-3">All Drinks</h2>
      <p className="text-muted">Browse the full cocktail collection 🍸</p>

      <div className="row g-3">
        {drinks.map((drink) => (
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
    </div>
  );
}