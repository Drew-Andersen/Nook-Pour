import { NavLink, Link } from "react-router-dom";
import { Navbar, Container, Nav, Badge } from "react-bootstrap";

export default function Header({ barCount = 0, favoriteCount = 0 }) {
  return (
    <Navbar expand="md" className="site-nav" collapseOnSelect>
      <Container>
        <Navbar.Brand as={Link} to="/" className="d-flex align-items-center gap-2">
          <img src="/images/logo.png" alt="" width="40" height="40" />
          <span className="brand-name">Nook &amp; Pour</span>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="main-nav" />
        <Navbar.Collapse id="main-nav">
          <Nav className="ms-auto align-items-md-center gap-md-2">
            <Nav.Link as={NavLink} to="/ingredients" eventKey="bar">
              My Bar {barCount > 0 && <Badge pill bg="primary">{barCount}</Badge>}
            </Nav.Link>
            <Nav.Link as={NavLink} to="/drinks" eventKey="make">
              What Can I Make?
            </Nav.Link>
            <Nav.Link as={NavLink} to="/alldrinks" eventKey="all">
              All Drinks
            </Nav.Link>
            <Nav.Link as={NavLink} to="/favorites" eventKey="fav">
              Favorites {favoriteCount > 0 && <Badge pill bg="primary">{favoriteCount}</Badge>}
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
