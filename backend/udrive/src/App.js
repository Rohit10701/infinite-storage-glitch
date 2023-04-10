import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {useEffect} from 'react'
function App() {
  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/abc').then((res)=>{console.log(res)}).catch((e)=>{
      console.log(e)
    })
  })
  return (
    <div className="App">
      
    </div>
  );
}

export default App;
