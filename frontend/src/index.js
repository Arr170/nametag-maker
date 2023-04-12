import ReactDOM from 'react-dom/client'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import Small from './pages/Small'
import Big from './pages/Big'
import React from 'react'

export default function App(){
  return(
    <BrowserRouter>
      <Routes>
        <Route path = '/' element = {<Home/>}/>
        <Route path = 'small' element = {<Small/>}/>
        <Route path = 'big' element = {<Big />}/>
      </Routes>
    </BrowserRouter>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <App />
)

