/* eslint-disable no-const-assign */
/* eslint-disable no-unused-vars */

import React, { useState} from 'react'
import axios from 'axios'
import '../App.css'
import bg2 from '../bg_2.png'
import bg1 from'../bg_1.png'
import ToggleSwitch from '../elements/ToggleSwitch'
import { SketchPicker } from 'react-color'


function Big() {
  const [info, setInfo] = useState('hello')
  const [infoState, setInfoState] = useState('hidden')
  const [readyCheck, setReadyCheck] = useState(0)
  const [shownTemplate, setShownTemplate] = useState(bg1)
  const [withStats, setWithStats] = useState(0)
  const [enterStats, setEnterStats] = useState('hidden')
  const [enterNames, setEnterNames] = useState('formtext')
  const [sentTemplate, setSentTemplate] = useState('bg_1.png')
  const [showColorPicker, setShowColorPicker] = useState('justShow') //or hidden
  const [showBgPreview, setShowBgPreview] = useState('hidden') //or templateContainer
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
  
  function handleModeChange(){
    console.log('before', withStats)
    if(withStats)
    {
      console.log('hej?')
      setWithStats(0)
      setShowColorPicker('justShow')
      setEnterNames('formtext')
      setShowBgPreview('hidden')
      setEnterStats('hidden')
    } 
    else
    {
      setWithStats(1)
      setEnterNames('hidden')
      setShowColorPicker('hidden')
      setShowBgPreview('templateContainer')
      setEnterStats('formtext')
    }

    
  }
 
  
  function handleTemplateChange(){
    if(shownTemplate === bg1)
    {
      setShownTemplate(bg2)
      setSentTemplate('bg_2.png')
    }
    else{
      setShownTemplate(bg1)
      setSentTemplate('bg_1.png')
    }
    console.log(shownTemplate)

  }

  
  async function doBigUpload (event) {
    event.preventDefault()
    const form1 = document.getElementById('form1')
    const formData = new FormData(form1)
    formData.append('template', sentTemplate)
    formData.append('color', backgroundColor)
    setInfoState('info')
    setReadyCheck(0)

    console.log('to upload', formData.getAll('compN'))
    setInfo('In process...')

    if(withStats)
    {
      console.log('uploading stats')
      axios.post('/bigsizeStats', formData)
      .then(response => {
        console.log(response)
        setReadyCheck(1)
        setInfo('your PDF is ready!')})
    }
    else{
      console.log('uploading names')
      axios.post('/bigsizeNames', formData)
      .then(response => {
        console.log(response)
        setReadyCheck(1)
        setInfo('your PDF is ready!')})
    }
    
    
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
      setInfo('I said IN PROCESS!')
    }
  }
  //console.log(data)
  return(
      <div>
        <h1>Generate big nametags</h1>
        <div className = 'wrapper'>
          <div className = 'TopColumn'>
            <form id = 'form1' className = 'mainform'>
              <p className = 'formtext'>Competition name: <input className = 'inputs' type = 'text' name = 'compN'/></p>
              <p className = 'formtext'>Upload csv file: <input className = 'interactions' type = 'file' name = 'file'/></p>
              <p className = {enterNames}>Date: <input className='inputs' type = 'text' name = 'date'/> </p>
            </form>
            <div className = 'bottomButtonsContainer'>
              <button className = 'bottomButton' type = 'submit' onClick = {doBigUpload}>Start</button>
              <button className = 'bottomButton' onClick = {handleTemplateChange}>Change template</button>
              <button className = 'bottomButton' onClick = {download}>Download PDF</button>
            </div>
            <ToggleSwitch checkedLabel = 'with events' uncheckedLabel='names only' onChange={handleModeChange}/>
        </div>
        <div className = 'TopColumn'>
          <div className = {showBgPreview} > 
            <p className = 'templateText'>Chosen template:</p>
            <img className='templateImg' src = {shownTemplate} alt = 'template'/>
          </div>
          <div className={showColorPicker}>
            <p className='text'>Choose color for your nametag:</p>
            <ColorPick className='colorPick' />
          </div>
        </div>
      </div>
      <a className='link' href = '/'>back</a>
      <div className ={infoState}>
        {info}
      </div>
    </div>   
  )
}

export default Big;

