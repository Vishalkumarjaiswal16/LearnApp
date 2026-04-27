import { Link } from "react-router-dom";
import "../App.css";

function Home() {
  return (
    <div className="home-container">
      <div className="hero-section">
        <h1 className="hero-title">Master Your Future.</h1>
        <p className="hero-subtitle">
          Experience a highly personalized journey to master your skills with real-time progress tracking, adaptive courses, and intuitive dashboards.
        </p>
        <div className="hero-buttons">
          <Link to="/dashboard" className="btn btn-primary btn-large">
            Go to Dashboard
          </Link>
          <a href="#features" className="btn btn-secondary btn-large">
            Learn More
          </a>
        </div>
      </div>
      
      <div id="features" className="features-section">
        <div className="feature-card">
          <h3>Adaptive Courses</h3>
          <p>Courses that adapt to your skill level and pace.</p>
        </div>
        <div className="feature-card">
          <h3>Real-time Tracking</h3>
          <p>Monitor your progress with detailed analytics.</p>
        </div>
        <div className="feature-card">
          <h3>Expert Mentorship</h3>
          <p>Learn from the best in the industry.</p>
        </div>
      </div>
    </div>
  );
}

export default Home;