import { useOutletContext } from "react-router-dom";
import { Button, Card, Row, Col } from "react-bootstrap";
import { SAMPLE_INGREDIENTS } from "../data/drinks";
import { Link } from "react-router-dom";

export default function Ingredients() {
  const { selectedIngredients, setSelectedIngredients } = useOutletContext();

  function toggleIngredient(name) {
    setSelectedIngredients((prev) =>
      prev.includes(name) ? prev.filter((x) => x !== name) : [...prev, name]
    );
  }

  return (
    <div>
      <h2 className="mb-3">Select Your Ingredients</h2>
      <Row xs={2} md={3} lg={4} className="g-3">
        {SAMPLE_INGREDIENTS.map((ing) => (
          <Col key={ing}>
            <Card
              onClick={() => toggleIngredient(ing)}
              className={`text-center p-3 ${
                selectedIngredients.includes(ing) ? "border-warning shadow" : ""
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
