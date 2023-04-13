import React from "react"
import './ToggleSwitch.css'

export default function ToggleSwitch({labelLeft, labelRight}){
    return(
    <div className="container">
      {labelLeft}{" "}
      <div className="toggle-switch">
        <input type="checkbox" className="checkbox" 
               name={labelLeft} id={labelLeft} />
        <label className="label" htmlFor={labelLeft}>
          <span className="inner" />
          <span className="switch" />
        </label>
      </div>
      {" "}{labelRight}
    </div>
    )
}

