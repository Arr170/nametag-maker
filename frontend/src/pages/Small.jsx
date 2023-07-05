/* eslint-disable no-const-assign */
/* eslint-disable no-unused-vars */

import React, { useState} from 'react'
import axios from 'axios'
import '../App.css'
import { SketchPicker } from 'react-color'


function Small() {
  const [info, setInfo] = useState('hello')
  const [infoState, setInfoState] = useState('hidden')
  const [readyCheck, setReadyCheck] = useState(0)
  let backgroundColor = '#fff'

  
  class ColorPick extends React.Component {
    state = {
      background: '#fff',
    }
  
    handleChangeComplete = (color) => {
      this.setState({ background: color.hex })
      backgroundColor = color.hex
      console.log(backgroundColor)
    }
  
    render() {
      return (
        <SketchPicker
          color={ this.state.background }
          onChangeComplete={ this.handleChangeComplete }
        />
      )
    }
  }

  function doSmallUpload () {
    //creating formData to post
    const gotNames = document.getElementsByName('names')
    const compN = document.getElementsByName('compN')
    const form = document.getElementById('form1')
    const formData = new FormData(form)
    formData.append('color', backgroundColor)

    setInfoState('info')
    setReadyCheck(0)
    setInfo('In process...')
    


    axios.post('/smallsize', formData)
    .then(response => {
      console.log(response)
      setReadyCheck(1)
      setInfo('your PDF is ready!')

    })
  }
  
  function download(){
    if(readyCheck){
      
      axios({
        url: "/download",
        method: 'GET',
        responseType: 'blob',
      }).then(response => {
        // create a URL for the file and open it in a new tab
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'file.pdf')
        document.body.appendChild(link)
        link.click()
        setInfoState('hidden')
        setReadyCheck(0)
        })}
    else{
      setInfo('I said IN PROGRESS!')     
    }
  }
  //console.log(data)
  return(
      <div>
        <h1>Generate small nametags</h1>
        <div className = 'wrapper'>
          <div className = 'TopColumn'>
            <form id = 'form1' className = 'mainform'>
              <p className = 'formtext'>Competition name: <input className = 'inputs' type = 'text' name = 'compN'/></p>
              <p className = 'formtext'>Competitors' names separated by enter: <textarea className = 'inputs' type = 'text' name = 'names'/></p>
            </form>
            <div className = 'bottomButtonsContainerSmall'>
              <button className = 'bottomButton' type = 'submit' onClick = {doSmallUpload}>Start</button>
              <button className = 'bottomButton' onClick = {download}>Download PDF</button>
            </div>
        </div>
        <div className = 'TopColumn'>
          <p className = 'text'>Choose color for your nametag:</p>
          <ColorPick className='colorPick' />
        </div>
      </div>
      <a className='link' href = '/'>back</a>
      <div className ={infoState}>
        {info}
      </div>
    </div>   
  )
}

export default Small;

