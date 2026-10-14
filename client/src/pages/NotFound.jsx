import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import { Empty } from "../components/Status";

export default function NotFound({ what = "page" }) {
  return (
    <Empty emoji="🫙" title={`We couldn't find that ${what}`}>
      <p>It may have been moved, or the glass is just empty.</p>
      <Button as={Link} to="/">Back home</Button>
    </Empty>
  );
}
