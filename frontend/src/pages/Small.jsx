/* eslint-disable no-const-assign */
/* eslint-disable no-unused-vars */

import React, { useState} from 'react'
import axios from 'axios'
import '../App.css'
import bg2 from '../bg_2.png'
import bg1 from'../bg_1.png'
import { SketchPicker } from 'react-color';


function Small() {
  const [run, setRun] = useState('interactions')
  const [template, setTemplate] = useState('bg_1.png')
  const [info, setInfo] = useState('hello')
  const [infoState, setInfoState] = useState('hidden')
  const [readyCheck, setReadyCheck] = useState(0)
  const [shownTemplate, setShownTemplate] = useState(bg1)
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
 
  
  function handleTemplateChange(){
    shownTemplate === bg1 ? setShownTemplate(bg2): setShownTemplate(bg1)

  }

  function doSmallUpload () {
    //creating formData to post
    const gotNames = document.getElementsByName('names')
    const compN = document.getElementsByName('compN')
    const color = backgroundColor
    const form = document.getElementById('form1')
    const formData = new FormData(form)
    formData.append('color', color)

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
  
  /*async function doupload (event) {
    event.preventDefault()
    const form1 = document.getElementById('form1')
    const formData = new FormData(form1)
    setInfoState('info')
    setReadyCheck(0)

    console.log('to upload', formData.getAll('compN'))
    setInfo('In progress...')

    axios.post('/bigsize', formData)
    .then(response => {
      console.log(response)
    setReadyCheck(1)
    setInfo('your PDF is ready!')})
    setRun('interactions')  
  }*/

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
        })}
    else{
      setInfo('I said IN PROGRESS!')
      if(run === 'interactions'){setRun('runleft')}
      if(run === 'runleft'){setRun('runright')}
      if(run === 'runright'){setRun('runleft')}
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

