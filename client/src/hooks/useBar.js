import { useOutletContext } from "react-router-dom";

// Shared app state (selected ingredients, favorites, recipe modal) from <App />.
export default function useBar() {
  return useOutletContext();
}
