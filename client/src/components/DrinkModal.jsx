import PropTypes from "prop-types";
import { Modal, ListGroup, Button } from "react-bootstrap";

export default function DrinkModal({ show = false, handleClose = () => {}, drink = null }) {
  const ingredients = drink?.ingredients ?? [];
  const instructions = drink?.instructions ?? [];

  return (
    <Modal show={show} onHide={handleClose} centered>
      <Modal.Header closeButton>
        <Modal.Title>
          {drink ? (
            <>
              {drink.icon} {drink.name}
            </>
          ) : (
            "Drink details"
          )}
        </Modal.Title>
      </Modal.Header>

      <Modal.Body>
        <h5 className="mb-2">Ingredients</h5>
        {ingredients.length ? (
          <ListGroup className="mb-3">
            {ingredients.map((ing, i) => (
              <ListGroup.Item key={i}>{ing}</ListGroup.Item>
            ))}
          </ListGroup>
        ) : (
          <p className="text-muted">No ingredients available.</p>
        )}

        <h5 className="mb-2">Instructions</h5>
        {instructions.length ? (
          <ol>
            {instructions.map((step, i) => (
              <li key={i}>{step}</li>
            ))}
          </ol>
        ) : (
          <p className="text-muted">No instructions available.</p>
        )}
      </Modal.Body>

      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
        <Button variant="warning" className="text-white" onClick={handleClose}>
          {/* Replace with actual "Make" action when ready */}
          Make
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

DrinkModal.propTypes = {
  show: PropTypes.bool,
  handleClose: PropTypes.func.isRequired,
  drink: PropTypes.object,
};