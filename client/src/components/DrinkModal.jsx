import { Modal, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import DrinkImage from "./DrinkImage";
import FavoriteButton from "./FavoriteButton";
import Recipe from "./Recipe";

export default function DrinkModal({ drink, onClose, isFavorite, onToggleFavorite, have }) {
  return (
    <Modal show={Boolean(drink)} onHide={onClose} centered size="lg" className="drink-modal">
      {drink && (
        <>
          <Modal.Header closeButton>
            <Modal.Title className="d-flex align-items-center gap-2">
              {drink.name}
              <FavoriteButton active={isFavorite} onClick={() => onToggleFavorite(drink.id)} />
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <div className="row g-4">
              <div className="col-md-5">
                <DrinkImage drink={drink} size="lg" />
                <p className="text-muted mt-3 mb-0">{drink.description}</p>
              </div>
              <div className="col-md-7">
                <Recipe drink={drink} have={have} />
              </div>
            </div>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="outline-secondary" onClick={onClose}>
              Close
            </Button>
            <Button as={Link} to={`/drinks/${drink.id}`} variant="primary" onClick={onClose}>
              Open full recipe
            </Button>
          </Modal.Footer>
        </>
      )}
    </Modal>
  );
}
