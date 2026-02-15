import { useOutletContext } from "react-router-dom";
import { Button, Card, Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";

export default function Ingredients() {
  const { selectedIngredients, setSelectedIngredients } = useOutletContext();
  const [ ingredients, setIngredients ] = useState([])

  useEffect(() => {
    fetch("/api/ingredients")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch ingredients");
        return res.json()
      })
      .then((data) => setIngredients(data))
      .then((err) => console.error(err))
  }, [])

  function toggleIngredient(name) {
    setSelectedIngredients((prev) =>
      prev.includes(name) ? prev.filter((x) => x !== name) : [...prev, name]
    );
  }

  return (
    <div>
      <h2 className="mb-3">Select Your Ingredients</h2>
      <Row xs={2} md={3} lg={4} className="g-3">
        {ingredients.map((ing) => (
          <Col key={ing}>
            <Card
              onClick={() => toggleIngredient(ing)}
              className={`text-center p-3 ${
                selectedIngredients.includes(ing) ? "border-warning shadow bg-warning bg-opacity-25" : ""
              }`}
              style={{ cursor: "pointer" }}
            >
              <span role="img" aria-label="bottle" className="fs-2">
                🍾
              </span>
              <Card.Text className="fw-medium mt-2">{ing}</Card.Text>
            </Card>
          </Col>
        ))}
      </Row>

      <div className="mt-4 text-end">
        <Link to="/drinks">
          <Button variant="warning" className="text-white">
            View Drinks
          </Button>
        </Link>
      </div>
    </div>
  );
}
