export default function FavoriteButton({ active, onClick, className = "" }) {
  return (
    <button
      type="button"
      className={`fav-btn ${active ? "is-active" : ""} ${className}`}
      onClick={(e) => {
        e.stopPropagation();
        onClick();
      }}
      aria-pressed={active}
      aria-label={active ? "Remove from favorites" : "Save to favorites"}
      title={active ? "Remove from favorites" : "Save to favorites"}
    >
      {active ? "♥" : "♡"}
    </button>
  );
}
