import React from 'react'
import '../Homepage.css'

export default function Home(){
    return(
        <div>
            <h1>Nametag maker</h1>
            <p className = 'text'>Choose what type of nametags u wonna make</p>
            <a className = 'link' href='/Big'>big</a>
            <p/>
            <a className = 'link' href='/Small'>small</a>
        </div>
    )
}