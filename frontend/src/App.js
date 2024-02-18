import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';


function App() {
  const [Destinations, setDestinations] = useState([]);

  useEffect(() => {
    async function fetchDestinations() {
      try {
        const response = await axios.get('http://localhost:8000/destinations');
        setDestinations(response.data);
      } catch (error) {
        console.error('Error fetching weather forecast:', error);
      }
    }

    fetchDestinations();
  }, []);

  return (
    <div class="hero d-flex">
      <header class="mb-auto">
        <div class="">
          <img src="/icon.png" height="50" width="50" />
          <nav class="nav nav-masthead justify-content-center float-md-end">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
            <a class="nav-link" href="#">Features</a>
            <a class="nav-link" href="#">Contact</a>
          </nav>
        </div>
      </header>
    
    <div class="">

    
      <main class="">
        <h1 className="title">Clutch Vacations</h1>
    
        <p class="lead">
          {/* <a href="#" class="btn btn-lg btn-secondary fw-bold border-white bg-white">Learn more</a> */}
        </p>
      </main>
    </div>
    {/* <div>
        {Destinations.map((destination, index) => (
          <div key={index}>
            <p>Date: {destination.date}</p>
            <p>City: {destination.city}</p>
            <p>Cost: {destination.cost}</p>
          </div>
        ))}
      </div> */}
   
      </div>
   
  );
}

export default App;

