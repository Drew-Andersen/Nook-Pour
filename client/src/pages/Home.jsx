import { useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, Card } from "react-bootstrap";

export default function Home() {

  useEffect(() => {
    fetch("/api/hello")
      .then(res => res.json())
      .then(data => console.log(data.message));
  }, []);

  return (
    <Card className="text-center shadow-sm border-0">
      <Card.Body>
        <Card.Title className="fs-3 fw-semibold mb-3">Welcome to <br /> 
          <span className="app-name">Nook & Pour</span>
        </Card.Title>
        <img src="../../public/images/logo.png" width={200}/>
        {/* 
          Possible other names:
          Shake & Serve
          The Mixologist

        */}
        <Card.Text>
          Tell us what ingredients you have, and we’ll find cocktails and shots you can make.
        </Card.Text>
        <Button as={Link} to="/ingredients" className="text-white fw-semibold get-started-btn">
          Get Started
        </Button>
      </Card.Body>
    </Card>
  );
}