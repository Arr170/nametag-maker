/* eslint-disable no-const-assign */
/* eslint-disable no-unused-vars */

import React, { useState} from 'react'
import axios from 'axios'
import './App.css'


function App() {
  const[run, setRun] = useState('interactions')
  const [template, setTemplate] = useState('bg_1.png')
  const [info, setInfo] = useState('hello')
  const [infoState, setInfoState] = useState('hidden')
  const templates = ['bg_1.png', 'bg_2.png']
  const [readyCheck, setReadyCheck] = useState(0)

  

 
  
  function handleTemplateChange(){
    if(template === templates[0]){
      setTemplate(templates[1])
    }
    else{setTemplate(templates[0])}

  }

 
  
  async function doupload (event) {
    event.preventDefault()
    const form1 = document.getElementById('form1')
    const formData = new FormData(form1)
    setInfoState('info')
    setReadyCheck(0)
    //formData.append('file', file)//adding file
    //formData.append('file', compName)//adding comp name
    //formData.append('template', template)//adding tamplate

    console.log('to upload', formData.getAll('compN'))
    setInfo('In progress...')

    axios.post('/data', formData)
    .then(response => {
      console.log(response)
    setReadyCheck(1)
    setInfo('your PDF is ready!')})
    setRun('interactions')
    
    
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
        })}
    else{
      setInfo('I said IN PROGRESS!')
      if(run === 'interactions'){setRun('runleft')}
      if(run === 'runleft'){setRun('runright')}
      if(run === 'runright'){setRun('runleft')}
      //window.alert('your file is not ready yet')
    }
  }
  //console.log(data)
  return(
    <body>
        <h1>Nametag generator</h1>
        <form id = 'form1' class = 'mainform'>
          <p class = 'formtext'>Competition name: <input class = 'inputs' type = 'text' name = 'compN'/></p>
          <p class = 'formtext'>Choose template: <input class = 'inputs' type = 'text' name = 'template' value = {template} readOnly/>
          <input class = 'interactions' type = 'button' value = 'change template' onClick={handleTemplateChange}/>
          </p>
          <p class = 'formtext'>Upload csv file: <input class = 'interactions' type = 'file' name = 'file'/></p>
          

        </form>
        <div class = 'bottombuttons'>
        <button class = 'interactions' type = 'submit' onClick = {doupload}>upload</button>
        <button class = {run}  onClick = {download}>download</button>
        </div>
        <div class ={infoState}>
          {info}
        </div>
        
        

    </body>
  )
}

export default App;
//{data.one.map( num => <p key = {num}>{num}</p>)}
