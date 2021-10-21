// import logo from './logo.svg';
import './App.css';
import {useState, useEffect} form 'react'
import io from 'socket.io-client'
import {nanoid} from "nanoid"


// no dotenv

const socket = io.connect("http://localhost:5000")

function App() {

  const[message, setMessage] = useState('')

  return (
    <div className="App">
      <header className="App-header">
        <h1> Chatty app </h1>
      </header>
    </div>
  );
}

export default App;
