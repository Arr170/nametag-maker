import React, {useEffect, useState} from 'react'
import axios from 'axios'

function App() {
  const [data, setData] = useState()
  const [file, setFiles] = useState()

  // eslint-disable-next-line react-hooks/exhaustive-deps
  async function testFunc () {
    const result = await axios.get('/test')
    console.log(result.data.one)
    setData(result.data.one)
  }
  function handleChange (event){
    setFiles(event.target.files[0])
    console.log(event.target.files[0])
  }
  async function doupload (event) {
    event.preventDefault()
    
    //const entry = await document.getElementById("image-file").files[0]
    
    const formData = new FormData()
    
    //formData.append('file', file)
    formData.append('fuck it', 'fuck it')
    formData.append('file', file)

    console.log('to upload', formData.type)
    axios.post('/data', formData)
    .then(res => console.log(res))
    
  }
  //console.log(data)
  return(
    <div>
        <p>Hello</p>
        <button onClick = {testFunc}>click</button>
        <p>{data}</p>
        <input id="image-file" type="file" name = "file" onChange={handleChange}/>
        <button type = 'submit' onClick = {doupload}>upload</button>

    </div>
  )
}

export default App;
//{data.one.map( num => <p key = {num}>{num}</p>)}
