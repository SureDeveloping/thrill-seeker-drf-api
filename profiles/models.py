import React, { useEffect, useState } from "react";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import appStyles from "../../App.module.css";
import styles from "../../styles/Park.module.css";
import { useParams } from "react-router";
import { axiosReq } from "../../api/axiosDefaults";

function ParkPage() {
  const { id } = useParams();
  const [park, setPark] = useState({});
  const [author, setAuthor] = useState(null);

  useEffect(() => {
    const fetchParkData = async () => {
      try {
        const { data } = await axiosReq.get(`/parks/${id}`);
        setPark(data);
        setAuthor(data.user); // Annahme: park.user enthält den Autor des Parks
      } catch (error) {
        console.error("Error fetching park data:", error);
      }
    };

    fetchParkData();
  }, [id]);

  return (
    <Row className="h-100">
      <Col className="py-2 p-0 p-lg-2 order-lg-2" lg={5}>
        <div className={styles.ParkImageContainer}>
          <img
            src={park.image}
            alt={park.name}
            className={styles.ParkImage}
          />
        </div>
      </Col>

      <Col className="py-2 p-0 p-lg-2 order-lg-1" lg={7}>
        <div className={styles.DataCard}>
          <h2>{park.name}</h2>
          {author && (
            <>
              <p>
                Author:{" "}
                <>
                  <img
                    src={author.profile.profile_picture}
                    alt={author.username}
                    className={styles.AuthorImage}
                  />
                  {author.username}
                </>
              </p>
            </>
          )}
          <p>{park.description}</p>
          <p>Total Number of Rides: {park.total_number_of_rides}</p>
          <p>Total Number of Coasters: {park.total_number_of_coasters}</p>
          <p>Thrill Factor: {park.thrill_factor}</p>
          <p>Overall Rating: {park.overall_rating}</p>
          <p>
            Website:{" "}
            <a href={park.website} className={styles.Link}>
              {park.website}
            </a>
          </p>
          <p>Created At: {park.created_at}</p>
          <p>Updated At: {park.updated_at}</p>
        </div>
      </Col>
    </Row>
  );
}

export default ParkPage;