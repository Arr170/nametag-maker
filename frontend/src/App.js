import React, {useEffect, useState} from 'react'
import axios from 'axios'


function App() {
  const [data, setData] = useState()
  const [file, setFiles] = useState()
  const [compName, setCompName] = useState()
  const [template, setTemplate] = useState('bg_1.png')
  const templates = ['bg_1.png', 'bg_2.png']

  

  function handleCompNamdChange(event){
    setCompName(event.target.value)
    console.log(event.target.value)
  }
  
  function handleTemplateChange(){
    if(template === templates[0]){
      setTemplate(templates[1])
    }
    else{setTemplate(templates[0])}

  }

  async function testFunc () {
    const result = await axios.get('/test')
    console.log(result.data.one)
    setData(result.data.one)
  }
  function handleFileChange (event){
    setFiles(event.target.files[0])
    console.log(event.target.files[0])
  }
  async function doupload (event) {
    event.preventDefault()
    const form1 = document.getElementById('form1')
    const formData = new FormData(form1)
    //formData.append('file', file)//adding file
    //formData.append('file', compName)//adding comp name
    //formData.append('template', template)//adding tamplate

    console.log('to upload', formData.getAll('compN'))

    axios.post('/data', formData)
    .then(res => console.log(res))
    
  }
  //console.log(data)
  return(
    <div>
        <p>Hello</p>
        <button onClick = {testFunc}>click</button>
        <p>{data}</p>
        <form id = 'form1'>
          Competition name: <input type = 'text' name = 'compN'/><br></br>
          Upload csv file: <input type = 'file' name = 'file'/><br></br>
          template: <input type = 'text' name = 'template' value = {template} readOnly/><br></br>

        </form>
        <input type = 'button' value = 'change t' onClick={handleTemplateChange}/>
        <button type = 'submit' onClick = {doupload}>upload</button>

    </div>
  )
}

export default App;
//{data.one.map( num => <p key = {num}>{num}</p>)}
