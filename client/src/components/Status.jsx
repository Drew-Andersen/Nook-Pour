import { Button, Spinner } from "react-bootstrap";

export function Loading({ label = "Loading…" }) {
  return (
    <div className="status-box" role="status">
      <Spinner animation="border" variant="primary" />
      <p className="mt-3 mb-0">{label}</p>
    </div>
  );
}

export function ErrorMessage({ error, onRetry }) {
  return (
    <div className="status-box" role="alert">
      <div className="status-emoji">🫗</div>
      <p className="fw-semibold mb-1">Spilled the drinks.</p>
      <p className="text-muted">{error?.message || "Something went wrong."}</p>
      {onRetry && (
        <Button variant="outline-primary" onClick={onRetry}>
          Try again
        </Button>
      )}
    </div>
  );
}

export function Empty({ emoji = "🍸", title, children }) {
  return (
    <div className="status-box">
      <div className="status-emoji">{emoji}</div>
      <p className="fw-semibold mb-1">{title}</p>
      <div className="text-muted">{children}</div>
    </div>
  );
}
