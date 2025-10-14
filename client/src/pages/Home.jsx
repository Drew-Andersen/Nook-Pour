import { Link } from "react-router-dom";
import { Button, Card } from "react-bootstrap";

export default function Home() {
  return (
    <Card className="text-center shadow-sm border-0">
      <Card.Body>
        <Card.Title className="fs-3 fw-semibold mb-3">Welcome to Nook & Pour</Card.Title>
        <Card.Text>
          Tell us what ingredients you have, and we’ll find cocktails and shots you can make.
        </Card.Text>
        <Button variant="warning" as={Link} to="/ingredients" className="text-white fw-semibold">
          Select Ingredients
        </Button>
      </Card.Body>
    </Card>
  );
}