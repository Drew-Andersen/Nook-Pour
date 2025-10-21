import { useOutletContext } from "react-router-dom";
import { useState } from "react";
import { Card, Button, Form } from "react-bootstrap";

export default function AllDrinks() {
  const { drinks, handleShowModal } = useOutletContext();
  const [searchTerm, setSearchTerm] = useState("");

  const filteredDrinks = drinks.filter((drink) => {
    const term = searchTerm.toLowerCase();
    return (
      drink.name.toLowerCase().includes(term) ||
      drink.ingredients.some((ing) => ing.toLowerCase().includes(term))
    );
  });

  return (
    <div>
      <h2 className="mb-3">All Drinks</h2>
      <p className="text-muted">Browse or search the full cocktail collection</p>

      <Form className="mb-4 d-flex justify-content-center">
        <Form.Control
          type="text"
          placeholder="Search by drink or ingredient..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="shadow-sm w-50"
        />
      </Form>

      <div className="row g-3">
        {filteredDrinks.length > 0 ? (
          filteredDrinks.map((drink) => (
            <div className="col-md-6 col-lg-4" key={drink.id}>
              <Card className="shadow-sm h-100 border-0">
                <Card.Body>
                  <Card.Img src={drink.image} alt={drink.name} style={{ width: "140px" }} />
                  <Card.Title className="fs-5 d-flex align-items-center justify-content-center gap-2">
                    {drink.name}
                  </Card.Title>
                  <Card.Text className="text-muted small">
                    {drink.ingredients.join(" • ")}
                  </Card.Text>
                  <Button
                    variant="warning"
                    className="text-white w-100"
                    onClick={() => handleShowModal(drink)}
                  >
                    View Recipe
                  </Button>
                </Card.Body>
              </Card>
            </div>
          ))
        ) : (
          <p className="text-muted mt-4">No drinks found for &quot;{searchTerm}&quot;</p>
        )}
      </div>
    </div>
  );
}