import React from "react"
import './ToggleSwitch.css'

export default function ToggleSwitch({uncheckedLabel, checkedLabel, onChange}){
    return(
    <div className="container">
      {uncheckedLabel}{" "}
      <div className="toggle-switch">
        <input  type="checkbox" className="checkbox" 
               name="modeToggle" id="modeToggle" onChange={onChange}/>
        <label className="label" htmlFor="modeToggle">
          <span className="inner" />
          <span className="switch" />
        </label>
      </div>
      {" "}{checkedLabel}
    </div>
    )
}

