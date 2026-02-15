import { useOutletContext } from "react-router-dom";
import { useState, useEffect } from "react";
import { Card, Button, Form } from "react-bootstrap";

export default function AllDrinks() {
  const { handleShowModal } = useOutletContext();
  const [drinks, setDrinks] = useState([])
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetch('/api/drinks')
      .then(res => {
        if (!res.ok) {
          throw new Error('Failed to fetch drinks.')
        }
        return res.json()
      })
      .then(data => setDrinks(data))
      .then(err => console.error(err))
  }, [])

  const filteredDrinks = drinks.filter((drink) => {
    const term = searchTerm.toLowerCase();
    return (
      drink.name.toLowerCase().includes(term) ||
      drink.ingredients.some((ing) => ing.toLowerCase().includes(term))
    );
  });

  // fetch("/api/drinks/1")
  //   .then(res => res.json())
  //   .then(data => console.log(data))
  //   .catch(err => console.error(err));

  //   // Route used for testing connection to FlasK
  //   fetch("/api/hello")
  //     .then(res => res.json())
  //     .then(data => console.log(data))
  //     .catch(err => console.error(err));
  

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
          <p className="text-muted mt-4">No drinks found for {searchTerm};</p>
        )}
      </div>
    </div>
  );
}